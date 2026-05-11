"""Rettsregel: Kjøpsloven §§ 21-50 (mangler, forsinkelse, pris, betaling, medvirkning)."""

PARAGRAPHS = [
    # =============================================================
    # § 21 — Når må mangelen ha vært der?
    # =============================================================
    {
        "number": "21",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Når må mangelen ha vært der?",
        "description": "Mangelen må ha vært der da risikoen gikk over på deg — selv om den først viser seg senere. Selgeren svarer også for feil som skyldes hans kontraktbrudd.",
        "kort_svar": "Det avgjørende er om mangelen var der da risikoen gikk over på deg — som regel ved levering. Selv om feilen først dukker opp senere, kan den fortsatt være en mangel hvis årsaken lå i varen fra start. Selgeren svarer også for feil som oppstår senere hvis det skyldes hans kontraktbrudd, eller hvis han har gitt garanti.",
        "paragraftekst": """(1) Ved bedømmelse av om tingen har mangel, skal det tidspunktet da risikoen går over på kjøperen legges til grunn, selv om mangelen først viser seg seinere.

(2) Selgeren svarer også for mangel som oppstår seinere dersom den skyldes kontraktbrudd fra hans side. Det samme gjelder dersom selgeren ved garanti eller på annen måte har påtatt seg ansvar for at tingen vil ha angitte egenskaper eller være egnet til vanlig bruk eller en særlig bruksmåte i et tidsrom etter leveringen.""",
        "hva_betyr_html": """<p>Loven svarer på et viktig spørsmål: en feil dukker opp tre måneder etter kjøpet — er det en "mangel" selgeren må svare for, eller bare normal slitasje?</p>
<p>Regelen er: feilen må ha eksistert da risikoen gikk over på deg (typisk ved levering, jf. § 13). Det betyr ikke at feilen må ha vært synlig. Den kan ha ligget skjult som en svakhet i varen og først blitt et problem senere. Det er fortsatt en mangel.</p>
<p>Eksempel: en motor med fabrikkfeil som først ryker etter to måneders bruk — feilen var i motoren fra start, og det er mangel.</p>
<p><strong>To tilfeller hvor selgeren også svarer for senere feil:</strong></p>
<ul>
<li><strong>Selgerens kontraktbrudd (andre ledd, første setning):</strong> Hvis feilen oppstår senere fordi selgeren har gjort noe galt — for eksempel installert noe feil — er det selgerens ansvar.</li>
<li><strong>Garanti (andre ledd, andre setning):</strong> Hvis selgeren har gitt garanti, svarer han for at varen oppfyller garantien i hele garantiperioden. Da spiller det ingen rolle om feilen var der fra start.</li>
</ul>
<h3>Sammenligning: Var det mangel?</h3>
<table class="rule-table">
<thead><tr><th>Situasjon</th><th>Mangel?</th></tr></thead>
<tbody>
<tr><td>Feil var skjult, dukket opp etter 2 mnd</td><td>Ja, hvis feilen kan spores tilbake</td></tr>
<tr><td>Normal slitasje</td><td>Nei</td></tr>
<tr><td>Bruksskade du laget</td><td>Nei</td></tr>
<tr><td>Feil oppstod fordi selger installerte galt</td><td>Ja</td></tr>
<tr><td>Feil innenfor garantitid</td><td>Ja, hvis dekket av garantien</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Marius", "tekst": "Marius kjøper en brukt bil for 120 000 kr. Etter tre måneder ryker drivverket. Verkstedet sier slitasjen tyder på at det har vært på vei i lang tid — også før kjøpet. Selv om feilen først viste seg etter kjøp, var problemet til stede ved levering. Det er en mangel etter § 21 første ledd. Marius må kunne dokumentere dette — vurdering fra verksted er normalt bevis. Han kan reklamere etter § 32."},
            {"navn": "Ingrid", "tekst": "Ingrid kjøper en kaffemaskin med 2 års garanti på trykksystemet. Etter 14 måneder ryker pumpen — det viser seg å være normal slitasje, ikke en innebygget feil. Vanligvis ville dette ikke vært en mangel etter § 21 (1). Men siden selgeren har gitt garanti på trykksystemet, svarer han uansett etter § 21 (2). Ingrid har krav på reparasjon eller omlevering."},
        ],
        "vanlige_feil": [
            "Tror at hvis feilen viser seg etter kjøp, kan man ikke klage — feil",
            "Tror at all senere skade er din egen — det avhenger av årsaken",
            "Glemmer at bevisbyrden ligger hos deg etter kjøpsloven (i forbrukerkjøp er det motsatt de første 6 månedene)",
        ],
        "hva_bor_du_html": """<p><strong>Som kjøper:</strong></p>
<ul>
<li>Få faglig vurdering når feilen dukker opp — verksted, takstmann</li>
<li>Dokumenter med bilder og rapporter</li>
<li>Reklamer raskt etter at du oppdaget feilen (§ 32)</li>
</ul>
<p><strong>Som selger:</strong></p>
<ul>
<li>Vær tydelig på hva en eventuell garanti dekker</li>
<li>Hold deg innenfor det du faktisk har lovet</li>
<li>Hvis kjøperen klager: be om dokumentasjon på når feilen oppstod</li>
</ul>""",
        "dumme_sporsmal": [
            {"q": "Bilen virket fin i fem uker, så ryket motoren. Er det min skyld?", "a": "Ikke automatisk. Hvis verkstedet kan vise at problemet var underveis fra før kjøpet — for eksempel slitasjespor, gamle skader, forhold som tar lang tid å utvikle — er det mangel."},
            {"q": "Hva er forskjellen på garanti og reklamasjonsrett?", "a": "Reklamasjonsretten kommer fra loven og dekker mangler som var der ved kjøpet. Garanti er en avtale som gjelder uavhengig av om feilen var der fra start — så lenge feilen er innenfor det garantien dekker."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "13", "tittel": "Når går risikoen over", "available": True},
            {"lov": "kjopsloven", "paragraf": "17", "tittel": "Når har varen mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "32", "tittel": "Reklamasjonsfrister", "available": True},
            {"lov": "kjopsloven", "paragraf": "40", "tittel": "Erstatning ved mangel", "available": True},
        ],
    },
    # =============================================================
    # § 22 — Hva du kan kreve ved forsinkelse
    # =============================================================
    {
        "number": "22",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Hva du kan kreve ved forsinkelse",
        "description": "Får du ikke varen — eller får den for sent? Du kan kreve oppfyllelse, heve kjøpet, kreve erstatning og holde tilbake betaling.",
        "kort_svar": "Hvis varen ikke kommer eller kommer for sent, og det ikke er din skyld, har du fire mulige krav: krev at varen leveres likevel, hev kjøpet og få pengene tilbake, krev erstatning for tapet ditt, og hold tilbake din betaling. Du kan kombinere kravene — å kreve oppfyllelse stenger ikke for erstatning.",
        "paragraftekst": """(1) Dersom tingen ikke blir levert eller blir levert for seint, og dette ikke skyldes kjøperen eller forhold på hans side, kan han etter §§ 23 til 29 kreve oppfyllelse, heving og erstatning samt holde kjøpesummen tilbake etter § 42. Hans rett til erstatning faller ikke bort ved at han gjør gjeldende andre krav eller ved at disse ikke kan gjøres gjeldende.

(2) Dersom selgeren ikke i tide oppfyller sine plikter ellers etter kjøpet, gjelder bestemmelsene om forsinkelse tilsvarende så langt de passer, likevel ikke § 25 (2) og (3).""",
        "hva_betyr_html": """<p>Dette er døråpneren til alt som handler om forsinkelse. Når selgeren ikke leverer i tide — og det ikke er din skyld — har du fire verktøy:</p>
<p><strong>1. Krev oppfyllelse (§ 23):</strong> Krev at selgeren leverer likevel. Du kan fastholde kjøpet og insistere på å få varen.</p>
<p><strong>2. Hev kjøpet (§ 25):</strong> Trekk deg fra hele kjøpet, få tilbake det du har betalt, og kjøp varen et annet sted.</p>
<p><strong>3. Krev erstatning (§ 27):</strong> Få dekket det tapet forsinkelsen påførte deg — uten å miste retten til andre krav.</p>
<p><strong>4. Hold tilbake betaling (§ 42):</strong> Ikke betal det du skylder før selgeren leverer. Du beholder pengene som press.</p>
<p><strong>Viktig poeng:</strong> Du kan kombinere kravene. Du kan kreve oppfyllelse og samtidig kreve erstatning for at det ble forsinket. Eller heve og kreve erstatning for merkostnadene du fikk.</p>
<p>Andre ledd gjør reglene gjeldende også for andre plikter selgeren har — som å sende dokumenter eller varsle om noe. Da gjelder forsinkelsesreglene "så langt de passer", med to unntak: du kan ikke sette tilleggsfrist og automatisk heve hvis det bare er en sideplikt.</p>""",
        "eksempler": [
            {"navn": "Kari", "tekst": "Kari har bestilt nytt badekar fra et lite firma for 24 000 kr. Avtalt levering var 1. april. Det er nå 1. mai og ingenting har kommet. Kari har allerede betalt halvparten. Hun har fire valg: insistere på at badekaret leveres, heve kjøpet og få 12 000 kr tilbake, kreve erstatning for ekstra kostnader, eller holde tilbake restbetalingen. Hun kan også kombinere — for eksempel heve og kreve erstatning samtidig."},
            {"navn": "Ola", "tekst": "Ola driver et lite verksted og har bestilt reservedeler fra en grossist for 18 000 kr, leveringstid avtalt til torsdag. Det er fredag — ingen deler. Han har en kunde som venter og må kjøpe delene andre steder for 21 000 kr. Ola kan både heve hovedkjøpet og kreve mellomlegget på 3 000 kr som erstatning etter § 27 og § 68 (prisforskjell ved dekningstransaksjon)."},
        ],
        "vanlige_feil": [
            "Tror du må velge mellom oppfyllelse og erstatning — du kan ha begge",
            "Krever heving for tidlig — det krever vesentlig kontraktbrudd eller tilleggsfrist (§ 25)",
            "Glemmer å holde tilbake betaling — det er det sterkeste pressmiddelet du har",
            "Som selger: tror du kan unngå krav ved å levere «snart»",
        ],
        "hva_bor_du_html": """<p>Steg for steg når selgeren er forsinket:</p>
<ol>
<li>Send melding skriftlig — SMS eller e-post — om at varen er forsinket</li>
<li>Sett tilleggsfrist hvis avtalen ikke er klart nok overtrådt (§ 25 (2))</li>
<li>Hold tilbake din betaling så langt du har rett til</li>
<li>Vurder dekningskjøp og dokumenter kostnadene</li>
<li>Hev formelt hvis fristen passerer (§ 25)</li>
<li>Krev erstatning for konkrete tap</li>
</ol>
<p>Hold alt skriftlig. Det er det som teller hvis det blir tvist.</p>""",
        "related": [
            {"lov": "kjopsloven", "paragraf": "23", "tittel": "Krav om oppfyllelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "25", "tittel": "Heving ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "27", "tittel": "Erstatning ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "42", "tittel": "Tilbakeholdsrett", "available": True},
        ],
    },
    # =============================================================
    # § 23 — Krav om at selgeren leverer
    # =============================================================
    {
        "number": "23",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Krav om at selgeren leverer",
        "description": "Du kan kreve at selgeren leverer som avtalt — så lenge det ikke er umulig eller urimelig dyrt. Venter du for lenge med å si fra, taper du retten.",
        "kort_svar": "Du kan fastholde kjøpet og kreve at selgeren leverer. Unntak: hvis det er en hindring selgeren ikke kan overvinne, eller hvis det vil koste selgeren urimelig mye sammenliknet med din interesse. Forsvinner hindringen raskt, gjelder kravet igjen. Men venter du urimelig lenge med å fremme kravet, taper du det.",
        "paragraftekst": """(1) Kjøperen kan fastholde kjøpet og kreve oppfyllelse. Dette gjelder ikke om det foreligger en hindring som selgeren ikke kan overvinne, eller for så vidt oppfyllelse vil medføre så stor ulempe eller kostnad for selgeren at det står i vesentlig misforhold til kjøperens interesse i at selgeren oppfyller.

(2) Faller vanskene bort innen rimelig tid, kan kjøperen kreve oppfyllelse når ikke dette etter den tid som er gått, vil være vesentlig mer tyngende eller få en annen karakter enn selgeren kunne forutse eller det for øvrig vil være urimelig å kreve oppfyllelse.

(3) Kjøperen taper sin rett til oppfyllelse om han venter urimelig lenge med å fremme kravet.""",
        "hva_betyr_html": """<p>Hovedregelen er enkel: avtalen er bindende, og du kan kreve at den blir oppfylt. Men loven legger inn tre praktiske grenser:</p>
<p><strong>1. Umulig (første ledd, første del):</strong> Hvis varen er ødelagt eller fabrikken brent ned, kan du ikke kreve oppfyllelse av noe som ikke finnes. Det må være en hindring "selgeren ikke kan overvinne".</p>
<p><strong>2. Urimelig dyrt (første ledd, andre del):</strong> Hvis det å levere vil koste selgeren mye mer enn det er verdt for deg, faller kravet. Du har bestilt en spesialdel for 5 000 kr. Det viser seg at selgeren må gå til mye større kostnader for å skaffe den. Det kan være urimelig.</p>
<p><strong>3. Kortvarig hindring (andre ledd):</strong> Hvis hindringen forsvinner raskt, kan du fortsatt kreve oppfyllelse — såfremt situasjonen ikke har endret seg vesentlig.</p>
<p><strong>4. Du må fremme kravet i tide (tredje ledd):</strong> Hvis du venter urimelig lenge med å si fra at du fortsatt vil ha varen, mister du retten. Du kan ikke la saken ligge i seks måneder og så plutselig kreve levering.</p>""",
        "eksempler": [
            {"navn": "Tom", "tekst": "Tom har bestilt en spesialtilpasset racersykkel for 65 000 kr med avtalt levering 1. mai. Det er 1. juni. Selgeren sier «vi er sene fordi rammeleverandøren har problemer, men vi får det ordnet». Tom vil ha sykkelen — han har tenkt på den i månedsvis. Tom kan etter § 23 fastholde kjøpet og kreve oppfyllelse. Forsinkelsen skyldes en hindring (leverandørproblem), men det er ikke uoverkommelig. Tom må gi beskjed innen rimelig tid om at han fortsatt vil ha sykkelen, ikke bare vente i taushet."},
            {"navn": "Eva", "tekst": "Eva har bestilt en spesiell modell av en kjøkkenmaskin. Etter to måneder oppdager hun og selgeren at modellen er gått ut av produksjon — det er umulig å skaffe akkurat den maskinen. Her gjelder § 23 unntaket. Eva kan ikke kreve oppfyllelse av noe som ikke finnes. Men hun kan heve kjøpet (§ 25) og kreve erstatning (§ 27) — og selgeren burde gitt beskjed straks han fikk vite om problemet (§ 28)."},
        ],
        "vanlige_feil": [
            "Venter for lenge med å si fra at du fortsatt vil ha varen — du taper kravet",
            "Tror du alltid kan kreve levering uansett — det finnes grenser",
            "Glemmer at «rimelig tid» varierer med varens kompleksitet",
            "Krever heving før du har fastholdt — som regel bedre å sette tilleggsfrist først",
        ],
        "hva_bor_du_html": """<ul>
<li>Gi beskjed skriftlig at du krever oppfyllelse, og innen rimelig tid</li>
<li>Sett gjerne ny frist så det er tydelig</li>
<li>Vurder om varen fortsatt er verdt å vente på — eller om heving er bedre</li>
<li>Hold dokumentasjon på alt — meldinger, e-poster, datoer</li>
</ul>""",
        "related": [
            {"lov": "kjopsloven", "paragraf": "22", "tittel": "Hva du kan kreve ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "25", "tittel": "Heving ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "52", "tittel": "Selgerens rett til oppfyllelse", "available": False},
        ],
    },
    # =============================================================
    # § 24 — Når selgeren spør om du vil ha varen likevel
    # =============================================================
    {
        "number": "24",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Når selgeren spør om du vil ha varen likevel",
        "description": "Spør selgeren om du vil ta imot varen tross forsinkelsen — eller varsler om ny dato — og du ikke svarer, mister du retten til å heve.",
        "kort_svar": "Hvis selgeren spør om du vil ha varen tross forsinkelsen — eller varsler om en ny leveringsdato — og du ikke svarer innen rimelig tid, mister du retten til å heve. Forutsetningen er at selgeren faktisk leverer innen den oppgitte tiden.",
        "paragraftekst": """Dersom selgeren spør om kjøperen tross forsinkelsen vil motta levering, eller underretter kjøperen om at han vil levere innen en angitt tid, men kjøperen ikke svarer innen rimelig tid etter at han har fått meldingen, kan han ikke heve om oppfyllelse skjer innen den tid som er angitt.""",
        "hva_betyr_html": """<p>Loven gir selgeren en mulighet til å redde situasjonen — og krever av deg å gi klar beskjed.</p>
<p><strong>To situasjoner:</strong></p>
<ul>
<li>Selgeren spør: «Vil du fortsatt ha varen tross forsinkelsen?»</li>
<li>Selgeren varsler: «Jeg leverer innen [dato].»</li>
</ul>
<p>Hvis du ikke svarer innen rimelig tid, og selgeren leverer som lovet, kan du ikke heve. Tausheten din regnes som godtakelse av den nye fristen.</p>
<p><strong>Logikken:</strong> Selgeren skal vite om han skal levere eller ikke. Du kan ikke sitte stille og senere late som du aldri ville ha varen.</p>
<p><strong>Viktig:</strong> Dette gjelder bare retten til å heve. Du kan fortsatt kreve erstatning for selve forsinkelsen (§ 27) — for eksempel ekstra kostnader du har hatt fordi du ventet.</p>""",
        "eksempler": [
            {"navn": "Marius", "tekst": "Marius har bestilt en spesialtilpasset kontorstol for 14 000 kr med avtalt levering 1. mars. Det er 15. mars. Selgeren sender e-post 16. mars: «Beklager, vi leverer 25. mars.» Hvis Marius ikke svarer og selgeren leverer 25. mars, kan ikke Marius heve. Han godtok i praksis den nye fristen ved å være taus. Hvis Marius derimot svarer «nei, jeg vil ikke ha den lenger — jeg har kjøpt en annen», står han fritt til å heve."},
            {"navn": "Anne", "tekst": "Anne hadde satt en tilleggsfrist på 14 dager. Fristen gikk ut. Selgeren sender melding: «Jeg leverer i morgen.» Anne svarer ikke. Selgeren leverer. Anne kan ikke heve. Men hvis tilleggsfristen var gått ut og hun raskt hadde hevet før selgerens melding, hadde situasjonen vært annerledes."},
        ],
        "vanlige_feil": [
            "Ignorerer meldinger fra selger og tror du står fritt — du gjør ikke det",
            "Tror du må heve umiddelbart — du har rimelig tid til å svare, men ikke ubegrenset",
            "Glemmer at erstatningsretten ikke faller bort",
        ],
        "hva_bor_du_html": """<p>Når selgeren spør eller varsler ny dato:</p>
<ul>
<li>Svar skriftlig — ikke vær taus</li>
<li>Gjør valget tydelig: ta imot, sette ny tilleggsfrist, eller heve</li>
<li>Skriv det ned: dato, hva du har sagt</li>
<li>Krev fortsatt erstatning for konkrete tap</li>
</ul>
<p>Standard-svar hvis du vil heve: «Jeg har allerede gått ut over rimelig ventetid. Jeg trekker meg fra kjøpet og krever pengene tilbake.»</p>""",
        "related": [
            {"lov": "kjopsloven", "paragraf": "22", "tittel": "Hva du kan kreve ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "25", "tittel": "Heving ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "29", "tittel": "Frist for å heve etter for sen levering", "available": True},
        ],
    },
    # =============================================================
    # § 25 — Heving ved forsinkelse
    # =============================================================
    {
        "number": "25",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Heving ved forsinkelse",
        "description": "Du kan heve kjøpet hvis forsinkelsen er vesentlig — eller hvis selgeren ikke leverer innen tilleggsfristen du har satt.",
        "kort_svar": "Du kan heve kjøpet på to måter: hvis forsinkelsen er vesentlig (sterkt kontraktbrudd), eller hvis du har satt en rimelig tilleggsfrist og selgeren ikke leverer innen den. Mens tilleggsfristen løper kan du ikke heve — med mindre selgeren sier han ikke vil eller kan levere.",
        "paragraftekst": """(1) Kjøperen kan heve kjøpet når forsinkelsen medfører vesentlig kontraktbrudd.

(2) Kjøpet kan også heves dersom selgeren ikke leverer innen en rimelig tilleggsfrist for oppfyllelse som kjøperen har fastsatt.

(3) Mens tilleggsfristen løper kan ikke kjøperen heve, med mindre selgeren har sagt at han ikke vil oppfylle innen fristen.""",
        "hva_betyr_html": """<p>Heving er det sterkeste verktøyet du har. Du kansellerer kjøpet, får pengene tilbake, og selgeren får varen tilbake. Loven gir to veier inn:</p>
<p><strong>1. Vesentlig kontraktbrudd (første ledd):</strong> Hvis forsinkelsen i seg selv er så alvorlig at det rammer formålet med kjøpet, kan du heve uten videre. Tenk: du skulle bruke utstyret på et bestemt arrangement som nå er ferdig, eller forsinkelsen er så langvarig at det «ikke gir mening lenger». Hva som er vesentlig avhenger av:</p>
<ul>
<li>Hvor lenge forsinkelsen har vart</li>
<li>Hva varen skulle brukes til</li>
<li>Om selgeren visste om formålet</li>
<li>Om du har gjort dekningskjøp et annet sted</li>
<li>Konsekvensene for deg</li>
</ul>
<p><strong>2. Tilleggsfrist (andre ledd):</strong> Hvis forsinkelsen ikke er klart vesentlig, kan du sette en rimelig tilleggsfrist. Hvis selgeren da ikke leverer, kan du heve — uansett om bruddet var «vesentlig» eller ikke. Dette er den tryggeste veien.</p>
<p>«Rimelig» varierer med varen — for en standard nettbestilling kanskje 7–14 dager, for en kompleks tilvirkning lenger.</p>
<p><strong>Mens fristen løper (tredje ledd):</strong> Du må vente til tilleggsfristen er ute før du kan heve — med mindre selgeren sier rett ut at han ikke kommer til å levere innen fristen. Da kan du heve med en gang.</p>
<h3>Sammenligning: Hev direkte eller via tilleggsfrist?</h3>
<table class="rule-table">
<thead><tr><th>Situasjon</th><th>Direkte heving (1. ledd)?</th><th>Tilleggsfrist trygt valg</th></tr></thead>
<tbody>
<tr><td>Forsinkelsen rammer formålet (gave, arrangement)</td><td>Ja</td><td>Også</td></tr>
<tr><td>Selgeren visste om viktig dato</td><td>Ja</td><td>Også</td></tr>
<tr><td>Tre dager over avtalt for et «vanlig» kjøp</td><td>Tvilsomt</td><td>Ja, sett tilleggsfrist</td></tr>
<tr><td>Selgeren sier han ikke kommer til å levere</td><td>Ja</td><td>Du trenger ikke vente</td></tr>
<tr><td>Uklart om forsinkelsen er vesentlig</td><td>Risikabelt</td><td>Sett tilleggsfrist</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Lars", "tekst": "Lars har bestilt et leketog til sønnens 6-årsdag, avtalt levering 10. desember. 18. desember har det fortsatt ikke kommet. Bursdagen er 22. desember. Forsinkelsen er allerede klart vesentlig — selgeren visste sannsynligvis om formålet (det er en bursdagsgave), og forsinkelsen rammer hele poenget. Lars kan heve direkte etter § 25 (1), uten å sette tilleggsfrist. Hvis ingenting tilsa at det var en gave, ville Lars først måttet sette tilleggsfrist."},
            {"navn": "Eva", "tekst": "Eva har bestilt en oppvaskmaskin. Den skulle leveres 5. april. Det er 25. april og den har ikke kommet. Eva skriver: «Jeg setter en tilleggsfrist på 10 dager. Hvis maskinen ikke er levert innen 5. mai, hever jeg kjøpet.» 5. mai kommer — fortsatt ingen maskin. Eva kan nå heve. Hun sender en melding: «Jeg viser til min tilleggsfrist av 25. april. Fristen er utløpt. Jeg hever kjøpet og krever betalingen tilbake.»"},
        ],
        "vanlige_feil": [
            "Hever direkte ved kort forsinkelse — kan møte motargument om manglende vesentlighet",
            "Setter altfor kort tilleggsfrist — selgeren kan si fristen ikke var rimelig",
            "Hever i tilleggsfristen mens den løper — du må vente",
            "Glemmer at heving må meddeles innen rimelig tid (§ 29)",
        ],
        "hva_bor_du_html": """<p>Trygg fremgangsmåte:</p>
<ol>
<li>Skriftlig melding om forsinkelsen</li>
<li>Sett en konkret tilleggsfrist — for eksempel «10 dager fra i dag, frem til [dato]»</li>
<li>Si tydelig at du vil heve hvis varen ikke kommer innen fristen</li>
<li>Vent på fristen — ikke handle før den er ute</li>
<li>Send hevingsmelding så snart fristen er passert</li>
<li>Krev erstatning for konkrete tap i tillegg (§ 27)</li>
</ol>
<p>Hold alt på SMS, e-post eller chat — du trenger datoene som bevis.</p>""",
        "dumme_sporsmal": [
            {"q": "Hva er «rimelig» tilleggsfrist?", "a": "For standardvarer typisk 7–14 dager. For spesialvarer eller tilvirkning lenger. Som tommelregel: jo enklere det burde være å levere, jo kortere kan fristen være."},
            {"q": "Kan jeg heve hvis forsinkelsen «bare» er noen dager?", "a": "Sjelden uten tilleggsfrist — selgeren kan motsette seg at det er vesentlig. Med tilleggsfrist har du klar rett."},
            {"q": "Hva skjer når jeg hever?", "a": "Kjøpet faller bort. Du får tilbake det du har betalt. Selgeren får tilbake varen hvis den er levert. Du kan kreve erstatning i tillegg."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "22", "tittel": "Hva du kan kreve ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "29", "tittel": "Frist for å heve", "available": True},
            {"lov": "kjopsloven", "paragraf": "39", "tittel": "Heving ved mangel", "available": True},
        ],
    },
    # =============================================================
    # § 26 — Heving av tilvirkningskjøp
    # =============================================================
    {
        "number": "26",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Heving av tilvirkningskjøp",
        "description": "Får du laget noe spesielt for deg — og det blir forsinket — kan du heve bare hvis forsinkelsen ødelegger formålet med kjøpet.",
        "kort_svar": "Hvis du har bestilt noe som lages spesielt for deg — etter dine spesifikasjoner — er det vanskeligere å heve. Du kan bare heve hvis forsinkelsen gjør at formålet med kjøpet blir «vesentlig forfeilet». Loven beskytter produsenten, som ellers ville sittet med en spesialvare ingen andre vil ha.",
        "paragraftekst": """Gjelder kjøpet en ting som skal tilvirkes særskilt for kjøperen etter hans oppgaver eller ønsker, og kan selgeren derfor ikke uten vesentlig tap disponere tingen på annen måte, kan kjøperen bare heve dersom forsinkelsen medfører at hans formål med kjøpet blir vesentlig forfeilet.""",
        "hva_betyr_html": """<p>Når noen lager noe spesielt til deg — målbestilt sofa, gravert skilt, spesialtrykk T-skjorter, en CNC-kuttet del — sitter de igjen med noe ingen andre vil ha hvis du trekker deg. Loven beskytter dem mot urimelig heving.</p>
<p>Hovedregelen i § 25 om heving er strengere her. Du kan ikke heve bare fordi det er noen ukers forsinkelse, selv om du har satt tilleggsfrist. Du må kunne vise at formålet med kjøpet er «vesentlig forfeilet».</p>
<p><strong>Eksempler på når formålet er forfeilet:</strong></p>
<ul>
<li>Det er en bryllupskake, og bryllupet er forbi</li>
<li>Det er reklame for et arrangement som nå er over</li>
<li>Det er en bursdagsgave til en bestemt dato</li>
<li>Det er sesongvare som er gått ut av sesong</li>
</ul>
<p><strong>Eksempler på når det neppe er forfeilet:</strong></p>
<ul>
<li>Du synes bare det tar for lang tid</li>
<li>Du har funnet noe annet du vil ha</li>
<li>Det er en hjemmebrukt vare uten tidskritisk formål</li>
</ul>
<p>Loven krever altså to ting samtidig: at varen er tilvirket spesielt for deg (slik at selgeren ikke kan selge den til andre uten tap), og at formålet er vesentlig forfeilet.</p>""",
        "eksempler": [
            {"navn": "Sara", "tekst": "Sara har bestilt en bryllupskake fra en konditor for 12 000 kr, til levering 15. juni — selve bryllupsdagen. Det er 16. juni og det er fortsatt ingen kake. Formålet er åpenbart vesentlig forfeilet. Bryllupet er ferdig. Sara kan heve direkte etter § 26. Hun kan også kreve erstatning for kakene hun måtte improvisere."},
            {"navn": "Tom", "tekst": "Tom har bestilt et spesialtilpasset kjøkken for 280 000 kr, levering avtalt til 1. mai. Det er 1. juli — to måneder for sent. Hvis Tom bare er irritert over forsinkelsen, men kjøkkenet fortsatt vil tjene formålet (hjemme kjøkken), er det vanskelig å heve etter § 26. Hvis han derimot venter med å flytte inn fordi kjøkkenet ikke er ferdig, og dette koster ham i form av husleie eller arbeid — kan formålet være forfeilet. Han bør først sette tilleggsfrist og dokumentere konkret hvordan forsinkelsen rammer ham."},
        ],
        "vanlige_feil": [
            "Tror at vanlig § 25 om tilleggsfrist gjelder fullt ut for spesialvarer — det gjør den ikke",
            "Hever spesialbestilling uten å kunne vise at formålet er forfeilet — selgeren kan kreve betaling likevel",
            "Forveksler «kjedelig forsinkelse» med «vesentlig forfeilet formål»",
        ],
        "hva_bor_du_html": """<p><strong>Som kjøper:</strong></p>
<ul>
<li>Vurder om formålet faktisk er forfeilet — ikke bare om du er lei av å vente</li>
<li>Dokumenter formålet skriftlig før kjøpet — «skal brukes på arrangement X den dato Y»</li>
<li>Sett tilleggsfrist før du hever — det skader ikke posisjonen din</li>
<li>Hvis du hever på tynt grunnlag, kan selgeren kreve betaling for arbeidet</li>
</ul>
<p><strong>Som selger (tilvirker):</strong></p>
<ul>
<li>Avtal tydelig hvor lang leveringstid du trenger</li>
<li>Gi beskjed tidlig hvis du blir forsinket (§ 28)</li>
<li>Dokumenter arbeid utført og kostnader påløpt</li>
</ul>""",
        "related": [
            {"lov": "kjopsloven", "paragraf": "2", "tittel": "Tilvirkningskjøp", "available": True},
            {"lov": "kjopsloven", "paragraf": "22", "tittel": "Krav ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "25", "tittel": "Heving ved forsinkelse generelt", "available": True},
        ],
    },
    # =============================================================
    # § 27 — Erstatning ved forsinkelse
    # =============================================================
    {
        "number": "27",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Erstatning ved forsinkelse",
        "description": "Du kan kreve erstatning for tapet en forsinkelse har påført deg — med mindre selgeren kan dokumentere at årsaken lå helt utenfor hans kontroll.",
        "kort_svar": "Hvis selgerens forsinkelse koster deg penger, kan du kreve det erstattet. Selgeren slipper bare hvis han kan dokumentere at årsaken var en hindring helt utenfor hans kontroll — som han ikke kunne forutse eller unngå. Ordinære indirekte tap (driftsavbrudd, tapt fortjeneste) krever sterkere grunnlag. Hvis det er selgerens egen feil, kan du kreve erstatning uansett.",
        "paragraftekst": """(1) Kjøperen kan kreve erstatning for det tap han lider som følge av forsinkelse fra selgerens side. Dette gjelder likevel ikke så langt selgeren godtgjør at forsinkelsen skyldes hindring utenfor hans kontroll som han ikke med rimelighet kunne ventes å ha tatt i betraktning på avtaletiden eller å unngå eller overvinne følgene av.

(2) Beror forsinkelsen på en tredjemann som selgeren har gitt i oppdrag helt eller delvis å oppfylle kjøpet, er selgeren fri for ansvar bare om også tredjemann ville være fritatt etter regelen i første ledd. Det samme gjelder om forsinkelsen beror på en leverandør som selgeren har brukt, eller på noen annen i tidligere salgsledd.

(3) Ansvarsfrihet gjelder så lenge hindringen virker. Faller hindringen bort, kan ansvar gjøres gjeldende dersom selgeren da plikter å oppfylle men ikke gjør dette.

(4) Reglene foran i paragrafen her omfatter ikke slikt indirekte tap som nevnt i § 67 (2).

(5) Kjøperen kan i alle høve kreve erstatning dersom forsinkelsen eller tapet skyldes feil eller forsømmelse på selgerens side.""",
        "hva_betyr_html": """<p>Dette er en av de viktigste paragrafene i kjøpsloven. Den styrer når selgeren må betale for tapet du har hatt på grunn av forsinkelsen.</p>
<p><strong>Hovedregelen (første ledd):</strong> Du har krav på erstatning. Selgeren har strengt ansvar — han slipper bare hvis han kan vise at forsinkelsen skyldtes en hindring utenfor hans kontroll som han verken kunne forutse eller unngå. Dette kalles «kontrollansvar». Eksempler på hindringer som kan kvalifisere: naturkatastrofer, krig, streiker, alvorlig sykdom. Eksempler som ikke kvalifiserer: dårlig planlegging, normal sykdom, vanlige logistikkproblemer, økonomiske problemer.</p>
<p><strong>Underleverandører teller med (andre ledd):</strong> Selgeren kan ikke skylde på leverandørene sine. Hvis underleverandøren også ville hatt en gyldig unnskyldning, da slipper selgeren — ellers ikke. Du skal ikke straffes for at selgeren har valgt feil underleverandør.</p>
<p><strong>Hindring må fortsette (tredje ledd):</strong> Når hindringen er borte, må selgeren levere. Hvis han ikke gjør det, er ansvaret tilbake.</p>
<p><strong>Indirekte tap omfattes ikke (fjerde ledd):</strong> Dette er viktig. Konsekvenstap — driftsavbrudd, mistet fortjeneste, «tap fordi du ikke kunne bruke varen» — krever sterkere grunnlag (se § 67 (2)). Du får dekket direkte tap, ikke ringvirkningene.</p>
<p><strong>Unntak ved skyld (femte ledd):</strong> Hvis det er selgerens egen feil eller forsømmelse, gjelder ingen av begrensningene. Da kan du kreve full erstatning — også indirekte tap.</p>
<h3>Sammenligning: Hva får du dekket?</h3>
<table class="rule-table">
<thead><tr><th>Type tap</th><th>Direkte?</th><th>Krav om skyld?</th></tr></thead>
<tbody>
<tr><td>Mellomlegg på dekningskjøp</td><td>Ja</td><td>Nei (kontrollansvar holder)</td></tr>
<tr><td>Ekstra fraktkostnader</td><td>Ja</td><td>Nei</td></tr>
<tr><td>Lagerleie i ventetiden</td><td>Ja</td><td>Nei</td></tr>
<tr><td>Tapt fortjeneste fra mistet kontrakt</td><td>Indirekte</td><td>Ja (skyld må vises)</td></tr>
<tr><td>Driftsavbrudd</td><td>Indirekte</td><td>Ja</td></tr>
<tr><td>Tap fordi varen ikke kunne brukes</td><td>Indirekte</td><td>Ja</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Ola", "tekst": "Ola driver et lite verksted og hadde bestilt reservedeler for 18 000 kr. Selgeren leverer ikke i tide. Ola må kjøpe samme deler andre steder — for 22 000 kr. Mellomlegget på 4 000 kr er et direkte tap. Etter § 27 første ledd kan Ola kreve det erstattet, så lenge selgeren ikke kan vise en gyldig hindring. Vanlige logistikkproblemer hos selgeren holder ikke. Ola får dekket sine 4 000 kr."},
            {"navn": "Eva", "tekst": "Eva driver et lite designfirma og hadde bestilt utstyr for å levere et oppdrag. Utstyret kom tre uker for sent. Eva mistet oppdraget, verdt 80 000 kr i fortjeneste. Tapt fortjeneste fra mistet kontrakt er indirekte tap etter § 67 (2). Det dekkes ikke av første ledd i § 27. For å få dette erstattet må Eva kunne vise at selgeren har vært uaktsom — altså § 27 (5). Hvis hun kan, får hun det dekket — men det stilles strenge krav til å vise konkret skyld."},
        ],
        "vanlige_feil": [
            "Krever erstatning for alt — selv om mye er indirekte tap som krever skyld",
            "Som selger: tror «det var min leverandør sin feil» friker deg fra ansvar — det gjør det stort sett ikke",
            "Tror «kontrollansvar» betyr at selgeren slipper unna lett — det er motsatt: selgeren må bevise hindringen",
            "Glemmer plikten til å begrense eget tap (§ 70)",
        ],
        "hva_bor_du_html": """<p><strong>Dokumenter alt:</strong></p>
<ul>
<li>Datoer for forsinkelsen</li>
<li>Konkrete kostnader (kvitteringer, fakturaer)</li>
<li>Forsøk på dekningskjøp</li>
<li>Kommunikasjon med selger</li>
</ul>
<p><strong>Krev erstatning skriftlig:</strong></p>
<ul>
<li>Spesifiser hvert tap</li>
<li>Vis dokumentasjon</li>
<li>Sett betalingsfrist (typisk 14 dager)</li>
</ul>
<p><strong>Hvis selgeren nekter:</strong></p>
<ul>
<li>Forliksrådet for mindre beløp</li>
<li>Tingretten for større saker</li>
<li>Vurder smårettssaker — billig og enkelt</li>
</ul>""",
        "dumme_sporsmal": [
            {"q": "Selgeren sier «det er ikke vår skyld». Slipper han?", "a": "Det er ikke nok å si det — selgeren må dokumentere at det var en hindring utenfor hans kontroll. Bevisbyrden er hans, ikke din."},
            {"q": "Kan jeg kreve dekket «ergrelse» eller bortkastet tid?", "a": "Vanskelig. Erstatning forutsetter normalt økonomisk tap som kan dokumenteres."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "22", "tittel": "Krav ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "28", "tittel": "Opplysningsplikt om hindring", "available": True},
            {"lov": "kjopsloven", "paragraf": "67", "tittel": "Omfanget av erstatning", "available": False},
            {"lov": "kjopsloven", "paragraf": "70", "tittel": "Plikt til å begrense tap", "available": False},
        ],
    },
    # =============================================================
    # § 28 — Selgerens plikt til å varsle om forsinkelse
    # =============================================================
    {
        "number": "28",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Selgerens plikt til å varsle om forsinkelse",
        "description": "Når selgeren blir forsinket, må han gi deg beskjed innen rimelig tid. Får du ikke melding, kan du kreve dekket tap du kunne ha unngått.",
        "kort_svar": "Hvis selgeren blir hindret fra å levere i tide, må han si fra til deg om hindringen og hvordan den påvirker leveringen. Får du ikke beskjed innen rimelig tid etter at selgeren burde ha visst om problemet, kan du kreve dekket det tapet du kunne ha unngått hvis du hadde blitt varslet.",
        "paragraftekst": """Hindres selgeren å oppfylle kjøpet til rett tid, skal han gi kjøperen melding om hindringen og dens virkning på muligheten for å oppfylle. Får kjøperen ikke slik melding innen rimelig tid etter at selgeren fikk eller burde fått kjennskap til hindringen, kan kjøperen kreve erstattet tap som kunne vært unngått om han hadde fått meldingen i tide.""",
        "hva_betyr_html": """<p>Selgeren har en plikt: så snart han skjønner at varen kommer for sent, må han si fra. Og det må skje innen rimelig tid — ikke uken før avtalt leveringsdato, men når problemet faktisk oppstår.</p>
<p><strong>To deler:</strong></p>
<p><strong>1. Plikten:</strong> Si fra om hindringen og hvordan den påvirker leveringen. Du må få vite hva som skjer og hvor lenge det forventes å ta.</p>
<p><strong>2. Konsekvensen ved brudd:</strong> Hvis du ikke får beskjed i tide, kan du kreve erstattet det tapet du kunne ha unngått hvis du hadde fått beskjed. Tenk: hadde du visst at maskinen ble en måned forsinket, kunne du leid noe annet. Den ekstrakostnaden du fikk fordi du ventet i uvitenhet — kan du kreve dekket.</p>
<p>Dette gjelder uavhengig av om selgeren har gyldig grunn til forsinkelsen ellers (§ 27). Selv om selgeren slipper unna for selve forsinkelsen, kan han bli erstatningspliktig for at han ikke varslet i tide.</p>""",
        "eksempler": [
            {"navn": "Marius", "tekst": "Marius driver et lite firma som lager møbler. Han har bestilt eik fra en leverandør, levering avtalt 1. mars. Leverandøren får problemer i februar, men sier ingenting. Marius planlegger produksjon basert på 1. mars-levering og forplikter seg til en kundeordre. Først 5. mars sier leverandøren: «Vi får ikke levert før 1. mai.» Marius må nå rive opp planene, betale dagbot til sin kunde — 15 000 kr. Etter § 28 kan Marius kreve disse 15 000 kr erstattet. Hadde han fått beskjed i februar, kunne han ha endret planene tidlig og unngått dagboten."},
            {"navn": "Anne", "tekst": "Anne har bestilt en spesialdesignet lampe. Selgeren får beskjed fra produsenten 1. april om at det blir to ukers forsinkelse. Selgeren sender melding til Anne samme dag. Anne kan dermed gjøre sine egne tilpasninger og unngå unødvendige kostnader. Selgeren har oppfylt sin plikt etter § 28 og er ikke ansvarlig for tap Anne har kunne unngått ved riktig varsel."},
        ],
        "vanlige_feil": [
            "Som selger: tror du kan vente med varsel til siste øyeblikk — du må varsle innen rimelig tid etter du burde ha visst",
            "Som selger: tror manglende varsel ikke har konsekvens hvis du ellers har gyldig hindring — feil, du kan bli erstatningsansvarlig likevel",
            "Som kjøper: glemmer å dokumentere når selgeren faktisk varslet (eller burde ha varslet)",
            "Som kjøper: tror du ikke har krav fordi forsinkelsen var «uunngåelig» — du kan fortsatt ha krav på erstatning for manglende varsel",
        ],
        "hva_bor_du_html": """<p><strong>Som selger:</strong></p>
<ul>
<li>Følg med på leverandører og logistikk</li>
<li>Si fra så snart du ser at det kan glippe — ikke vent til datoen</li>
<li>Skriftlig melding er trygt</li>
<li>Forklar både hindringen og forventet ny tid</li>
</ul>
<p><strong>Som kjøper:</strong></p>
<ul>
<li>Hvis selgeren ikke gir lyd fra seg, ta kontakt selv — det dokumenterer kommunikasjonen</li>
<li>Når forsinkelsen oppdages, spør om når selgeren visste om problemet</li>
<li>Kalkuler hva du kunne ha unngått med tidligere varsel</li>
<li>Krev erstatning skriftlig</li>
</ul>""",
        "related": [
            {"lov": "kjopsloven", "paragraf": "22", "tittel": "Krav ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "27", "tittel": "Erstatning ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "58", "tittel": "Kjøperens opplysningsplikt", "available": False},
        ],
    },
    # =============================================================
    # § 29 — Frist for å heve etter for sen levering
    # =============================================================
    {
        "number": "29",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Frist for å heve etter for sen levering",
        "description": "Når varen først er levert — bare for sent — må du si fra om heving innen rimelig tid etter at du fikk vite om leveringen.",
        "kort_svar": "Hvis varen er levert — bare for sent — kan du fortsatt heve, men du må si fra til selgeren innen rimelig tid etter at du fikk vite om leveringen. Venter du for lenge med å si fra, taper du hevingsretten. Du beholder eventuelt erstatningskravet.",
        "paragraftekst": """Er tingen levert for seint kan kjøperen ikke heve kjøpet, med mindre han gir selgeren melding om kravet innen rimelig tid etter at han fikk vite om leveringen.""",
        "hva_betyr_html": """<p>Loven gir en klar tidsfrist for én bestemt situasjon: varen kom for sent, men den kom. Da må du raskt bestemme deg — skal du beholde den eller heve?</p>
<p>Logikken er enkel. Når selgeren først har levert, må han få vite raskt om du aksepterer leveringen eller ikke. Han kan ikke bli sittende i ukevis og lure på om kjøpet står ved makt.</p>
<p><strong>«Rimelig tid» avhenger av:</strong></p>
<ul>
<li>Hva slags vare det er</li>
<li>Om du har testet varen</li>
<li>Om du har hatt grunn til å nøle (for eksempel ferier)</li>
<li>Hva som er normalt i bransjen</li>
</ul>
<p>For en vanlig privat handel: dager til en uke eller to er normalt rimelig. Lenger blir risikabelt.</p>
<p><strong>Viktig:</strong> Dette gjelder kun heving. Selv om du mister hevingsretten, kan du fortsatt kreve erstatning for konkrete tap forsinkelsen påførte deg (§ 27).</p>""",
        "eksempler": [
            {"navn": "Petter", "tekst": "Petter har bestilt en racersykkel for 38 000 kr, levering avtalt 1. april. Sykkelen kommer først 15. mai — seks uker for sent. Petter er irritert, men pakker den ut og begynner å bruke den. Tre uker senere blir han enda mer irritert og sender melding: «Jeg hever kjøpet». For sent. Etter § 29 må Petter ha sagt fra innen rimelig tid etter at han fikk vite om leveringen. Tre uker mens han brukte sykkelen er for lenge. Han kan beholde sykkelen og kreve erstatning for konkrete tap — men ikke heve."},
            {"navn": "Sara", "tekst": "Sara hadde bestilt en oppvaskmaskin med avtalt levering 10. mai. Den kommer 5. juni. Sara har i mellomtiden kjøpt en annen. Hun pakker ikke opp, og sender beskjed samme dag: «Jeg hever kjøpet — leveringen er for sen, og jeg har skaffet meg annet.» Sara har handlet innen rimelig tid (samme dag) og kan heve. Selgeren må hente maskinen tilbake og betale tilbake det Sara har betalt."},
        ],
        "vanlige_feil": [
            "Tror du har all verden av tid til å bestemme deg — du har ikke det",
            "Begynner å bruke varen og krever heving etterpå — det signaliserer aksept",
            "Glemmer å sende skriftlig melding — muntlige beskjeder er vanskelig å bevise",
            "Tror du ikke har noe igjen hvis du mister hevingsretten — erstatningskravet står",
        ],
        "hva_bor_du_html": """<p>Når varen kommer for sent:</p>
<ul>
<li>Ikke pakk opp og bruk varen hvis du vurderer heving</li>
<li>Ta beslutningen raskt — ideelt innen få dager</li>
<li>Skriv tydelig: «Jeg hever kjøpet på grunn av forsinkelsen. Jeg krever pengene tilbake.»</li>
<li>Ta vare på alt skriftlig — melding, dato, bevis på at varen kom for sent</li>
<li>Krev fortsatt erstatning for konkrete tap</li>
</ul>""",
        "dumme_sporsmal": [
            {"q": "Hvor lenge er «rimelig tid»?", "a": "For mest hverdagslige varer: dager til en uke. For komplekse varer som krever testing: noe lenger. Som regel er det best å være rask — ikke vente."},
            {"q": "Mister jeg alt hvis jeg er for sen?", "a": "Du mister bare hevingsretten. Erstatningskravet for konkrete tap består."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "22", "tittel": "Krav ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "25", "tittel": "Heving ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "39", "tittel": "Heving ved mangel", "available": True},
        ],
    },
    # =============================================================
    # § 30 — Hva du kan kreve ved mangel (SENTRALPARAGRAF)
    # =============================================================
    {
        "number": "30",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Hva du kan kreve ved mangel",
        "description": "Har varen mangel? Du kan kreve retting, omlevering, prisavslag, heving, erstatning og holde tilbake betaling. Alle krav kan kombineres.",
        "kort_svar": "Når varen har mangel, har du seks mulige reaksjoner: kreve retting, kreve omlevering, kreve prisavslag, heve kjøpet, kreve erstatning, og holde tilbake betalingen. Du kan kombinere dem. Å kreve én ting stenger ikke for å kreve noe annet — særlig ikke erstatning, som alltid kan komme i tillegg.",
        "paragraftekst": """(1) Dersom det foreligger mangel og denne ikke skyldes kjøperen eller forhold på hans side, kan han etter §§ 31 til 40 kreve retting, omlevering, prisavslag, heving og erstatning samt holde kjøpesummen tilbake etter § 42. Hans rett til erstatning faller ikke bort ved at han gjør gjeldende andre krav eller ved at disse ikke kan gjøres gjeldende.

(2) For andre feil ved selgerens oppfyllelse gjelder reglene om mangler så langt de passer.""",
        "hva_betyr_html": """<p>Dette er sentralparagrafen for alt som handler om mangler. Når varen ikke er som den skulle (etter § 17, § 18 eller § 19), gir loven deg seks verktøy:</p>
<p><strong>1. Retting (§ 34):</strong> Selgeren reparerer feilen. Du beholder varen.</p>
<p><strong>2. Omlevering (§ 34):</strong> Selgeren gir deg en ny vare. Den gamle går tilbake.</p>
<p><strong>3. Prisavslag (§ 38):</strong> Du beholder varen, men betaler mindre — proporsjonalt med hvor mye dårligere varen er.</p>
<p><strong>4. Heving (§ 39):</strong> Kjøpet kanselleres. Du gir tilbake varen, får tilbake pengene.</p>
<p><strong>5. Erstatning (§ 40):</strong> Du får dekket konkrete tap forårsaket av mangelen — uavhengig av om du krever noe annet.</p>
<p><strong>6. Hold tilbake betaling (§ 42):</strong> Hvis du ikke har betalt fullt ut, kan du holde tilbake nok til å sikre dine krav.</p>
<p><strong>Kombiner fritt:</strong> Erstatning kan alltid komme i tillegg til andre krav. Hvis selgeren retter, men du har hatt konkrete tap, kan du fortsatt kreve dem dekket.</p>
<p><strong>Andre feil teller også (andre ledd):</strong> Hvis selgeren har misligholdt annet enn akkurat varens egenskaper — for eksempel mangler dokumentasjon, garantipapirer, instruksjonsmanual eller annet som hører med — gjelder reglene «så langt de passer».</p>
<h3>Sammenligning: Hvilket krav passer best?</h3>
<table class="rule-table">
<thead><tr><th>Situasjon</th><th>Beste krav</th></tr></thead>
<tbody>
<tr><td>Varen virker, men har mindre feil</td><td>Prisavslag eller retting</td></tr>
<tr><td>Varen virker ikke, kan rettes</td><td>Retting</td></tr>
<tr><td>Varen er feilprodusert hele veien</td><td>Omlevering</td></tr>
<tr><td>Mangelen er så stor at varen er ubrukelig</td><td>Heving</td></tr>
<tr><td>Mangelen ga deg konkrete kostnader</td><td>Erstatning (i tillegg)</td></tr>
<tr><td>Du har ennå ikke betalt</td><td>Hold tilbake (i tillegg)</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Tom", "tekst": "Tom har kjøpt en racersykkel for 45 000 kr fra en privat selger. Det viser seg at giringssystemet er ødelagt. Reparasjon koster 8 000 kr. Tom har flere valg: retting (krev at selgeren betaler reparasjonen), prisavslag (krev 8 000 kr i prisavslag og fiks selv), heving (vanskelig hvis mangelen ikke er vesentlig), eller erstatning (krev dekket ekstrakostnader for eksempel om han måtte leie sykkel mens reparasjonen pågikk). Det praktiske er ofte prisavslag eller retting. Tom kan også kombinere — for eksempel retting + erstatning for leiekostnad."},
            {"navn": "Anne", "tekst": "Anne kjøper en sofa der avtalen inkluderte armbeskytter. Sofaen kommer uten. Det er ikke «feil ved varen» som sådan, men en manglende komponent. Etter § 30 (2) gjelder mangelsreglene «så langt de passer». Anne kan kreve oppfyllelse (manglende del levert), prisavslag (hvis den ikke kan skaffes), eller eventuelt heving hvis sofaen ikke fyller funksjonen sin uten den."},
        ],
        "vanlige_feil": [
            "Tror du må velge ett krav — du kan kombinere",
            "Reklamerer for sent (§ 32 om reklamasjonsfrist)",
            "Glemmer å kreve erstatning som tillegg",
            "Krever heving for små feil — det krever vesentlig mangel",
            "Tror «retting» må selgeren godta — selgeren har faktisk rett til å rette først (§ 36)",
        ],
        "hva_bor_du_html": """<p>Steg for steg ved mangel:</p>
<ol>
<li>Reklamer raskt (§ 32): skriftlig melding om hva som er galt</li>
<li>Velg krav: hva passer best i din situasjon</li>
<li>Gi selgeren mulighet til å rette/omlevere (§ 36 — selgeren har en viss rett til det)</li>
<li>Hold tilbake betaling så langt du har krav</li>
<li>Dokumenter alt: bilder, kvitteringer, kommunikasjon</li>
<li>Krev erstatning for konkrete tap</li>
</ol>
<p>Vanlig kombinasjon: retting + erstatning, eller prisavslag + erstatning.</p>""",
        "dumme_sporsmal": [
            {"q": "Kan jeg bare bli ferdig med selgeren og kjøpe nytt et annet sted?", "a": "Ja — det er heving. Men du må vise at mangelen er vesentlig, eller ha gitt selgeren mulighet til retting først. Og selgeren har normalt rett til å forsøke å rette før du kan heve."},
            {"q": "Får jeg full erstatning hvis varen var dyr?", "a": "Du får erstatning for tapet du har hatt, ikke for varens pris. Pris får du tilbake ved heving — erstatning er for det som kom på toppen."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "32", "tittel": "Reklamasjonsfrister", "available": True},
            {"lov": "kjopsloven", "paragraf": "34", "tittel": "Retting og omlevering", "available": True},
            {"lov": "kjopsloven", "paragraf": "38", "tittel": "Prisavslag", "available": True},
            {"lov": "kjopsloven", "paragraf": "39", "tittel": "Heving ved mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "40", "tittel": "Erstatning ved mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "42", "tittel": "Tilbakeholdsrett", "available": True},
        ],
    },
]
