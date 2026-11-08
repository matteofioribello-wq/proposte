K = '<b style="color:var(--ink)">'

PASSAPAROLA = '''<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:22px">
  <div class="card" style="padding:24px 26px;height:300px;display:flex;flex-direction:column">
    <div class="num" style="font-size:44px;color:var(--ottone)">10%</div>
    <div class="disp" style="font-size:27px;margin-top:8px">Per voi, a ogni azienda</div>
    <p style="font-size:15.5px;line-height:1.5;color:var(--muted);margin-top:8px">Ogni azienda che ci presentate e che lavora con noi vi vale il 10% del suo primo lavoro, come credito da usare con noi: mesi di gestione della pubblicità, modifiche, foto. <b style="color:var(--ink)">Il credito non scade.</b></p>
  </div>
  <div style="background:var(--giallo);border-radius:10px;padding:24px 26px;height:300px;display:flex;flex-direction:column">
    <div class="num" style="font-size:44px">REGALO</div>
    <div class="disp" style="font-size:27px;margin-top:8px">Per chi presentate</div>
    <p style="font-size:15.5px;line-height:1.5;margin-top:8px">Un controllo gratuito del suo sito, fatto a mano, e il 5% di sconto sul primo lavoro, «da parte vostra». <b>Così non chiedete un favore: fate un regalo.</b></p>
  </div>
  <div class="dark" style="border-radius:10px;padding:24px 26px;height:300px;display:flex;flex-direction:column">
    <div class="num" style="font-size:44px;color:var(--giallo)">× 3</div>
    <div class="disp" style="font-size:27px;margin-top:8px;color:#fff">Se diventano tre</div>
    <p style="font-size:15.5px;line-height:1.5;color:#C9CED1;margin-top:8px">Tre aziende che lavorano con noi entro la fine del 2027: <b style="color:#fff">la manutenzione del vostro sito è gratis per due anni</b>, oltre ai crediti.</p>
  </div>
</div>
<div style="background:var(--steel);border-radius:10px;padding:16px 22px;margin-top:16px;font-size:15.5px;color:var(--muted);display:flex;gap:26px;align-items:center">
  <b class="mono" style="color:var(--ink);white-space:nowrap">UN ESEMPIO</b>
  <span>Ci presentate un ristorante che fa con noi un sito da 5.000 €: <b style="color:var(--ink)">500 € di credito per voi</b>, più di tre mesi di pubblicità gestita gratis. Basta un nome e un numero, o un messaggio a Simone.</span>
</div>'''

C = dict(
name="Outdoorsolutions", domain="outdoorsolutions.it", logo="logo-cliente.png", tally="4aBE7O",
data="9 novembre 2026", scadenza="venerdì 27 novembre",
payoff="Siti web e pubblicità per le aziende, da Lumezzane",
footleft="Proposta per Outdoorsolutions · Ideos Consulting",
h1='Vent\'anni di passaparola.<br>Adesso fate lavorare<br><span style="color:var(--giallo)">anche Google.</span>', h1size=74,
lead="Abbiamo guardato outdoorsolutions.it come lo guarda il titolare di un bar che a novembre vuole scaldare il dehors: dal telefono, da Google, con fretta. Ecco cosa abbiamo visto e cosa proponiamo.",
alert_label="Trovato in «Informazioni aziendali»", alert_title="⚠ Il telefono<br>è sbagliato",
alert_text='Il numero è scritto «+344 0945467»: manca il +39. <b style="color:#fff">Chi lo copia o lo tocca dal telefono non vi trova.</b> Si sistema in un minuto.',
found_title="Quattro cose che un cliente nota subito",
found=[("Fuori norma", "Dal telefono, nessuna porta", "La prima schermata è una foto: niente titolo, niente «chiamaci». L'icona per l'accessibilità copre il logo e l'avviso dei cookie esce dallo schermo. " + K + "Chi arriva da un annuncio se ne va.</b>"),
("Da rifare", "Nessuno conta le richieste", "Sul sito non c'è nessuno strumento di misura: né Google Analytics né il pixel di Meta. " + K + "Oggi non si sa quante richieste arrivano né da dove: la pubblicità andrebbe al buio.</b>"),
("Da rifare", "Un carrello per un dehors", "44 prodotti, da 565 a 14.500 €, con «Aggiungi al carrello». Un bar o un architetto vuole un sopralluogo e un preventivo. " + K + "Il pulsante giusto è «Chiedi un sopralluogo».</b>"),
("Da tenere", "Marchi che si vendono da soli", "Bromic, Heatscope, Favex, Manutti; noleggio operativo, assistenza 24 ore su 24, rivenditori in tutta Italia, eventi aggiornati. " + K + "La sostanza c'è: va messa davanti a chi cerca.</b>")],
why2_t="Simone lo conoscete", why2="Avete già lavorato insieme: sapete come lavora e come risponde. Nel vostro sito mettiamo la stessa cura.",
blocks_title="Quattro blocchi.<br>Si può partire anche solo dalla pubblicità",
blocks=[("A", "Il sito nuovo", "LO COSTRUIAMO NOI · UNA VOLTA", "Piccolo e fatto per le richieste: caldo, fresco, noleggio, assistenza e il catalogo con «chiedi un preventivo».", "Pagina 5 · 3.900 €"),
("B", "Le richieste in ordine", "NOI PREPARIAMO · VOI USATE", "Pagine per la pubblicità, richieste in un'unica lista, calcolatore dei riscaldatori.", "Pagina 6 · da 150 €"),
("C", "Vi diamo una mano", "NOI · OGNI MESE", "Il sito sempre a posto e, se volete, newsletter e social curati da noi.", "Pagina 7 · da 39 €/mese"),
("D", "Pubblicità Google e Meta", "NOI GESTIAMO · VOI PAGATE GLI ANNUNCI", "Annunci per chi cerca caldo d'inverno e fresco d'estate. La gestione è nostra, la carta è vostra.", "Pagina 8 · da 99 €/mese")],
advice="Se il budget è stretto, partite da B e D: la pubblicità del caldo si accende entro fine novembre, il sito arriva dopo. Riepilogo a pagina 9.",
a_title="Un sito piccolo, fatto per far chiamare",
a_feats=[("Una porta per ogni bisogno", "Scaldare il dehors, rinfrescare l'estate, noleggiare invece di comprare, l'assistenza: ognuno trova subito la sua pagina."),
("Chiedi un sopralluogo", "Al posto del carrello: un modulo breve con foto e misure dello spazio. Arriva a voi completo, pronto per il preventivo."),
("Il catalogo che vende", "I 44 prodotti con foto, prezzo «a partire da» e il pulsante per chiedere un preventivo su quel modello."),
("Pronto per la pubblicità", "Le richieste si contano dal primo giorno: sapete quanto vi costa ogni contatto e da dove arriva.")],
a_incl=["Lo stesso indirizzo: outdoorsolutions.it", "Testi e foto di oggi, riordinati", "Telefono e WhatsApp a portata di pollice", "Le vecchie pagine portano a quelle nuove", "L'aspetto lo decidiamo dopo il questionario", "Un incontro per consegnarvi sito e password"],
a_price="3.900 €", a_note="Lo spazio del sito è gratuito e senza pubblicità. Il dominio outdoorsolutions.it resta vostro, come oggi.",
b_label="Le richieste in ordine", b_title="Noi prepariamo gli strumenti, voi li usate",
b_intro="Si pagano una volta. Le pagine per la pubblicità funzionano anche col sito di oggi: si parte subito, il sito nuovo arriva quando volete.",
b_items=[("Pagine per la pubblicità", "Due pagine, una per il caldo e una per il fresco, con modulo per il sopralluogo e il conteggio delle richieste. Funzionano anche senza rifare il sito.", "900 €", "una volta · si parte subito", True),
("Le richieste in un'unica lista", "Ogni richiesta, dal sito o dagli annunci, finisce in un elenco gratuito con da dove arriva, lo stato e un promemoria per richiamare.", "400 €", "una volta · voi: 1 minuto a richiesta", True),
("Quanti riscaldatori servono?", "Il cliente inserisce metri quadri e tipo di spazio, il sito consiglia modello e quantità e vi manda la richiesta già pronta.", "450 €", "una volta"),
("Rata del noleggio operativo", "Una rata mensile indicativa per ogni soluzione, calcolata con i vostri parametri: chi non vuole comprare si fa avanti lo stesso.", "350 €", "una volta"),
("Newsletter stagionale", "La vostra lista di iscritti in ordine e un modello di mail per l'apertura di ogni stagione, da mandare in cinque minuti.", "300 €", "una volta"),
("Google Maps e recensioni", "Scheda aziendale con orari, foto e telefono giusto, più un QR per chiedere una recensione dopo ogni installazione.", "150 €", "una volta")],
c_title="Un messaggio a Simone, al resto pensiamo noi",
c_plan1=["Aggiornamenti di sicurezza e copie del sito", "Fino a un'ora al mese di piccole modifiche", "Risposta entro due giorni lavorativi", "Se qualcosa non va, ce ne accorgiamo noi"],
c_name2="Ufficio marketing", c_price2="149 €", c_more="newsletter e social curati da noi",
c_plan2=["Una novità al mese sul sito: un lavoro, un marchio, un evento", "Quattro post al mese su Instagram e Facebook", "Una newsletter a inizio di ogni stagione", "Ogni tre mesi: quante richieste e da dove"],
d_title='Il caldo d\'inverno, il fresco d\'estate: <span style="color:var(--giallo)">la pubblicità segue le stagioni</span>',
d_intro="Da ottobre a febbraio cerchiamo chi vuole scaldare il dehors, da aprile ad agosto chi vuole rinfrescarlo. A marzo e settembre si spegne: pagate solo quando serve.",
d_items=[("Avvio Google", "Account Google intestato a voi, annunci per chi cerca «riscaldatori per esterni», «nebulizzatori per dehors», «noleggio funghi riscaldanti» nella vostra zona. Richieste contate dal primo giorno.", "390 €", "una volta"),
("Avvio Meta", "Facebook e Instagram: le foto dei vostri dehors davanti a bar, ristoranti, hotel e case con giardino, con il modulo di richiesta dentro l'annuncio.", "290 €", "una volta"),
("Gestione", "Google e Meta insieme (99 € con uno solo). Ogni settimana spegniamo gli annunci che non portano richieste; ogni mese vi diciamo quante ne sono arrivate e quanto è costata ciascuna.", "149 €", "al mese, solo quando è accesa"),
("Foto e video dei lavori", "Mezza giornata su un'installazione: dehors acceso di sera, nebulizzatori d'estate. Più tre brevi video per gli annunci.", "450 €", "una volta")],
d_budget="+ 300–600 € al mese", d_platforms="Google e Meta",
combos=[("Subito la pubblicità, il sito dopo.", ["B · Pagine per la pubblicità", "D · Avvio Google e Meta", "D · Gestione, nei mesi accesi"], "1.580 €", '149 € <span style="font-size:20px">solo nei mesi di pubblicità</span>'),
("Sito nuovo, richieste in ordine, pubblicità.", ["A · Il sito nuovo", "B · Le richieste in un'unica lista", "D · Avvio Google e Meta", "C · Custode"], "4.980 €", '39 € <span style="font-size:20px">+ 149 € con la pubblicità</span>'),
("La Consigliata, più chi vende per voi.", ["Tutto della Consigliata", "B · Quanti riscaldatori servono?", "D · Foto e video dei lavori", "C · Ufficio marketing"], "5.880 €", '149 € <span style="font-size:20px">+ 149 € con la pubblicità</span>')],
extra=[("Il passaparola, ricompensato", "Vi conoscono in tanti.<br>Ogni azienda che ci presentate <span class=\"hl\">vale per voi</span>", "Vent'anni di passaparola sono il vostro punto forte. Se una delle aziende che conoscete ha bisogno di un sito o di clienti nuovi, ve lo riconosciamo così.", PASSAPAROLA, "Credito valido sul primo lavoro firmato dall'azienda presentata · non cumulabile con altri sconti")],
t_title="La pubblicità prima, il sito per la primavera",
t_intro="Il caldo si vende adesso: le pagine per la pubblicità e gli annunci partono subito. Il sito nuovo lo costruiamo in inverno, così è pronto per la stagione del fresco.",
steps=[("Pubblicità", "UNA SETTIMANA DALL'OK", "Conteggio delle richieste, pagina per il caldo, annunci Google e Meta accesi."),
("Raccolta", "ENTRO IL 27 NOVEMBRE", "Questionario, una chiacchierata di 30 minuti, foto dei lavori e testi."),
("Il sito", "DICEMBRE–GENNAIO", "Prima pagina da approvare in una settimana, poi catalogo, sopralluogo e strumenti scelti."),
("Online", "FINE GENNAIO", "Controlli e accensione. A marzo si prepara la pubblicità del fresco.")],
t_box1=("SE IL QUESTIONARIO ARRIVA ENTRO IL 27 NOVEMBRE", "Sito online entro fine gennaio 2027"),
t_box2=("LA PUBBLICITÀ DEL CALDO, DALL'OK", "Accesa in una settimana"),
)
