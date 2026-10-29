/* @ds-bundle: {"format":4,"namespace":"RockRoll","components":[{"name":"Targa"},{"name":"Plettro"},{"name":"Timbro"},{"name":"Bottone"},{"name":"Hero"},{"name":"Sezione"},{"name":"CartaAudit"},{"name":"Consiglio"},{"name":"Fasi"},{"name":"Investimento"},{"name":"ChiSiamo"},{"name":"Brief"},{"name":"PiePagina"}]} */
(function () {
  var React = window.React;
  var h = React.createElement;
  function cx() { return Array.prototype.filter.call(arguments, Boolean).join(" "); }

  var PICK = "M50 3 C80 3 97 17 97 38 C97 63 72 90 50 103 C28 90 3 63 3 38 C3 17 20 3 50 3 Z";

  function Targa(p) {
    var size = p.size || "m", variante = p.variante || "ghisa", dettagli = p.dettagli !== false;
    return h("div", { className: cx("rr-targa", "rr-targa--" + size, "rr-targa--" + variante, p.className), role: "img", "aria-label": "Rock&Roll Studio" },
      h("span", { className: "rr-targa__vite rr-targa__vite--tl" }),
      h("span", { className: "rr-targa__vite rr-targa__vite--tr" }),
      h("span", { className: "rr-targa__vite rr-targa__vite--bl" }),
      h("span", { className: "rr-targa__vite rr-targa__vite--br" }),
      dettagli ? h("div", { className: "rr-targa__riga", "aria-hidden": "true" }, h("span", null, "COSTRUZIONI DIGITALI"), h("span", null, "LUMEZZANE (BS)")) : null,
      h("div", { className: "rr-targa__nome", "aria-hidden": "true" },
        h("div", { className: "rr-targa__rr" }, "ROCK", h("span", { className: "rr-targa__amp" }, "&"), "ROLL"),
        h("div", { className: "rr-targa__studio" }, "STUDIO")),
      dettagli ? h("div", { className: "rr-targa__riga rr-targa__fondo", "aria-hidden": "true" }, h("span", null, "MOD. " + (p.anno || "2026")), h("span", null, "MATR. " + (p.matricola || "001")), h("span", null, "TOLL. ±0")) : null
    );
  }

  function Plettro(p) {
    var size = p.size || 48;
    var colore = p.colore === "ghisa" ? "var(--hero)" : "var(--giallo)";
    var foro = p.colore === "ghisa" ? "var(--giallo)" : "var(--on-giallo)";
    return h("svg", { className: cx("rr-plettro", p.className), width: size, height: Math.round(size * 1.06), viewBox: "0 0 100 106", role: p.label ? "img" : undefined, "aria-label": p.label, "aria-hidden": p.label ? undefined : "true" },
      h("path", { d: PICK, fill: colore }),
      h("circle", { cx: 50, cy: 18, r: 5, fill: p.foro || foro }),
      p.sigla === false ? null : h("text", { x: 50, y: 62, textAnchor: "middle", fontFamily: "Big Shoulders Stencil Display, sans-serif", fontWeight: 900, fontSize: 34, fill: foro }, "R&R")
    );
  }

  var TIMBRI = { "fuori-norma": "Fuori norma", "da-rifare": "Da rifare", "da-tenere": "Da tenere", "collaudato": "Collaudato" };
  var TILT = { "fuori-norma": "-4deg", "da-rifare": "3deg", "da-tenere": "-2deg", "collaudato": "4deg" };
  function Timbro(p) {
    var tipo = p.tipo || "fuori-norma";
    var style = { "--rr-tilt": p.inclinazione != null ? p.inclinazione + "deg" : TILT[tipo] };
    return h("span", { className: cx("rr-timbro", "rr-timbro--" + tipo, p.className), style: style }, p.children || TIMBRI[tipo]);
  }

  function Bottone(p) {
    var variante = p.variante || "primario";
    var cls = cx("rr-btn", "rr-btn--" + variante, p.className);
    if (p.href) return h("a", { className: cls, href: p.href, target: p.target, rel: p.target === "_blank" ? "noopener" : undefined }, p.children);
    return h("button", { type: p.type || "button", className: cls, onClick: p.onClick }, p.children);
  }

  function Hero(p) {
    var capitoli = p.capitoli || ["01 · Collaudo", "02 · Direzione", "03 · Investimento", "04 · Brief"];
    return h("header", { className: cx("rr-hero", p.className) },
      p.ampersand ? h("div", { className: "rr-hero__amp", "aria-hidden": "true" }, "&") : null,
      h("div", { className: "rr-wrap rr-hero__in" },
        h("div", { className: "rr-hero__barra" },
          h("div", { className: "rr-hero__marchi" },
            h(Targa, { size: "s", dettagli: false }),
            p.cliente || p.logoCliente ? h("span", { className: "rr-hero__per", "aria-hidden": "true" }, "×") : null,
            p.logoCliente ? h("img", { className: "rr-hero__cliente", src: p.logoCliente, alt: p.cliente || "Logo cliente" })
              : (p.cliente ? h("span", { className: "rr-hero__cliente-testo" }, p.cliente) : null)),
          p.occhiello ? h("div", { className: "rr-hero__occhiello" }, p.occhiello) : null),
        h("div", { className: "rr-hero__testo" },
          h("h1", { className: "rr-hero__titolo" }, p.titolo, p.evidenza ? " " : null, p.evidenza ? h("span", { className: "rr-hero__evidenza" }, p.evidenza) : null),
          p.sottotitolo ? h("p", { className: "rr-hero__sotto" }, p.sottotitolo) : null,
          capitoli.length ? h("nav", { className: "rr-hero__capitoli", "aria-label": "Capitoli" }, capitoli.map(function (c, i) {
            var item = typeof c === "string" ? { testo: c } : c;
            return h(item.href ? "a" : "span", { key: i, href: item.href, className: cx("rr-chip", (item.attivo || (!item.href && i === capitoli.length - 1 && p.evidenziaUltimo !== false)) && "rr-chip--attivo") }, item.testo);
          })) : null)),
      h("div", { className: "rr-strisce", "aria-hidden": "true" })
    );
  }

  function Sezione(p) {
    return h("section", { id: p.id, className: cx("rr-sezione", p.tono === "acciaio" && "rr-sezione--acciaio", p.className) },
      h("div", { className: "rr-wrap" },
        p.occhiello || p.titolo ? h("div", { className: "rr-sezione__testa" },
          p.occhiello ? h("div", { className: "rr-label" }, p.occhiello) : null,
          p.titolo ? h("h2", { className: "rr-sezione__titolo" }, p.titolo) : null,
          p.intro ? h("p", { className: "rr-sezione__intro" }, p.intro) : null) : null,
        p.children));
  }

  function CartaAudit(p) {
    return h("article", { className: cx("rr-carta", p.className) },
      h(Timbro, { tipo: p.timbro || "da-rifare" }),
      h("h3", { className: "rr-carta__titolo" }, p.titolo),
      h("p", { className: "rr-carta__testo" }, p.testo),
      p.direzione ? h("div", { className: "rr-carta__direzione" }, h("b", null, "Direzione: "), p.direzione) : null,
      p.children);
  }

  function Consiglio(p) {
    return h("aside", { className: cx("rr-consiglio", p.className) },
      h(Plettro, { size: 72, colore: "ghisa" }),
      h("div", { className: "rr-consiglio__corpo" },
        h("div", { className: "rr-consiglio__occhiello" }, p.occhiello || "Il nostro consiglio"),
        p.titolo ? h("h3", { className: "rr-consiglio__titolo" }, p.titolo) : null,
        h("div", { className: "rr-consiglio__testo" }, p.children),
        p.firma === null ? null : h("div", { className: "rr-consiglio__firma" }, p.firma || "Matteo & Simone")));
  }

  var FASI = [
    { titolo: "Collaudo", testo: "Audit del sito e brief con voi." },
    { titolo: "Progetto", testo: "Struttura, testi e grafica da approvare." },
    { titolo: "Officina", testo: "Sviluppo, contenuti e lingue." },
    { titolo: "Consegna", testo: "Messa online, formazione, assistenza." }
  ];
  function Fasi(p) {
    var fasi = p.fasi || FASI;
    return h("ol", { className: cx("rr-fasi", p.className), style: { margin: 0, padding: 0, listStyle: "none" } },
      fasi.map(function (f, i) {
        return h("li", { key: i, className: "rr-fase" },
          h("div", { className: "rr-fase__n", "aria-hidden": "true" }, String(i + 1).padStart(2, "0")),
          h("div", { className: "rr-fase__titolo" }, f.titolo),
          h("div", { className: "rr-fase__testo" }, f.testo),
          f.quando ? h("div", { className: "rr-fase__quando" }, f.quando) : null);
      }));
  }

  function Investimento(p) {
    var righe = p.righe || [];
    var colMercato = righe.some(function (r) { return r.mercato; });
    return h("div", { className: p.className },
      h("div", { className: "rr-invest" },
        h("table", null,
          h("thead", null, h("tr", null,
            h("th", { scope: "col" }, "Voce"), h("th", { scope: "col" }, "Cosa comprende"), h("th", { scope: "col" }, p.etichettaPrezzo || "Investimento"),
            colMercato ? h("th", { scope: "col" }, "Sul mercato") : null)),
          h("tbody", null,
            righe.map(function (r, i) {
              return h("tr", { key: i, className: r.extra ? "rr-invest__extra" : undefined },
                h("td", null, h("div", { className: "rr-invest__voce" }, r.voce), r.extra ? h("div", { className: "rr-invest__mercato" }, "Opzionale") : null),
                h("td", { className: "rr-invest__desc" }, r.descrizione),
                h("td", { className: "rr-invest__prezzo" }, r.prezzo),
                colMercato ? h("td", { className: "rr-invest__mercato" }, r.mercato || "") : null);
            }),
            p.totale ? h("tr", { className: "rr-invest__totale" },
              h("td", null, h("div", { className: "rr-invest__voce" }, p.totale.voce || "Totale")),
              h("td", null, p.totale.descrizione || ""),
              h("td", { className: "rr-invest__prezzo" }, p.totale.prezzo),
              colMercato ? h("td", { className: "rr-invest__mercato" }, p.totale.mercato || "") : null) : null))),
      p.impegno === null ? null : h("div", { className: "rr-impegno" },
        h(Timbro, { tipo: "collaudato", inclinazione: 0 }, "Promessa"),
        h("div", null,
          h("h4", { className: "rr-impegno__titolo" }, (p.impegno && p.impegno.titolo) || "Il nostro impegno sul prezzo"),
          h("p", { className: "rr-impegno__testo" }, (p.impegno && p.impegno.testo) || "Stiamo nella fascia bassa del mercato perché lavoriamo senza costi di struttura. Se dopo il brief qualcosa costa meno del previsto, lo togliamo dal preventivo."))),
      h("div", { className: "rr-nota" }, p.nota || "Prezzi IVA esclusa."));
  }

  function ChiSiamo(p) {
    var persone = p.persone || [];
    return h("div", { className: cx("rr-team", p.className) }, persone.map(function (x, i) {
      var iniziali = (x.nome || "").split(" ").map(function (s) { return s.charAt(0); }).join("").slice(0, 2);
      return h("article", { key: i, className: "rr-persona" },
        h("div", { className: "rr-persona__testa" },
          x.foto ? h("img", { className: "rr-persona__foto", src: x.foto, alt: x.nome }) : h("div", { className: "rr-persona__foto rr-persona__foto--vuota", "aria-hidden": "true" }, iniziali),
          h("div", null, h("h3", { className: "rr-persona__nome" }, x.nome), h("div", { className: "rr-persona__ruolo" }, x.ruolo))),
        x.testo ? h("p", { className: "rr-persona__testo" }, x.testo) : null,
        x.competenze && x.competenze.length ? h("div", { className: "rr-persona__skill" }, x.competenze.map(function (c, j) { return h("span", { key: j, className: "rr-skill" }, c); })) : null);
    }));
  }

  function Brief(p) {
    var domande = p.domande || [];
    return h("div", { className: cx("rr-brief", p.className) },
      h("div", { className: "rr-label", style: { color: "var(--on-hero-muted)" } }, p.occhiello || "Il brief"),
      h("h3", { className: "rr-brief__titolo" }, p.titolo || "Dieci domande, dieci minuti."),
      p.testo ? h("p", { className: "rr-brief__testo" }, p.testo) : null,
      domande.length ? h("ol", null, domande.map(function (d, i) { return h("li", { key: i }, h("span", null, d)); })) : null,
      h("div", { className: "rr-brief__azioni" },
        h(Bottone, { href: p.href, target: "_blank" }, p.cta || "Compila il brief"),
        p.tempi ? h("span", { className: "rr-brief__tempo" }, p.tempi) : null));
  }

  function PiePagina(p) {
    return h("footer", { className: cx("rr-piede", p.className) },
      h("div", { className: "rr-wrap rr-piede__in" },
        h("div", { className: "rr-piede__marchio" }, h(Plettro, { size: 28, sigla: false, foro: "var(--hero)" }), h("span", null, "ROCK&ROLL STUDIO · SITI WEB RICAVATI DAL PIENO")),
        p.email ? h("span", { className: "rr-piede__email" }, p.email) : null,
        h("span", null, p.nota || ("Prezzi IVA esclusa · validità " + (p.validita || "30 giorni")))));
  }

  var api = { Targa: Targa, Plettro: Plettro, Timbro: Timbro, Bottone: Bottone, Hero: Hero, Sezione: Sezione, CartaAudit: CartaAudit, Consiglio: Consiglio, Fasi: Fasi, Investimento: Investimento, ChiSiamo: ChiSiamo, Brief: Brief, PiePagina: PiePagina };
  window.RockRoll = window.RockRoll || {};
  Object.assign(window.RockRoll, api);
})();
