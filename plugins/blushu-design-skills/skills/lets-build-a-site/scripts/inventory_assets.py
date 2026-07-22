#!/usr/bin/env python3
"""Inventory likely website assets without project dependencies."""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import struct
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CATEGORIES = {
    "image": {".avif", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".svg", ".webp"},
    "video": {".avi", ".m4v", ".mov", ".mp4", ".webm"},
    "audio": {".flac", ".m4a", ".mp3", ".ogg", ".wav"},
    "font": {".eot", ".otf", ".ttf", ".woff", ".woff2"},
    "document": {".csv", ".doc", ".docx", ".md", ".pdf", ".ppt", ".pptx", ".rtf", ".txt", ".xls", ".xlsx"},
    "data": {".json", ".toml", ".yaml", ".yml"},
}
EXTENSION_CATEGORY = {extension: category for category, extensions in CATEGORIES.items() for extension in extensions}
DEFAULT_IGNORES = {
    ".git",
    ".next",
    ".site-work",
    ".skill-work",
    ".venv",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "vendor",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Project or asset directory to scan")
    parser.add_argument("--output", type=Path, help="Write JSON to this path instead of stdout")
    parser.add_argument("--all-files", action="store_true", help="Include extensions outside known asset categories")
    parser.add_argument("--include-hidden", action="store_true", help="Include hidden files and directories except explicit ignores")
    parser.add_argument("--ignore", action="append", default=[], metavar="NAME", help="Additional directory basename to ignore; repeatable")
    return parser.parse_args()


def png_size(file_path: Path) -> tuple[int, int] | None:
    with file_path.open("rb") as handle:
        header = handle.read(24)
    if len(header) >= 24 and header.startswith(b"\x89PNG\r\n\x1a\n"):
        return struct.unpack(">II", header[16:24])
    return None


def gif_size(file_path: Path) -> tuple[int, int] | None:
    with file_path.open("rb") as handle:
        header = handle.read(10)
    if len(header) == 10 and header[:6] in {b"GIF87a", b"GIF89a"}:
        return struct.unpack("<HH", header[6:10])
    return None


def jpeg_size(file_path: Path) -> tuple[int, int] | None:
    with file_path.open("rb") as handle:
        if handle.read(2) != b"\xff\xd8":
            return None
        while True:
            marker_start = handle.read(1)
            if not marker_start:
                return None
            if marker_start != b"\xff":
                continue
            marker = handle.read(1)
            while marker == b"\xff":
                marker = handle.read(1)
            if marker in {b"\xd8", b"\xd9"}:
                continue
            length_bytes = handle.read(2)
            if len(length_bytes) != 2:
                return None
            segment_length = struct.unpack(">H", length_bytes)[0]
            if segment_length < 2:
                return None
            if marker and marker[0] in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
                segment = handle.read(5)
                if len(segment) != 5:
                    return None
                height, width = struct.unpack(">HH", segment[1:5])
                return width, height
            handle.seek(segment_length - 2, os.SEEK_CUR)


def image_size(file_path: Path, extension: str) -> tuple[int, int] | None:
    if extension == ".png":
        return png_size(file_path)
    if extension == ".gif":
        return gif_size(file_path)
    if extension in {".jpg", ".jpeg"}:
        return jpeg_size(file_path)
    return None


def should_skip_name(name: str, include_hidden: bool) -> bool:
    return not include_hidden and name.startswith(".")


def collect(
    root: Path, args: argparse.Namespace, output_path: Path | None
) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    entries: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    ignored = DEFAULT_IGNORES | set(args.ignore)

    for current_root, directories, files in os.walk(root, followlinks=False):
        directories[:] = sorted(
            directory
            for directory in directories
            if directory not in ignored and not should_skip_name(directory, args.include_hidden)
        )
        for filename in sorted(files):
            if should_skip_name(filename, args.include_hidden):
                continue
            file_path = Path(current_root) / filename
            if file_path.is_symlink():
                continue
            if output_path and file_path.resolve() == output_path:
                continue
            extension = file_path.suffix.lower()
            category = EXTENSION_CATEGORY.get(extension)
            if not category and not args.all_files:
                continue
            try:
                metadata = file_path.stat()
                width_height = image_size(file_path, extension) if category == "image" else None
                entry: dict[str, Any] = {
                    "path": file_path.relative_to(root).as_posix(),
                    "category": category or "other",
                    "extension": extension,
                    "media_type": mimetypes.guess_type(file_path.name)[0],
                    "bytes": metadata.st_size,
                    "modified_utc": datetime.fromtimestamp(metadata.st_mtime, timezone.utc).isoformat(),
                }
                if width_height:
                    entry["width"] = width_height[0]
                    entry["height"] = width_height[1]
                entries.append(entry)
            except (OSError, ValueError, struct.error) as error:
                errors.append({"path": file_path.relative_to(root).as_posix(), "error": str(error)})
    return entries, errors


def payload(root: Path, entries: list[dict[str, Any]], errors: list[dict[str, str]]) -> dict[str, Any]:
    categories = Counter(entry["category"] for entry in entries)
    return {
        "schema_version": 1,
        "root": str(root),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "files": len(entries),
            "bytes": sum(entry["bytes"] for entry in entries),
            "by_category": dict(sorted(categories.items())),
            "errors": len(errors),
        },
        "entries": entries,
        "errors": errors,
    }


def main() -> int:
    args = parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 2
    output_path = args.output.expanduser().resolve() if args.output else None
    entries, errors = collect(root, args, output_path)
    report = payload(root, entries, errors)
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
