# -*- coding: utf-8 -*-
"""
build_verktoy.py — genererer statiske verktøy-sider for rettsregel.no
Alle satser er verifisert per juni 2026 (G per 1.5.2026, forsinkelsesrente
1. halvår 2026, inkassosats 2026, fri rettshjelp etter reform 15.10.2025).
Kjør:  python3 build_verktoy.py
Output: HTML-filer i samme mappe + deler styles.css.
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

def pn(n):  # norsk tusenskille for tekst
    return format(int(round(n)), ",d").replace(",", " ")

# ---- felles satser (kilde i kommentar) ----
G        = 136549      # NAV, per 1.5.2026
SEKSG    = 6*G         # 819 294
HALVG    = 68275      # 0,5G per 1.5.2026 (NAV, avrundet opp)
FEMG     = 5*G         # 682 745
RENTE    = "12,00"     # forsinkelsesrente 1. halvår 2026 (Finanstilsynet)
STDKOMP  = 460         # standardkompensasjon B2B (forsinkelsesrenteloven §3a)
INKSATS  = 750         # inkassosatsen 2026
PURRE    = 38          # purregebyr / inkassovarsel 2026
BO_EGEN  = 113         # betalingsoppfordring (egeninkasso) 2026
RETTSGEB = 1345        # rettsgebyr 2026
ENGANGS  = 92648       # engangsstønad 2026

SHELL = """<!DOCTYPE html>
<html lang="no">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__ – Rettsregel</title>
<meta name="description" content="__DESC__">
<link rel="canonical" href="https://rettsregel.no/verktoy/__SLUG__.html">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..600&family=Schibsted+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="wrap">
  <div class="top"><span class="brand-dot"></span><a href="../">Rettsregel</a> &nbsp;/&nbsp; <a href="../">Verktøy</a></div>
  <span class="tag">__KICKER__</span>
  <h1>__TITLE__</h1>
  <p class="lede">__LEDE__</p>
__BODY__
  <p class="disclaimer">Verktøyet gir et veiledende estimat basert på gjeldende satser og regler (oppdatert juni 2026). Det er generell informasjon, ikke juridisk rådgivning, og erstatter ikke en konkret vurdering. Sjekk alltid mot offisielle kilder før du handler.</p>
</div>
<script>
const nf = n => Math.round(n).toLocaleString('nb-NO');
const nf2 = n => n.toLocaleString('nb-NO',{minimumFractionDigits:2,maximumFractionDigits:2});
const val = id => parseFloat((document.getElementById(id).value||'').replace(/\\s/g,'').replace(',','.'))||0;
function seg(group, cb){
  document.querySelectorAll('[data-seg="'+group+'"] button').forEach(b=>{
    b.addEventListener('click',()=>{
      document.querySelectorAll('[data-seg="'+group+'"] button').forEach(x=>x.setAttribute('aria-pressed','false'));
      b.setAttribute('aria-pressed','true'); cb && cb(b.dataset.v);
    });
  });
}
function segv(group){const b=document.querySelector('[data-seg="'+group+'"] button[aria-pressed=true]');return b?b.dataset.v:null;}
__SCRIPT__
</script>
</body>
</html>"""

def page(slug, kicker, title, lede, desc, body, script):
    html = (SHELL
        .replace("__SLUG__", slug)
        .replace("__KICKER__", kicker)
        .replace("__TITLE__", title)
        .replace("__LEDE__", lede)
        .replace("__DESC__", desc)
        .replace("__BODY__", body)
        .replace("__SCRIPT__", script))
    with open(os.path.join(OUT, slug + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    return slug

pages = []

# =========================================================
# 1. FORSINKELSESRENTE
# =========================================================
pages.append(page(
 "forsinkelsesrente", "Forsinkelsesrenteloven",
 "Forsinkelsesrente-kalkulator",
 "Regn ut hvor mye forsinkelsesrente du kan kreve på en ubetalt faktura eller et forfalt krav.",
 "Beregn forsinkelsesrente (morarente) etter forsinkelsesrenteloven. Gjeldende sats 1. halvår 2026: 12,00 %.",
 """
  <div class="card">
    <div class="field"><label for="bel">Skyldig beløp (hovedstol)</label>
      <div class="inputaffix"><input id="bel" type="number" inputmode="decimal" placeholder="10 000"><span class="suffix">kr</span></div></div>
    <div class="row">
      <div class="field"><label for="frd">Forfallsdato</label><input id="frd" type="date"></div>
      <div class="field"><label for="tld">Betalt / regn til</label><input id="tld" type="date"></div>
    </div>
    <div class="field"><label for="sats">Rentesats</label>
      <div class="hint">Standard 1. halvår 2026 er 12,00 %. Endre om kravet løper over en periode med annen sats.</div>
      <div class="inputaffix"><input id="sats" type="text" inputmode="decimal" value=\"""" + RENTE + """\"><span class="suffix">% p.a.</span></div></div>
    <div class="field"><label class="check"><input id="b2b" type="checkbox"><span>Næringskrav (B2B) – legg til standardkompensasjon """ + str(STDKOMP) + """ kr</span></label></div>
    <button class="btn" onclick="calc()">Regn ut</button>
  </div>
  <div class="result" id="res">
    <div class="biglabel">Forsinkelsesrente</div>
    <div class="big" id="big">–</div>
    <div class="lines" id="lines"></div>
    <div class="note" id="note"></div>
  </div>
  <div class="lawbox"><b>Slik fungerer det:</b> Renten løper fra dagen etter forfall til betaling skjer (forsinkelsesrenteloven § 2). Mot en forbruker kan du ikke avtale høyere sats enn den fastsatte. Standardkompensasjon (§ 3a) gjelder bare når skyldner er næringsdrivende/offentlig.</div>
 """,
 """
const today=new Date().toISOString().slice(0,10);
document.getElementById('tld').value=today;
function calc(){
  const bel=val('bel'), sats=val('sats');
  const f=document.getElementById('frd').value, t=document.getElementById('tld').value;
  if(!bel||!f||!t){alert('Fyll inn beløp og datoer.');return;}
  const d1=new Date(f), d2=new Date(t);
  let days=Math.round((d2-d1)/86400000);
  if(days<0){alert('Sluttdato er før forfall.');return;}
  const rente=bel*(sats/100)*days/365;
  const komp=document.getElementById('b2b').checked?""" + str(STDKOMP) + """:0;
  const total=bel+rente+komp;
  document.getElementById('big').textContent=nf(rente)+' kr';
  let h='<div class="ln"><span>Antall dager forsinket</span><span>'+days+' dager</span></div>';
  h+='<div class="ln"><span>Rentesats</span><span>'+document.getElementById('sats').value+' % p.a.</span></div>';
  h+='<div class="ln"><span>Daglig rente</span><span>'+nf2(bel*(sats/100)/365)+' kr</span></div>';
  if(komp)h+='<div class="ln"><span>Standardkompensasjon</span><span>'+nf(komp)+' kr</span></div>';
  h+='<div class="ln tot"><span>Totalt å kreve (hovedstol + rente'+(komp?' + komp.':'')+')</span><span>'+nf(total)+' kr</span></div>';
  document.getElementById('lines').innerHTML=h;
  document.getElementById('note').textContent= days>183 ? 'Kravet strekker seg over mer enn ett halvår – renten kan ha endret seg i perioden. Del eventuelt opp og bruk riktig sats for hver periode.' : '';
  document.getElementById('res').classList.add('show');
}
 """))

# =========================================================
# 2. DOKUMENTAVGIFT
# =========================================================
pages.append(page(
 "dokumentavgift", "Boligkjøp",
 "Dokumentavgift-kalkulator",
 "Regn ut dokumentavgiften (2,5 %) og tinglysingsgebyret du må betale når du kjøper bolig.",
 "Beregn dokumentavgift på 2,5 % av kjøpesummen pluss tinglysingsgebyr ved boligkjøp.",
 """
  <div class="card">
    <div class="field"><label for="kjop">Kjøpesum / markedsverdi</label>
      <div class="inputaffix"><input id="kjop" type="number" inputmode="decimal" placeholder="4 000 000"><span class="suffix">kr</span></div></div>
    <div class="field"><label>Type bolig</label>
      <div class="seg" data-seg="type">
        <button data-v="selveier" aria-pressed="true">Selveier / fast eiendom</button>
        <button data-v="borettslag">Borettslag (andel)</button>
      </div>
      <div class="hint" style="margin-top:8px">Andel i borettslag har <b>ikke</b> dokumentavgift – kun et eierskiftegebyr til forretningsfører.</div>
    </div>
    <div class="field"><label for="ting">Tinglysing</label>
      <select id="ting"><option value="585">Papir – 585 kr</option><option value="440">Elektronisk – 440 kr</option></select></div>
    <button class="btn" onclick="calc()">Regn ut</button>
  </div>
  <div class="result" id="res">
    <div class="biglabel">Dokumentavgift</div>
    <div class="big" id="big">–</div>
    <div class="lines" id="lines"></div>
    <div class="note" id="note"></div>
  </div>
  <div class="lawbox"><b>Fritak finnes</b> bl.a. ved overføring mellom ektefeller, arv til lovbestemte arvinger, og ved nyoppført bolig (da betales avgift kun av tomteverdien). Ved samlivsbrudd kan felles bolig være fritatt hvis vilkår om felles adresse/barn er oppfylt.</div>
 """,
 """
seg('type', calc);
function calc(){
  const kjop=val('kjop'); const ting=parseFloat(document.getElementById('ting').value);
  if(!kjop){return;}
  const borettslag = segv('type')==='borettslag';
  let avgift=0, grunnlag=0;
  if(!borettslag){
    grunnlag=Math.floor(kjop/1000)*1000;            // avrundes ned til nærmeste 1000
    avgift=Math.floor((grunnlag*0.025)/10)*10;       // avrundes ned til nærmeste 10
    if(avgift<250) avgift=250;                        // minimum
  }
  document.getElementById('big').textContent=nf(avgift)+' kr';
  let h='';
  if(borettslag){
    h+='<div class="ln"><span>Dokumentavgift</span><span>0 kr (ingen ved borettslag)</span></div>';
  } else {
    h+='<div class="ln"><span>Avgiftsgrunnlag</span><span>'+nf(grunnlag)+' kr</span></div>';
    h+='<div class="ln"><span>Sats</span><span>2,5 %</span></div>';
  }
  h+='<div class="ln"><span>Tinglysingsgebyr</span><span>'+nf(ting)+' kr</span></div>';
  h+='<div class="ln tot"><span>Sum offentlige omkostninger</span><span>'+nf(avgift+ting)+' kr</span></div>';
  document.getElementById('lines').innerHTML=h;
  document.getElementById('note').textContent= borettslag ? 'I tillegg kommer eierskiftegebyr til borettslagets forretningsfører (varierer, ofte 4 000–6 000 kr).' : '';
  document.getElementById('res').classList.add('show');
}
 """))

# =========================================================
# 3. SYKEPENGER
# =========================================================
pages.append(page(
 "sykepenger", "Folketrygdloven",
 "Sykepenger-kalkulator",
 "Regn ut hvor mye du får i sykepenger fra NAV. Sykepenger dekker inntekt opp til 6G – maks "+pn(SEKSG)+" kr i året.",
 "Beregn sykepenger fra NAV ut fra årsinntekten din. Dekning opp til 6G (819 294 kr i 2026).",
 """
  <div class="card">
    <div class="field"><label>Hvem er du?</label>
      <div class="seg" data-seg="type">
        <button data-v="arb" aria-pressed="true">Arbeidstaker</button>
        <button data-v="frilans">Frilanser</button>
        <button data-v="selv">Selvstendig</button>
      </div></div>
    <div class="field"><label for="lonn">Årsinntekt (brutto)</label>
      <div class="inputaffix"><input id="lonn" type="number" inputmode="decimal" placeholder="600 000"><span class="suffix">kr</span></div></div>
    <button class="btn" onclick="calc()">Regn ut</button>
  </div>
  <div class="result" id="res">
    <div class="biglabel" id="biglabel">Sykepenger per måned</div>
    <div class="big" id="big">–</div>
    <div class="lines" id="lines"></div>
    <div class="note" id="note"></div>
  </div>
  <div class="lawbox" id="law"></div>
 """,
 """
const SEKSG=""" + str(SEKSG) + """;
seg('type', calc);
function calc(){
  const lonn=val('lonn'); if(!lonn)return;
  const t=segv('type');
  const dekn = (t==='selv')?0.8:1.0;       // selvstendig 80 %, ellers 100 %
  const grunnlag=Math.min(lonn,SEKSG);
  const aar=grunnlag*dekn;
  const mnd=aar/12;
  document.getElementById('big').textContent=nf(mnd)+' kr';
  let h='<div class="ln"><span>Sykepengegrunnlag</span><span>'+nf(grunnlag)+' kr'+(lonn>SEKSG?' (kappet ved 6G)':'')+'</span></div>';
  h+='<div class="ln"><span>Dekningsgrad</span><span>'+(dekn*100)+' %</span></div>';
  h+='<div class="ln"><span>Per år</span><span>'+nf(aar)+' kr</span></div>';
  h+='<div class="ln"><span>Per dag (5 dager/uke)</span><span>'+nf(aar/260)+' kr</span></div>';
  if(lonn>SEKSG){const tap=(lonn-SEKSG)*dekn/12;h+='<div class="ln tot"><span>Inntekt over 6G som NAV ikke dekker</span><span>'+nf(tap)+' kr/mnd</span></div>';}
  document.getElementById('lines').innerHTML=h;
  let law='';
  if(t==='arb'){
    document.getElementById('note').textContent='Arbeidsgiver betaler de første 16 kalenderdagene (arbeidsgiverperioden), deretter overtar NAV i inntil 248 dager (ca. ett år).';
    law='<b>Arbeidstaker:</b> 100 % av lønn opptil 6G. Mange arbeidsgivere dekker også inntekt over 6G – sjekk arbeidsavtalen eller tariffavtalen.';
  } else if(t==='frilans'){
    document.getElementById('note').textContent='Frilansere får sykepenger fra og med dag 17.';
    law='<b>Frilanser:</b> 100 % av sykepengegrunnlaget fra dag 17, opptil 6G.';
  } else {
    document.getElementById('note').textContent='Selvstendig næringsdrivende får sykepenger fra og med dag 17.';
    law='<b>Selvstendig næringsdrivende:</b> 80 % fra dag 17, opptil 6G. Du kan tegne frivillig tilleggsforsikring hos NAV for 80 % fra dag 1 eller 100 % dekning.';
  }
  document.getElementById('law').innerHTML=law;
  document.getElementById('res').classList.add('show');
}
 """))

# =========================================================
# 4. FORELDREPENGER
# =========================================================
pages.append(page(
 "foreldrepenger", "Folketrygdloven",
 "Foreldrepenger-kalkulator",
 "Se hva du får i foreldrepenger, og sammenlign 100 % i 49 uker mot 80 % i 61 uker. Dekning opp til 6G.",
 "Beregn foreldrepenger fra NAV. Sammenlign 100 % (49 uker) og 80 % (61 uker) og se fordelingen mellom foreldrene.",
 """
  <div class="card">
    <div class="field"><label for="lonn">Årsinntekt (brutto)</label>
      <div class="inputaffix"><input id="lonn" type="number" inputmode="decimal" placeholder="600 000"><span class="suffix">kr</span></div></div>
    <div class="field"><label>Dekningsgrad</label>
      <div class="seg" data-seg="dg">
        <button data-v="100" aria-pressed="true">100 % – 49 uker</button>
        <button data-v="80">80 % – 61 uker</button>
      </div></div>
    <button class="btn" onclick="calc()">Regn ut</button>
  </div>
  <div class="result" id="res">
    <div class="biglabel">Utbetaling per måned</div>
    <div class="big" id="big">–</div>
    <div class="lines" id="lines"></div>
    <div class="note" id="note"></div>
  </div>
  <div class="lawbox" id="law"></div>
 """,
 """
const SEKSG=""" + str(SEKSG) + """, HALVG=""" + str(HALVG) + """, ENG=""" + str(ENGANGS) + """;
seg('dg', calc);
function calc(){
  const lonn=val('lonn'); if(!lonn)return;
  if(lonn<HALVG){
    document.getElementById('big').textContent=nf(ENG)+' kr';
    document.getElementById('lines').innerHTML='<div class="ln"><span>Engangsstønad (utbetales én gang)</span><span>'+nf(ENG)+' kr</span></div>';
    document.getElementById('note').textContent='Inntekten din er under 0,5G ('+nf(HALVG)+' kr). Da har du ikke rett til foreldrepenger, men får engangsstønad.';
    document.getElementById('law').innerHTML='';
    document.getElementById('res').classList.add('show');return;
  }
  const dg=segv('dg')==='80'?0.8:1.0;
  const grunnlag=Math.min(lonn,SEKSG);
  const mnd=grunnlag*dg/12;
  const uker = dg===1?49:61;
  const total=grunnlag*dg*(uker/52);
  document.getElementById('big').textContent=nf(mnd)+' kr';
  let h='<div class="ln"><span>Dekningsgrad</span><span>'+(dg*100)+' %</span></div>';
  h+='<div class="ln"><span>Varighet</span><span>'+uker+' uker'+(dg===0.8?' + 1 dag':'')+'</span></div>';
  h+='<div class="ln"><span>Grunnlag</span><span>'+nf(grunnlag)+' kr'+(lonn>SEKSG?' (kappet ved 6G)':'')+'</span></div>';
  if(lonn>SEKSG)h+='<div class="ln"><span>Inntekt over 6G (dekkes ikke av NAV)</span><span>'+nf((lonn-SEKSG)*dg/12)+' kr/mnd</span></div>';
  h+='<div class="ln tot"><span>Samlet utbetaling over hele perioden</span><span>'+nf(total)+' kr</span></div>';
  document.getElementById('lines').innerHTML=h;
  document.getElementById('note').textContent='Total utbetaling er omtrent lik enten du velger 100 % eller 80 %. 100 % gir høyere månedsbeløp, 80 % gir lengre tid hjemme.';
  const q = dg===1
    ? 'Mødrekvote 15 uker · fedre-/medmorkvote 15 uker · fellesperiode 16 uker (deles fritt). I tillegg 3 uker før termin forbeholdt mor.'
    : 'Mødrekvote 19 uker · fedre-/medmorkvote 19 uker · fellesperiode 20 uker + 1 dag (deles fritt). I tillegg 3 uker før termin forbeholdt mor.';
  document.getElementById('law').innerHTML='<b>Fordeling ved '+(dg*100)+' %:</b> '+q;
  document.getElementById('res').classList.add('show');
}
 """))

# =========================================================
# 5. HUSLEIEØKNING (KPI)
# =========================================================
pages.append(page(
 "husleieokning", "Husleieloven",
 "Lovlig husleieøkning (KPI)",
 "Hvor mye kan utleier øke husleia? Husleieloven § 4-2 lar leia justeres med konsumprisindeksen én gang i året.",
 "Regn ut lovlig husleieøkning etter konsumprisindeksen (KPI), jf. husleieloven § 4-2.",
 """
  <div class="card">
    <div class="field"><label for="leie">Dagens månedsleie</label>
      <div class="inputaffix"><input id="leie" type="number" inputmode="decimal" placeholder="12 000"><span class="suffix">kr</span></div></div>
    <div class="row">
      <div class="field"><label for="kg">KPI ved forrige justering</label>
        <div class="hint">Indeks-tall fra SSB</div>
        <input id="kg" type="number" inputmode="decimal" placeholder="128,5"></div>
      <div class="field"><label for="kn">KPI nå</label>
        <div class="hint">Nyeste indeks fra SSB</div>
        <input id="kn" type="number" inputmode="decimal" placeholder="133,2"></div>
    </div>
    <div class="field"><label for="dato">Dato for forrige leiefastsetting/-økning</label>
      <input id="dato" type="date"></div>
    <button class="btn" onclick="calc()">Regn ut</button>
  </div>
  <div class="result" id="res">
    <div class="biglabel">Ny lovlig maks månedsleie</div>
    <div class="big" id="big">–</div>
    <div class="lines" id="lines"></div>
    <div class="verdict" id="verdict" style="margin-top:14px"></div>
    <div class="note" id="note"></div>
  </div>
  <div class="lawbox"><b>To regler:</b> Etter <b>§ 4-2</b> kan leia KPI-justeres tidligst ett år etter forrige fastsetting, med minst én måneds skriftlig varsel. Etter <b>§ 4-3</b> kan hver part hvert tredje år kreve leia satt til «gjengs leie» (markedsnivå for liknende leieforhold), med seks måneders varsel.</div>
 """,
 """
function calc(){
  const leie=val('leie'), kg=val('kg'), kn=val('kn');
  if(!leie||!kg||!kn){alert('Fyll inn leie og begge KPI-tallene.');return;}
  const faktor=kn/kg;
  const ny=leie*faktor;
  const pct=(faktor-1)*100;
  document.getElementById('big').textContent=nf(ny)+' kr';
  let h='<div class="ln"><span>KPI-endring i perioden</span><span>'+nf2(pct)+' %</span></div>';
  h+='<div class="ln"><span>Tillatt økning</span><span>'+nf(ny-leie)+' kr/mnd</span></div>';
  h+='<div class="ln tot"><span>Ny maks månedsleie</span><span>'+nf(ny)+' kr</span></div>';
  document.getElementById('lines').innerHTML=h;
  const v=document.getElementById('verdict');
  const d=document.getElementById('dato').value;
  if(d){
    const months=(new Date()-new Date(d))/86400000/30.44;
    if(months<12){v.className='verdict bad';v.innerHTML='<span class="ic">✕</span><span>Det er bare '+Math.floor(months)+' mnd siden forrige fastsetting. KPI-justering kan tidligst kreves etter 12 måneder.</span>';}
    else{v.className='verdict ok';v.innerHTML='<span class="ic">✓</span><span>Det er over 12 måneder siden forrige justering – økningen er tillatt med minst én måneds skriftlig varsel.</span>';}
  } else { v.className='verdict warn';v.innerHTML='<span class="ic">!</span><span>Husk: KPI-justering krever at det er gått minst 12 måneder, og minst én måneds skriftlig varsel.</span>'; }
  document.getElementById('note').textContent='Negativ KPI-utvikling gir lavere maks. Leia kan aldri settes høyere enn KPI tilsier etter § 4-2.';
  document.getElementById('res').classList.add('show');
}
 """))

# =========================================================
# 6. INKASSOSALÆR-SJEKKER
# =========================================================
pages.append(page(
 "inkassosalaer", "Inkassoloven",
 "Inkassosalær-sjekker",
 "Er inkassokostnaden lovlig? Regn ut maksimalt inkassosalær etter inkassoforskriftens satser for 2026.",
 "Sjekk om inkassosalæret er lovlig. Maksimale satser etter inkassoforskriften for 2026.",
 """
  <div class="card">
    <div class="field"><label for="hs">Opprinnelig krav (hovedstol)</label>
      <div class="inputaffix"><input id="hs" type="number" inputmode="decimal" placeholder="5 000"><span class="suffix">kr</span></div></div>
    <div class="field"><label>Hvem er skyldner?</label>
      <div class="seg" data-seg="skyld">
        <button data-v="forb" aria-pressed="true">Forbruker (privatperson)</button>
        <button data-v="nar">Næringsdrivende</button>
      </div></div>
    <div class="field"><label for="mva">Kreditorens momsstatus</label>
      <div class="hint">Banker, forsikring, helse og undervisning har normalt ikke fradragsrett – da er salæret høyere.</div>
      <select id="mva"><option value="fra">Har fradragsrett for mva (vanligst)</option><option value="ikke">Har ikke fradragsrett for mva</option></select></div>
    <div class="field"><label>Hvor langt er saken kommet?</label>
      <div class="seg" data-seg="trinn">
        <button data-v="enkel" aria-pressed="true">Betalingsoppfordring (lett salær)</button>
        <button data-v="tung">Etter tilleggsfrist (tungt salær)</button>
      </div></div>
    <div class="field"><label for="krevd">Salær du faktisk er krevd for <span class="hint" style="display:inline">(valgfritt)</span></label>
      <div class="inputaffix"><input id="krevd" type="number" inputmode="decimal" placeholder="f.eks. 1 200"><span class="suffix">kr</span></div></div>
    <button class="btn" onclick="calc()">Sjekk</button>
  </div>
  <div class="result" id="res">
    <div class="biglabel">Lovlig maks inkassosalær</div>
    <div class="big" id="big">–</div>
    <div class="verdict" id="verdict"></div>
    <div class="lines" id="lines"></div>
    <div class="note" id="note"></div>
  </div>
  <div class="lawbox"><b>Gjeldende gebyrer 2026:</b> purregebyr og inkassovarsel """ + str(PURRE) + """ kr, betalingsoppfordring du selv sender (egeninkasso) """ + str(BO_EGEN) + """ kr, standardkompensasjon ved næringskrav """ + str(STDKOMP) + """ kr. «Tungt salær» (dobbelt) kan tidligst kreves når betalingsfristen i betalingsoppfordringen er oversittet med mer enn 28 dager.</div>
 """,
 """
// Maksimalsatser inkassoforskriften 2026 (Finanstilsynet). [t.o.m. hovedstol, enkel, tung]
const T={
 forb_fra:[[500,187.5,375],[1000,262.5,525],[2500,300,600],[10000,600,1200],[50000,1200,2400],[250000,2700,5400],[Infinity,5400,10800]],
 nar_fra :[[500,281.25,562.5],[1000,393.75,787.5],[2500,450,900],[10000,900,1800],[50000,1800,3600],[250000,4050,8100],[Infinity,8100,16200]],
 forb_ikke:[[500,234.38,468.75],[1000,328.13,656.25],[2500,375,750],[10000,750,1500],[50000,1500,3000],[250000,3375,6750],[Infinity,6750,13500]],
 nar_ikke :[[500,351.56,703.13],[1000,492.19,984.38],[2500,562.5,1125],[10000,1125,2250],[50000,2250,4500],[250000,5062.5,10125],[Infinity,10125,20250]]
};
seg('skyld', calc); seg('trinn', calc);
function calc(){
  const hs=val('hs'); if(!hs)return;
  const key=(segv('skyld')==='forb'?'forb':'nar')+'_'+(document.getElementById('mva').value==='fra'?'fra':'ikke');
  const tbl=T[key];
  const row=tbl.find(r=>hs<=r[0]);
  const enkel=row[1], tung=row[2];
  const tungtrinn=segv('trinn')==='tung';
  const maks=tungtrinn?tung:enkel;
  document.getElementById('big').textContent=nf2(maks)+' kr';
  let h='<div class="ln"><span>Lett salær (betalingsoppfordring)</span><span>'+nf2(enkel)+' kr</span></div>';
  h+='<div class="ln"><span>Tungt salær (etter tilleggsfrist)</span><span>'+nf2(tung)+' kr</span></div>';
  h+='<div class="ln"><span>Purregebyr / inkassovarsel</span><span>""" + str(PURRE) + """ kr</span></div>';
  document.getElementById('lines').innerHTML=h;
  const krevd=val('krevd'); const v=document.getElementById('verdict');
  if(krevd){
    if(krevd<=maks+0.5){v.className='verdict ok';v.innerHTML='<span class="ic">✓</span><span>Salæret på '+nf2(krevd)+' kr er innenfor lovlig maks ('+nf2(maks)+' kr) på dette trinnet.</span>';}
    else{v.className='verdict bad';v.innerHTML='<span class="ic">✕</span><span>'+nf2(krevd)+' kr er <b>høyere</b> enn lovlig maks ('+nf2(maks)+' kr). Du kan klage til inkassoselskapet og eventuelt Finanstilsynet / Inkassoklagenemnda.</span>';}
  } else { v.className='';v.innerHTML='';v.style.display='none'; }
  if(krevd) v.style.display='flex';
  document.getElementById('note').textContent='Mva legges på salæret dersom kreditor ikke har fradragsrett – det er innbakt i tallene over. Flere krav mot samme kreditor skal slås sammen til én sak.';
  document.getElementById('res').classList.add('show');
}
 """))

# =========================================================
# 7. FRI RETTSHJELP-SJEKKER
# =========================================================
pages.append(page(
 "fri-rettshjelp", "Rettshjelploven",
 "Fri rettshjelp – sjekk om du kvalifiserer",
 "Fra 15. oktober 2025 vurderes fri rettshjelp etter betalingsevne. Sjekk om du er under grensen på 5G ("+pn(FEMG)+" kr).",
 "Sjekk om du har rett til fri rettshjelp etter den nye betalingsevne-modellen. Grense 5G (682 745 kr i 2026).",
 """
  <div class="card">
    <div class="field"><label>Husstand</label>
      <div class="seg" data-seg="hus">
        <button data-v="en" aria-pressed="true">Enslig</button>
        <button data-v="par">Par / felles økonomi</button>
      </div></div>
    <div class="field" id="f1"><label for="i1">Bruttoinntekt per år</label>
      <div class="inputaffix"><input id="i1" type="number" inputmode="decimal" placeholder="400 000"><span class="suffix">kr</span></div></div>
    <div class="field" id="f2" style="display:none"><label for="i2">Partnerens bruttoinntekt per år</label>
      <div class="inputaffix"><input id="i2" type="number" inputmode="decimal" placeholder="350 000"><span class="suffix">kr</span></div></div>
    <div class="field"><label for="form">Nettoformue</label>
      <div class="hint">Verdi av og gjeld i egen bolig holdes utenfor.</div>
      <div class="inputaffix"><input id="form" type="number" inputmode="decimal" placeholder="0"><span class="suffix">kr</span></div></div>
    <button class="btn" onclick="calc()">Sjekk</button>
  </div>
  <div class="result" id="res">
    <div class="verdict" id="verdict"></div>
    <div class="lines" id="lines"></div>
    <div class="note" id="note"></div>
  </div>
  <div class="lawbox"><b>Slik regnes det:</b> Betalingsevnen er bruttoinntekt pluss halvparten av nettoformuen (utenom egen bolig). For par legges inntektene sammen og det brukes en faktor på 0,6. Er betalingsevnen under 5G får du fri rettshjelp i utvalgte sakstyper. Det gis i tillegg fradrag for barn, og egenandelen avhenger av økonomien din – bruk <a href="https://www.statsforvalteren.no" target="_blank" rel="noopener">Statsforvalterens kalkulator</a> for nøyaktig beregning.</div>
 """,
 """
const FEMG=""" + str(FEMG) + """, ENG_G=""" + str(G) + """;
seg('hus', v=>{document.getElementById('f2').style.display=(v==='par')?'block':'none';});
function calc(){
  const par=segv('hus')==='par';
  const i1=val('i1'), i2=par?val('i2'):0, form=val('form');
  if(!i1 && !i2){alert('Fyll inn inntekt.');return;}
  let evne;
  if(par) evne=0.6*((i1+i2)+0.5*form);
  else    evne=i1+0.5*form;
  const v=document.getElementById('verdict');
  if(evne<=FEMG){
    v.className='verdict ok';
    v.innerHTML='<span class="ic">✓</span><span>Du er trolig <b>under grensen</b> og kan ha rett til fri rettshjelp i sakstypene ordningen dekker.</span>';
  } else if(evne<=FEMG*1.15){
    v.className='verdict warn';
    v.innerHTML='<span class="ic">!</span><span>Du er litt over grensen. Med fradrag for barn kan du likevel kvalifisere – sjekk Statsforvalterens kalkulator.</span>';
  } else {
    v.className='verdict bad';
    v.innerHTML='<span class="ic">✕</span><span>Betalingsevnen er over grensen. Du har trolig ikke rett til behovsprøvd fri rettshjelp, men enkelte saker gis uavhengig av inntekt.</span>';
  }
  let h='<div class="ln"><span>Beregnet betalingsevne</span><span>'+nf(evne)+' kr</span></div>';
  h+='<div class="ln"><span>Grense (5G)</span><span>'+nf(FEMG)+' kr</span></div>';
  h+='<div class="ln tot"><span>Egenandel</span><span>'+(evne<ENG_G?'Fritatt (under 1G)':'1–99 % etter økonomi')+'</span></div>';
  document.getElementById('lines').innerHTML=h;
  document.getElementById('note').textContent='Noen sakstyper (f.eks. barnevern og tvangssaker) gir fri rettshjelp uavhengig av inntekt og formue.';
  document.getElementById('res').classList.add('show');
}
 """,
 ))

# Legg til en myk CTA på fri-rettshjelp-siden (Walrus-funnel) ved å skrive om etterpå
# (gjøres i etterbehandling under)

# =========================================================
# 8. FORELDELSE-SJEKKER
# =========================================================
pages.append(page(
 "foreldelse", "Foreldelsesloven",
 "Foreldelse-sjekker",
 "Er kravet foreldet? Regn ut foreldelsesfristen etter foreldelsesloven – 3 år for vanlige krav, 10 år for gjeldsbrev.",
 "Sjekk om et pengekrav er foreldet. Beregn foreldelsesfristen etter foreldelsesloven (3 eller 10 år).",
 """
  <div class="card">
    <div class="field"><label>Type krav</label>
      <div class="seg" data-seg="type">
        <button data-v="3" aria-pressed="true">Vanlig krav (3 år)</button>
        <button data-v="10">Gjeldsbrev / pengelån (10 år)</button>
      </div>
      <div class="hint" style="margin-top:8px">Faktura, kjøp, tjenester o.l. = 3 år. Lån dokumentert med gjeldsbrev = 10 år.</div></div>
    <div class="field"><label for="forfall">Forfallsdato</label>
      <div class="hint">Da kravet tidligst kunne kreves betalt.</div>
      <input id="forfall" type="date"></div>
    <div class="field"><label class="check"><input id="avbr" type="checkbox" onchange="document.getElementById('avbrf').style.display=this.checked?'block':'none'"><span>Fristen er avbrutt (skyldner erkjente kravet skriftlig, eller du tok rettslig skritt)</span></label>
      <div id="avbrf" style="display:none;margin-top:10px"><input id="avbrd" type="date"></div></div>
    <button class="btn" onclick="calc()">Sjekk</button>
  </div>
  <div class="result" id="res">
    <div class="biglabel">Kravet foreldes</div>
    <div class="big" id="big">–</div>
    <div class="verdict" id="verdict"></div>
    <div class="note" id="note"></div>
  </div>
  <div class="lawbox"><b>Viktig:</b> Fristen avbrytes (og starter på nytt) hvis skyldner erkjenner kravet, eller du tar rettslig skritt – f.eks. forliksklage eller utleggsbegjæring (§§ 14–17). I tillegg finnes en <b>tilleggsfrist</b> på inntil 1 år fra du fikk eller burde fått kunnskap om kravet og skyldner (§ 10), men aldri mer enn 10 år ekstra. Reglene har mange unntak.</div>
 """,
 """
seg('type', ()=>{ if(document.getElementById('res').classList.contains('show')) calc(); });
const months=['januar','februar','mars','april','mai','juni','juli','august','september','oktober','november','desember'];
function fmt(d){return d.getDate()+'. '+months[d.getMonth()]+' '+d.getFullYear();}
function calc(){
  const aar=parseInt(segv('type'));
  const start=document.getElementById('avbr').checked? document.getElementById('avbrd').value : document.getElementById('forfall').value;
  if(!start){alert('Fyll inn dato.');return;}
  const d=new Date(start); const f=new Date(d); f.setFullYear(f.getFullYear()+aar);
  document.getElementById('big').textContent=fmt(f);
  const now=new Date();
  const v=document.getElementById('verdict');
  if(now>f){
    v.className='verdict bad';
    v.innerHTML='<span class="ic">✕</span><span>Kravet er <b>trolig foreldet</b> – fristen gikk ut '+fmt(f)+'. Sjekk om noe har avbrutt fristen underveis.</span>';
  } else {
    const dager=Math.ceil((f-now)/86400000);
    v.className='verdict ok';
    v.innerHTML='<span class="ic">✓</span><span>Kravet er <b>ikke foreldet</b> ennå. Det gjenstår '+nf(dager)+' dager til fristen.</span>';
  }
  document.getElementById('note').textContent=document.getElementById('avbr').checked?'Fristen er regnet fra avbruddsdatoen, og løper '+aar+' nye år fra da.':'';
  document.getElementById('res').classList.add('show');
}
 """))

# =========================================================
# Etterbehandling: legg CTA inn på fri-rettshjelp (Walrus-funnel)
# =========================================================
p = os.path.join(OUT, "fri-rettshjelp.html")
with open(p, encoding="utf-8") as f: html = f.read()
cta = """  <div class="cta">
    <h3>Trenger du en advokat?</h3>
    <p>Får du ikke fri rettshjelp, eller vil du ha en vurdering av saken din?</p>
    <a href="https://rettsregel.no/kontakt/">Ta kontakt</a>
  </div>
"""
html = html.replace('  <p class="disclaimer">', cta + '  <p class="disclaimer">')
with open(p, "w", encoding="utf-8") as f: f.write(html)

# =========================================================
# 9. UTROSKAPSKONTRAKT (dokumentgenerator)
# =========================================================
pages.append(page(
 "utrokontrakt", "Samliv",
 "Utroskapskontrakt – lag avtalen selv",
 "Lag en samlivsavtale med troskapsklausul. Velg hva som regnes som utroskap og hvilke konsekvenser som skal gjelde – så genererer vi en ferdig avtale til signering.",
 "Lag en utroskapskontrakt (troskapsklausul) for samboere eller ektefeller. Velg definisjon og konsekvens, og last ned en ferdig avtale. Med ærlig forklaring av hva som faktisk er håndhevbart.",
 """
  <div class="card">
    <div class="field"><label>Hvem inngår avtalen?</label>
      <div class="seg" data-seg="rel">
        <button data-v="sam" aria-pressed="true">Samboere</button>
        <button data-v="ekte">Ektefeller</button>
      </div></div>
    <div class="row2">
      <div class="field"><label for="na">Navn – part 1</label>
        <input id="na" type="text" placeholder="Ola Nordmann"></div>
      <div class="field"><label for="nb">Navn – part 2</label>
        <input id="nb" type="text" placeholder="Kari Nordmann"></div>
    </div>
    <div class="field"><label>Hva regnes som utroskap? <span class="hint" style="display:inline">(kryss av alt som gjelder)</span></label>
      <div class="chips">
        <label class="chip"><input type="checkbox" class="defchk" data-label="seksuell omgang med en annen person" checked> Seksuell omgang med andre</label>
        <label class="chip"><input type="checkbox" class="defchk" data-label="kyssing eller annen fysisk intimitet med en annen person"> Kyssing / fysisk intimitet</label>
        <label class="chip"><input type="checkbox" class="defchk" data-label="et følelsesmessig (emosjonelt) forhold til en annen person"> Emosjonelt forhold</label>
        <label class="chip"><input type="checkbox" class="defchk" data-label="kontakt av seksuell karakter via dating-apper, meldinger eller deling av nakenbilder"> Digitalt (dating-apper, sexting)</label>
        <label class="chip"><input type="checkbox" class="defchk" data-label="salg eller deling av seksuelt innhold med andre (f.eks. på betalingsplattformer)"> Betalt/delt innhold</label>
      </div>
      <input id="defannet" type="text" placeholder="Annet (skriv fritt) …" style="margin-top:8px"></div>
    <div class="field"><label>Konsekvens ved brudd <span class="hint" style="display:inline">(kryss av alt som gjelder)</span></label>
      <div class="chips">
        <label class="chip"><input type="checkbox" class="conschk" data-label="flytte ut av felles bolig innen {dager} dager" checked> Flytter ut innen X dager</label>
        <label class="chip"><input type="checkbox" class="conschk" data-label="avstå fra sin andel av en eventuell gevinst ved salg av felles bolig"> Avstår andel av boliggevinst</label>
        <label class="chip"><input type="checkbox" class="conschk" data-label="betale et avtalt beløp på {belop} kr til den andre parten"> Betaler avtalt beløp</label>
        <label class="chip"><input type="checkbox" class="conschk" data-label="dekke kostnaden ved parterapi dersom partene velger å fortsette samlivet"> Dekker parterapi</label>
      </div>
      <input id="consannet" type="text" placeholder="Annen konsekvens (skriv fritt) …" style="margin-top:8px"></div>
    <div class="row2">
      <div class="field"><label for="dager">Frist for utflytting (dager)</label>
        <input id="dager" type="number" inputmode="numeric" placeholder="30"></div>
      <div class="field"><label for="belop">Avtalt beløp (kr)</label>
        <input id="belop" type="number" inputmode="numeric" placeholder="50 000"></div>
    </div>
    <div class="row2">
      <div class="field"><label for="sted">Sted</label>
        <input id="sted" type="text" placeholder="Oslo"></div>
      <div class="field"><label for="dato">Dato</label>
        <input id="dato" type="date"></div>
    </div>
    <button class="btn" onclick="gen()">Lag avtale</button>
  </div>

  <div class="result" id="res">
    <div class="docbar">
      <button class="ghost" onclick="window.print()">Skriv ut / lagre som PDF</button>
      <button class="ghost" onclick="kopier()">Kopier tekst</button>
    </div>
    <div class="avtale" id="avtale"></div>
  </div>

  <div class="lawbox"><b>Hva er faktisk bindende?</b><br>
  <b>Samboere</b> har full avtalefrihet – dere kan inngå en slik avtale. Det svake punktet er <b>håndhevelsen</b>, ikke gyldigheten: det må kunne sannsynliggjøres at brudd har skjedd, «utroskap» må være presist definert (gråsoner skaper tvist), og et urimelig høyt straffebeløp kan settes ned eller settes til side etter <b>avtaleloven § 36</b>. Overføring av eierandel i bolig kan dessuten utløse <b>dokumentavgift og skatt</b>.<br><br>
  <b>Ektefeller</b>: en troskapsklausul kan <b>ikke</b> tas inn i en ektepakt – ektepakt regulerer kun formuesordningen (særeie m.m.). En egen avtale er mulig, men står svakere, og utroskap gir uansett <b>ingen særskilt rett til skilsmisse</b> og påvirker ikke skilsmisseoppgjøret i seg selv (ekteskapsloven har ingen regler om utroskap).</div>

  <div class="cta">
    <p>Vil dere ha en avtale som faktisk holder ved en tvist? Få en advokat til å sette den opp riktig.</p>
    <a href="https://rettsregel.no/kontakt/">Ta kontakt</a>
  </div>

  <p class="readmore">Les mer: <a href="kan-man-lage-utroskapskontrakt.html">Kan man lage en utroskapskontrakt i Norge?</a></p>

  <style>
  .chips{display:flex;flex-wrap:wrap;gap:8px}
  .chip{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line);border-radius:999px;padding:8px 14px;font-size:.92rem;cursor:pointer;background:var(--card);user-select:none}
  .chip input{accent-color:var(--accent)}
  .row2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  @media(max-width:520px){.row2{grid-template-columns:1fr}}
  .docbar{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:18px}
  .ghost{background:var(--card);border:1px solid var(--line);color:var(--ink);border-radius:10px;padding:9px 16px;font:inherit;font-weight:600;cursor:pointer}
  .avtale{background:#fff;color:#1a1a1a;border:1px solid var(--line);border-radius:12px;padding:34px 38px;line-height:1.6;font-size:.98rem}
  .avtale h2{font-family:'Fraunces',serif;font-size:1.45rem;margin:0 0 4px}
  .avtale .sub{color:#555;margin:0 0 22px;font-size:.9rem}
  .avtale h3{font-size:1rem;margin:20px 0 6px}
  .avtale ol,.avtale ul{margin:6px 0 6px 20px}
  .avtale li{margin:3px 0}
  .sig{display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-top:46px}
  .sigline{border-top:1px solid #333;padding-top:6px;font-size:.85rem;color:#444}
  @media print{
    body *{visibility:hidden}
    #avtale,#avtale *{visibility:visible}
    #avtale{position:absolute;left:0;top:0;width:100%;border:none;padding:0}
  }
  </style>
 """,
 """
seg('rel');
function esc(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function gen(){
  const a = esc((document.getElementById('na').value||'Part 1').trim());
  const b = esc((document.getElementById('nb').value||'Part 2').trim());
  const relword = segv('rel')==='ekte' ? 'ektefeller' : 'samboere';
  const defs = [...document.querySelectorAll('.defchk:checked')].map(x=>x.dataset.label);
  const da = (document.getElementById('defannet').value||'').trim(); if(da) defs.push(da);
  const dager = parseInt(document.getElementById('dager').value)||'…';
  const belop = val('belop');
  const cons = [];
  document.querySelectorAll('.conschk:checked').forEach(x=>{
    cons.push(x.dataset.label.replace('{dager}',dager).replace('{belop}', belop?nf(belop):'…'));
  });
  const ca = (document.getElementById('consannet').value||'').trim(); if(ca) cons.push(ca);
  const sted = esc((document.getElementById('sted').value||'').trim());
  const dato = document.getElementById('dato').value;
  let datotxt = '';
  if(dato){ const d=new Date(dato); const m=['januar','februar','mars','april','mai','juni','juli','august','september','oktober','november','desember'];
    datotxt = d.getDate()+'. '+m[d.getMonth()]+' '+d.getFullYear(); }
  const stedDato = [sted, datotxt].filter(Boolean).join(', ');

  if(defs.length===0){ alert('Velg minst én ting som regnes som utroskap.'); return; }
  if(cons.length===0){ alert('Velg minst én konsekvens.'); return; }

  let h = '';
  h += '<h2>Samlivsavtale med troskapsklausul</h2>';
  h += '<p class="sub">Inngått mellom '+a+' og '+b+'</p>';
  h += '<p>Denne avtalen inngås mellom <b>'+a+'</b> og <b>'+b+'</b>, heretter kalt «partene», som lever sammen som '+relword+'. Partene ønsker med dette å klargjøre felles forventninger om gjensidig troskap og hva som skal gjelde dersom forventningene brytes.</p>';

  h += '<h3>§ 1 Gjensidig troskapsplikt</h3>';
  h += '<p>Partene forplikter seg til gjensidig troskap så lenge samlivet består. Forpliktelsen gjelder begge parter likt.</p>';

  h += '<h3>§ 2 Hva som regnes som brudd</h3>';
  h += '<p>Som brudd på troskapsplikten regnes at en av partene har:</p><ul>';
  defs.forEach(d=> h += '<li>'+esc(d)+'</li>');
  h += '</ul>';

  h += '<h3>§ 3 Konsekvens ved brudd</h3>';
  h += '<p>Dersom en av partene bryter § 2, skal vedkommende:</p><ol>';
  cons.forEach(c=> h += '<li>'+esc(c)+'</li>');
  h += '</ol><p>Konsekvensene gjelder uavhengig av hvem av partene som har brutt avtalen.</p>';

  h += '<h3>§ 4 Varsel og dokumentasjon</h3>';
  h += '<p>Den parten som påberoper seg et brudd, må kunne sannsynliggjøre at brudd har funnet sted. Partene kan avtale et møte – eventuelt med mekler eller parterapeut – før en konsekvens iverksettes.</p>';

  h += '<h3>§ 5 Gyldighet og forbehold</h3>';
  h += '<p>Partene er kjent med at en troskapsklausul kan være vanskelig å håndheve i praksis, og at et urimelig vilkår kan revideres eller settes til side etter avtaleloven § 36. Overføring av eierandel i felles bolig kan utløse dokumentavgift og skatt. Avtalen erstatter ikke reglene i ekteskapsloven eller annen lovgivning.</p>';

  h += '<div class="sig">';
  h += '<div class="sigline">Sted og dato: '+(stedDato||'________________')+'<br><br><br>______________________________<br>'+a+'</div>';
  h += '<div class="sigline">Sted og dato: '+(stedDato||'________________')+'<br><br><br>______________________________<br>'+b+'</div>';
  h += '</div>';

  document.getElementById('avtale').innerHTML = h;
  document.getElementById('res').classList.add('show');
  const r=document.getElementById('res'); if(r.scrollIntoView) r.scrollIntoView({behavior:'smooth',block:'start'});
}
function kopier(){
  const t = document.getElementById('avtale').innerText;
  navigator.clipboard && navigator.clipboard.writeText(t);
  const btns=document.querySelectorAll('.ghost'); btns[1].textContent='Kopiert ✓';
  setTimeout(()=>btns[1].textContent='Kopier tekst',1500);
}
 """))

# =========================================================
# INDEX
# =========================================================
cards = [
 ("forsinkelsesrente","Forsinkelsesrenteloven","Forsinkelsesrente","Regn ut morarente på en ubetalt faktura."),
 ("inkassosalaer","Inkassoloven","Inkassosalær-sjekker","Er inkassokostnaden lovlig?"),
 ("foreldelse","Foreldelsesloven","Foreldelse-sjekker","Er kravet foreldet?"),
 ("dokumentavgift","Boligkjøp","Dokumentavgift","2,5 % avgift ved boligkjøp."),
 ("sykepenger","Folketrygdloven","Sykepenger","Hvor mye får du i sykepenger?"),
 ("foreldrepenger","Folketrygdloven","Foreldrepenger","100 % eller 80 %? Se hva du får."),
 ("husleieokning","Husleieloven","Husleieøkning (KPI)","Hvor mye kan leia økes?"),
 ("fri-rettshjelp","Rettshjelploven","Fri rettshjelp","Kvalifiserer du til gratis advokat?"),
 ("utrokontrakt","Samliv","Utroskapskontrakt","Lag en samlivsavtale med troskapsklausul."),
]
grid = "\n".join(
 '    <a class="tool" href="%s.html"><div class="k">%s</div><div class="t">%s</div><p class="d">%s</p></a>' % c
 for c in cards)
index = SHELL
index = index.replace("__SLUG__","").replace("__KICKER__","Gratis verktøy")
index = index.replace("__TITLE__","Rettsregel Verktøy")
index = index.replace("__DESC__","Gratis juridiske kalkulatorer og sjekkere – forsinkelsesrente, inkasso, foreldelse, sykepenger, foreldrepenger, dokumentavgift, husleie og fri rettshjelp.")
index = index.replace("__LEDE__","Gratis kalkulatorer og sjekkere bygget på norsk lov. Oppdaterte satser for 2026.")
index = index.replace("__BODY__", '  <div class="grid">\n'+grid+'\n  </div>')
index = index.replace("__SCRIPT__","")
index = index.replace('<div class="top"><span class="brand-dot"></span><a href="../">Rettsregel</a> &nbsp;/&nbsp; <a href="../">Verktøy</a></div>',
                      '<div class="top"><span class="brand-dot"></span><a href="https://rettsregel.no">Rettsregel</a></div>')
index = index.replace('href="../styles.css"','href="styles.css"')
index = index.replace('href="https://rettsregel.no/verktoy/.html"','href="https://rettsregel.no/verktoy/"')
with open(os.path.join(OUT,"index.html"),"w",encoding="utf-8") as f: f.write(index)

print("Bygget:", ", ".join(pages), "+ index")