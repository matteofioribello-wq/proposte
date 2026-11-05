# Presentazione PDF per i clienti

Ogni cliente riceve un PDF 16:9 (9 pagine) con i link al brief su Tally e all'analisi completa. Stesso schema della proposta I.GO, grafica Rock&Roll.

## Regola

Niente demo, mockup o screenshot del sito nuovo prima del brief: la grafica si sceglie insieme dopo (brief → call di 45 minuti → home in una settimana). Gli screenshot del sito di oggi, per il collaudo, vanno bene.

## Pagine

1. Copertina con logo del cliente e la battuta
2. In sintesi: calendario in tre date, prezzo, pulsanti Brief e Analisi
3. Cosa abbiamo trovato (timbri Fuori norma, Da rifare, Da tenere)
4. Cosa proponiamo
5. La grafica la scegliamo insieme, dopo il brief
6. Risultati misurabili dal lancio
7. Tempi e fasi
8. Investimento voce per voce
9. Prossimo passo: Brief e Analisi

## Nuovo cliente

1. Copia `gnali/` in `<cliente>/`, sostituisci `logo-cliente.png` e i testi in `deck.html`.
2. Genera il PDF con Chrome (dalla cartella del cliente):

```
"C:/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu --no-pdf-header-footer --allow-file-access-from-files --virtual-time-budget=5000 --print-to-pdf=proposta.pdf deck.html
```

3. Niente `box-shadow` né filtri: su iPhone il PDF si rompe.
4. Copia il PDF in `public/<cliente>/` e linkalo dalla pagina di sintesi.
