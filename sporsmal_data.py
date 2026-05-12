"""Spørsmål-artikler for Rettsregel.

Hver SPORSMAL har:
- title, slug, kategori, description, last_updated
- kort_svar: kort tekstavsnitt (uten markdown)
- body_md: full markdown body fra og med første H2 til og med "Relevante paragrafer"
- related_paragrafer: liste av {lov, nummer, beskrivelse}
"""

SPORSMAL = [
    {
        "title": "Utleier nekter å gi tilbake depositumet — hva gjør du?",
        "slug": "utleier-nekter-depositum",
        "kategori": "bolig",
        "description": "Utleier holder igjen depositumet uten grunn? Du har rett til pengene tilbake. Lær hva du kan kreve og hvordan du bruker Husleietvistutvalget.",
        "kort_svar": "Du har krav på depositumet tilbake når leieforholdet er avsluttet og du ikke skylder husleie eller har påført dokumentert skade. Utleier kan ikke holde tilbake penger bare fordi de er misfornøyde. Klager du til Husleietvistutvalget, er det gratis og avgjøres vanligvis innen tre måneder.",
        "body_md": """## Utleier svarer ikke — eller lager plutselig en lang liste med feil

Du har ryddet, vasket og levert nøklene. Likevel hører du ingenting, eller du mottar en liste med "skader" du aldri visste om.

Dette skjer mange leietakere. Noen gir opp fordi de tror det er for tungvint å klage. Det er det ikke — og depositumet er dine penger.

## Hva loven sier

Etter husleieloven § 3-5 skal depositumet stå på en sperret konto i leietakers navn. Utleier disponerer ikke pengene — de tilhører deg, med opptjente renter.

Utleier kan kreve fradrag for to ting: dokumentert skade utover normal slitasje, eller ubetalt husleie. Normal slitasje — maling som falmer, gulv med bruksmerker, fuger som mørkner — er ikke din regning.

Vil utleier ikke frigjøre depositumet, kan du sende krav direkte til banken etter husleieloven § 3-6. Utleier har da fem uker på å dokumentere et eventuelt krav. Gjør de ikke det, utbetales pengene til deg.

## Eksempel: Kari

Kari leide i tre år. Etter utflytting holdt utleier igjen 25 000 kr med begrunnelsen "generell slitasje". Kari hadde tatt bilder ved innflytting og signert innflyttingsprotokoll. Hun sendte krav til banken etter § 3-6, la ved dokumentasjonen — og fikk hele depositumet utbetalt etter seks uker.

## Hva du skal gjøre — steg for steg

1. **Dokumenter tilstanden ved utflytting** — Ta bilder av alle rom med dato. Signér en utflyttingsprotokoll hvis mulig.
2. **Be om skriftlig begrunnelse** — Send e-post: "Hva er årsaken til at depositumet ikke er utbetalt?"
3. **Send krav til banken** — Skriv til depositumbanken og krev utbetaling etter husleieloven § 3-6. Legg ved innflyttingsprotokoll og bilder.
4. **Klag til Husleietvistutvalget** — Hvis banken ikke utbetaler, klager du digitalt på husleietvistutvalget.no. Det koster ingenting.
5. **Ta vare på all kommunikasjon** — Alle meldinger og e-poster kan bli bevis.

## Vanlige feil

- Ikke ta bilder ved utflytting — da mister du bevisgrunnlaget
- Vente for lenge med å sende krav skriftlig
- Godta et lavere beløp uten å forstå hva du gir fra deg

## Vanlige spørsmål

**Utleier hevder det er skader, men jeg er uenig — hva gjør jeg?**

Krev dokumentasjon: kvitteringer fra håndverker og bilder. Normal slitasje er ikke din regning. Husleietvistutvalget avgjør slike tvister uten at du trenger advokat.

**Hva om jeg ikke har innflyttingsprotokoll?**

Vanskeligere, men ikke umulig. Bilder fra innflytting, vitner og levetabeller for materialer kan fremdeles brukes. Dokumenter det du har.

**Kan utleier holde igjen for manglende rengjøring?**

Ja, men kun for faktiske kostnader til profesjonell rengjøring — med kvittering. Ikke et sjablongbeløp.
""",
        "related_paragrafer": [
            {"lov": "husleieloven", "nummer": "3-5", "beskrivelse": "depositumkonto og leietakers eierskap"},
            {"lov": "husleieloven", "nummer": "3-6", "beskrivelse": "utbetaling fra depositumkonto"},
            {"lov": "husleieloven", "nummer": "10-2", "beskrivelse": "fradrag og oppgjør ved fraflytting"},
        ],
    },
    {
        "title": "Håndverkeren leverte ikke som avtalt — hva kan du kreve?",
        "slug": "haandverker-leverte-ikke-som-avtalt",
        "kategori": "forbruk",
        "description": "Håndverkeren leverte dårlig arbeid eller overholdt ikke avtalen? Her er rettighetene dine og stegene du tar nå.",
        "kort_svar": "Er arbeidet dårlig utført eller avviker fra det dere avtalte, har du krav på utbedring uten ekstra kostnad. Nekter håndverkeren, kan du kreve prisavslag — og i alvorlige tilfeller heve avtalen. Klag skriftlig så snart du oppdager feilen.",
        "body_md": """## Malingen flasser, røret lekker, og jobben er "ferdig"

Det er ubehagelig å klage. Mange lar det ligge og håper det går over. Men feil fra håndverkere forsvinner ikke av seg selv — og venter du for lenge, kan du miste retten.

En mangel trenger ikke å være dramatisk. Det holder at arbeidet avviker fra det dere avtalte, eller ikke er utført på faglig forsvarlig måte. Muntlige avtaler teller like mye som skriftlige.

## Hva loven sier

Etter håndverkertjenesteloven § 17 er det en mangel hvis tjenesten ikke er faglig forsvarlig, eller avviker fra det som ble avtalt. Du kan kreve at håndverkeren utbedrer for sin regning.

Nekter håndverkeren, eller mislykkes utbedringen to ganger, kan du kreve prisavslag etter § 22. Er mangelen vesentlig, kan du heve avtalen etter § 24 og slippe restbeløpet.

Reklamasjonsfristen er fem år fra arbeidet ble ferdigstilt. Men du må klage innen rimelig tid etter at du oppdaget feilen — vent ikke.

## Eksempel: Per

Per fikk lagt nytt parkettgulv. To måneder etter begynner plankene å bukte seg. Han sendte e-post med bilder og krevde utbedring med 14 dagers frist. Håndverkeren ignorerte henvendelsen. Per klagde til Forbrukertvistutvalget, la ved tilbudet og bildene — og fikk 18 000 kr i prisavslag.

## Hva du skal gjøre — steg for steg

1. **Dokumenter feilen** — Ta bilder eller video med dato. Vær konkret: hva er galt og hvor.
2. **Klag skriftlig innen rimelig tid** — E-post eller SMS så snart du oppdager feilen.
3. **Krev utbedring med frist** — Gi en konkret frist, for eksempel 14 dager. Si tydelig hva som skal rettes.
4. **Innhent uavhengig vurdering** — En annen fagperson som bekrefter mangelen styrker saken din.
5. **Klag til Forbrukertvistutvalget** — Gratis, digital klage på forbrukertvistutvalget.no.

## Vanlige feil

- Betale fullt ut uten å ta forbehold om mangelen — det svekker kravet ditt
- Klage muntlig — alt skriftlig, alltid
- Rette feilen selv uten å informere håndverkeren — da mister du kravet om utbedring

## Vanlige spørsmål

**Håndverkeren sier feilen skyldes at jeg bruker det feil — hva gjør jeg?**

Håndverkeren må sannsynliggjøre at arbeidet var feilfritt ved levering. Innhent en uavhengig faglig vurdering — den veier tungt i en klagesak.

**Jeg har allerede betalt — kan jeg fremdeles klage?**

Ja. Betaling er ikke aksept av mangelen, så lenge du klager innen rimelig tid etter at du oppdaget den.

**Håndverkeren er konkurs — hva nå?**

Sjekk om firmaet hadde garantiforsikring. Meld kravet til boet via tingretten. Har du ennå ikke betalt restbeløpet, kan du holde det tilbake.
""",
        "related_paragrafer": [
            {"lov": "haandverkertjenesteloven", "nummer": "17", "beskrivelse": "hva som utgjør en mangel"},
            {"lov": "haandverkertjenesteloven", "nummer": "22", "beskrivelse": "rett til prisavslag"},
            {"lov": "haandverkertjenesteloven", "nummer": "24", "beskrivelse": "rett til heving av avtalen"},
        ],
    },
    {
        "title": "Bilen jeg kjøpte har skjult feil — hva kan jeg kreve?",
        "slug": "bilen-har-skjult-feil",
        "kategori": "forbruk",
        "description": "Oppdaget en feil på bilen etter kjøpet som selgeren ikke opplyste om? Her er reklamasjonsretten din og hva du gjør i dag.",
        "kort_svar": "Kjøpte du bilen av en forhandler og oppdager en feil innen to år, har du reklamasjonsrett. Oppdages feilen innen seks måneder, antas den å ha eksistert ved kjøpet — selger må bevise det motsatte. Klag skriftlig så snart du oppdager noe.",
        "body_md": """## Bilen virket fin — til den ikke gjorde det lenger

Girkassen hakker. Varsellampen lyser. Rusten dukker opp i hjulbuene. Selgeren "visste ingenting".

Kjøpte du av en forhandler (næringsdrivende), er du beskyttet av forbrukerkjøpsloven. Kjøpte du av privatperson, gjelder kjøpsloven — noe svakere, men du har fremdeles rettigheter hvis selgeren kjente til feilen og holdt det tilbake.

## Hva loven sier

Etter forbrukerkjøpsloven § 16 er det en mangel hvis bilen avviker fra det som ble avtalt, eller selger ga feilaktige opplysninger. Det gjelder også feil selger burde ha kjent til.

Oppdager du feilen innen seks måneder, snur bevisbyrden: forhandleren må bevise at bilen var feilfri ved levering. Etter seks måneder er det du som må sannsynliggjøre at feilen lå der fra start.

Du kan kreve utbedring, prisavslag etter § 29, eller heving etter § 32 hvis feilen er vesentlig. Reklamasjonsfristen er to år.

## Eksempel: Mette

Mette kjøpte en tre år gammel SUV. Fire måneder etter kjøpet begynte girkassen å hakke. Forhandleren hevdet "normal slitasje". Siden feilen dukket opp innen seks måneder, måtte forhandleren bevise at problemet ikke fantes ved levering — det klarte de ikke. Mette fikk bilen reparert uten kostnad.

## Hva du skal gjøre — steg for steg

1. **Klag skriftlig til forhandleren** — E-post med dato, beskrivelse av feilen og krav om svar innen 14 dager.
2. **Ikke reparer bilen selv** — Da svekker du kravet. Vent til forhandleren har fått muligheten til å utbedre.
3. **Innhent uavhengig teknisk vurdering** — En mekaniker-rapport styrker saken din betydelig.
4. **Velg krav: reparasjon, prisavslag eller heving** — Heving krever at mangelen er vesentlig.
5. **Klag til Forbrukertvistutvalget** — Gratis klage digitalt hvis forhandler avviser.

## Vanlige feil

- Reparere bilen uten å varsle selger — du mister retten til utbedring
- Reklamere muntlig — alt skriftlig, alltid
- Vente mer enn to år fra leveringsdato med å klage

## Vanlige spørsmål

**Bilen ble solgt "som den er" — hjelper ikke det forhandleren?**

Nei. "Som den er"-forbehold gjelder ikke for forbrukerkjøp fra næringsdrivende. Reklamasjonsretten kan ikke fratas deg på forhånd.

**Kjøpte av privatperson — har jeg noen rettigheter?**

Ja, men svakere. "Som den er"-forbehold gjelder. Likevel er selgeren ansvarlig hvis de kjente til feilen og ikke opplyste om den — det er svik.

**Feilen kom etter ett år — er det for sent?**

Nei. Fristen er to år for forbrukerkjøp. Men klag så snart du oppdager feilen — du mister retten hvis du venter unødvendig lenge.
""",
        "related_paragrafer": [
            {"lov": "forbrukerkjopsloven", "nummer": "16", "beskrivelse": "hva som er en mangel"},
            {"lov": "forbrukerkjopsloven", "nummer": "29", "beskrivelse": "rett til prisavslag"},
            {"lov": "forbrukerkjopsloven", "nummer": "32", "beskrivelse": "rett til heving"},
        ],
    },
    {
        "title": "Naboen klager på støy fra deg — hva gjelder?",
        "slug": "naboen-klager-paa-stoy",
        "kategori": "bolig",
        "description": "Naboen klager på støy fra leiligheten din? Her er hva loven faktisk krever av deg — og når en klage er urimelig.",
        "kort_svar": "En klage er ikke det samme som et brudd. Støy fra normal beboelse — barn, musikk på dagtid, selskaper til rimelig tid — er ikke et lovbrudd. Er støyen faktisk urimelig sett opp mot hva som er vanlig i området, kan du bli pålagt å redusere den. Gjentatte brudd kan gi utleier grunnlag for å heve leiekontrakten.",
        "body_md": """## Naboen banker på — hva betyr det egentlig?

En klage er ikke en dom. Naboen kan ha rett. Eller klagen kan være urimelig. Nøkkelen er hva som objektivt sett er urimelig støy i nettopp ditt bomiljø.

Støy fra vanlig beboelse er ikke et brudd på noe. Støy som holder naboer våkne, høy bass etter midnatt, eller langvarig bråk over tid — det kan det være.

## Hva loven sier

Naboloven § 2 slår fast at ingen kan utsette naboeiendommen for urimelig eller unødvendig ulempe. "Urimelig" vurderes ut fra hva som er vanlig i området. I en by tåler naboer mer enn i en eneboliggate.

Bor du i utleiebolig, gjelder husleieloven § 5-1 i tillegg: du plikter å følge husordensreglene og ikke forstyrre andre beboere. Gjentatte dokumenterte klager som du ikke tar tak i, kan gi utleier grunnlag for heving.

Kommunen kan i alvorlige saker pålegge lydmålinger og gi formelle påbud.

## Eksempel: Jonas

Jonas fikk klage fra naboen under om musikk etter klokken 23. Han trodde volumet var greit. Naboen varslet utleier skriftlig. Utleier sendte advarsel. Jonas skrudde ned musikken etter 22 og hørte ikke mer fra noen.

## Hva du skal gjøre — steg for steg

1. **Ta klagen seriøst** — Skriv ned hva naboen klaget på, dato og klokkeslett.
2. **Vurder om klagen er rimelig** — Er støyen faktisk utover det normale? Vær ærlig.
3. **Svar naboen skriftlig** — Bekreft at du har mottatt klagen og hva du vil gjøre. Hold tonen rolig og saklig.
4. **Gjør konkrete endringer om nødvendig** — Tidspunkt, volum, eller type aktivitet.
5. **Ta vare på kommunikasjonen** — Hvis saken eskalerer, dokumenterer dette at du tok tak i det.

## Vanlige feil

- Ignorere klagen — det gir naboen og utleier grunnlag for å eskalere
- Bli konfronterende — det gjør situasjonen verre og kan brukes mot deg
- Ikke dokumentere at du faktisk responderte og gjorde noe

## Vanlige spørsmål

**Naboen klager, men støyen er innenfor det normale — hva gjør jeg?**

Svar skriftlig og beskriv hva slags lyd det er snakk om. Dokumentér at du ikke bryter husordensregler. Er klagen urimelig, kan en tvist avgjøre at du er i din fulle rett.

**Kan naboen tvinge meg til å flytte?**

Nei, ikke direkte. Men gjentatte brudd kan gi utleier rett til å heve leiekontrakten. En enkelt klage gir ikke grunnlag for det.

**Naboen bruker klager som pressmiddel mot meg — hva gjør jeg?**

Dokumenter alt. Fortsett å følge reglene. Snakk med utleier. Er det trakassering, kan du klage til Husleietvistutvalget.
""",
        "related_paragrafer": [
            {"lov": "naboloven", "nummer": "2", "beskrivelse": "tålegrensen for ulempe mellom naboer"},
            {"lov": "husleieloven", "nummer": "5-1", "beskrivelse": "leietakers plikt til ro og orden"},
        ],
    },
    {
        "title": "Naboen har bygget for nær tomtegrensa — hva kan du gjøre?",
        "slug": "nabo-bygget-for-naer-tomtegrense",
        "kategori": "bolig",
        "description": "Naboens garasje eller tilbygg er for nær grensa uten godkjenning? Her er reglene for byggeavstand og hva du kan kreve.",
        "kort_svar": "Byggverk skal som hovedregel stå minst fire meter fra nabogrensen. Er bygget nærmere uten dispensasjon fra kommunen, er det et ulovlig tiltak — og du kan klage til kommunen og kreve at saken følges opp. I ytterste konsekvens kan kommunen gi pålegg om riving.",
        "body_md": """## Naboen har satt opp noe — og det er for nært

En garasje, et uthus, et gjerde, et tilbygg. Du måler opp og ser at det er nærmere grensen enn det skal være. Kanskje skygger det i hagen. Kanskje det er midt i utsikten.

Spørsmålet er: ble det søkt om dette, og fikk naboen lov?

## Hva loven sier

Etter plan- og bygningsloven § 29-4 skal byggverk plasseres minst fire meter fra nabogrensen. Kortere avstand krever enten skriftlig samtykke fra deg som nabo, eller en formell dispensasjon fra kommunen.

Mange byggetiltak er søknadspliktige. Er tiltaket satt opp uten søknad eller godkjenning, er det ulovlig — og kommunen kan pålegge riving.

Naboloven § 2 gjelder parallelt: er bygget til urimelig skade eller ulempe for deg — for eksempel alvorlig skygging — kan du ha krav på erstatning eller retting uavhengig av byggesakene.

## Eksempel: Arne

Arnes nabo satte opp en garasje 1,5 meter fra grensen uten å søke kommunen. Arne kontaktet byggesaksavdelingen skriftlig og la ved en enkel situasjonskart med mål. Kommunen åpnet tilsynssak. Naboen søkte dispensasjon i etterkant — og fikk avslag. Garasjen ble revet.

## Hva du skal gjøre — steg for steg

1. **Mål avstanden** — Bruk målebånd og ta bilder med tydelig dokumentasjon.
2. **Sjekk kommunens byggesak-arkiv** — Se om tiltaket er søkt om og godkjent. Dette gjør du på kommunens nettsider eller ved å ringe byggesaksavdelingen.
3. **Klag til kommunen skriftlig** — Send e-post til byggesaksavdelingen med beskrivelse, bilder og kartskisse. Krev at kommunen vurderer om tiltaket er ulovlig.
4. **Klag til Statsforvalteren** — Gjør kommunen ingenting, eskalerer du hit.
5. **Vurder nabolovskrav separat** — Har du lidt konkret tap (tap av lys, sikt, bruk av tomt), kan du reise krav etter naboloven uavhengig av byggesaken.

## Vanlige feil

- Bare snakke med naboen uten å kontakte kommunen — det gir sjelden resultat
- Vente for lenge — jo lenger bygget har stått, jo vanskeligere er det å nå frem
- Glemme å dokumentere med bilder og mål tidlig i prosessen

## Vanlige spørsmål

**Naboen sier de har fått muntlig tillatelse — stemmer det?**

Nei. Bygningstillatelser er alltid skriftlige og registrert hos kommunen. Muntlig tillatelse eksisterer ikke i byggesaksretten.

**Kan jeg kreve at naboen river bygget?**

Ja, via kommunen eller rettssystemet — men det krever at overtredelsen er dokumentert og vesentlig. Kommunen kan utstede pålegg om riving.

**Bygget sto der da jeg kjøpte huset — hva nå?**

Sjekk byggesak-arkivet. Er det ikke godkjent, kan du fremdeles klage — men lang tid kan ha gitt naboen hevd eller dispensasjon i etterkant. Sjekk arkivet før du konkluderer.
""",
        "related_paragrafer": [
            {"lov": "plan-og-bygningsloven", "nummer": "29-4", "beskrivelse": "avstand fra nabogrense"},
            {"lov": "naboloven", "nummer": "2", "beskrivelse": "tålegrensen for ulempe"},
        ],
    },
    {
        "title": "Kjæresten flyttet ut — hvem eier hva?",
        "slug": "kjaeresten-flyttet-ut-hvem-eier-hva",
        "kategori": "familie",
        "description": "Samboerskap er over og uenig om hvem som eier hva? Uten ekteskap er det ingen automatisk deling. Her er reglene.",
        "kort_svar": "Samboere deler ikke automatisk på verdier slik ektefeller gjør. Du eier det du kan dokumentere at du kjøpte eller eier. Uten samboeravtale kan det bli tvist om boligen, bil og felles innkjøp. Dokumentasjon er avgjørende.",
        "body_md": """## Dere var enige om alt — til dere ikke var det lenger

Relasjonens slutt er vanskelig nok. Så begynner spørsmålene: hvem beholder leiligheten? Hva med kjøkkenmaskinen? Hvem betalte mest i fellesutgifter?

Norsk lov gir samboere ingen automatisk delingsrett. Det som gjelder, er hva du kan dokumentere at du eier.

## Hva loven sier

Husstandsfellesskapsloven § 2 gir den av dere som ikke eier boligen, rett til å overta den hvis det er urimelig at den andre beholder den — typisk der felles barn bor. Men det skjer alltid mot full betaling av markedsverdi.

Eier dere boligen i sameie, regulerer sameieloven § 2 eierskapet etter andel. Uten annen avtale antas like store andeler, men du kan dokumentere en annen fordeling gjennom bankutskrifter, tinglysning og lånedokumenter.

Privat løsøre — møbler, elektronikk, biler — eies av den som kjøpte det. Kvitteringer og bankutskrifter er bevis.

## Eksempel: Sofie og Thomas

Sofie og Thomas eide leiligheten 50/50. Thomas hadde betalt 70 prosent av fellesutgiftene i fem år. Da de gikk fra hverandre, krevde Thomas kompensasjon. Uten skriftlig avtale eller dokumenterte overføringer hadde han lite å stille med — sameieloven ga dem 50/50 av boligens verdi.

## Hva du skal gjøre — steg for steg

1. **Lag en oversikt** — Skriv ned hva dere eier, hvem som kjøpte det og hva det er verdt.
2. **Finn frem kvitteringer og bankutskrifter** — For bolig: tinglysningsdokumenter, låneandel og betalingshistorikk.
3. **Avklar boligspørsmålet først** — Skal én overta? Til hvilken pris? Innhent verdivurdering fra megler.
4. **Sett opp en skriftlig oppgjørsavtale** — Skriv ned hva dere er enige om og signer begge. Det trenger ikke å gå gjennom advokat.
5. **Er dere uenige, bruk en nøytral tredjepart** — En advokat eller megler kan hjelpe til forhandling uten at dere trenger å gå til retten.

## Vanlige feil

- Ikke dokumentere hvem som betalte hva underveis — det er for sent etter bruddet
- Tro at lang samboertid gir automatisk rett til halvparten — det gjør det ikke
- Inngå muntlige avtaler om hvem som overtar boligen uten å tinglyse det

## Vanlige spørsmål

**Vi har barn sammen — endrer det noe?**

Barn gir rettigheter etter barneloven, men ikke rett til hverandres verdier. Den som har daglig omsorg kan ha sterkere krav på å overta boligen etter husstandsfellesskapsloven.

**Jeg betalte mer enn halvparten av boligen — kan jeg få igjen det?**

Ja, via bankutskrifter og lånedokumenter. Du kan kreve en større andel av salgsprovenyet enn 50/50 hvis du kan sannsynliggjøre en annen eierandel.

**Har jeg arverett etter samboer?**

Kun hvis dere har hatt eller venter felles barn. Da har lengstlevende en begrenset arverett. Uten barn er det ingen automatisk arverett — og ingen ting erstatter et testament.
""",
        "related_paragrafer": [
            {"lov": "husstandsfellesskapsloven", "nummer": "2", "beskrivelse": "rett til å overta bolig ved oppgjør"},
            {"lov": "sameieloven", "nummer": "2", "beskrivelse": "eierparter i sameie"},
        ],
    },
    {
        "title": "Arbeidsgiveren vil ikke betale lønn — hva gjør du?",
        "slug": "arbeidsgiver-vil-ikke-utbetale-lonn",
        "kategori": "arbeid",
        "description": "Lønn som ikke kommer er alvorlig. Her er rettighetene dine, hva du kan kreve og hvem du kontakter i dag.",
        "kort_svar": "Arbeidsgiver er lovpliktig til å betale lønn til avtalt tid. Uteblir lønnen, kan du varsle Arbeidstilsynet, levere krav i forliksrådet, og i ytterste konsekvens holde tilbake arbeidet. Du beholder stillingsvernet mens du klager — si ikke opp selv.",
        "body_md": """## Lønnen har ikke kommet — og arbeidsgiveren svarer ikke

Du har jobbet. Pengene skulle vært der. De er ikke det. Heller ikke neste uke. Dette gjelder uansett om du er fast ansatt, midlertidig ansatt eller har timekontrakt.

"Midlertidig likviditetsproblem" er ikke din risiko. Det er arbeidsgiverens.

## Hva loven sier

Etter arbeidsmiljøloven § 14-15 skal lønn utbetales til avtalt tidspunkt. Arbeidsgiver kan ikke utsette utbetalingen ensidig — heller ikke i en vanskelig periode.

Feriepenger er også lønn, regulert av ferieloven § 11. Ubetalte feriepenger kreves på samme måte.

Betaler ikke arbeidsgiver, kan du kreve lønn med renter etter forsinkelsesrenteloven, varsle Arbeidstilsynet, eller ta ut stevning i forliksrådet. Er arbeidsgiver insolvent, kan du søke dekning via Lønnsgarantifondet.

## Eksempel: Håkon

Håkon jobbet tre måneder uten å motta lønn. Arbeidsgiver sa pengene kom "neste uke" gjentatte ganger. Håkon sendte skriftlig krav med sju dagers frist, varslet Arbeidstilsynet og leverte krav i forliksrådet. Han fikk lønnen pluss forsinkelsesrenter innen seks uker.

## Hva du skal gjøre — steg for steg

1. **Krev lønn skriftlig med frist** — E-post: "Jeg har ikke mottatt lønn for [periode]. Ber om utbetaling innen [dato — sju dager]."
2. **Varsle Arbeidstilsynet** — Digitalt på arbeidstilsynet.no. De kan gi pålegg og kontrollere arbeidsgiveren.
3. **Lever krav i forliksrådet** — Enkelt og gratis. Gjøres via namsmannen i din kommune.
4. **Vurder Lønnsgarantifondet** — Er arbeidsgiver insolvent eller konkurs, kan du søke dekning her.
5. **Ikke si opp selv** — Da mister du stillingsvernet og potensielt dagpengene. Vent til situasjonen avklares.

## Vanlige feil

- Si opp selv — da mister du rettigheter du ellers hadde hatt
- Vente for lenge med å sende skriftlig krav
- Ikke dokumentere arbeidstiden og avtalt lønn

## Vanlige spørsmål

**Arbeidsgiver sier det er midlertidig — hva gjør jeg?**

Forståelig situasjon, men det er ikke din risiko. Send kravet og fristen likevel. Gi én sjanse, men la det ikke dra ut mer enn en måned.

**Jeg er selvstendig næringsdrivende — gjelder dette meg?**

Nei, arbeidsmiljøloven gjelder ansatte. Er du frilanser eller selvstendig næringsdrivende, reguleres kravet av kontrakten og inkassoloven.

**Kan jeg holde tilbake arbeidet?**

I prinsippet ja, men det er risikabelt uten juridisk råd. Gjøres det feil, kan arbeidsgiver bruke det mot deg. Søk råd før du tar det steget.
""",
        "related_paragrafer": [
            {"lov": "arbeidsmiljoloven", "nummer": "14-15", "beskrivelse": "tidspunkt for lønnsutbetaling"},
            {"lov": "ferieloven", "nummer": "11", "beskrivelse": "utbetaling av feriepenger"},
        ],
    },
    {
        "title": "Fått inkassovarsel for noe jeg ikke har bestilt — hva gjør jeg?",
        "slug": "inkassovarsel-ikke-bestilt",
        "kategori": "forbruk",
        "description": "Inkassovarsel for en regning du ikke kjenner igjen? Du er ikke pliktig til å betale. Her er hva du gjør i dag.",
        "kort_svar": "Du er ikke pliktig til å betale et krav du bestrider. Send skriftlig innsigelse til inkassobyrået og krev dokumentasjon på avtalegrunnlaget. Betaler du uten å forstå hva det gjelder, kan det tolkes som aksept. Ikke betal før du vet hva du betaler for.",
        "body_md": """## Et brev fra et inkassobyrå for noe du ikke kjenner igjen

Du åpner brevet. Inkassobyrå. 4 800 kroner. Et telefon-abonnement. En strømleverandør. En netthandel. Ingenting som stemmer.

Dette skjer enten fordi noen har bestilt noe i ditt navn (ID-tyveri), fordi det er en administrativ feil, eller fordi det er et bedrageriforsøk. Uansett — du skal ikke betale det.

## Hva loven sier

Etter inkassoloven § 5 har du rett til å bestride et krav. Inkassobyrået er da pliktig til å stanse inndrivingen og be oppdragsgiver dokumentere grunnlaget.

Inkassosalærene som legges på etter § 10 er kun gyldige på gyldige krav. Bestrider du kravet og vinner frem, faller salærene bort.

Mistenker du ID-tyveri, skal du anmelde forholdet til politiet og kontakte et kredittopplysningsbyrå (Bisnode, Experian) for å sperre for nye kredittoppslag.

## Eksempel: Ingrid

Ingrid fikk inkassovarsel på et strøm-abonnement hun aldri hadde tegnet. Hun sendte skriftlig innsigelse til inkassobyrået og krevde dokumentasjon. Det kom ingen dokumentasjon. Saken ble henlagt. Ingrid sperret kredittopplysningene sine.

## Hva du skal gjøre — steg for steg

1. **Ikke betal** — Betaling kan tolkes som aksept av kravet. Vent til du vet hva du betaler for.
2. **Krev dokumentasjon skriftlig** — E-post til inkassobyrået: "Jeg bestrider kravet. Send dokumentasjon for avtalegrunnlaget med bestillingsdato, signatur og leveringsdetaljer."
3. **Sjekk gjeldsregisteret** — På gjeldsregisteret.no ser du hvilke kredittavtaler som er registrert på deg.
4. **Anmeld til politiet ved ID-tyveri** — Du trenger anmeldelsesnummeret i videre dialog med banker og kredittbyrå.
5. **Klag til Finansklagenemnda** — Fortsetter inkassobyrået uten grunnlag, klager du gratis på finansklagenemnda.no.

## Vanlige feil

- Betale for å bli kvitt brevet — det løser ikke problemet og dokumenterer ikke at kravet var feil
- Ikke svare i det hele tatt — da antas kravet å stå uimotsagt
- Overse muligheten for at det er ID-tyveri som ligger bak

## Vanlige spørsmål

**Jeg ignorerte varselet og nå er saken hos namsmannen — hva gjør jeg?**

Send innsigelse til namsmannen umiddelbart. Du kan protestere mot tvangsinndrivelse. Namsmannen sender saken til forliksrådet, og der kan du legge frem bevis for at kravet er uberettiget.

**Kan inkassobyrået skade kredittscore min?**

En betalingsanmerkning registreres først hvis det ender med dom eller gjeld som ikke betales. Bestrider du tidlig nok og vinner frem, skal ingen anmerkning registreres.

**Hva er ID-tyveri og hvordan beskytter jeg meg fremover?**

ID-tyveri er at noen bruker dine personopplysninger til å inngå avtaler. Sperring for kredittoppslag er det enkleste forebyggende tiltaket.
""",
        "related_paragrafer": [
            {"lov": "inkassoloven", "nummer": "5", "beskrivelse": "rett til å bestride krav"},
            {"lov": "inkassoloven", "nummer": "10", "beskrivelse": "inkassosalær og gebyrenes gyldighet"},
        ],
    },
]
