Rock&Roll Studio è uno studio web di Lumezzane (BS), di Matteo Fioribello e Simone Giori, per le PMI B2B del distretto: metalmeccanica, rubinetteria, valvolame, minuteria. L'identità è **La Targa**: la targhetta metallica delle macchine d'officina diventa il logo. Heavy metal nel senso letterale. La & gigante viene dalla direzione «Poster da concerto» ed è l'unico elemento pop.

Payoff: **Siti web ricavati dal pieno.**

## Come parliamo

Irriverenti con i siti, mai con le persone. Chi legge è un titolare concreto, spesso sopra i cinquanta, poco digitale e molto attento ai conti.

- Una battuta per pagina, non di più. Di solito sta nel titolo della hero.
- Gergo d'officina, non da startup: «collaudo», «fuori norma», «ricavato dal pieno», «tolleranza», «officina». Mai «funnel», «user journey», «brand awareness», «growth hacking».
- Prendiamo in giro il sito vecchio, mai chi l'ha fatto e mai il cliente. Se il sito è recente, si propone come integrarlo e non si critica.
- Numeri e prezzi sempre chiari: il rock sta nel tono, non nei conti.
- Diamo del voi all'azienda e parliamo come «noi» (Matteo & Simone).
- Niente emoji, niente punti esclamativi, niente superlativi («il migliore», «rivoluzionario»).
- Titoli in maiuscolo condensato, testi in tono normale. Frasi brevi.

Esempi veri:

| Dove | Così |
| --- | --- |
| Payoff | Siti web ricavati dal pieno. |
| Titolo hero | Quasi cinquant'anni di raccordi a tenuta. Il sito, invece, perde. |
| Homepage | Il vostro sito ha quindici anni di servizio. Diamogli la pensione che si merita. |
| Audit | Collaudo del sito: tre pezzi fuori norma, uno da rifare da zero. |
| Oggetto mail | Preventivo pronto. Tolleranza sui tempi: zero. |
| Promessa | Stiamo nella fascia bassa del mercato perché lavoriamo senza costi di struttura. |

## Colori

- `surface` è il fondo di ogni pagina, `surface-raised` per card e tabelle, `surface-steel` per alternare le sezioni. Si separano con il colore, non con le ombre.
- `hero` (ghisa) è il fondo della hero e del piè di pagina in entrambi i temi; sopra si usano `on-hero` e `on-hero-muted`.
- `giallo` è un segnale, non uno sfondo: la & del logo, il timbro Fuori norma, il bottone principale, il box Il nostro consiglio, la fascia a strisce. Sopra il giallo si usa sempre `on-giallo`. Mai testo giallo su fondo chiaro.
- `ottone` è l'omaggio al distretto: la & del logo su fondo chiaro, la targa in ottone, il timbro Da tenere. Per il testo color ottone si usa `ottone-ink`.
- `acciaio` solo per la scritta STUDIO e le superfici metalliche.
- Testo: `ink` su tutte le surface, `ink-muted` per etichette e secondario. Entrambi superano 4.5:1 su ogni surface in tutti e due i temi.
- Focus da tastiera: `focus`, 2px pieno con 2px di stacco.

## Caratteri

- `display` (Big Shoulders Display 800–900, maiuscolo) per titoli, voci di tabella e bottoni. Stili `display-xl`, `display-l`, `display-m`, `heading`.
- `stencil` (Big Shoulders Stencil) solo per timbri, numeri grandi e la sigla R&R. Stili `stamp`, `numeral`.
- `sans` (Archivo) per tutto il testo da leggere. Stili `body-l`, `body`, `body-s`.
- `mono` (IBM Plex Mono) per occhielli, prezzi, date, matricole. Stili `label` (maiuscolo, spaziato) e `data`.
- Mai più di tre famiglie nella stessa schermata (display, sans, mono). Lo stencil conta come display.

## Forme, spazi, superfici

- Spazi dalla scala `space-1` … `space-8`. Tra sezioni `space-8`; padding delle card `space-5`; margini laterali minimi `space-4`. Contenuto largo al massimo 1240 px.
- Angoli: `radius-sm` per chip, timbri e bottoni; `radius-md` per card e box; `radius-lg` solo per la targa.
- Nessuna ombra tranne `shadow-plate` sotto la targa. Texture ammesse: la spazzolatura della ghisa e dell'ottone, la fascia a strisce di cantiere, la carta millimetrata nei disegni tecnici.
- Foto: prodotti e reparti reali del cliente, luce naturale, nessuna foto stock di strette di mano o di persone al computer.
- Le pagine vanno lette prima da telefono: tutto si impila sotto i 640 px.

## Logo

Il gruppo **Loghi** contiene gli SVG vettoriali (testi già convertiti in tracciati) e **Loghi-PNG** le stesse versioni a doppia risoluzione.

- `rr-targa-ghisa.svg` è il logo principale. `rr-targa-ottone.svg` è per le occasioni speciali.
- `rr-wordmark-su-chiaro.svg` e `rr-wordmark-su-scuro.svg`: la versione orizzontale per intestazioni, firme e documenti.
- `rr-plettro.svg` è l'icona: plettro e medaglietta insieme. `rr-avatar.svg` per i profili social, `rr-favicon.svg` per il sito.
- `rr-sigla.svg` è la sigla stencil R&R, per timbri e firme brevi.
- `rr-ampersand.svg` è la & gigante: si usa come elemento grafico, tagliata dal bordo, mai insieme alla targa grande.
- La targa non si ricolora, non si inclina e non perde le viti. Spazio libero attorno pari all'altezza della scritta STUDIO.

## Icone

Il sistema non ha un set di icone proprio: l'unica icona di marca è il plettro. Quando serve un'icona funzionale (freccia, download, telefono) usa icone a tratto da 2px nel colore del testo, mai emoji.

## La pagina-proposta

Ogni proposta dello studio è una pagina web a scorrimento costruita con questi componenti, in quest'ordine:

1. `Hero` con il logo ufficiale del cliente e la battuta nel titolo.
2. `Sezione` «In sintesi» con 3 `CartaAudit` e un `Consiglio`.
3. Situazione di partenza, audit, esperienza d'acquisto, Google: ogni sezione si chiude con un `Consiglio` dove serve una direzione.
4. Cosa proponiamo (mockup).
5. `Fasi` e tempi.
6. `Investimento` con forchette e promessa sul prezzo.
7. `ChiSiamo` con Matteo e Simone.
8. `Brief` con il pulsante verso Tally.
9. `PiePagina`.

Il form del brief su Tally usa lo stesso tema: fondo `surface`, testo `ink`, pulsante `giallo` con testo `on-giallo`, font Archivo. Il logo nel form va come immagine sotto il titolo (`rr-wordmark-su-chiaro.png`), perché Tally ritaglia a quadrato il logo d'intestazione.
