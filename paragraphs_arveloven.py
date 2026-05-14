"""Arveloven — paragraf-data for Rettsregel."""

PARAGRAPHS = [
    {
        "number": "1",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Hva loven gjelder",
        "kategori": "arv",
        "description": "Hva dekker arveloven? Kort fortalt gjelder den fordeling av arv, uskifte, arveavtaler og skifte av dødsbo.",
        "kort_svar": "Arveloven bestemmer hvordan formue og eiendeler skal fordeles når noen dør. Den dekker hvem som har rett på arv, reglene for uskiftet bo, og hvordan selve booppgjøret skal gjennomføres.",
        "paragraftekst": "Loven gjelder fordelingen av arv etter loven eller testament, ektefellers og samboeres rett til å sitte i uskifte og avtaler om arv.\n\nLoven gjelder også dødsfallsbehandling og skifte av dødsbo, herunder deling av ektefellenes eiendeler etter den ene ektefellens død og skifte av uskiftebo.",
        "hva_betyr_html": """<p>Paragrafen setter rammene for hva hele arveloven handler om. Loven har to hoveddeler i praksis: selve retten til å arve, og hvordan det praktiske oppgjøret etter et dødsfall skal skje.</p>
<p>For det første styrer loven hvem som har rett på verdiene — enten fordi loven automatisk gir dem arverett, eller fordi avdøde har skrevet testament. Den styrer også hvem som kan sitte i uskiftet bo (utsette arveoppgjøret).</p>
<p>For det andre handler loven om «skifte» — selve ryddejobben. Dødsboet (bankkontoer, hus, gjeld) skal gjøres opp, og arveloven bestemmer hvem som har ansvaret for at det skjer riktig.</p>""",
        "eksempler": [{"navn": "Per og Kari", "tekst": "Per dør og etterlater seg kona Kari og to voksne barn. Arveloven bestemmer at Kari kan velge å sitte i uskiftet bo — beholde hus og penger inntil videre. Den bestemmer også hvordan arven skal fordeles mellom barna når Kari selv en dag går bort."}],
        "vanlige_feil": ["Tro at arveloven bare handler om hvem som får penger — den styrer også ansvaret for avdødes gjeld", "Blande sammen arv med skatt — arveloven handler ikke om skatt", "Tro at man kan avtale seg bort fra arveloven uten gyldig testament"],
        "hva_bor_du_html": "<p>Når du skal håndtere et dødsbo, start med å finne ut om det finnes et testament (tingretten har et register). Finnes det ikke, er det lovens faste regler som gjelder. Ta stilling til om dere vil skifte privat eller offentlig — offentlig skifte med oppnevnt advokat er dyrt.</p>",
        "dumme_sporsmal": [
            {"q": "Må jeg betale arveavgift etter denne loven?", "a": "Nei, arveavgiften i Norge ble fjernet i 2014. Arveloven handler bare om hvem som arver hva og hvordan skiftet foregår."},
            {"q": "Kan jeg gjøre barna mine arveløse?", "a": "Nei. Loven sikrer at barna har rett på en minstearv (pliktdelsarv) uansett. Du kan begrense arven deres til en viss sum, men ikke frata dem arven helt."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "2", "tittel": "Definisjoner: Arving, livsarving og samboer", "available": True}, {"lov": "arveloven", "paragraf": "4", "tittel": "Første arvegangsklasse", "available": True}],
    },
    {
        "number": "2",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Viktige definisjoner — arving, livsarving og samboer",
        "kategori": "arv",
        "description": "Hva er egentlig en livsarving? Og når regnes man juridisk som samboer i arvesaker? Her får du arvelovens viktigste definisjoner forklart.",
        "kort_svar": "En «arving» er den som har rett på arv. En «livsarving» er avdødes barn, barnebarn eller oldebarn. En «samboer» er en person over 18 år som lever med en annen i et ekteskapslignende parforhold.",
        "paragraftekst": "Med arving menes den som etter loven eller etter testament har rett til arv etter arvelateren.\n\nMed livsarving menes arvelaterens barn og barnets eller barnas etterkommere.\n\nMed samboer menes en person over 18 år som bor sammen med en annen person over 18 år i et ekteskapsliknende parforhold. Personene regnes som samboere selv om de bor fra hverandre for en tid på grunn av utdanning, arbeid, sykdom, institusjonsopphold eller liknende.",
        "hva_betyr_html": """<p>Tre fagord som går igjen i nesten alle arverettslige regler:</p>
<p><strong>Arving</strong> — hvem som helst med et lovlig krav på en del av arven. Enten et familiemedlem som arver automatisk, eller en venn/organisasjon som er nevnt i et testament.</p>
<p><strong>Livsarving</strong> — person i rett nedstigende linje fra avdøde: primært barna. Å være livsarving gir deg de sterkeste rettighetene — du er sikret en minstearv (pliktdelsarv) uansett hva foreldrene har skrevet i testament.</p>
<p><strong>Samboer</strong> — begge over 18 år, lever som et par. Pendling, sykehusopphold eller studier bryter ikke samboerforholdet juridisk. To absolutte unntak: De kan ikke være nær slekt, og ingen av dem kan formelt være gift eller samboer med noen andre.</p>""",
        "eksempler": [{"navn": "Lars og Tom", "tekst": "Lars og Tom har bodd som kjærester i ti år. Tom må bo på omsorgssenter de siste to årene på grunn av sykdom. Etter arveloven regnes de fortsatt som samboere, fordi adskillelsen var midlertidig og skyldtes sykdom."}],
        "vanlige_feil": ["Tro at stebarn regnes som livsarvinger", "Tro at man er juridisk samboer selv om den ene aldri fikk formell skilsmisse fra et tidligere ekteskap", "Tro at to søsken som bor sammen regnes som samboere"],
        "hva_bor_du_html": "<p>Er du samboer, men partneren er formelt fortsatt gift med en annen? Farlig situasjon — du har null arverettigheter. Sørg for at skilsmissen er formelt gjennomført. Samboere bør uansett alltid skrive gjensidig testament.</p>",
        "dumme_sporsmal": [
            {"q": "Er adopterte barn livsarvinger?", "a": "Ja. Adopterte barn har nøyaktig samme status og arverettigheter som biologiske barn."},
            {"q": "Hva med særboere — kjærester som bor i hver sin leilighet?", "a": "Særboere regnes ikke som samboere i loven. For arverettigheter som samboer må dere faktisk bo på samme adresse. Fravær godtas bare hvis det er forbigående (sykdom, pendling)."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "4", "tittel": "Første arvegangsklasse", "available": True}, {"lov": "arveloven", "paragraf": "12", "tittel": "Arverett for samboere med felles barn", "available": True}],
    },
    {
        "number": "3",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Hvordan arv fordeles og hvem som arver",
        "kategori": "arv",
        "description": "Hvem har rett på arven din? Her forklarer vi hvordan loven fordeler verdiene hvis du ikke har testament, og hva staten gjør hvis du ikke har familie.",
        "kort_svar": "Arveloven gir arverett til slektningene dine og til ektefellen eller samboeren din. Du kan endre fordelingen ved testament. Dør du uten arvinger og uten testament, går formuen til frivillig arbeid for barn og unge.",
        "paragraftekst": "Rett til arv etter loven har arvelaterens slektninger og eventuelt ektefelle eller samboer. Arvelateren kan innenfor lovens rammer fastsette en annen fordeling ved å opprette testament. Har ikke arvelateren arvinger, går arven til frivillig virksomhet til fordel for barn og unge.",
        "hva_betyr_html": """<p>Loven setter opp en fast prioritetsliste. Ektefelle/samboer og familie (barn, barnebarn, foreldre, søsken) arver automatisk. Gjør du ingenting, er det disse reglene som bestemmer.</p>
<p>Men loven gir deg stor frihet: Med et testament kan du gi bort verdier til en venn, et barnebarn eller Redd Barna. Det eneste loven nekter deg, er å ta fra ektefellen eller barna den faste minstearven de har krav på.</p>
<p>Har du ingen gjenlevende slektninger og ikke testament? Pengene går ikke til staten, men til frivillig virksomhet for barn og unge.</p>""",
        "eksempler": [{"navn": "Ingrid", "tekst": "Ingrid er ugift og barnløs. Nærmeste familie er en nevø. Hun skriver testament: familiehytta til en venninne, alle penger til Dyrebeskyttelsen. Fordi hun verken har ektefelle eller livsarvinger, kan hun testamentere bort alt hun eier. Lovens standardregler om at nevøen skal arve, settes til side."}],
        "vanlige_feil": ["Tro at staten sluker alle pengene hvis man ikke har familie", "Tro at et muntlig løfte kan erstatte arvelovens fordeling — det må gjøres via et gyldig skriftlig testament", "Tro at man kan testamentere bort alt selv om man har barn"],
        "hva_bor_du_html": "<p>Er du fornøyd med at loven gir alt til barna og ektefellen? Da trenger du ikke gjøre noe. Er du samboer, enslig uten nær familie, eller vil støtte et veldedig formål — opprette et testament. Sørg for at det er formelt riktig med vitner.</p>",
        "dumme_sporsmal": [
            {"q": "Hva hvis jeg bare har en fjern fetter?", "a": "Fetteren arver deg ikke. Arveretten stopper ved barnebarna til besteforeldrene dine. Har du ingen nærmere familie og ikke testament, går pengene til formål for barn og unge."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "4", "tittel": "Første arvegangsklasse", "available": True}, {"lov": "arveloven", "paragraf": "5", "tittel": "Andre arvegangsklasse", "available": True}],
    },
    {
        "number": "4",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Barnas rett til arv — første arvegangsklasse",
        "kategori": "arv",
        "description": "Hvem står fremst i arvekøen? Barna dine (livsarvinger) tilhører første arvegangsklasse og deler arven likt.",
        "kort_svar": "Dine nærmeste arvinger er barna dine, og de deler arven likt. Hvis et av barna dine er dødt, går andelen videre til dette barnets barn (dine barnebarn).",
        "paragraftekst": "De nærmeste slektsarvingene er arvelaterens livsarvinger. Arven deles likt mellom arvelaterens barn. Hvis et barn er død, går dette barnets del av arven til barnets livsarvinger med lik andel på hver gren. Hvis et barn er død uten å etterlate seg livsarvinger, går dette barnets del til de andre barna.",
        "hva_betyr_html": """<p>Barna dine, også kalt livsarvinger, står aller først i arvegangsklassene. De arver alt du har — med mindre du etterlater deg ektefelle eller samboer som har krav på sin andel først.</p>
<p>Arven deles i nøyaktig like store deler mellom barna. Det spiller ingen rolle om du hadde mer kontakt med ett barn, eller om noen er fra et tidligere forhold (særkullsbarn). Alle biologiske og adopterte barn stiller likt.</p>
<p>Dør et av barna dine før deg? Arven går rett ned til det avdøde barnets egne barn (dine barnebarn), ikke over til søsknene.</p>""",
        "eksempler": [{"navn": "Arne", "tekst": "Arne dør og etterlater seg 900 000 kr. Han var ikke gift. Han hadde to barn: Sara og Jonas. Sara lever og får 450 000 kr. Jonas døde i en ulykke, men etterlot seg to barn. Arnes barnebarn arver Jonas sin del (225 000 kr hver)."}],
        "vanlige_feil": ["Tro at det eldste barnet har rett på mer", "Glemme at særkullsbarn fra tidligere forhold har nøyaktig samme arverett som fellesbarn", "Tro at barnebarn automatisk arver mens foreldrene deres (barna dine) lever"],
        "hva_bor_du_html": "<p>Vil du at et spesifikt barn skal arve noe konkret — for eksempel familiehytta? Skriv et skriftlig testament. Ikke stol på at de «sikkert blir enige». Husk at du ikke kan bryte reglene for pliktdelsarv.</p>",
        "dumme_sporsmal": [
            {"q": "Får stebarnet mitt arv etter meg automatisk?", "a": "Nei. Et stebarn er ikke din livsarving og har ingen arverett etter loven, uansett hvor mange år dere har bodd sammen. Vil du at stebarnet skal arve, må du opprette testament."},
            {"q": "Hva skjer hvis barnebarnet som arver er under 18 år?", "a": "Pengene forvaltes av Statsforvalteren frem til barnet fyller 18 år for å sikre midlene."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "5", "tittel": "Andre arvegangsklasse", "available": True}, {"lov": "arveloven", "paragraf": "8", "tittel": "Ektefellens arverett", "available": True}],
    },
    {
        "number": "5",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Foreldrenes rett til arv — andre arvegangsklasse",
        "kategori": "arv",
        "description": "Hvem arver deg hvis du ikke har barn? Da går arven til foreldrene og søsknene dine — andre arvegangsklasse.",
        "kort_svar": "Dør du uten barn eller barnebarn, går arven til foreldrene dine. De deler arven likt. Er en forelder død, går den halvdelen videre til den avdøde forelderens barn — det vil si dine søsken.",
        "paragraftekst": "Hvis arvelateren ikke har livsarvinger, går arven til foreldrene. Foreldrene arver likt. Hvis en forelder er død, går denne forelderens del av arven til hans eller hennes livsarvinger med lik andel på hver gren.",
        "hva_betyr_html": """<p>Dette er lovens «plan B». Ingen livsarvinger (barn/barnebarn)? Da rykker arven ett ledd tilbake i slektstreet til «andre arvegangsklasse» — mor og far.</p>
<p>Har du ikke ektefelle med arverett, får mor og far halvparten av arven hver. Er en av dem allerede død, forsvinner ikke arven — den goes videre til den avdøde forelderens barn (dine søsken).</p>
<p>Er begge foreldrene døde, vil dine søsken (eller deres barn — dine nevøer og nieser) ende opp med å dele alt.</p>""",
        "eksempler": [{"navn": "Marius", "tekst": "Marius (30) dør ugift og barnløs. Etterlater seg 1 000 000 kr. Moren lever og arver 500 000 kr. Faren er død. Faren hadde to barn med Marius sin mor pluss ett barn fra et tidligere ekteskap. Farens 500 000 kr deles mellom hans tre barn — ca 166 000 kr hver."}],
        "vanlige_feil": ["Glemme at halvsøsken har nøyaktig samme rett til sin biologiske forelders halvdel som helsøsken", "Foreldre som tror de arver barnet uansett — har barnet egne barn, arver foreldrene ingenting", "Tro at en fraskilt forelder mister retten til å arve barnet"],
        "hva_bor_du_html": "<p>Er du ung, singel og barnløs? Alt du eier går til foreldrene og søsknene. Ønsker du heller at en ny samboer eller venner skal arve deg? Opprett testament. Du har ingen barn, så du kan testamentere bort 100 % av alt du eier.</p>",
        "dumme_sporsmal": [
            {"q": "Arver far og mor meg selv om vi ikke har snakket på 20 år?", "a": "Ja. Arveloven bryr seg verken om følelser eller manglende kontakt. For å hindre det, må du lage et testament."},
            {"q": "Arver søsknene mine hvis jeg har barn?", "a": "Nei. Søsken arver bare hvis du ikke har egne barn og foreldrene dine er døde. Barna dine blokkerer all arv til andre i slekten."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "4", "tittel": "Første arvegangsklasse", "available": True}, {"lov": "arveloven", "paragraf": "6", "tittel": "Tredje arvegangsklasse", "available": True}],
    },
    {
        "number": "6",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Besteforeldrenes rett til arv — tredje arvegangsklasse",
        "kategori": "arv",
        "description": "Ingen barn, foreldre eller søsken? Arveloven peker da på besteforeldrene og deres slekt. Men grensen går ved fettere og kusiner.",
        "kort_svar": "Dør du uten barn, foreldre eller søsken, går arven til besteforeldrene dine — eller til deres barn og barnebarn (onkler, tanter, fettere og kusiner). Men der stopper arveretten. Dine tremenninger arver deg ikke.",
        "paragraftekst": "Hvis arvelateren ikke har slektsarvinger etter §§ 4 og 5, går arven til besteforeldrene eller til livsarvinger etter dem. Fjernere livsarvinger etter besteforeldrene enn deres barnebarn har likevel ikke arverett etter loven.",
        "hva_betyr_html": """<p>Tredje og siste stopp for slektsarven. Loven deler arven i to: halvparten til morssiden, halvparten til farssiden.</p>
<p>Siden besteforeldrene som oftest er døde, går arven videre nedover deres grener: til onkler og tanter, og videre til fettere og kusiner. Her setter loven en absolutt grense: Barn av fettere og kusiner (tremenninger) har ingen arverett. Er det tomt for slektninger innenfor grensen, går pengene til statens pott for frivillig arbeid blant barn og unge.</p>""",
        "eksempler": [{"navn": "Håkon", "tekst": "Håkon (78) dør. Enebarn, aldri gift, ingen barn. Foreldrene er døde. På farssiden er det ingen slektninger igjen. Hele 2 millioner kr går til morssiden. På morssiden er tanten død, men hun etterlot seg to barn (Håkons kusiner). De arver 1 million kr hver."}],
        "vanlige_feil": ["Tremenninger som tror de har rett på arv", "Tro at slekt i utlandet mister arveretten — den gjelder uavhengig av bosted", "Tro at en nær venn går foran en fjern fetter uten testament"],
        "hva_bor_du_html": "<p>Har du bare fjerne slektninger? Vurder testament. Loven vil gi alt til fettere og kusiner du kanskje knapt har møtt. Uten barn eller ektefelle står du helt fritt til å testamentere bort alt du eier til hvem du vil.</p>",
        "dumme_sporsmal": [
            {"q": "Halve arven min skulle til farssiden, men der er alle døde. Får staten de pengene?", "a": "Nei. Så lenge du har arvinger på minst én side, går hele potten dit. Staten (frivillig virksomhet) får bare arven hvis BEGGE sider er tomme for arvinger."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "5", "tittel": "Andre arvegangsklasse", "available": True}, {"lov": "arveloven", "paragraf": "3", "tittel": "Fordeling når avdøde ikke har arvinger", "available": True}],
    },
    {
        "number": "7",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Foreldreskap og unntak ved overgrep",
        "kategori": "arv",
        "description": "Holder det å være biologisk i slekt for å kreve arv? Nei — loven krever juridisk foreldreskap. Loven stopper også arv etter alvorlige lovbrudd.",
        "kort_svar": "For å ha arverett som slektning, må slektskapet være formelt fastsatt etter barneloven eller ved adopsjon. Loven forbyr også en far og hans slekt å ta arv etter et barn dersom barnet ble unnfanget ved voldtekt og faren er dømt for dette.",
        "paragraftekst": "Arverett etter dette kapitlet gjelder bare foreldreskap som følger av reglene i barneloven, adopsjonsloven eller annen lov.\n\nFaren og farens slekt tar ikke arv etter barnet dersom det er unnfanget som følge av en handling som er et brudd på straffelovens bestemmelser om voldtekt eller overgrep, og som faren er dømt for.",
        "hva_betyr_html": """<p>Du kan ikke kreve arv fra noen bare ved å påstå at du er i slekt. Juridisk farskap og morskap må være registrert etter barneloven. Adopsjon kutter arveretten til de biologiske foreldrene fullstendig.</p>
<p>Den andre regelen er en sterk moralregel: En overgriper skal ikke tjene på et overgrep. Er en far dømt for voldtekt eller grove seksuelle overgrep som resulterte i at barnet ble unnfanget, mister faren og hele hans familie all rett til å arve dette barnet.</p>""",
        "eksempler": [{"navn": "Eva", "tekst": "Eva ble født etter en overfallsvoldtekt, og gjerningsmannen ble dømt. Eva dør 40 år gammel uten barn eller ektemann. Normalt ville arven deles mellom morssiden og farssiden. Men § 7 blokkerer faren og hele hans familie. All arven etter Eva går utelukkende til moren og morens familie."}],
        "vanlige_feil": ["Tro at man kan kreve farsarv hvis farskapet aldri ble formelt fastsatt", "Adopterte barn som tror de kan arve sine biologiske foreldre i tillegg til adoptivforeldrene"],
        "hva_bor_du_html": "<p>Vet du at du har et barn et sted, eller kjenner du faren din, men det er aldri blitt formelt registrert? Rydd opp i dette FØR et dødsfall skjer. Uten juridisk bekreftet foreldreskap gir det ingen automatisk arverett.</p>",
        "dumme_sporsmal": [
            {"q": "Er fosterbarn likestilt med adopterte barn?", "a": "Nei. Et fosterbarn har ingen automatisk arverett etter sine fosterforeldre. Det kreves en formell adopsjon eller et testament."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "4", "tittel": "Første arvegangsklasse", "available": True}],
    },
    {
        "number": "8",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Ektefellens arverett når arvelateren har barn",
        "kategori": "arv",
        "description": "Loven sikrer ektefellen penger før barna får sitt. Lær hvordan «4G-regelen» kan gjøre at ektefellen arver alt i små bo, mens barna får resten i store bo.",
        "kort_svar": "Som gjenlevende ektefelle har du rett på én fjerdedel (25 %) av arven når den som dør har barn. Men loven gir deg en minstearv på 4G. Er boet under 4G, arver du alt — og barna får ingenting.",
        "paragraftekst": "Ektefellen har rett til en firedel av arven når det er livsarvinger etter arvelateren, men ektefellen har uansett rett til en minstearv på fire ganger folketrygdens grunnbeløp ved arvefallet.",
        "hva_betyr_html": """<p><strong>Hovedregelen (store bo):</strong> Du som ektefelle arver 1/4. Barna deler de resterende 3/4. Eksempel: 4 millioner kr — du får 1 million, barna deler 3 millioner.</p>
<p><strong>Minstearv (4G):</strong> Grunnbeløpet (G) justeres hvert år. Er hele boet under 4G (ca 500 000 kr), tar du rubbel og bit. Barna får ingenting. Dette kan sjokkere særkullsbarn i blandede familier.</p>""",
        "eksempler": [
            {"navn": "Kari og Toms barn", "tekst": "Karis ektemann Tom dør. Tom hadde to barn fra sitt første ekteskap. Tom etterlot seg 350 000 kr på konto. Barna krever sin arv, men Kari viser til § 8: Under 4G = hun tar alt. Barna får ingenting."},
        ],
        "vanlige_feil": ["Tro at barnas pliktdelsarv alltid utbetales — ektefellens minstearv går foran", "Tro at ektefellen kan gjemme verdier ved å verdsette dem lavt — barna kan kreve skiftetakst"],
        "hva_bor_du_html": """<p>Er du barn fra et tidligere forhold og får beskjed om at «boet er under 4G»? Krev fullt innsyn. Be om kopi av ligningen, kontoutskrifter og verdsettelse av eiendommer. Er hytta verdsatt til ligningsverdi i stedet for markedsverdi, kan du kreve at den takseres av megler.</p>""",
        "dumme_sporsmal": [
            {"q": "Gjelder 4G-regelen selv om vi hadde ektepakt med særeie?", "a": "Ja. Minstearven på 4G gjelder uansett om mannen bare hadde penger som var hans fullstendige særeie. Det er en absolutt sikkerhetsventil."},
            {"q": "Gjelder dette også gjeld?", "a": "Minstearven regnes av boets netto. Trekk fra avdødes gjeld og begravelsesutgifter først."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "9", "tittel": "Ektefellens arverett uten barn", "available": True}, {"lov": "arveloven", "paragraf": "14", "tittel": "Retten til uskifte", "available": True}],
    },
    {
        "number": "9",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Ektefellens arverett når arvelateren ikke har barn",
        "kategori": "arv",
        "description": "Arver du alt når ektefellen dør barnløs? Nei. Loven gir deg halvparten og en minstearv på 6G — med svigerfamilien på den andre halvdelen.",
        "kort_svar": "Dør ektefellen din uten barn, har du rett på halvparten av arven. Minstearven er 6G (ca 700 000 kr). Er avdødes foreldre og søsken døde, arver du alt uansett.",
        "paragraftekst": "Ektefellen har rett til halvparten av arven når arvelaterens nærmeste slektsarvinger er foreldrene eller deres etterkommere, men ektefellen har uansett rett til en minstearv på seks ganger folketrygdens grunnbeløp ved arvefallet.\n\nEktefellen arver alt når det verken er livsarvinger eller slektsarvinger etter arvelateren.",
        "hva_betyr_html": """<p>Mange par uten barn tror at de arver hverandre fullt og helt. Det er feil. Dør en barnløs ektefelle, ser loven mot foreldrene — og deretter søsknene.</p>
<p><strong>Du får halvparten</strong> av arven, og avdødes slekt (foreldre/søsken) deler den andre halvparten.</p>
<p><strong>Minstearven er 6G</strong> (høyere enn for par med barn). Er boet under 6G, tar du alt og svigerfamilien får ingenting.</p>
<p>Er avdødes foreldre og alle søsken/nevøer/nieser døde, arver du alt.</p>""",
        "eksempler": [{"navn": "Sara og Petter", "tekst": "Sara og Petter, gift i ti år uten barn. Petter dør, etterlater 2 000 000 kr. Petters far og bror lever. Over 6G: halvering slår inn. Sara arver 1 000 000 kr. Den andre halvparten deles av Petters far og bror. Sara ble overrasket — men slik er loven når det ikke finnes testament."}],
        "vanlige_feil": ["Barnløse ektepar som tror den gjenlevende automatisk arver alt uten testament", "Glemme at svigerfamilie har krav på inntil halvparten av huset man eide sammen"],
        "hva_bor_du_html": "<p>Barnløse ektepar bør nesten alltid skrive gjensidig testament. Siden dere ikke har barn, er det ingen pliktdelsarv å ta hensyn til. Dere kan gi hverandre 100 %. Gjør det.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om ektefellen min testamenterte bort alt til naboen?", "a": "Du har fremdeles et ufravikelig krav på minstearven på 6G. Ektefellen kan ikke testamentere deg under denne grensen uten at du ble varslet mens han/hun levde."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "8", "tittel": "Ektefellens arverett med barn", "available": True}, {"lov": "arveloven", "paragraf": "10", "tittel": "Kan du begrense ektefellens arv i testament?", "available": True}],
    },
    {
        "number": "10",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Kan du begrense ektefellens arv i testament?",
        "kategori": "arv",
        "description": "Vil du gi barna mer og ektefellen mindre? Det er lov — men ektefellen må ha visst om testamentet, og minstearven er uansett hellig.",
        "kort_svar": "Du kan skrive et testament som gir ektefellen din mindre arv enn lovens utgangspunkt. Men ektefellen må ha fått vite om testamentet før du dør. Og du kan aldri frata ektefellen minstearven på 4G eller 6G.",
        "paragraftekst": "Ektefellens rett til arv kan begrenses ved testament bare hvis han eller hun har fått kunnskap om testamentet før arvelaterens død. Et beløp tilsvarende seks ganger folketrygdens grunnbeløp ved arvefallet kan ikke fratas ektefellen ved testament. Etterlater arvelateren seg livsarvinger, er beløpsgrensen fire ganger folketrygdens grunnbeløp.",
        "hva_betyr_html": """<p>Loven aksepterer ikke at du i hemmelighet testamenterer ektefellen din pengelens. Vil du redusere ektefellens andel, må du spille med åpne kort: Ektefellen må ha fått vite om testamentet FØR du dør.</p>
<p>Ektefellen trenger ikke samtykke — bare ha fått kunnskap. Unntaket gjelder bare hvis det var umulig å varsle (alvorlig demens, forsvunnet).</p>
<p>Uansett kan du aldri ta fra dem minstearven: 4G hvis dere har barn, 6G hvis dere ikke har barn. Den er absolutt.</p>""",
        "eksempler": [{"navn": "Jens og Astrid", "tekst": "Jens vil at særkullsbarna skal ha mest mulig. Han skriver testament: Astrid skal kun arve 4G, resten til barna. Han gir Astrid en kopi mens han lever. Siden hun ble informert og han holder seg over grensen på 4G, er testamentet 100 % gyldig."}],
        "vanlige_feil": ["Skrive et testament som tar fra ektefellen lovens andel, uten å fortelle dem om det", "Tro at man kan testamentere ektefellen under minstearvsgrensen"],
        "hva_bor_du_html": "<p>Oppretter du et testament som innskrenker ektefellens arverett? Sørg for bevis. Sikreste løsning: La ektefellen signere på selve testamentet med teksten «Erklærer å ha fått kunnskap om dette testamentet» og dato.</p>",
        "dumme_sporsmal": [
            {"q": "Hva skjer hvis jeg glemte å fortelle kona mi at hun får mindre?", "a": "Den delen av testamentet som fratar henne lovens andel, erklæres ugyldig. Hun krever sin fjerdedel eller halvpart som om testamentet aldri fantes for hennes del."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "8", "tittel": "Ektefellens arverett", "available": True}, {"lov": "arveloven", "paragraf": "9", "tittel": "Ektefellens arverett uten barn", "available": True}],
    },
    {
        "number": "11",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Mister du arven ved separasjon og skilsmisse?",
        "kategori": "arv",
        "description": "Holder det å flytte fra hverandre for å miste arveretten? Nei. Loven krever at en formell begjæring er sendt og mottatt av Statsforvalteren eller tingretten.",
        "kort_svar": "Ektefeller mister retten til arv (og uskifte) når kravet om separasjon eller skilsmisse er sendt inn og offisielt mottatt av Statsforvalteren eller tingretten. Å flytte fra hverandre er ikke nok.",
        "paragraftekst": "Ektefellen har ikke rett til arv etter §§ 8 eller 9 hvis en av ektefellene har begjært separasjon eller fremsatt stevning med krav om skilsmisse før arvelateren døde, og begjæringen eller stevningen er mottatt av statsforvalteren eller retten før dødsfallet.",
        "hva_betyr_html": """<p>Grensen er tydelig: Arveretten opphører det øyeblikket separasjonsskjemaet lander i innboksen til Statsforvalteren — ikke når bruddet er et faktum i hjemmet, og ikke når skilsmissen er endelig innvilget.</p>
<p>Det er uten betydning hvem av dere som sendte inn begjæringen, eller om den andre var uenig. Dør en av dere i separasjonsåret — selv om skilsmissen ikke er ferdig — er dere ikke lenger arvinger etter hverandre.</p>""",
        "eksempler": [{"navn": "Per og Ingrid", "tekst": "Per sender separasjonsbegjæring elektronisk til Statsforvalteren om morgenen. Samme dag, etter at Statsforvalteren har mottatt begjæringen, får Per hjerteinfarkt og dør. Selv om de var formelt gift da Per døde, arver Ingrid ingenting. Begjæringen var mottatt."}],
        "vanlige_feil": ["Ektefeller som flytter fra hverandre men drøyer med papirene — dør den ene, arver den andre alt", "Tro at en privat avtale om samlivsbrudd opphever arveretten"],
        "hva_bor_du_html": "<p>Er bruddet et faktum? Ikke la papirarbeidet ligge. Send inn begjæring om separasjon via Altinn umiddelbart. Det skaper juridisk beskyttelse av arven din med én gang — spesielt viktig hvis du har særkullsbarn.</p>",
        "dumme_sporsmal": [
            {"q": "Han hadde et testament der jeg fikk penger. Faller dette bort ved separasjon?", "a": "Ikke automatisk via § 11, men arveloven § 58 sier at testamentet normalt faller bort hvis samlivet tok slutt. For full sikkerhet: Trekk også tilbake det gamle testamentet ditt."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "8", "tittel": "Ektefellens arverett", "available": True}, {"lov": "arveloven", "paragraf": "14", "tittel": "Retten til uskifte", "available": True}],
    },
    {
        "number": "12",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Arverett for samboere med felles barn",
        "kategori": "arv",
        "description": "Samboere arver ikke hverandre automatisk — men har dere felles barn, har du krav på en minstearv på 4G. Lær om samboerens arverettigheter.",
        "kort_svar": "Er du samboer og har, har hatt eller venter felles barn med partneren din, har du rett på en minstearv på fire ganger folketrygdens grunnbeløp (4G) hvis partneren dør. Dette er alt loven gir deg automatisk.",
        "paragraftekst": "Den som var samboer med arvelateren ved dødsfallet og har, har hatt eller venter barn med arvelateren, har rett til en arv på fire ganger folketrygdens grunnbeløp ved arvefallet. Dette gjelder også om det er livsarvinger etter arvelateren.\n\nSamboerens rett til arv kan begrenses ved testament bare hvis han eller hun har fått kunnskap om testamentet før arvelaterens død.",
        "hva_betyr_html": """<p>Samboere stiller svakt i loven. Uten testament: ingenting. Men har dere dannet familie med felles barn, gir loven deg ett viktig sikkerhetsnett: 4G.</p>
<p>Er hele boet under 4G, tar du alt og barna venter. Er boet over 4G, tar du dine 4G, og resten fordeles mellom barna.</p>
<p>Du får aldri mer enn 4G etter loven — selv om boet er på 10 millioner. Gifte ektefeller ville fått en fjerdedel (2,5 millioner). Forskjellen er enorm.</p>""",
        "eksempler": [{"navn": "Sofie og Lars", "tekst": "Sofie er samboer med Lars, som har en voksen sønn fra før. Lars og Sofie har en felles toåring. Lars dør uten testament. Boet er 900 000 kr. Sofie tar 4G (480 000 kr). De resterende 420 000 kr deles mellom barna — 210 000 kr til hvert."}],
        "vanlige_feil": ["Tro at langvarig samboerskap automatisk gir arverett — uten barn gir loven deg ingenting", "Tro at stebarn utløser regelen — det må være felles biologisk/adoptert barn", "Tro at samboer får en fjerdedel som en ektefelle"],
        "hva_bor_du_html": "<p>Å stole blindt på lovens 4G er farlig. Er boet stort nok, kan du ende opp uten mulighet til å kjøpe ut barna fra huset ditt. Skriv et gjensidig testament som utvider samboerens rettigheter — og ta en livsforsikring med partneren som begunstiget.</p>",
        "dumme_sporsmal": [
            {"q": "Vi har bodd sammen i 10 år men ikke fått barn. Får jeg ingenting?", "a": "Korrekt — du får null etter lovens hovedregler. Samboere uten barn er fullstendig avhengige av et gjensidig testament."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "13", "tittel": "Arverett for samboere etter fem år", "available": True}, {"lov": "arveloven", "paragraf": "8", "tittel": "Ektefellens arverett med barn", "available": True}],
    },
    {
        "number": "13",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Arverett etter testament for samboere etter fem år",
        "kategori": "arv",
        "description": "Har dere bodd sammen i fem år uten barn? Loven gir dere mulighet til å skrive et testament som sikrer den lengstlevende inntil 4G — selv om det spiser av barnas pliktdelsarv.",
        "kort_svar": "Samboere uten felles barn arver ikke hverandre automatisk. Men etter fem år kan samboeren skrive et testament som gir den gjenlevende inntil 4G — og dette er gyldig selv om det reduserer barnas pliktdelsarv.",
        "paragraftekst": "Arvelateren kan fastsette i testament at den han eller hun har vært samboer med i de siste fem årene før dødsfallet, har rett til arv opp til fire ganger folketrygdens grunnbeløp ved arvefallet uten hensyn til livsarvingenes pliktdelsarv etter § 50.",
        "hva_betyr_html": """<p>Normalt er barnas pliktdelsarv hellig og kan ikke settes til side. Men etter fem år åpner loven ett spesielt smutthull: Du kan testamentere inntil 4G til samboeren din, selv om det går på bekostning av barnas pliktdelsarv.</p>
<p>Det krever et gyldig, skriftlig testament. De fem årene utløser ingenting av seg selv.</p>
<p>Betingelsen: Dere må ha bodd sammenhengende som et par i fem år rett FØR dødsfallet. Midlertidige avbrudd (sykehus, pendling) bryter ikke fristen.</p>""",
        "eksempler": [{"navn": "Jonas og Eva", "tekst": "Jonas og Eva har vært samboere i seks år. Ingen felles barn, men Jonas har sønnen Lars. Jonas oppretter testament: Eva får 4G (480 000 kr). Jonas dør, boet er 600 000 kr. Lars krever sin pliktdelsarv, men § 13 gjør at Eva vinner. Eva får 480 000 kr, Lars får 120 000 kr."}],
        "vanlige_feil": ["Tro at fem års samboerskap automatisk gir arverett — du får ingenting uten testament", "Skrive testament etter tre år og tro at det «oppgraderes» automatisk til § 13 etter fem år"],
        "hva_bor_du_html": "<p>Har dere bodd sammen i fem år? Opprett et gjensidig testament i dag med to vitner. Skriv tydelig at arven gis i medhold av arveloven § 13 og skal gå foran livsarvingenes pliktdelsarv.</p>",
        "dumme_sporsmal": [
            {"q": "Hva hvis vi har felles barn? Må vi vente fem år?", "a": "Nei. Felles barn gir rett til 4G automatisk fra dag én etter § 12, uten å vente fem år og uten testament (men testament anbefales for å sikre mer)."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "12", "tittel": "Arverett for samboere med felles barn", "available": True}],
    },
    {
        "number": "14",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Retten til å sitte i uskiftet bo for gifte",
        "kategori": "arv",
        "description": "Hva betyr «uskiftet bo»? Ektefeller kan utsette arveoppgjøret med felles barn. Slik fungerer uskifte i praksis.",
        "kort_svar": "Som gjenlevende ektefelle kan du «sitte i uskiftet bo» — beholde hus, penger og eiendeler uten å betale ut barna med én gang. Skiftet utsettes til du gifter deg på nytt eller dør. Du trenger ikke barnas tillatelse (så lenge de er felles barn).",
        "paragraftekst": "Når den ene ektefellen dør, har den lengstlevende ektefellen rett til å overta felleseiet uskiftet overfor den førstavdødes andre arvinger etter loven.\n\nDen lengstlevende har rett til å sitte i uskifte med særeie hvis dette er bestemt i ektepakt eller bestemt av en giver eller testator, eller hvis arvingene samtykker.",
        "hva_betyr_html": """<p>Å «skifte» et bo betyr å gjøre opp arven. Å sitte i «uskifte» betyr det motsatte: Hele arveoppgjøret settes på pause.</p>
<p>Du beholder alle eiendelene (felleseiet) og trenger ikke betale ut barna. Du overtar retten til å bo i huset, kjøre bilen, bruke pengene — nesten som før. Barna arver ikke før du velger å skifte frivillig, gifter deg på nytt, eller dør.</p>
<p><strong>Viktig:</strong> Du overtar også avdødes gjeld. Sjekk alltid gjelden FØR du velger uskifte. Og uskifte skjer ikke automatisk — du må fylle ut skjema og sende til tingretten innen 60 dager.</p>""",
        "eksempler": [{"navn": "Kari og Ola", "tekst": "Ola og Kari har to felles barn, nedbetalt hus og sparepenger. Ola dør. Kari sender melding til tingretten om uskifte. Hun trenger ikke spørre barna. Hun beholder huset og pengene. Barna arver først når Kari dør om 20 år."}],
        "vanlige_feil": ["Tro at uskifte skjer av seg selv — du må fylle ut skjema (Melding om uskiftet bo) til tingretten", "Tro at man kan sitte i uskifte med avdødes særeie uten samtykke", "Glemme at du personlig overtar ansvaret for avdødes gjeld og lån"],
        "hva_bor_du_html": "<p>Mister du ektefellen? Vurder uskifte. Hadde avdøde lite gjeld, er det som oftest den beste løsningen. Hadde avdøde mye kredittkortgjeld og inkasso? Tenk deg nøye om — du blir personlig ansvarlig for alt. Sjekk alltid gjelden først.</p>",
        "dumme_sporsmal": [
            {"q": "Barna mine krever arv, kan de nekte meg å sitte i uskifte?", "a": "Nei. Så lenge de er felles barn av deg og avdøde, kan de ikke nekte. Bare særkullsbarn (barn fra tidligere forhold) kan nekte."},
            {"q": "Hva skjer med uskiftet hvis jeg får ny kjæreste?", "a": "Ny kjæreste er greit. Men gifter du deg på nytt, må du gjøre opp arven og betale ut barna FØR du inngår nytt ekteskap."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "15", "tittel": "Uskifte med særkullsbarn", "available": True}],
    },
    {
        "number": "15",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Uskifte når avdøde hadde særkullsbarn",
        "kategori": "arv",
        "description": "Hadde ektefellen din barn fra et tidligere forhold? Da har du ingen automatisk rett til uskiftet bo. Særkullsbarna må samtykke.",
        "kort_svar": "Du har ingen automatisk rett til uskiftet bo med arven til ektefellens barn fra tidligere forhold. For å beholde huset og midlene uten å skifte, må disse særkullsbarna si ja. Sier de nei, må du betale dem ut.",
        "paragraftekst": "Den lengstlevende ektefellen har rett til uskifte med arvelaterens særskilte livsarving (særkullsbarn eller livsarving til særkullsbarn) bare hvis denne arvingen samtykker. Det kan settes vilkår for samtykke.",
        "hva_betyr_html": """<p>Mens felles barn pent må vente på arven, har særkullsbarn en spesiell beskyttelse. Et «særkullsbarn» er ektefellens barn fra et tidligere forhold. Siden dette barnet ikke er i slekt med deg, vil ikke loven tvinge dem til å vente til du dør.</p>
<p>Vil du sitte i uskifte, må du be særkullsbarna om lov. De kan si nei. De kan også sette vilkår for å si ja — for eksempel at du ikke tar opp mer gjeld med pant i huset.</p>
<p>Er særkullsbarnet under 18 år, er saken enda vanskeligere: Da er det vergen (eksen til avdøde) og Statsforvalteren som bestemmer. Statsforvalteren sier nesten alltid nei.</p>""",
        "eksempler": [{"navn": "Anne og Marius", "tekst": "Anne er gift med Tom. Tom har en voksen sønn, Marius, fra tidligere. Tom dør. Anne vil sitte i uskifte, men Marius trenger pengene nå og sier nei. Anne har da ingen rett til uskifte. Huset må selges eller Anne tar opp lån for å kjøpe ut Marius sin arveandel."}],
        "vanlige_feil": ["Tro at man er sikret uskifte bare fordi man har vært gift lenge med særkullsbarnets forelder", "Ektefeller med mine og dine barn som drøyer med testament fordi «vi blir nok enige»"],
        "hva_bor_du_html": "<p>Er du gift med noen som har særkullsbarn? Gå aldri ut fra at de gir deg uskifte. Snakk med dem nå mens dere alle lever — dere kan inngå en forhåndsavtale. Opprett også et testament som maksimerer den gjenlevendes arv.</p>",
        "dumme_sporsmal": [
            {"q": "Må alle særkullsbarna være enige?", "a": "Ja. Er det tre særkullsbarn og to sier ja men én sier nei, kan du ikke sitte i uskifte med den som sier nei. Du kan imidlertid betale ut den ene og sitte i delvis uskifte med de to andre. Se § 16."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "14", "tittel": "Retten til uskifte", "available": True}, {"lov": "arveloven", "paragraf": "16", "tittel": "Uskifte når noen av arvingene krever arv", "available": True}],
    },
    {
        "number": "16",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Uskifte når bare noen arvinger krever arv",
        "kategori": "arv",
        "description": "Mister du retten til uskifte hvis ett særkullsbarn krever utbetaling? Nei — du kan betale ut det ene barnet og sitte i uskifte med resten.",
        "kort_svar": "Selv om ett særkullsbarn nekter og krever arven sin nå, mister du ikke uskifteretten overfor de andre arvingene. Du kan betale ut det ene barnet, og fortsette å sitte i uskifte med de resterende.",
        "paragraftekst": "Selv om noen arvinger kan kreve arv, mister ikke den lengstlevende ektefellen retten til uskifte med andre arvinger.",
        "hva_betyr_html": """<p>Denne paragrafen redder gjenlevende ektefeller i sammensatte familier og tillater «delvis skifte».</p>
<p>Et særkullsbarn sier nei til uskifte og vil ha pengene sine. Det ødelegger ikke uskifteretten overfor de andre barna. Du gjør opp med det ene barnet — kjøper det ut via banklån eller sparepenger — og sender dette til tingretten. Deretter får du uskifteattest for de resterende arvingene.</p>""",
        "eksempler": [{"navn": "Eva og barna", "tekst": "Evas mann Per dør. Særkullsbarnet Lars vil ha 800 000 kr nå. Fellesbarn Sofie (800 000 kr) har ikke lov til å nekte. Eva tar opp lån og betaler ut Lars. Lars er ferdig med saken. Eva sitter i uskifte, og Sofie arver sin del + Evas egne verdier når Eva dør."}],
        "vanlige_feil": ["Tro at hele huset må selges fordi ett av barna sier nei til uskifte", "Glemme at særkullsbarnet som kjøpes ut, ikke har krav på mer arv når den gjenlevende ektefellen dør"],
        "hva_bor_du_html": "<p>Regn på om du har økonomi til å løse ut særkullsbarnet. Kan du øke boliglånet? Sørg for en skriftlig avtale der barnet kvitterer på å ha mottatt full arv. Send dette til tingretten sammen med søknaden om uskifte for de øvrige arvingene.</p>",
        "dumme_sporsmal": [
            {"q": "Får særkullsbarnet som jeg kjøper ut, mer arv når jeg dør?", "a": "Nei. Betaler du dem ut nå, er det et fullt og endelig oppgjør. Dør du 30 år senere og boligen har femdoblet seg i verdi, har dette særkullsbarnet ingen krav på mer."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "15", "tittel": "Uskifte med særkullsbarn", "available": True}, {"lov": "arveloven", "paragraf": "14", "tittel": "Retten til uskifte", "available": True}],
    },
]


_EXTRA_ARV = [
    {
        "number": "17",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Kan ektefellen nektes uskifte i et testament?",
        "kategori": "arv",
        "description": "Kan ektefellen din nekte deg å sitte i uskiftet bo ved å skrive et hemmelig testament? Svaret er nei. Du har krav på å få vite det mens partneren lever.",
        "kort_svar": "Ektefellen din kan skrive et testament som tar fra deg retten til å sitte i uskiftet bo. Men for at dette skal være gyldig, må du ha fått vite om testamentet før ektefellen din døde. Hemmelige testamenter som nekter deg uskifte, er ikke gyldige.",
        "paragraftekst": "Ektefellens rett til uskifte etter dette kapitlet kan begrenses ved testament bare hvis han eller hun har fått kunnskap om testamentet før arvelaterens død. Vilkåret om at ektefellen må ha fått kunnskap om testamentet, gjelder ikke hvis det var umulig eller urimelig vanskelig å varsle ektefellen om testamentet.",
        "hva_betyr_html": """<p>Som utgangspunkt har du en sterk rett til å utsette arveoppgjøret med felles barn ved å sitte i uskiftet bo. Men avdøde kan ha hatt gode grunner for at hele boet heller burde gjøres opp med én gang — kanskje en familiebedrift som måtte overføres, eller et ekteskap som hang i en tynn tråd.</p>
<p>Siden det å miste uskifteretten kan bety at du må selge hjemmet ditt, stiller loven et ufravikelig krav: Du skal ha fått beskjed mens ektefellen din fortsatt er i live. Dette gir deg muligheten til å planlegge fremtiden din økonomisk — eller eventuelt søke om skilsmisse.</p>
<p>Unntaket er hvis du er helt umulig å få tak i, for eksempel forsvunnet eller så syk at du ikke forstår noe som helst.</p>""",
        "eksempler": [{"navn": "Håkon og Mette", "tekst": "Håkon eier en kostbar næringseiendom og vil at sønnen skal ta over driften straks Håkon dør. Han skriver testament: 'Min kone Mette skal ikke ha rett til å sitte i uskiftet bo med næringseiendommen.' For at dette skal gjelde, må Håkon vise testamentet til Mette. Mette trenger ikke å like det — men hun må ha lest eller blitt fortalt innholdet. Fordi Mette er varslet, faller uskifteretten for næringseiendommen bort den dagen Håkon dør."}],
        "vanlige_feil": ["Opprette testament hos advokat og låse det i en safe uten å fortelle partneren — klausulen om uskifte blir da ugyldig", "Tro at ektefellen må signere en formell godkjenning — de må bare få kunnskap om det", "Glemme bevisbyrden — arvingene vil slite med å bevise at du visste om testamentet hvis det ikke finnes et skriftlig bevis"],
        "hva_bor_du_html": "<p>Vil du nekte ektefellen å sitte i uskifte? Sørg for bevis. Få ektefellen til å signere direkte på selve testamentet med teksten «Erklærer å ha fått kunnskap om dette», dato og signatur. Da er det ingen tvil.</p><p>Er du gjenlevende og barna drar frem et hemmelig testament som nekter deg uskifte: Krev dokumentasjon på at du noen gang ble varslet. Kan de ikke bevise det, gjelder testamentet ikke for den delen.</p>",
        "dumme_sporsmal": [
            {"q": "Faller minstearven min på 4G bort hvis jeg nektes uskifte?", "a": "Nei, absolutt ikke. Retten til uskifte og retten til minstearv (4G) er to helt forskjellige ting. Du får fortsatt din lovfestede andel av arven."},
            {"q": "Kan barna bestemme seg for å nekte meg uskifte?", "a": "Ikke hvis de er felles barn. Dette krever enten at de er særkullsbarn, eller at avdøde selv nektet deg det gjennom et gyldig varslet testament."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "14", "tittel": "Retten til uskifte", "available": True}, {"lov": "arveloven", "paragraf": "10", "tittel": "Inngrep i ektefellens arverett ved testament", "available": True}, {"lov": "arveloven", "paragraf": "18", "tittel": "Personlige forhold som stanser uskifte", "available": True}],
    },
    {
        "number": "18",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Personlige forhold som stanser uskifte",
        "kategori": "arv",
        "description": "Har du stor gjeld eller bruker du penger helt uforsvarlig? Da kan arvingene nekte deg å sitte i uskifte, for å redde familiens verdier. Les vilkårene her.",
        "kort_svar": "Du kan nektes å sitte i uskiftet bo hvis du har høy personlig gjeld som truer arven til arvingene, eller hvis du er så økonomisk uansvarlig at du ikke kan forventes å ta vare på verdiene på en forsvarlig måte.",
        "paragraftekst": "Den lengstlevende ektefellen har ikke rett til uskifte hvis det sannsynliggjøres at hans eller hennes gjeldsforpliktelser vil gjøre det vanskeligere å få dekket krav mot den avdøde ektefellen, eller at disse forpliktelsene vil redusere arven til den avdødes arvinger vesentlig. Det samme gjelder hvis den lengstlevende ektefellen på en klanderverdig måte har påført eller utsatt seg selv eller andre for et betydelig formuestap og derfor ikke kan ventes å styre uskifteformuen på en forsvarlig måte.",
        "hva_betyr_html": """<p>Loven setter to klare grunner til at barna kan stoppe deg fra å overta boet uskiftet:</p>
<p><strong>1. Du har stor gjeld.</strong> Når du sitter i uskifte, blandes avdødes formue med din. Dine kreditorer kan da ta pant i huset. Er gjelden stor nok, kan barna nekte deg uskifte.</p>
<p><strong>2. Du er grovt økonomisk uansvarlig.</strong> Tung spillegalskap, omfattende svindel, rusproblemer som drenerer økonomien. Det holder ikke at barna synes du sløser litt — du må ha opptrådt «klanderverdig» og påført deg selv et «betydelig formuestap».</p>""",
        "eksempler": [{"navn": "Tom", "tekst": "Toms kone dør. Barna kan bevise at Tom har 2 millioner i spillegjeld og aktive inkassosaker. Hvis Tom overtar huset uskiftet, vil kreditorene ta pant umiddelbart. Barna nekter Tom uskifte og viser til § 18. Tom må skifte boet med en gang — barna redder farsarven unna Toms kreditorer."}],
        "vanlige_feil": ["Barna prøver å nekte uskifte bare fordi far drikker mye, uten å bevise faktisk «betydelig formuestap»", "Tro at vanlig boliglån stopper uskifte — det er misligholdt gjeld loven vil til livs"],
        "hva_bor_du_html": "<p>Er du arving og ser at den gjenlevende er i ferd med å dra hele formuen ned i et sluk? Meld fra skriftlig til tingretten om at vilkårene i § 18 er oppfylt. Legg ved dokumentasjon (betalingsanmerkninger, bevis på spillegjeld).</p>",
        "dumme_sporsmal": [
            {"q": "Hva menes med «betydelig formuestap»?", "a": "Det må være mye penger i forhold til totaløkonomien. Å bruke 50 000 kr på en båt er ikke nok. Å ta opp 1 million til 20 % rente for å investere i krypto kan fort være nok."},
            {"q": "Hvem avgjør om jeg er «uforsvarlig»?", "a": "Tingretten avgjør i siste instans hvis barna krever offentlig skifte eller nekter deg uskifte."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "14", "tittel": "Retten til uskifte", "available": True}, {"lov": "arveloven", "paragraf": "28", "tittel": "Retten til å kreve skifte", "available": True}, {"lov": "arveloven", "paragraf": "30", "tittel": "Krav på vederlag ved sløsing", "available": True}],
    },
    {
        "number": "19",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Frist for å kreve uskifte — 60 dager",
        "kategori": "arv",
        "description": "Skal du overta boet etter din avdøde ektefelle? Pass på fristen! Du har 60 dager på å melde fra til tingretten om at du ønsker å sitte i uskiftet bo.",
        "kort_svar": "For å gjøre bruk av retten til å sitte i uskiftet bo, må du gi skriftlig beskjed til tingretten innen 60 dager etter at ektefellen din døde.",
        "paragraftekst": "En ektefelle som vil gjøre bruk av retten til uskifte, skal innen 60 dager etter dødsfallet sende melding til tingretten etter reglene i § 96.",
        "hva_betyr_html": """<p>Retten til å sitte i uskifte kommer ikke seilende av seg selv. Du må aktivt fylle ut en blankett og sende den til domstolen der den avdøde bodde. Du har 60 dager fra dødsfallet.</p>
<p>I de tunge ukene etter et dødsfall er det mye å tenke på, men fristen er viktig: Uten den kan tingretten starte et offentlig skifte, noe som koster store summer.</p>
<p>Skjemaet heter «Melding om uskiftet bo» og finnes på domstol.no.</p>""",
        "eksempler": [{"navn": "Anne", "tekst": "Annes ektemann dør 1. mars. I sorgen glemmer hun alt av papirer frem til slutten av mai. Da er fristen på 60 dager utløpt. Anne kontakter tingretten umiddelbart. Siden ingen arvinger ennå har krevd skifte, er tingretten grei — men hun tok en stor risiko."}],
        "vanlige_feil": ["Legge saken i skuffen og tro at siden man har felles barn og felles hus, ordner staten det automatisk", "Glemme at avdødes bankkontoer er frosset frem til uskifteattesten er utstedt"],
        "hva_bor_du_html": "<p>Gå inn på domstol.no, last opp skjemaet «Melding om uskiftet bo», og fyll det ut. Send det innen to måneder fra dødsfallet.</p>",
        "dumme_sporsmal": [
            {"q": "Hva skjer hvis jeg sender skjemaet etter 65 dager?", "a": "Sjelden en full krise hvis du er noen dager for sent ute og ingen arvinger har krevd skifte. Tingretten kan forlenge fristen. Men overser du fristen fullstendig, kan tingretten starte et offentlig skifte — svært dyrt."},
            {"q": "Må jeg legge ved full takst av huset innen 60 dager?", "a": "Nei. Meldingen krever bare en grov oversikt. Du trenger ikke megler eller takstmann for å kreve uskifte."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "14", "tittel": "Retten til uskifte", "available": True}, {"lov": "arveloven", "paragraf": "20", "tittel": "Du overtar avdødes gjeld", "available": True}],
    },
    {
        "number": "20",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Du overtar avdødes gjeld i et uskiftet bo",
        "kategori": "arv",
        "description": "Skal du sitte i uskiftet bo? Vit at du samtidig påtar deg fullt personlig ansvar for all gjelden til avdøde. Lær hvordan du sjekker gjelden trygt med proklama.",
        "kort_svar": "Når du velger å overta boet uskiftet, påtar du deg samtidig fullt ansvar for all gjelden den avdøde hadde — personlig. Hvis du er usikker på gjelden, bør du utstede proklama FØR du sier ja til uskifte.",
        "paragraftekst": "Ved å overta boet uskiftet blir den lengstlevende ektefellen ansvarlig for arvelaterens forpliktelser. Ektefellen kan utstede proklama etter §§ 100 til 103.",
        "hva_betyr_html": """<p>Dette er den viktigste fellen å unngå. «Uskifte» betyr at du overtar alt — både pluss og minus. Idet tingretten gir deg uskifteattesten, flyttes all avdødes gjeld over på dine skuldre. Personlig ansvar: bankene kan ta trekk i lønnen din.</p>
<p><strong>Proklama</strong> er redningsknappen: En offisiell annonse i Norsk Lysingsblad som ber alle kreditorer melde seg innen seks uker. Melder de seg ikke, slettes gjelden automatisk. Utsteder du proklama FØR du tar over i uskifte, vet du nøyaktig hva du påtar deg.</p>
<p>Viser gjelden seg å overstige verdiene? Da snur du i døra — boet skiftes, du slipper å bli personlig ruinert av ukjent gjeld.</p>""",
        "eksempler": [{"navn": "Eva", "tekst": "Evas ektemann drev et lite byggefirma. Eva søkte straks om uskifte for å beholde hjemmet. Måneder senere krevde Skatteetaten 800 000 kr i ubetalt moms, og en leverandør 500 000 kr. Siden Eva satt i uskifte, var hun nå personlig ansvarlig og måtte selge huset. Hadde hun brukt proklama, ville hun fått oversikten FØR fellen klappet igjen."}],
        "vanlige_feil": ["Krysse av for uskifte uten å sjekke avdødes gjeld i Gjeldsregisteret", "Tro at boliglånet er den eneste gjelden (ubetalt skatt og skjulte kredittkort dukker ofte opp)", "Vente med proklama til ETTER man har sendt skjemaet til tingretten"],
        "hva_bor_du_html": "<p>Har dere ryddig økonomi og full oversikt? Da er uskifte trygt. Er du det minste i tvil? Be tingretten om proklama FØR du velger uskifte. Det koster litt, men tar bare seks uker — og da vet du nøyaktig hva du påtar deg.</p>",
        "dumme_sporsmal": [
            {"q": "Faller studielånet til avdøde over på meg?", "a": "Nei. Gjeld til Lånekassen slettes automatisk ved dødsfall. Det er den eneste gjelden som fordamper av seg selv."},
            {"q": "Kan jeg levere tilbake uskifteattesten når jeg ser at det er for mye gjeld?", "a": "Nei, bordet fanger. Gjør undersøkelsene med proklama FØR du velger uskifte."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "14", "tittel": "Retten til uskifte", "available": True}, {"lov": "arveloven", "paragraf": "21", "tittel": "Hvilke eiendeler inngår i uskifteboet", "available": True}],
    },
    {
        "number": "21",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Hvilke nye eiendeler går inn i uskifteboet?",
        "kategori": "arv",
        "description": "Hva skjer hvis du vinner i Lotto eller arver egne foreldre mens du sitter i uskifte? Verdiene går inn i potten og skal deles med ektefellens barn — med mindre du bruker tre-måneders-regelen.",
        "kort_svar": "Alt du eier og alt du skaffer deg mens du sitter i uskiftet bo, glir inn i fellespotten som barna til avdøde skal del av. Unntaket er arv og livsforsikringer — de kan holdes utenfor hvis du krever skifte innen tre måneder.",
        "paragraftekst": "Alt som den lengstlevende ektefellen blir eier av, går inn i uskifteformuen. Får den lengstlevende gave, arv eller utbetaling etter en livsforsikring, går dette ikke inn i uskifteformuen hvis det blir krevd skifte innen tre måneder etter at det ble mottatt.",
        "hva_betyr_html": """<p>Uskiftet er som en åpen sekk — alt du sparer av lønn og all verdiøkning på boligen legges i sekken. Barna til avdøde vil til slutt ha en del av sparepengene DU setter av fra din lønn etter at partneren din døde.</p>
<p><strong>Unntaket:</strong> Arv, store gaver og livsforsikringer kan holdes utenfor — MEN du må kreve at uskifteboet skiftes innen tre måneder. Gjør du ikke det, faller millionene ned i sekken og deles med svigerfamilien.</p>
<p>En lottogevinst er derimot ingen av disse kategoriene — den glir rett inn i uskiftesekken.</p>""",
        "eksempler": [{"navn": "Ingrid", "tekst": "Ingrid sitter i uskifte. Tolv år etter arver hun 4 millioner fra sin mor. Ektemannens to særkullsbarn venter. For å holde morens arv unna, kontakter Ingrid tingretten innen tre måneder og krever at uskifteboet skiftes. De 4 millionene fra moren er ikke en del av dette oppgjøret, og Ingrid beholder dem 100 %."}],
        "vanlige_feil": ["Tro at penger man tjener holdes adskilt fra avdødes barn — nei, alt går i potten", "Glemme tre-måneders-fristen for å skifte boet når man mottar en stor arv"],
        "hva_bor_du_html": "<p>Står du foran en stor arv fra egne foreldre mens du sitter i uskifte? Regn på saken! Er det særkullsbarn som venter, kan det lønne seg å kreve skifte av uskifteboet FØR foreldrene dine dør.</p>",
        "dumme_sporsmal": [
            {"q": "Hva hvis foreldrene mine testamenterte at arven skal være mitt særeie?", "a": "Da er du reddet! Arv med særeievilkår fra testator går ikke inn i uskiftepotten. Du trenger ikke skifte boet innen tre måneder."},
            {"q": "Vant 2 millioner i Lotto. Kan jeg bruke 3-måneders-regelen?", "a": "Nei. Paragrafen lister spesifikt opp gave, arv og livsforsikring. En lottogevinst er ingen av delene — den går rett i uskiftesekken."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "22", "tittel": "Råderetten over uskifteformuen", "available": True}, {"lov": "arveloven", "paragraf": "29", "tittel": "Skifte av uskifteformuen", "available": True}],
    },
    {
        "number": "22",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Hva kan du gjøre med pengene i et uskiftet bo?",
        "kategori": "arv",
        "description": "Sitter du i uskiftet bo? Du styrer som en eier. Du kan selge huset, reise på luksusferie og bruke pengene. Men loven har noen grenser du må vite om.",
        "kort_svar": "Når du sitter i uskiftet bo, har du full råderett. Du opptrer som en vanlig eier og kan fritt bruke penger, selge eiendom og reise. Det eneste du ikke kan, er å gi bort urimelig store gaver eller favorisere ett barn over et annet uten samtykke.",
        "paragraftekst": "Den lengstlevende ektefellen rår i levende live som en eier over alt som hører til uskifteformuen, med de unntakene som følger av lov, testament eller avtale.",
        "hva_betyr_html": """<p>Mange arvinger tror feilaktig at et uskiftet bo er en «fryst sparekonto». Det er helt feil. Loven gir deg nesten all makt som eier: Du kan selge enebolingen, bruke 100 000 kr på en bobil, eller reise til Karibia. Du har lov til å bruke opp pengene gjennom normal livsførsel.</p>
<p>Unntakene: Du kan ikke gi bort store eiendommer (§ 23 om gaver), og du kan ikke gi arveforskudd til bare ett barn (§ 24).</p>
<p>I testament kan du rå over din andel av uskifteboet (typisk 50 %) — ikke over avdødes andel.</p>""",
        "eksempler": [{"navn": "Per", "tekst": "Per sitter i uskifte, huset er nedbetalt, og det er én million på kontoen. Barna mener han bør spare. Per kjøper bobil til 800 000 kr og betaler for en jordomseiling. Barna prøver å stoppe ham — og taper. Per rår som eier i levende live, og forbruk er fullt lovlig."}],
        "vanlige_feil": ["Arvinger tror den gjenlevende må ha godkjenning for å selge familiehuset", "Gjenlevende tror de fritt kan gi bort hytta til favorittbarnet — salg og forbruk er lov, gaver er strengt regulert"],
        "hva_bor_du_html": "<p>Sitter du i uskifte? La ikke barna diktere pengene dine. Du har rett til god levestandard. Men forsøk ikke å «tømme» boet bevisst for å snyte særkullsbarn — grovt klanderverdig forbruk kan koste deg uskifteretten og utløse krav om vederlag (§ 30).</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg selge hytta for 500 000 kr når markedsverdien er 3 millioner?", "a": "Nei. Et slikt salg er et «gavesalg» — du gir bort 2,5 millioner. Å gi store gaver er ulovlig uten samtykke (§ 23). Å selge til markedspris derimot, er helt fritt."},
            {"q": "Eier jeg alt? Er det teknisk sett mine penger?", "a": "Du har eiers rådighet, men potten tilhører juridisk sett også den avdøde. Du er forvalter og eier på samme tid — du kan ikke testamentere bort den avdødes andel."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "23", "tittel": "Gaver fra uskifteboet", "available": True}, {"lov": "arveloven", "paragraf": "24", "tittel": "Arveforskudd fra uskifteboet", "available": True}, {"lov": "arveloven", "paragraf": "30", "tittel": "Krav på vederlag ved sløsing", "available": True}],
    },
    {
        "number": "23",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Kan du gi bort gaver fra et uskiftet bo?",
        "kategori": "arv",
        "description": "Sitter du i uskiftet bo, kan du ikke dele ut store gaver eller gi hytter på «billigsalg». Gaver som står i misforhold til formuen, er ulovlige og kan kreves tilbake.",
        "kort_svar": "Det er ulovlig å gi bort gaver som er uforholdsmessig store sett i forhold til hele formuen din. Dette gjelder også «gavesalg». Gjør du det uten samtykke, kan arvingene kreve gaven omstøtt — tilbakelevert til boet.",
        "paragraftekst": "Den lengstlevende ektefellen kan ikke uten samtykke fra arvingene gi gaver som står i misforhold til formuen i uskifteboet. Dette gjelder også gavesalg. Hvis den lengstlevende har gitt en gave og mottakeren forsto eller burde ha forstått at gaven var i strid med reglene, kan arvingene kreve gaven omstøtt. Kravet må reises ved søksmål innen ett år etter at arvingen fikk kunnskap om gaven.",
        "hva_betyr_html": """<p>Du kan fritt gi vanlige julegaver og bursdagsgaver. Grensen brytes når gaven «står i misforhold» til totaløkonomien. Domstolene sier typisk at gaver over 10–20 % av boets totale verdi er ulovlige.</p>
<p>Et «gavesalg» er like ulovlig: Å selge familiehytta til sønnen for 1 million når markedsverdien er 4 millioner, er det samme som en gave på 3 millioner.</p>
<p>Arvingene har en streng ett-årig frist for å saksøke — løper fra den dagen de fikk vite om gaven.</p>""",
        "eksempler": [{"navn": "Kari og hyttesalget", "tekst": "Kari sitter i uskifte med 5 millioner i totalformue. Hun overfører hytta (verdt 1 million) gratis til datteren Anne. Sønnen Lars mener dette (20 % av formuen) er uforholdsmessig. Siden Anne burde skjønt at det brøt reglene, stevner Lars henne ti måneder senere. Lars vinner — Anne må tilbakeføre hyttas verdi til boet."}],
        "vanlige_feil": ["Tro at regelen om 10–20 % er absolutt — domstolene gjør en helhetsvurdering", "Vente over ett år med å saksøke etter å ha funnet ut om gaven — fristen er knallhard"],
        "hva_bor_du_html": "<p>Ønsker du å overføre fast eiendom eller større summer til ett barn? Innhent alltid skriftlig samtykke fra ALLE andre arvinger FØR overføringen. Sier de ja på papiret, kan du gi hva du vil.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg saksøke moren min for å ha gitt gaven?", "a": "Nei. Paragrafen retter seg mot gavemottakeren. Det er barnet eller personen som mottok gaven som må saksøkes for å tilbakeføre verdien."},
            {"q": "Fikk svigerdatteren min en ulovlig gave? Hun forsto jo ikke reglene.", "a": "Loven sier at mottakeren «forsto eller burde ha forstått». Folk forventes å vite at noen sitter i uskifte og sjekke om gaven er for stor. Posisjonen som uskyldig er svært vanskelig å forsvare."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "22", "tittel": "Råderetten over uskifteformuen", "available": True}, {"lov": "arveloven", "paragraf": "24", "tittel": "Arveforskudd fra uskifteboet", "available": True}, {"lov": "arveloven", "paragraf": "25", "tittel": "Arvingenes rett til bevissikring", "available": True}],
    },
    {
        "number": "24",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Kan du gi forskudd på arv fra uskifteboet?",
        "kategori": "arv",
        "description": "Skal du hjelpe barna inn på boligmarkedet med penger fra uskifteboet? Du må gi alle barna like mye — eller ha skriftlig samtykke. Bryter du regelen, kan det bli svært dyrt.",
        "kort_svar": "Vil du gi forskudd på arv mens du sitter i uskiftet bo, må du gi alle arvingene en like stor andel. Ønsker du bare å gi til ett barn, må alle de andre samtykke skriftlig.",
        "paragraftekst": "Den lengstlevende ektefellen kan gi fullt eller delvis arveoppgjør av uskifteformuen til en arving bare hvis alle arvingene får en like stor del av sin arv eller har gitt samtykke. Har en arving fått arveoppgjør i strid med dette, kan hver av de andre kreve tilsvarende oppgjør. Nekter den lengstlevende, kan arvingene kreve at uskifteformuen skiftes.",
        "hva_betyr_html": """<p>Vil du hjelpe datteren inn på boligmarkedet med 1 million, men be sønnen vente? Det er ulovlig uten sønnens skriftlige samtykke.</p>
<p>Og konsekvensen er hard: Finner sønnen ut at datteren fikk 1 million, kan han kreve at HAN OG SÅ får 1 million utbetalt umiddelbart. Nekter du? Han kan tvinge frem et fullt skifte av uskifteboet — du mister retten til å sitte der.</p>
<p>Løsningen er en <strong>låneavtale</strong> i stedet for arveoppgjør: Sett opp et gjeldsbrev der barnet låner summen av deg. Da fjerner du ikke verdier fra uskifteformuen og trenger ikke samtykke fra de andre.</p>""",
        "eksempler": [{"navn": "Eva og bolighjelpen", "tekst": "Eva overfører 1,5 millioner til sønnen Marius uten å informere datteren Sofie. Sofie finner ut, og krever 1,5 millioner til seg selv. Eva har ikke råd uten å selge boligen. Sofie krever at hele uskifteboet skiftes. Eva mister retten til å sitte i uskifte og må flytte."}],
        "vanlige_feil": ["Hjelpe barn inn på boligmarkedet og tro at det er en lovlig «investering» — det er arveoppgjør", "Tro at en lapp om at «det trekkes fra i arven senere» er nok — søsknene kan fortsatt kreve sin sum nå"],
        "hva_bor_du_html": "<p>Vil du hjelpe bare ett barn med et stort beløp? Lag låneavtale med gjeldsbrev i stedet for å gi arv. Da fjerner du ikke verdier fra uskifteformuen og trenger ikke samtykke.</p>",
        "dumme_sporsmal": [
            {"q": "Gjelder dette lommepenger og småhjelp?", "a": "Nei. Å hjelpe med en strømregning på 5 000 kr rammes ikke. Det er store verdioverføringer (arveoppgjør) som krever likedeling eller samtykke."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "23", "tittel": "Gaver fra uskifteboet", "available": True}, {"lov": "arveloven", "paragraf": "28", "tittel": "Retten til å kreve skifte", "available": True}],
    },
    {
        "number": "25",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Arvingenes rett til å sikre bevis om uskifteboet",
        "kategori": "arv",
        "description": "Mistenker du at den som sitter i uskifte gir bort store gaver i skjul? Arveloven lar deg kreve bevissikring gjennom domstolen for å avsløre ulovligheter.",
        "kort_svar": "Har du grunn til å tro at den som sitter i uskiftet bo deler ut ulovlige gaver eller sniker unna verdier, kan du be tingretten om bevissikring — for eksempel utlevering av bankutskrifter.",
        "paragraftekst": "En arving kan begjære bevissikring utenfor rettssak etter reglene i tvisteloven kapittel 28 også i tilfeller der det er grunn til å tro at den lengstlevende ektefellen har rådet over uskifteformuen i strid med §§ 23 eller 24, eller på en måte som gir rett til å kreve skifte.",
        "hva_betyr_html": """<p>Som arving har du normalt ikke krav på innsyn i bankkontoene til den gjenlevende. Men har du sterke indikasjoner på ulovlig aktivitet, kan du gå til domstolen.</p>
<p>Fortell dommeren hva du mistenker og hvorfor. Finner dommeren mistanken reell, kan domstolen kreve at banken utleverer kontoutskrifter — uten at den gjenlevende kan nekte. Du får bevisene FØR du eventuelt saksøker noen.</p>
<p>Husk: Det holder ikke å være generelt nysgjerrig. Du må ha «grunn til å tro» — noe konkret, som en grunnbokutskrift som viser eierskifte til null kroner.</p>""",
        "eksempler": [{"navn": "Jonas", "tekst": "Jonas er særkullsbarn og ga stemoren samtykke til uskifte. To år etter ser Jonas på sosiale medier at stemorens datter plutselig har kjøpt en leilighet til fem millioner uten jobb. Jonas begjærer bevissikring. Tingretten pålegger banken å utlevere kontoutskrifter. Utskriftene viser en overføring på to millioner. Jonas har beviset han trenger."}],
        "vanlige_feil": ["Kreve bevissikring bare for å «sjekke hvordan det står til» — du trenger konkrete holdepunkter", "Tro at advokaten kan tvinge banken til å gi ut utskrifter — bare en dommer kan oppheve bankens taushetsplikt"],
        "hva_bor_du_html": "<p>Start alltid med en skriftlig henvendelse der du ber om forklaring. Får du avvisende svar og har konkrete bevis (som grunnbokutskrift), kontakt advokat for å utforme en begjæring om bevissikring.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg stoppe henne fra å bruke mer penger mens retten sjekker?", "a": "Bevissikring fryser ikke bankkontoene. Tror du hun vil tømme resten i panikk, kan du i tillegg begjære en «midlertidig forføyning» for å fryse kontoen."},
            {"q": "Hva hvis jeg tar feil?", "a": "Da kan du bli dømt til å betale motpartens saksomkostninger. Bevissikring er et kraftig verktøy som koster penger hvis du taper."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "23", "tittel": "Gaver fra uskifteboet", "available": True}, {"lov": "arveloven", "paragraf": "24", "tittel": "Arveforskudd fra uskifteboet", "available": True}, {"lov": "arveloven", "paragraf": "30", "tittel": "Krav på vederlag ved sløsing", "available": True}],
    },
    {
        "number": "26",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Hvem tar arv når et uskiftebo endelig gjøres opp?",
        "kategori": "arv",
        "description": "Hva skjer hvis et av barna dør mens faren sitter i uskiftet bo? Lær hvem som har rett på arven når uskiftet endelig skal avsluttes.",
        "kort_svar": "Du har bare rett på arv fra et uskiftet bo hvis du er i live den dagen boet faktisk gjøres opp. Dør du FØR uskifteboet er avsluttet, går din andel videre til dine egne arvinger.",
        "paragraftekst": "Arvingene etter den førstavdøde tar arv i et uskiftet bo bare hvis de lever når den lengstlevende ektefellen dør, når det skriftlig kreves offentlig skifte, når et privat skifte innledes, eller når uskifteformuen ellers skal skiftes.",
        "hva_betyr_html": """<p>Et uskifte kan vare i over 30 år. Loven fryser tidspunktet den dagen skiftet starter: De som lever da, er arvingene.</p>
<p>Dør et barn i mellomtiden, forsvinner ikke dets rett til arven. Barnets andel går rett ned til barnets egne barn (barnebarna dine). Barnebarna trer inn i forelderens sted og venter på at uskiftet avsluttes.</p>
<p>Er avdødes hele arvegangsklasse utdødd? Da glir arven ikke opp til fjern slekt på avdødes side — den tilhører den gjenlevendes formue.</p>""",
        "eksempler": [{"navn": "Kari og familien", "tekst": "Kari sitter i uskifte etter Per. Barna er Sara og Tom. Femten år etter dør Tom, gift med Anne og med to barn. Kari dør fem år etter. Toms andel av farsarven går rett ned til Toms to barn. Toms kone Anne får ingenting — arven følger blodlinjen."}],
        "vanlige_feil": ["Barn som prøver å testamentere bort sin forventede arv fra uskifteboet — arven følger arvelovens linjer ned til livsarvingene, ikke inn i barnets dødsbo"],
        "hva_bor_du_html": "<p>Er du barnebarn og forelderen din dør mens bestemor sitter i uskifte? Du har nå rykket opp som «direkte arving» til bestefars arv. Du må varsles hvis bestemor vil gjøre endringer i boet.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om hele slekten dør ut mens mor sitter i uskifte?", "a": "Da er «arvegangsklassen dødd ut» og fars arv glir over til mors egen formue. Alt går til mors arvinger, ikke til fjern slekt på fars side."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "14", "tittel": "Retten til uskifte", "available": True}, {"lov": "arveloven", "paragraf": "29", "tittel": "Skifte av uskifteformuen", "available": True}],
    },
    {
        "number": "27",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Nytt ekteskap eller ny samboer stopper uskiftet",
        "kategori": "arv",
        "description": "Skal du gifte deg på nytt? Da faller retten til uskiftet bo bort automatisk. Du må skifte boet først. Det samme gjelder hvis du får ny samboer i over to år.",
        "kort_svar": "Du kan ikke ta med deg den forrige ektefellens verdier inn i et nytt ekteskap. Gifter du deg på nytt, mister du automatisk retten til å sitte i uskiftet bo. Får du en ny samboer, kan arvingene kreve skifte etter to år.",
        "paragraftekst": "Retten til uskifte faller bort hvis den lengstlevende gifter seg. En arving kan kreve skifte av uskifteformuen hvis den lengstlevende har hatt samboer i minst to år eller har, har hatt eller venter barn med samboeren.",
        "hva_betyr_html": """<p><strong>Bryllup = automatisk stopp:</strong> Gifter du deg, faller uskifteretten bort i det sekundet du sier ja. Du kan ikke møte opp i kirken uten å ha bevist overfor Skatteetaten at skiftet er ryddet opp i FØR bryllupet.</p>
<p><strong>Ny samboer = betinget stopp:</strong> Etter to år har arvingene rett til å kreve arven sin. Venter dere barn sammen, faller to-årsfristen bort — de kan kreve skifte med én gang. Bryr ikke arvingene seg? Du kan bli boende med samboeren i ti år uten at noe skjer.</p>""",
        "eksempler": [{"navn": "Ingrid og den nye kjæresten", "tekst": "Ingrid sitter i uskifte. Etter tre år møter hun Petter og de planlegger bryllup. For å få prøvingsattest fra Skatteetaten, MÅ Ingrid ha signatur fra barna om at skiftet er gjort — eller at de aksepterer giftemålet. Barna vil ha farsarven. Ingrid tar opp lån og betaler dem ut FØR bryllupet."}],
        "vanlige_feil": ["Prøve å gifte seg i utlandet for å omgå systemet — ekteskapet kan ikke anerkjennes i Norge uten at skiftet er gjort", "Arvinger som glemmer å kreve skifte etter to år med samboer — retten til å kreve skifte ligger der til de bruker den"],
        "hva_bor_du_html": "<p>Planlegger du bryllup? Start planleggingen av skiftet tidlig. Er verdiene i huset, må du snakke med banken om refinansiering for å betale ut barna.</p>",
        "dumme_sporsmal": [
            {"q": "Stopper to-årsregelen hvis den nye samboeren min flytter ut i en måned?", "a": "Midlertidige avbrudd nullstiller ikke fristen. Det kreves et reelt og varig brudd. Endret adresse i Folkeregisteret er ofte det avgjørende beviset."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "28", "tittel": "Retten til å kreve skifte", "available": True}, {"lov": "arveloven", "paragraf": "29", "tittel": "Skifte av uskifteformuen", "available": True}],
    },
    {
        "number": "28",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Når kan du kreve at uskifteboet oppløses?",
        "kategori": "arv",
        "description": "Den gjenlevende kan avslutte uskiftet når som helst. Arvingene kan kreve det bare ved grovt misbruk — eller når et særkullsbarn fyller 18 år.",
        "kort_svar": "Den som sitter i uskifte, kan frivillig avslutte det når som helst. Som arving kan du tvinge gjennom skifte bare hvis midlene sløses bort grovt — eller som særkullsbarn når du fyller 18 år.",
        "paragraftekst": "Den lengstlevende ektefellen kan når som helst skifte uskifteformuen helt eller delvis med alle arvingene. En arving kan kreve skifte av uskifteformuen hvis den lengstlevende rår over den på en så klanderverdig måte at den blir vesentlig redusert eller står i fare for å bli det. Har vergen og statsforvalteren samtykket i uskifte på vegne av en livsarving, kan livsarvingen kreve skifte for seg selv når han eller hun er blitt myndig.",
        "hva_betyr_html": """<p>For deg som venter på arv: Du kan ikke tvinge skiftet bare fordi du trenger penger. Det kreves alvorlig misbruk — systematisk tapping, bevisst sløsing for å snyte arvingene, spillegalskap som truer kassen.</p>
<p>Et viktig unntak: Er du særkullsbarn som var mindreårig da forelderen døde, og Statsforvalteren samtykket til uskifte på dine vegne — den dagen du fyller 18 år, kan du kreve din arv utbetalt.</p>""",
        "eksempler": [{"navn": "Sara fyller 18", "tekst": "Saras mor dør når Sara er 15 år. Stefaren ønsker å bo i rekkehuset. Statsforvalteren godkjenner uskifte. Da Sara fyller 18 år, sender hun krav om sin del av arven etter mor. Stefaren tar opp lån, kjøper henne ut, og sitter deretter som eneeier."}],
        "vanlige_feil": ["Barn tror de kan tvinge forelder til å selge huset bare fordi de har dårlig råd — loven krever alvorlig misbruk"],
        "hva_bor_du_html": "<p>Er du arving og ser at midlene sløses bort? Skaff bevis (§ 25 om bevissikring) og kontakt tingretten umiddelbart for å kreve offentlig skifte — ikke vent til det er tomt.</p>",
        "dumme_sporsmal": [
            {"q": "Hva er «klanderverdig måte»?", "a": "Å kjøpe en dyr bil eller ta to cruise er sjelden nok. Klanderverdig betyr systematisk tapping, åpenbar sløsing utover egne ressurser (som å gamble på kreditt), eller å selge verdier langt under pris til venner."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "25", "tittel": "Bevissikring", "available": True}, {"lov": "arveloven", "paragraf": "27", "tittel": "Nytt ekteskap stopper uskiftet", "available": True}],
    },
    {
        "number": "29",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Hvordan fordeles pengene når uskifteboet skiftes?",
        "kategori": "arv",
        "description": "Når et uskifte endelig er over, skal potten deles. Hovedregelen er 50/50 mellom familiene. Her får du reglene for hvordan dere beregner skiftet i praksis.",
        "kort_svar": "Når lengstlevende ektefelle dør og uskiftet avsluttes, deles hele potten normalt likt: 50 % til den førstavdødes arvinger, 50 % til den lengstlevendes arvinger.",
        "paragraftekst": "Ved skifte etter den lengstlevende ektefellens død skal uskifteformuen deles likt mellom den førstavdødes arvinger og den lengstlevendes arvinger om ikke noe annet er bestemt.",
        "hva_betyr_html": """<p><strong>Hovedregelen (skifte ved død):</strong> Alt deles i to like store deler. 50 % er den førstavdødes arv, 50 % er den lengstlevendes arv. I kjernefamilier med bare felles barn er dette uten praktisk betydning. Men i blandede familier deler hvert «lag» bare sin halvpart.</p>
<p><strong>Skifte i levende live:</strong> Den gjenlevende tar ut sin ektefellearv (¼ av den avdødes halvdel, eller minstearv 4G) FØR resten fordeles til avdødes arvinger.</p>
<p>Særkullsbarn har krav på verdien den dagen boet faktisk skiftes — ikke verdien den dagen den første forelderen døde. All verdiøkning telles med.</p>""",
        "eksempler": [{"navn": "Mine og dine barn", "tekst": "Ola og Kari er gift uten felles barn — Ola har en sønn, Kari en datter. Ola dør i 2010 (hus verdt 2 mill). Sønnen samtykker til uskifte. Kari dør i 2026 med 6 millioner totalt. Skifte 50/50: Olas sønn får 3 millioner, Karis datter får 3 millioner. Sønnen tjente grovt på verdiøkning i 16 år."}],
        "vanlige_feil": ["Blande sammen skifte ved død og skifte i levende live (gjenlevende tar ektefellearv fra avdødes pott bare ved skifte i levende live)", "Glemme tidligere forskudd på arv — disse skal korrigeres for FØR kaken deles"],
        "hva_bor_du_html": "<p>Er familien en blanding av mine og dine barn, eller var det særeie? Kontakt advokat den dagen boet skal skiftes. Brøkregningen over to tiår er kompleks og fører ofte til stygge krangler.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om mor har tapt penger på børsen i de 10 årene hun satt i uskifte?", "a": "Da er potten mindre. Risikoen for verditap — og sjansen for verdistigning — følger uskiftet. Arvingene deler den virkelige nettoverdien den dagen det skiftes."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "14", "tittel": "Retten til uskifte", "available": True}, {"lov": "arveloven", "paragraf": "8", "tittel": "Ektefellens arverett med barn", "available": True}],
    },
    {
        "number": "30",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Krav på erstatning hvis uskifteformuen ble sløst bort",
        "kategori": "arv",
        "description": "Har den som sitter i uskifte bevisst tømt boet og gjemt pengene i særeie? Loven lar deg kreve vederlag (erstatning) under arveoppgjøret.",
        "kort_svar": "Har den gjenlevende ektefellen grovt sløst bort uskifteformuen, eller brukt fellespenger for å fylle sin private særeieformue, kan arvingene kreve kompensasjon (vederlag) under skiftet.",
        "paragraftekst": "Er uskifteformuen vesentlig redusert fordi den lengstlevende ektefellen har vanskjøttet sin økonomi, misbrukt sin rett til å rå over uskifteformuen eller handlet utilbørlig, kan den førstavdødes arvinger kreve vederlag av uskifteformuen eller, der den ikke strekker til, av den lengstlevendes formue utenfor uskifteformuen.",
        "hva_betyr_html": """<p>To vanlige former for misbruk som utløser vederlagskrav:</p>
<p><strong>1. Den ville sløsingen.</strong> Systematisk rasering av økonomien — penger gjemt unna, store ulovlige overføringer. Er arven «vesentlig redusert» (typisk 10–20 %), har du krav på erstatning.</p>
<p><strong>2. Den kalde berikelsen.</strong> Stemor tar fellespenger fra uskiftet og bruker dem til å pusse opp sin private særeie-gård. Fellespotten tømmes, hennes private verdier stiger. Loven: Disse pengene skal kompenseres til deg under skiftet.</p>
<p>Er det tomt for penger under skiftet? Kravet kan da rettes mot den lengstlevendes egne verdier utenfor uskifteformuen.</p>""",
        "eksempler": [{"navn": "Stemors oppussing", "tekst": "Petters far dør, stemoren sitter i uskifte. Over ti år tar hun 3 millioner i lån med pant i fellesrekkehuset og bruker pengene på å restaurere sin særeie-gård. Petter krever vederlag etter § 30. Skifteretten fastslår at stemoren ulovlig overførte verdier. Penger hentes fra gården og legges tilbake i fellespotten."}],
        "vanlige_feil": ["Kreve erstatning fordi mor «reiste tre ganger til Spania» — vanlig forbruk gir ingen rett til vederlag uansett hvor urettferdig det føles"],
        "hva_bor_du_html": "<p>Ser du at midler pumpes inn i den gjenlevendes personlige særeie? Reager umiddelbart — krev bevissikring (§ 25), stopp uskiftet (§ 28), og reis krav om vederlag under selve oppgjøret.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg kreve penger direkte fra hennes arvinger?", "a": "Kravet rettes mot verdier i boet under selve skiftet. Har hennes arvinger allerede fått pengene og saken er avsluttet, er det ekstremt vanskelig å kreve dem tilbake."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "22", "tittel": "Råderetten over uskifteformuen", "available": True}, {"lov": "arveloven", "paragraf": "28", "tittel": "Retten til å kreve skifte", "available": True}],
    },
    {
        "number": "31",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Hva hører med i uskifteboet under skiftet?",
        "kategori": "arv",
        "description": "Skal du i gang med å fordele arven fra et uskiftet bo? Loven slår fast at alt den lengstlevende eier på selve skiftedagen, skal inn i oppgjøret.",
        "kort_svar": "Når et uskiftebo gjøres opp, regnes absolutt alt den lengstlevende ektefellen eier på skiftedagen som en del av uskifteformuen — med mindre det kan bevises at det er formelt særeie.",
        "paragraftekst": "Alt som den lengstlevende ektefellen eier, hører med til uskifteformuen når det skal skiftes, hvis ikke noe annet blir sannsynliggjort.",
        "hva_betyr_html": """<p>Alt deles i én krukke. Absolutt hvert eneste eiendel og krone den lengstlevende eier den dagen boet skiftes, inngår i potten — inkludert biler kjøpt for 10 år siden, og all verdiøkning på boligen.</p>
<p>Eneste unntak: Noen kan «sannsynliggjøre» at en verdi ikke hører hjemme der — for eksempel et formelt tinglyst særeie, eller arv mottatt med klare særeievilkår på en adskilt konto.</p>
<p>Blander du særeiepenger inn på regningskontoen i ti år? Da er de umulige å spore, og mistes til fellespotten.</p>""",
        "eksempler": [{"navn": "Båten", "tekst": "Per sitter i uskifte etter Anne. Per dør. Pers særkullsbarn påstår at seilbåten Per kjøpte for fem år siden er hans private. § 31 stopper krangelen: Siden alt Per eide på dødsdagen er uskifteformue, går båten inn i potten og deles 50/50 med Annes arvinger."}],
        "vanlige_feil": ["Tro at verdistigningen på boligen holdes utenfor — den inngår i potten", "Blande private særeiepenger inn i boets felleskonto — da er de umulige å spore og mistes til fellespotten"],
        "hva_bor_du_html": "<p>Sitter du i uskifte og mottar penger du har rett til å holde for deg selv? Opprett en EGEN bankkonto. Ikke bland disse pengene med regningskontoen din. Adskillelse + dokumentasjon er det eneste som hjelper.</p>",
        "dumme_sporsmal": [
            {"q": "Skal jeg betale skatt av det formuen har økt med?", "a": "Nei, arv er skattefri i Norge. Arvingene skattlegges ikke av verdistigningen i oppgjøret."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "21", "tittel": "Hvilke eiendeler inngår", "available": True}, {"lov": "arveloven", "paragraf": "29", "tittel": "Skifte av uskifteformuen", "available": True}],
    },
    {
        "number": "32",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Samboeres rett til å sitte i uskifte",
        "kategori": "arv",
        "description": "Samboere kan også sitte i uskiftet bo, men reglene er strammere enn for gifte. Du får bare beholde hus, bil og hytte — ikke bankkontoer eller andre eiendeler.",
        "kort_svar": "Som samboer har du rett til uskifte bare hvis dere har felles barn. Og selv da er det begrenset: Du får beholde felles bolig, innbo, bil og fritidsbolig — ikke bankkontoer, aksjer eller andre eiendeler.",
        "paragraftekst": "Den som var samboer med arvelateren ved dødsfallet og har, har hatt eller venter barn med arvelateren, har overfor arvelaterens andre arvinger etter loven rett til å overta følgende uskiftet: a. felles bolig og innbo, b. bil og fritidsbolig med innbo som tjente til felles bruk. Samboeren har rett til uskifte med arvelaterens særskilte livsarving bare hvis denne arvingen samtykker.",
        "hva_betyr_html": """<p>Samboere og gifte er svært forskjellige i uskiftelovgivningen. For det første: Ingen felles barn? Da har du null uskifterett uansett antall år sammen.</p>
<p>For det andre: Har dere felles barn er «menyen» begrenset — bare felles bolig + innbo, felles familiebil, felles hytte. De tre millionene mannen hadde i banken? Aksjene? Næringseiendommen? Alt dette MÅ gjøres opp og fordeles til barna med en gang.</p>
<p>Vil du som samboer få sitte i uskifte med bankkontoer og aksjer? Da må partneren ha skrevet dette i testament, eller barna må samtykke.</p>""",
        "eksempler": [{"navn": "Sofie og Lars", "tekst": "Sofie og Lars har to felles barn, men Lars har én sønn fra før. Særkullsbarnet nekter samtykke. Sofie mister all uskifterett overfor ham og må kjøpe ham ut. Overfor de to felles barna får Sofie sitte i uskifte med hus og hytte — men de felles barna skal ha Lars' sparepenger i banken straks (samboeruskifte gjelder ikke bankkontoer uten testament)."}],
        "vanlige_feil": ["Tro at samboere uten barn kan bruke testament til å få uskifte overfor avdødes familie — loven tillater ikke dette", "Tro at «innbo» inkluderer store bankinnskudd eller verdipapirer"],
        "hva_bor_du_html": "<p>Uskifte for samboere er komplisert. Opprett i stedet et grundig gjensidig testament, og vurder livsforsikring der dere begunstiger hverandre — slik at den gjenlevende har råd til å kjøpe ut barna.</p>",
        "dumme_sporsmal": [
            {"q": "Jeg eide 50 % av huset fra før. Påvirker uskiftet dette?", "a": "Nei, du eier fremdeles dine egne 50 %. Uskiftet handler bare om at du utsetter arveoppgjøret av den halvparten avdøde eide."},
            {"q": "Må jeg søke om dette, eller skjer det av seg selv?", "a": "Ingenting skjer av seg selv. Du må sende «Melding om uskiftet bo for samboere» til tingretten innen 60 dager (§ 34)."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "12", "tittel": "Arverett for samboere med felles barn", "available": True}, {"lov": "arveloven", "paragraf": "35", "tittel": "Samboere arver avdødes gjeld", "available": True}],
    },
    {
        "number": "33",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Kan partneren nekte deg uskifte med et testament?",
        "kategori": "arv",
        "description": "Samboeren din kan ta fra deg retten til å sitte i uskiftet bo ved å skrive et testament. Men du må ha fått vite om det mens partneren levde.",
        "kort_svar": "Samboeren din kan skrive et testament som bestemmer at du ikke får sitte i uskiftet bo. For at dette skal være gyldig, må du ha fått vite om testamentet FØR samboeren din døde.",
        "paragraftekst": "En samboers rett til uskifte etter dette kapitlet kan begrenses ved testament bare hvis han eller hun har fått kunnskap om testamentet før arvelaterens død. Vilkåret om at samboeren må ha fått kunnskap om testamentet, gjelder ikke hvis det var umulig eller urimelig vanskelig å varsle samboeren om testamentet.",
        "hva_betyr_html": """<p>Akkurat som for ektefeller (§ 17): Hemmelige testamenter som plutselig dras frem er ugyldig på dette punktet. Du må ha hatt kunnskap om det mens partneren levde.</p>
<p>Testamentet fratar deg uskifteretten, men ikke selve minstearven på 4G — du har fremdeles krav på din arv etter § 12, med mindre du også ble varslet spesifikt om at dette ble fjernet.</p>
<p>Testamentet fratar deg uskifteretten for avdødes andel av boet — men din egen 50 % eierandel er uberørt.</p>""",
        "eksempler": [{"navn": "Lars og Ingrid", "tekst": "Lars er syk og ønsker at alle tre barna skal få arven sin straks. Han skriver testament: Ingrid skal ikke ha uskifte. Han tar med en kopi hjem og gir den til Ingrid. Hun er varslet. Når Lars dør, kan Ingrid ikke kreve uskifte. Huset selges eller hun kjøper ut barna."}],
        "vanlige_feil": ["Opprette testament hos advokat og la det ligge i safe uten å fortelle partneren — ugyldig for uskifteretten", "Tro at samboeren må samtykke — hun trenger bare å vite om det"],
        "hva_bor_du_html": "<p>Vil du nekte samboeren uskifte? Be samboeren signere en kopi med «Lest og gjort kjent med innholdet», dato og signatur. Det betyr ikke at de godkjenner det — bare at de har sett det.</p>",
        "dumme_sporsmal": [
            {"q": "Faller eierandelen min i huset bort?", "a": "Nei. Testamentet kan bare nekte deg å sitte i uskifte med avdødes andel. Du eier fremdeles dine egne 50 %."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "32", "tittel": "Samboeres rett til uskifte", "available": True}, {"lov": "arveloven", "paragraf": "17", "tittel": "Tilsvarende regel for ektefeller", "available": True}],
    },
    {
        "number": "34",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Frist for å kreve uskifte som samboer — 60 dager",
        "kategori": "arv",
        "description": "Skal du beholde felles bolig etter at samboeren din døde? Du har en krystallklar frist. Du må melde fra til tingretten innen 60 dager etter dødsfallet.",
        "kort_svar": "For å bruke retten til uskiftet bo som samboer, må du gi skriftlig melding til tingretten senest 60 dager etter at samboeren din døde.",
        "paragraftekst": "En samboer som vil gjøre bruk av retten til uskifte, skal innen 60 dager etter dødsfallet sende melding til tingretten etter reglene i § 96.",
        "hva_betyr_html": """<p>Ingenting skjer av seg selv. Du har nøyaktig 60 dager fra dødsdagen til å bestemme deg og sende skjema til tingretten.</p>
<p>Uten meldingen kan tingretten starte et offentlig skifte — en bostyrer tar over styringen av huset, noe som koster titusenvis i gebyrer.</p>
<p>Skjemaet heter «Melding om uskiftet bo for samboere» og finnes på domstol.no. Det er gratis å sende inn.</p>""",
        "eksempler": [{"navn": "Tom og fristen", "tekst": "Tom ønsker å beholde huset etter avdød samboer. Da det har gått 75 dager, oppdager han at fristen var 60 dager. Han ringer tingretten. Siden ingen arvinger ennå har krevd skifte, godtar tingretten papirene — men Tom tok en stor risiko."}],
        "vanlige_feil": ["Legge saken i skuffen og håpe det ordner seg automatisk", "Glemme å legge ved samtykke fra Statsforvalteren hvis avdøde hadde mindreårige barn"],
        "hva_bor_du_html": "<p>Prioriter papirarbeidet i ukene etter begravelsen. Last ned skjemaet, lag en grov verdioversikt, og sjekk om det er særkullsbarn som må samtykke. Trenger du mer tid, kontakt tingretten og be formelt om forlenget frist.</p>",
        "dumme_sporsmal": [
            {"q": "Teller fristen fra dødsdagen eller fra begravelsen?", "a": "Fristen begynner å tikke nøyaktig på dødsdatoen, uavhengig av når begravelsen holdes."},
            {"q": "Hva koster det å sende inn meldingen?", "a": "Det er gratis. Domstolen krever ikke rettsgebyr for en vanlig melding om uskiftet bo."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "32", "tittel": "Samboeres rett til uskifte", "available": True}, {"lov": "arveloven", "paragraf": "35", "tittel": "Du overtar avdødes gjeld", "available": True}],
    },
    {
        "number": "35",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Samboere overtar avdødes gjeld i uskifteboet",
        "kategori": "arv",
        "description": "Krysser du av for samboer-uskifte? Du blir personlig ansvarlig for all gjeld avdøde hadde. Sjekk alltid gjelden med proklama FØR du sier ja.",
        "kort_svar": "Når du som samboer velger uskifte, overtar du fullt personlig ansvar for all gjelden til avdøde samboer. Bruk proklama for å avdekke skjult gjeld FØR du signerer papirene.",
        "paragraftekst": "Ved å overta boet uskiftet blir samboeren ansvarlig for arvelaterens forpliktelser. Samboeren kan utstede proklama etter §§ 100 til 103.",
        "hva_betyr_html": """<p>Akkurat som for ektefeller (§ 20): Uskifte betyr du overtar alt — pluss og minus. All gjeld avdøde hadde blir din personlige gjeld.</p>
<p>Proklama: Offisiell annonse i Norsk Lysingsblad. Kreditorer har seks uker på seg. Melder de seg ikke — slettes gjelden. Da vet du hva du påtar deg FØR du signerer.</p>
<p>Er gjelden større enn verdiene? Si nei til uskifte — boet er insolvent og du skal ikke ta over ansvaret personlig.</p>""",
        "eksempler": [{"navn": "Anna og de ukjente kredittkortene", "tekst": "Annas samboer Morten dør. Hun velger uskifte uten proklama. To millioner i egenkapital — trygt, tror hun. Tre måneder etter dumper krav fra inkassoselskaper: Morten hadde 1,5 millioner i skjulte forbrukslån. Anna er nå personlig ansvarlig. Huset selges for å betale gjelden."}],
        "vanlige_feil": ["Be om uskifteattest på dag 1 uten å sjekke gjeld — spesielt farlig hvis avdøde drev eget firma"],
        "hva_bor_du_html": "<p>Sjekk gjeldsregisteret, se siste skattemelding, og vurder proklama hvis du har den minste tvil. Er gjelden større enn verdiene? Si nei til uskifte.</p>",
        "dumme_sporsmal": [
            {"q": "Forsvinner studielånet hans?", "a": "Studielån hos Lånekassen slettes ved død. Det er den eneste trygge typen gjeld."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "32", "tittel": "Samboeres rett til uskifte", "available": True}, {"lov": "arveloven", "paragraf": "20", "tittel": "Tilsvarende for ektefeller", "available": True}],
    },
    {
        "number": "36",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Hvilke nye verdier inngår i et samboer-uskifte?",
        "kategori": "arv",
        "description": "For ektefeller går alt inn i uskiftepotten. For samboere er det annerledes: Bare eiendeler som hører naturlig sammen med boet, deles med avdødes barn.",
        "kort_svar": "For samboere i uskifte holdes din private økonomi adskilt fra boet. Bare ting du kjøper som «hører naturlig sammen» med det du overtok — som et nytt tak på huset — inngår i potten barna skal dele.",
        "paragraftekst": "Alt samboeren er eller blir eier av som hører naturlig sammen med de eiendelene han eller hun har overtatt uskiftet, går inn i uskifteformuen. § 21 annet ledd gjelder tilsvarende.",
        "hva_betyr_html": """<p>Her er den store fordelen samboere har over ektefeller i uskifte: Dine egne bankkontoer og sparepenger er bare dine. Avdødes barn har ingen krav på pengene du tjener etter dødsfallet.</p>
<p>Men verdier som «hører naturlig sammen» med det du overtok, faller inn: Bygger du garasje på felleshuset, hører garasjen til uskifteboet. Kjøper du ny bil som erstatter den gamle fellesbilen, inngår den nye i boet.</p>""",
        "eksempler": [{"navn": "Eva og den nye bilen", "tekst": "Eva sitter i samboeruskifte med huset og en gammel stasjonsvogn. Bilen kollapser. Eva kjøper ny elbil — 50 000 kr vrakpant + 450 000 kr egne sparepenger. Siden bilen erstatter familiens kjøretøy, hører den «naturlig sammen» med uskifteboet. Avdødes barn kan kreve sin andel av elbilens verdi ved skiftet."}],
        "vanlige_feil": ["Blande egne penger inn i huset uten å forstå at verdiøkningen deles med avdødes barn", "Tro at ALL sparing i uskifteperioden tilhører stebarna — nei, bare verdiene innenfor det avgrensede boet"],
        "hva_bor_du_html": "<p>Planlegger du store påbygg på huset? Vurder om du heller vil skifte boet med barna FØR du bygger — da eier du huset 100 % selv og all verdiøkning tilfaller deg alene.</p>",
        "dumme_sporsmal": [
            {"q": "Jeg har kjøpt meg en ny båt. Går den inn i potten?", "a": "Bare hvis du overtok en felles båt i uskiftet og den nye erstatter den. Var det ingen båt i boet fra før, er båten din privat."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "32", "tittel": "Hva man overtar som samboer", "available": True}],
    },
    {
        "number": "37",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Samboerens rett til å bruke og gi bort uskiftemidler",
        "kategori": "arv",
        "description": "Samboer i uskifte? Du råder over huset og bilen som en eier og kan selge. Men du kan ikke gi store gaver uten samtykke fra arvingene.",
        "kort_svar": "Som samboer i uskifte bestemmer du fullt ut over huset, innboet og bilen. Du kan selge og flytte. Men du kan ikke gi store gaver, og du kan bare testamentere over din egen andel av verdiene.",
        "paragraftekst": "Den lengstlevende samboeren rår i levende live som en eier over alt som hører til uskifteformuen. For adgangen til å gi gaver og arveoppgjør av uskifteformuen gjelder §§ 23 og 24 tilsvarende. Arvingene kan begjære bevissikring utenfor rettssak etter reglene i § 25.",
        "hva_betyr_html": """<p>Samme prinsipp som for ektefeller (§ 22): Du er eier i levende live. Vil du selge fellesboligen og kjøpe seniorleilighet? Fullt lovlig.</p>
<p>Grensene er de samme: Store gaver uten samtykke er ulovlig (§ 23). Arveforskudd til bare ett barn krever at alle får like mye eller samtykker (§ 24).</p>
<p>I testament kan du bare disponere over din egen andel av uskifteboet — ikke over avdødes andel.</p>""",
        "eksempler": [{"navn": "Marius bytter hus", "tekst": "Marius satt i samboer-uskifte med fellesboligen (6 mill). Solgte og kjøpte seniorleilighet til 4 mill. Avdødes særkullsbarn krevde 2 mill mellomlegg straks. Marius trenger ikke gå med på det — han kan flytte overskuddet til høyrentekonto (som inngår i uskiftet) og fortsette å sitte i uskifte. Barna venter til han dør."}],
        "vanlige_feil": ["Samboere i uskifte tror de kan gi hytta som gave til ett av barna uten å spørre de andre"],
        "hva_bor_du_html": "<p>Vil du overføre fast eiendom til ett barn? Innhent alltid skriftlig samtykke fra ALLE andre arvinger FØR overføringen. Uten det risikerer du omstøtelsessøksmål.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg ta opp et nytt lån med pant i boligen?", "a": "Gråsone. Du rår som eier og kan pantsette. Men tar du opp lån for å finansiere forbruk, kan du krysse grensen for «klanderverdig» opptreden som gir arvingene rett til å oppløse uskiftet."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "23", "tittel": "Gaver fra uskifteboet", "available": True}, {"lov": "arveloven", "paragraf": "36", "tittel": "Hvilke verdier inngår", "available": True}],
    },
    {
        "number": "38",
        "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Når mister en samboer retten til uskifte?",
        "kategori": "arv",
        "description": "Fant du en ny livspartner? Gifter du deg, mister du uskifteretten straks. Får du ny samboer og bor sammen i to år, kan arvingene tvinge frem arveoppgjør.",
        "kort_svar": "En gjenlevende samboer mister uskifteretten ved nytt ekteskap. Arvingene kan også kreve skifte hvis du bor med en ny samboer i minst to år, eller dere venter felles barn.",
        "paragraftekst": "Retten til uskifte faller bort hvis den lengstlevende samboeren gifter seg. En arving kan kreve skifte av uskifteformuen hvis den lengstlevende har hatt samboer i minst to år eller har, har hatt eller venter barn med den nye samboeren.",
        "hva_betyr_html": """<p><strong>Bryllup = automatisk stopp:</strong> Du kan ikke gifte deg uten å ha bevist overfor Skatteetaten at skiftet etter den forrige samboeren er ryddet opp i.</p>
<p><strong>Ny samboer = betinget stopp:</strong> Etter to år kan arvingene kreve oppgjør. Får dere barn, faller to-årsfristen bort — de kan kreve skifte umiddelbart. Bryr ikke arvingene seg, kan du bli boende i mange år til.</p>""",
        "eksempler": [{"navn": "Eva og den nye mannen", "tekst": "Eva sitter i samboeruskifte. Tre år etter treffer hun Nils og han flytter inn. Da Nils har bodd der over to år, sender Siris (særkullsbarnet) krav om skifte. Eva må refinansiere huset og kjøpe ut Siris farsarv, eller selge."}],
        "vanlige_feil": ["Tro at man unngår regelen ved at den nye samboeren formelt har adresse et annet sted — bor dere faktisk sammen kan naboer vitne", "Arvinger som «glemmer» å kreve skifte — retten oppstår etter to år og består til de faktisk krever det"],
        "hva_bor_du_html": "<p>Planlegger du nytt ekteskap? Ha en plan for skiftet FØR du sier ja. Er det ny samboer som har bodd der to år? Vurder frivillig skifte for å løse situasjonen ryddig.</p>",
        "dumme_sporsmal": [
            {"q": "Barna er mine egne fellesbarn. Må jeg betale dem ut hvis jeg får samboer?", "a": "Ja. Egne fellesbarn har nøyaktig samme rett som særkullsbarn til å kreve skifte etter to år med ny samboer."},
            {"q": "Må huset selges?", "a": "Nei, huset må ikke selges. Skiftet krever bare at arvingene får verdien av sin andel utbetalt i penger. Kan du ta opp et lån, beholder du huset som eneeier."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "27", "tittel": "Tilsvarende for ektefeller", "available": True}, {"lov": "arveloven", "paragraf": "32", "tittel": "Samboeres rett til uskifte", "available": True}],
    },
]

PARAGRAPHS = PARAGRAPHS + _EXTRA_ARV
