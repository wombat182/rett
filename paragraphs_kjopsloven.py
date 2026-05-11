"""Rettsregel: Kjøpsloven §§ 1-20 (hopper over § 4 som er om forbrukerkjøp)."""

PARAGRAPHS = [
    {
        "number": "1",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Når gjelder kjøpsloven?",
        "description": "Kjøpsloven styrer kjøp mellom privatpersoner og mellom firmaer. Handler du i butikk gjelder forbrukerkjøpsloven. For bolig gjelder avhendingslova.",
        "kort_svar": "Kjøpsloven gjelder når du kjøper eller selger en ting — så lenge ingen annen lov tar over. Den gjelder typisk mellom privatpersoner (Finn.no-handel) eller mellom firmaer. Kjøper du noe fra en butikk som forbruker, gjelder forbrukerkjøpsloven i stedet. For hus og leilighet gjelder avhendingslova.",
        "paragraftekst": """(1) Loven gjelder kjøp for så vidt ikke annet er fastsatt i lov. For forbrukerkjøp gjelder forbrukerkjøpsloven. For kjøp av fast eiendom gjelder avhendingslova.

(2) Loven gjelder også bytte av ting så langt den passer.""",
        "hva_betyr_html": """<p>Kjøpsloven er reglene for hvordan en handel skal foregå når du kjøper eller selger noe. Men den er litt som en reservelov — den trer inn der ingen annen lov gjelder.</p>
<p><strong>Tre situasjoner du må holde fra hverandre:</strong></p>
<ul>
<li><strong>Privatkjøp</strong> (du selger ting på Finn.no, kjøper sykkel av naboen): Kjøpsloven gjelder.</li>
<li><strong>Forbrukerkjøp</strong> (du kjøper en TV på Power, klær på H&amp;M): Forbrukerkjøpsloven gjelder. Den gir deg bedre beskyttelse.</li>
<li><strong>Bolig</strong> (du kjøper eller selger hytte, leilighet, hus): Avhendingslova gjelder.</li>
</ul>
<p>Andre ledd sier at hvis du bytter ting (du gir bort skien din mot en snowboard), bruker du de samme reglene som ved kjøp — så langt det passer.</p>
<h3>Sammenligning: Hvilken lov gjelder?</h3>
<table class="rule-table">
<thead><tr><th>Situasjon</th><th>Lov</th></tr></thead>
<tbody>
<tr><td>Du selger sykkel til naboen</td><td>Kjøpsloven</td></tr>
<tr><td>Bedriften kjøper kontorstoler fra annen bedrift</td><td>Kjøpsloven</td></tr>
<tr><td>Du kjøper sofa hos IKEA</td><td>Forbrukerkjøpsloven</td></tr>
<tr><td>Du kjøper hytte</td><td>Avhendingslova</td></tr>
<tr><td>Du bytter ski mot snowboard med en venn</td><td>Kjøpsloven</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Petter", "tekst": "Petter selger sin gamle Suzuki til Lars via Finn.no for 35 000 kr. To uker senere stopper motoren. Lars vil ha pengene tilbake. Her gjelder kjøpsloven, ikke forbrukerkjøpsloven. Det betyr at Lars må undersøke om Petter var klar over feilen, om sykkelen var i vesentlig dårligere stand enn prisen tilsa, eller om noe ble fortiet. Det er strengere krav for kjøperen i privatkjøp enn når du handler i butikk."},
            {"navn": "Kari", "tekst": "Kari kjøper ny komfyr fra Elkjøp. Den virker ikke. Her gjelder forbrukerkjøpsloven, og hun har sterkere rettigheter: 5 års reklamasjonsfrist, og selgeren må bevise at feilen ikke var der fra start hvis den dukker opp innen 6 måneder."},
        ],
        "vanlige_feil": [
            "Tror du har 5 års reklamasjonsfrist når du har kjøpt brukt av en privatperson (du har 2 år etter kjøpsloven)",
            "Bruker kjøpsloven på leilighetskjøpet — avhendingslova har egne regler",
            "Tror du kan klage til Forbrukertilsynet etter et Finn.no-kjøp (det kan du ikke — der må du gå rettens vei eller via Forbrukerrådet sin mekling)",
        ],
        "hva_bor_du_html": """<p>Før du krangler om en handel: finn ut hvilken lov som gjelder. Spør deg selv:</p>
<ul>
<li>Kjøpte du av en bedrift som forbruker? → Forbrukerkjøpsloven</li>
<li>Kjøpte du av en annen privatperson? → Kjøpsloven</li>
<li>Er det en bolig eller eiendom? → Avhendingslova</li>
</ul>
<p>Reglene er forskjellige nok til at svaret avgjør hva du kan kreve.</p>""",
        "dumme_sporsmal": [
            {"q": "Kan jeg klage til Finn.no hvis sykkelen jeg kjøpte var ødelagt?", "a": "Nei, Finn.no er bare en markedsplass. Du må forholde deg direkte til selgeren etter kjøpsloven."},
            {"q": "Gjelder kjøpsloven hvis jeg kjøper noe fra en bedrift som ikke er butikk?", "a": "Hvis du kjøper som privatperson og selgeren driver næring, er det forbrukerkjøp uansett om butikken er en nettside, et lager eller en mann med varebil."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "2", "tittel": "Tilvirkingskjøp og tjenester", "available": True},
            {"lov": "kjopsloven", "paragraf": "3", "tittel": "Når avtale går foran loven", "available": True},
            {"lov": "kjopsloven", "paragraf": "5", "tittel": "Internasjonale kjøp", "available": True},
            {"lov": "forbrukerkjopsloven", "paragraf": "1", "tittel": "Når den loven gjelder", "available": False},
            {"lov": "avhendingslova", "paragraf": "1-1", "tittel": "Salg av fast eiendom", "available": False},
        ],
    },
    {
        "number": "2",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Tilvirkingskjøp og tjenester",
        "description": "Er det kjøp eller tjeneste? Hvis du bestiller noe som skal lages spesielt for deg, gjelder kjøpsloven — men ikke hvis arbeidet er hovedsaken.",
        "kort_svar": "Bestiller du noe som skal lages for deg — skreddersydd dress, spesialbygd hylle, en kake til bryllupet — er det kjøp etter kjøpsloven, så lenge produsenten holder materialene. Men hvis det meste av jobben er arbeid og ikke vare, blir det en tjeneste i stedet. Bygging av hus eller hytte er aldri kjøp.",
        "paragraftekst": """(1) Loven gjelder bestilling av ting som skal tilvirkes, når ikke den som bestiller skal skaffe en vesentlig del av materialet. Loven gjelder ikke avtale om oppføring av bygning eller annet anlegg på fast eiendom.

(2) Loven gjelder ikke avtale som pålegger den part som skal levere tingen, også å utføre arbeid eller annen tjeneste, og dette utgjør den overveiende del av hans forpliktelser.""",
        "hva_betyr_html": """<p>Loven svarer på et grenseproblem: når er noe et kjøp, og når er det en tjeneste? Det avgjør hvilke regler som gjelder hvis det går galt.</p>
<p><strong>Første ledd</strong> sier: bestiller du noe som skal lages spesielt, regnes det fortsatt som kjøp — så lenge selgeren skaffer det meste av materialet selv. Bare hvis du stiller med materialene, faller det utenfor kjøpsloven.</p>
<p>Men: hus, hytte og andre byggverk på tomten din regnes aldri som kjøp. Der gjelder bustadoppføringslova (hvis du er forbruker) eller en av entrepriselovene.</p>
<p><strong>Andre ledd</strong> sier: hvis arbeid og tjeneste er hovedsaken, og varen bare er en del, gjelder ikke kjøpsloven. Da gjelder håndverkertjenesteloven eller annen tjenestelov i stedet.</p>
<p>Tommelfingerregelen: er det mest vare eller mest arbeid?</p>
<h3>Sammenligning: Kjøp eller tjeneste?</h3>
<table class="rule-table">
<thead><tr><th>Bestilling</th><th>Hva gjelder?</th></tr></thead>
<tbody>
<tr><td>Skreddersydd dress (skredderen har stoffet)</td><td>Kjøpsloven</td></tr>
<tr><td>Spesialbygd kjøkken hos snekker</td><td>Kjøpsloven (vare er hovedsaken)</td></tr>
<tr><td>Tilbygg på huset</td><td>Bustadoppføringslova / entrepriselovene</td></tr>
<tr><td>Maleren maler huset ditt</td><td>Håndverkertjenesteloven</td></tr>
<tr><td>Konditor lager bursdagskake</td><td>Kjøpsloven</td></tr>
<tr><td>Frisøren klipper deg</td><td>Håndverkertjenesteloven / forbrukertjenester</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Ingrid", "tekst": "Ingrid bestiller en stor bryllupskake hos en konditor for 8 500 kr. Konditoren bruker egne ingredienser og dekorerer den etter Ingrids ønsker. Når kaken kommer er den feil farge og smaker rart. Dette er et tilvirkingskjøp etter § 2 første ledd — konditoren leverte både vare og arbeid, men varen (kaken) er hovedsaken. Kjøpsloven gjelder. Ingrid kan kreve prisavslag, omlevering eller heving etter §§ 30 og utover."},
            {"navn": "Tom", "tekst": "Tom hyrer en rørlegger for å pusse opp badet. Rørleggeren leverer rørene og fliser for 25 000 kr, men selve arbeidet koster 80 000 kr. Til sammen 105 000 kr. Her er arbeidet hovedsaken. Kjøpsloven gjelder ikke — det er håndverkertjenesteloven som styrer."},
        ],
        "vanlige_feil": [
            "Tror kjøpsloven gjelder når du har hyret håndverker — den gjør stort sett ikke det",
            "Bruker kjøpsloven på avtale om husbygging — det er et eget regelverk",
            "Krever omlevering etter kjøpsloven når det egentlig er en tjeneste — gå da etter retting eller prisavslag i håndverkertjenesteloven",
        ],
        "hva_bor_du_html": """<p>Når du har en konflikt med noen som har laget noe for deg: spør deg selv om vare eller arbeid er hovedsaken.</p>
<ul>
<li>Mer enn halvparten vare → kjøpsloven (og se § 26 for heving av tilvirkningskjøp)</li>
<li>Mer enn halvparten arbeid → håndverkertjenesteloven eller liknende</li>
<li>Bygging på fast eiendom → bustadoppføringslova / entrepriselovene</li>
</ul>
<p>Reglene minner om hverandre, men reklamasjonsfrister og rettigheter er ulike.</p>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "1", "tittel": "Når gjelder kjøpsloven generelt", "available": True},
            {"lov": "kjopsloven", "paragraf": "3", "tittel": "Når avtalen går foran loven", "available": True},
            {"lov": "kjopsloven", "paragraf": "26", "tittel": "Heving av tilvirkningskjøp", "available": False},
            {"lov": "haandverkertjenesteloven", "paragraf": "1", "tittel": "Når den gjelder", "available": False},
        ],
    },
    {
        "number": "3",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Avtalen går foran loven",
        "description": "Kan dere avtale dere bort fra kjøpsloven? Ja, det meste. Hva dere har skrevet i avtalen — eller pleier å gjøre — gjelder oftest foran loven.",
        "kort_svar": "Det dere har avtalt — skriftlig eller muntlig — går foran kjøpsloven. Det samme gjør faste rutiner mellom dere fra tidligere, og handelsbruk i bransjen. Loven er bare et sikkerhetsnett som fyller hullene der avtalen er stille.",
        "paragraftekst": "Bestemmelsene i loven gjelder ikke for så vidt annet følger av avtalen, etablert praksis mellom partene, eller handelsbruk eller annen sedvane som må anses bindende mellom partene.",
        "hva_betyr_html": """<p>Kjøpsloven er en såkalt "fravikelig" lov. Det betyr at dere som handler kan bli enige om andre regler enn de loven setter — og da gjelder avtalen.</p>
<p><strong>Tre ting kan slå loven:</strong></p>
<ol>
<li><strong>Avtalen mellom dere.</strong> Det dere ble enige om da kjøpet ble inngått.</li>
<li><strong>Etablert praksis mellom dere.</strong> Hvis du og samme leverandør har handlet i fem år og alltid gjort det på en bestemt måte, blir den måten bindende — selv om dere aldri har skrevet det ned.</li>
<li><strong>Handelsbruk eller sedvane.</strong> I bransjer som handler mye seg imellom oppstår faste skikker. Hvis en skikk er så vanlig at "alle" i bransjen følger den, kan den binde dere selv om dere aldri har snakket om den.</li>
</ol>
<p><strong>Viktig forskjell fra forbrukerkjøp:</strong> I forbrukerkjøpsloven kan dere ikke avtale dere bort fra kjøperens rettigheter. I kjøpsloven kan dere det. Det er derfor det er ekstra viktig å lese kontrakten når du selger eller kjøper privat eller som bedrift.</p>""",
        "eksempler": [
            {"navn": "Sara", "tekst": "Sara selger sin gamle Volvo til Marius via Finn.no. I annonsen står det «selges som den er, prøvekjøring anbefales». Marius prøvekjører, kjøper for 45 000 kr og oppdager senere at clutchen er på vei ut. «Som den er» er en avtaleklausul, og kjøpsloven godtar sånne forbehold (se § 19). Marius kan ikke kreve like mye som ved et standardkjøp — han kan bare gjøre mangel gjeldende hvis bilen er i vesentlig dårligere stand enn prisen tilsa, eller hvis Sara har holdt tilbake informasjon."},
            {"navn": "Lars", "tekst": "Lars driver en liten kafé og har handlet kaffebønner fra samme rosteri i tre år. De har alltid avtalt at Lars kan reklamere på dårlige bønner innen 7 dager. Det står ikke i noen kontrakt — det er bare sånn det har vært. Denne praksisen er bindende etter § 3, selv om kjøpsloven har andre frister. Rosteriet kan ikke plutselig si «du må reklamere innen 24 timer» — den nye regelen må avtales på nytt."},
        ],
        "vanlige_feil": [
            "Tror muntlige avtaler ikke teller — de gjør det, men de er vanskeligere å bevise",
            "Glemmer å lese kontrakten før de signerer",
            "Tror handelsbruk gjelder også for forbrukere — det gjør det normalt ikke når det går ut over forbrukerens rettigheter",
            "Setter likhetstegn mellom «vi pleier» og «vi har avtalt» — praksis må ha vart en stund og være tydelig",
        ],
        "hva_bor_du_html": """<p>Hvis du ikke leser kontrakten godt nok og signerer noe som svekker dine rettigheter, er du normalt bundet av det. Du kan ikke etterpå si «jeg trodde kjøpsloven gjaldt». Det er bare hvis avtalen er åpenbart urimelig (jf. avtaleloven § 36) at den kan settes til side.</p>
<ul>
<li>Les hele kontrakten før du signerer — særlig "småskrift" om reklamasjon, ansvar og leveringstid</li>
<li>Skriv ned det dere har avtalt muntlig hvis kjøpet er stort</li>
<li>Spør om bransjen har bestemte rutiner du bør kjenne til</li>
<li>Som selger: vær tydelig på forbehold før kjøpet, ikke etter</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "1", "tittel": "Når gjelder loven", "available": True},
            {"lov": "kjopsloven", "paragraf": "9", "tittel": "Leveringstid når avtalen er stille", "available": True},
            {"lov": "kjopsloven", "paragraf": "19", "tittel": "Ting solgt «som den er»", "available": True},
            {"lov": "kjopsloven", "paragraf": "45", "tittel": "Pris når avtalen er stille", "available": False},
        ],
    },
    {
        "number": "5",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Internasjonale kjøp",
        "description": "Når du kjøper varer fra utlandet som bedrift, gjelder ofte FN-konvensjonen om internasjonale løsørekjøp — ikke vanlig norsk kjøpsrett.",
        "kort_svar": "Når en norsk bedrift kjøper varer fra utlandet, gjelder normalt FN-konvensjonen om internasjonale løsørekjøp (CISG) — ikke vanlig norsk kjøpsrett. Men hvis handelen er mellom Norden (Norge, Sverige, Danmark, Finland, Island), gjelder vanlig kjøpslov.",
        "paragraftekst": "For kjøp som er omfattet av virkeområdet for FN-konvensjonen 11. april 1980 om kontrakter for internasjonale løsørekjøp, gjelder lovens kapittel XV. Dette gjelder ikke kjøp der selgeren har forretningsstedet i Norge, Danmark, Finland, Island eller Sverige og kjøperen har forretningsstedet i et annet av disse landene (nordisk kjøp).",
        "hva_betyr_html": """<p>Når en norsk bedrift kjøper noe fra et firma i et annet land, kan ikke begge sider bare bruke sin egen lov — det blir kaos. Derfor har FN laget en felles regelbok som kalles CISG (United Nations Convention on Contracts for the International Sale of Goods).</p>
<p><strong>Tre ting du må vite:</strong></p>
<ol>
<li><strong>Når CISG gjelder:</strong> Når selger og kjøper holder til i forskjellige land som har godtatt konvensjonen — Tyskland, USA, Kina og 90+ andre land. Da går denne foran vanlig kjøpslov.</li>
<li><strong>Norden er et unntak:</strong> Norge, Sverige, Danmark, Finland og Island har valgt å bruke vanlig nasjonal kjøpslov seg imellom, ikke CISG.</li>
<li><strong>Forbrukerkjøp er ikke med:</strong> CISG gjelder bare når begge parter er næringsdrivende.</li>
</ol>
<p>I praksis: Hvis du driver firma og kjøper maskiner fra Tyskland, gjelder CISG. Kjøper du fra Sverige, gjelder vanlig kjøpslov.</p>""",
        "eksempler": [
            {"navn": "Anne", "tekst": "Anne driver et lite tre-foredlingsfirma og bestiller en CNC-fres fra en tysk produsent for 350 000 kr. Maskinen kommer med en feil i styringssystemet. Her gjelder CISG (FN-konvensjonen), ikke vanlig norsk kjøpslov. Reglene minner mye om kjøpsloven — Anne kan kreve retting, prisavslag, heving, erstatning — men fristene og enkelte vilkår er litt annerledes. Det står i kjøpsloven kapittel XV, som tar inn CISG som norsk lov."},
            {"navn": "Ola", "tekst": "Ola driver en sportsbutikk og bestiller hjelmer fra en svensk leverandør. Her gjelder vanlig norsk kjøpslov (eller svensk om dere har avtalt det) — ikke CISG. Det er fordi handelen er mellom to nordiske land."},
        ],
        "vanlige_feil": [
            "Tror CISG også gjelder forbrukerkjøp — den gjelder bare mellom næringsdrivende",
            "Glemmer at avtalen kan velge bort CISG — partene kan avtale at norsk lov skal gjelde isteden",
            "Tror reglene er identiske med kjøpsloven — de er like, men ikke identiske",
            "Vet ikke hvilket lands rett som gjelder ved tvist — sjekk lovvalgsklausulen i kontrakten",
        ],
        "hva_bor_du_html": """<p>Når du handler over landegrensene som bedrift:</p>
<ul>
<li>Sjekk lovvalg i kontrakten — hva slags lov er valgt?</li>
<li>Vurder om CISG passer dere — den kan velges bort om dere vil ha vanlig norsk lov</li>
<li>Avtal verneting — hvor skal en eventuell tvist løses?</li>
<li>Lag tydelige leveringsvilkår — bruk Incoterms (FOB, CIF, DAP osv.) så ansvar for transport og forsikring er klart</li>
</ul>
<p>For større handler: snakk med en advokat før kontrakten signeres. CISG har fallgruver som kan koste mye.</p>""",
        "dumme_sporsmal": [
            {"q": "Gjelder CISG hvis jeg bestiller fra Wish eller AliExpress?", "a": "Da er du som regel forbruker, ikke næringsdrivende, og CISG gjelder ikke. Men du har heller ikke alltid full forbrukerkjøpsbeskyttelse — det avhenger av selgerens hjemland og hvor enkel den er å gå løs på."},
            {"q": "Kan vi avtale at norsk lov skal gjelde selv om vi handler med et tysk firma?", "a": "Ja. Dere kan både velge norsk lov og velge bort CISG. Det må stå tydelig i kontrakten."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "1", "tittel": "Generelt virkeområde", "available": True},
            {"lov": "kjopsloven", "paragraf": "87", "tittel": "FN-konvensjonen som norsk lov", "available": False},
            {"lov": "kjopsloven", "paragraf": "3", "tittel": "Avtale går foran loven", "available": True},
        ],
    },
    {
        "number": "6",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Hentekjøp",
        "description": "Skal du hente varen selv? Da er den levert først når du har overtatt den fysisk. Selgeren skal holde den klar på sitt forretningssted eller bosted.",
        "kort_svar": "Et hentekjøp er når du som kjøper henter varen selv. Da er varen \"levert\" først når du har overtatt den. Selgeren skal holde den klar på sitt forretningssted — eller der det var avtalt at den ligger.",
        "paragraftekst": """(1) Tingen skal holdes klar for henting på det sted der selgeren hadde sitt forretningssted (i tilfelle bosted jf § 83) da kjøpet ble inngått. Visste partene ved kjøpet at tingen eller det vareparti eller produksjonssted som tingen skal tas fra, var på et annet sted, skal tingen holdes klar for henting der.

(2) Tingen er levert når den er overtatt av kjøperen.""",
        "hva_betyr_html": """<p>Hentekjøp er hovedregelen i kjøpsloven. Hvis dere ikke har avtalt noe annet, regnes det som at kjøperen skal hente.</p>
<p><strong>Loven svarer på to spørsmål:</strong></p>
<p><strong>Hvor skal varen hentes?</strong> Som hovedregel hos selgeren — der bedriften eller personen holder til. Men: hvis dere visste ved avtaleinngåelsen at varen lå et annet sted (på et lager, på en gård, hos en underleverandør), er det det stedet som gjelder.</p>
<p><strong>Når er varen "levert"?</strong> Først når du fysisk har tatt den med deg. Dette har stor betydning for risiko (§ 13): det er først ved henting at ansvaret for varen går over fra selger til kjøper. Brenner selgerens lager kvelden før du henter, er det selgerens problem — ikke ditt.</p>""",
        "eksempler": [
            {"navn": "Eva", "tekst": "Eva kjøper en brukt symaskin fra Petter via Finn.no for 4 500 kr. Petter bor i Drammen og maskinen står på loftet hans. Eva bor i Oslo og avtaler at hun kommer og henter neste lørdag. Mellom kjøp og henting er det Petter som har risikoen for maskinen. Hvis det blir innbrudd i huset hans, eller hvis loftet brenner, må han enten skaffe en tilsvarende maskin eller betale Eva tilbake. Risikoen går først over på Eva når hun har lastet maskinen i bilen og kjørt avgårde."},
            {"navn": "Marius", "tekst": "Marius driver et lite gartneri og kjøper en brukt traktor fra et landbruksfirma i Oslo. Begge vet at traktoren står på en gård i Hedmark. Da skal Marius hente den der — ikke i Oslo. Det står ikke i avtalen, men det fulgte av det partene visste på kjøpstidspunktet."},
        ],
        "vanlige_feil": [
            "Tror selgeren har ansvaret helt frem til du har fått varen hjem — risikoen flytter seg når du faktisk overtar",
            "Forutsetter at varen kan hentes hvor som helst — som hovedregel er det selgerens adresse",
            "Henter ikke i tide og blir overrasket når selgeren krever betaling likevel (§ 13 andre ledd: risikoen kan gå over hvis du er sen)",
        ],
        "hva_bor_du_html": """<p>Hvis du som kjøper ikke henter når du skulle, kan risikoen gå over på deg likevel (§ 13). Da må du betale selv om varen skulle gå tapt mens den ventet. I tillegg kan selgeren kreve erstatning for sin ulempe (§ 55 og § 57).</p>
<ul>
<li>Avtal tydelig hvor varen skal hentes — særlig hvis den ikke ligger der selgeren bor</li>
<li>Avtal tidspunkt — eller kom raskt, så risikoen flytter seg</li>
<li>Sjekk varen ved henting før du drar — det er din siste sjanse før risikoen blir din</li>
<li>Få kvittering på at varen er overtatt, og når</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "7", "tittel": "Plasskjøp og sendekjøp", "available": True},
            {"lov": "kjopsloven", "paragraf": "9", "tittel": "Når skal varen leveres", "available": True},
            {"lov": "kjopsloven", "paragraf": "13", "tittel": "Når går risikoen over", "available": True},
            {"lov": "kjopsloven", "paragraf": "50", "tittel": "Kjøperens plikt til å hente", "available": False},
        ],
    },
    {
        "number": "7",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Plasskjøp og sendekjøp",
        "description": "Skal varen sendes til deg? Da er den «levert» når den er overgitt til transportøren — ikke når den kommer fram. Det avgjør hvem som har risikoen.",
        "kort_svar": "Skal varen leveres til deg av selgeren selv eller hans bud (plasskjøp), er den levert når du får den. Skal den sendes med fraktfører — Posten, Bring, transportfirma — er den levert allerede når selgeren overgir den til transportøren. Det betyr at det er du som har risikoen mens varen er underveis i posten.",
        "paragraftekst": """(1) Skal tingen bringes til kjøperen på samme sted eller innenfor det område der selgeren vanligvis sørger for å bringe ut slike ting (plasskjøp), skjer levering når tingen mottas der.

(2) Skal tingen ellers sendes til kjøperen (sendekjøp) og annet ikke følger av transportklausul eller annen avtale, skjer levering ved at tingen blir overgitt til den fraktfører som påtar seg transport fra avsendingsstedet. Utfører selgeren transporten selv, skjer levering først når tingen mottas av kjøperen.

(3) Er tingen solgt «fritt», «levert» eller «fritt levert» med angivelse av et bestemt sted, anses den ikke levert før den er kommet fram til dette sted.""",
        "hva_betyr_html": """<p>Loven skiller mellom tre situasjoner — og det er ikke bare juridisk pirk. Det avgjør hvem som taper hvis varen blir borte eller skades underveis.</p>
<p><strong>Plasskjøp (første ledd):</strong> Selgeren bringer varen til deg som en del av tjenesten sin — typisk innenfor samme by eller område. Tenk møbelbutikken som kjører ut sofaen hjem til deg. Varen er levert når du faktisk mottar den. Risikoen flytter seg ved døra di.</p>
<p><strong>Sendekjøp (andre ledd):</strong> Selgeren sender varen med en transportør — Posten, Bring, DHL. Da er varen levert allerede idet selgeren overleverer pakken til transportøren. Hvis pakken forsvinner mellom postkontoret og deg, er det dessverre ditt problem mot Posten — ikke selgerens problem.</p>
<p><strong>Selgeren kjører selv:</strong> Hvis selgeren utfører transporten selv (ikke som vanlig service, men som engangssak), er det levering først når du har mottatt varen.</p>
<p><strong>Fritt levert-klausul (tredje ledd):</strong> Hvis selgeren har sagt at varen er "fritt levert" til en bestemt adresse, er den ikke levert før den er der. Da bærer selgeren risikoen hele veien.</p>
<h3>Sammenligning: Hvem har risikoen under transport?</h3>
<table class="rule-table">
<thead><tr><th>Type kjøp</th><th>Levert når</th><th>Hvem har risikoen</th></tr></thead>
<tbody>
<tr><td>Hentekjøp</td><td>Du henter</td><td>Selgeren (frem til henting)</td></tr>
<tr><td>Plasskjøp (selgeren kjører)</td><td>Du mottar hjemme</td><td>Selgeren</td></tr>
<tr><td>Sendekjøp (Posten/Bring)</td><td>Overlevert transportør</td><td>Du (kjøper)</td></tr>
<tr><td>Fritt levert til X</td><td>Pakken er framme på X</td><td>Selgeren</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Anne", "tekst": "Anne kjøper en sofa fra et lite møbelfirma i Oslo for 18 000 kr. De har egen utkjøring innenfor Oslo og kjører den hjem til henne. Underveis sklir den av lasteplanet og blir ripet opp. Dette er et plasskjøp. Sofaen er ikke levert før Anne har den hjemme. Møbelfirmaet må enten reparere, levere ny eller gi prisavslag — Anne skal ikke betale for ripene."},
            {"navn": "Tom", "tekst": "Tom bestiller en racersykkel for 32 000 kr fra et lite nisjeverksted i Bergen. De sender den med Bring. Mellom Bergen og Oslo blir esken skadet, og sykkelen blir bøyd. Dette er et sendekjøp. Sykkelen ble \"levert\" idet verkstedet overga den til Bring. Tom har derfor risikoen for transportskaden. Han må gå løs på Bring, ikke på selgeren. Unntak: I praksis tegner selgeren ofte transportforsikring eller skriver \"fritt levert\" i avtalen. Da bærer selgeren risikoen likevel. Sjekk alltid hva som står."},
        ],
        "vanlige_feil": [
            "Tror at fordi du betalte for frakten, har selgeren risikoen — det stemmer ikke i sendekjøp",
            "Krever pengene tilbake av selger når Posten har mistet pakken — du må normalt gå på Posten",
            "Glemmer å avtale \"fritt levert\" når du kjøper noe verdifullt på avstand",
            "Som selger: tror du er ferdig når pakken er sendt — sjekk at du dokumenterer overlevering til transportør",
        ],
        "hva_bor_du_html": """<p><strong>Som kjøper:</strong></p>
<ul>
<li>Be om "fritt levert" når du kjøper noe verdifullt fra avstand</li>
<li>Be om transportforsikring der det er mulig — sjekk hva selgeren tilbyr</li>
<li>Pakk opp og sjekk varen samme dag — synlig transportskade må meldes raskt til transportør</li>
<li>Ta bilder hvis emballasjen er skadet</li>
</ul>
<p><strong>Som selger:</strong></p>
<ul>
<li>Vær tydelig på fraktvilkår i annonsen eller kontrakten</li>
<li>Bruk sporbar forsendelse på dyre varer</li>
<li>Dokumenter overlevering til transportør</li>
</ul>""",
        "dumme_sporsmal": [
            {"q": "Posten mistet pakken min med en dyr klokke. Får jeg pengene tilbake av selgeren?", "a": "Hvis det er et vanlig sendekjøp uten \"fritt levert\"-klausul: nei. Du må kreve erstatning fra Posten. Selgeren er ute av bildet idet pakken ble levert til Posten."},
            {"q": "Hva hvis pakken aldri ble sendt av selgeren?", "a": "Da er det noe helt annet — det er ingen levering, og selgeren har brutt avtalen. Krev oppfyllelse eller pengene tilbake."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "6", "tittel": "Hentekjøp", "available": True},
            {"lov": "kjopsloven", "paragraf": "8", "tittel": "Selgerens tilleggsplikter ved sendekjøp", "available": True},
            {"lov": "kjopsloven", "paragraf": "13", "tittel": "Når går risikoen over", "available": True},
            {"lov": "kjopsloven", "paragraf": "15", "tittel": "Når varen kjøpes mens den er i transit", "available": True},
        ],
    },
    {
        "number": "8",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Selgerens plikter ved sendekjøp",
        "description": "Skal selgeren sende varen til deg? Da må de velge fornuftig transportmåte, hjelpe deg med forsikringsinfo og merke pakken tydelig som din.",
        "kort_svar": "Når en selger sender en vare til deg, må de ordne transporten på en fornuftig måte. Hvis de ikke tegner forsikring selv, må de gi deg det du trenger for å gjøre det. Og pakken må være merket sånn at det er tydelig at den er til deg.",
        "paragraftekst": """(1) Skal selgeren sørge for at tingen blir sendt, plikter han å inngå avtaler som trengs for å få den transportert til bestemmelsesstedet på egnet måte og på vanlige vilkår for slik transport.

(2) Skal ikke selgeren tegne transportforsikring for tingen, må han når kjøperen ber om det, gi de opplysninger kjøperen trenger for å kunne tegne forsikring.

(3) Dersom selgeren leverer tingen til en fraktfører uten at det ved merking, i transportdokument eller på annen måte tydelig framgår at den skal til kjøperen, må selgeren gi kjøperen slik melding som gjør det klart hva han skal motta.""",
        "hva_betyr_html": """<p>Selv om risikoen flytter seg til deg ved sendekjøp (§ 7), har selgeren noen plikter de må oppfylle. Tre stykker:</p>
<p><strong>1. Velg fornuftig transport (første ledd):</strong> Selgeren kan ikke sende et flygel som vanlig pakkepost. De må velge en transportmåte som passer varen og som er normal i bransjen — "på egnet måte og på vanlige vilkår".</p>
<p><strong>2. Hjelp med forsikring (andre ledd):</strong> Hvis du som kjøper skal forsikre varen selv, må selgeren gi deg informasjonen du trenger — transportør, rute, verdi, leveringstid. Ellers kan du ikke tegne forsikring.</p>
<p><strong>3. Merk pakken tydelig (tredje ledd):</strong> Pakken må vise at den er til deg. Hvis ikke, må selgeren si fra om hva som er sendt og hvordan du skjønner at det er din pakke. Dette henger sammen med § 14: risikoen går ikke over før varen er "identifisert" som din.</p>""",
        "eksempler": [
            {"navn": "Ingrid", "tekst": "Ingrid kjøper et antikt skap fra et lite firma i Trondheim for 65 000 kr. Selgeren tilbyr seg å sende det med en bilfraktrute som tar mindre verdifulle varer i samme bil, uten polstring. Det er ikke \"egnet måte\" for et antikt skap. Selgeren har en plikt etter § 8 til å velge en transportør som faktisk håndterer møbler og polstrer dem forsvarlig — ikke den billigste muligheten."},
            {"navn": "Petter", "tekst": "Petter driver en liten butikk og kjøper et helt vareparti av T-skjorter fra en leverandør for 80 000 kr. Han vil tegne transportforsikring selv. Han spør leverandøren om transportør, antall kolli og vekt — og får det. Da kan han tegne forsikring. Hvis leverandøren hadde nektet å gi informasjonen, hadde de brutt § 8."},
        ],
        "vanlige_feil": [
            "Som selger: velger den billigste fraktmåten uten å tenke på om den passer for varen",
            "Som selger: glemmer å merke pakken tydelig — særlig ved varepartier",
            "Som kjøper: ber ikke om informasjon for å tegne forsikring og taper når noe skjer",
            "Glemmer at brudd på disse pliktene kan gi grunnlag for erstatning (§ 27)",
        ],
        "hva_bor_du_html": """<p>Hvis selgeren sender varen på en uegnet måte og den blir skadet, kan du som kjøper ha krav på erstatning etter § 27, selv om risikoen formelt var hos deg. Du kan også reklamere på selve leveringen. Hvis selgeren ikke merker pakken og du ikke får tatt imot den, går risikoen ikke over (§ 14) — da er det selgerens problem.</p>
<p><strong>Som kjøper:</strong></p>
<ul>
<li>Spør om hvilken transportør selgeren bruker — særlig for dyre eller skjøre varer</li>
<li>Be om sporing</li>
<li>Be om informasjon for å tegne forsikring hvis selgeren ikke gjør det</li>
<li>Krev "fritt levert" på særlig dyre varer</li>
</ul>
<p><strong>Som selger:</strong></p>
<ul>
<li>Pakk forsvarlig og velg transportør som passer varen</li>
<li>Merk pakken tydelig med kjøperens navn og adresse</li>
<li>Send sporingsnummer til kjøperen</li>
<li>Vurder om du burde tilby transportforsikring som del av prisen</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "7", "tittel": "Plasskjøp og sendekjøp", "available": True},
            {"lov": "kjopsloven", "paragraf": "13", "tittel": "Når går risikoen over", "available": True},
            {"lov": "kjopsloven", "paragraf": "14", "tittel": "Identifikasjon av varen", "available": True},
            {"lov": "kjopsloven", "paragraf": "27", "tittel": "Erstatning ved forsinkelse", "available": False},
        ],
    },
    {
        "number": "9",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Når skal varen leveres?",
        "description": "Står det ikke noe om leveringstid i avtalen? Da skal varen leveres innen «rimelig tid». Hva som er rimelig, avhenger av hva slags vare det er.",
        "kort_svar": "Hvis dere ikke har avtalt en leveringstid, skal varen leveres innen \"rimelig tid\" etter kjøpet. Hva som er rimelig kommer an på varen — en standard ting kanskje innen et par uker, en spesialbestilling lenger. Hvis det er avtalt et tidsrom, kan selgeren som hovedregel velge når innenfor det.",
        "paragraftekst": """(1) Skal tingen ikke leveres etter påkrav eller uten opphold, og følger tiden for levering heller ikke ellers av avtale, skal den leveres innen rimelig tid etter kjøpet.

(2) Er det avtalt et tidsrom for levering, har selgeren rett til å velge tidspunktet om forholdene ikke viser at valget tilkommer kjøperen.

(3) Har selgeren ved hentekjøp rett til å velge tidspunkt for levering, skal han i tide gi kjøperen melding om når tingen kan hentes.""",
        "hva_betyr_html": """<p>Loven gir tre regler for leveringstid:</p>
<p><strong>Ingen avtalt tid (første ledd):</strong> Hvis dere ikke har snakket om når varen skal leveres, gjelder "rimelig tid". Hva som er rimelig varierer:</p>
<ul>
<li>Standardvare på lager: noen dager til en uke</li>
<li>Vare som må bestilles inn: et par uker</li>
<li>Spesialbestilling/tilvirkning: gjerne uker eller måneder</li>
</ul>
<p>Bestemmes ikke av magefølelse, men av hva som er normalt for den type vare i den bransjen.</p>
<p><strong>Avtalt tidsrom (andre ledd):</strong> Hvis dere har sagt "leveres mellom 10. og 20. mai", kan selgeren velge dato innenfor det vinduet. Du som kjøper kan ikke kreve eksakt 10. mai med mindre forholdene tilsier at du skulle bestemme.</p>
<p><strong>Selgeren skal varsle ved hentekjøp (tredje ledd):</strong> Hvis det er hentekjøp og selgeren velger tidspunktet, må de gi deg beskjed i tide så du rekker å komme.</p>""",
        "eksempler": [
            {"navn": "Lars", "tekst": "Lars bestiller en spesialfarget elsykkel hos en liten produsent. Det står ikke noe om leveringstid i avtalen. Tre uker går, og ingen sykkel kommer. Lars ringer og blir sagt \"det tar litt tid\". Hva er \"rimelig tid\"? For en spesialprodusert elsykkel kan 4-8 uker være rimelig. For en standardvare på lager kan det være 1-2 uker. Lars må vurdere hva som er normalt i sykkelbransjen, gjerne sjekke andre tilbydere, før han kan si at forsinkelsen er et kontraktbrudd. Når den \"rimelige tiden\" er passert, kan Lars sette en tilleggsfrist og deretter heve kjøpet hvis ikke selgeren leverer (§§ 22-25)."},
            {"navn": "Kari", "tekst": "Kari kjøper kjøkkenmøbler og betaler. Det er avtalt \"levering i uke 20\". Selgeren sender ut sjåføren onsdag uke 20, men Kari er ikke hjemme. Hadde Kari rett til å bestemme dag? Som hovedregel nei. Når avtalen sier \"uke 20\", kan selgeren velge dag — med mindre forholdene viser at kjøperen skal bestemme (typisk fordi varen er stor og krever at noen er hjemme). I praksis avtaler man derfor ofte et eksakt tidspunkt for store leveranser."},
        ],
        "vanlige_feil": [
            "Tror \"rimelig tid\" er 1-2 dager uansett — det varierer mye",
            "Krever heving etter ti dager når varen normalt tar tre uker å produsere",
            "Glemmer at avtalen kan sette helt andre frister enn loven (§ 3)",
            "Som selger: gir ikke beskjed når varen er klar til henting",
        ],
        "hva_bor_du_html": """<p><strong>Som kjøper:</strong></p>
<ul>
<li>Avtal alltid leveringstid skriftlig — "rimelig tid" gir konflikt</li>
<li>Hvis det går for lenge: send en skriftlig melding med tilleggsfrist (§ 25 andre ledd)</li>
<li>Krev erstatning hvis forsinkelsen koster deg penger (§ 27)</li>
</ul>
<p><strong>Som selger:</strong></p>
<ul>
<li>Vær realistisk om leveringstid — overlovning er det vanligste konfliktgrunnlaget</li>
<li>Hvis du blir forsinket: gi beskjed med en gang (§ 28 om opplysningsplikt)</li>
<li>Ved hentekjøp: send tydelig melding når varen er klar</li>
</ul>""",
        "dumme_sporsmal": [
            {"q": "Hvor lang tid er «rimelig» for en vanlig vare?", "a": "For en standardvare på lager er normalt opptil et par uker greit. Spesialbestillinger kan ta lenger. Spør selgeren ved kjøpet — det er det eneste som gir deg sikkerhet."},
            {"q": "Kan jeg kreve dagbot ved forsinkelse?", "a": "Bare hvis det er avtalt. Loven gir deg rett til erstatning for faktisk tap (§ 27), ikke dagbot. Vil du ha dagbot, må det stå i avtalen."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "6", "tittel": "Hentekjøp", "available": True},
            {"lov": "kjopsloven", "paragraf": "22", "tittel": "Hva du kan kreve ved forsinkelse", "available": False},
            {"lov": "kjopsloven", "paragraf": "23", "tittel": "Krav om oppfyllelse", "available": False},
            {"lov": "kjopsloven", "paragraf": "25", "tittel": "Heving ved forsinkelse", "available": False},
        ],
    },
    {
        "number": "10",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Selgerens rett til å holde varen tilbake",
        "description": "Har du ikke betalt? Da kan selgeren nekte å gi deg varen — så lenge dere ikke har avtalt kreditt. Penger mot vare, samtidig.",
        "kort_svar": "Hvis dere ikke har avtalt kreditt eller utsatt betaling, kan selgeren nekte å gi deg varen før du betaler. Det er hovedregelen: varen og pengene skal bytte hender samtidig. Skal varen sendes, kan selgeren ikke nekte å sende — men kan ordne det sånn at du ikke får tak i varen før pengene er på konto.",
        "paragraftekst": """(1) Har ikke selgeren gitt kreditt eller henstand med betalingen, plikter han ikke ved å overgi tingen, overlevere dokument eller på annen måte å overføre rådigheten over tingen uten at kjøpesummen betales samtidig.

(2) Skal selgeren sende tingen til et annet sted, kan han likevel ikke la være å sende den, men han kan hindre at kjøperen får rådigheten før kjøpesummen betales.""",
        "hva_betyr_html": """<p>Loven gir selgeren en "tilbakeholdsrett" — en juridisk håndbrekk. Det fungerer slik:</p>
<p><strong>Hovedregelen (første ledd):</strong> Penger mot vare, samtidig. Hvis du som kjøper ikke betaler, kan selgeren nekte å overlevere varen — uansett om det er en sykkel, en bil eller en kjøkkenmaskin.</p>
<p><strong>Unntak:</strong> Hvis dere har avtalt kreditt ("betal innen 14 dager") eller henstand (utsatt betaling), gjelder ikke tilbakeholdsretten. Da har du krav på å få varen først.</p>
<p><strong>Sendekjøp er litt annerledes (andre ledd):</strong> Hvis varen skal sendes med Posten eller en transportør, kan ikke selgeren la være å sende den. Men de kan ordne det sånn at du ikke får utlevert varen før betalingen er på konto — typisk ved oppkrav eller "betaling mot fraktbrev". Da reiser varen, men du får den ikke ut av pakkeboksen før du har betalt.</p>
<h3>Sammenligning: Når får du varen?</h3>
<table class="rule-table">
<thead><tr><th>Avtale</th><th>Hva kan selgeren gjøre?</th></tr></thead>
<tbody>
<tr><td>Ingen avtale om kreditt</td><td>Holde varen tilbake til du betaler</td></tr>
<tr><td>Avtalt kreditt (faktura 14 dager)</td><td>Må overlevere varen først</td></tr>
<tr><td>Sendekjøp uten kreditt</td><td>Kan sende mot oppkrav eller fraktbrev</td></tr>
<tr><td>Forskuddsbetaling avtalt</td><td>Du må betale før varen sendes</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Marius", "tekst": "Marius kjøper en brukt Toyota fra Sara for 95 000 kr på Finn.no. De avtaler henting lørdag. Marius dukker opp og vil ha nøklene med en gang — han skal betale med Vipps når han kommer hjem. Sara kan nekte. § 10 gir henne rett til å holde tilbake bilen til betalingen er gjennomført. Det er bare hvis de uttrykkelig har avtalt kreditt, at Marius kan kreve nøklene først. Det praktiske er å sende Vipps mens de står der — så slipper de begge denne situasjonen."},
            {"navn": "Tom", "tekst": "Tom bestiller arbeidsutstyr fra en leverandør for 12 000 kr. De har ikke avtalt kreditt. Leverandøren sender varene med oppkrav: Tom må betale når pakken kommer fram, ellers får han den ikke. Det er § 10 andre ledd i praksis."},
        ],
        "vanlige_feil": [
            "Som kjøper: tror du kan kreve varen først og betale senere uten avtale",
            "Som selger: glemmer å sette betalingsbetingelser i tilbudet og blir bundet til kreditt på lik linje med fakturasystemet ditt",
            "Tror selgeren kan nekte å sende varen i et sendekjøp — det kan de ikke, men de kan låse rådigheten",
        ],
        "hva_bor_du_html": """<p>Som selger kan du miste tilbakeholdsretten hvis du gir varen først og deretter krever betaling — du har da i praksis gitt kreditt. Hvis kjøperen så ikke betaler, må du gå rettens vei.</p>
<p><strong>Som selger:</strong></p>
<ul>
<li>Vær tydelig på betalingsbetingelser før kjøp inngås</li>
<li>Bruk Vipps, betalingsterminal eller oppkrav ved overlevering</li>
<li>Ikke gi fra deg varen til pengene er bekreftet på konto (Vipps tar sekunder; bankoverføring kan ta dager)</li>
<li>Vær oppmerksom på falske kvitteringer og falske bankvarsler — verifiser selv</li>
</ul>
<p><strong>Som kjøper:</strong></p>
<ul>
<li>Betal når du henter — Vipps er det enkleste</li>
<li>Hvis du må ha kreditt, avtal det skriftlig før kjøpet</li>
<li>Ved sendekjøp: sjekk om det er oppkrav eller forskudd</li>
</ul>""",
        "dumme_sporsmal": [
            {"q": "Kan selgeren nekte å sende varen hvis jeg ikke har betalt forskudd?", "a": "Hvis dere ikke har avtalt forskuddsbetaling, så nei — selgeren må sende varen. Men han kan sende den slik at du ikke får den utlevert før du betaler."},
            {"q": "Hva med Vipps — er den «mottatt» når Vipps-meldingen kommer?", "a": "Praktisk talt ja. Vipps-overføringer er normalt umiddelbare og garantert. Sjekk at pengene er på konto, ikke bare at det står \"betalt\" i Vipps-appen til kjøperen."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "42", "tittel": "Kjøperens tilbakeholdsrett (motstykket)", "available": False},
            {"lov": "kjopsloven", "paragraf": "48", "tittel": "Hvor skal du betale", "available": False},
            {"lov": "kjopsloven", "paragraf": "49", "tittel": "Når skal du betale", "available": False},
            {"lov": "kjopsloven", "paragraf": "54", "tittel": "Heving når kjøperen ikke betaler", "available": False},
        ],
    },
    {
        "number": "11",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Hvem betaler for hva før levering?",
        "description": "Selgeren bærer kostnadene med varen frem til levering. Men hvis du som kjøper forsinker leveringen, må du betale ekstra utgifter selgeren får.",
        "kort_svar": "Selgeren betaler alle utgifter knyttet til varen frem til den er levert. Lagring, vedlikehold, frakt til leveringsstedet — alt det er selgerens regning. Men hvis du som kjøper forsinker leveringen — for eksempel ikke henter når du skulle — må du betale for de ekstra kostnadene som oppstår på grunn av deg.",
        "paragraftekst": "Selgeren bærer kostnadene med tingen til den er levert. Paragrafen her gjelder ikke kostnader ved at leveringen blir forsinket som følge av forhold på kjøperens side.",
        "hva_betyr_html": """<p>Regelen er todelt og ganske enkel:</p>
<p><strong>Hovedregel:</strong> Frem til varen er levert (etter §§ 6-7), er det selgerens utgifter. Står varen på et lager? Selgerens kostnad. Må den vedlikeholdes? Selgerens kostnad. Skal den fraktes til hentestedet? Selgerens kostnad.</p>
<p><strong>Unntaket:</strong> Hvis leveringen blir forsinket fordi du som kjøper ikke gjør det du skal — ikke henter, ikke betaler, ikke gir nødvendig informasjon — må du betale for de ekstra kostnadene det medfører. Da blir lagerleien plutselig din regning.</p>
<p>Når det gjelder selve frakt-kostnaden ved sendekjøp, er det vanlig at kjøperen betaler frakten — men det er noe man avtaler. § 11 handler om kostnader knyttet til selve varen før den er levert, ikke frakt som sådan.</p>""",
        "eksempler": [
            {"navn": "Eva", "tekst": "Eva kjøper et brukt kjøleskap fra Petter for 3 500 kr. De avtaler at hun skal hente det i helgen. Eva utsetter og utsetter. Etter tre uker må Petter flytte kjøleskapet til et minilager fordi han skal pusse opp — det koster 800 kr i måneden. Etter § 11 må Eva dekke disse 800 kronene. Det er forsinkelsen hennes som har skapt utgiften. Petter kan kreve det dekket, eller trekke det fra om hun kommer og avgjøre uenighet senere."},
            {"navn": "Ola", "tekst": "Ola driver et lite firma og selger en spesialmaskin til en bedrift for 250 000 kr. Maskinen er klar, men kjøperen har problemer med betalingen og ber Ola \"holde på den litt\". Ola må leie ekstra lagerplass i fire uker. De ekstra lagerkostnadene kan Ola kreve dekket — sammen med eventuelle andre krav etter § 55 (heving) og § 57 (erstatning)."},
        ],
        "vanlige_feil": [
            "Som kjøper: tror selgeren bare må holde på varen \"gratis\" så lenge man vil",
            "Som selger: glemmer å dokumentere de ekstra kostnadene man får på grunn av kjøperens treghet",
            "Tror at selgeren har plikt til å dekke fraktkostnader uansett — frakt avtales mellom partene",
        ],
        "hva_bor_du_html": """<p><strong>Som selger:</strong></p>
<ul>
<li>Hvis kjøperen forsinker: send skriftlig varsel og dokumenter når og hvor varen ligger</li>
<li>Ta vare på kvitteringer for ekstra lagerleie, transport eller vedlikehold</li>
<li>Se også § 72 om selgerens omsorgsplikt og § 75 om erstatning og sikkerhet for kostnader</li>
</ul>
<p><strong>Som kjøper:</strong></p>
<ul>
<li>Hent eller motta varen til avtalt tid</li>
<li>Hvis du må utsette: spør selgeren om kostnaden ved utsettelsen — og betal det avtalte</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "7", "tittel": "Plasskjøp og sendekjøp", "available": True},
            {"lov": "kjopsloven", "paragraf": "13", "tittel": "Når går risikoen over", "available": True},
            {"lov": "kjopsloven", "paragraf": "50", "tittel": "Kjøperens plikt til å hente", "available": False},
            {"lov": "kjopsloven", "paragraf": "72", "tittel": "Selgerens omsorgsplikt", "available": False},
        ],
    },
    {
        "number": "12",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Hva risikoen for varen betyr",
        "description": "Når risikoen for varen er gått over på deg, må du betale selv om varen blir ødelagt eller forsvinner — så lenge det ikke er selgerens skyld.",
        "kort_svar": "\"Risiko\" i kjøpsloven betyr: hvem må betale hvis varen blir borte, ødelagt eller redusert i verdi mellom kjøp og levering. Når risikoen har gått over på deg, må du betale kjøpesummen selv om varen blir borte underveis — så lenge det ikke skyldes selgeren.",
        "paragraftekst": "Når risikoen for tingen er gått over på kjøperen, faller ikke hans plikt til å betale kjøpesummen bort ved at tingen deretter går tapt, skades eller minskes som følge av hending som ikke beror på selgeren.",
        "hva_betyr_html": """<p>"Risikoens overgang" er kanskje det viktigste juridiske ordet i kjøpsloven. Det avgjør hvem som taper pengene hvis noe går galt.</p>
<p><strong>Risiko handler om uforutsette hendelser:</strong></p>
<ul>
<li>Varen brenner opp</li>
<li>Varen blir stjålet</li>
<li>Varen blir skadet av vannlekkasje</li>
<li>Varen forsvinner i posten</li>
</ul>
<p>Hvis dette skjer mens selgeren har risikoen, må selgeren enten skaffe en ny vare eller betale deg tilbake. Du slipper å betale.</p>
<p>Hvis det skjer etter at du har overtatt risikoen, må du betale kjøpesummen likevel — selv om du aldri får varen. Det er sånn forsikringene er bygd opp: du forsikrer deg mot din egen risiko, ikke andres.</p>
<p><strong>Viktig unntak:</strong> Selgeren har fortsatt ansvaret hvis det er hans skyld at noe har skjedd. Hvis selgeren har pakket dårlig eller behandlet varen uvørent, kan han ikke skjule seg bak risikoreglene.</p>""",
        "eksempler": [
            {"navn": "Lars", "tekst": "Lars kjøper en samlerverdig BMW-motorsykkel fra Tom for 180 000 kr. Han har betalt og overtatt nøkkelen og papirene. Sykkelen står hjemme hos Tom mens Lars venter på henger. Natten etter brenner Toms garasje ned. Spørsmålet er: hvem har risikoen? Hvis levering har skjedd (Lars har overtatt sykkelen, jf. § 6), er det Lars som har risikoen. Han har mistet 180 000 kr og må håpe han har innboforsikring. Hvis ikke levering har skjedd, er det Tom som har risikoen — han må gi pengene tilbake til Lars. Dette viser hvor viktig det er å avtale klart når risikoen flytter seg."},
            {"navn": "Ingrid", "tekst": "Ingrid bestiller en kostbar kameralinse fra Tyskland for 25 000 kr. Det er et sendekjøp uten \"fritt levert\"-klausul. Linsen overgis til DHL — risikoen går da over på Ingrid (§ 7 andre ledd). Underveis blir pakken stjålet. Ingrid må betale linsen, men kan gå på DHL eller eventuell forsikring. Selgeren er ute av bildet, fordi de har levert som avtalt."},
        ],
        "vanlige_feil": [
            "Tror selgeren alltid har risikoen til varen er hjemme hos deg — feil, særlig ved sendekjøp",
            "Tror du slipper å betale hvis varen aldri kom frem — det avhenger av hvem som hadde risikoen",
            "Glemmer å sjekke forsikring før risikoen går over",
        ],
        "hva_bor_du_html": """<p>Hvis du har risikoen og varen blir borte: du betaler likevel. Eneste vei ut er forsikring eller å rette krav mot den som faktisk er skyld i tapet (typisk transportør).</p>
<ul>
<li>Avtal tydelig når risikoen går over — særlig for dyre kjøp</li>
<li>Skaff transportforsikring hvis du har risikoen i transport</li>
<li>Sjekk innboforsikringen for verdifulle kjøp som ikke fysisk er hos deg</li>
<li>Dokumenter når varen overleveres med bilder eller signatur</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "7", "tittel": "Plasskjøp og sendekjøp", "available": True},
            {"lov": "kjopsloven", "paragraf": "13", "tittel": "Når går risikoen over", "available": True},
            {"lov": "kjopsloven", "paragraf": "14", "tittel": "Identifikasjon av varen", "available": True},
            {"lov": "kjopsloven", "paragraf": "15", "tittel": "Risiko ved transittkjøp", "available": True},
        ],
    },
    {
        "number": "13",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Når går risikoen over på kjøperen?",
        "description": "Risikoen flytter seg fra selger til kjøper når varen er levert. Henter du ikke i tide, kan risikoen gå over selv om du ikke har varen i hånden.",
        "kort_svar": "Risikoen går fra selger til kjøper når varen er levert — etter reglene i §§ 6-7. Henter du som kjøper ikke i tide, eller medvirker du ikke som du skal, kan risikoen gå over likevel — selv om du ikke har varen fysisk hos deg.",
        "paragraftekst": """(1) Risikoen går over på kjøperen når tingen er levert som avtalt eller i samsvar med §§ 6 eller 7.

(2) Blir tingen ikke hentet eller mottatt til rett tid, og beror dette på kjøperen eller forhold på hans side, går risikoen over på ham når tingen er stilt til hans rådighet og det inntrer kontraktbrudd fra hans side ved at han ikke overtar tingen.

(3) Skal kjøper hente tingen på et annet sted enn hos selgeren, går risikoen over når leveringstiden er inne og kjøperen er kjent med at tingen er stilt til hans rådighet på leveringsstedet.""",
        "hva_betyr_html": """<p>Tre ulike situasjoner — tre regler:</p>
<p><strong>Vanlig levering (første ledd):</strong> Når varen er levert som avtalt, går risikoen over. For hentekjøp: når du har varen i hånden. For plasskjøp: når den er fremme hos deg. For sendekjøp: når den er overgitt til transportøren.</p>
<p><strong>Du henter ikke i tide (andre ledd):</strong> Selgeren har stilt varen klar, men du dukker ikke opp. Da kan risikoen gå over på deg likevel — så lenge det er din feil, og du dermed er i kontraktbrudd. Logikken: du skal ikke kunne unngå risiko ved å være treg.</p>
<p><strong>Henting et annet sted (tredje ledd):</strong> Hvis du skulle hente på et annet sted enn hos selgeren (et lager, en gård) og du vet at varen står klar der, går risikoen over når leveringstiden inntreffer — selv om du ikke har vært innom enda.</p>
<h3>Sammenligning: Når går risikoen over?</h3>
<table class="rule-table">
<thead><tr><th>Situasjon</th><th>Risiko går over når</th></tr></thead>
<tbody>
<tr><td>Hentekjøp</td><td>Du henter varen</td></tr>
<tr><td>Plasskjøp</td><td>Varen er fremme hos deg</td></tr>
<tr><td>Sendekjøp</td><td>Varen overgis til transportør</td></tr>
<tr><td>Du henter ikke i tide</td><td>Avtalt hentedato (kontraktbrudd)</td></tr>
<tr><td>Fjernlager + du er informert</td><td>Leveringstiden inntreffer</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Sara", "tekst": "Sara kjøper en brukt påhengsmotor fra Ola for 18 000 kr. Hun betaler på fredag og avtaler henting søndag. Søndag kommer hun ikke. Mandag stjeles motoren fra Olas hage. Sara har risikoen fra søndag — da hun skulle ha hentet — fordi hun ikke har medvirket som avtalt (§ 13 andre ledd). Hun må betale, selv om hun aldri får motoren. Hadde tyveriet skjedd lørdag (før avtalt hentedato), ville Ola hatt risikoen og måttet betale tilbake."},
            {"navn": "Tom", "tekst": "Tom kjøper et parti reservedeler hos en grossist i Drammen. De avtaler at delene skal hentes på et lager i Vestby på en bestemt dato. Tom vet om dette. Når datoen kommer og delene står klar, går risikoen over på Tom — selv om han først kjører Vestby uka etter og oppdager at lageret har vært utsatt for vannlekkasje. Dette er hard medisin — derfor er det viktig å hente i tide eller å avtale spesielt om risiko."},
        ],
        "vanlige_feil": [
            "Tror risikoen flytter seg når du betaler — det stemmer ikke",
            "Tror risikoen kan stå hos selgeren uansett hvor sent du henter — feil",
            "Tror \"klar for henting\"-melding er nok — leveringsstedet og kjent informasjon spiller inn",
        ],
        "hva_bor_du_html": """<p><strong>Som kjøper:</strong></p>
<ul>
<li>Hent eller motta varen i tide</li>
<li>Hvis du blir forsinket: gi beskjed og avtal ny dato — skriftlig</li>
<li>Sjekk om innboforsikringen dekker varer du har risiko for, men ikke har fått hjem enda</li>
</ul>
<p><strong>Som selger:</strong></p>
<ul>
<li>Gi tydelig melding om at varen er klar, og hvor</li>
<li>Dokumenter datoen for klargjøring</li>
<li>Hvis kjøperen ikke kommer: du har omsorgsplikt etter § 72, men kan kreve dekning av kostnader</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "6", "tittel": "Hentekjøp", "available": True},
            {"lov": "kjopsloven", "paragraf": "7", "tittel": "Plasskjøp og sendekjøp", "available": True},
            {"lov": "kjopsloven", "paragraf": "12", "tittel": "Hva risikoen innebærer", "available": True},
            {"lov": "kjopsloven", "paragraf": "50", "tittel": "Kjøperens plikt til å hente", "available": False},
        ],
    },
    {
        "number": "14",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Varen må være merket som din",
        "description": "Risikoen går ikke over på deg før det er gjort tydelig at varen er din — gjennom merking, fraktbrev eller annen identifikasjon.",
        "kort_svar": "Risikoen kan ikke gå over på deg før det er klart at akkurat den varen er tiltenkt deg — ikke en annen kjøper. Står varen blant ti like uten merking, har ikke risikoen flyttet seg. Det er først når det er identifisert — ved navn, etikett, fraktbrev eller på annen måte — at du har den juridiske risikoen.",
        "paragraftekst": "Risikoen går ikke over på kjøperen før det ved merking, transportdokument eller på annen måte er gjort klart at tingen er tiltenkt kjøperen.",
        "hva_betyr_html": """<p>Det er ikke nok at selgeren bare har en stabel med varer på lageret og sier "din ligger der et sted". Loven krever at det skal være tydelig hvilken vare som er din.</p>
<p><strong>Identifikasjon kan skje på flere måter:</strong></p>
<ul>
<li><strong>Merking:</strong> navnet ditt eller en kode på pakken</li>
<li><strong>Transportdokument:</strong> fraktbrev som peker på deg</li>
<li><strong>Egen plassering:</strong> varen står på en hylle merket med ditt navn</li>
<li><strong>På annen måte:</strong> alt som gjør det klart at akkurat dette objektet er ditt</li>
</ul>
<p><strong>Praktisk konsekvens:</strong> Hvis selgeren har 100 sykler på lager og du har kjøpt én, må selgeren peke ut hvilken som er din før risikoen går over. Ellers vil brann på lageret være selgerens problem, ikke ditt — for det er ikke avgjort hvilken av syklene som var "din".</p>""",
        "eksempler": [
            {"navn": "Anne", "tekst": "Anne driver en kafé og kjøper 50 kg av en spesialbønne fra en kaffegrossist. Grossisten har 500 kg på lager og har ikke skilt ut Annes andel ennå. Underveis tar fukt knekken på halve lageret. Spørsmålet er: er Annes 50 kg identifisert? Hvis ikke, har grossisten risikoen — han må skaffe 50 kg uten skader fra det som er igjen, eller fra ny levering. Dersom han hadde plassert Annes 50 kg på en egen pall og merket den, ville Anne ha risikoen."},
            {"navn": "Marius", "tekst": "Marius kjøper et bestemt kjøleskap fra en bruktforhandler. Selgeren merker det med \"RESERVERT MARIUS\" og setter det i et hjørne. Da er det identifisert. Hvis Marius ikke henter i tide, kan risikoen gå over på ham etter § 13 (2)."},
        ],
        "vanlige_feil": [
            "Som kjøper: krever risikoovergang når varen står \"et sted på lageret\"",
            "Som selger: tror \"din står her\" muntlig er nok — bedre å merke fysisk",
            "Glemmer at det også gjelder for sendekjøp — fraktbrevet må peke på kjøperen",
        ],
        "hva_bor_du_html": """<p><strong>Som selger:</strong></p>
<ul>
<li>Merk varen tydelig så snart kjøpet er inngått — spesielt ved varepartier</li>
<li>Bruk navn, ordrenummer eller andre koder</li>
<li>Dokumenter med bilde</li>
</ul>
<p><strong>Som kjøper:</strong></p>
<ul>
<li>Be om bilde av varen merket med ditt navn ved store kjøp</li>
<li>Sjekk fraktbrev og pakkeseddel ved levering</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "7", "tittel": "Plasskjøp og sendekjøp", "available": True},
            {"lov": "kjopsloven", "paragraf": "8", "tittel": "Tilleggsplikter ved sendekjøp", "available": True},
            {"lov": "kjopsloven", "paragraf": "13", "tittel": "Når går risikoen over", "available": True},
        ],
    },
    {
        "number": "15",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Risiko ved kjøp av varer i transit",
        "description": "Kjøper du varer som allerede er underveis? Da går risikoen over ved avtaleinngåelsen — men selgeren svarer for skader han kjente til.",
        "kort_svar": "Kjøper du varer som allerede er på vei med fartøy, bil eller fly — for eksempel en lasteskipscontainer som er underveis fra Asia — går risikoen over på deg når avtalen inngås. Men selgeren svarer fortsatt for skader han visste om eller burde vite om uten å si fra.",
        "paragraftekst": "Gjelder kjøpet ting under transport, går risikoen over ved avtaleslutningen når forholdene ikke viser at kjøperen har påtatt seg risikoen allerede fra det tidspunktet da tingen ble overgitt til den fraktfører som har utstedt transportdokumentet. Selgeren har i alle høve risikoen for tap eller skade som han kjente eller burde kjenne til ved kjøpet, men ikke opplyste kjøperen om.",
        "hva_betyr_html": """<p>Denne paragrafen handler om en spesiell situasjon: varen er allerede underveis når kjøpet inngås. Tenk på import — en bedrift kjøper en container med varer som allerede er på vei med skip fra Kina. Hvem har risikoen mens den seiler?</p>
<p><strong>To regler:</strong></p>
<p><strong>Hovedregelen:</strong> Risikoen går over på kjøperen ved avtaleinngåelsen. Det vil si: i det øyeblikket dere blir enige om kjøpet, har du som kjøper risikoen — selv om varen er ute på havet.</p>
<p><strong>Unntak ved transportdokument:</strong> Hvis forholdene viser det (typisk fordi det er utstedt et transportdokument, som konnossement), kan risikoen ha gått over tilbake i tid — til da fraktføreren overtok varen. Dette er vanlig i internasjonal handel.</p>
<p><strong>Selgerens kunnskap:</strong> Uansett: hvis selgeren visste eller burde vite at varen var skadet før kjøpet, og ikke sa noe — har selgeren risikoen. Du kan ikke selge en allerede ødelagt container uten å si fra.</p>""",
        "eksempler": [
            {"navn": "Eva", "tekst": "Eva driver et lite firma som selger asiatisk inventar. Hun kjøper en container med møbler fra en grossist i Singapore mens containeren allerede er underveis til Norge med skip. Avtalen blir inngått tirsdag. Etter § 15 går risikoen over på Eva fra og med tirsdag — eller eventuelt tilbake i tid hvis transportdokumentet tilsier det. Hvis containeren blir skadet på fredag, er det Evas problem mot forsikringen. Men: hvis grossisten i Singapore visste at containeren hadde fått en lekkasje på tirsdag morgen og solgte til Eva uten å si fra — da bærer han risikoen for vannskadene."},
        ],
        "vanlige_feil": [
            "Tror risikoen først flytter seg når varen kommer fram — feil ved transittkjøp",
            "Glemmer å sjekke transportdokumentet — det kan flytte risikoen helt tilbake til avskipning",
            "Som selger: holder tilbake informasjon om skade — det rammer deg likevel",
        ],
        "hva_bor_du_html": """<p><strong>Som kjøper i transittkjøp:</strong></p>
<ul>
<li>Forsikre deg om varens stand før kjøp — eventuelt få inspeksjon i transitthavn</li>
<li>Tegn transportforsikring fra avtaledagen</li>
<li>Be om å se transportdokumentet før avtale signeres</li>
</ul>
<p><strong>Som selger:</strong></p>
<ul>
<li>Oppgi alt du vet om varens stand</li>
<li>Hold tilbake informasjon er kontraktbrudd</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "7", "tittel": "Plasskjøp og sendekjøp", "available": True},
            {"lov": "kjopsloven", "paragraf": "13", "tittel": "Når går risikoen over", "available": True},
            {"lov": "kjopsloven", "paragraf": "14", "tittel": "Identifikasjon av varen", "available": True},
        ],
    },
    {
        "number": "16",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Kjøp med returrett",
        "description": "Har du kjøpt på prøve eller med rett til å levere tilbake? Da har du risikoen for varen helt til den faktisk er tilbake hos selgeren.",
        "kort_svar": "Hvis du har kjøpt en vare på prøve eller med rett til å levere den tilbake, har du risikoen for varen mens du har den. Den går ikke tilbake til selgeren før varen faktisk er overtatt igjen. Mister du varen, må du betale den.",
        "paragraftekst": "Er en ting kjøpt og levert på prøve eller for øvrig med rett til tilbakelevering, har kjøperen risikoen etter reglene i kapitlet her inntil tingen igjen er overtatt av selgeren.",
        "hva_betyr_html": """<p>Noen kjøp gir deg rett til å gi varen tilbake — typisk "prøveperiode" på 14 eller 30 dager. Loven sier at i denne perioden har du som kjøper risikoen. Det betyr:</p>
<ul>
<li>Mister du varen: du må betale</li>
<li>Stjeles varen: du må betale</li>
<li>Skader du den: du må betale, eller verdien forringes (jf. § 66 om tilbakelevering)</li>
</ul>
<p>Risikoen går ikke tilbake til selgeren før varen er fysisk overtatt igjen. Å sende den i posten er ikke nok — den må være kommet fram og overtatt.</p>
<p><strong>Viktig:</strong> Dette er ikke det samme som angrerett for forbrukerkjøp (angrerettloven). For nettkjøp og dørsalg som forbruker gjelder egne regler om risiko ved retur.</p>""",
        "eksempler": [
            {"navn": "Petter", "tekst": "Petter får prøve en racersykkel hjemme i to uker før han bestemmer seg. Avtalt pris er 45 000 kr. I prøveperioden blir sykkelen stjålet utenfor en kafé. Petter har risikoen. Han må betale sykkelen, selv om han aldri bestemte seg for å beholde den. Han kan håpe på innboforsikring."},
            {"navn": "Sara", "tekst": "Sara har bestilt klær fra en nisjebutikk privat (ikke et forbrukerkjøp) og fått avtalt prøverett. Hun sender to plagg tilbake med Posten. Pakken forsvinner. Sara har risikoen til selgeren har overtatt klærne igjen. Hvis Posten ikke finner pakken, må Sara dekke beløpet."},
        ],
        "vanlige_feil": [
            "Tror risikoen flytter seg når du sender varen tilbake — den flytter seg når selgeren mottar",
            "Forveksler dette med forbrukerangrerett — der gjelder andre regler om risiko",
            "Glemmer å forsikre varen i prøveperioden",
        ],
        "hva_bor_du_html": """<ul>
<li>Sørg for at innboforsikringen dekker varer du har på prøve</li>
<li>Send retur med sporing og forsikring</li>
<li>Be om bekreftelse på mottak fra selgeren — så vet du når risikoen er av deg</li>
<li>Behandle varen som om den var din i prøveperioden — det er økonomisk sett akkurat det</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "12", "tittel": "Hva risikoen innebærer", "available": True},
            {"lov": "kjopsloven", "paragraf": "13", "tittel": "Når går risikoen over", "available": True},
            {"lov": "kjopsloven", "paragraf": "66", "tittel": "Tilbakelevering ved heving og omlevering", "available": False},
        ],
    },
    {
        "number": "17",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Når har varen en mangel?",
        "description": "Varen har mangel hvis den ikke svarer til avtalen, ikke duger til vanlig bruk, eller ikke passer til det selgeren visste du skulle bruke den til.",
        "kort_svar": "Varen har mangel hvis den ikke er som avtalt — i mengde, kvalitet, egenskaper eller innpakning. Hvis ingenting konkret er avtalt, skal varen kunne brukes til det den vanligvis brukes til. Den skal også passe til ditt spesielle formål hvis selgeren visste hva du skulle bruke den til. Hvis selgeren har vist deg en prøve eller modell, skal varen være som den.",
        "paragraftekst": """(1) Tingen skal være i samsvar med de krav til art, mengde, kvalitet, andre egenskaper og innpakning som følger av avtalen.

(2) Dersom annet ikke følger av avtalen, skal tingen:
(a) passe for de formål som tilsvarende ting vanligvis brukes til;
(b) passe for et bestemt formål som selgeren var eller måtte være kjent med da kjøpet ble inngått, unntatt når forholdene viser at kjøperen for så vidt ikke bygde på selgerens sakkunnskap og vurdering eller ikke hadde rimelig grunn til å gjøre det;
(c) ha egenskaper som selger har vist til ved å legge fram prøve eller modell;
(d) være pakket på vanlig eller annen forsvarlig måte som trengs for å bevare og beskytte tingen.

(3) Tingen har mangel dersom den ikke er i samsvar med kravene i paragrafen her.""",
        "hva_betyr_html": """<p>Dette er fundamentet for hele mangelsbegrepet i kjøpsloven. Når har varen en feil som selgeren må svare for? Loven gir to nivåer:</p>
<p><strong>Avtalen først (første ledd):</strong> Det dere har avtalt, gjelder. Hvis dere har sagt "20 stykker rødmalte stoler", skal det være 20, røde, og stoler — ikke 18 grå pinner.</p>
<p><strong>Hvis avtalen er stille (andre ledd):</strong> Loven setter inn fire minstekrav:</p>
<ul>
<li><strong>(a) Vanlig bruk:</strong> Varen skal passe til det tilsvarende varer brukes til. En sykkel skal kunne sykles. En kjøkkenmaskin skal kunne mikse mat.</li>
<li><strong>(b) Spesielt formål:</strong> Hvis du har fortalt selgeren hva du skal bruke varen til, og selgeren har ekspertise på området, skal varen passe til det formålet. Sa du "jeg trenger en bærbar til videoredigering", kan du ikke få utlevert en kontorlaptop.</li>
<li><strong>(c) Prøve eller modell:</strong> Hvis selgeren har vist deg et eksempel, skal varen være som det. Stoffprøve, demobil, vareprøve — varen skal matche.</li>
<li><strong>(d) Innpakning:</strong> Varen skal være pakket på en måte som beskytter den.</li>
</ul>
<p>Hvis varen ikke oppfyller noen av disse kravene, er det en mangel. Da kan du gjøre gjeldende krav etter §§ 30 og utover.</p>
<h3>Sammenligning: Mangel eller ikke?</h3>
<table class="rule-table">
<thead><tr><th>Situasjon</th><th>Mangel etter § 17?</th></tr></thead>
<tbody>
<tr><td>Vaskemaskinen tar 10 kg, det stod 8 i avtalen</td><td>Nei — den er bedre, ikke verre</td></tr>
<tr><td>Sofaen kom uten det avtalte trekket</td><td>Ja — ikke i samsvar med avtalen</td></tr>
<tr><td>Den brukte bilen er litt slitt</td><td>Avhenger av kjøpesummen og hva som var rimelig å vente</td></tr>
<tr><td>Kjøleskapet bråker mer enn vanlig</td><td>Ja, hvis det går utover vanlig bruk</td></tr>
<tr><td>Selgeren visste du skulle ha den til X, men varen passer ikke</td><td>Ja</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Lars", "tekst": "Lars eier et lite småbruk og kjøper en brukt traktor av en forhandler for 220 000 kr. Han forklarer at den skal brukes til å bære vedstabler og rydde snø på små stier. Selgeren anbefaler en modell. Når Lars får den hjem viser det seg at traktoren er for tung for stiene og graver ned i bakken. Den passer ikke til \"det bestemte formålet\" Lars hadde forklart, og som selgeren visste om. Det er en mangel etter § 17 (2) bokstav b. Lars kan kreve omlevering, prisavslag eller heving."},
            {"navn": "Ingrid", "tekst": "Ingrid bestiller en spesiallaget sofa basert på en stoffprøve hun fikk se hos forhandleren. Når sofaen kommer er stoffet en annen farge og tydelig glattere enn prøven. Etter § 17 (2) bokstav c skal stoffet være som prøven. Det er en mangel. Ingrid kan kreve omlevering eller prisavslag."},
        ],
        "vanlige_feil": [
            "Tror enhver liten irritasjon er en mangel — det må gå utover avtalen eller vanlig bruk",
            "Glemmer å fortelle selgeren hva varen skal brukes til — da har du ikke krav på \"spesielt formål\"-vern",
            "Forveksler personlig smak med mangel — varen må være objektivt utilstrekkelig",
            "Som selger: gir muntlige løfter du ikke kan stå inne for — det blir en del av avtalen (§ 17 første ledd)",
        ],
        "hva_bor_du_html": """<p><strong>Som kjøper:</strong></p>
<ul>
<li>Vær konkret om hva du trenger varen til</li>
<li>Be om prøve eller modell ved spesialvare</li>
<li>Få avtalen skriftlig hvis det er noe spesifikt du forventer</li>
<li>Sjekk varen ved levering (§ 31)</li>
</ul>
<p><strong>Som selger:</strong></p>
<ul>
<li>Vær ærlig om hva varen kan og ikke kan</li>
<li>Vis frem prøve som faktisk representerer det du leverer</li>
<li>Ikke gi løfter du ikke kan oppfylle</li>
</ul>""",
        "dumme_sporsmal": [
            {"q": "Er det mangel hvis varen bare ikke matcher det jeg hadde tenkt?", "a": "Bare hvis det du hadde tenkt var avtalt, eller hvis selgeren burde forstått det. Magefølelse holder ikke. Avtalen, vanlig bruk, eller dokumentert spesielt formål er det som teller."},
            {"q": "Selgeren sa varen var \"topp kvalitet\", men jeg er ikke fornøyd. Mangel?", "a": "\"Topp kvalitet\" er en vurdering, ikke en spesifikk egenskap. Hvis varen tilsvarer normalt for sin pris, er det vanskelig å nå frem. Men hvis det var en kvantifiserbar lovnad (f.eks. \"minst 200 timer batteritid\") og det ikke stemmer, er det mangel."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "18", "tittel": "Opplysninger om varen", "available": True},
            {"lov": "kjopsloven", "paragraf": "19", "tittel": "Varer solgt \"som den er\"", "available": True},
            {"lov": "kjopsloven", "paragraf": "20", "tittel": "Kjøperens onde tro og forundersøkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "30", "tittel": "Hva du kan kreve ved mangel", "available": False},
        ],
    },
    {
        "number": "18",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Når selgerens markedsføring blir bindende",
        "description": "Står det noe i annonsen, på pakken eller i markedsføringen som ikke stemmer? Det kan være en mangel — selgeren er bundet av det som er sagt om varen.",
        "kort_svar": "Hvis varen ikke svarer til opplysninger selgeren har gitt i markedsføring, annonser eller på pakken — og dette kan ha påvirket kjøpet ditt — er det en mangel. Det samme gjelder opplysninger fra tidligere ledd (produsent, importør) hvis selgeren visste eller burde visst om dem. Unntak: hvis opplysningen er rettet tydelig i tide.",
        "paragraftekst": """(1) Reglene om mangler gjelder også når tingen ikke svarer til opplysninger som selgeren i sin markedsføring eller ellers har gitt om tingen, dens egenskaper eller bruk og som kan antas å ha innvirket på kjøpet.

(2) Reglene i første ledd gjelder tilsvarende når tingen ikke svarer til opplysning som noen annen enn selgeren har gitt på tingens innpakning, i annonse eller annen markedsføring på vegne av selgeren eller tidligere salgsledd. Dette gjelder ikke om selgeren verken visste eller burde ha visst at opplysningen var gitt.

(3) Reglene i første og andre ledd gjelder ikke når opplysningen i tide er rettet på en tydelig måte.""",
        "hva_betyr_html": """<p>Du kjøper sjelden bare en vare — du kjøper også informasjonen om varen. Annonsetekst, varedeklarasjon, produktblad, beskrivelse i nettbutikken. Loven sier: hvis selgeren har sagt noe om varen som kan ha påvirket din beslutning om å kjøpe, og det viser seg å være feil, er det en mangel.</p>
<p><strong>Tre ledd:</strong></p>
<p><strong>Selgerens egne opplysninger (første ledd):</strong> Alt selgeren har sagt eller skrevet om varen — i annonse, e-post, butikk, hjemmeside — kan bli en del av "avtalen". To vilkår: opplysningen må gjelde varen (ikke generelle utsagn om bransjen) og må kunne ha påvirket kjøpet.</p>
<p><strong>Opplysninger fra andre (andre ledd):</strong> Også produsentens markedsføring, importørens info, eller tekst på pakken kan binde selgeren — så lenge selgeren visste eller burde visst om opplysningen. Det er rimelig: selger Power en TV med produsentens spesifikasjoner på esken, må Power svare hvis spesifikasjonene er gale.</p>
<p><strong>Tydelig rettelse (tredje ledd):</strong> Hvis opplysningen er rettet i tide og på tydelig måte — for eksempel ved en korrigeringsannonse eller informasjon i butikken før kjøp — er selgeren fri.</p>""",
        "eksempler": [
            {"navn": "Tom", "tekst": "Tom kjøper et drone-kamera fra en spesialforhandler etter å ha sett en annonse som sa \"opptil 45 minutter flytid\". Det faktiske er nærmere 25 minutter ved normalt bruk. Hvis annonsen var villedende og påvirket Toms valg, er det en mangel etter § 18 første ledd. Tom kan kreve prisavslag, eventuelt heving hvis avviket er vesentlig."},
            {"navn": "Anne", "tekst": "Anne kjøper en spesialkrem fra et lite apotek. På pakken står det \"egnet for sensitiv hud — testet på Universitetet i Oslo\". Kremen gir Anne kraftig reaksjon, og det viser seg at testen aldri har vært utført. Selv om opplysningen er på pakken (ikke direkte fra apoteket), er det en mangel etter § 18 andre ledd — så lenge apoteket visste eller burde visst at påstanden var fremsatt. Anne kan kreve prisavslag, omlevering eller heving."},
        ],
        "vanlige_feil": [
            "Tror bare det som står i kontrakten teller — annonsetekst, e-poster og chatmeldinger teller også",
            "Som selger: bruker overdrevne formuleringer i markedsføringen som kan binde deg",
            "Tror \"ca.\" og \"opptil\" gir deg fritt spillerom — det gjør det ikke ubegrenset",
            "Glemmer å rette feil informasjon før kjøpet skjer",
        ],
        "hva_bor_du_html": """<p>Da er det mangel — og du har samme krav som ved andre mangler (§ 30): retting, omlevering, prisavslag, heving og erstatning. Hvilket krav som passer best, avhenger av hvor alvorlig avviket er.</p>
<p><strong>Som kjøper:</strong></p>
<ul>
<li>Ta vare på annonser, e-poster, chat-meldinger som beskriver varen — det er bevis</li>
<li>Skjermbilde av nettsider før kjøp</li>
<li>Ta opp avvik så snart du oppdager det</li>
</ul>
<p><strong>Som selger:</strong></p>
<ul>
<li>Vær konservativ i markedsføringen</li>
<li>Rett feil tydelig og raskt — § 18 (3) er en redningsplanke, men du må gjøre noe aktivt</li>
<li>Husk at også produsentens markedsføring kan binde deg</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "17", "tittel": "Når varen har mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "19", "tittel": "Varer solgt \"som den er\"", "available": True},
            {"lov": "kjopsloven", "paragraf": "86", "tittel": "Ansvar for tidligere salgsledds opplysninger", "available": False},
        ],
    },
    {
        "number": "19",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Varer solgt «som den er»",
        "description": "Står «selges som den er» i annonsen? Det gir selgeren mindre ansvar — men ikke fritt spillerom. Du kan fortsatt klage på alvorlige feil.",
        "kort_svar": "Selv om en vare er solgt \"som den er\" eller med liknende forbehold, kan du klage på mangler i tre tilfeller: hvis selgeren har gitt feil opplysninger, hvis selgeren har holdt tilbake vesentlig informasjon han måtte kjenne til, eller hvis varen er i vesentlig dårligere stand enn prisen tilsa. Klausulen begrenser ansvaret — den fjerner det ikke.",
        "paragraftekst": """(1) Selv om tingen er solgt «som den er» eller med liknende alminnelig forbehold, foreligger mangel når
(a) tingen ikke svarer til opplysninger som selgeren har gitt om tingen, dens egenskaper eller bruk og som kan antas å ha innvirket på kjøpet,
(b) selgeren ved kjøpet har forsømt å gi opplysning om vesentlige forhold ved tingen eller dens bruk som han måtte kjenne til og som kjøperen hadde grunn til å rekne med å få, såframt unnlatelsen kan antas å ha innvirket på kjøpet, eller
(c) tingen er i vesentlig dårligere stand enn kjøperen hadde grunn til å rekne med etter kjøpesummens størrelse og forholdene ellers.

(2) Selges brukte ting på auksjon gjelder reglene i første ledd tilsvarende så langt de passer.""",
        "hva_betyr_html": """<p>"Som den er", "as is", "med forbehold om feil og mangler" — slike fraser er kjente fra brukthandel, særlig bil og bolig. Klausulen gjør at selgeren tar mindre ansvar enn ved en vanlig vare. Men det er ikke et skjold mot alt.</p>
<p><strong>Tre situasjoner der du fortsatt kan klage:</strong></p>
<p><strong>(a) Feil opplysninger:</strong> Selgeren sa noe om varen som ikke stemmer, og det kan ha påvirket kjøpet. Sa han "motoren er nylig overhalt"? Da må det være sant — selv om bilen ble solgt "som den er".</p>
<p><strong>(b) Holdt tilbake viktig informasjon:</strong> Selgeren visste om noe vesentlig — en stor feil, en historie — og fortalte det ikke. Du hadde rimelig grunn til å forvente å få det å vite. Klassisk eksempel: bilen har vært totalskadet og reparert. Det skulle selgeren ha sagt.</p>
<p><strong>(c) Vesentlig dårligere stand enn forventet:</strong> Selv uten konkrete feil-opplysninger kan varen være så dårlig at den ikke svarer til prisen. Tenk: du betaler 80 000 kr for en bil som likner en bruktbil i ok stand, men det viser seg at motoren er ferdig. Da er den i "vesentlig dårligere stand" enn 80 000 kr tilsa. Da har du krav, selv om det stod "som den er".</p>
<p><strong>Brukte ting på auksjon (andre ledd):</strong> Reglene gjelder tilsvarende der det passer.</p>
<p><strong>Viktig endring fra 2024:</strong> For forbrukerkjøp av brukte varer er det ikke lenger tillatt å bruke "som den er"-klausul (forbrukerkjøpsloven). Kjøpsloven § 19 gjelder bare når kjøpet er privat-til-privat eller mellom næringsdrivende.</p>
<h3>Sammenligning: Mangel selv ved «som den er»?</h3>
<table class="rule-table">
<thead><tr><th>Situasjon</th><th>Mangel?</th></tr></thead>
<tbody>
<tr><td>Selgeren sa "motoren er nyrenovert" — det stemmer ikke</td><td>Ja (bokstav a)</td></tr>
<tr><td>Selgeren visste om alvorlig feil, fortalte ikke</td><td>Ja (bokstav b)</td></tr>
<tr><td>Bilen koster 80 000, motoren ryker etter 2 mnd, kostnad 60 000</td><td>Sannsynligvis (bokstav c)</td></tr>
<tr><td>Bilen har normal slitasje for alderen</td><td>Nei</td></tr>
<tr><td>Selgeren visste ikke om feilen selv</td><td>Vurderingen blir bokstav c (vesentlig dårligere stand)</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Sara", "tekst": "Sara selger sin gamle Volvo til Marius for 65 000 kr via Finn.no, \"som den er\". Marius oppdager etter tre uker at clutchen er ferdig — det vil koste 28 000 kr å fikse. Sara visste det ikke — clutchen virket greit for henne. Da hjelper § 19 bokstav b ikke. Men kan Marius bruke bokstav c? Han må vise at bilen er i \"vesentlig dårligere stand\" enn 65 000 kr skulle tilsi. Det er en konkret vurdering: er 28 000 kr i reparasjon mye for en 65 000 kr bil? Trolig ja — Marius kan ha krav på prisavslag. Hadde Sara visst om clutchen og holdt det skjult, ville bokstav b også vært relevant."},
            {"navn": "Tom", "tekst": "Tom kjøper en BMW motorsykkel for 110 000 kr av en privatperson, \"som den er\". To måneder senere oppdager han at sykkelen har vært totalt vraket, demontert og bygget opp igjen. Det stod ikke noe om dette i annonsen. Hvis selgeren visste dette, er det en mangel etter § 19 bokstav b — han har fortiet vesentlig informasjon Tom hadde grunn til å forvente å få. Tom kan kreve prisavslag eller heving."},
        ],
        "vanlige_feil": [
            "Som kjøper: tror \"som den er\" er total ansvarsfraskrivelse — det er det ikke",
            "Som selger: tror du kan skjule alvorlige feil bare ved å skrive \"som den er\" — du kan ikke",
            "Glemmer at også fortielser er ansvarsgrunnlag, ikke bare aktive løgner",
            "Tror \"vesentlig dårligere\" er en mild vurdering — det skal en del til",
        ],
        "hva_bor_du_html": """<p>Du har samme krav som ved alle mangler: retting, omlevering, prisavslag, heving og erstatning (§§ 30 og utover). Men ved "som den er"-salg kan kravet være mer begrenset i praksis fordi du må vise vesentlig avvik. Spesielt: Ved kjøp av brukte ting på auksjon kan du ikke kreve prisavslag (§ 37 (2)). Andre krav står ved makt.</p>
<p><strong>Som kjøper på brukmarkedet:</strong></p>
<ul>
<li>Undersøk varen grundig før kjøp (§ 20 — det du burde oppdaget kan du ikke klage på senere)</li>
<li>Ved bil: be om service-historikk, vurder en NAF-test eller verkstedtitt</li>
<li>Still konkrete spørsmål skriftlig — det kan binde selgeren senere</li>
<li>Få mest mulig på SMS eller e-post</li>
</ul>
<p><strong>Som selger på brukmarkedet:</strong></p>
<ul>
<li>Skriv det du vet om varens stand og historie i annonsen</li>
<li>Ikke bagatelliser kjente feil</li>
<li>"Som den er" beskytter mot småfeil — ikke mot alvorlige skjulte forhold</li>
<li>La kjøper undersøke grundig før salg</li>
</ul>""",
        "dumme_sporsmal": [
            {"q": "Jeg kjøpte en bil «som den er», og motoren røk etter 14 dager. Har jeg ingen rettigheter?", "a": "Du har rettigheter — men terskelen er høyere. Vurder etter bokstav c: er det vesentlig dårligere stand enn prisen tilsa? Eller bokstav b: visste selgeren om det? Begge gir grunnlag for krav."},
            {"q": "Er auksjonssalg helt uten ansvar?", "a": "Nei. § 19 (2) gjør reglene gjeldende også for brukte ting på auksjon. Men du kan ikke kreve prisavslag (se § 37)."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "3", "tittel": "Avtale går foran loven", "available": True},
            {"lov": "kjopsloven", "paragraf": "17", "tittel": "Når varen har mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "18", "tittel": "Ansvar for opplysninger", "available": True},
            {"lov": "kjopsloven", "paragraf": "20", "tittel": "Kjøperens forundersøkelse", "available": True},
        ],
    },
    {
        "number": "20",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Når du visste om feilen",
        "description": "Visste du om feilen før kjøpet, kan du ikke klage på den. Det samme gjelder feil du burde sett under en undersøkelse selgeren oppfordret deg til.",
        "kort_svar": "Du kan ikke klage på en mangel som du kjente eller måtte kjenne til ved kjøpet. Har du undersøkt varen — eller uten god grunn latt være å undersøke selv om selgeren ba deg om det — kan du ikke klage på feil du burde ha oppdaget. Unntak: hvis selgeren har vært grovt uaktsom eller uærlig.",
        "paragraftekst": """(1) Kjøperen kan ikke gjøre gjeldende som mangel noe han kjente eller måtte kjenne til ved kjøpet.

(2) Har kjøperen før kjøpet undersøkt tingen eller uten rimelig grunn unnlatt å etterkomme selgerens oppfordring om å undersøke den, kan kjøperen ikke gjøre gjeldende noe som han burde ha oppdaget ved undersøkelsen, med mindre selgeren har handlet grovt aktløst eller for øvrig i strid med redelighet og god tro.

(3) Reglene foran gjelder tilsvarende når kjøperen før kjøpet er gitt høve til å undersøke en prøve og mangelen angår en egenskap som skulle framgå av prøven.""",
        "hva_betyr_html": """<p>Du kan ikke kreve "ny vare" for noe du allerede så feilen på da du kjøpte. Loven gir tre regler:</p>
<p><strong>Du visste eller måtte vite (første ledd):</strong> Hvis du kjente til feilen da du kjøpte, kan du ikke senere klage på den. "Måtte kjenne til" er strengere — det er feil som var så åpenbare at du må ha lagt merke til dem.</p>
<p><strong>Du undersøkte eller skulle ha undersøkt (andre ledd):</strong> Hvis du faktisk har sjekket varen, eller hvis selgeren ba deg sjekke og du uten god grunn ikke gjorde det, taper du retten til å klage på feil du burde ha sett. Det handler om hva en alminnelig oppmerksom person ville oppdaget.</p>
<p>Men: hvis selgeren har vært grovt uaktsom eller uærlig, kommer du i posisjon igjen. Du skal ikke straffes for at selgeren har vært upålitelig.</p>
<p><strong>Prøve eller modell (tredje ledd):</strong> Hvis selgeren har gitt deg sjansen til å se en prøve, gjelder samme regel — du kan ikke klage på det prøven viste.</p>
<h3>Sammenligning: Kan du klage?</h3>
<table class="rule-table">
<thead><tr><th>Situasjon</th><th>Klagerett?</th></tr></thead>
<tbody>
<tr><td>Du så feilen og kjøpte likevel</td><td>Nei</td></tr>
<tr><td>Du sjekket varen og burde sett feilen</td><td>Nei</td></tr>
<tr><td>Selgeren ba deg sjekke, du ikke gjorde det</td><td>Som regel nei</td></tr>
<tr><td>Du sjekket men feilen var skjult</td><td>Ja</td></tr>
<tr><td>Selgeren visste om feilen og lurte deg</td><td>Ja, uansett</td></tr>
<tr><td>Feilen er noe en lekmann ikke kunne sett</td><td>Ja</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Petter", "tekst": "Petter kjøper en brukt bil av en privatperson for 45 000 kr. Han ser tydelig at det er rust under bilen ved prøvekjøring. To måneder senere reklamerer han på rusten. Petter kan ikke klage på det. Han så rusten ved kjøpet (§ 20 første ledd). Hvis han ville hatt rust-fri bil, måtte han enten forhandlet pris eller valgt en annen bil."},
            {"navn": "Eva", "tekst": "Eva kjøper en brukt symaskin. Selgeren sier \"kom gjerne innom og test den før du bestemmer deg\". Eva er busy, hopper over, og kjøper på et bilde. Når hun får maskinen hjem oppdager hun at en av sømtypene ikke virker — noe en testkjøring ville avslørt umiddelbart. Etter § 20 andre ledd kan Eva ikke klage. Selgeren oppfordret henne til å undersøke, Eva hadde ikke god grunn til å la være, og feilen var noe hun burde ha oppdaget. Med mindre selgeren visste om feilen og likevel ba Eva komme — da kan han ha handlet i strid med god tro, og Eva kan klage likevel."},
        ],
        "vanlige_feil": [
            "Kjøper i fart uten å sjekke, og blir overrasket etterpå",
            "Tror du kan klage på alt fordi du «ikke er ekspert» — det forventes alminnelig oppmerksomhet",
            "Som selger: lar være å oppfordre til undersøkelse — du har en sterkere posisjon ved å gjøre det",
            "Glemmer at \"grov uaktsomhet\" fra selgers side gjør at du kommer i posisjon igjen",
        ],
        "hva_bor_du_html": """<p><strong>Som kjøper:</strong></p>
<ul>
<li>Sjekk varen før du kjøper — særlig ved store kjøp, brukt og spesialvarer</li>
<li>Ta med en kyndig venn hvis du ikke selv har peiling</li>
<li>Be om bilder, video, prøvekjøring, demo</li>
<li>Hvis du ikke får undersøke, dokumenter at du ba om det og fikk nei</li>
</ul>
<p><strong>Som selger:</strong></p>
<ul>
<li>Oppfordre til undersøkelse — det gir deg vern etter § 20 (2)</li>
<li>Vær ærlig — uærlighet fjerner selve vernet (§ 33)</li>
<li>La kjøper teste varen før salget er gjennomført</li>
</ul>""",
        "dumme_sporsmal": [
            {"q": "Selgeren sa varen var perfekt, jeg sjekket ikke. Kan jeg klage?", "a": "Det kommer an på. Hvis selgeren visste at noe ikke stemte og likevel sa \"perfekt\", har han handlet i strid med god tro — da kan du klage selv om du ikke sjekket. Hvis selgeren oppriktig trodde varen var perfekt, og feilen var åpenbar, kan du tape retten."},
            {"q": "Jeg så feilen, men selgeren sa det ikke var noe å bry seg om. Kan jeg klage?", "a": "Vanskelig. Du så feilen og kjøpte likevel. Men hvis selgeren aktivt bagatelliserte noe alvorlig, kan det gå inn under \"i strid med redelighet og god tro\" — og du kan komme i posisjon."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "17", "tittel": "Når varen har mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "19", "tittel": "Varer solgt \"som den er\"", "available": True},
            {"lov": "kjopsloven", "paragraf": "31", "tittel": "Kjøperens undersøkelse etter levering", "available": False},
            {"lov": "kjopsloven", "paragraf": "33", "tittel": "Unntak fra reklamasjonsreglene ved uaktsomhet", "available": False},
        ],
    },
    {
        "number": "21",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Når må mangelen ha vært der?",
        "description": "Mangelen må ha vært der da risikoen gikk over på deg — selv om den først viser seg senere. Selgeren svarer også for feil som skyldes hans kontraktbrudd.",
        "kort_svar": "Det avgjørende er om mangelen var der da risikoen gikk over på deg — som regel ved levering. Selv om feilen først dukker opp senere, kan den fortsatt være en mangel hvis årsaken lå i varen fra start. Selgeren svarer også for feil som oppstår senere hvis det skyldes hans kontraktbrudd, eller hvis han har gitt garanti.",
        "paragraftekst": """(1) Ved bedømmelse av om tingen har mangel, skal det tidspunktet da risikoen går over på kjøperen legges til grunn, selv om mangelen først viser seg seinere.

(2) Selgeren svarer også for mangel som oppstår seinere dersom den skyldes kontraktbrudd fra hans side. Det samme gjelder dersom selgeren ved garanti eller på annen måte har påtatt seg ansvar for at tingen vil ha angitte egenskaper eller være egnet til vanlig bruk eller en særlig bruksmåte i et tidsrom etter leveringen.""",
        "hva_betyr_html": """<p>Loven svarer på et viktig spørsmål: en feil dukker opp tre måneder etter kjøpet — er det en «mangel» selgeren må svare for, eller bare normal slitasje?</p>
<p>Regelen er: feilen må ha eksistert da risikoen gikk over på deg (typisk ved levering, jf. § 13). Det betyr ikke at feilen må ha vært synlig. Den kan ha ligget skjult som en svakhet i varen og først blitt et problem senere. Det er fortsatt en mangel.</p>
<p>Eksempel: en motor med fabrikkfeil som først ryker etter to måneders bruk — feilen var i motoren fra start, og det er mangel.</p>
<p><strong>To tilfeller hvor selgeren også svarer for senere feil:</strong></p>
<ul>
<li><strong>Selgerens kontraktbrudd</strong> (andre ledd, første setning): Hvis feilen oppstår senere fordi selgeren har gjort noe galt — for eksempel installert noe feil — er det selgerens ansvar.</li>
<li><strong>Garanti</strong> (andre ledd, andre setning): Hvis selgeren har gitt garanti, svarer han for at varen oppfyller garantien i hele garantiperioden. Da spiller det ingen rolle om feilen var der fra start.</li>
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
            {"lov": "kjopsloven", "paragraf": "17", "tittel": "Når varen har mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "32", "tittel": "Reklamasjonsfrister", "available": True},
            {"lov": "kjopsloven", "paragraf": "40", "tittel": "Erstatning ved mangel", "available": True},
        ],
    },
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
<p>Andre ledd gjør reglene gjeldende også for andre plikter selgeren har — som å sende dokumenter eller varsle om noe. Da gjelder forsinkelsesreglene «så langt de passer», med to unntak: du kan ikke sette tilleggsfrist og automatisk heve hvis det bare er en sideplikt.</p>""",
        "eksempler": [
            {"navn": "Kari", "tekst": "Kari har bestilt nytt badekar fra et lite firma for 24 000 kr. Avtalt levering var 1. april. Det er nå 1. mai og ingenting har kommet. Kari har allerede betalt halvparten. Kari har fire valg: insistere på levering, heve og få 12 000 kr tilbake, kreve erstatning for forlenget håndverkerleie, eller holde tilbake resten av betalingen. Hun kan også kombinere — for eksempel heve og kreve erstatning samtidig."},
            {"navn": "Ola", "tekst": "Ola driver et lite verksted og har bestilt reservedeler fra en grossist for 18 000 kr, leveringstid avtalt til torsdag. Det er fredag — ingen deler. Han har en kunde som venter og må kjøpe delene andre steder for 21 000 kr. Ola kan både heve hovedkjøpet og kreve mellomlegget på 3 000 kr som erstatning etter § 27 og § 68 (prisforskjell ved dekningstransaksjon)."},
        ],
        "vanlige_feil": [
            "Tror du må velge mellom oppfyllelse og erstatning — du kan ha begge",
            "Krever heving for tidlig — det krever vesentlig kontraktbrudd eller tilleggsfrist (§ 25)",
            "Glemmer å holde tilbake betaling — det er den sterkeste pressmiddel du har",
            "Som selger: tror du kan unngå krav ved å levere «snart»",
        ],
        "hva_bor_du_html": """<p><strong>Steg for steg når selgeren er forsinket:</strong></p>
<ol>
<li>Send melding skriftlig — SMS eller e-post — om at varen er forsinket</li>
<li>Sett tilleggsfrist hvis avtalen ikke er klart nok overtrådt (§ 25 (2))</li>
<li>Hold tilbake din betaling så langt du har rett til</li>
<li>Vurder dekningskjøp og dokumenter kostnadene</li>
<li>Hev formelt hvis fristen passerer</li>
<li>Krev erstatning for konkrete tap</li>
</ol>
<p>Hold alt skriftlig. Det er det som teller hvis det blir tvist.</p>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "23", "tittel": "Krav om oppfyllelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "25", "tittel": "Heving ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "27", "tittel": "Erstatning ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "42", "tittel": "Tilbakeholdsrett", "available": True},
        ],
    },
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
<p><strong>Umulig</strong> (første ledd, første del): Hvis varen er ødelagt eller fabrikken brent ned, kan du ikke kreve oppfyllelse av noe som ikke finnes. Det må være en hindring «selgeren ikke kan overvinne».</p>
<p><strong>Urimelig dyrt</strong> (første ledd, andre del): Hvis det å levere vil koste selgeren mye mer enn det er verdt for deg, faller kravet. Du har bestilt en spesialdel for 5 000 kr. Det viser seg at selgeren må gå til mye større kostnader for å skaffe den. Det kan være urimelig.</p>
<p><strong>Kortvarig hindring</strong> (andre ledd): Hvis hindringen forsvinner raskt, kan du fortsatt kreve oppfyllelse — såfremt situasjonen ikke har endret seg vesentlig.</p>
<p><strong>Du må fremme kravet i tide</strong> (tredje ledd): Hvis du venter urimelig lenge med å si fra at du fortsatt vil ha varen, mister du retten. Du kan ikke la saken ligge i seks måneder og så plutselig kreve levering.</p>""",
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
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "22", "tittel": "Hva du kan kreve ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "25", "tittel": "Heving ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "52", "tittel": "Selgerens rett til oppfyllelse", "available": False},
        ],
    },
    {
        "number": "24",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Når selgeren spør om du vil ha varen likevel",
        "description": "Spør selgeren om du vil ta imot varen tross forsinkelsen — eller varsler om ny dato — og du ikke svarer, mister du retten til å heve.",
        "kort_svar": "Hvis selgeren spør om du vil ha varen tross forsinkelsen — eller varsler om en ny leveringsdato — og du ikke svarer innen rimelig tid, mister du retten til å heve. Forutsetningen er at selgeren faktisk leverer innen den oppgitte tiden.",
        "paragraftekst": "Dersom selgeren spør om kjøperen tross forsinkelsen vil motta levering, eller underretter kjøperen om at han vil levere innen en angitt tid, men kjøperen ikke svarer innen rimelig tid etter at han har fått meldingen, kan han ikke heve om oppfyllelse skjer innen den tid som er angitt.",
        "hva_betyr_html": """<p>Loven gir selgeren en mulighet til å redde situasjonen — og krever av deg å gi klar beskjed.</p>
<p><strong>To situasjoner:</strong></p>
<ul>
<li>Selgeren spør: «Vil du fortsatt ha varen tross forsinkelsen?»</li>
<li>Selgeren varsler: «Jeg leverer innen [dato].»</li>
</ul>
<p>Hvis du ikke svarer innen rimelig tid, og selgeren leverer som lovet, kan du ikke heve. Tausheten din regnes som godtakelse av den nye fristen.</p>
<p>Logikken: Selgeren skal vite om han skal levere eller ikke. Du kan ikke sitte stille og senere late som du aldri ville ha varen.</p>
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
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "22", "tittel": "Hva du kan kreve ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "25", "tittel": "Heving ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "29", "tittel": "Frist for å heve etter for sen levering", "available": True},
        ],
    },
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
<p><strong>Vesentlig kontraktbrudd</strong> (første ledd): Hvis forsinkelsen i seg selv er så alvorlig at det rammer formålet med kjøpet, kan du heve uten videre. Tenk: du skulle bruke utstyret på et bestemt arrangement som nå er ferdig, eller forsinkelsen er så langvarig at det «ikke gir mening lenger». Hva som er vesentlig avhenger av:</p>
<ul>
<li>Hvor lenge forsinkelsen har vart</li>
<li>Hva varen skulle brukes til</li>
<li>Om selgeren visste om formålet</li>
<li>Om du har gjort dekningskjøp et annet sted</li>
<li>Konsekvensene for deg</li>
</ul>
<p><strong>Tilleggsfrist</strong> (andre ledd): Hvis forsinkelsen ikke er klart vesentlig, kan du sette en rimelig tilleggsfrist. Hvis selgeren da ikke leverer, kan du heve — uansett om bruddet var «vesentlig» eller ikke. Dette er den tryggeste veien.</p>
<p>«Rimelig» varierer med varen — for en standard nettbestilling kanskje 7-14 dager, for en kompleks tilvirkning lenger.</p>
<p><strong>Mens fristen løper</strong> (tredje ledd): Du må vente til tilleggsfristen er ute før du kan heve — med mindre selgeren sier rett ut at han ikke kommer til å levere innen fristen. Da kan du heve med en gang.</p>
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
            {"navn": "Lars", "tekst": "Lars har bestilt et leketog til sønnens 6-årsdag, avtalt levering 10. desember. 18. desember har det fortsatt ikke kommet. Bursdagen er 22. desember. Forsinkelsen er allerede klart vesentlig — selgeren visste sannsynligvis om formålet (det er en bursdagsgave), og forsinkelsen rammer hele poenget. Lars kan heve direkte etter § 25 (1), uten å sette tilleggsfrist. Hvis ingenting tilsa at det var en gave, og det «bare» var en helt vanlig bestilling, ville Lars først måttet sette tilleggsfrist."},
            {"navn": "Eva", "tekst": "Eva har bestilt en oppvaskmaskin. Den skulle leveres 5. april. Det er 25. april og den har ikke kommet. Eva skriver: «Jeg setter en tilleggsfrist på 10 dager. Hvis maskinen ikke er levert innen 5. mai, hever jeg kjøpet.» 5. mai kommer — fortsatt ingen maskin. Eva kan nå heve. Hun sender en melding: «Jeg viser til min tilleggsfrist av 25. april. Fristen er utløpt. Jeg hever kjøpet og krever betalingen tilbake.»"},
        ],
        "vanlige_feil": [
            "Hever direkte ved kort forsinkelse — kan møte motargument om manglende vesentlighet",
            "Setter altfor kort tilleggsfrist — selgeren kan si fristen ikke var rimelig",
            "Hever i tilleggsfristen mens den løper — du må vente",
            "Glemmer at heving må meddeles innen rimelig tid (§ 29)",
        ],
        "hva_bor_du_html": """<p><strong>Trygg fremgangsmåte:</strong></p>
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
            {"q": "Hva er «rimelig» tilleggsfrist?", "a": "For standardvarer typisk 7-14 dager. For spesialvarer eller tilvirkning lenger. Som tommelregel: jo enklere det burde være å levere, jo kortere kan fristen være."},
            {"q": "Kan jeg heve hvis forsinkelsen «bare» er noen dager?", "a": "Sjelden uten tilleggsfrist — selgeren kan motsette seg at det er vesentlig. Med tilleggsfrist har du klar rett."},
            {"q": "Hva skjer når jeg hever?", "a": "Kjøpet faller bort (§ 64). Du får tilbake det du har betalt. Selgeren får tilbake varen hvis den er levert. Du kan kreve erstatning i tillegg."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "22", "tittel": "Hva du kan kreve ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "29", "tittel": "Frist for å heve", "available": True},
            {"lov": "kjopsloven", "paragraf": "39", "tittel": "Heving ved mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "64", "tittel": "Virkninger av heving", "available": False},
        ],
    },
    {
        "number": "26",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Heving av tilvirkningskjøp",
        "description": "Får du laget noe spesielt for deg — og det blir forsinket — kan du heve bare hvis forsinkelsen ødelegger formålet med kjøpet.",
        "kort_svar": "Hvis du har bestilt noe som lages spesielt for deg — etter dine spesifikasjoner — er det vanskeligere å heve. Du kan bare heve hvis forsinkelsen gjør at formålet med kjøpet blir «vesentlig forfeilet». Loven beskytter produsenten, som ellers ville sittet med en spesialvare ingen andre vil ha.",
        "paragraftekst": "Gjelder kjøpet en ting som skal tilvirkes særskilt for kjøperen etter hans oppgaver eller ønsker, og kan selgeren derfor ikke uten vesentlig tap disponere tingen på annen måte, kan kjøperen bare heve dersom forsinkelsen medfører at hans formål med kjøpet blir vesentlig forfeilet.",
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
            {"navn": "Tom", "tekst": "Tom har bestilt et spesialtilpasset kjøkken for 280 000 kr, levering avtalt til 1. mai. Det er 1. juli — to måneder for sent. Tom vil heve. Hvis Tom bare er irritert over forsinkelsen, men kjøkkenet fortsatt vil tjene formålet (hjemme kjøkken), er det vanskelig å heve etter § 26. Hvis han derimot venter med å flytte inn fordi kjøkkenet ikke er ferdig, og dette koster ham i form av husleie eller arbeid — kan formålet være forfeilet. Han bør først sette tilleggsfrist (§ 25 (2)) og dokumentere konkret hvordan forsinkelsen rammer ham."},
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
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "2", "tittel": "Tilvirkningskjøp", "available": True},
            {"lov": "kjopsloven", "paragraf": "22", "tittel": "Krav ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "25", "tittel": "Heving ved forsinkelse generelt", "available": True},
        ],
    },
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
<p><strong>Hovedregelen</strong> (første ledd): Du har krav på erstatning. Selgeren har strengt ansvar — han slipper bare hvis han kan vise at forsinkelsen skyldtes en hindring utenfor hans kontroll som han verken kunne forutse eller unngå. Dette kalles «kontrollansvar». Eksempler på hindringer som kan kvalifisere: naturkatastrofer, krig, streiker, alvorlig sykdom. Eksempler som ikke kvalifiserer: dårlig planlegging, normal sykdom, vanlige logistikkproblemer, økonomiske problemer.</p>
<p><strong>Underleverandører teller med</strong> (andre ledd): Selgeren kan ikke skylde på leverandørene sine. Hvis underleverandøren også ville hatt en gyldig unnskyldning, da slipper selgeren — ellers ikke. Du skal ikke straffes for at selgeren har valgt feil underleverandør.</p>
<p><strong>Hindring må fortsette</strong> (tredje ledd): Når hindringen er borte, må selgeren levere. Hvis han ikke gjør det, er ansvaret tilbake.</p>
<p><strong>Indirekte tap omfattes ikke</strong> (fjerde ledd): Dette er viktig. Konsekvenstap — driftsavbrudd, mistet fortjeneste, «tap fordi du ikke kunne bruke varen» — krever sterkere grunnlag (se § 67 (2)). Du får dekket direkte tap, ikke ringvirkningene.</p>
<p><strong>Unntak ved skyld</strong> (femte ledd): Hvis det er selgerens egen feil eller forsømmelse, gjelder ingen av begrensningene. Da kan du kreve full erstatning — også indirekte tap.</p>
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
            {"navn": "Eva", "tekst": "Eva driver et lite designfirma og hadde bestilt utstyr for å levere et oppdrag. Utstyret kom tre uker for sent. Eva mistet oppdraget, verdt 80 000 kr i fortjeneste. Tapt fortjeneste fra mistet kontrakt er indirekte tap etter § 67 (2) bokstav c. Det dekkes ikke av første ledd i § 27. For å få dette erstattet må Eva kunne vise at selgeren har vært uaktsom — altså § 27 (5)."},
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
    {
        "number": "28",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Selgerens plikt til å varsle om forsinkelse",
        "description": "Når selgeren blir forsinket, må han gi deg beskjed innen rimelig tid. Får du ikke melding, kan du kreve dekket tap du kunne ha unngått.",
        "kort_svar": "Hvis selgeren blir hindret fra å levere i tide, må han si fra til deg om hindringen og hvordan den påvirker leveringen. Får du ikke beskjed innen rimelig tid etter at selgeren burde ha visst om problemet, kan du kreve dekket det tapet du kunne ha unngått hvis du hadde blitt varslet.",
        "paragraftekst": "Hindres selgeren å oppfylle kjøpet til rett tid, skal han gi kjøperen melding om hindringen og dens virkning på muligheten for å oppfylle. Får kjøperen ikke slik melding innen rimelig tid etter at selgeren fikk eller burde fått kjennskap til hindringen, kan kjøperen kreve erstattet tap som kunne vært unngått om han hadde fått meldingen i tide.",
        "hva_betyr_html": """<p>Selgeren har en plikt: så snart han skjønner at varen kommer for sent, må han si fra. Og det må skje innen rimelig tid — ikke uken før avtalt leveringsdato, men når problemet faktisk oppstår.</p>
<p><strong>To deler:</strong></p>
<ul>
<li><strong>Plikten:</strong> Si fra om hindringen og hvordan den påvirker leveringen. Du må få vite hva som skjer og hvor lenge det forventes å ta.</li>
<li><strong>Konsekvensen ved brudd:</strong> Hvis du ikke får beskjed i tide, kan du kreve erstattet det tapet du kunne ha unngått hvis du hadde fått beskjed. Tenk: hadde du visst at maskinen ble en måned forsinket, kunne du leid noe annet. Den ekstrakostnaden du fikk fordi du ventet i uvitenhet — kan du kreve dekket.</li>
</ul>
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
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "22", "tittel": "Krav ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "27", "tittel": "Erstatning ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "58", "tittel": "Kjøperens opplysningsplikt om hindring", "available": False},
        ],
    },
    {
        "number": "29",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Frist for å heve etter for sen levering",
        "description": "Når varen først er levert — bare for sent — må du si fra om heving innen rimelig tid etter at du fikk vite om leveringen. Venter du, taper du retten.",
        "kort_svar": "Hvis varen er levert — bare for sent — kan du fortsatt heve, men du må si fra til selgeren innen rimelig tid etter at du fikk vite om leveringen. Venter du for lenge med å si fra, taper du hevingsretten. Du beholder eventuelt erstatningskravet.",
        "paragraftekst": "Er tingen levert for seint kan kjøperen ikke heve kjøpet, med mindre han gir selgeren melding om kravet innen rimelig tid etter at han fikk vite om leveringen.",
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
<p><strong>1. Retting</strong> (§ 34): Selgeren reparerer feilen. Du beholder varen.</p>
<p><strong>2. Omlevering</strong> (§ 34): Selgeren gir deg en ny vare. Den gamle går tilbake.</p>
<p><strong>3. Prisavslag</strong> (§ 38): Du beholder varen, men betaler mindre — proporsjonalt med hvor mye dårligere varen er.</p>
<p><strong>4. Heving</strong> (§ 39): Kjøpet kanselleres. Du gir tilbake varen, får tilbake pengene.</p>
<p><strong>5. Erstatning</strong> (§ 40): Du får dekket konkrete tap forårsaket av mangelen — uavhengig av om du krever noe annet.</p>
<p><strong>6. Hold tilbake betaling</strong> (§ 42): Hvis du ikke har betalt fullt ut, kan du holde tilbake nok til å sikre dine krav.</p>
<p><strong>Kombiner fritt:</strong> Erstatning kan alltid komme i tillegg til andre krav. Hvis selgeren retter, men du har hatt konkrete tap, kan du fortsatt kreve dem dekket.</p>
<p><strong>Andre feil teller også</strong> (andre ledd): Hvis selgeren har misligholdt annet enn akkurat varens egenskaper — for eksempel mangler dokumentasjon, garantipapirer, instruksjonsmanual eller annet som hører med — gjelder reglene «så langt de passer».</p>
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
            {"navn": "Tom", "tekst": "Tom har kjøpt en racersykkel for 45 000 kr fra en privat selger. Det viser seg at giringssystemet er ødelagt. Reparasjon koster 8 000 kr. Tom har flere valg: retting (selgeren betaler), prisavslag på 8 000 kr og fikse selv, heving (vanskelig hvis mangelen ikke er vesentlig), eller erstatning for ekstrakostnader som leiesykkel. Det praktiske er ofte prisavslag eller retting. Tom kan også kombinere — for eksempel retting + erstatning for leiekostnad."},
            {"navn": "Anne", "tekst": "Anne kjøper en sofa der avtalen inkluderte armbeskytter. Sofaen kommer uten. Det er ikke «feil ved varen» som sådan, men en manglende komponent. Etter § 30 (2) gjelder mangelsreglene «så langt de passer». Anne kan kreve oppfyllelse (manglende del levert), prisavslag (hvis den ikke kan skaffes), eller eventuelt heving hvis sofaen ikke fyller funksjonen sin uten den."},
        ],
        "vanlige_feil": [
            "Tror du må velge ett krav — du kan kombinere",
            "Reklamerer for sent (§ 32 om reklamasjonsfrist)",
            "Glemmer å kreve erstatning som tillegg",
            "Krever heving for små feil — det krever vesentlig mangel",
            "Tror «retting» må selgeren godta — selgeren har faktisk rett til å rette først (§ 36)",
        ],
        "hva_bor_du_html": """<p><strong>Steg for steg ved mangel:</strong></p>
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
    {
        "number": "31",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Du må undersøke varen etter levering",
        "description": "Etter levering skal du sjekke varen så snart du har rimelig sjanse til det. Slurver du med sjekken, kan du miste retten til å klage.",
        "kort_svar": "Etter at varen er levert, må du undersøke den så snart du har rimelig mulighet. «God skikk» i bransjen avgjør hvor grundig. Hvis varen sendes videre, kan du vente til den er fremme på endelig bestemmelsessted. Hopper du over undersøkelsen, kan du miste retten til å klage på feil du burde ha oppdaget.",
        "paragraftekst": """(1) Etter levering skal kjøperen så snart han etter forholdene har rimelig høve til det, undersøke tingen slik god skikk tilsier.

(2) Framgår det at tingen skal transporteres fra leveringsstedet, kan kjøperen vente med å undersøke den til den er kommet fram til bestemmelsesstedet.

(3) Endrer kjøperen bestemmelsesstedet mens tingen er undervegs, eller sender han den videre uten at han har hatt rimelig høve til å undersøke den, og selgeren ved kjøpet kjente eller burde ha kjent til muligheten for slik omdirigering eller videresending, kan undersøkelsen utsettes til tingen er kommet fram til det nye bestemmelsesstedet.""",
        "hva_betyr_html": """<p>Loven krever en aktiv kjøper. Du kan ikke bare ta imot varen, sette den bort og ignorere den i månedsvis. Du må undersøke den så snart du har rimelig sjanse — for å oppdage eventuelle feil.</p>
<p><strong>Hovedregel</strong> (første ledd): «Så snart du har rimelig høve» — som regel innen dager etter levering. «God skikk» betyr at undersøkelsen skal være som det er normalt for slike varer: åpne pakken, sjekk om varen virker, prøv funksjoner som lar seg teste.</p>
<p><strong>Vare som skal sendes videre</strong> (andre ledd): Hvis varen åpenbart skal til et annet sted (du importerer noe for å selge videre, eller bestiller for en kunde), kan du vente til den er fremme der.</p>
<p><strong>Omdirigering underveis</strong> (tredje ledd): Hvis du endrer bestemmelsessted underveis — eller sender varen videre uten å ha sjansen til å sjekke — og selgeren visste at dette kunne skje, kan undersøkelsen utsettes til den er fremme på endelig sted.</p>
<p><strong>Hvorfor er dette viktig?</strong> Hvis du ikke undersøker når du skulle, kan du tape retten til å klage på feil du burde ha sett (§ 32 om reklamasjonsfrist). Klokken begynner å tikke når du burde ha oppdaget feilen — ikke når du faktisk gjorde det.</p>""",
        "eksempler": [
            {"navn": "Lars", "tekst": "Lars bestiller verktøy for 12 000 kr. Pakken kommer, han setter den i kjelleren og glemmer den. Tre måneder senere åpner han — to deler er knust. Etter § 31 skulle Lars ha undersøkt varen så snart han hadde rimelig sjanse — dager etter levering. Reklamasjonsfristen i § 32 begynte å løpe da. Tre måneder er sannsynligvis for sent — han har latt seg «burde oppdage» feilen lenge før han faktisk gjorde det."},
            {"navn": "Eva", "tekst": "Eva driver et lite firma som importerer kontorinventar. Hun bestiller stoler fra en leverandør og sender dem direkte videre til kunde i Bergen. Selgeren visste om at Eva er videreselger. Etter § 31 (3) kan Eva utsette undersøkelsen til stolene er fremme i Bergen. Reklamasjonsfristen begynner å løpe fra det tidspunktet, ikke fra leveringen til Eva."},
        ],
        "vanlige_feil": [
            "Lar varer ligge uåpnet i kjelleren i uker",
            "Tror reklamasjonsfristen begynner når du oppdager feilen — den begynner når du burde oppdaget",
            "Antar at «god skikk» er en lett undersøkelse — det varierer med varen og bransjen",
            "Som videreselger: glemmer å informere selgeren om at varen skal videre",
        ],
        "hva_bor_du_html": """<p><strong>Når varen er levert:</strong></p>
<ul>
<li>Åpne raskt — ideelt samme dag eller innen få dager</li>
<li>Sjekk synlig stand: emballasje, skader, fullstendighet</li>
<li>Test funksjon: slå på, prøv hovedfunksjoner</li>
<li>Ta bilder av eventuelle feil med en gang</li>
<li>Reklamer raskt hvis noe er galt (§ 32)</li>
</ul>
<p><strong>Som videreselger:</strong></p>
<ul>
<li>Si fra til selgeren at varen skal videresendes</li>
<li>Ta vare på dokumentasjon på når varen kom fram til endelig sted</li>
<li>Be sluttkunden om rask tilbakemelding</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "20", "tittel": "Kjøperens forundersøkelse før kjøpet", "available": True},
            {"lov": "kjopsloven", "paragraf": "32", "tittel": "Reklamasjonsfrister", "available": True},
            {"lov": "kjopsloven", "paragraf": "33", "tittel": "Unntak fra reklamasjonsreglene", "available": True},
        ],
    },
    {
        "number": "32",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Reklamasjonsfristene",
        "description": "Du må reklamere innen rimelig tid etter at du oppdaget eller burde oppdaget feilen — og uansett innen to år etter overtakelse.",
        "kort_svar": "Du har to reklamasjonsfrister du må holde: den relative — innen rimelig tid etter at du oppdaget eller burde oppdaget feilen — og den absolutte — innen to år etter at du overtok varen. Begge må overholdes. Hvis selgeren har gitt lengre garanti, gjelder den.",
        "paragraftekst": """(1) Kjøperen taper sin rett til å gjøre en mangel gjeldende dersom han ikke innen rimelig tid etter at han oppdaget eller burde ha oppdaget den, gir selgeren melding som angir hva slags mangel det gjelder.

(2) Reklamerer kjøperen ikke innen to år etter den dag da han overtok tingen, kan han ikke seinere gjøre mangelen gjeldende. Dette gjelder ikke dersom selgeren ved garanti eller annen avtale har påtatt seg ansvar for mangler i lengre tid.""",
        "hva_betyr_html": """<p>To frister gjelder samtidig. Brytes en av dem, taper du retten.</p>
<p><strong>Den relative fristen</strong> (første ledd): Når du har oppdaget — eller burde ha oppdaget — feilen, må du si fra «innen rimelig tid». Hva som er rimelig:</p>
<ul>
<li>Privat handel: dager til noen få uker</li>
<li>Mellom bedrifter: ofte raskere</li>
<li>Komplekse feil som krever undersøkelse: noe lenger</li>
</ul>
<p><strong>Den absolutte fristen</strong> (andre ledd): To år fra du overtok varen. Etter to år kan du ikke klage på mangelen, selv om den nettopp ble synlig. Unntak: hvis selgeren har gitt garanti som strekker seg lenger.</p>
<p><strong>Viktig forskjell fra forbrukerkjøp:</strong> I forbrukerkjøp (forbrukerkjøpsloven § 27) er den absolutte fristen 5 år for varer som er ment å vare vesentlig lenger enn 2 år (TV, bil, hvitevarer). I kjøpsloven er det 2 år — uansett vare.</p>
<p><strong>Meldingen må angi mangelen:</strong> Du må fortelle hva som er feil. Det er ikke nok å skrive «noe er galt». Beskriv konkret hva problemet er.</p>
<h3>Sammenligning: Privat vs. forbruker</h3>
<table class="rule-table">
<thead><tr><th>Situasjon</th><th>Kjøpsloven (privat)</th><th>Forbrukerkjøpsloven</th></tr></thead>
<tbody>
<tr><td>Vanlig bruk, kort levetid</td><td>2 år</td><td>2 år</td></tr>
<tr><td>Vare med lang forventet levetid (TV, bil)</td><td>2 år</td><td>5 år</td></tr>
<tr><td>Garanti</td><td>Hva som er avtalt</td><td>Hva som er avtalt + minst lovens frist</td></tr>
<tr><td>Relativ frist</td><td>Rimelig tid</td><td>Rimelig tid (minst 2 mnd som forbruker)</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Tom", "tekst": "Tom kjøper en brukt bil for 95 000 kr fra en privatperson 1. mars. I oktober — sju måneder senere — oppdager han en motorfeil som kan spores tilbake til før kjøpet. Tom er innenfor toårsfristen. Spørsmålet er den relative fristen: når oppdaget eller burde han ha oppdaget feilen? Hvis feilen først ble synlig i oktober, må han reklamere innen rimelig tid etter det — typisk innen noen uker. Sender Tom melding i oktober eller november: greit. Venter han til mars året etter: trolig for sent etter den relative fristen."},
            {"navn": "Sara", "tekst": "Sara kjøper en symaskin privat for 6 500 kr. Etter to og et halvt år oppdager hun en mangel som kan spores tilbake til kjøpet. Sara har overskredet den absolutte toårsfristen og kan ikke lenger reklamere — med mindre selgeren har gitt en lengre garanti."},
        ],
        "vanlige_feil": [
            "Tror du har 5 år som privat kjøper — du har 2",
            "Venter med å reklamere fordi du ikke vil mase — du taper retten",
            "Sender vag melding uten å spesifisere mangelen — den teller ikke",
            "Tror garanti = reklamasjonsfrist — garanti er noe annet (frivillig fra selger)",
        ],
        "hva_bor_du_html": """<p><strong>Når du oppdager en feil:</strong></p>
<ol>
<li>Reklamer skriftlig — SMS, e-post, brev — innen få dager</li>
<li>Beskriv mangelen konkret: hva, hvor, når oppdaget</li>
<li>Spesifiser kravet: retting, omlevering, prisavslag, heving, erstatning</li>
<li>Ta vare på meldingen — dato og innhold er avgjørende</li>
<li>Hold deg innen toårsfristen — sett påminnelse hvis du nærmer deg</li>
</ol>
<p><strong>Standard reklamasjonsmelding:</strong></p>
<p><em>«Jeg kjøpte [vare] av deg [dato] for [pris]. [Dato i dag] oppdaget jeg [konkret beskrivelse av mangel]. Jeg krever [retting / omlevering / prisavslag / heving].»</em></p>""",
        "dumme_sporsmal": [
            {"q": "Er det nok å sende SMS?", "a": "Ja, men husk å ta vare på den. E-post er kanskje tryggere fordi den har stempling."},
            {"q": "Hva er «rimelig tid»?", "a": "Som privatperson: typisk dager til 2-3 uker. Som bedrift: ofte raskere. Vær så rask du kan."},
            {"q": "Telles helger og ferie?", "a": "Som hovedregel ja — men ekstrem omstendighet (sykehus, langvarig sykdom) kan strekke fristen noe. Som regel ikke ferie."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "31", "tittel": "Undersøkelse etter levering", "available": True},
            {"lov": "kjopsloven", "paragraf": "33", "tittel": "Unntak ved selgerens uaktsomhet", "available": True},
            {"lov": "kjopsloven", "paragraf": "85", "tittel": "Reklamasjon mot tidligere salgsledd", "available": False},
            {"lov": "forbrukerkjopsloven", "paragraf": "27", "tittel": "Frister i forbrukerkjøp", "available": False},
        ],
    },
    {
        "number": "33",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Unntak fra reklamasjonsfristene",
        "description": "Har selgeren vært grovt uaktsom eller uærlig? Da gjelder ikke reklamasjonsfristene. Du kan klage selv etter at toårsfristen er gått ut.",
        "kort_svar": "Hvis selgeren har vært grovt uaktsom eller handlet i strid med «redelighet og god tro», gjelder ikke reklamasjonsfristene i §§ 31 og 32. Du kan klage selv om to år er gått, og selv om du var sen med meldingen. Loven beskytter ikke uærlige selgere.",
        "paragraftekst": "Uansett §§ 31 og 32 kan kjøperen gjøre mangelen gjeldende dersom selgeren har opptrådt grovt aktløst eller for øvrig i strid med redelighet og god tro.",
        "hva_betyr_html": """<p>Reklamasjonsfristene har en moralsk grense. De gjelder ikke når selgeren har vært direkte uærlig eller helt klart skjødesløs.</p>
<p><strong>Loven nevner to typer atferd:</strong></p>
<ul>
<li><strong>Grov uaktsomhet:</strong> Selgeren har vært vesentlig mer uforsiktig enn det som er rimelig. Det er sterkere enn «uaktsomhet» — det skal være tydelig skjødesløst.</li>
<li><strong>I strid med redelighet og god tro:</strong> Selgeren har handlet uærlig — har skjult informasjon, gitt feil opplysninger, eller på annen måte forsøkt å lure deg.</li>
</ul>
<p>Når dette er tilfelle, kan du klage selv om:</p>
<ul>
<li>Du oppdaget feilen langt etter at du burde ha oppdaget den</li>
<li>Det er gått mer enn to år siden overtakelse</li>
<li>Du har vært treg med å sende reklamasjon</li>
</ul>
<p>Logikken er klar: en uærlig selger skal ikke kunne gjemme seg bak tidsfristene. Hvis han har gjort noe galt, skal han stå til ansvar — uansett hvor lenge det går.</p>""",
        "eksempler": [
            {"navn": "Marius", "tekst": "Marius kjøper en brukt bil for 180 000 kr. Tre år senere, ved en uavhengig taksering, oppdager han at bilen har vært totalt vraket og bygget opp igjen. Selgeren visste dette — det fremgår av papirer han har skjult. Vanligvis ville Marius vært ferdig: toårsfristen er passert. Men etter § 33 gjelder ikke fristen når selgeren har handlet i strid med god tro. Selgeren skjulte vesentlig informasjon han var pliktig å gi (jf. § 19 bokstav b). Marius kan reklamere selv etter tre år."},
            {"navn": "Eva", "tekst": "Eva kjøper en symaskin og får utlevert papirer som påstår at det er en ny modell. To og et halvt år senere oppdager hun at det er en eldre modell solgt som ny. Selgeren har vært direkte uærlig. Reklamasjonsfristen er ikke til hinder etter § 33. Eva kan reklamere."},
        ],
        "vanlige_feil": [
            "Tror selgeren slipper unna fordi to år er gått — det stemmer ikke ved uærlighet",
            "Som kjøper: oppgir kampen for tidlig fordi fristene har gått",
            "Som selger: tror skjulte feil kan «preskriberes» — det kan de ikke når du har skjult dem aktivt",
            "Glemmer at bevisbyrden er din — du må kunne dokumentere selgerens uærlighet",
        ],
        "hva_bor_du_html": """<p><strong>Når du tror selgeren har vært uærlig:</strong></p>
<ul>
<li>Dokumenter alt som tyder på uærlighet — gamle annonser, skriftlige løfter, historikk</li>
<li>Skaff bevis fra tredjepart — verkstedrapport, takst, eksperter</li>
<li>Reklamer skriftlig med spesifikk anklage om grov uaktsomhet/uærlighet</li>
<li>Vurder advokathjelp — særlig hvis beløpet er stort</li>
<li>Forliksrådet eller domstol hvis selgeren nekter</li>
</ul>
<p>Du kan gjøre gjeldende alle de vanlige mangelskravene (§ 30): retting, omlevering, prisavslag, heving og erstatning.</p>""",
        "dumme_sporsmal": [
            {"q": "Hva regnes som «grov uaktsomhet»?", "a": "Det er mer enn vanlig slurv. Selgeren må ha vært tydelig skjødesløs på en måte de fleste ville reagert på. Eksempel: solgt en bil de visste hadde alvorlige feil uten å nevne det."},
            {"q": "Trenger jeg klare bevis på uærlighet?", "a": "Du må kunne vise det med rimelig sikkerhet. Mistanke er ikke nok — du trenger dokumentasjon eller logikk som peker på at selgeren visste eller burde visst."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "19", "tittel": "Varer solgt «som den er»", "available": True},
            {"lov": "kjopsloven", "paragraf": "31", "tittel": "Undersøkelse etter levering", "available": True},
            {"lov": "kjopsloven", "paragraf": "32", "tittel": "Reklamasjonsfrister", "available": True},
        ],
    },
    {
        "number": "34",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Krav om retting og omlevering",
        "description": "Du kan kreve at selgeren retter mangelen — for hans regning. Omlevering kan du bare kreve hvis mangelen er vesentlig.",
        "kort_svar": "Du kan kreve at selgeren retter mangelen — uten å betale for det selv — så lenge det ikke koster ham urimelig mye. Omlevering (helt ny vare) kan du bare kreve hvis mangelen er vesentlig, og varen kan erstattes. Hvis selgeren ikke gjør jobben, kan du fikse selv og kreve dekket kostnaden.",
        "paragraftekst": """(1) Kjøperen kan kreve at selgeren for egen rekning retter mangel dersom dette kan skje uten å volde selgeren urimelig kostnad eller ulempe. Selgeren kan isteden foreta omlevering etter § 36.

(2) Kjøperen kan kreve omlevering når mangelen er vesentlig. Dette gjelder ikke dersom det foreligger hindring eller misforhold som nevnt i § 23. Omlevering kan heller ikke kreves når kjøpet gjelder en ting som foreligger ved kjøpet og har slike egenskaper at den ut fra partenes forutsetninger ikke med rimelighet kan erstattes med en annen.

(3) Oppfyller ikke selgeren sin plikt til å rette eller omlevere, kan kjøperen kreve erstatning for sine forsvarlige utgifter ved å få mangelen rettet.""",
        "hva_betyr_html": """<p>Loven setter opp et hierarki for hvordan en mangel kan ordnes — og hva du som kjøper kan kreve.</p>
<p><strong>Retting</strong> (første ledd): Hovedregelen. Du kan kreve at selgeren reparerer feilen for sin regning. Begrensning: hvis rettingen ville koste selgeren urimelig mye sammenliknet med det det er verdt for deg, faller kravet. Selgeren kan også velge å omlevere i stedet for å rette.</p>
<p><strong>Omlevering</strong> (andre ledd): Strengere krav. Tre vilkår må være oppfylt:</p>
<ul>
<li>Mangelen må være vesentlig. Småfeil holder ikke.</li>
<li>Det må ikke foreligge en hindring selgeren ikke kan overvinne, eller misforhold — altså at det vil koste mye mer enn det er verdt.</li>
<li>Varen må kunne erstattes med en annen. Du kan ikke kreve omlevering av en unik ting — et bestemt maleri, en spesifikk brukt bil, et antikt møbel.</li>
</ul>
<p><strong>Egen retting</strong> (tredje ledd): Hvis selgeren ikke gjør jobben — verken retter eller omleverer — kan du fikse mangelen selv og kreve kostnaden dekket. Du må holde deg til «forsvarlige utgifter» — ikke gå til den dyreste fiks-eren for å bli rasende.</p>
<h3>Sammenligning: Retting eller omlevering?</h3>
<table class="rule-table">
<thead><tr><th>Situasjon</th><th>Krav på retting</th><th>Krav på omlevering</th></tr></thead>
<tbody>
<tr><td>Liten feil, lett å reparere</td><td>Ja</td><td>Nei</td></tr>
<tr><td>Vesentlig feil, vare kan erstattes</td><td>Ja</td><td>Ja (du kan velge)</td></tr>
<tr><td>Unik vare (kunst, antikk, brukt unika)</td><td>Ja</td><td>Nei</td></tr>
<tr><td>Urimelig kostnad ved retting</td><td>Nei</td><td>Vurderes</td></tr>
<tr><td>Selgeren leverer ikke svar</td><td>Ja, og du kan fikse selv</td><td>Ja</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Lars", "tekst": "Lars kjøper en ny oppvaskmaskin for 8 500 kr fra en mindre forhandler. Maskinen lekker. Reparasjon koster anslagsvis 1 200 kr. Lars kan kreve retting etter § 34 (1). Kostnaden er rimelig sammenliknet med verdien av varen — selgeren kan ikke nekte. Er mangelen så stor at maskinen ikke fungerer i det hele tatt, kan Lars også kreve omlevering etter § 34 (2). Han kan ikke kreve det hvis lekkasjen er liten."},
            {"navn": "Anne", "tekst": "Anne kjøper en håndlaget vase fra en kunstner for 12 000 kr. Vasen har en mangel — en sprekk. Anne vil ha en ny. Anne kan ikke kreve omlevering, selv om mangelen er vesentlig. Vasen er unik (§ 34 (2) — kan ikke «rimelig erstattes med en annen»). Anne må nøye seg med retting (hvis mulig), prisavslag eller heving."},
            {"navn": "Tom", "tekst": "Tom har bestilt en spesialkomponent for 15 000 kr. Den er feil. Han kontakter selgeren skriftlig flere ganger — ingen respons. Til slutt får han en annen verksted til å fikse komponenten for 4 000 kr. Etter § 34 (3) kan Tom kreve disse 4 000 kr dekket. Han må kunne vise at kostnaden var «forsvarlig» — altså rimelig nivå, ikke premium-priset."},
        ],
        "vanlige_feil": [
            "Krever omlevering for små feil — får nei",
            "Tar varen direkte til reparasjon uten å gi selgeren mulighet — selgeren har rett til å forsøke selv (§ 36)",
            "Tror omlevering alltid kan kreves — feil ved unika varer",
            "Glemmer at «egen retting»-kravet krever at selgeren faktisk har misligholdt",
        ],
        "hva_bor_du_html": """<p><strong>Steg for steg:</strong></p>
<ol>
<li>Reklamer skriftlig (§ 32) — beskriv mangelen</li>
<li>Be om retting eller omlevering — vær konkret</li>
<li>Sett rimelig frist — typisk 14-30 dager</li>
<li>Hvis ingenting skjer: send påminnelse, sett ny frist</li>
<li>Hvis fortsatt ingenting: fiks selv (forsvarlige kostnader) og krev dekket</li>
<li>Hold dokumentasjon: kvitteringer, kommunikasjon, bilder</li>
</ol>
<p><strong>Tommelregel:</strong> Gi selgeren minst én sjanse før du gjør noe selv. Det styrker kravet ditt.</p>""",
        "dumme_sporsmal": [
            {"q": "Kan selgeren si nei til å reparere fordi det «koster for mye»?", "a": "Ja, men bare hvis kostnaden er urimelig sammenliknet med verdien for deg. Hvis det vil koste mer å reparere enn varen er verdt, kan selgeren si nei — men da har du fortsatt prisavslag, omlevering eller heving som alternativer."},
            {"q": "Hvor lang frist er rimelig for retting?", "a": "Avhenger av varen og tilgjengeligheten av deler. For en standardvare: 2-4 uker. For komplekst utstyr: gjerne lenger. Det skal være konkret realistisk."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "30", "tittel": "Krav ved mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "35", "tittel": "Melding om krav på retting/omlevering", "available": True},
            {"lov": "kjopsloven", "paragraf": "36", "tittel": "Selgerens rett til å rette", "available": True},
            {"lov": "kjopsloven", "paragraf": "37", "tittel": "Prisavslag eller heving etter manglende retting", "available": True},
        ],
    },
    {
        "number": "35",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Melding om krav på retting eller omlevering",
        "description": "Du må gi beskjed om at du krever retting eller omlevering sammen med reklamasjonen, eller kort tid etter. Ellers mister du kravet.",
        "kort_svar": "Når du reklamerer på en mangel, må du også si fra om at du krever retting eller omlevering — enten med en gang, eller kort tid etter. Hvis du venter for lenge, mister du den spesifikke kravsformen, men kan fortsatt ha andre krav. Unntak: hvis selgeren har vært uærlig eller grovt uaktsom.",
        "paragraftekst": "Kjøper taper sitt krav på retting eller omlevering dersom han ikke gir selgeren melding om kravet sammen med reklamasjon etter § 32 eller innen rimelig tid deretter. Kjøperen har likevel kravet i behold dersom selgeren har opptrådt grovt aktløst eller for øvrig i strid med redelighet og god tro.",
        "hva_betyr_html": """<p>Det er én ting å si «varen har en feil». Det er noe annet å si «jeg krever at du fikser den». Loven krever at du gjør begge deler — gjerne samtidig.</p>
<p><strong>Tidspunktet:</strong> Sammen med reklamasjonen, eller innen «rimelig tid» etter. Hva som er rimelig avhenger av varen og situasjonen, men du bør være rask. Dager til et par uker er normalt trygt.</p>
<p><strong>Konsekvens hvis du er treg:</strong> Du mister kravet på akkurat retting eller omlevering. Men du kan fortsatt ha krav på prisavslag (§ 38), heving (§ 39) og erstatning (§ 40). De har egne frister.</p>
<p><strong>Unntak ved uærlighet:</strong> Hvis selgeren har vært grovt uaktsom eller handlet i strid med god tro, gjelder ikke fristen. Da kan du fortsatt kreve retting eller omlevering — i tråd med § 33.</p>
<p><strong>Hvorfor finnes denne regelen?</strong> Selgeren skal vite hva du faktisk vil. Skal han skaffe en ny vare, sende en tekniker, eller bare gi prisavslag? Han kan ikke planlegge hvis du ikke spesifiserer.</p>""",
        "eksempler": [
            {"navn": "Petter", "tekst": "Petter kjøper en brukt bil for 75 000 kr og oppdager etter to uker at bremsene har en mangel. Han skriver til selgeren: «Bremsene er feil — vi må snakke om dette.» Det er en reklamasjon, men ikke et spesifikt krav. To måneder senere skriver Petter: «Jeg vil at du omleverer bilen.» For sent — Petter har tapt kravet på omlevering etter § 35. Han kan fortsatt kreve prisavslag eller heving, men det er en annen vei å gå. Lærdom: gi spesifikt krav fra start."},
            {"navn": "Anne", "tekst": "Anne kjøper en oppvaskmaskin og oppdager at den ikke tørker som lovet. Hun skriver: «Jeg reklamerer på at oppvaskmaskinen ikke tørker. Jeg krever at den blir reparert innen 14 dager. Hvis det ikke lar seg gjøre, krever jeg omlevering.» Dette er en klar reklamasjon med klart krav. Selgeren vet nøyaktig hva han skal gjøre."},
        ],
        "vanlige_feil": [
            "Reklamerer uten å spesifisere hvilket krav du gjør gjeldende",
            "Bytter krav frem og tilbake — «først ville jeg ha retting, så omlevering, så prisavslag»",
            "Tror «retting og omlevering» er det samme — det er to ulike krav",
            "Glemmer at andre krav (prisavslag, heving) har egne regler hvis du mister disse",
        ],
        "hva_bor_du_html": """<p>Når du sender reklamasjon:</p>
<ol>
<li>Beskriv mangelen konkret</li>
<li>Si tydelig hva du krever: retting, omlevering, prisavslag, heving — eller flere alternativer rangert</li>
<li>Sett en frist: typisk 14 dager</li>
<li>Hold dokumentasjon</li>
</ol>
<p><strong>Mal:</strong></p>
<p><em>«Jeg reklamerer herved på [vare] kjøpt [dato]. Mangelen er [konkret beskrivelse]. Jeg krever primært [retting / omlevering] innen [dato]. Subsidiært krever jeg [prisavslag / heving]. Jeg forbeholder meg retten til å kreve erstatning.»</em></p>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "32", "tittel": "Reklamasjonsfrister", "available": True},
            {"lov": "kjopsloven", "paragraf": "33", "tittel": "Unntak ved uærlighet", "available": True},
            {"lov": "kjopsloven", "paragraf": "34", "tittel": "Retting og omlevering", "available": True},
        ],
    },
    {
        "number": "36",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Selgerens rett til å rette eller omlevere",
        "description": "Selgeren har rett til å forsøke å rette mangelen — selv om du ikke har bedt om det. Du må normalt gi ham sjansen før du krever andre løsninger.",
        "kort_svar": "Selv om du ikke ber om det, har selgeren rett til å rette mangelen eller levere en ny vare — på egen regning. Forutsetningen er at det ikke gir deg vesentlig ulempe, og at det er ingen risiko for at du ikke får dine penger tilbake. Hvis selgeren spør og du ikke svarer, kan han gjøre jobben innen tiden han har angitt.",
        "paragraftekst": """(1) Selv om kjøperen ikke krever det, kan selgeren for egen kostnad rette mangel eller foreta omlevering, når dette kan skje uten vesentlig ulempe for kjøperen og uten risiko for at kjøperen ikke får dekket sine utlegg av selgeren.

(2) Dersom selgeren spør om kjøperen vil godta retting eller omlevering, eller underretter kjøperen om at han vil rette eller omlevere innen en angitt tid, men kjøperen ikke svarer innen rimelig tid etter at han har fått meldingen, kan selgeren foreta det nødvendige innen den tid som er angitt.

(3) Selgeren kan ikke gjøre gjeldende at han ikke har fått høve til å rette eller omlevere, dersom kjøperen har sørget for å få rettet mangelen og det etter forholdene ville være urimelig å kreve at han ventet på selgerens retting eller omlevering.""",
        "hva_betyr_html": """<p>Loven gir selgeren rett til å rette opp — selv om du har krevd noe annet. Tanken: gi selgeren mulighet til å redde handelen før du krever prisavslag eller heving.</p>
<p><strong>Selgerens initiativ</strong> (første ledd): Selgeren kan tilby retting eller omlevering selv om du ikke har bedt om det. Vilkår:</p>
<ul>
<li>Det må ikke gi vesentlig ulempe for deg</li>
<li>Du må ikke risikere å tape penger på det</li>
</ul>
<p>Hvis du for eksempel allerede har skaffet noe annet og selgeren plutselig vil rette: det kan være ulempe nok.</p>
<p><strong>Stilltiende godkjenning</strong> (andre ledd): Hvis selgeren spør om du godtar retting eller varsler om at han vil rette innen en bestemt tid, og du ikke svarer innen rimelig tid — kan selgeren utføre arbeidet innen den fristen. Tausheten din regnes som godkjenning.</p>
<p><strong>Du kan fikse selv hvis det haster</strong> (tredje ledd): Hvis det er urimelig å vente på selgeren — for eksempel fordi du trenger varen til en bestemt dato — kan du fikse selv. Selgeren kan ikke etterpå hevde at han skulle hatt sjansen.</p>
<p><strong>Praktisk konsekvens:</strong> Hvis du krever prisavslag eller heving, må du som regel gi selgeren mulighet til å rette først. Han kan «redde» handelen ved å fikse. Først hvis han ikke gjør det, kan du gå videre til prisavslag eller heving (§ 37).</p>""",
        "eksempler": [
            {"navn": "Eva", "tekst": "Eva reklamerer på en oppvaskmaskin og krever prisavslag — hun synes det er en småfeil hun vil ha kompensert for. Selgeren svarer: «La meg fikse den i stedet.» Etter § 36 (1) har selgeren rett til å forsøke retting — så lenge det ikke gir Eva vesentlig ulempe. Eva må normalt akseptere det. Hvis rettingen ikke fungerer eller drar ut, har hun da rett til prisavslag eller heving (§ 37)."},
            {"navn": "Tom", "tekst": "Tom har reklamert på en symaskin. Selgeren skriver: «Jeg sender ut en tekniker neste fredag for å fikse.» Tom svarer ikke. Selgeren sender tekniker fredag — han er ute, ingen åpner. Selgeren krever ny avtale. Etter § 36 (2) har Tom i prinsippet «godkjent» rettingen ved å være taus. Han kan ikke senere si «jeg ville ikke ha retting». Selgeren har gjort som han sa."},
            {"navn": "Marius", "tekst": "Marius driver et lite serveringssted og oppdager at en ny kjølemaskin ikke virker — det er fredag, lørdag er kalkulert som hans største dag. Selgeren kan tidligst sende tekniker mandag. Marius leier en alternativ kjølemaskin for helgen og krever dekket kostnaden. Etter § 36 (3) kan Marius gå utenom selgeren — det var urimelig å vente. Han har krav på dekning av leiekostnaden som direkte tap."},
        ],
        "vanlige_feil": [
            "Krever prisavslag uten å gi selgeren mulighet til retting — selgeren kan motsette seg",
            "Lar være å svare på selgerens forslag — tausheten teller som ja",
            "Tar varen rett på verksted uten å si fra — selgeren kan nekte å dekke",
            "Som selger: prøver å rette i månedsvis uten å lykkes — det gir kjøperen rett til andre krav",
        ],
        "hva_bor_du_html": """<p><strong>Som kjøper:</strong></p>
<ul>
<li>Svar på selgerens forslag — ikke vær taus</li>
<li>Gi selgeren rimelig tid til å rette én gang</li>
<li>Hvis det haster: dokumenter hvorfor du måtte handle selv</li>
<li>Holdt dokumentasjon på alle forsøk</li>
</ul>
<p><strong>Som selger:</strong></p>
<ul>
<li>Tilby retting raskt og konkret</li>
<li>Spør tydelig om kjøperens godkjenning eller angi tidspunkt</li>
<li>Hvis kjøperen ikke svarer: gjør jobben innenfor den varslede tiden</li>
<li>Dokumenter forsøket</li>
</ul>""",
        "dumme_sporsmal": [
            {"q": "Må jeg gi selgeren mulighet til å rette flere ganger?", "a": "Som regel har selgeren rett til ett forsøk. Etter det kan du normalt gå over til prisavslag eller heving (se § 37)."},
            {"q": "Hva er «vesentlig ulempe» for meg som kjøper?", "a": "For eksempel: at varen må stå uten bruk i lang tid, at du må gå uten den i en periode du trenger den, at retting krever at du gjør noe upraktisk."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "34", "tittel": "Krav på retting og omlevering", "available": True},
            {"lov": "kjopsloven", "paragraf": "37", "tittel": "Prisavslag eller heving etter manglende retting", "available": True},
            {"lov": "kjopsloven", "paragraf": "38", "tittel": "Prisavslag", "available": True},
        ],
    },
    {
        "number": "37",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Prisavslag eller heving etter manglende retting",
        "description": "Hvis selgeren ikke retter mangelen — eller bruker for lang tid — kan du kreve prisavslag eller heve kjøpet.",
        "kort_svar": "Hvis retting eller omlevering ikke skjer — eller ikke skjer innen rimelig tid etter at du klaget — kan du gå videre og kreve prisavslag eller heve kjøpet. Du må ikke akseptere endeløse reparasjonsforsøk. Unntak: hvis du nekter et retteforsøk du faktisk plikter å motta (§ 36). Ved brukte ting kjøpt på auksjon kan du ikke kreve prisavslag.",
        "paragraftekst": """(1) Dersom retting eller omlevering ikke kommer på tale eller ikke blir foretatt innen rimelig tid etter at kjøperen har klaget over mangelen, kan kjøperen kreve prisavslag eller heve kjøpet etter §§ 38 eller 39. Dette gjelder ikke dersom kjøperen avslår avhjelp som han plikter å motta.

(2) Kjøperen kan ikke kreve prisavslag ved kjøp av brukte ting på auksjon.""",
        "hva_betyr_html": """<p>Du er ikke fanget i evig venting på at selgeren skal fikse. Loven setter en grense.</p>
<p><strong>To situasjoner som åpner for prisavslag/heving</strong> (første ledd):</p>
<ul>
<li>Retting kommer ikke på tale: selgeren nekter, ignorerer deg, eller varen kan ikke repareres</li>
<li>Retting drar ut: rettingen skjer ikke innen rimelig tid etter klage</li>
</ul>
<p>«Rimelig tid» varierer:</p>
<ul>
<li>Standardvare med deler tilgjengelig: 2-4 uker</li>
<li>Komplekst utstyr som krever spesialdeler: gjerne lenger</li>
<li>Sesongvare som må brukes nå: kortere</li>
</ul>
<p><strong>Du må ha akseptert lovlige forsøk</strong> (samme ledd, andre setning): Hvis selgeren tilbyr en rimelig rette-mulighet (etter § 36), kan du ikke nekte og deretter kreve prisavslag. Du må gi selgeren en sjanse — minst én — før du går videre.</p>
<p><strong>Auksjonsregelen</strong> (andre ledd): Brukte ting kjøpt på auksjon har en spesialregel: ikke prisavslag. Du kan fortsatt heve eller kreve erstatning, men ikke prisavslag. Tanken er at auksjonspris er en forhandlet pris og at justering er upraktisk.</p>
<h3>Sammenligning: Når kan du gå til prisavslag/heving?</h3>
<table class="rule-table">
<thead><tr><th>Situasjon</th><th>Prisavslag eller heving?</th></tr></thead>
<tbody>
<tr><td>Selgeren nekter å fikse</td><td>Ja</td></tr>
<tr><td>Selgeren har brukt urimelig lang tid</td><td>Ja</td></tr>
<tr><td>Selgeren har forsøkt retting som ikke virket</td><td>Ja</td></tr>
<tr><td>Selgeren tilbyr rimelig retting, du sier nei</td><td>Nei (først etter feilet forsøk)</td></tr>
<tr><td>Brukte ting på auksjon</td><td>Bare heving (ikke prisavslag)</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Lars", "tekst": "Lars har reklamert på en oppvaskmaskin. Selgeren sier «vi sender tekniker neste uke». Det skjer ikke. Lars purrer. Det går nye to uker. Lars purrer igjen. Etter seks uker har ingen kommet. Etter § 37 har Lars rett til å kreve prisavslag eller heve kjøpet. Selgeren har hatt rimelig tid og gjort ingenting. Lars trenger ikke vente lenger."},
            {"navn": "Ingrid", "tekst": "Ingrid har reklamert på en sofa. Selgeren tilbyr å sende ut polstrer som kan ordne mangelen — for selgers regning, neste uke. Ingrid sier «nei, jeg vil heller ha prisavslag». Selgeren har rett her. Tilbudet er rimelig og uten ulempe for Ingrid. Hun «plikter å motta» rettingen. Hvis hun nekter, kan hun ikke kreve prisavslag etter § 37 i denne omgang. Hvis polstrere kommer og det fortsatt ikke fungerer, har hun rett til prisavslag etter at retteforsøket har slått feil."},
            {"navn": "Tom", "tekst": "Tom kjøper en brukt traktor på auksjon for 95 000 kr. Han oppdager senere en mangel. Han kan ikke kreve prisavslag etter § 37 (2). Men han kan kreve retting, omlevering (hvis mulig), heving og erstatning."},
        ],
        "vanlige_feil": [
            "Krever prisavslag før selgeren har fått prøvd retting",
            "Aksepterer endeløse rette-forsøk uten å sette grense",
            "Tror du må vente «til selgeren er ferdig» — du må gi rimelig tid, ikke ubegrenset",
            "Glemmer at auksjonskjøp har egne regler",
        ],
        "hva_bor_du_html": """<p><strong>Praktisk fremgangsmåte:</strong></p>
<ol>
<li>Reklamer med krav om retting (§ 32, § 35)</li>
<li>Gi rimelig frist — 14-30 dager</li>
<li>Send påminnelse når halve fristen er gått</li>
<li>Når fristen er utløpt: send melding om at du nå krever prisavslag eller hever</li>
<li>Dokumenter alt</li>
</ol>
<p><strong>Mal for overgang:</strong></p>
<p><em>«Jeg reklamerte [dato] på mangelen [beskrivelse] og krevde retting. Frist ble satt til [dato]. Rettingen har ikke skjedd. Jeg krever derfor [prisavslag på X kr / hever kjøpet og krever pengene tilbake]. Jeg forbeholder meg krav på erstatning.»</em></p>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "34", "tittel": "Krav på retting og omlevering", "available": True},
            {"lov": "kjopsloven", "paragraf": "36", "tittel": "Selgerens rett til å rette", "available": True},
            {"lov": "kjopsloven", "paragraf": "38", "tittel": "Prisavslag", "available": True},
            {"lov": "kjopsloven", "paragraf": "39", "tittel": "Heving ved mangel", "available": True},
        ],
    },
    {
        "number": "38",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Hvordan prisavslag regnes ut",
        "description": "Prisavslag beregnes etter forholdet mellom varens verdi med mangel og verdi uten mangel — ikke etter reparasjonskostnaden alene.",
        "kort_svar": "Prisavslaget skal speile forholdet mellom hva varen er verdt med mangelen og hva den ville vært verdt uten. Formelen: ny pris / avtalt pris = mangelfull verdi / kontraktmessig verdi. I praksis brukes ofte reparasjonskostnaden som tilnærming, men selve regelen er forholdsmessig.",
        "paragraftekst": "Har tingen mangel, kan kjøperen kreve prisavslag slik at forholdet mellom nedsatt og avtalt pris svarer til forholdet mellom tingens verdi i mangelfull og kontraktmessig stand på leveringstiden.",
        "hva_betyr_html": """<p>Prisavslag handler om å gjenopprette balansen i handelen. Du har betalt for en vare som skulle hatt X-verdi. Du fikk en vare som har Y-verdi. Du skal betale i samme forhold.</p>
<p><strong>Formelen:</strong></p>
<p><em>Nedsatt pris / Avtalt pris = Mangelfull verdi / Kontraktmessig verdi</em></p>
<p>Eksempel: Du har betalt 100 000 kr. Uten mangel er varen verdt 100 000 kr. Med mangel er den verdt 80 000 kr. Da:</p>
<p><em>Nedsatt pris / 100 000 = 80 000 / 100 000</em><br>
<em>Nedsatt pris = 80 000 kr</em></p>
<p>Du har krav på 20 000 kr i prisavslag.</p>
<p><strong>Hvorfor ikke bare reparasjonskostnaden?</strong> Fordi reparasjon ikke alltid gir full gjenoppretting. En reparert vare kan være mindre verdt enn en feilfri. Prisavslag etter § 38 fanger den fulle verdireduksjonen.</p>
<p>I praksis brukes ofte reparasjonskostnaden som tilnærming når den er rimelig. Men hvis varen er gammel eller spesiell, kan verdivurdering avvike fra reparasjonskostnad.</p>
<p><strong>Tidspunktet:</strong> Verdien skal vurderes på leveringstiden — ikke i dag. Det betyr at sammenlikningen er kontraktmessig stand vs. mangelfull stand, begge på leveringstidspunktet.</p>
<h3>Sammenligning: Prisavslag vs. erstatning</h3>
<table class="rule-table">
<thead><tr><th>Type</th><th>Hva dekker det?</th></tr></thead>
<tbody>
<tr><td>Prisavslag (§ 38)</td><td>Verdiforskjellen i selve varen</td></tr>
<tr><td>Erstatning (§ 40)</td><td>Konkrete tap pga mangelen — utgifter, tapt fortjeneste</td></tr>
</tbody>
</table>
<p>Du kan kreve begge samtidig. Prisavslag gjelder selve varen; erstatning gjelder skadene mangelen påførte deg.</p>""",
        "eksempler": [
            {"navn": "Sara", "tekst": "Sara kjøper en brukt bil for 80 000 kr. Det viser seg at det er rust som verken hun eller selgeren visste om. Bilen er fortsatt brukbar, men en taksering viser at en rustfri tilsvarende bil ville vært verdt 80 000 kr, mens denne med rust er verdt 65 000 kr. Prisavslaget: Nedsatt pris / 80 000 = 65 000 / 80 000, altså Nedsatt pris = 65 000 kr. Sara har krav på 15 000 kr i prisavslag."},
            {"navn": "Tom", "tekst": "Tom kjøper en symaskin for 4 500 kr. Det viser seg at en av syl-funksjonene ikke virker. En tilsvarende modell uten den funksjonen koster 3 800 kr. Tom har krav på 700 kr i prisavslag (forskjellen mellom avtalt verdi og faktisk verdi). Reparasjon hadde kostet 1 200 kr — men det er verdiavslag etter § 38, ikke reparasjonsregning, som er hovedregelen. I praksis aksepterer ofte selgere reparasjonskostnaden hvis den er tilnærmet riktig."},
        ],
        "vanlige_feil": [
            "Tror prisavslag = reparasjonskostnad. Det er en tilnærming, ikke regelen",
            "Glemmer at verdien skal vurderes på leveringstidspunktet",
            "Tar med konsekvenstap (driftsavbrudd, ulemper) i prisavslaget — det hører til erstatning",
            "Som selger: tilbyr lite prisavslag basert på «hva som er rimelig» uten å regne forholdsvis",
        ],
        "hva_bor_du_html": """<p><strong>Som kjøper:</strong></p>
<ul>
<li>Få en uavhengig vurdering av verdien både med og uten mangel</li>
<li>Regn ut prisavslaget etter formelen</li>
<li>Vurder om reparasjonskostnaden er en god tilnærming</li>
<li>Krev erstatning i tillegg hvis du har hatt konkrete tap</li>
</ul>
<p><strong>Som selger:</strong></p>
<ul>
<li>Tilby et prisavslag som faktisk reflekterer verdiendringen</li>
<li>Du kan ofte slippe billigere med rask retting enn med stort prisavslag</li>
</ul>""",
        "dumme_sporsmal": [
            {"q": "Hvis varen er ubrukelig — er prisavslag = full pris?", "a": "Da snakker vi om heving, ikke prisavslag. Prisavslag forutsetter at du beholder varen. Hvis den er totalt ubrukelig, er heving rett krav (§ 39)."},
            {"q": "Kan jeg kreve prisavslag og retting?", "a": "Nei, ikke for samme mangel. Velg ett — eller la selgeren rette først, og kreve prisavslag for verditapet hvis rettingen er ufullkommen."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "30", "tittel": "Krav ved mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "34", "tittel": "Retting og omlevering", "available": True},
            {"lov": "kjopsloven", "paragraf": "37", "tittel": "Når du kan gå til prisavslag", "available": True},
            {"lov": "kjopsloven", "paragraf": "39", "tittel": "Heving ved mangel", "available": True},
        ],
    },
    {
        "number": "39",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Heving ved mangel",
        "description": "Du kan heve kjøpet hvis mangelen er vesentlig — men du må gi beskjed innen rimelig tid etter at du oppdaget eller burde oppdaget den.",
        "kort_svar": "Du kan heve kjøpet hvis mangelen utgjør vesentlig kontraktbrudd. Heving må du si fra om innen rimelig tid etter at du oppdaget eller burde oppdaget mangelen — eller etter at rette-/omleveringsforsøk har slått feil. Unntak: hvis selgeren har vært grovt uaktsom eller uærlig, bortfaller denne fristen.",
        "paragraftekst": """(1) Kjøperen kan heve kjøpet dersom mangelen medfører vesentlig kontraktbrudd.

(2) Kjøperen kan ikke heve kjøpet med mindre han gir selgeren melding om heving innen rimelig tid etter at han fikk eller burde ha fått kjennskap til mangelen, eller etter utløpet av den frist som kan følge av krav eller melding etter §§ 34 eller 36. Dette gjelder likevel ikke dersom selgeren har opptrådt grovt aktløst eller for øvrig i strid med redelighet og god tro.""",
        "hva_betyr_html": """<p>Heving er den sterkeste reaksjonen ved mangel. Kjøpet kanselleres, du gir tilbake varen, og pengene kommer tilbake.</p>
<p><strong>Vilkår: vesentlig kontraktbrudd</strong> (første ledd): Mangelen må være alvorlig nok til å rive opp hele handelen. Vurderingen avhenger av:</p>
<ul>
<li>Hvor mye varens verdi er redusert</li>
<li>Om varen kan brukes til formålet</li>
<li>Om mangelen kan rettes — og hvor god rettingen er</li>
<li>Hvor mye ulempe mangelen har påført deg</li>
<li>Forholdet mellom partene</li>
</ul>
<p>Småfeil holder ikke. Avvikende farge på et detaljnivå holder sannsynligvis ikke. En motor som ikke virker, eller en sofa som er upraktisk for hovedformålet, kan derimot kvalifisere.</p>
<p><strong>Tidsfrist</strong> (andre ledd): Du må gi beskjed innen rimelig tid etter:</p>
<ul>
<li>At du oppdaget mangelen (eller burde ha oppdaget den)</li>
<li>Eller etter at retting/omlevering har feilet (§§ 34, 36)</li>
</ul>
<p>Hva er rimelig? Som regel dager til noen få uker. Venter du for lenge, taper du hevingsretten — selv om mangelen ellers var vesentlig.</p>
<p><strong>Unntak ved uærlighet:</strong> Hvis selgeren har vært grovt uaktsom eller uærlig, gjelder ikke fristen. Du kan da heve uavhengig.</p>
<h3>Sammenligning: Når kan du heve?</h3>
<table class="rule-table">
<thead><tr><th>Situasjon</th><th>Heving mulig?</th></tr></thead>
<tbody>
<tr><td>Liten kosmetisk feil</td><td>Sjelden — sannsynligvis prisavslag eller retting</td></tr>
<tr><td>Funksjonsfeil som kan rettes</td><td>Først etter feilet retting (§ 37)</td></tr>
<tr><td>Funksjonsfeil som ikke kan rettes</td><td>Ja, hvis vesentlig</td></tr>
<tr><td>Selgeren har skjult vesentlig informasjon</td><td>Ja, uten frist</td></tr>
<tr><td>Varen er totalt ubrukelig</td><td>Ja</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Eva", "tekst": "Eva har kjøpt en symaskin for 8 500 kr. Etter to uker oppdager hun at hovedfunksjonen ikke virker. Hun reklamerer og selgeren sender ut tekniker — flere ganger. Maskinen virker fortsatt ikke etter tre forsøk over tre måneder. Eva kan nå heve etter § 39. Mangelen er vesentlig (hovedfunksjonen virker ikke), og rette-forsøkene har slått feil. Hun må sende skriftlig hevingsmelding raskt etter at hun konkluderer med at retting ikke fungerer."},
            {"navn": "Tom", "tekst": "Tom kjøper en brukt bil for 130 000 kr. Tre måneder senere oppdager han at den har vært totalvraket og bygget opp igjen. Selgeren hadde holdt dette skjult. Mangelen er åpenbart vesentlig — en vraket bil er ikke det Tom kjøpte. Selgeren har handlet i strid med god tro (§ 19 b, § 33). Fristen i § 39 (2) gjelder ikke — Tom kan heve selv etter lengre tid, så lenge bevisene er der."},
        ],
        "vanlige_feil": [
            "Hever på små mangler — selgeren kan motsette seg",
            "Hever uten å ha gitt selgeren mulighet til retting — kan slå tilbake",
            "Venter for lenge med å sende hevingsmelding etter at retting har slått feil",
            "Bruker varen videre etter at heving er meldt — det signaliserer aksept",
        ],
        "hva_bor_du_html": """<p><strong>Steg for steg ved heving:</strong></p>
<ol>
<li>Sørg for at mangelen er vesentlig — dokumenter med bilder, takst, vurdering</li>
<li>Reklamer først med krav om retting/omlevering (§ 32, § 35)</li>
<li>Vent ut rimelig frist for selgerens forsøk</li>
<li>Send hevingsmelding skriftlig når det er klart at retting ikke skjer eller har slått feil</li>
<li>Ikke bruk varen videre</li>
<li>Ordne tilbakelevering når selgeren bekrefter</li>
<li>Krev erstatning for konkrete tap i tillegg (§ 40)</li>
</ol>
<p><strong>Mal for hevingsmelding:</strong></p>
<p><em>«Jeg viser til mangelen som ble reklamert [dato]. Retting har ikke ført frem / har ikke skjedd innen rimelig tid. Jeg hever herved kjøpet i medhold av kjøpsloven § 39. Jeg krever full tilbakebetaling av kjøpesummen [X kr]. Jeg har varen klar for tilbakelevering.»</em></p>""",
        "dumme_sporsmal": [
            {"q": "Hva er forskjellen på prisavslag og heving?", "a": "Prisavslag: du beholder varen, betaler mindre. Heving: kjøpet rives opp, du gir tilbake varen, får pengene tilbake."},
            {"q": "Når må jeg heve — innen hvor lang tid?", "a": "Innen rimelig tid etter at det er klart at retting ikke skjer eller har slått feil. Dager til noen få uker er normalt trygt. Lenger er risikabelt."},
            {"q": "Kan jeg heve og kreve erstatning?", "a": "Ja. Erstatning kommer alltid i tillegg til andre krav (§ 30)."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "25", "tittel": "Heving ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "30", "tittel": "Krav ved mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "37", "tittel": "Prisavslag eller heving etter manglende retting", "available": True},
            {"lov": "kjopsloven", "paragraf": "40", "tittel": "Erstatning ved mangel", "available": True},
        ],
    },
    {
        "number": "40",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Erstatning ved mangel",
        "description": "Du kan kreve erstatning for tap mangelen påførte deg. Indirekte tap krever sterkere grunnlag. Hvis selgeren har vært uaktsom eller gitt garanti, dekkes mer.",
        "kort_svar": "Du har krav på erstatning for tap som mangelen påførte deg. Selgeren slipper bare hvis han kan vise at mangelen skyldtes en hindring utenfor hans kontroll. Indirekte tap (tapt fortjeneste, driftsavbrudd) dekkes kun hvis selgeren har vært uaktsom eller har gitt løfter om varens egenskaper.",
        "paragraftekst": """(1) Kjøperen kan kreve erstatning for det tap han lider som følge av mangel ved tingen, for så vidt selgeren ikke godtgjør at det forhold at leveringen er mangelfull, skyldes hindring som nevnt i § 27. Reglene ellers i §§ 27 og 28 gjelder tilsvarende.

(2) Reglene i første ledd omfatter ikke slikt indirekte tap som nevnt i § 67 (2).

(3) Kjøperen kan i alle høve kreve erstatning dersom (a) mangelen eller tapet skyldes feil eller forsømmelse fra selgers side eller (b) tingen allerede på avtaletiden avvek fra det som er tilsikret av selgeren.""",
        "hva_betyr_html": """<p>Mangelen kan ha kostet deg mer enn bare reduksjonen i varens verdi. Du måtte kjøpe noe annet, leie noe i mellomtiden, fikse skader. Den ekstrabelastningen kan du kreve erstattet.</p>
<p><strong>Hovedregel</strong> (første ledd): Strengt ansvar (kontrollansvar). Selgeren må betale for tapet — han slipper bare hvis han kan vise at mangelen skyldes en hindring utenfor hans kontroll, som han ikke kunne forutse eller unngå. Det er sjelden at en mangel i en vare oppfyller dette — produsenten skal kontrollere det.</p>
<p>Direkte tap dekkes — ekstra utgifter knyttet direkte til mangelen.</p>
<p><strong>Indirekte tap dekkes ikke under hovedregelen</strong> (andre ledd). Hva er indirekte tap?</p>
<ul>
<li>Tapt fortjeneste fra kontrakter du ikke kunne oppfylle</li>
<li>Driftsavbrudd</li>
<li>Avsavn (ulempe fordi du ikke kunne bruke varen som forutsatt)</li>
<li>Følgeskader på andre ting</li>
</ul>
<p>For å få indirekte tap dekket må du gå inn under tredje ledd:</p>
<p><strong>Unntak</strong> (tredje ledd):</p>
<ul>
<li><strong>(a) Uaktsomhet eller feil:</strong> Selgeren har vært uaktsom eller gjort feil. Da kan du kreve alt — også indirekte tap.</li>
<li><strong>(b) Tilsikrede egenskaper:</strong> Selgeren har gått god for at varen har bestemte egenskaper, og det stemte ikke. Da kan du også kreve alt.</li>
</ul>
<h3>Sammenligning: Hvilket grunnlag for hvilken erstatning?</h3>
<table class="rule-table">
<thead><tr><th>Type tap</th><th>Grunnlag</th></tr></thead>
<tbody>
<tr><td>Ekstra reparasjon (direkte)</td><td>§ 40 (1) — kontrollansvar</td></tr>
<tr><td>Mellomlegg ved dekningskjøp (direkte)</td><td>§ 40 (1)</td></tr>
<tr><td>Leiekostnader mens varen er borte (direkte)</td><td>§ 40 (1)</td></tr>
<tr><td>Tapt fortjeneste (indirekte)</td><td>§ 40 (3) — krever uaktsomhet eller tilsikrede egenskaper</td></tr>
<tr><td>Driftsavbrudd (indirekte)</td><td>§ 40 (3)</td></tr>
<tr><td>Skade på andre ting (indirekte)</td><td>§ 40 (3)</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Sara", "tekst": "Sara kjøper et nytt kjøleskap. Det viser seg å være feilkonstruert — temperaturen er for høy. Hun mister mat for 2 500 kr og må kjøpe iskasse for 800 kr mens reparasjon pågår. Etter § 40 (1) kan Sara kreve disse 3 300 kr som direkte tap. Selgeren kan ikke vise at feilkonstruksjonen var utenfor hans kontroll — det er en produsentfeil. Sara får erstatning."},
            {"navn": "Ola", "tekst": "Ola driver en liten produksjonsbedrift. Han kjøper en spesialmaskin som viser seg å være mangelfull. Produksjonen står stille i to uker mens reparasjon pågår. Tapt fortjeneste: 65 000 kr. Tapt fortjeneste er indirekte tap (§ 67 (2) bokstav c). Det dekkes ikke av § 40 (1). For å få det dekket må Ola vise enten selgerens uaktsomhet eller at selgeren hadde gått god for at maskinen ville fungere på en bestemt måte."},
        ],
        "vanlige_feil": [
            "Krever indirekte tap uten å vise uaktsomhet eller garantipåstander",
            "Som selger: tror du slipper unna fordi mangelen var «din leverandørs feil» — det holder ikke, du har strengt ansvar",
            "Glemmer å begrense eget tap (§ 70)",
            "Tar med «ergrelse» og «stress» — vanskelig å få dekket uten dokumentert økonomisk tap",
        ],
        "hva_bor_du_html": """<p><strong>Dokumentasjon er alt:</strong></p>
<ul>
<li>Kvitteringer for ekstrautgifter</li>
<li>Korrespondanse om mangelen</li>
<li>Vurdering fra fagperson om mangelens art</li>
<li>Eventuelle markedsføringspåstander fra selgeren (om bokstav b)</li>
<li>Bevis på uaktsomhet (om bokstav a)</li>
</ul>
<p><strong>Skriftlig erstatningskrav:</strong></p>
<p><em>«Jeg krever erstatning for følgende tap som følge av mangelen ved [vare]: [spesifiser hvert tap med beløp og dokumentasjon]. Totalt: [sum] kr. Vedlagt følger dokumentasjon. Beløpet bes innbetalt innen 14 dager.»</em></p>""",
        "dumme_sporsmal": [
            {"q": "Kan jeg kreve erstatning og prisavslag samtidig?", "a": "Ja. Prisavslag dekker verdiforskjellen i varen. Erstatning dekker dine ekstrakostnader. Det er to ulike ting."},
            {"q": "Hvor langt går «direkte tap»?", "a": "Det som er en umiddelbar konsekvens av mangelen, og som kan dokumenteres økonomisk. Reparasjon, dekningskjøp, ekstra frakt. Ikke det som er ringvirkninger over tid."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "27", "tittel": "Erstatning ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "30", "tittel": "Krav ved mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "67", "tittel": "Omfanget av erstatning", "available": False},
            {"lov": "kjopsloven", "paragraf": "70", "tittel": "Plikt til å begrense tap", "available": False},
        ],
    },
    {
        "number": "41",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Når en tredjeperson har rettigheter i varen",
        "description": "Har noen andre eiendomsrett, panterett eller annen rett i varen du har kjøpt? Det er en rettsmangel — og du har samme krav som ved andre mangler.",
        "kort_svar": "Hvis det viser seg at noen andre har rettigheter i varen — for eksempel pant, eiendomsrett eller en patentrett som rammer din bruk — er det en «rettsmangel». Du har samme krav som ved andre mangler. Reklamasjon må gjøres innen rimelig tid, men toårsfristen gjelder ikke. Du har alltid krav på erstatning for tap du ikke kunne forutse.",
        "paragraftekst": """(1) Har tredjemann eiendomsrett, panterett eller annen rett i tingen (rettsmangel), gjelder reglene om mangler tilsvarende dersom det ikke følger av avtalen at kjøperen skal overta tingen med den begrensning tredjemanns rett medfører. Toårsfristen for reklamasjon i § 32 (2) gjelder likevel ikke.

(2) Kjøperen kan i alle høve kreve erstatning for tap som følge av rettsmangel som forelå ved kjøpet og som han verken kjente eller burde ha kjent til.

(3) Gjør tredjemann krav på å ha rett i tingen og dette bestrides, gjelder reglene i første og andre ledd tilsvarende når kravet ikke er klart ugrunnet.

(4) For tredjemannskrav som bygger på immaterialrett gjelder reglene i første ledd tilsvarende.""",
        "hva_betyr_html": """<p>Du har kjøpt en vare og tror den er fri og din. Så viser det seg at noen andre har et krav i varen. Det er en «rettsmangel» — ikke en feil ved tingen selv, men en juridisk byrde du ikke visste om.</p>
<p><strong>Tre typiske eksempler:</strong></p>
<ul>
<li><strong>Pant:</strong> Bilen du kjøpte har et pant tinglyst fra forrige eier — banken har sikkerhet i bilen</li>
<li><strong>Eiendomsrett:</strong> Den du kjøpte av, var ikke egentlig eier — han hadde lånt eller stjålet varen</li>
<li><strong>Immaterielle rettigheter:</strong> Produktet bryter et patent eller varemerke som en tredjepart eier (fjerde ledd)</li>
</ul>
<p><strong>Hovedregel</strong> (første ledd): Samme krav som ved andre mangler — retting, omlevering, prisavslag, heving, erstatning. Unntak: hvis dere har avtalt at du skal overta tingen med den begrensningen tredjemanns rett medfører (typisk: du visste om pantet og betalte mindre).</p>
<p><strong>Ingen toårsfrist:</strong> Den absolutte toårsfristen i § 32 (2) gjelder ikke for rettsmangler. Logikken: en rettsmangel kan ligge skjult i tiår uten å bli synlig.</p>
<p><strong>Du har alltid rett til erstatning</strong> (andre ledd) for tap fra rettsmangel som var der ved kjøpet, og som du ikke kjente til eller burde kjent til. Dette er sterkere enn vanlig erstatning — du trenger ikke vise selgerens uaktsomhet.</p>
<p><strong>Omstridt krav</strong> (tredje ledd): Hvis tredjepart hevder å ha rett, og det bestrides, gjelder reglene «når kravet ikke er klart ugrunnet». Du må altså ikke vente på endelig dom — det holder at kravet er reelt.</p>
<p><strong>Immaterialrett</strong> (fjerde ledd): Patent, varemerke, opphavsrett — samme regler gjelder.</p>""",
        "eksempler": [
            {"navn": "Petter", "tekst": "Petter kjøper en brukt bil for 95 000 kr fra Lars. Tre måneder senere får han brev fra banken: bilen har et tinglyst pant på 40 000 kr fra Lars sin tid som eier. Pantet er fortsatt aktivt fordi Lars ikke har innfridd gjelden. Dette er en rettsmangel etter § 41. Petter kan kreve at Lars rydder opp i pantet, prisavslag tilsvarende verdiforringelsen, heving hvis pantet er vesentlig, eller erstatning. Toårsfristen i § 32 gjelder ikke."},
            {"navn": "Anne", "tekst": "Anne kjøper et brukt kamera fra Tom for 18 000 kr. Tre uker senere kommer politiet og sier kameraet er stjålet — eieren krever det tilbake. Tom hadde ingen eiendomsrett å overføre. Det er en rettsmangel etter § 41 (1). Hun mister kameraet og kan kreve full erstatning fra Tom etter § 41 (2): pengene tilbake pluss eventuelt direkte tap."},
            {"navn": "Marius", "tekst": "Marius driver en liten elektronikkbutikk og importerer en spesialprodukt fra Asia. Han selger noen før han får krav fra en patentinnehaver: produktet bryter et europeisk patent. Etter § 41 (4) er det en rettsmangel — selv om varen i seg selv er feilfri. Marius kan kreve omlevering, prisavslag, heving, eller erstatning fra sin leverandør."},
        ],
        "vanlige_feil": [
            "Forveksler rettsmangel med vanlig mangel — fristene er ulike",
            "Tror toårsfristen gjelder også for rettsmangler — den gjør ikke",
            "Som kjøper: glemmer å sjekke om bilen har pant før kjøp — det kan du selv unngå",
            "Som selger: glemmer å informere om eksisterende heftelser",
        ],
        "hva_bor_du_html": """<p><strong>Som kjøper:</strong></p>
<ul>
<li>Sjekk pantsetting før du kjøper bil eller annet stort — det går å gjøre i Brønnøysundregistrene/Statens vegvesen</li>
<li>Forsikre deg om eierforhold — vis ID, sjekk vognkort, be om dokumentasjon</li>
<li>Reklamer raskt når rettsmangelen oppdages</li>
<li>Krev både retting og erstatning hvis aktuelt</li>
</ul>
<p><strong>Som selger:</strong></p>
<ul>
<li>Vær åpen om alle heftelser</li>
<li>Rydd opp i pant før salg</li>
<li>Hvis du selger med kjente begrensninger, skriv det tydelig i avtalen</li>
</ul>""",
        "dumme_sporsmal": [
            {"q": "Hva er forskjellen på rettsmangel og vanlig mangel?", "a": "Vanlig mangel = noe galt med tingen selv. Rettsmangel = noe galt med rettighetene til tingen. Reglene er like, men frister og bevisbyrde varierer noe."},
            {"q": "Trenger jeg å sjekke pant på alt jeg kjøper?", "a": "For dyre ting som bil, båt, snøscooter — ja, klart. For mindre kjøp er det normalt ikke verdt det."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "30", "tittel": "Krav ved mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "32", "tittel": "Reklamasjonsfrister", "available": True},
            {"lov": "kjopsloven", "paragraf": "40", "tittel": "Erstatning ved mangel", "available": True},
        ],
    },
    {
        "number": "42",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Din rett til å holde tilbake betaling",
        "description": "Når selgeren har gjort kontraktbrudd, kan du holde tilbake så mye av betalingen at det dekker kravet ditt — som press for å få ordnet saken.",
        "kort_svar": "Hvis selgeren har gjort et kontraktbrudd — forsinkelse eller mangel — kan du holde tilbake så mye av betalingen at det sikrer at du får dekket kravet ditt. Det er det viktigste pressmiddelet du har. Du må bare holde tilbake et rimelig beløp — ikke hele kjøpesummen for en småfeil.",
        "paragraftekst": "Har kjøperen krav som følger av selgerens kontraktbrudd, kan kjøperen holde tilbake så mye av kjøpesummen som vil sikre at han får kravet dekket.",
        "hva_betyr_html": """<p>Hvis du fortsatt skylder penger til selgeren — typisk på faktura — og selgeren har misligholdt på en eller annen måte, kan du la være å betale hele beløpet. Du holder tilbake nok til å dekke kravet ditt.</p>
<p><strong>To forutsetninger:</strong></p>
<ul>
<li><strong>Du må ha et krav:</strong> Forsinkelse, mangel, erstatningskrav — noe konkret du kan vise til.</li>
<li><strong>Beløpet må stå i forhold til kravet:</strong> Hvis du har et krav på 5 000 kr, kan du ikke holde tilbake 50 000 kr. Du må holde tilbake et beløp som er rimelig sammenliknet med kravet, men gjerne med en margin.</li>
</ul>
<p><strong>Hvorfor er dette så viktig?</strong> Tilbakeholdsrett er det praktiske pressmiddelet i kjøpsretten. Når penger fortsatt er hos deg, har selgeren incitament til å løse saken. Når pengene er borte, må du jakte på dem.</p>
<p><strong>Du må kommunisere:</strong> Hold tilbake skriftlig, og fortell selgeren hvorfor. Skjult tilbakeholdelse ser ut som mislighold fra din side.</p>
<h3>Sammenligning: Hvor mye kan du holde tilbake?</h3>
<table class="rule-table">
<thead><tr><th>Kravets størrelse</th><th>Anbefalt tilbakeholdelse</th></tr></thead>
<tbody>
<tr><td>800 kr småfeil</td><td>1 000-2 000 kr (margin)</td></tr>
<tr><td>8 000 kr reparasjon</td><td>10 000-12 000 kr</td></tr>
<tr><td>Hele varen ubrukelig</td><td>Hele restbetalingen</td></tr>
<tr><td>Ukjent omfang ennå</td><td>Et rimelig anslag</td></tr>
</tbody>
</table>""",
        "eksempler": [
            {"navn": "Lars", "tekst": "Lars har bestilt et badekar for 24 000 kr. Han har betalt 12 000 kr i forskudd. Resten skal betales ved levering. Badekaret kommer, men det er en mangel — overflaten har en stor flekk som krever profesjonell polering for 4 000 kr. Lars kan holde tilbake et beløp som dekker kravet. Han skriver: «Jeg holder tilbake 5 000 kr av sluttbetalingen til mangelen er ordnet. Resten betaler jeg i dag.» Det er rimelig — tilstrekkelig til å dekke kostnaden med en liten margin."},
            {"navn": "Eva", "tekst": "Eva har bestilt nye dører for 45 000 kr, med 15 000 kr betalt i forskudd. Dørene skulle leveres 1. mai, det er 1. juli og fortsatt ingen levering. Eva må leie midlertidig løsning for 8 000 kr. Når dørene endelig leveres, kan Eva holde tilbake 8 000 kr i restbetalingen for å sikre erstatningskravet."},
            {"navn": "Tom", "tekst": "Tom har kjøpt en oppvaskmaskin for 9 500 kr. Det er en småfeil som koster 800 kr å rette. Tom har betalt 5 000 kr, og skylder 4 500 kr. Han bestemmer seg for å ikke betale noe. Det er trolig urimelig. Holder han tilbake 4 500 kr for en 800 kr feil, kan selgeren si at Tom misligholder selv. Da risikerer Tom forsinkelsesrente og andre konsekvenser."},
        ],
        "vanlige_feil": [
            "Holder tilbake hele beløpet for små feil — kan bli ansett som mislighold",
            "Holder tilbake i taushet — fortell selgeren hvorfor",
            "Holder tilbake uten å ha et konkret krav",
            "Glemmer å vise dokumentasjon på kravet",
        ],
        "hva_bor_du_html": """<p><strong>Når du holder tilbake:</strong></p>
<ol>
<li>Vurder kravet ditt: hva har du krav på i kroner?</li>
<li>Sett et rimelig beløp med margin — 25-50% over selve kravet</li>
<li>Send skriftlig beskjed til selgeren med begrunnelse</li>
<li>Betal det du faktisk skylder — ikke hold tilbake mer enn nødvendig</li>
<li>Frigjør pengene når selgeren har ordnet saken</li>
</ol>
<p><strong>Mal:</strong></p>
<p><em>«Jeg viser til [vare/avtale]. På grunn av [forsinkelse / mangel] som jeg har reklamert på [dato], holder jeg tilbake [beløp] kr av kjøpesummen i medhold av kjøpsloven § 42. Det resterende beløpet på [X kr] betaler jeg [dato]. Det tilbakeholdte beløpet frigjøres når [konkret betingelse].»</em></p>""",
        "dumme_sporsmal": [
            {"q": "Kan jeg holde tilbake hvis jeg allerede har betalt?", "a": "Nei — det er da heller «krav om tilbakebetaling» du må reise. Tilbakeholdsrett forutsetter at det fortsatt er penger hos deg."},
            {"q": "Hva med kortbetaling som allerede er trukket?", "a": "Pengene er hos selgeren. Da må du heller reise krav om tilbakeføring eller krav på kjøpsloven andre regler."},
        ],
        "related": [
            {"lov": "kjopsloven", "paragraf": "10", "tittel": "Selgerens motsvarende tilbakeholdsrett", "available": True},
            {"lov": "kjopsloven", "paragraf": "22", "tittel": "Krav ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "30", "tittel": "Krav ved mangel", "available": True},
        ],
    },
    {
        "number": "43",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Mangel ved bare en del av varen",
        "description": "Hvis bare en del av leveransen har feil, gjelder mangelreglene for den delen. Hev hele kjøpet bare hvis bruddet er vesentlig for det hele.",
        "kort_svar": "Hvis bare en del av varen har mangel, gjelder mangelsreglene for den delen. Du kan heve hele kjøpet bare hvis kontraktbruddet er vesentlig for hele leveransen. Hvis selgeren har antatt levering ferdig selv om det mangler noe, behandles dette som en mangel.",
        "paragraftekst": """(1) Gjelder selgerens kontraktbrudd bare en del av det solgte, får reglene i kapitlet her anvendelse på denne del. Kjøperen kan heve kjøpet i sin helhet når kontraktbruddet er vesentlig for hele kjøpet.

(2) Må selgeren etter forholdene antas å ha avsluttet sin levering enda ikke alt er levert, får reglene om mangler anvendelse.""",
        "hva_betyr_html": """<p>Du har bestilt 100 stoler. 80 er perfekte, 20 har feil. Hva nå?</p>
<p><strong>Mangelsreglene gjelder den delen som er gal</strong> (første ledd): De 20 stolene utløser krav — retting, omlevering, prisavslag for de stolene, heving for de stolene, erstatning.</p>
<p><strong>Heving av hele kjøpet:</strong> Du kan bare heve hele kjøpet hvis mangelen i 20 stoler gjør at hele bestillingen er meningsløs. Trenger du alle 100 til et arrangement og 80 ikke er nok — kan det være vesentlig. Trenger du dem til hver sin bruk — sannsynligvis ikke.</p>
<p><strong>Avsluttet levering</strong> (andre ledd): Hvis selgeren har antatt at han er ferdig med å levere, men det mangler ting — for eksempel manglet 5 stoler, men selgeren har avsluttet — behandles det som mangel. Du har de samme kravene.</p>""",
        "eksempler": [
            {"navn": "Ingrid", "tekst": "Ingrid har bestilt 50 kontorstoler. 45 leveres perfekte, 5 har skader. Reklamasjon viser at de fem skal omleveres. Ingrid har krav på omlevering for de fem etter § 43 (1). Hun kan ikke heve hele leveransen — de 45 perfekte stolene er fortsatt brukbare. Hvis hun hadde bestilt stolene til et bestemt arrangement der hun trenger alle 50 samme dag, og selgeren ikke får omlevert i tide, kan formålet med hele kjøpet være vesentlig forfeilet — og hun kan heve alt."},
            {"navn": "Marius", "tekst": "Marius har bestilt et nytt kjøkken — skap, benkeplate, vask, oppvaskmaskin. Skap og benkeplate kommer perfekt. Vasken er feil farge, og oppvaskmaskinen mangler hjul. Marius kan kreve retting eller omlevering for de delene som er gale. Han kan ikke heve hele kjøpet — skapene fungerer. Han kan ha krav på et lite prisavslag eller erstatning hvis det medfører ulempe."},
        ],
        "vanlige_feil": [
            "Krever heving av hele bestillingen for små del-mangler",
            "Glemmer at man kan ha krav på forskjellige reaksjoner for ulike deler",
            "Tror «alt eller ingenting» — det er nyansert i loven",
        ],
        "hva_bor_du_html": """<ul>
<li>Spesifiser nøyaktig hvilke deler som har mangel</li>
<li>Krev tilsvarende — retting, omlevering — for hver del</li>
<li>Vurder om mangelen påvirker bruken av resten</li>
<li>Heving av alt krever vesentlig betydning for hele</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "30", "tittel": "Krav ved mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "39", "tittel": "Heving ved mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "44", "tittel": "Levering etter hvert", "available": True},
        ],
    },
    {
        "number": "44",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Levering i flere omganger",
        "description": "Skal varen leveres i flere omganger? Du kan heve den enkelte leveringen — og noen ganger fremtidige eller tidligere leveringer som henger sammen.",
        "kort_svar": "Hvis varen skal leveres i flere omganger og det er kontraktbrudd ved en av dem, kan du heve akkurat den leveringen etter de vanlige reglene. Du kan også heve fremtidige leveringer hvis bruddet gir grunn til å tro at det vil bli problemer igjen. Og du kan heve tidligere og senere leveringer som ikke gir mening hver for seg — for eksempel en serie som henger sammen.",
        "paragraftekst": """(1) Skal selgeren levere etter hvert og er det kontraktbrudd ved en enkelt dellevering, kan kjøperen heve for denne levering etter reglene om heving.

(2) Gir kontraktbruddet kjøperen god grunn til å rekne med at det vil inntre kontraktbrudd som vil gi hevingsrett ved seinere leveringer, kan han på dette grunnlag heve for slike leveringer dersom det skjer innen rimelig tid.

(3) Dersom kjøperen hever for en enkelt levering, kan han samtidig heve kjøpet for tidligere eller seinere leveringer som på grunn av sammenhengen mellom leveringene ikke vil kunne brukes til formål som partene forutsatte på avtaletiden.""",
        "hva_betyr_html": """<p>Mange avtaler innebærer levering over tid — abonnement, månedlige leveranser, et større oppdrag som leveres i puljer. Loven har egne regler for dette.</p>
<p><strong>Heving av én levering</strong> (første ledd): Hvis en enkelt leveranse er for sen eller har vesentlig mangel, kan du heve akkurat den. Du beholder resten av avtalen.</p>
<p><strong>Heve fremtidige leveringer</strong> (andre ledd): Hvis bruddet gir deg «god grunn» til å tro at det vil bli problemer også senere, kan du si nei takk til fremtidige leveringer. Du må handle «innen rimelig tid». Eksempel: leverandøren leverer tre måneder for sent i januar, igjen i februar, og du ser ikke bedring — du kan si: «Jeg trekker meg fra avtalen, jeg vil ikke ha mer.»</p>
<p><strong>Tidligere og senere leveringer som henger sammen</strong> (tredje ledd): Hvis du hever for én levering, kan du også heve tidligere eller senere leveringer som ikke gir mening uten den. Eksempel: en serie bøker der bind 3 mangler — du kan heve hele serien hvis det ikke gir mening med bare 1, 2, 4 og 5.</p>""",
        "eksempler": [
            {"navn": "Lars", "tekst": "Lars driver et lite snekkerverksted og har avtale om månedlig levering av eik. Tredjegangslevering kommer en måned for sent, fjerdegangslevering er av dårlig kvalitet. Femtegangslevering ser ut til å bli sen igjen. Lars kan etter § 44 (2) heve for fremtidige leveringer — bruddene gir grunn til å tro at problemer fortsetter. Han varsler skriftlig og finner ny leverandør."},
            {"navn": "Eva", "tekst": "Eva har bestilt en samlerserie på 10 bind. Bind 1-5 er perfekte. Bind 6 har trykkfeil og er ubrukelig. Etter retteforsøk leveres ikke en feilfri bind 6. Eva kan heve for bind 6 etter § 44 (1). Hun kan også heve hele serien etter § 44 (3) hvis den ikke gir mening uten bind 6 — det er et samlerverk hvor sammenhengen er viktig."},
        ],
        "vanlige_feil": [
            "Hever hele avtalen for én dårlig levering uten å vurdere § 44",
            "Venter for lenge med å heve fremtidige leveringer — du må handle innen rimelig tid",
            "Glemmer at «henger sammen»-regelen krever at sammenhengen var forutsatt fra start",
        ],
        "hva_bor_du_html": """<p>Ved problemer i abonnement eller seriekontrakter:</p>
<ul>
<li>Reklamer på den enkelte leveransen</li>
<li>Hvis mønster: send skriftlig melding om at du trekker deg fra fremtidige leveringer</li>
<li>Krev erstatning for konkrete merkostnader</li>
<li>Hvis serien henger sammen: vurder om hele kjøpet bør heves</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "25", "tittel": "Heving ved forsinkelse", "available": True},
            {"lov": "kjopsloven", "paragraf": "39", "tittel": "Heving ved mangel", "available": True},
            {"lov": "kjopsloven", "paragraf": "43", "tittel": "Mangel ved del av varen", "available": True},
        ],
    },
    {
        "number": "45",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Pris når avtalen er stille",
        "description": "Hvis ingen pris er avtalt, skal du betale gjengs pris — det vanlige nivået for slik vare. Hvis det ikke finnes gjengs pris, må prisen være rimelig.",
        "kort_svar": "Hvis du har inngått et kjøp uten å avtale pris, skal du betale «gjengs pris» — det normale prisnivået på avtaletidspunktet for tilsvarende vare. Hvis det ikke finnes en gjengs pris, skal prisen være rimelig ut fra varens art og kvalitet. Urimelige priser binder ikke.",
        "paragraftekst": "Er kjøp inngått uten at prisen følger av avtalen, skal kjøperen betale gjengs pris på avtaletiden for samme slags ting solgt under tilsvarende forhold, for så vidt prisen ikke er urimelig. Er det ingen slik gjengs pris, må kjøperen betale det som er rimelig under omsyn til tingens art og godhet og tilhøva ellers.",
        "hva_betyr_html": """<p>Det er overraskende vanlig å handle uten å avtale eksakt pris — særlig mellom bedrifter med løpende kundeforhold, eller når man bestiller spesialarbeid. Loven svarer på hva som skjer da.</p>
<p><strong>To regler:</strong></p>
<ul>
<li><strong>Gjengs pris:</strong> Hvis varen omsettes regelmessig og det finnes et normalt prisnivå, gjelder det. Eksempel: standardvirke fra en grossist har en gjengs pris. Tilsvarende kunder, tilsvarende forhold.</li>
<li><strong>Rimelig pris:</strong> Hvis det ikke finnes gjengs pris — særlig for unike eller spesialiserte varer — skal prisen være «rimelig» ut fra varens art og godhet. Det er en bredere vurdering: kvalitet, vanskelighetsgrad, marked.</li>
</ul>
<p><strong>Urimelige priser binder ikke:</strong> Selv om det finnes en «gjengs pris», binder den ikke hvis den er urimelig. Vurderingen tar hensyn til kjøper og kontekst.</p>""",
        "eksempler": [
            {"navn": "Kari", "tekst": "Kari driver en liten serveringsbedrift og kjøper trekull fra samme leverandør hver måned. Denne gangen glemmer de å nevne pris. Leverandøren leverer som vanlig og fakturerer 280 kr per sekk — markedsprisen. Etter § 45 betaler Kari «gjengs pris». 280 kr er det normale — Kari kan ikke insistere på en lavere pris hun selv ønsket. Hadde leverandøren plutselig fakturert 500 kr per sekk — som ville være langt over markedet — kunne Kari ha vist til urimelighetsregelen."},
            {"navn": "Marius", "tekst": "Marius bestiller en spesiallaget benk fra en snekker. De avtaler ikke pris — Marius regner med at det blir greit. Når benken er ferdig, fakturerer snekkeren 35 000 kr. Det finnes ingen «gjengs pris» for unike benker. Etter § 45 må prisen være «rimelig» ut fra arbeidet — materialer, tidsbruk, kvalitet. Hvis snekkeren har brukt 60 timer og høykvalitetsmaterialer, kan 35 000 kr være rimelig. Er det 20 timer og standardmaterialer, kan det være urimelig."},
        ],
        "vanlige_feil": [
            "Glemmer å avtale pris og blir overrasket av fakturaen",
            "Tror «gjengs pris» alltid er den laveste — det er normalprisen, ikke billigst",
            "Som kjøper: krever en lavere pris uten hjemmel",
            "Som selger: prøver å ta urimelig høy pris fordi det ikke er avtalt",
        ],
        "hva_bor_du_html": """<p><strong>Som kjøper:</strong></p>
<ul>
<li>Avtal pris før kjøpet — alltid</li>
<li>Be om tilbud eller estimat skriftlig</li>
<li>Hvis du får faktura du synes er urimelig: be om underlag og sammenlikning</li>
</ul>
<p><strong>Som selger:</strong></p>
<ul>
<li>Hvis du leverer uten pris, hold deg til markedet</li>
<li>Send tilbud før arbeid begynner — det reduserer konflikter</li>
<li>Dokumenter tidsbruk og materialkostnader for unike varer</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "3", "tittel": "Avtale går foran loven", "available": True},
            {"lov": "kjopsloven", "paragraf": "46", "tittel": "Pris etter mengde", "available": True},
            {"lov": "kjopsloven", "paragraf": "47", "tittel": "Bundet av regning", "available": True},
        ],
    },
    {
        "number": "46",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Pris etter mengde, mål eller vekt",
        "description": "Ved pris etter mengde, mål eller vekt teller det som er der når risikoen går over på deg — ikke det som var i utgangspunktet.",
        "kort_svar": "Hvis prisen avhenger av mengde, mål eller vekt — for eksempel kornleveranser eller drivstoff — er det mengden ved tidspunktet da risikoen gikk over på deg som teller. Hvis prisen er etter vekt, trekkes vekten av emballasjen først.",
        "paragraftekst": """(1) Skal kjøpesummen fastsettes etter tall, mål eller vekt, legges til grunn mengden på det tidspunkt da risikoen for tingen går over på kjøperen.

(2) Er prisen fastsatt etter vekt, trekkes først vekten av innpakningen fra.""",
        "hva_betyr_html": """<p>For varer som måles eller veies — korn, drivstoff, sand, frukt — er prisen ofte «X kr per kg» eller «Y kr per liter». Hva som faktisk måles, og når, kan ha stor økonomisk betydning.</p>
<p><strong>Tidspunkt</strong> (første ledd): Det som teller, er mengden idet risikoen går over på deg (jf. § 13). Ikke det selgeren hadde i utgangspunktet, og ikke det som er igjen når du er ferdig med å bruke det.</p>
<p>Eksempel: Selger har 1 050 kg korn på lager. Han laster 1 020 kg på din vogn ved overtakelse. Under transport ryker noe pga vær — du har 990 kg når du kommer hjem. Risikoen gikk over ved overtakelse (1 020 kg). Du betaler for 1 020 kg, ikke for 1 050 (selgers utgangspunkt) eller 990 (det du faktisk har hjemme).</p>
<p><strong>Vekt minus emballasje</strong> (andre ledd): Hvis prisen er etter vekt, trekkes innpakningen fra. Du skal ikke betale for kassen som inneholder kornet.</p>""",
        "eksempler": [
            {"navn": "Ola", "tekst": "Ola bestiller havre til 4,20 kr per kg fra en grossist. Han henter selv. Lasten veies ved overtakelse: 980 kg netto (etter at vekten av sekkene er trukket fra). Ola betaler for 980 kg × 4,20 kr = 4 116 kr. Hvis sekkene veide 25 kg, har grossisten regnet riktig — § 46 (2) krever at emballasjevekten trekkes fra."},
            {"navn": "Eva", "tekst": "Eva får levert 3 200 liter fyringsolje. Måleren ved overtakelse viser 3 195 liter. Underveis til tanken hennes lekker det ut 8 liter — i tanken hennes er det 3 187. Etter § 46 betaler Eva for 3 195 liter — det som var levert ved risikoens overgang. De 8 liter som forsvant senere, er hennes problem."},
        ],
        "vanlige_feil": [
            "Krever prisreduksjon for det som forsvant etter overtakelse — du har risikoen",
            "Glemmer at emballasje skal trekkes fra",
            "Som selger: tar betalt for utgangsvekt, ikke faktisk levert mengde",
        ],
        "hva_bor_du_html": """<ul>
<li>Veie/måle ved overtakelse — det er det avgjørende tidspunktet</li>
<li>Skriftlig dokumentasjon av nettoinnhold</li>
<li>Sjekk fakturaen mot målepunkt og avtale</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "13", "tittel": "Når går risikoen over", "available": True},
            {"lov": "kjopsloven", "paragraf": "45", "tittel": "Pris når avtalen er stille", "available": True},
        ],
    },
    {
        "number": "47",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Når faktura blir bindende",
        "description": "Får du regning du ikke har avtalt prisen for, er du bundet av den hvis du ikke sier ifra innen rimelig tid. Unntak: hvis lavere pris er avtalt eller fakturaen er urimelig.",
        "kort_svar": "Hvis du får en faktura eller regning og ikke sier ifra innen rimelig tid, er du bundet av prisen som står der. Unntak: hvis dere har avtalt en lavere pris, eller hvis fakturaen er urimelig. Det betyr at du må reagere raskt på fakturaer du er uenig i.",
        "paragraftekst": "Har kjøperen fått rekning eller nota, er han bundet av den pris som er oppført, om han ikke innen rimelig tid sier fra at han ikke godtar den. Dette gjelder ikke når lavere pris følger av avtale eller den oppførte pris er urimelig.",
        "hva_betyr_html": """<p>En faktura er ikke bare et betalingskrav — det er også et tilbud om pris. Hvis du tier, sier du i praksis ja.</p>
<p><strong>Hovedregel:</strong> Hvis du får regning og ikke sier ifra innen rimelig tid, gjelder prisen som er oppført. Tausheten din binder.</p>
<p><strong>To unntak:</strong></p>
<ul>
<li><strong>Lavere pris er avtalt:</strong> Hvis dere har avtalt en konkret pris og fakturaen er høyere, gjelder avtalen — ikke fakturaen. Du kan kreve at fakturaen rettes.</li>
<li><strong>Urimelig pris:</strong> Selv om dere ikke har avtalt pris, kan ikke selgeren bare sette hva han vil. Hvis fakturaen er urimelig — langt over markedet eller det rimelige — er du ikke bundet.</li>
</ul>
<p>«Rimelig tid» for å protestere avhenger av sammenhengen. Som privatperson eller småbedrift: 1-2 uker er normalt trygt. Forretningsforhold med løpende fakturering kan kreve raskere reaksjon.</p>
<p><strong>Hvorfor er dette så viktig?</strong> Mange tror at de kan bare la fakturaen ligge og diskutere senere. Det stemmer ikke. Tausheten gjør deg bundet.</p>""",
        "eksempler": [
            {"navn": "Petter", "tekst": "Petter har leid en håndverker til mindre arbeid. De avtalte ikke konkret pris. Petter får regning på 12 500 kr — han syns det er mye for det som ble gjort. Hvis Petter ikke protesterer, gjelder fakturaen etter § 47. Han må reagere innen rimelig tid: send en skriftlig melding der han bestrider prisen, gjerne med begrunnelse om hva han mener er rimelig. Han kan ha krav på at prisen settes ned hvis 12 500 er over «rimelig» nivå."},
            {"navn": "Sara", "tekst": "Sara har avtalt med en leverandør at vareleveransen koster 18 000 kr. Fakturaen kommer på 22 500 kr. Avtalen gjelder etter § 47 — Sara er ikke bundet av fakturaprisen. Hun skriver til leverandøren: «Avtalen var 18 000 kr. Jeg ber om kreditnota for 4 500 kr og betaler 18 000 kr.»"},
        ],
        "vanlige_feil": [
            "Lar fakturaer ligge og tror du kan diskutere senere",
            "Bestrider muntlig uten å ha skriftlig bevis",
            "Glemmer å reagere raskt — fristen tikker",
            "Tror urimelighet er lett å vise — det krever ofte sammenliknende dokumentasjon",
        ],
        "hva_bor_du_html": """<p>Når du får en faktura du er uenig i:</p>
<ol>
<li>Reager raskt — innen 1-2 uker</li>
<li>Skriftlig protest — e-post eller brev</li>
<li>Begrunn: avtalt pris, urimelig pris, eller annet</li>
<li>Hold tilbake den omstridte delen, betal det du faktisk skylder</li>
<li>Be om kreditnota og spesifikasjon</li>
</ol>
<p><strong>Mal:</strong></p>
<p><em>«Jeg viser til faktura [nr] av [dato] på [beløp]. Jeg godtar ikke fakturabeløpet. Begrunnelse: [avtalt pris var X / fakturabeløpet er urimelig fordi Y]. Jeg ber om kreditnota og ny faktura på korrekt beløp [Z kr]. Jeg betaler det jeg faktisk skylder ved utløp av ordinær frist.»</em></p>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "3", "tittel": "Avtale går foran loven", "available": True},
            {"lov": "kjopsloven", "paragraf": "45", "tittel": "Pris når avtalen er stille", "available": True},
        ],
    },
    {
        "number": "48",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Hvor skal du betale?",
        "description": "Du skal betale på selgerens forretningssted. Skjer betaling ved overlevering av varen eller dokument, betaler du der overlevering skjer.",
        "kort_svar": "Hovedregelen er at du skal betale på selgerens forretningssted. Hvis betaling skjer mot overlevering av vare eller dokument, betaler du der overleveringen skjer. Betalingsplikten omfatter også å akseptere veksel eller stille bankgaranti hvis det er avtalt. Hvis selgeren flytter etter avtalen er inngått, må han dekke ekstra kostnader fra flyttingen.",
        "paragraftekst": """(1) Kjøpesummen skal betales på selgerens forretningssted (i tilfelle bosted jf § 83). Dersom betaling skal skje mot overlevering av tingen eller dokument, skal det gjøres på det sted overleveringen skjer.

(2) Plikten til å betale kjøpesummen omfatter også plikt etter avtalen til å akseptere veksel, stille remburs, bankgaranti eller annen sikkerhet samt å treffe andre tiltak for å få betalt kjøpesummen.

(3) Selgeren svarer for økte kostnader i forbindelse med betalingen som skyldes at han har flyttet sitt forretningssted etter at kjøpet ble inngått.""",
        "hva_betyr_html": """<p>Loven gir tre regler om betalingssted og -metode:</p>
<p><strong>Hvor:</strong> Som hovedregel betaler du der selgeren har sitt forretningssted (eller bosted hvis privatperson). I praksis i dag betyr det at du sender penger til selgerens konto — det er en form for betaling «på selgerens forretningssted».</p>
<p>Hvis betaling skjer mot overlevering — typisk vare-mot-penger i butikk eller ved henting — betaler du der overleveringen skjer.</p>
<p><strong>Hva:</strong> Betalingsplikten er ikke bare å overføre penger. Hvis dere har avtalt bankgaranti, remburs eller annen sikkerhet, må du sørge for det også. Dette gjelder særlig i bedriftshandel og internasjonal handel.</p>
<p><strong>Selgerens flytting:</strong> Hvis selgeren flytter etter at kjøpet er inngått og det fører til ekstra kostnader for deg (gebyrer, lengre transport for kontant betaling), må selgeren dekke det.</p>
<p>I praksis er denne paragrafen mest relevant for B2B-handel og internasjonal handel. Mellom privatpersoner skjer mesteparten via Vipps eller bankoverføring.</p>""",
        "eksempler": [
            {"navn": "Anne", "tekst": "Anne kjøper en gammel kommode fra Tom for 8 500 kr. Hun avtaler å hente — og betale — samtidig. Hun møter opp, sjekker kommoden, og betaler via Vipps mens hun står der. Dette er betaling «der overleveringen skjer» etter § 48 første ledd. Det vanlige privatscenario."},
            {"navn": "Tom", "tekst": "Tom driver et lite import-firma og kjøper varer fra en tysk leverandør. Avtalen krever at Tom stiller bankgaranti før varene sendes. Tom har betalingsplikt utvidet etter § 48 (2) — han må ikke bare overføre penger, men også sørge for at bankgarantien er på plass. Ellers misligholder han."},
        ],
        "vanlige_feil": [
            "Tror betaling er gjort når du sender Vipps — den må også komme fram",
            "Glemmer at bankoverføringer kan ta dager",
            "Som B2B-kjøper: tror veksel/remburs er valgfritt når det er avtalt",
        ],
        "hva_bor_du_html": """<ul>
<li>Bekreft betaling — Vipps-bekreftelse, kontoutskrift, kvittering</li>
<li>Vær oppmerksom på tidsforskjell ved internasjonal handel</li>
<li>Ha sikkerhetsmarginer ved store kjøp — start betalingen i god tid før overlevering</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "10", "tittel": "Selgerens tilbakeholdsrett", "available": True},
            {"lov": "kjopsloven", "paragraf": "49", "tittel": "Når skal du betale", "available": True},
        ],
    },
    {
        "number": "49",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Når skal du betale?",
        "description": "Står betalingstid ikke i avtalen, betaler du når selgeren krever det — men ikke før varen er levert eller stilt til din rådighet.",
        "kort_svar": "Hvis ikke betalingstidspunkt er avtalt, skal du betale når selgeren krever det — men ikke før varen er levert eller stilt til din rådighet. Du har normalt rett til å undersøke varen før betaling, men kan ikke utsette betalingen med mer enn 30 dager på den måten. Ved bruk av konnossement i transport kan betaling kreves uten at du har sett varen.",
        "paragraftekst": """(1) Følger ikke betalingstiden av avtalen, skal kjøperen betale når selgeren krever det, men ikke før tingen blir overlevert kjøperen eller stilt til hans rådighet i samsvar med avtalen og loven.

(2) Før kjøperen betaler har han likevel rett til å få undersøke tingen på vanlig måte, når dette ikke er uforenlig med den avtalte framgangsmåte for levering og betaling av kjøpesummen. Kjøperen kan ikke som følge av en slik undersøkelse utsette betalingen med mer enn 30 dager, med mindre selgeren uttrykkelig har godkjent dette.

(3) Dersom det brukes konnossement ved transporten av tingen til bestemmelsesstedet, eller transporten til kjøperen for øvrig skjer på slike vilkår at selgeren ikke kan rå over tingen etter betalingen, kan betaling kreves mot konnossement, fraktbrev eller annet bevis for at tingen blir transportert på slike vilkår. Dette gjelder selv om tingen ikke er kommet fram eller kjøperen ikke har hatt høve til å undersøke den.""",
        "hva_betyr_html": """<p>Tre regler om betalingstidspunkt:</p>
<p><strong>Hovedregel</strong> (første ledd): Hvis ingenting er avtalt om når du skal betale, er det enkelt:</p>
<ul>
<li>Selgeren må kreve betaling — du har ikke plikt til å betale på eget initiativ</li>
<li>Du skal ikke betale før varen er levert eller stilt til din rådighet</li>
</ul>
<p>Med andre ord: penger mot vare. Du betaler ikke før du har varen eller kan disponere over den.</p>
<p><strong>Rett til å undersøke</strong> (andre ledd): Før du betaler har du rett til å sjekke varen på normal måte — åpne kassen, slå på maskinen, sjekke fakta. Men denne undersøkelsen kan ikke brukes til å utsette betalingen mer enn 30 dager.</p>
<p>Unntak: hvis det er avtalt en bestemt fremgangsmåte for betaling som ikke gir rom for forundersøkelse (for eksempel oppkrav eller forskuddsbetaling).</p>
<p><strong>Konnossement</strong> (tredje ledd): Ved internasjonal sjøhandel og enkelte andre transportformer brukes konnossement — et transportdokument som gir disposisjonsrett over varen. Når slik dokumentbasert handel skjer, kan selgeren kreve betaling mot konnossement uten at du har sett selve varen. Logikken: dokumentet gir deg rett til å disponere over varen, og uten betaling får selgeren tilbake disposisjonsretten.</p>""",
        "eksempler": [
            {"navn": "Lars", "tekst": "Lars har bestilt en symaskin fra en privatperson for 6 500 kr. De har ikke avtalt når Lars skal betale. Selgeren leverer maskinen. Etter § 49 må Lars betale når selgeren krever det — typisk samme dag eller dagene etter levering. Han kan be om å sjekke maskinen først, men kan ikke trekke ut betalingen."},
            {"navn": "Eva", "tekst": "Eva har kjøpt en brukt motor for 28 000 kr. Hun ber selgeren om å sjekke at den faktisk virker før hun betaler. Selgeren godtar — Eva tar med en mekanikervenn og tester. Det er § 49 (2) i praksis. Eva har rett til «undersøkelse på vanlig måte». Men hun kan ikke dra det ut i ukevis — 30 dager er øvre grense, og ofte er rimelig tid mye kortere."},
            {"navn": "Tom", "tekst": "Tom driver et lite firma og importerer korn fra utlandet med skipstransport. Avtalen bruker konnossement — det er normalt i sjøhandel. Etter § 49 (3) kan selgeren kreve betaling mot konnossement, ikke mot vare i hånden. Tom betaler basert på dokumentene som gir ham rett til å hente kornet i havn. Han kan ikke holde tilbake penger til kornet er fysisk hjemme."},
        ],
        "vanlige_feil": [
            "Tror du må betale med en gang kjøpet er inngått — du må vente til levering eller selgerens krav",
            "Trekker ut undersøkelsen for å utsette betalingen — det er begrenset til 30 dager",
            "Som selger: glemmer å kreve betaling og blir surprised at penger ikke kommer",
            "Forveksler konnossementsregler med vanlig hentekjøp",
        ],
        "hva_bor_du_html": """<p><strong>Som kjøper:</strong></p>
<ul>
<li>Avtal alltid betalingstid skriftlig — det er enklere</li>
<li>Undersøk varen før betaling hvis du kan</li>
<li>Hvis du vil ha kreditt (betal senere), avtal det tydelig</li>
</ul>
<p><strong>Som selger:</strong></p>
<ul>
<li>Krev betaling skriftlig så snart varen er levert</li>
<li>Send faktura med klar forfallsdato</li>
<li>Vurder forsinkelsesrente (§ 71) hvis betalingen drar ut</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "10", "tittel": "Selgerens tilbakeholdsrett", "available": True},
            {"lov": "kjopsloven", "paragraf": "48", "tittel": "Hvor du skal betale", "available": True},
        ],
    },
    {
        "number": "50",
        "lov": "kjopsloven",
        "lov_display": "Kjøpsloven",
        "title": "Du må medvirke til kjøpet",
        "description": "Du må gjøre din del — gi info selgeren trenger, og hente eller motta varen. Hvis du ikke gjør det, er du i kontraktbrudd.",
        "kort_svar": "Du har to plikter som kjøper: medvirke der det er rimelig at selgeren trenger din hjelp for å levere, og overta varen — enten ved å hente eller motta den. Glemmer eller nekter du, er du i kontraktbrudd og selgeren kan kreve oppfyllelse, heving og erstatning.",
        "paragraftekst": "Kjøperen skal (a) yte slik medvirkning som det er rimelig å vente av ham for at selgeren skal kunne oppfylle kjøpet, og (b) overta tingen ved å hente eller motta den.",
        "hva_betyr_html": """<p>Kjøpsloven legger ikke bare plikter på selgeren. Du som kjøper må også gjøre din del. Loven nevner to plikter:</p>
<p><strong>Medvirkning</strong> (bokstav a): Du må gjøre det som er rimelig å forvente av deg for at selgeren kan levere. Eksempler:</p>
<ul>
<li>Gi nødvendig informasjon (mål, spesifikasjoner, leveringsadresse)</li>
<li>Stille på avtalt sted til avtalt tid</li>
<li>Sørge for nødvendige tillatelser eller forberedelser</li>
<li>Bekrefte spesifikasjoner når selgeren ber om det</li>
</ul>
<p>Vurderingen er hva som er rimelig. Du må ikke gjøre selgerens jobb, men du må ikke heller stille deg passiv mens han trenger din respons.</p>
<p><strong>Overtakelse</strong> (bokstav b): Du må enten hente eller motta varen. Du kan ikke bare la den stå hos selgeren eller nekte å åpne for budet.</p>
<p><strong>Konsekvenser hvis du svikter:</strong> Du er i kontraktbrudd. Selgeren kan kreve oppfyllelse, heve, kreve erstatning og holde tilbake levering. Risikoen kan også gå over på deg (§ 13 andre ledd).</p>""",
        "eksempler": [
            {"navn": "Marius", "tekst": "Marius bestiller spesialtilpassede dører for 65 000 kr. Selgeren ber om mål og fargevalg. Marius svarer ikke i to uker. Levering blir forsinket. Marius er i medvirkningsbrudd etter § 50 (a). Forsinkelsen er hans skyld — selgeren kan kreve erstatning for konkrete tap og fortsatt kreve betaling når dørene er klare."},
            {"navn": "Ingrid", "tekst": "Ingrid har kjøpt en brukt kjøkkenmaskin fra Tom for 4 200 kr. Avtalt henting onsdag. Ingrid kommer ikke og svarer ikke på meldinger. Tom har risikoen for varen kun frem til avtalt henting. Etter onsdag går risikoen over på Ingrid (§ 13). Tom kan kreve betaling, eventuelt heve eller selge maskinen til en annen og kreve erstatning hvis han ikke får ut samme pris."},
        ],
        "vanlige_feil": [
            "Tror selgeren skal «ordne alt» — du har egne plikter",
            "Glemmer at forsinkelse fra din side flytter risiko og kostnader",
            "Som selger: gir ikke beskjed om at du venter på info fra kjøperen — dokumenter det",
        ],
        "hva_bor_du_html": """<p><strong>Som kjøper:</strong></p>
<ul>
<li>Svar raskt på henvendelser fra selgeren</li>
<li>Møt opp i tide</li>
<li>Gi nødvendig informasjon tydelig og skriftlig</li>
<li>Hvis du må utsette, varsle selgeren</li>
</ul>
<p><strong>Som selger:</strong></p>
<ul>
<li>Be skriftlig om informasjon du trenger</li>
<li>Dokumenter at du har bedt</li>
<li>Sett rimelig frist for kjøperens svar</li>
</ul>""",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "kjopsloven", "paragraf": "13", "tittel": "Risikoens overgang ved manglende medvirkning", "available": True},
        ],
    },
]
