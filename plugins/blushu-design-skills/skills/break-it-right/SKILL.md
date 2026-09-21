---
name: break-it-right
description: Analizza, compone, implementa e verifica i ritorni a capo dei testi web in base a significato, punteggiatura e ritmo visivo. Utilizzare durante la creazione o revisione di siti, landing page, prototipi HTML e interfacce frontend quando hero, titoli, lead, card, CTA, navigazione o microcopy presentano interruzioni illogiche, parole orfane, righe sbilanciate, overflow o testi brevi che dovrebbero rimanere su una sola riga.
---

# Break It Right

## Obiettivo

Comporre intenzionalmente le righe dei testi web affinché significato, punteggiatura e ritmo visivo coincidano a ogni larghezza.

Non limitarsi ad applicare proprietà CSS. Nei profili che autorizzano modifiche, analizzare linguisticamente il testo, renderizzare la pagina, osservare il risultato reale e correggerlo fino al rispetto dei criteri di accettazione.

Non ottimizzare per ottenere il minor numero possibile di righe. Mantenere sulla stessa riga le unità sintattiche e semantiche quando entrano comodamente nello spazio disponibile. Quando il testo deve spezzarsi, scegliere il punto linguisticamente più naturale.

## Risoluzione del profilo di esecuzione

Risolvere il profilo prima di caricare riferimenti o ispezionare l'artefatto:

- **create:** produrre una nuova specifica o composizione editoriale; scrivere solo quando la richiesta lo autorizza;
- **change:** applicare una modifica richiesta entro l'ambito nominato, ma scrivere solo con un'autorizzazione separata fornita dal task;
- **review:** cercare problemi di composizione senza modificare file;
- **verify:** verificare soltanto claim o criteri di accettazione dichiarati su un lavoro concluso; restare sempre in sola lettura.

Scegliere il profilo da un token esplicito dopo il nome della skill, poi da un campo `Mode` esplicito nel handoff, poi dal linguaggio non ambiguo della richiesta; altrimenti mantenere il comportamento esistente, usando `change` solo quando la richiesta autorizza chiaramente l'implementazione. Una richiesta focalizzata non concede permesso di scrittura.

Se la richiesta corrente contiene soltanto il nome della skill e un eventuale token di profilo, senza un task recente o handoff utilizzabile, restituire soltanto il `Mode` risolto oppure `Mode: unresolved`, `Status: NEEDS_TASK`, i campi mancanti e `Mutations: none`; poi fermarsi prima di ispezionare artefatti o caricare riferimenti.

Per un handoff di workflow in `verify`, richiedere `Question`, `Scope`, `Baseline`, `Criteria`, `Authority: read-only`, `Locked Decisions`, `Invocation ID`, `Artifact Revision` e `Pass Limit: 1`. In una chiamata conversazionale diretta è possibile recuperare artefatto, domanda chiusa, ambito, baseline e criteri dal contesto immediatamente precedente solo quando una sola interpretazione è fortemente supportata.

Se non è possibile risolvere un task concreto, restituire soltanto `Mode: verify`, `Status: NEEDS_TASK`, i campi mancanti e `Mutations: none`; poi fermarsi senza caricare riferimenti condizionali, ispezionare file non pertinenti, instradare lavoro o proporre una review.

In `verify`:

1. Controllare solo i criteri dichiarati e lo stato adiacente direttamente interessato, usando il minimo di rendering, evidenze e riferimenti necessari.
2. Eseguire un solo passaggio limitato. Riprovare una singola azione strumentale solo per un errore chiaramente transitorio e sicuro.
3. Non mutare file, design, configurazione o sistemi esterni; non ampliare in un audit globale; non raccomandare o applicare correzioni; non invocare altre skill; e non eseguire handoff o `Next Task`.
4. Preservare le decisioni bloccate. Segnalare una possibile regressione adiacente solo come segnale fuori ambito non investigato.
5. Concludere con `Mode`, `Status: PASS | FAIL | BLOCKED`, `Scope` controllato, `Evidence` specifica per criterio, `Failed Criteria`, eventuali `Out-of-scope Signals`, `Owner` in caso di fallimento e `Mutations: none`. `PASS` richiede evidenza per ogni criterio; usare `BLOCKED` quando mancano font effettivo, rendering, baseline, artefatto o strumento decisivo.

Questo report terminale sostituisce la consegna ordinaria descritta sotto.

## Ambito

Applicare il controllo completo a:

- hero title e display title;
- H1, H2 e H3;
- lead e sottotitoli;
- titoli delle card;
- citazioni e callout;
- CTA;
- voci di navigazione;
- label, eyebrow, prezzi, date e microcopy.

Per i normali paragrafi, prediligere il wrapping naturale del browser. Non inserire `<br>` manuali nel body copy salvo composizioni editoriali esplicitamente richieste.

## Processo obbligatorio

Applicare il processo completo soltanto a `create` e `change` quando il task autorizza le operazioni richieste. In `review`, eseguire le fasi analitiche e di rendering sull'artefatto esistente, ma saltare ogni passo che implementa, corregge o ripete il rendering dopo una modifica. In `verify`, eseguire soltanto i controlli richiesti dal profilo limitato sopra: i criteri dichiarati prevalgono sulle verifiche globali e sull'elenco completo delle larghezze.

Per ogni testo rilevante:

1. Classificare il ruolo del testo.
2. Stabilire se il contenuto è statico o dinamico.
3. Stabilire se il copy è approvato o modificabile.
4. Scomporre la frase in unità semantiche.
5. Individuare e classificare i possibili punti di interruzione.
6. Rilevare lead, sottotitoli, callout e testi brevi statici composti da più frasi.
7. Implementare inizialmente un wrapping naturale e una misura adeguata.
8. Renderizzare con il font effettivo.
9. Confrontare le varianti obbligatorie quando il testo contiene più frasi.
10. Verificare tutte le larghezze richieste.
11. Correggere seguendo l'ordine di intervento definito in questa skill.
12. Ripetere rendering e verifica dopo ogni modifica significativa.

Non dichiarare completato il lavoro basandosi soltanto sulla lettura del codice.

## Analisi semantica

Individuare prima di tutto le parole che costituiscono un'unica unità di significato.

Mantenere insieme quando possibile:

- articolo e sostantivo: `il progetto`, `una soluzione`;
- preposizione e complemento: `per la tua azienda`, `nel cuore dell'Abruzzo`;
- ausiliare e verbo: `abbiamo realizzato`, `può trasformare`;
- aggettivo e sostantivo quando formano un'espressione unitaria;
- verbo e complemento breve quando separarli altera il ritmo;
- nome e cognome;
- numero e unità di misura;
- prezzo e valuta;
- data e parti della stessa data;
- CTA brevi: `scopri di più`, `richiedi informazioni`;
- espressioni brevi: `su misura`, `per te`, `Made in Italy`.

Non terminare una riga, quando evitabile, con:

- articolo;
- preposizione breve;
- congiunzione;
- verbo ausiliare;
- parola funzionale che dipende chiaramente da quella successiva.

## Gerarchia dei punti di interruzione

Quando un testo deve andare a capo, preferire nell'ordine:

1. dopo un punto;
2. dopo due punti o punto e virgola;
3. dopo una virgola;
4. dopo un trattino lungo;
5. tra due proposizioni complete;
6. tra due gruppi semanticamente autonomi;
7. in un punto neutro che non separi elementi dipendenti.

Utilizzare questa gerarchia come criterio di scelta, non come automatismo. Non inserire un ritorno a capo dopo ogni segno di punteggiatura.

Mantenere sempre la punteggiatura sulla riga precedente. Non separare mai una parola dalla virgola, dal punto o dagli altri segni che la seguono.

## Preferenza per la singola riga

Mantenere su una sola riga quando entrano comodamente:

- frasi brevi;
- unità semantiche brevi;
- CTA;
- voci di navigazione;
- eyebrow e label;
- prezzi;
- date;
- nomi;
- brevi titoli di card.

Considerare un testo adatto alla singola riga solo se:

- rispetta la dimensione tipografica prevista;
- conserva il padding del componente;
- non produce overflow;
- non richiede tracking eccessivamente negativo;
- rimane leggibile alla larghezza esaminata.

Non ridurre drasticamente il font, non comprimere il layout e non applicare `nowrap` a frasi lunghe soltanto per ottenere una singola riga.

## Parole e righe orfane

Nei titoli, lead, citazioni e testi brevi:

- non lasciare una sola parola nell'ultima riga;
- evitare un'ultima riga composta da due parole molto brevi;
- evitare un'ultima riga visivamente inferiore a circa il 25–30% della larghezza del blocco;
- evitare righe sproporzionate rispetto alle precedenti;
- evitare una riga composta soltanto da una parola funzionale e dalla parola successiva;
- consentire eccezioni soltanto se costituiscono una scelta editoriale intenzionale e verificata.

Valutare la silhouette complessiva del testo. Evitare scalette artificiali, righe quasi identiche seguite da una riga minima e composizioni che sembrano accidentali.

## Comportamento per tipo di contenuto

### Titoli statici

Consentire composizioni editoriali controllate tramite span o break responsive dopo verifica visiva completa.

### Copy dinamico o proveniente da CMS

Evitare break manuali codificati nel markup. Utilizzare misura, scala, wrapping naturale e contenitori flessibili. Se il progetto richiede composizione editoriale, prevedere un campo o metadato esplicito per il punto di interruzione.

### Copy approvato

Non modificare il testo. Correggere misura, layout, scala e comportamento responsive.

### Copy provvisorio

Consentire modifiche minime per eliminare orfani o interruzioni innaturali, preservando significato, tono e informazioni. Segnalare il copy modificato quando la modifica è sostanziale.

## Controllo obbligatorio dei confini tra frasi

Applicare questo controllo a lead, sottotitoli, callout e testi brevi statici contenenti due o più frasi separate da un punto.

Non limitarsi a verificare orfani, overflow, righe sbilanciate o parole funzionali isolate. Per ogni testo interessato, renderizzare e confrontare obbligatoriamente almeno queste varianti:

1. wrapping naturale senza break manuali;
2. interruzione dopo il punto a tutte le larghezze;
3. interruzione dopo il punto soltanto da tablet o desktop, lasciando il wrapping naturale su mobile.

Eseguire il confronto sul rendering reale con il font effettivamente caricato. Valutare tutte le varianti a 320, 375, 390, 768, 1024, 1280 e 1440px.

Preferire il break sulla punteggiatura quando:

- separa due frasi semanticamente autonome;
- migliora la scansione e il ritmo editoriale;
- produce righe equilibrate;
- non genera overflow o parole orfane;
- non aumenta in modo sproporzionato l'altezza del componente;
- non peggiora nessuna delle larghezze obbligatorie.

Non approvare un lead composto da più frasi senza aver provato visivamente almeno una variante che rispetti il confine sintattico dopo il punto.

Non inserire automaticamente un `<br>` dopo ogni punto. Trattare la punteggiatura come candidato editoriale prioritario e scegliere la variante migliore attraverso il confronto visivo.

Evitare che una seconda frase breve cominci accidentalmente alla fine della riga precedente lasciando il resto della frase sulla riga successiva. In questa situazione, provare prioritariamente a spostare l'intera seconda frase su una nuova riga.

Per i testi statici, se il break migliora tablet o desktop ma peggiora mobile, utilizzare un break responsive. Per i testi dinamici o provenienti da CMS, evitare break codificati nel markup e prevedere, quando necessario, un metadato editoriale che abiliti la composizione intenzionale.

Considerare il confronto tra alternative parte dell'audit. `Zero problemi rilevati` non equivale a `migliore composizione`: non limitarsi a cercare difetti, ma confrontare alternative plausibili e scegliere quella tipograficamente più efficace.

## Implementazione CSS di base

Utilizzare come base, adattandola al progetto:

```css
:where(h1, h2, h3, .display-title, .lead, .card-title) {
  text-wrap: balance;
}

:where(.body-copy, .prose p) {
  text-wrap: pretty;
}
```

Non considerare `text-wrap: balance` sufficiente: bilancia la lunghezza delle righe ma non garantisce la correttezza semantica.

Non utilizzare `word-break: break-all` sul testo editoriale. Applicare `overflow-wrap: anywhere` soltanto a URL, identificatori o stringhe dinamiche non separabili che potrebbero causare overflow.

Non impostare altezze fisse sui contenitori di testo. Consentire sempre l'espansione verticale del contenuto.

## Pattern: mantenere insieme un gruppo

Usare soltanto per gruppi brevi e dopo aver verificato l'assenza di overflow a 320px:

```html
<span class="keep-together">su misura</span>
```

```css
.keep-together {
  white-space: nowrap;
}
```

Per gruppi che devono rimanere uniti solo da tablet in su:

```html
<span class="keep-together keep-together--wide">intorno al tuo business</span>
```

```css
.keep-together {
  white-space: nowrap;
}

@media (max-width: 47.99rem) {
  .keep-together--wide {
    white-space: normal;
  }
}
```

Adattare il breakpoint al layout reale. Non assumere che `47.99rem` sia corretto per ogni progetto.

## Pattern: righe editoriali responsive

Per testi statici e composizioni intenzionali:

```html
<h1 class="hero-title">
  <span class="composed-line composed-line--wide">Esperienze autentiche,</span>
  <span class="composed-line composed-line--wide">pensate intorno a te.</span>
</h1>
```

```css
.composed-line {
  display: block;
}

@media (max-width: 47.99rem) {
  .composed-line--wide {
    display: inline;
  }
}
```

Quando gli span tornano inline, verificare che nel markup rimanga uno spazio corretto tra le frasi.

## Pattern: break solo desktop

```html
<h1 class="hero-title">
  Esperienze autentiche,<br class="desktop-break">
  pensate intorno a te.
</h1>
```

```css
@media (max-width: 47.99rem) {
  .desktop-break {
    display: none;
  }
}
```

Usare questo pattern soltanto se la frase ricomposta mantiene lo spazio corretto e il risultato mobile è stato verificato.

## Ordine di correzione

Quando una composizione non funziona, intervenire in questo ordine:

1. Rimuovere `<br>`, `nowrap` o regole ereditate che producono il problema.
2. Verificare che il testo sia linguisticamente corretto e ben segmentabile.
3. Modificare leggermente `max-inline-size` o larghezza del contenitore.
4. Correggere il copy se è provvisorio e modificabile.
5. Adattare moderatamente font-size, line-height o tracking senza compromettere la gerarchia.
6. Applicare `text-wrap: balance` o `pretty` quando appropriato.
7. Mantenere insieme una breve unità semantica.
8. Inserire righe editoriali o un break responsive come ultima soluzione.
9. Renderizzare nuovamente tutti i breakpoint.

Provare sia ad allargare sia a restringere leggermente il blocco: allargare può recuperare una parola orfana; restringere può spostare un'intera unità logica sulla riga successiva.

## Verifica visiva obbligatoria

Controllare almeno:

- 320px;
- 375px;
- 390px;
- 768px;
- 1024px;
- 1280px;
- 1440px.

Verificare inoltre:

- font principale caricato;
- font fallback attivo o caricamento rallentato;
- zoom browser al 200%;
- testo più lungo realistico nei componenti dinamici;
- presenza di accenti, apostrofi, numeri e simboli;
- eventuali animazioni prima e dopo il loro completamento.

Quando è disponibile un browser o uno strumento di preview, acquisire o osservare il rendering reale. Se non è possibile eseguire il controllo visivo, dichiarare esplicitamente che il wrapping non è stato verificato e non affermare che la composizione è definitiva.

## Criteri di accettazione

Non considerare completo un componente testuale finché:

- nessun titolo termina con una singola parola isolata;
- nessuna interruzione separa elementi semanticamente dipendenti quando evitabile;
- i punti di interruzione preferiscono punteggiatura e pause sintattiche;
- la punteggiatura rimane collegata alla parola precedente;
- i testi brevi rimangono su una riga quando entrano comodamente;
- CTA, prezzi, date, nomi e unità di misura non vengono separati;
- nessun `nowrap` provoca overflow;
- nessun ritorno manuale pensato per desktop rompe tablet o mobile;
- nessun testo viene tagliato, sovrapposto o nascosto;
- il risultato è stato verificato con il font effettivo;
- il risultato è stato controllato a tutte le larghezze richieste.
- ogni lead con più frasi è stato confrontato con una composizione che rispetta i confini tra le frasi;
- nessuna seconda frase breve comincia accidentalmente alla fine della riga precedente;
- la scelta tra wrapping naturale e break sulla punteggiatura è stata verificata visivamente, non dedotta soltanto dal codice;
- l'audit ha confrontato alternative plausibili anche quando la composizione iniziale non presentava problemi evidenti.

## Consegna

In `change`, implementare direttamente le correzioni autorizzate. `Review` rimane sempre in sola lettura; se il task autorizza una mutazione, risolvere il profilo come `change`. In `create`, modificare artefatti solo con autorizzazione esplicita. In `verify`, usare esclusivamente il report terminale definito nel profilo di esecuzione.

Al termine di una modifica autorizzata, riepilogare in modo conciso soltanto:

- componenti che hanno richiesto un break manuale;
- testi con più frasi confrontati e variante selezionata;
- gruppi mantenuti insieme con `nowrap`;
- copy provvisorio modificato;
- verifiche visive non eseguibili.

Non elencare ogni normale regolazione CSS.
