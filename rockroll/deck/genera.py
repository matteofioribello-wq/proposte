import re, sys, os
S = os.path.dirname(os.path.abspath(__file__))
HEAD = open(os.path.join(S, 'deckhead.html'), encoding='utf-8').read()
STYLE2 = open(os.path.join(S, 'deckstyle2.html'), encoding='utf-8').read()
B = '../../brand/logos/svg/'

def foot(left, n, dark=False):
    logo = 'rr-logo-compatto-su-scuro.svg' if dark else 'rr-logo-compatto-su-chiaro.svg'
    return f'<div class="foot"><div class="l"><img src="{B}{logo}" alt="">{left}</div><div>Matteo &amp; Simone · {n}</div></div>'

def svc(title, desc, price, unit, rec=False, h=230):
    tag = '<span class="tag">CONSIGLIATO</span>' if rec else ''
    return f'''<div class="svc{' rec' if rec else ''}" style="height:{h}px">
      <div style="display:flex;justify-content:space-between;align-items:center;gap:8px"><div class="tt">{title}</div>{tag}</div>
      <p>{desc}</p>
      <div class="ft"><span class="pr">{price}</span><span class="vo">{unit}</span></div>
    </div>'''

def darkcard(title, desc, price, unit):
    return f'''<div style="background:#26292C;border:1px solid #3A3F44;border-radius:10px;padding:20px;display:flex;flex-direction:column;height:300px">
      <div class="disp" style="font-size:23px;color:#fff">{title}</div>
      <p style="font-size:14px;line-height:1.45;color:#C9CED1;margin-top:8px">{desc}</p>
      <div style="margin-top:auto;border-top:1px solid #3A3F44;padding-top:10px;display:flex;justify-content:space-between;align-items:baseline"><b class="mono" style="color:var(--giallo);font-size:17px">{price}</b><span class="mono" style="font-size:11px;color:var(--onhero-m)">{unit}</span></div>
    </div>'''

def build(c):
    L = c['footleft']
    s = []
    # 1 cover
    s.append(f'''<section class="slide dark" style="padding:0">
  <div style="padding:56px 86px 0;display:flex;align-items:center;gap:22px">
    <img src="{B}rr-logo-su-scuro.svg" style="height:46px" alt="Rock ’n’ Roll Studio">
    <span style="font-family:Plex;color:var(--onhero-m);font-size:22px">×</span>
    <span style="background:#fff;border-radius:8px;padding:8px 14px;display:inline-flex"><img src="{c['logo']}" style="height:48px" alt="{c['name']}"></span>
  </div>
  <img src="{B}rr-sigla-su-scuro.svg" style="position:absolute;right:-60px;top:70px;height:760px;opacity:.10" alt="">
  <div style="padding:52px 86px 0;display:grid;grid-template-columns:1fr 420px;gap:56px;align-items:end">
    <div>
      <div class="label">Proposta · il nuovo sito {c['domain']}</div>
      <h1 style="font-size:{c.get('h1size',76)}px;margin-top:22px;color:#fff">{c['h1']}</h1>
      <p style="font-size:21px;line-height:1.5;color:#C9CED1;margin-top:26px;max-width:780px">{c['lead']}</p>
    </div>
    <div style="border:1px solid #3A3F44;border-radius:12px;padding:28px;background:#26292C">
      <div class="label nolead" style="color:var(--onhero-m)">{c['alert_label']}</div>
      <div class="disp" style="font-size:44px;color:var(--giallo);margin-top:14px;line-height:1">{c['alert_title']}</div>
      <p style="font-size:16px;line-height:1.5;color:#C9CED1;margin-top:14px">{c['alert_text']}</p>
    </div>
  </div>
  <div style="position:absolute;left:86px;bottom:66px;font-family:Plex;font-size:14px;color:var(--onhero-m);letter-spacing:.04em">ROCK ’N’ ROLL STUDIO · SITI WEB PER LE AZIENDE · MATTEO E SIMONE · PROPOSTA DEL {c.get('data','5 novembre 2026').upper()}</div>
  <div class="stripe" style="position:absolute;left:0;right:0;bottom:0"></div>
</section>''')
    # 2 found
    cards = ''
    for stamp, title, text in c['found']:
        cls = {'Da sistemare': 'st-fuori', 'Fuori norma': 'st-fuori', 'Da rifare': 'st-rifare', 'Da tenere': 'st-tenere'}[stamp]
        cards += f'''<div class="card" style="padding:20px 24px">
      <span class="stamp {cls}" style="font-size:18px">{stamp}</span>
      <div class="disp" style="font-size:27px;margin-top:12px">{title}</div>
      <p style="font-size:15px;line-height:1.5;color:var(--muted);margin-top:6px">{text}</p>
    </div>'''
    s.append(f'''<section class="slide">
  <div class="label">01 · Cosa abbiamo trovato</div>
  <h2>{c['found_title']}</h2>
  <p class="intro">Abbiamo aperto {c['domain']} dal telefono e dal computer il {c.get('data','5 novembre 2026')} e letto le pagine, senza accessi riservati.</p>
  <div style="display:grid;grid-template-columns:230px 1fr 1fr;gap:18px;margin-top:24px">
    <div style="grid-row:span 2;height:470px;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:#fff;position:relative"><img src="oggi-mobile.png" style="width:100%;height:100%;object-fit:cover;object-position:top" alt="Il sito oggi dal telefono"><div style="position:absolute;left:0;right:0;bottom:0;background:var(--hero);color:#fff;font-family:Plex;font-size:11px;padding:8px 10px">Il sito oggi, dal telefono</div></div>
    {cards}
  </div>
  {foot(L, 2)}
</section>''')
    # 3 chi siamo
    s.append(f'''<section class="slide">
  <div class="label">Chi siamo</div>
  <h2>Due persone, un solo studio.<br>E un numero di telefono che risponde.</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:26px">
    <div class="card" style="padding:26px;display:grid;grid-template-columns:120px 1fr;gap:22px">
      <img src="simone-giori.jpg" style="width:120px;height:120px;border-radius:50%;object-fit:cover;object-position:50% 30%" alt="Simone Giori">
      <div>
        <div class="disp" style="font-size:30px">Simone Giori</div>
        <div class="mono" style="font-size:12px;color:var(--muted);margin-top:4px">IL VOSTRO RIFERIMENTO</div>
        <p style="font-size:15.5px;line-height:1.5;color:var(--muted);margin-top:10px">Lumezzanese da generazioni e imprenditore: ha lavorato nelle assicurazioni e ha aperto e seguito attività in Italia e a Dubai. Conosce il distretto e le sue aziende. <b style="color:var(--ink)">È lui che passa da voi, tiene il progetto in mano dall'inizio alla fine e risponde al telefono.</b></p>
      </div>
    </div>
    <div class="card" style="padding:26px;display:grid;grid-template-columns:120px 1fr;gap:22px">
      <img src="matteo-fioribello.jpg" style="width:120px;height:120px;border-radius:50%;object-fit:cover" alt="Matteo Fioribello">
      <div>
        <div class="disp" style="font-size:30px">Matteo Fioribello</div>
        <div class="mono" style="font-size:12px;color:var(--muted);margin-top:4px">CHI COSTRUISCE IL SITO</div>
        <p style="font-size:15.5px;line-height:1.5;color:var(--muted);margin-top:10px">Product &amp; Growth Manager di iMamma, app con circa 130.000 utenti attive ogni mese: ogni giorno lavora su siti, dati, campagne e automazioni. <b style="color:var(--ink)">Costruisce siti e strumenti digitali in giorni, non in mesi,</b> e li misura dopo il lancio.</p>
      </div>
    </div>
  </div>
  <div style="display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:16px;margin-top:18px">
    <div style="background:var(--hero);color:var(--onhero);border-radius:10px;padding:20px 22px">
      <div class="disp" style="font-size:22px;color:var(--giallo)">Ci conosciamo da anni</div>
      <p style="font-size:14.5px;line-height:1.5;color:#C9CED1;margin-top:6px">Abbiamo già portato avanti insieme tanti progetti digitali. Rock ’n’ Roll Studio è il modo per farlo anche per le aziende del nostro distretto.</p>
    </div>
    <div class="card" style="padding:20px 22px">
      <div class="disp" style="font-size:22px">{c['why2_t']}</div>
      <p style="font-size:14.5px;line-height:1.5;color:var(--muted);margin-top:6px">{c['why2']}</p>
    </div>
    <div class="card" style="padding:20px 22px">
      <div class="disp" style="font-size:22px">Consigli su misura</div>
      <p style="font-size:14.5px;line-height:1.5;color:var(--muted);margin-top:6px">Niente pacchetti uguali per tutti: vi diciamo cosa serve a voi, e anche cosa non vi serve.</p>
    </div>
  </div>
  {foot(L, 3)}
</section>''')
    # 4 come è fatta
    blk = ''
    for letter, t, sub, d, pg in c['blocks']:
        border = 'border:2px solid var(--ink);' if letter == 'A' else ''
        blk += f'''<div class="card" style="{border}height:330px;display:flex;flex-direction:column">
      <div class="num" style="font-size:44px;color:var(--ottone)">{letter}</div>
      <div class="disp" style="font-size:28px;margin-top:8px">{t}</div>
      <div class="mono" style="font-size:12px;color:var(--muted);margin-top:6px">{sub}</div>
      <p style="font-size:15px;line-height:1.5;color:var(--muted);margin-top:10px">{d}</p>
      <div class="mono" style="margin-top:auto;font-size:15px;font-weight:500">{pg}</div>
    </div>'''
    s.append(f'''<section class="slide">
  <div class="label">02 · Come è fatta la proposta</div>
  <h2>{c.get('blocks_title','Quattro blocchi. Il primo serve,<br>gli altri li scegliete voi')}</h2>
  <p class="intro">Ogni blocco ha la sua pagina e il suo prezzo. Si possono aggiungere anche dopo, quando vi serve.</p>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:28px">{blk}</div>
  <div class="consiglio" style="margin-top:18px;padding:16px 28px">
    <span class="k" style="white-space:nowrap">Il nostro consiglio</span>
    <div class="t" style="font-size:21px">{c['advice']}</div>
  </div>
  {foot(L, 4)}
</section>''')
    # 5 A
    feats = ''.join(f'<div class="card" style="padding:18px 20px"><div class="disp" style="font-size:22px">{t}</div><p style="font-size:14.5px;line-height:1.45;color:var(--muted);margin-top:6px">{d}</p></div>' for t, d in c['a_feats'])
    incl = ''.join(f'<div>✓&nbsp; {x}</div>' for x in c['a_incl'])
    s.append(f'''<section class="slide">
  <div class="label">A · Il sito nuovo</div>
  <h2>{c['a_title']}</h2>
  <div style="display:grid;grid-template-columns:1fr 400px;gap:28px;margin-top:24px">
    <div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">{feats}</div>
      <div style="background:var(--steel);border-radius:10px;padding:18px 22px;margin-top:14px">
        <div class="label nolead">Compreso</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px 30px;margin-top:10px;font-size:15px">{incl}</div>
      </div>
    </div>
    <div class="dark" style="border-radius:12px;padding:28px;display:flex;flex-direction:column">
      <div class="label nolead">Il sito nuovo · una volta</div>
      <div class="num" style="font-size:56px;color:var(--giallo);margin-top:14px;white-space:nowrap">{c['a_price']}</div>
      <p style="font-size:15px;line-height:1.5;color:#C9CED1;margin-top:12px">IVA esclusa. Il prezzo fisso arriva entro due giorni lavorativi dalle vostre risposte.</p>
      <div style="display:grid;grid-template-columns:1fr auto;gap:12px;margin-top:22px;font-size:15px;border-top:1px solid #3A3F44;padding-top:16px">
        <span style="color:#C9CED1">Spazio del sito</span><b class="mono" style="color:var(--giallo)">0 €</b>
        <span style="color:#C9CED1">Dominio</span><b class="mono">già vostro</b>
      </div>
      <p style="font-size:13px;line-height:1.5;color:var(--onhero-m);margin-top:10px">{c['a_note']}</p>
      <div style="margin-top:auto;font-family:Plex;font-size:13px;color:var(--onhero-m)">Metà all'inizio · metà a sito online</div>
    </div>
  </div>
  {foot(L, 5)}
</section>''')
    # 6 B
    bcards = ''.join(svc(*x) for x in c['b_items'])
    s.append(f'''<section class="slide">
  <div class="label">B · {c['b_label']}</div>
  <h2>{c['b_title']}</h2>
  <p class="intro" style="margin-top:8px">{c['b_intro']}</p>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:20px">{bcards}</div>
  {foot('Prezzi IVA esclusa · i costi di eventuali servizi esterni ve li diciamo prima', 6)}
</section>''')
    # 7 C
    p1 = ''.join(f'<li>{x}</li>' for x in c['c_plan1'])
    p2 = ''.join(f'<li>{x}</li>' for x in c['c_plan2'])
    s.append(f'''<section class="slide">
  <div class="label">C · Vi diamo una mano, ogni mese</div>
  <h2>{c['c_title']}</h2>
  <p class="intro" style="margin-top:8px">Non solo aiuto tecnico: anche il lavoro di comunicazione che oggi non fa nessuno. Si disdice quando volete.</p>
  <div style="display:grid;grid-template-columns:1fr 1.25fr;gap:20px;margin-top:22px">
    <div class="plan card">
      <div class="lvl"><i style="background:var(--acciaio)"></i>Custode</div>
      <div style="display:flex;align-items:baseline;gap:8px;margin-top:10px"><span class="num" style="font-size:56px">39 €</span><span class="mono" style="color:var(--muted)">al mese</span></div>
      <p style="font-size:15px;color:var(--muted);margin-top:4px">Il sito sempre a posto.</p>
      <ul>{p1}</ul>
    </div>
    <div class="plan" style="background:var(--giallo)">
      <div style="display:flex;justify-content:space-between;align-items:center"><div class="lvl"><i style="background:var(--ink)"></i>{c['c_name2']}</div><span class="tag">CONSIGLIATO</span></div>
      <div style="display:flex;align-items:baseline;gap:8px;margin-top:10px"><span class="num" style="font-size:56px">{c['c_price2']}</span><span class="mono">al mese</span></div>
      <p style="font-size:15px;margin-top:4px">Tutto il Custode, più {c['c_more']}.</p>
      <ul style="display:grid;grid-template-columns:1fr 1fr;column-gap:22px">{p2}</ul>
    </div>
  </div>
  <div style="background:var(--steel);border-radius:10px;padding:14px 20px;margin-top:16px;font-size:15px;color:var(--muted)"><b style="color:var(--ink)">Senza canone:</b> le modifiche le facciamo quando ce le chiedete, a 35 € l'ora.</div>
  {foot('Prezzi IVA esclusa · si disdice con un mese di preavviso', 7)}
</section>''')
    # 8 D
    dcards = ''.join(darkcard(*x) for x in c['d_items'])
    s.append(f'''<section class="slide dark">
  <div class="label">D · Farsi conoscere</div>
  <h2 style="color:#fff">{c['d_title']}</h2>
  <p class="intro" style="margin-top:8px">{c['d_intro']}</p>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:24px">{dcards}</div>
  <div style="border:1px solid #3A3F44;border-radius:10px;padding:16px 22px;margin-top:16px;font-size:15px;color:#C9CED1;display:flex;gap:30px;align-items:center">
    <b class="mono" style="color:var(--giallo);white-space:nowrap">{c['d_budget']}</b>
    <span>È quanto va a {c['d_platforms']} per gli annunci, nei mesi di pubblicità. Lo pagate direttamente voi, con la vostra carta: noi non tocchiamo il budget.</span>
  </div>
  {foot('Prezzi IVA esclusa', 8, True)}
</section>''')
    # 9 combos
    def combo(name, color, sub, items, once, month, hl=False, tag=''):
        it = ''.join(f'<li>{x}</li>' for x in items)
        if hl:
            return f'''<div class="plan" style="background:var(--giallo)">
      <div style="display:flex;justify-content:space-between;align-items:center"><div class="lvl"><i style="background:var(--ink)"></i>{name}</div><span class="tag">{tag}</span></div>
      <p style="font-size:15px;margin-top:8px">{sub}</p><ul>{it}</ul>
      <div style="margin-top:auto;border-top:1px solid rgba(28,30,32,.25);padding-top:14px">
        <div class="mono" style="font-size:12px">UNA VOLTA</div><div class="num" style="font-size:40px">{once}</div>
        <div class="mono" style="font-size:12px;margin-top:8px">OGNI MESE</div><div class="num" style="font-size:30px">{month}</div></div></div>'''
        return f'''<div class="plan card">
      <div class="lvl"><i style="background:{color}"></i>{name}</div>
      <p style="font-size:15px;color:var(--muted);margin-top:8px">{sub}</p><ul>{it}</ul>
      <div style="margin-top:auto;border-top:1px solid var(--line);padding-top:14px">
        <div class="mono" style="font-size:12px;color:var(--muted)">UNA VOLTA</div><div class="num" style="font-size:40px">{once}</div>
        <div class="mono" style="font-size:12px;color:var(--muted);margin-top:8px">OGNI MESE</div><div class="num" style="font-size:30px">{month}</div></div></div>'''
    e, r, f = c['combos']
    s.append(f'''<section class="slide">
  <div class="label">Riepilogo</div>
  <h2>Tre combinazioni, dalla più semplice</h2>
  <div style="display:grid;grid-template-columns:1fr 1.15fr 1fr;gap:18px;margin-top:26px;align-items:stretch">
    {combo('Essenziale','var(--acciaio)',e[0],e[1],e[2],e[3])}
    {combo('Consigliata','',r[0],r[1],r[2],r[3],True,'LA NOSTRA SCELTA')}
    {combo('Completa','var(--ottone)',f[0],f[1],f[2],f[3])}
  </div>
  {foot('Prezzi IVA esclusa · validità 30 giorni · budget degli annunci a parte', 9)}
</section>''')
    # pagine extra (es. passaparola), dopo il riepilogo
    for i, (label, title, intro, inner, note) in enumerate(c.get('extra', [])):
        s.append(f'''<section class="slide">
  <div class="label">{label}</div>
  <h2>{title}</h2>
  <p class="intro" style="margin-top:8px">{intro}</p>
  {inner}
  {foot(note or L, 10 + i)}
</section>''')
    # 10 tempi
    steps = ''
    for i, (t, w, d) in enumerate(c['steps']):
        br = 'border-right:1px solid var(--line);' if i < 3 else ''
        steps += f'<div style="padding:24px;{br}"><div class="num" style="font-size:40px;color:var(--ottone)">0{i+1}</div><div class="disp" style="font-size:30px;margin-top:6px">{t}</div><div class="mono" style="font-size:13px;color:var(--muted);margin-top:6px">{w}</div><p style="font-size:15px;line-height:1.45;color:var(--muted);margin-top:10px">{d}</p></div>'
    s.append(f'''<section class="slide">
  <div class="label">I tempi</div>
  <h2>{c['t_title']}</h2>
  <p class="intro">{c['t_intro']}</p>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);border:2px solid var(--ink);border-radius:10px;overflow:hidden;margin-top:30px;background:var(--raised)">{steps}</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:20px">
    <div style="background:var(--giallo);border-radius:10px;padding:22px 26px"><div class="mono" style="font-size:12px;letter-spacing:.14em;font-weight:500">{c['t_box1'][0]}</div><div class="disp" style="font-size:36px;margin-top:8px">{c['t_box1'][1]}</div></div>
    <div style="background:var(--steel);border-radius:10px;padding:22px 26px"><div class="mono" style="font-size:12px;letter-spacing:.14em;font-weight:500;color:var(--muted)">{c['t_box2'][0]}</div><div class="disp" style="font-size:36px;margin-top:8px">{c['t_box2'][1]}</div></div>
  </div>
  {foot(L, 10 + len(c.get('extra', [])))}
</section>''')
    # 11 next
    s.append(f'''<section class="slide dark" style="padding-top:110px">
  <img src="{B}rr-sigla-su-scuro.svg" style="position:absolute;right:-80px;top:40px;height:720px;opacity:.08" alt="">
  <div class="label">Prossimo passo</div>
  <h1 style="font-size:84px;margin-top:20px;color:#fff">Dieci minuti di questionario,<br><span style="color:var(--giallo)">entro {c.get('scadenza','venerdì 27 novembre')}</span></h1>
  <p style="font-size:20px;line-height:1.5;color:#C9CED1;margin-top:22px;max-width:1000px">Poche domande, si risponde anche dal telefono. Diteci anche quale combinazione vi interessa: in due giorni lavorativi vi confermiamo il prezzo fisso e le date.</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:40px;position:relative">
    <a class="cta cta-y" href="https://tally.so/r/{c['tally']}?da=pdf">
      <div><div class="k">★ Poche domande · dieci minuti</div><div class="t">Rispondete al questionario</div><div class="u">tally.so/r/{c['tally']}</div></div><div class="arr">→</div>
    </a>
    <div class="cta cta-o">
      <div><div class="k" style="color:var(--giallo)">Preferite parlarne a voce?</div><div class="t">Passiamo da voi</div><div class="u" style="color:var(--onhero-m)">Rispondete alla mail di Simone</div></div><div class="arr">→</div>
    </div>
  </div>
  <div style="position:absolute;left:86px;right:86px;bottom:60px;display:flex;align-items:center;gap:22px">
    <img src="{B}rr-sigla-su-scuro.svg" style="height:56px" alt="">
    <div><div class="disp" style="font-size:24px;color:#fff">Rock ’n’ Roll Studio · Matteo &amp; Simone</div><div class="mono" style="font-size:13px;color:var(--onhero-m);margin-top:4px">{c.get('payoff','Siti web seri. Noi, un po’ meno.')} · Proposta del {c.get('data','5 novembre 2026')}, valida 30 giorni</div></div>
    <div style="margin-left:auto;display:flex;align-items:center;gap:12px;border:2px solid #A9B0B4;padding:4px 16px"><span class="mono" style="font-size:11px;color:var(--onhero-m);letter-spacing:.12em">FIRMATO</span><img src="{B}rr-firma-chiaro.svg" style="height:78px" alt="Firma Rock ’n’ Roll Studio"></div>
  </div>
  <div class="stripe" style="position:absolute;left:0;right:0;bottom:0;height:12px"></div>
</section>''')
    head = re.sub(r'<title>.*?</title>', f'<title>{c["name"]} · Proposta Rock ’n’ Roll Studio</title>', HEAD)
    return head + STYLE2 + '\n</head>\n<body>\n' + '\n\n'.join(s) + '\n</body>\n</html>\n'

if __name__ == '__main__':
    import importlib.util
    spec = importlib.util.spec_from_file_location('data', sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    open(sys.argv[2], 'w', encoding='utf-8').write(build(m.C))
