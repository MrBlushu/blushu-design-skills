# Content and layout

Use this reference to establish functional hierarchy, manage disclosure, choose list/detail behavior, present collections, and transform the interaction across viewport sizes.

## Contents

- [Establish hierarchy](#establish-hierarchy)
- [Disclosure patterns](#disclosure-patterns)
- [List and detail patterns](#list-and-detail-patterns)
- [Collection patterns](#collection-patterns)
- [Transform for smaller surfaces](#transform-for-smaller-surfaces)

## Establish hierarchy

Rank content by task role rather than visual taste:

1. primary object or outcome;
2. action needed to advance the task;
3. context needed to decide safely;
4. supporting metadata and secondary actions;
5. optional explanation or decoration.

Define what remains visible during loading, error, empty, selection, and editing states. A layout is incomplete if it only describes populated rest state.

### Visual framework

- **Problem/context:** give related screens a stable spatial grammar for identity, navigation, work area, and actions.
- **Fit:** users move repeatedly across a product; persistent regions or alignments reduce reorientation.
- **Avoid:** forcing different tasks into identical shells or reserving large empty regions for consistency alone.
- **System effects:** assign content regions; retain shell state deliberately; stabilize global/local navigation; keep status and action feedback in predictable places.
- **Variants:** responsive shell, role-specific regions, or focus mode.
- **Dependencies:** layout primitives, route hierarchy, tokens, and persistent state boundaries.
- **Verify:** repeated regions behave consistently, task focus remains dominant, responsive changes preserve relationships, and all states fit without overlap.

### Center stage

- **Problem/context:** make one object, visualization, or creation surface the clear center of work.
- **Fit:** the primary task depends on sustained attention; supporting tools can remain peripheral or contextual.
- **Avoid:** several peer objects require comparison, the focal object is tiny, or hidden tools become hard to discover.
- **System effects:** allocate most space to primary content; retain tool state outside it; keep navigation subordinate; show feedback near the affected object.
- **Variants:** canvas with inspectors, document with toolbar, or media viewer.
- **Dependencies:** scalable work area and controlled panel behavior.
- **Verify:** users identify the primary object immediately, key tools remain reachable, focus survives panel changes, and small viewports still support completion.

### Grid of equals

- **Problem/context:** present peer items for scanning, recognition, and selection without implying a false ranking.
- **Fit:** items have comparable structure; visual or short-text recognition matters; order is secondary or explicitly sortable.
- **Avoid:** dense comparison across many attributes, strong hierarchy, or items too irregular for stable cells.
- **System effects:** normalize card content; persist selection and sort; navigation opens or acts on an item; feedback belongs to the affected cell and collection.
- **Variants:** fixed/adaptive grid, selectable tiles, or virtualized grid.
- **Dependencies:** item identity, responsive sizing, and keyboard navigation model.
- **Verify:** reading order is clear, keyboard and touch reach every item, selection survives reflow, and unequal content does not break scanning.

## Disclosure patterns

### Module tabs

- **Problem/context:** switch among a small number of peer content modules within one stable object or place.
- **Fit:** modules are mutually exclusive, labels are concise, and switching is frequent enough to justify persistent choices.
- **Avoid:** sequential steps, deep hierarchy, too many or volatile labels, or content that must be compared simultaneously.
- **System effects:** partition peer content; retain shared and per-tab state; provide local navigation; expose active, loading, error, and changed status.
- **Variants:** fixed, scrollable, or responsive menu fallback.
- **Dependencies:** stable module identity, focus behavior, routing decision, and state retention policy.
- **Verify:** active tab is programmatically clear, keyboard movement works, direct links restore the right module, and switching does not lose edits silently.

### Accordion

- **Problem/context:** scan headings and selectively reveal several sections in a long vertical surface.
- **Fit:** section titles predict content; users need a subset; multiple sections may remain open for comparison.
- **Avoid:** primary content must stay visible, sections depend on hidden context, or expansion causes disruptive jumps.
- **System effects:** defer section bodies; store expansion state when useful; keep navigation in-page; announce expanded/collapsed and loading states.
- **Variants:** single-open or multi-open; nested use only with strong hierarchy.
- **Dependencies:** semantic controls and stable anchors.
- **Verify:** headings remain scannable, expansion preserves focus and location, state is conveyed without icons alone, and deep links reveal their target.

### Collapsible panels

- **Problem/context:** let users reclaim space from supporting tools or secondary content around a primary work area.
- **Fit:** panel usefulness varies by task; users can understand the hidden region from its control; the main area benefits materially.
- **Avoid:** collapsing required context, hiding primary navigation unexpectedly, or creating many independent mystery panels.
- **System effects:** resize or reflow content; persist user preference when appropriate; keep reveal control stable; signal hidden errors or activity.
- **Variants:** drawer, inspector, sidebar, or disclosure region.
- **Dependencies:** resize rules, focus transfer, persistence, and responsive fallback.
- **Verify:** users can restore the panel, primary work reflows safely, hidden state remains discoverable, and keyboard/focus order follows the visible layout.

## List and detail patterns

### Split view

- **Problem/context:** browse a collection while keeping selected detail visible and rapidly switching items.
- **Fit:** repeated comparison or triage; adequate width; list context matters during detail work.
- **Avoid:** narrow surfaces, detail needs full width, collection and detail have unrelated lifetimes, or selection is rare.
- **System effects:** show list and detail together; share selection and filters; keep navigation local; coordinate list, detail, empty, loading, and error feedback.
- **Variants:** resizable panes, three-pane hierarchy, or responsive drilldown.
- **Dependencies:** shared selection, independent scroll, and deep-link policy.
- **Verify:** selection and scroll survive updates, detail matches the highlighted item, keyboard traversal is coherent, and narrow layouts transform deliberately.

### Drilldown

- **Problem/context:** move from a collection to a full-surface detail when space or task focus favors one level at a time.
- **Fit:** detail is substantial; mobile/narrow viewport; users can return predictably to the collection context.
- **Avoid:** rapid item comparison, frequent cross-reference, or a return that reconstructs expensive list state.
- **System effects:** replace collection content with detail; preserve list query/position/selection; push a navigable place; show transition and return status.
- **Variants:** route push, stacked navigation, or responsive counterpart to split view.
- **Dependencies:** restorable list state and stable item routes.
- **Verify:** Back restores exact collection context, direct detail entry has a safe exit, edits survive navigation as intended, and stale/deleted items recover clearly.

### Inlay

- **Problem/context:** reveal limited detail inside a list or flow without leaving the surrounding context.
- **Fit:** detail is compact; users inspect a few items; local comparison benefits from proximity.
- **Avoid:** complex editing, large media, many simultaneous expansions, or expansion destabilizes location.
- **System effects:** insert detail near its source; bind state to item identity; keep global navigation unchanged; show expansion, loading, and inline errors locally.
- **Variants:** expandable row, preview card, or inline editor.
- **Dependencies:** stable heights/anchors, focus handling, and virtualization compatibility.
- **Verify:** expansion opens the correct item, position remains stable, only intended state persists, and virtualization or filtering cannot attach detail to the wrong row.

## Collection patterns

### Cards, grids, and carousel

- **Problem/context:** choose a collection presentation based on recognition, comparison, order, and available space.
- **Fit:** cards for heterogeneous summaries and actions; grids for visual peers; carousel only for a short ordered subset with intentional lateral browsing.
- **Avoid:** cards when dense rows compare better; grids for irregular detail; carousel for essential items users may never discover.
- **System effects:** define summary content; preserve collection state; set item/open/paging navigation; expose selection, overflow, loading, and boundaries.
- **Variants:** responsive list-grid switch, selectable cards, or scroll snap.
- **Dependencies:** stable identity, ordering, focus movement, and touch/keyboard parity.
- **Verify:** users can scan and reach all items, hidden overflow is evident, reflow preserves selection, and essential content is never reachable only by gesture.

### Pagination and infinite list

- **Problem/context:** navigate a collection too large or costly to load as one surface.
- **Fit:** pagination for stable pages, known position, sharing, and bounded retrieval; infinite loading for continuous exploration where exact position matters less.
- **Avoid:** infinite loading for goal-directed lookup, footer access, or fragile restoration; pagination when page boundaries have no user meaning and interrupt scanning.
- **System effects:** chunk content; persist query, position, and loaded range; expose page/load-more navigation; show loading, end, retry, empty, and changed-data feedback.
- **Variants:** numbered pages, load more, or windowed feed.
- **Dependencies:** cursor/page API, deduplication, restoration, and virtualization strategy.
- **Verify:** no duplicates or gaps, refresh and Back restore useful position, keyboard users reach newly loaded content, failures retry in place, and the end is explicit.

## Transform for smaller surfaces

Do not scale a desktop arrangement mechanically. Re-evaluate:

- dominant task and minimum context required to perform it;
- which simultaneous regions become a sequence, drilldown, sheet, or collapsible surface;
- whether hover, right-click, drag, or dense keyboard shortcuts need visible equivalents;
- touch target, reach, virtual keyboard, safe area, and interrupted session behavior;
- preservation of selection, drafts, filters, and return position across transformed views;
- whether large data tables need prioritization, summary/detail, horizontal handling, or alternate tasks;
- loading and error placement when the initiating content is no longer visible.

Verify at representative widths and with real content extremes. Equivalent capability means completing the same user task safely, not reproducing every desktop region at once.
