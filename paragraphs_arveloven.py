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

_ARVELOVEN_39_62 = [
    {
        "number": "39", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Hvordan fordeles pengene når et samboer-uskifte avsluttes?",
        "kategori": "arv",
        "description": "Når uskiftet etter en samboer er over, deles ikke potten 50/50. Fordelingen skjer etter den nøyaktige eierbrøken dere hadde i boligen den dagen samboeren din døde.",
        "kort_svar": "Når uskiftet etter en samboer avsluttes, deles verdiene etter den nøyaktige eierbrøken dere to hadde i boligen og bilen den dagen samboeren din døde — ikke automatisk 50/50 slik som for gifte.",
        "paragraftekst": "Ved skifte etter den lengstlevende samboerens død, skal uskifteformuen deles mellom den førstavdødes arvinger og den lengstlevendes arvinger på grunnlag av verdiforholdet mellom samboernes eiendeler i uskifteboet da uskiftet ble etablert. Ved skifte mens den lengstlevende samboeren lever, har han eller hun krav på arv etter §§ 12 eller 13.",
        "hva_betyr_html": """<p>Siden samboere sjelden eier nøyaktig halvparten av alt, kan ikke loven bare klippe oppgjøret på midten. Dere må se tilbake til den dagen samboeren din døde og finne den nøyaktige eierbrøken fra det tidspunktet.</p>
<p>Eksempel: Mannen din eide 70 % av huset, du eide 30 %. Når du dør tjue år senere og huset er tredoblet i verdi, skal avdødes barn ha 70 % av salgssummen og dine egne barn 30 %. Brøken fra dødsdagen brukes på hele den nye verdien.</p>
<p>Skifter du mens du lever, tar du ut din faste eierandel (30 %) pluss din samboerminstearv (4G). Hans barn får resten av hans 70 %.</p>""",
        "eksempler": [{"navn": "Eva og den skjeve brøken", "tekst": "Eva eide 20 %, Tom 80 % av rekkehuset. Tom dør, Eva sitter i uskifte. Femten år etter selger Eva huset for 8 millioner. Evas andel: 1,6 mill (20 %). Toms pott: 6,4 mill (80 %). Fra Toms pott trekkes Evas samboerminstearv (4G ca 480 000 kr). Resten (5,92 mill) deles på Toms barn."}],
        "vanlige_feil": ["Barna tror morsarven er et fastfryst beløp fra dødsdagen — de har krav på brøken av nåverdien, inkludert all verdistigning", "Glemme å trekke fra felles gjeld før man finner fordelingsbrøken", "Tro at det deles 50/50 bare fordi man har bodd der lenge"],
        "hva_bor_du_html": "<p>Den dagen du fyller ut skjemaet for uskifte, bør du og barna skrive et felles dokument der dere låser brøken: «Avdødes andel av uskifteboet er beregnet til 70 %, gjenlevendes andel er 30 %.» Begge signerer. Legg det i safe. Da blir matematikken enkel om 20 år.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om jeg bygget garasje med egne penger mens jeg satt i uskifte?", "a": "Etter § 36 inngår alle forbedringer som hører naturlig sammen med boligen i uskifteformuen. Verdiøkningen fra garasjen ganges med den gamle brøken, og stebarna får sin andel av garasjens verdi."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "36", "tittel": "Hvilke eiendeler inngår", "available": True}, {"lov": "arveloven", "paragraf": "12", "tittel": "Samboers rett til 4G", "available": True}],
    },
    {
        "number": "40", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Testament og dødsdisposisjoner forklart",
        "kategori": "arv",
        "description": "Hva er egentlig et testament, og hvorfor er det ugyldig å gi bort huset på dødsleiet uten vitner? Lær forskjellen på gaver og dødsdisposisjoner.",
        "kort_svar": "Du bestemmer hvem som arver deg ved å skrive et testament. Gaver som kun får virkning etter din død (dødsdisposisjoner) er ugyldige med mindre de er skrevet i et formelt testament med to vitner.",
        "paragraftekst": "En arvelater kan innenfor lovens rammer bestemme i testament hvem som skal arve ham eller henne. En dødsdisposisjon må fremgå av et testament for å være gyldig. Som dødsdisposisjon regnes avtale og gave som verken hadde eller var ment å ha realitet for arvelateren i hans eller hennes levetid. Dette gjelder blant annet gave fra en giver som snart skal dø, og som vet det.",
        "hva_betyr_html": """<p>Loven skiller strengt mellom to ting:</p>
<p><strong>Gaver mens du lever (lovlig uten testament):</strong> Du kan gi bort hva du vil. Vil du gi hytta til naboen? I orden, så lenge gaven gjennomføres umiddelbart med reelle konsekvenser for deg.</p>
<p><strong>Dødsdisposisjoner (krever testament):</strong> En gave som i realiteten først skjer når du dør. To klassiske feller: (1) Du overfører skjøtet på huset til datteren, men bor der gratis og betaler alt vedlikehold til du dør — gaven har ingen realitet. (2) Du overfører to millioner fra sykesengen mens du vet du har dager igjen — krever testament med vitner.</p>""",
        "eksempler": [{"navn": "Per og den hemmelige kontoen", "tekst": "Per får vite at han har terminal kreft og logger inn i nettbanken og overfører 800 000 kr til en venninne. Etter Pers død krever barna tilbake. Fordi Per visste at han snart skulle dø, er overføringen en ugyldig dødsdisposisjon uten testament. Venninnen må betale alle pengene tilbake til boet."}],
        "vanlige_feil": ["Å prøve å snyte barna for pliktdelsarv ved å «gi bort» huset, men beholde all faktisk rådighet", "Skrive et vanlig brev om å gi bort verdier «når jeg faller fra» uten vitner og formkrav"],
        "hva_bor_du_html": "<p>Vil du gi en stor gave: Gjør det mens du er frisk. Sørg for at eiendeler faktisk overdras — tinglys skjøtet, la mottaker ta over forsikring og avgifter. Vil du at noen skal få noe etter du er borte: Oprett et formelt testament med vitner. Ingen snarveier.</p>",
        "dumme_sporsmal": [
            {"q": "Gjelder dette også livsforsikringer?", "a": "Nei. Å begunstige noen i en livsforsikring har eget unntak. Det ordner du direkte med forsikringsselskapet uten testament."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "41", "tittel": "Testasjonsevne", "available": True}, {"lov": "arveloven", "paragraf": "42", "tittel": "Formkrav til testament", "available": True}],
    },
    {
        "number": "41", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Hvem kan skrive et testament (testasjonsevne)?",
        "kategori": "arv",
        "description": "For å skrive et gyldig testament må du være 18 år og frisk nok til å forstå hva du gjør. Alvorlig demens eller rus gjør testamentet ugyldig.",
        "kort_svar": "Du må ha fylt 18 år og være ved dine fulle fem. Lider du av alvorlig demens, psykisk sykdom eller var sterkt ruset da du skrev under, er testamentet ugyldig.",
        "paragraftekst": "Den som har fylt 18 år, kan opprette testament. En testamentarisk disposisjon er ugyldig hvis testator på grunn av sinnslidelse, demens, rus eller annen psykisk funksjonsnedsettelse på testasjonstidspunktet ikke hadde evne til å forstå eller vurdere disposisjonen.",
        "hva_betyr_html": """<p><strong>Alderskravet:</strong> Under 18 år er testamentet direkte ugyldig.</p>
<p><strong>Mentalkravet:</strong> Du må forstå rekkevidden av det du gjør. Alvorlig demens, dype vrangforestillinger eller sterk medisinpåvirkning gjør testamentet ugyldig. Men loven krever at tilstanden var til stede akkurat da pennen traff papiret. Selv personer med mild demens kan ha «lyse øyeblikk» der de er fullt kompetente.</p>""",
        "eksempler": [{"navn": "Karis demens", "tekst": "Kari (82) er dypt dement og bor på skjermet avdeling. En fjern nevø kommer med et ferdigskrevet testament som gir hytta til ham. Kari signerer. Barna viser til legejournaler som dokumenterer at Kari på dette tidspunktet umulig kunne forstå verdien av hytta. Retten dømmer testamentet ugyldig — Kari manglet testasjonsevne."}],
        "vanlige_feil": ["Vente med å skrive testament til man er alvorlig syk — da angriper arvingene det raskt", "Tro at vergemål betyr at man ikke kan skrive testament — du kan ha verge og likevel ha testasjonsevne"],
        "hva_bor_du_html": "<p>Skal du skrive testament og begynner å bli eldre eller tar tunge medisiner? Skaff en legeerklæring SAMME DAG du signerer. Legen skriver at du er klar og orientert og i stand til å forstå innholdet. Stift erklæringen til testamentet — da fjerner du ethvert angrepsgrunnlag.</p>",
        "dumme_sporsmal": [
            {"q": "Kan noen under vergemål skrive testament?", "a": "Ja. Å ha verge tar ikke automatisk fra deg testasjonsevnen. En verge kan styre bankkontoene dine, men så lenge du forstår konsekvensene av testamentet ditt, kan du skrive det."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "42", "tittel": "Formkrav til testament", "available": True}, {"lov": "arveloven", "paragraf": "45", "tittel": "Ugyldighet ved utnyttelse", "available": True}],
    },
    {
        "number": "42", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Formkrav til testament: Slik gjør du det lovlig",
        "kategori": "arv",
        "description": "Et testament er null verdt hvis formkravene brytes. Det må være skriftlig, og to vitner må være til stede sammen med deg. Lær fellene du må unngå.",
        "kort_svar": "Testament må være skriftlig. Du signerer mens to vitner er til stede. Vitnene må vite det er et testament, ha fylt 18 år, og skrive under mens du er i rommet. Brytes dette er testamentet ugyldig.",
        "paragraftekst": "Et testament skal være skriftlig. Testator skal underskrive dokumentet. To vitner skal bevitne underskriften ved at testator skriver under dokumentet eller vedkjenner seg underskriften mens vitnene sammen eller hver for seg er til stede. Vitnene skal vite at dokumentet skal være et testament, og de skal skrive under dokumentet mens testator er til stede. Hvis reglene ikke er fulgt, er testamentet ugyldig.",
        "hva_betyr_html": """<p>Sjekkliste for gyldige formkrav:</p>
<p>1. <strong>Skriftlig.</strong> Video eller lydopptak holder ikke.<br>
2. <strong>Du signerer</strong> (eller vedkjenner deg signaturen).<br>
3. <strong>To vitner</strong> over 18 år, mentalt friske.<br>
4. <strong>Samtidighetskravet:</strong> Begge vitnene må se deg vedkjenne deg signaturen OG skrive under mens du er til stede.<br>
5. <strong>Vitnene vet at det er et testament</strong> — de trenger ikke lese innholdet.<br>
6. <strong>Dato</strong> er ikke strengt krav men livsfarlig å utelate.</p>""",
        "eksempler": [{"navn": "Olas ugyldige testament", "tekst": "Ola ber naboene Per og Kari signere — men Per signerer og kjører på jobb, deretter signerer Kari uten Per til stede. Vitnerekken var aldri «til stede sammen» ved vedkjennelsen. Testamentet er ugyldig. Pengene fordeles etter arveloven."}],
        "vanlige_feil": ["Vitnene signerer på hvert sitt sted og dokumentet sendes rundt — totalt ugyldig", "Vitnene signerer i en annen etasje mens testator er oppe — de MÅ signere mens testator er til stede", "Familien brukes som vitner (inhabilitet, se § 44)"],
        "hva_bor_du_html": "<p>Gjør det militært: (1) Skriv ut dokumentet. (2) Be to friske naboer (ingen som arver) inn i stuen SAMTIDIG. (3) Si: «Dette er mitt testament, jeg signerer nå» og skriv under. (4) Nabo 1 signerer mens du og nabo 2 ser på. (5) Nabo 2 signerer mens du og nabo 1 ser på. (6) Dato og sted på dokumentet.</p>",
        "dumme_sporsmal": [
            {"q": "Må vitnene lese hva som står der?", "a": "Nei. Du kan holde et blankt ark over teksten. De bekrefter bare at det ER du som signerer og at dokumentet er et testament."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "43", "tittel": "Vitnepåtegning", "available": True}, {"lov": "arveloven", "paragraf": "44", "tittel": "Hvem kan ikke være vitne", "available": True}],
    },
    {
        "number": "43", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Vitnepåtegning: Teksten som sikrer testamentet ditt",
        "kategori": "arv",
        "description": "Hva bør vitnene faktisk skrive på papiret? En god vitnepåtegning gjør testamentet nesten uangripelig i retten.",
        "kort_svar": "Vitnene bør skrive en kort tekst (påtegning) der de bekrefter at reglene ble fulgt, at du virket ved sans og samling, og at du handlet frivillig. Denne teksten anses som tilstrekkelig bevis med mindre noen har sterk dokumentasjon mot den.",
        "paragraftekst": "Testamentsvitnene bør i påtegning på testamentet opplyse om reglene i § 42 er fulgt, om testator har opprettet testamentet av fri vilje, og om testator var ved sans og samling. Påtegningen bør dateres, og vitnene bør oppgi sine fødselsdatoer. Påtegningen skal anses som bevis nok for de forhold den omfatter, om ikke særlige forhold gir grunn til å tvile på den.",
        "hva_betyr_html": """<p>Et testament uten påtegning er teknisk gyldig, men sårbart. Med påtegning legger du bevisbyrden på den som vil angripe testamentet.</p>
<p>Siste setning i paragrafen er nøkkelen: Påtegningen «skal anses som bevis nok». Det betyr at en dommer som regel stoler fullt på hva vitnene har skrevet — med mindre det finnes ekstremt sterke motstridende bevis.</p>
<p>Bruk denne malen:<br><em>«Vi bekrefter at [Navn] i dag, mens vi begge var til stede, undertegnet dette testamentet og erklærte at det er hans/hennes testament. Vi bekrefter at vi er over 18 år, ikke arver etter testamentet, og at testator handlet av fri vilje og var ved full sans og samling.»</em><br>Dato, navn, fødselsdato og adresse til begge vitner.</p>""",
        "eksempler": [{"navn": "Arveoppgjøret etter Lars", "tekst": "Lars gir samboeren sin alt. Barna påstår at Lars var ruset og at vitnene ikke var der samtidig. Fordi Lars brukte en god vitnepåtegning, krever dommeren at barna beviser påstandene. Uten solid motbevis stoler retten på påtegningen. Testamentet kjennes gyldig."}],
        "vanlige_feil": ["Vitnene bare signerer uten noen tekst — da er det fritt frem for angrep på testasjonsevne og prosess", "Uleselig skrift slik at man ikke vet hvem vitnene er"],
        "hva_bor_du_html": "<p>Bruk alltid en formell mal for vitnepåtegning. Sørg for at vitnene forstår hva de skriver under på. Legg det inn i testamentsmalen — det tar to minutter ekstra og gir dokumentet et juridisk panser.</p>",
        "dumme_sporsmal": [
            {"q": "Blir testamentet ugyldig hvis påtegningen mangler?", "a": "Nei. Paragrafen bruker «bør», ikke «skal». Mangler teksten, er testamentet fremdeles gyldig — men det blir mye enklere å angripe det i domstolen."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "42", "tittel": "Formkrav til testament", "available": True}, {"lov": "arveloven", "paragraf": "41", "tittel": "Testasjonsevne", "available": True}],
    },
    {
        "number": "44", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Inhabilitet: Hvem kan IKKE være vitne?",
        "kategori": "arv",
        "description": "La aldri familien signere som vitner! Hvis vitnet eller vitnets nærmeste familie arver i testamentet, slettes den gaven automatisk.",
        "kort_svar": "Du kan ikke velge hvem som helst som vitne. Hvis vitnet eller vitnets nære familie arver etter testamentet, blir den delen av testamentet ugyldig. Bruk aldri familie eller venner av mottakerne som vitner.",
        "paragraftekst": "En disposisjon i testamentet til fordel for et av testamentsvitnene er ugyldig. Det samme gjelder disposisjon til fordel for ektefellen eller samboeren, barn, foreldre, søsken, eller ektefellen til slektninger i rett linje. En disposisjon til fordel for noen vitnet er ansatt hos på testasjonstiden, er ugyldig.",
        "hva_betyr_html": """<p>Et vitne skal være hundre prosent nøytralt. Hvis vitnet har noe å vinne på testamentet, stoler ikke loven på dem.</p>
<p>Eksempel: Du testamenterer 1 million til Peter. Da kan INGEN av disse personene stå som vitne: Peter selv, kona til Peter, barna til Peter, foreldrene til Peter, søsknene til Peter, kona til Peters bror — eller ansatte i en organisasjon som mottar penger.</p>
<p>Konsekvens: Bare den spesifikke gaven til den inhabille personen slettes. Resten av testamentet gjelder fortsatt.</p>""",
        "eksempler": [{"navn": "Bror som vitne", "tekst": "Sara gir alt til niesen Thea. Theas far (Saras bror) signerer som vitne. Etter § 44 er Theas far inhabil som vitne for en disposisjon til fordel for sin datter. Gaven til Thea erklæres ugyldig. Pengene fordeles etter loven i stedet — og Thea får ingenting."}],
        "vanlige_feil": ["En kone ber sin egen mann signere som vitne på et testament der kona selv arver huset", "Bruker sønnen som vitne på et testament som gir hytta til datteren (sønn er bror til mottaker = inhabil)"],
        "hva_bor_du_html": "<p>Gjør det enkelt: Bruk aldri noen i familien, og aldri noen som kjenner mottakerne av arven. To gode naboer som overhodet ikke arver etter deg er ideelt. Eller to ansatte på advokatkontoret (så lenge advokaten ikke arver).</p>",
        "dumme_sporsmal": [
            {"q": "Jeg vil gi penger til vennen Lars. Kan en annen ukjent venn være vitne?", "a": "Ja. Å være venner skaper ikke inhabilitet. Det er formelle familiebånd som gjør folk inhabile."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "42", "tittel": "Formkrav til testament", "available": True}, {"lov": "arveloven", "paragraf": "45", "tittel": "Ugyldighet ved utnyttelse", "available": True}],
    },
    {
        "number": "45", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Arveløs på grunn av svik, tvang eller utnyttelse",
        "kategori": "arv",
        "description": "Ingen kan tvinge eller lure deg til å skrive testament. Blir du utnyttet på grunn av svakhet eller avhengighet, erklærer domstolen testamentet ugyldig.",
        "kort_svar": "Et testament er ugyldig hvis noen har brukt tvang, løgn eller utnyttet din svake helse eller avhengighet for å få deg til å gi dem penger. Testamentet er også ugyldig hvis det krever åpenbar ødeleggelse av verdier uten fornuftig formål.",
        "paragraftekst": "En testamentarisk disposisjon er ugyldig hvis den er fremkalt ved tvang, svik eller annen utilbørlig påvirkning, for eksempel ved misbruk av testators svakhetstilstand, avhengige stilling eller manglende dømmekraft. En testamentarisk disposisjon er også ugyldig hvis den går ut på bruk eller ødeleggelse som åpenbart ikke har noe fornuftig formål.",
        "hva_betyr_html": """<p>Paragraf 45 er arvelovens moralparagraf mot arvejegere. Fire røde flagg:</p>
<p><strong>1. Tvang</strong> — trusler om vold eller sanksjoner.<br>
<strong>2. Svik</strong> — løgner som påvirker hva du gir bort.<br>
<strong>3. Svakhetsmisbruk</strong> — den klassiske: hjemmehjelpen som bruker din totale avhengighet av henne til å presse frem et testament i sin favør.<br>
<strong>4. Ødeleggelse uten formål</strong> — du kan ikke testamentere at huset ditt skal brennes ned eller pengene brennes i peisen.</p>""",
        "eksempler": [{"navn": "Hjemmehjelpen og arven", "tekst": "Anders er 88 år og nesten blind. Den private hjemmehjelpen hans gråter og forteller at hun mister leiligheten. Hun kjører ham til advokat og guider hans skjelvende hånd. Alt testamenteres til henne. Etter Anders' død vinner nevøene saken etter § 45 — hjemmehjelpen misbrukte hans avhengige stilling. Testamentet strykes og hun får ingenting."}],
        "vanlige_feil": ["Barna tror «litt masete» oppførsel er nok — det skal mye til, utilbørlig betyr kritikkverdig over streken", "Glemme at bevisbyrden ligger hos dem som hevder tvang eller svik"],
        "hva_bor_du_html": "<p>Skal du tilgodese nabo, helsepersonell eller en ung samboer? Gjør det uten at disse personene er involvert i prosessen. Ikke la dem kjøre deg til advokaten. Gjør det klart at du opptrer på helt eget initiativ.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg skrive at min Rolex skal gravlegges sammen med meg?", "a": "Å bli gravlagt med personlige, mindre eiendeler er fint. Men å kreve at en stor økonomisk verdi bevisst destrueres kan rammes av forbudet om «ødeleggelse uten fornuftig formål»."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "41", "tittel": "Testasjonsevne", "available": True}, {"lov": "arveloven", "paragraf": "44", "tittel": "Inhabilitet", "available": True}],
    },
    {
        "number": "46", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Nødtestament: Når ulykken er ute",
        "kategori": "arv",
        "description": "Havner du i en livsfarlig ulykke og vil fordele arven din? Loven åpner for et kjapt nødtestament — men det slutter å gjelde hvis du overlever.",
        "kort_svar": "I en akutt nødsituasjon kan du lage et nødtestament: Enten muntlig til to vitner som er til stede, eller skriftlig alene hvis du ikke har vitner. Nødtestamentet slettes automatisk tre måneder etter at faren er over.",
        "paragraftekst": "Hvis farlig sykdom eller annet nødstilfelle hindrer noen fra å opprette testament etter § 42, kan han eller hun likevel opprette gyldig testament ved at det opprettes muntlig for to vitner som er til stede sammen. Hvis det er umulig for testator å opprette testament med vitner, kan testator likevel opprette gyldig testament med et dokument som han eller hun underskriver alene. Testament etter første eller annet ledd er ikke lenger gyldig når testator i tre måneder etter at testamentet ble opprettet, ikke har vært hindret i å følge reglene i § 42.",
        "hva_betyr_html": """<p><strong>Metode 1 — Muntlig for to vitner:</strong> Er det vitner i nærheten (to ambulansearbeidere, to klatrere i snøstormen), kan du rope det ut. Begge vitner MÅ høre deg samtidig. De bør skrive det ned så fort de kan.</p>
<p><strong>Metode 2 — Skriftlig alene:</strong> Ligger du alene i hytta med akutt hjerteproblem? Skriv det på en lapp og signer alene. Domstolen godkjenner det uten vitner i ekte nødsituasjoner.</p>
<p><strong>Tre-månedersregelen:</strong> Overlever du, slettes nødtestamentet automatisk tre måneder etter at faren er over. Du MÅ skrive et nytt, vanlig testament med vitner.</p>""",
        "eksempler": [{"navn": "Båten som sank", "tekst": "Marius er alene på fisketur og båten synker i storm. Han skriver i loggboken: «Samboeren Sara skal ha alt, ikke barna fra første ekteskap.» Han signerer og legger den i vanntett boks. Marius drukner. Barna protesterer — men retten godkjenner nødtestamentet etter § 46 andre ledd."}],
        "vanlige_feil": ["Bruke nødtestament bare fordi man har dårlig tid — det kreves reell nød", "Glemme å skrive lovlig testament innen tre måneder etter man kommer hjem fra sykehuset"],
        "hva_bor_du_html": "<p>Håp at du aldri trenger denne paragrafen. Løsningen er å skrive et vanlig testament i fredstid. Overlever du et drama der du lagde nødtestament: Ta frem kalenderen umiddelbart og skriv et nytt ordentlig testament med to vitner.</p>",
        "dumme_sporsmal": [
            {"q": "Er det greit om bare ett vitne hører meg?", "a": "Nei. For muntlige nødtestamenter kreves TO vitner til stede samtidig. Har du bare én, må du bruke metode 2 og skrive det ned på papir alene."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "42", "tittel": "Formkrav (den normale måten)", "available": True}, {"lov": "arveloven", "paragraf": "40", "tittel": "Dødsdisposisjoner", "available": True}],
    },
    {
        "number": "47", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Kan du ombestemme deg og trekke tilbake et testament?",
        "kategori": "arv",
        "description": "Angret deg på testamentet? Loven gir deg full frihet til å endre, rive i stykker eller skrive et helt nytt testament akkurat når du vil.",
        "kort_svar": "Du har alltid lov til å ombestemme deg. Et testament er ikke bindende for deg mens du lever. Du kan når som helst trekke det tilbake, endre det eller skrive et helt nytt, med mindre du bevisst har låst deg gjennom en arvepakt.",
        "paragraftekst": "En testator kan tilbakekalle eller endre testamentet sitt hvis ikke noe annet er bestemt i loven.",
        "hva_betyr_html": """<p>Et testament er ferskvare helt frem til ditt siste pust. Du eier fortsatt tingene dine, kan selge og bruke dem som du vil. Testamentet er bare et stykke papir som forteller hva som skal skje med det som tilfeldigvis er igjen den dagen du dør.</p>
<p>To unntak: (1) Du har mistet testasjonsevnen (blitt for dement til å forstå hva du gjør). (2) Du har opprettet en arvepakt (§ 49) der du frivillig har fraskrevet deg retten til å endre mening.</p>""",
        "eksempler": [{"navn": "Kari og de tre testamentene", "tekst": "Kari skriver testament til nevøen Lars. Blir uvenner med Lars og skriver nytt til Røde Kors. Lars sier «du lovet meg arven!». Lars har ingen sak — Kari har full rett til å endre testamentet så ofte hun vil. Senere river hun Røde Kors-testamentet uten å skrive nytt. Da gjelder arvelovens vanlige regler."}],
        "vanlige_feil": ["Barna tror foreldrene brøt loven ved å endre testamentet uten å informere dem — du har ingen plikt til å informere barna", "Tro at man ikke kan selge bilen man testamenterte bort — du kan selge med verdens beste samvittighet"],
        "hva_bor_du_html": "<p>Livet endrer seg. Gå gjennom testamentet ditt hvert femte år. Stemmer det med hva du ønsker? Er det nye barnebarn, ny samboer, brutt kontakt med noen? Ta grep og endre det.</p>",
        "dumme_sporsmal": [
            {"q": "Koster det penger å endre et testament?", "a": "Nei, ikke hvis du gjør det selv hjemme med to nye vitner. Staten krever ingen gebyrer for selve endringen."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "48", "tittel": "Formkrav ved tilbakekall", "available": True}, {"lov": "arveloven", "paragraf": "49", "tittel": "Arvepakt", "available": True}],
    },
    {
        "number": "48", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Hvordan sletter du et gammelt testament?",
        "kategori": "arv",
        "description": "Å krysse ut et navn med penn gjør det ikke gyldig endret. Du må enten ødelegge hele dokumentet fysisk, eller skrive et nytt med to vitner.",
        "kort_svar": "For å slette et testament: Enten ødelegge hele originalen fysisk (rive, brenne, makulere), eller skrive et helt nytt dokument med to vitner der du tilbakekaller det gamle. Å stryke over enkeltpunkter er ikke nok.",
        "paragraftekst": "Testator kan helt eller delvis tilbakekalle testamentet eller endre det ved å følge reglene i §§ 41 til 46. Hele testamentet kan dessuten tilbakekalles ved at det ødelegges eller overstrykes på en slik måte at det virker sannsynlig at det ikke lenger er ment å gjelde. Hele testamentet må i så fall ødelegges eller overstrykes. Et tilbakekall eller en endring som ikke oppfyller vilkårene, er ugyldig.",
        "hva_betyr_html": """<p>Mange lager rot i arveoppgjøret fordi de tror de kan stryke over et navn med rød tusj. Totalt feil og ulovlig.</p>
<p><strong>Vil du endre</strong> (bytte hvem som får bilen)? Nytt dokument med to vitner. Samme formkrav som opprettelse.</p>
<p><strong>Vil du slette hele testamentet?</strong> Enklere: Finn originalen og klipp den i tusen biter, eller bren den. Loven krever at du «ødelegger» det fysisk, eller tegner et digert kryss over absolutt hele dokumentet.</p>
<p>Viktig: Å rive en kopi hjemme hjelper ingenting hvis originalen ligger hos tingretten. Det er originalen som teller.</p>""",
        "eksempler": [{"navn": "Tusj-fellen", "tekst": "Svein tegner en strek over nevøens navn i testamentet og skriver niesen inn i margen i stedet. Etter Sveins død er endringen ugyldig — han verken rev hele dokumentet eller brukte to vitner på endringen. Nevøen han var sur på får hytta likevel."}],
        "vanlige_feil": ["Å krysse over bare én setning — for at overstryking skal gjelde MÅ hele testamentet strykes over", "Rive kopien hjemme men glemme originalen hos advokaten"],
        "hva_bor_du_html": "<p>Sikreste metode: Skriv et helt nytt, komplett testament som starter med «Dette testamentet tilbakekaller alle mine tidligere testamenter». To vitner signerer. Kast deretter det gamle i peisen. Ingen tvil om hva som gjelder.</p>",
        "dumme_sporsmal": [
            {"q": "Hva skjer hvis det finnes to testamenter når jeg dør?", "a": "Yngst vinner. Det nyeste overstyrer det gamle på punkter der de er i konflikt. Er de ikke i konflikt, gjelder begge."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "42", "tittel": "Formkrav (samme krav gjelder)", "available": True}, {"lov": "arveloven", "paragraf": "47", "tittel": "Retten til å endre", "available": True}],
    },
    {
        "number": "49", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Arvepakt: Kan du låse arven din for alltid?",
        "kategori": "arv",
        "description": "Vil du binde deg selv til et testament slik at du aldri kan endre det? Da kan du inngå en arvepakt — ofte gjort som gjenytelse for stell og pleie.",
        "kort_svar": "En arvepakt er et spesielt testament der du frivillig gir fra deg retten til å ombestemme deg. Når du har inngått en arvepakt om å gi noen en eiendom eller penger, kan du ikke lenger endre eller trekke tilbake denne gaven.",
        "paragraftekst": "Testator kan ved arvepakt binde seg til ikke å opprette, endre eller tilbakekalle et testament. Arvepakt opprettes etter reglene i §§ 41 til 46.",
        "hva_betyr_html": """<p>Et testament med hengelås. I arvepakten skriver du at «dette testamentet kan ikke endres eller tilbakekalles». Uansett om du blir dement, sur, eller møter en ny kjæreste — arvepakten står fast.</p>
<p>Arvepakten må oppfylle samme formkrav som et vanlig testament (skriftlig, to vitner).</p>
<p>Typisk brukstilfelle: Datteren din sier «Jeg skal flytte hjem og stelle deg i tjue år og bruke sparepengene mine på gården din — men bare hvis du garanterer at jeg arver gården.» For at hun skal tørre risikoen, oppretter dere en arvepakt.</p>""",
        "eksempler": [{"navn": "Avtalen om hytta", "tekst": "Sønnen Lars betaler 500 000 kr for å totalrenovere farens hytte mot garanti for å arve den alene. De inngår skriftlig arvepakt foran to vitner. Fem år etter vil faren gi hytta til en ny samboer. Advokaten sier nei — faren er låst. Lars får hytta."}],
        "vanlige_feil": ["Tro at et vanlig testament er bindende — et vanlig testament er aldri bindende, du MÅ skrive «arvepakt» eller «forplikter meg til ikke å endre dette»", "Tro at arvepakt hindrer deg i å selge eiendommen mens du lever"],
        "hva_bor_du_html": "<p>Ikke inngå arvepakt med mindre det er tvingende nødvendig. Du mister din egen frihet. Hvis du er arving og skal investere egne penger i foreldrenes hus mot løfte om fremtidig arv: Krev formell arvepakt med to vitner. Et hyggelig løfte over kaffekoppen er null verdt.</p>",
        "dumme_sporsmal": [
            {"q": "Kan vi angre oss hvis BEGGE er enige?", "a": "Ja. Hvis begge parter er enige om å oppløse arvepakten, kan dere kaste den og skrive nytt testament. Arvepakten er til for å beskytte mottakeren, ikke for å torturere dere begge."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "47", "tittel": "Retten til å endre testament", "available": True}, {"lov": "arveloven", "paragraf": "42", "tittel": "Formkrav", "available": True}],
    },
    {
        "number": "50", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Pliktdelsarv: Hvor mye må barna få?",
        "kategori": "arv",
        "description": "Du kan ikke gjøre barna dine arveløse. Pliktdelsarven sikrer at to tredjedeler av alt du eier går til barna, med et tak på 15G per barn.",
        "kort_svar": "Barna dine har lovfestet krav på pliktdelsarv: to tredjedeler (2/3) av formuen din. Resten kan du testamentere til hvem du vil. Men pliktdelsarven kan aldri overstige 15 ganger grunnbeløpet (ca 1,9 mill kr) per barn.",
        "paragraftekst": "To tredeler av formuen etter arvelateren er pliktdelsarv for livsarvingene. Pliktdelsarven er likevel aldri større enn 15 ganger folketrygdens grunnbeløp ved arvefallet til hvert av arvelaterens barn eller hvert barns linje. Arvelateren kan bare rå over pliktdelsarven ved testament hvis det er særskilt hjemmel for dette i lov eller livsarvingene samtykker.",
        "hva_betyr_html": """<p><strong>Hovedregelen:</strong> 2/3 av din formue er låst til barna. Du har bare frihet over den siste 1/3 (fri arv).</p>
<p><strong>Taket på 15G:</strong> Rike folk slipper å gi alt til barna. Har du to barn og 30 millioner, har hvert barn krav på maks 15G (ca 1,9 mill). Totalt ca 3,8 millioner. De resterende 26+ millionene er fri arv.</p>
<p><strong>Eksempel:</strong> Har du 3 millioner og to barn: 2 millioner er bundet (2/3). Du kan testamentere de siste 1 million fritt. Lars og Anne har krav på 1 million hver som pliktdel. Lars strykes ikke fra arven, uansett hvilke testamenter du skriver.</p>""",
        "eksempler": [{"navn": "Jens gjør forskjell på barna", "tekst": "Jens eier 3 millioner, ugift. Skriver testament: «Datteren Anne skal arve absolutt alt». Sønnen Lars saksøker. 2/3 av 3 mill = 2 mill er bundet. Lars og Anne har krav på 1 mill hver i pliktdel. Testamentet er ugyldig for Lars sin pliktdel. Lars får 1 million. Anne beholder resten."}],
        "vanlige_feil": ["Prøve å gjøre barn arveløse via testament «fordi vi ikke har snakket på 20 år» — det underkjennes alltid for pliktdelens del", "Glemme at 15G-taket regnes ut fra G-verdien den dagen du dør, ikke den dagen du skriver testamentet"],
        "hva_bor_du_html": "<p>Regn ut verdien av det du eier minus gjeld. 1/3 av nettoformuen er din frie pott. Det er den du kan lage moro med i et testament. For verdier over 15G per barn er du enda friere — og bør absolutt bruke det.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg ikke bare gi bort huset før jeg dør for å gjøre dem arveløse?", "a": "Jo! Pliktdelsarven gjelder bare det du eier den dagen du dør. Gir du bort hytta som en reell livsdisposisjon 20 år før du dør, er det utenfor rekkevidden av pliktdelsarven."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "4", "tittel": "Første arvegangsklasse", "available": True}, {"lov": "arveloven", "paragraf": "8", "tittel": "Ektefellens arverett", "available": True}],
    },
    {
        "number": "51", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Kan du tvinge barnet til å arve penger i stedet for hytta?",
        "kategori": "arv",
        "description": "Barna har krav på verdien av pliktdelsarven, men du bestemmer i testamentet om de får kontanter eller en spesiell hytte.",
        "kort_svar": "Gjennom testament kan du bestemme hva barna skal få pliktdelsarven sin i — kontanter, hytta, bilen. Du kan øremerke familiehytta til ett spesielt barn selv om hytten er verdt mer enn barnets andel, så lenge det barnet kjøper ut de andre for overskuddet.",
        "paragraftekst": "Arvelateren kan bestemme ved testament at en livsarving skal få pliktdelsarven utbetalt i kontanter. Arvelateren kan ved testament gi en livsarving rett til å få arven utdelt som en bestemt eiendel, også om eiendelen er verd mer enn arvingens del av arven, forutsatt at livsarvingen betaler det overskytende til boet.",
        "hva_betyr_html": """<p>Barna har krav på en bestemt verdi i kroner — ikke krav på å eie akkurat sofaen din eller huset ditt.</p>
<p><strong>Kontant-regelen:</strong> Du kan tvinge datteren til å motta sin pliktdelsarv i penger. Da kan sønnen overta familiebedriften alene uten at søsteren krever å eie 50 % av aksjene.</p>
<p><strong>Gjenstands-regelen:</strong> Du kan gi datteren som vedlikeholdt hytta førsterett til å overta den. Er hytta verdt 3 mill og hennes andel bare 1 mill, er testamentet gyldig likevel — hun betaler mellomlegget (2 mill) til boet. Har hun ikke råd, kan hun takke nei og hytten selges.</p>""",
        "eksempler": [{"navn": "Stian og veteranbilen", "tekst": "Stian eier veteranbil (500 000 kr) og bankkonto (500 000 kr). To barn. I testamentet: Eldest barn får veteranbilen, yngste gets bankkontoen. Begge arver 500 000 kr — ingen loddtrekning, ingen tvangssalg, ingen krangel."}],
        "vanlige_feil": ["Tro at barnet som øremerkes hytta får den gratis selv om den er verdt mer enn barnets arveandel", "Ikke skrive noe i testamentet og stole på at barna blir enige — ender ofte med tvangssalg"],
        "hva_bor_du_html": "<p>Har du spesifikke eiendeler (slektsgård, hytte, båt, kunst, aksjer)? Bruk denne paragrafen! Skriv: «Sønnen X skal ha rett til å overta eiendommen Y. Eventuell overskytende verdi utbetales til boet.» Forhindrer krangel og bitter arvestrid.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg tvinge et barn til å ta over hundene mine?", "a": "Nei. Du kan øremerke hvem som får rett til kjæledyr, men ingen kan tvinges til å ta imot noe de ikke vil ha. Vil de ikke ha hundene, blir de boets problem."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "50", "tittel": "Pliktdelsarven", "available": True}, {"lov": "arveloven", "paragraf": "104", "tittel": "Rett til å overta eiendeler", "available": False}],
    },
    {
        "number": "52", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Vil du at arven til barnet ditt skal være særeie?",
        "kategori": "arv",
        "description": "Du kan bruke testamentet til å beskytte barnets arv mot en fremtidig skilsmisse. Loven lar deg bestemme at arven skal være barnets særeie.",
        "kort_svar": "Du kan skrive i testamentet at arven du gir barna skal være særeie — arven deles ikke med barnets ektefelle ved en eventuell skilsmisse. Dette er kanskje det vanligste punktet foreldre legger inn i et testament.",
        "paragraftekst": "Arvelateren kan bestemme ved testament at en ordning som nevnt i ekteskapsloven §§ 42 og 43 skal gjelde for livsarvingens pliktdelsarv.",
        "hva_betyr_html": """<p>Arv er ikke automatisk særeie. Uten at du bestemmer noe, kan arven din blandes inn i barnets felleseie og havne hos en ektefelle ved skilsmisse.</p>
<p>Med § 52 kan du feste en betingelse: Arven er barnets særeie. Den deles ikke ved skilsmisse, uansett antall ekteår og uansett hvilken ektepakt barna har laget seg imellom.</p>
<p>En god formular: <em>«Arv etter meg, samt avkastning av den og hva som trer i stedet for den, skal være arvingens fullstendige særeie. Arvingen kan likevel fritt endre dette gjennom ektepakt.»</em></p>""",
        "eksempler": [{"navn": "Far beskytter hytta", "tekst": "Jonas testamenterer hytten til Petter med klausul om særeie. Ti år etter krever Petters kone skilsmisse og halvparten av verdiene. Siden Jonas brukte § 52, holdes hytta helt utenfor skilsmisseoppgjøret. Petter beholder den alene."}],
        "vanlige_feil": ["Tro at penger barn arver «automatisk» er særeie — de er det ikke uten uttrykkelig bestemmelse", "Barna putter særeie-arven på familiens felleskonto — da blandes pengene og særeievernet svekkes"],
        "hva_bor_du_html": "<p>Har du barn? Legg alltid inn særeie-klausul i testamentet. En god formulering tar to minutter å skrive og gir livsvarig beskyttelse mot fremtidige skilsmisser du ikke kan forutse.</p>",
        "dumme_sporsmal": [
            {"q": "Beskytter særeie arven mot namsmannen hvis barnet mitt får gjeld?", "a": "Nei. Særeie beskytter KUN mot ektefellen ved skilsmisse. Kreditorer og namsmannen kan ta pant i særeie-eiendeler uansett."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "50", "tittel": "Pliktdelsarven", "available": True}, {"lov": "arveloven", "paragraf": "53", "tittel": "Sperre arven for barn under 25 år", "available": True}],
    },
    {
        "number": "53", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Kan du sperre arven for barn under 25 år?",
        "kategori": "arv",
        "description": "Er du redd 18-åringen din vil sløse bort all arven? Du kan ved testament låse arven frem til barnet fyller 25 år. Pengene beskyttes også mot barnets kreditorer.",
        "kort_svar": "Du kan skrive i testamentet at barnet ditt ikke skal få fri tilgang til arven sin før det fyller 25 år. Pengene låses og forvaltes, men barnet har rett på rentene underveis. Arven beskyttes også mot barnets kreditorer i denne perioden.",
        "paragraftekst": "Når det må anses å være til det beste for livsarvingen, kan arvelateren ved testament fastsette begrensninger for livsarvingens råderett over pliktdelsarven frem til livsarvingen fyller 25 år. Avkastningen av arven tilfaller uansett livsarvingen.",
        "hva_betyr_html": """<p>Et barn som blir myndig ved 18 år, rår over sin egen økonomi. Arver det millioner, kan pengene fort fordufte. § 53 lar deg sette arven «i bankboksen» frem til barnet er 25 år.</p>
<p>Pengene forvaltes av det offentlige (Statsforvalteren) eller en tillitsmann du utpeker. Barnet mottar renteavkastningen underveis. Pengene beskytes også mot barnets kreditorer — inkassokrav og forbrukslån kan ikke røre dem.</p>
<p>Grensen: Du kan ikke sperre pliktdelsarven lenger enn til 25 år. Den frie arven kan derimot sperres lenger.</p>""",
        "eksempler": [{"navn": "Mor låser arven", "tekst": "Kari er alenemor og kreftsyk. Sønnen Emil (17) sliter med rusproblemer. Kari låser Emils arv frem til han er 25 år i testamentet. Da Kari dør, forvalter Statsforvalteren pengene. Emil får rentene, men kapitalen er urørt inntil 25-årsdagen."}],
        "vanlige_feil": ["Låse arven frem til barnet er 30 år — dette er ulovlig for pliktdelsarven, den slippes alltid fri ved 25 år", "Tro at pengene bare settes inn på barnets sparekonto — sperring krever en offisiell forvalter"],
        "hva_bor_du_html": "<p>Særlig relevant for foreldre med rusavhengige barn eller barn som mangler økonomisk styring. Oppsøk advokat — å lage en god tillitsmannsordning med klare instrukser krever god formulering.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg låse den frie arven lenger enn til 25 år?", "a": "Ja. Taket på 25 år gjelder bare pliktdelsarven. Den frie tredjedelen av formuen din kan du i prinsippet binde lenger, eller knytte til en stiftelse."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "50", "tittel": "Pliktdelsarven", "available": True}, {"lov": "arveloven", "paragraf": "52", "tittel": "Særeie for arven", "available": True}],
    },
    {
        "number": "54", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Hva skjer med arven hvis barnet dør ungt eller aldri får testasjonsevne?",
        "kategori": "arv",
        "description": "Hvis barnet ditt er under 18 år eller har varig psykisk funksjonshemming, kan du styre hvor arven deres skal gå hvis de skulle dø kort tid etter deg.",
        "kort_svar": "Du kan i testamentet bestemme hva som skal skje med arven til barnet ditt dersom barnet dør før det fyller 18 år, eller aldri vil bli mentalt i stand til å skrive et eget testament.",
        "paragraftekst": "Arvelateren kan bestemme ved testament hvordan en livsarvings mottatte pliktdelsarv skal fordeles for det tilfellet at livsarvingen dør før fylte 18 år. En slik bestemmelse mister sin virkning når livsarvingen fyller 18 år, eller hvis livsarvingen før dette tidspunktet oppretter testament eller får barn.",
        "hva_betyr_html": """<p><strong>Scenario 1 (barn under 18):</strong> Du dør, sønnen arver. Sønnen dør et halvt år etter, 17 år gammel. Da følger pengene vanlig arvelov — og kan ende opp hos din ekskone. Du kan forhindre dette ved å skrive i testamentet hvem pengene skal gå til hvis sønnen dør før han er 18. Bestemmelsen slettes automatisk den dagen sønnen fyller 18.</p>
<p><strong>Scenario 2 (varig manglende testasjonsevne):</strong> Har du et barn med dyp psykisk utviklingshemming som aldri vil kunne skrive eget testament, kan du styre hva som skjer med arven etter barnet dør.</p>""",
        "eksempler": [{"navn": "Mor stanser eksen", "tekst": "Janne skiller seg fra voldelig Petter. Sønnen Ole (12 år) arver Janne. Janne frykter at Petter vil arve hvis Ole dør som barn. I testamentet: «Dør Ole før fylte 18 uten egne barn, går arven til Kreftforeningen.» Ole dør 17½ år gammel. Petters arverett blokkeres. Pengene går til Kreftforeningen."}],
        "vanlige_feil": ["Foreldre med myndige barn prøver å styre hvem som arver barnets penger etter barnets død som 50-åring — totalt ulovlig for friske, myndige barn"],
        "hva_bor_du_html": "<p>Har du et mindreårig barn og er alvorlig syk, og det er stor konflikt mellom foreldrene? Bruk denne regelen for å sikre at arven ikke havner hos feil person. For barn med dyp funksjonshemming er det nesten påkrevd å ha et testament som tar høyde for § 54 andre ledd.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om sønnen min er 16 år og får et barn selv før han dør?", "a": "Da sier loven at testamentets bestemmelse mister virkning. Det ufødte eller fødte barnebarnet arver faren i stedet."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "50", "tittel": "Pliktdelsarven", "available": True}, {"lov": "arveloven", "paragraf": "41", "tittel": "Testasjonsevne", "available": True}],
    },
    {
        "number": "55", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Kan du gjøre et barn helt arveløst?",
        "kategori": "arv",
        "description": "Barna har i utgangspunktet krav på arv uansett. Men hvis barnet har begått alvorlig lovbrudd mot familien, kan du faktisk gjøre det helt arveløst — med statens godkjenning.",
        "kort_svar": "Du kan ikke gjøre barna arveløse fordi dere er uvenner. Loven tillater bare fjerning av pliktdelsarven hvis barnet har begått alvorlig lovbrudd mot deg eller nær familie, OG du får godkjenning fra staten.",
        "paragraftekst": "Arvelateren kan bestemme ved testament at en livsarving ikke skal ta pliktdelsarv hvis livsarvingen har gjort seg skyldig til straff for et lovbrudd med en strafferamme på fengsel i ett år eller mer mot arvelateren eller arvelaterens nære familie. Et slikt testament gjelder bare når det er stadfestet av Kongen.",
        "hva_betyr_html": """<p>To krav for å gjøre et barn arveløst:</p>
<p><strong>1. Grovt lovbrudd:</strong> Handlingen må ha strafferamme på minst ett år. Vold, grove trusler, svindel mot deg eller din ektefelle, barn eller søsken. Ikke småtyveri fra tenårene.</p>
<p><strong>2. Statens godkjenning:</strong> Testamentet MÅ sendes inn og «stadfestes av Kongen» (Justisdepartementet) med bevis for lovbruddet. Uten stempelet gjelder ikke unntaket.</p>
<p>Konsekvens: Det kriminelle barnet behandles som om det allerede var dødt. Andelen går til barnets egne barn (dine barnebarn) eller de andre søsknene.</p>""",
        "eksempler": [{"navn": "Vold i familien", "tekst": "Jonas blir utsatt for grov vold av sønnen Tom, som dømmes til to år. Jonas oppretter testament med § 55-klausul, sender det til departementet og får det godkjent. Når Jonas dør, nektes Tom all arv. Toms andel deles mellom de to andre søsknene."}],
        "vanlige_feil": ["Prøve å gjøre barn arveløse fordi de «ikke har hatt kontakt på tyve år» — testamentet kjennes ugyldig", "Glemme å sende inn for stadfestelse — uten statens stempel gjelder ikke unntaket"],
        "hva_bor_du_html": "<p>Har du et familiemedlem som har svindlet eller mishandlet familien? Kontakt advokat. Prosessen krever riktig dokumentasjon med politianmeldelser eller dommer.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om barnet mitt stjal fra naboen — kan jeg fjerne arven da?", "a": "Nei. Lovbruddet MÅ være rettet direkte mot deg eller din nærmeste familie. At barnet er kriminell ute i samfunnet, gir ingen rett til å fjerne pliktdelsarven."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "50", "tittel": "Pliktdelsarven", "available": True}, {"lov": "arveloven", "paragraf": "72", "tittel": "Fradømmelse av arverett", "available": False}],
    },
    {
        "number": "56", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Ekstra arv til barn som fortsatt forsørges",
        "kategori": "arv",
        "description": "Hvis et barn under utdanning mister forelderen sin, har barnet krav på en ekstra sum fra dødsboet for å sikre livsopphold, FØR resten av arven deles.",
        "kort_svar": "Barn som var økonomisk avhengige av avdøde har rett på en ekstra sum fra boet til livsopphold og utdanning. Dette kravet trekkes ut FØR arven deles med voksne søsken og kan ikke fjernes ved testament.",
        "paragraftekst": "Barn av arvelateren som arvelateren fortsatt forsørget da han eller hun døde, har rett til en sum av boet til å sikre livsopphold og utdanning mv. dersom dette er rimelig etter forholdene. Retten etter første ledd kan ikke begrenses ved testament. Retten skal oppfylles i boet før annen arv.",
        "hva_betyr_html": """<p>En far dør med en datter på 35 år og en sønn på 15 år. Etter loven deler de likt. Men det er svært urettferdig for 15-åringen som nettopp har mistet forsørgeren sin.</p>
<p>§ 56 gir det yngste barnet rett til å trekke ut en fast sum FØR fordelingen starter. Summen vurderes konkret — en 15-åring trenger mer tid enn en 19-åring.</p>
<p>Kravet er knallsterkt: Det kan IKKE fjernes ved testament, og det betales FØR en eneste krone fordeles til voksne søsken. Barnepensjon fra NAV og livsforsikringer tas med i regnestykket.</p>""",
        "eksempler": [{"navn": "Storesøster og lillebror", "tekst": "Per dør og etterlater 1 million til Siri (30) og Marius (16). Normalt 50/50. Marius' verge krever 300 000 kr til livsopphold etter § 56. De trekkes ut FØR fordelingen. Resten (700 000 kr) deles 50/50 — Siri får 350 000 kr, Marius ytterligere 350 000 kr. Marius er dermed klart bedre stilt."}],
        "vanlige_feil": ["Eldre søsken insisterer på streng 50/50-deling og nekter å anerkjenne mindreåriges forsørgerkrav", "Glemme å kreve dette beløpet for mindreårig barn under privat arveoppgjør"],
        "hva_bor_du_html": "<p>Er du verge for et mindreårig barn som mister en forelder? Krev midler etter § 56 under skiftet. Ikke godta at stesøsken bare vil dele alt i to. Krev at en pott holdes til utdanning FØR en krone fordeles.</p>",
        "dumme_sporsmal": [
            {"q": "Kan faren min skrive i testamentet at jeg ikke får disse pengene?", "a": "Nei. § 56 slår uttrykkelig fast at retten til utdannings/livsoppholdsmidler ikke kan fjernes ved testament. Det er en av få regler som totaloverstyrer den som er død."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "50", "tittel": "Pliktdelsarven", "available": True}, {"lov": "arveloven", "paragraf": "4", "tittel": "Første arvegangsklasse", "available": True}],
    },
    {
        "number": "57", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Skrev de feil i testamentet? Tolkning av viljen",
        "kategori": "arv",
        "description": "Fant du en skrivefeil i testamentet? Loven sier at det er den egentlige meningen som teller — ikke de knusktørre ordene på papiret.",
        "kort_svar": "Et testament tolkes slik den som skrev det faktisk mente. Har testamentet fått feil innhold på grunn av en feilskrift eller annen feil, gjelder det slik testator mente — når dette kan klarlegges.",
        "paragraftekst": "Testamentet skal tolkes i samsvar med det testator mente. Har testamentet på grunn av feilskrift eller annen feil fått et annet innhold enn hva testator mente ved opprettelsen, skal testamentet gjelde slik testator mente, når dette kan klarlegges.",
        "hva_betyr_html": """<p>Loven driver ikke grammatikk-politi. Det er den avdødes egentlige vilje som gjelder, ikke bokstavelig fortolkning av ordene.</p>
<p>Eksempler: Testamenterte «min blå Ford» men solgte den og kjøpte rød Ford? Ment å skrive «100 000 kr» men fikk «10 000 kr»? Brukte kallenavnet «Lille-Per» i stedet for det formelle navnet? Kan meningen klarlegges, rettes feilen.</p>
<p>«Klarlegges» er nøkkelordet. Notater, e-poster med advokat, utkast, vitneforklaringer — alt som kaster lys over hva de egentlig mente.</p>""",
        "eksempler": [{"navn": "Kallenavnet", "tekst": "Kari testamenterer hytten til «Lille-Per». Ingen «Lille-Per» i Folkeregisteret. Men alle vet at grandnevøen Per Andreassen alltid ble kalt «Lille-Per». Fjerne slektninger prøver å ugyldiggjøre testamentet pga upresist navn. Retten viser til § 57: meningen kan klarlegges, grandnevøen får hytten."}],
        "vanlige_feil": ["Å tro man kan bruke advokatfunn i formuleringene til å felle testamentet — åpenbar mening vinner over flisespikkeri", "Bruke bare kallenavn og pronomen i testamentet uten fulle navn og fødselsdato"],
        "hva_bor_du_html": "<p>Finn en åpenbar feil i et testament? Samle bevis umiddelbart — e-post med advokat, utkast, vitneforklaringer. Har du selv et testamente med feil? Skriv et nytt med korrekt informasjon og tydelige identifikatorer (fullt navn, fødselsdato, matrikkelnnummer på eiendommer).</p>",
        "dumme_sporsmal": [
            {"q": "Hva hvis det er klin umulig å vite hva personen mente?", "a": "Hvis teksten er totalt uforståelig og ingen bevis for meningen finnes, må punktet i testamentet strykes. Dommeren kan ikke gjette seg frem."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "58", "tittel": "Supplerende tolkningsregler", "available": True}, {"lov": "arveloven", "paragraf": "59", "tittel": "Forutsetningssvikt", "available": True}],
    },
    {
        "number": "58", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Slik tolker du et uklart testament (de fem reglene)",
        "kategori": "arv",
        "description": "Hva gjør dere hvis testamentet mangler detaljer? Arveloven har fem faste reserveregler som slår inn for å fylle hullene etter den avdøde.",
        "kort_svar": "Når et testament er utydelig og dere ikke finner hva den avdøde egentlig mente, bruker dere lovens fem reserveregler: Ting går foran penger. Barnebarn trer inn. Skilsmisse sletter arven til eksen. Forsvunne ting gir ikke penger. Yngste testament vinner.",
        "paragraftekst": "Når det ikke er grunn til å tro at testator mente noe annet, skal disse reglene gjelde: a. Strekker ikke arven til, skal den som skal arve en bestemt ting, gå foran den som skal arve en pengesum. b. Om en testamentsarving dør før testator, trer testamentsarvingens livsarvinger i stedet. c. Har noen innsatt sin ektefelle eller samboer som arving, og samlivet tok slutt før testator døde, faller testasjonen bort. d. Den som skal arve en bestemt ting, kan ikke kreve vederlag hvis tingen ikke finnes i boet. e. Er det mer enn ett testament, gjelder alle, men et yngre testament tilbakekaller eller overstyrer det eldre ved motstrid.",
        "hva_betyr_html": """<p>Fem verktøy for å løse konflikter i uklare testamenter:</p>
<p><strong>A. Ting vinner over penger.</strong> Tom konto + hytte: Hytten eierne vinner, pengekravene taper.<br>
<strong>B. Barnebarn tar over.</strong> Arvingen i testamentet dør før deg? Arvingens barn trer inn.<br>
<strong>C. Skilsmisse sletter eksen.</strong> Testamenterte til kona i 1990, skilte dere i 2010? Testamentet til kona gjelder IKKE. Automatisk.<br>
<strong>D. Forsvunne ting gir ikke penger.</strong> Testamenterte bilen, men solgte den? Mottakeren kan ikke kreve bilens verdi i penger fra bankkontoen.<br>
<strong>E. Yngst vinner.</strong> To testamenter som strider mot hverandre: det nyeste vinner.</p>""",
        "eksempler": [{"navn": "Båten som ble borte", "tekst": "Lars testamenterer «cabincruiseren» til Tom. Lars selger båten tre år etter. Tom krever 500 000 kr fra bankkontoen. Tom taper: Etter bokstav D kan man ikke kreve penger i stedet for en bestemt ting som ikke lenger finnes i boet."}],
        "vanlige_feil": ["Eksen dukker opp med et gammelt testament og krever arv fordi «han glemte å rive det» — bokstav C stopper dette", "Gi bort millioner man ikke har — skaper voldsomme skuffelser og bokstav A slår inn"],
        "hva_bor_du_html": "<p>Unngå at § 58 brukes: Skriv inn hva som skal skje. «Hvis Tom dør før meg, skal bilen IKKE gå til Toms barn, men tilbake til boet.» Da overstyrer du lovens standardregler og alt blir krystallklart.</p>",
        "dumme_sporsmal": [
            {"q": "Sletter skilsmisseregelen alt i testamentet?", "a": "Den sletter bare disponisjon til fordel for eksen. Resten av testamentet (f.eks. at hunden skal gå til naboen) gjelder fullt ut."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "57", "tittel": "Tolkning av testament", "available": True}, {"lov": "arveloven", "paragraf": "59", "tittel": "Forutsetningssvikt", "available": True}],
    },
    {
        "number": "59", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Testamentet bygget på en løgn eller feil?",
        "kategori": "arv",
        "description": "Skrev de et testament i den tro at barnebarnet tok over gården, men ble barnebarnet advokat i byen? Da kan arvingene endre testamentet.",
        "kort_svar": "Hvis den som skrev testamentet tok feil om noe avgjørende, eller ting endret seg dramatisk etterpå, kan testamentet endres eller kjennes ugyldig. Dette kalles forutsetningssvikt.",
        "paragraftekst": "Hvis testator var uvitende om eller hadde en uriktig oppfatning av forhold som var avgjørende for en testamentarisk disposisjon, eller hvis slike forhold har endret seg etter at testamentet ble opprettet, skal testamentet gjelde slik som testator ville ha ment med den rette kunnskapen, når dette kan klarlegges. Tolkningsregelen gjelder likevel ikke hvis testator senere er blitt kjent med det riktige forholdet og kunne ha endret testamentet.",
        "hva_betyr_html": """<p>Av og til gir folk bort penger av en veldig spesifikk grunn som viser seg å være feil. Loven lar da domstolen rydde opp.</p>
<p>Dommeren spør: «Hadde den avdøde visst den riktige sannheten — ville de da skrevet testamentet på denne måten?» Er svaret åpenbart nei, rettes testamentet.</p>
<p><strong>Viktig unntak:</strong> Fant personen ut om feilen mens de levde og hadde sjanse til å endre testamentet, men lot det bare ligge — da gjelder testamentet uansett. Loven beskytter kun de som IKKE visste.</p>""",
        "eksempler": [{"navn": "Medisinstudiet", "tekst": "Onkel Per øremerker 1 million til niesen Siri «for at hun skal fullføre medisinstudiet». Siri dropper ut av medisin. Per får hjerneslag uken etter og dør uten å kunne endre noe. Familien krever forutsetningssvikt. Siri mister millionen — grunnlaget for gaven er borte og Per hadde ikke mulighet til å endre det."}],
        "vanlige_feil": ["Tro at enhver endring i livssituasjonen utgjør forutsetningssvikt — det må gjelde «avgjørende» forhold som utløste testamentet", "Glemme at den avdøde kanskje visste om den nye situasjonen i årevis uten å endre papiret"],
        "hva_bor_du_html": "<p>Skriv betingelsene uttrykkelig ned i testamentet: «Jeg gir 1 million til Per under forutsetning av at han tar over gårdsbruket.» Da gjør du jobben for arvingene og advokatene som en dag skal rydde opp.</p>",
        "dumme_sporsmal": [
            {"q": "Kan retten gjette hva han ville ha ment?", "a": "Nei — paragrafen sier «når dette kan klarlegges». Retten must ha nok informasjon om personens verdier til å vite hva de ville ha gjort. Kan det ikke bevises, strykes punktet."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "57", "tittel": "Tolkning av testament", "available": True}, {"lov": "arveloven", "paragraf": "45", "tittel": "Ugyldighet ved svik", "available": True}],
    },
    {
        "number": "60", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Felles og gjensidig testament: Hva er det?",
        "kategori": "arv",
        "description": "Skal du og ektefellen skrive testament? De fleste ektepar velger å lage et felles testament på ett papir der de gir arven til hverandre.",
        "kort_svar": "Et «felles testament» er to personers siste ønsker på ett dokument. Et «gjensidig testament» er når to gir arven til hverandre. Paragrafene 61 og 62 gir spesialregler for disse.",
        "paragraftekst": "Bestemmelsene i §§ 61 og 62 gjelder når to eller flere personer har opprettet testament i samme dokument (felles testament), og når to eller flere personer har opprettet testament til fordel for hverandre (gjensidig testament).",
        "hva_betyr_html": """<p>En ren ordbok-paragraf som definerer to begreper:</p>
<p><strong>Felles testament</strong> = formatet. I stedet for to separate ark signerer begge på ett felles papir. Formkravene med to vitner gjelder for begges signaturer.</p>
<p><strong>Gjensidig testament</strong> = innholdet. «Den av oss som lever lengst, arver alt etter den andre.» Ekstremt vanlig blant barnløse ektepar og samboere som vil sikre hverandre.</p>
<p>De to henger nesten alltid sammen: De fleste oppretter ett felles, gjensidig testament på ett papir.</p>""",
        "eksempler": [{"navn": "Samboerne uten barn", "tekst": "Tone og Petter er samboere uten barn. Uten testament vil den andres foreldre arve alt. De oppretter et gjensidig testament på ett dokument: «Dør Petter, arver Tone alt. Dør Tone, arver Petter alt.» Sikrer den gjenlevende fullstendig."}],
        "vanlige_feil": ["Tro at et felles testament låser deg for alltid — du kan oftest endre din del mens dere lever (se § 61)", "Glemme å dekke hva som skjer når BEGGE til slutt er døde"],
        "hva_bor_du_html": "<p>Er du samboer uten barn, eller gift med mine og dine barn? Et felles gjensidig testament er kanskje den viktigste forsikringen du noen gang tegner. Dekk alltid «sekundærdisposisjonen»: Hvem arver når BEGGE er borte?</p>",
        "dumme_sporsmal": [
            {"q": "Må vi være gift for å lage et gjensidig testament?", "a": "Nei. To venner, to søsken eller to samboere kan absolutt lage et felles gjensidig testament."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "61", "tittel": "Tilbakekall av felles testament", "available": True}, {"lov": "arveloven", "paragraf": "62", "tittel": "Tolkningsregler for felles testament", "available": True}],
    },
    {
        "number": "61", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Kan du endre det felles testamentet i skjul?",
        "kategori": "arv",
        "description": "Har dere skrevet gjensidig testament og en endrer mening? Loven forbyr hemmelige endringer. Du MÅ varsle den andre for at det skal gjelde.",
        "kort_svar": "Du kan endre din del av et felles testament, men endringen er bare gyldig hvis den andre får vite om den mens dere begge lever. Hemmelige endringer er ulovlig. Etter den enes død er friheten til å endre sterkt begrenset.",
        "paragraftekst": "Et tilbakekall eller en endring av et felles testament eller gjensidig testament er gyldig bare hvis den andre testatoren har fått kunnskap om tilbakekallet eller endringen før arvelaterens død. Hvis et felles testament sier noe om fordelingen etter at begge er døde, kan den lengstlevende bare endre det som er bestemt om arv til den lengstlevendes egne arvinger etter loven.",
        "hva_betyr_html": """<p><strong>Mens dere begge lever:</strong> Vil du endre din del i skjul? Nei. Endringen er bare gyldig hvis partneren din har fått «kunnskap» om det. Tanken: Partneren stolte på dokumentet, og må få sjansen til å sikre seg selv hvis du trekker deg.</p>
<p><strong>Etter at den ene er død:</strong> Har du arvet alt, er hendene dine mer bundne. Du kan IKKE stryke arvingene til din avdøde partner fra testamentet. Du kan bare endre hva du bestemmer for din EGEN slekt.</p>
<p>Unntak: Var dere barnløse og ville ellers arvet hverandre 100 % etter loven, kan du i mange tilfeller endre testamentet fritt etter partnerens død.</p>""",
        "eksempler": [{"navn": "Bror byttes ut", "tekst": "Gunnar og Siri har gjensidig testament — når begge er borte deles arven mellom Gunnars bror og Siris søster. Gunnar dør, Siri arver alt. Siri stryker Gunnars bror og gir alt til søsteren. Gunnars bror saksøker. Broren vinner: Siri hadde ingen rett til å stryke arven til Gunnars familie etter hans død."}],
        "vanlige_feil": ["Folk river i stykker felles-testamentet etter at partneren har kommet på pleiehjem uten å si det til dem", "Tro at «siden jeg arvet det, kan jeg skrive nytt testament til fordel for min nye kjæreste» — du eier det, men det gamle testamentet binder fremtiden"],
        "hva_bor_du_html": "<p>Vil du ha frihet til å endre alt etter partnerens død? Skriv det inn mens dere begge lever: «Den lengstlevende står fritt til å tilbakekalle eller endre dette testamentet, også for den delen som stammer fra den førstavdøde.»</p>",
        "dumme_sporsmal": [
            {"q": "Må han signere på at jeg har endret det?", "a": "Nei. Han trenger ikke samtykke eller godkjenne det. Kravet er bare «kunnskap» — han må ha sett det eller lest det. En e-post er nok."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "60", "tittel": "Felles og gjensidig testament", "available": True}, {"lov": "arveloven", "paragraf": "62", "tittel": "Tolkningsregler", "available": True}],
    },
    {
        "number": "62", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Hva skjer hvis det felles testamentet mangler viktige detaljer?",
        "kategori": "arv",
        "description": "Arvet du ektefellen i et gjensidig testament, men dere glemte å skrive hvordan pengene fordeles når DU dør? Loven bruker faste reserveregler.",
        "kort_svar": "Når lengstlevende har arvet i et gjensidig testament, rår de over hele formuen som eier. Hvis testamentet ikke sier noe om fordeling når begge er døde, deles potten automatisk 50/50 mellom de to familiene.",
        "paragraftekst": "Har den lengstlevende testatoren overtatt arven etter et felles testament, rår den lengstlevende i levende live som en eier over hele formuen. Hvis testamentet bestemmer noe om arverett for den førstavdødes arvinger, men ikke om den nærmere fordelingen, skal halvparten av den samlede formuen gå til den førstavdødes arvinger og halvparten til den lengstlevendes arvinger. Gjelder bare for barnløse testatorpar.",
        "hva_betyr_html": """<p>Tre reserveregler for barnløse ektepar med dårlig skrevne testamenter:</p>
<p><strong>A. I levende live:</strong> Enken rår over alt som eier — kan selge huset, reise bort pengene, gi gaver. Avdødes familie kan ikke blande seg inn.</p>
<p><strong>B. 50/50 ved død:</strong> Testamentet sier «arven skal gå til begges familier» men ikke hvilken brøk? Loven klipper automatisk i to. 50 % til den første avdødes slekt, 50 % til den sist avdødes slekt.</p>
<p><strong>C. Full frihet:</strong> Testamentet sa bare «lengstlevende tar alt» og ingenting om hva som skjer etterpå? Da eier enken alt fritt — kan skrive nytt testament til hvem hun vil. Gjør hun det ikke, deles alt 50/50.</p>""",
        "eksempler": [{"navn": "Arvebrøken", "tekst": "Barnløse Hans og Grete, gjensidig testament: «Lengstlevende arver alt. Etter oss til begges familier.» Hans dør, Grete arver 4 mill. Grete dør 15 år etter, boet er 8 mill. Testamentet mangler brøk — § 62 b slår inn: 4 mill til Hans' brødre og nieser, 4 mill til Gretes slektninger."}],
        "vanlige_feil": ["Avdødes familie prøver å stoppe enken fra å selge huset — hun rår som eier, de har ingen makt mens hun lever", "Glemme at enken fritt kan skrive nytt testament til ny kjæreste hvis testamentet ikke sier noe om fordelingen etterpå"],
        "hva_bor_du_html": "<p>Unngå at § 62 brukes: Skriv alltid inn en sekundærdisposisjon. «Når den lengstlevende av oss dør, fordeles formuen slik: 60 % til hans slekt, 40 % til hennes slekt.» Da slipper dere lovens reserveregler.</p>",
        "dumme_sporsmal": [
            {"q": "Er dette bare for barnløse?", "a": "Ja. Innledningen presiserer at disse reglene gjelder «hvis testatorene ikke etterlater seg livsarvinger». Har de barn, styres oppgjøret av barnas ufravikelige pliktdelsarv i stedet."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "60", "tittel": "Felles og gjensidig testament", "available": True}, {"lov": "arveloven", "paragraf": "61", "tittel": "Tilbakekall", "available": True}],
    },
]

PARAGRAPHS = PARAGRAPHS + _ARVELOVEN_39_62

_ARVELOVEN_63_82 = [
    {
        "number": "63", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Slik oppbevarer du testamentet trygt hos tingretten",
        "kategori": "arv",
        "description": "Du kan levere det originale testamentet til tingretten for trygg registrering. Det er hemmelig mens du lever, og tingretten sørger for at det fremlegges når du dør.",
        "kort_svar": "Du kan levere det originale testamentet til tingretten for oppbevaring. Tingretten registrerer det på fødselsnummeret ditt og legger det automatisk frem når du dør. Strengt hemmelig mens du lever — ingen kan sjekke om du har testament.",
        "paragraftekst": "Testator kan levere testamentet, i original, til oppbevaring og registrering hos enhver tingrett. Testamentet kan leveres i lukket omslag. Retten skal ikke gi opplysninger til andre enn testator om at den har et testament til oppbevaring. Retten skal sørge for at et testament som er levert til oppbevaring, legges frem når testator er død. Oppbevaring og registrering har ikke betydning for testamentets gyldighet.",
        "hva_betyr_html": """<p>Et testament er bare nyttig hvis arvingene faktisk finner det. Tingretten fungerer som en trygg bankboks: du leverer originalen, tingretten kobler det til fødselsnummeret ditt, og den dag du dør får de automatisk beskjed fra Folkeregisteret og legger det frem.</p>
<p>Du kan levere i forseglet konvolutt om du vil holde innholdet privat selv for rettens ansatte. Ingen — ikke barna, ikke samboeren — kan sjekke om du har testament så lenge du lever. Absolutt taushetsplikt.</p>
<p>Gjør tingretten en feil (roter bort dokumentet eller glemmer å legge det frem), kan de som tapte arven kreve erstatning fra staten.</p>""",
        "eksempler": [{"navn": "Kari", "tekst": "Kari (72) gir en sum til Kreftforeningen men vil ikke at barna vet om det mens hun lever. Hun legger testamentet i forseglet konvolutt og leverer til tingretten med passet. Ti år etter dør Kari. Tingretten får automatisk melding, åpner konvolutten og kontakter både barna og Kreftforeningen."}],
        "vanlige_feil": ["Legge originalen i en hjemmeskuff der den kan kastes eller holdes skjult", "Levere kopi — tingretten godtar kun originalen", "Skrive nytt testament hjemme men glemme å hente ut det gamle fra tingretten"],
        "hva_bor_du_html": """<ol>
<li>Få testamentet riktig signert med to vitner (§ 42).</li>
<li>Ta med originalen og gyldig legitimasjon.</li>
<li>Lever til nærmeste tingrett — du kan bruke alle landets tingretter uavhengig av bosted.</li>
<li>Betal engangsgebyr (sjekk domstol.no for nøyaktig beløp — typisk under 1 000 kr).</li>
<li>Får du nytt behov: hent ut det gamle og lever nytt.</li>
</ol>""",
        "dumme_sporsmal": [
            {"q": "Kan barna mine ringe tingretten og sjekke om jeg har testament?", "a": "Nei. Tingretten vil ikke en gang bekrefte eller avkrefte at de har et dokument på navnet ditt så lenge du lever."},
            {"q": "Koster det penger?", "a": "Ja, et engangsgebyr ved innlevering. Det koster ingenting for arvingene når de henter det etter dødsfallet."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "64", "tittel": "Bortkommet testament", "available": True}, {"lov": "arveloven", "paragraf": "42", "tittel": "Formkrav til testament", "available": True}],
    },
    {
        "number": "64", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Hva skjer hvis testamentet er borte?",
        "kategori": "arv",
        "description": "Gjelder et testament selv om originalen er forsvunnet? Ja — hvis innholdet kan bevises og det ikke er trolig at det ble tilbakekalt.",
        "kort_svar": "Et forsvunnet testament gjelder fortsatt hvis innholdet kan bevises med kopi eller vitner. Unntaket er hvis det er mest sannsynlig at den avdøde kastet det med vilje for å tilbakekalle det.",
        "paragraftekst": "Hvis det kan sannsynliggjøres at testator har etterlatt seg et gyldig testament, men dette testamentet ikke er å finne etter testators død, skal det gjelde hvis innholdet kan bringes på det rene. Testamentet legges likevel ikke til grunn hvis det mest trolig er tilbakekalt.",
        "hva_betyr_html": """<p>Papirer kan brenne, kastes ved en feiltakelse under flytting, eller forsvinne i rot. Et testament slutter ikke å gjelde bare fordi originalen er borte — to vilkår må imidlertid være oppfylt:</p>
<p><strong>1. Innholdet må kunne bevises.</strong> En kopi med signaturer, en scannet versjon, advokatens utskrift. Muntlig vitneforklaring om "hva han sa" er mye vanskeligere.</p>
<p><strong>2. Testamentet er ikke tilbakekalt.</strong> Var originalen borte etter at personen ga uttrykk for anger? Da antar loven at det ble kastet med vilje. Den som vil at testamentet skal gjelde, har bevisbyrden.</p>""",
        "eksempler": [{"navn": "Marius og Tom", "tekst": "Marius dør brått. Ingen original finnes. Nevøen Tom har fotokopi av testament med hytta til ham. Det fremkommer at Marius hadde innbrudd der papirer ble stjålet. Ingen bevis for at han ville gjøre Tom arveløs. Retten godkjenner kopien — testamentet forsvant i innbruddet, ikke ved tilbakekall."}],
        "vanlige_feil": ["Oppbevare originalen usikret uten å fortelle noen at den er der", "Tro at en usignert Word-fil beviser et gyldig testament", "Brenne originalen for å tilbakekalle, men glemme kopien hos advokaten"],
        "hva_bor_du_html": "<p>Oppbevar originalen hos tingretten (§ 63) — eneste feilsikre metode. Vil du tilbakekalle: skriv «TILBAKEKALT» med dato og signatur over hele dokumentet, eller opprett et nytt testament som uttrykkelig erstatter det gamle.</p>",
        "dumme_sporsmal": [
            {"q": "Er det straffbart å kaste noen andres testament for å sikre egen arv?", "a": "Ja, svært alvorlig lovbrudd (dokumentfalsk og bedrageri). Den som bevisst ødelegger et testament kan fradømmes all rett til arv."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "63", "tittel": "Oppbevaring hos tingretten", "available": True}, {"lov": "arveloven", "paragraf": "48", "tittel": "Tilbakekall og endring", "available": True}],
    },
    {
        "number": "65", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Frister for å kreve arv eller klage på et testament",
        "kategori": "arv",
        "description": "Har du funnet et testament du arver etter? Eller vil du klage fordi det er ugyldig? Du har kun seks måneder på å varsle tingretten. Oversitter du fristen, taper du kravet.",
        "kort_svar": "Du har seks måneder på å varsle tingretten skriftlig — enten om at du krever arv etter et testament, eller om at du mener et testament er ugyldig. Fristen løper fra du fikk vite om dødsfallet OG innholdet i testamentet.",
        "paragraftekst": "En rett etter et testament kan gjøres gjeldende bare hvis minst én av testamentsarvingene skriftlig har varslet tingretten om sitt arvekrav innen seks måneder etter at testamentsarvingen fikk vite om testators død og innholdet i testamentet. Skal en arving gjøre gjeldende at en disposisjon er ugyldig, må varslet gis innen seks måneder etter at vedkommende fikk vite at testator var død, hva disposisjonen gikk ut på, og hvorfor disposisjonen kunne være ugyldig.",
        "hva_betyr_html": """<p>To situasjoner, én frist:</p>
<p><strong>Situasjon 1 — du arver etter testamentet:</strong> Finner du et testament du er tilgodesett i, og ingen andre vet om det, har du seks måneder fra du forsto innholdet til å varsle tingretten skriftlig. Tier du stille i syv måneder, er arven tapt. Unntak: er tingretten allerede kjent med testamentet eller de vanlige arvingene vet om det, trenger du ikke varsle.</p>
<p><strong>Situasjon 2 — du vil angripe testamentet:</strong> Mener du det er ugyldig (demens, tvang, falsk)? Seks måneder fra du fant ut om dødsfallet, innholdet OG grunnen til ugyldighetspåstanden. Venter du, blir testamentet stående.</p>""",
        "eksempler": [{"navn": "Ingrid og hytta", "tekst": "Tante Berit dør i januar. Ingrid finner i mars et testament der hun skal arve familiehytta alene. Hun er den eneste som har sett det. Fristen begynner i mars — hun har frem til september. Hadde hun ventet til julaften, ville testamentet vært tapt."}],
        "vanlige_feil": ["Sende testamentet til advokaten uten at advokaten varsler tingretten", "Fortelle familien muntlig uten å sende skriftlig varsel til tingretten", "Klage over testamentet i familieselskap uten å faktisk sende skriftlig påstand til retten"],
        "hva_bor_du_html": "<p>Aldri vent. Ta kontakt med tingretten der den avdøde bodde. Gjør alt skriftlig (e-post eller brev). For ugyldighetsangrep holder det at ÉN av søsknene varsler — det fryser fristen for alle.</p>",
        "dumme_sporsmal": [
            {"q": "Jeg visste om dødsfallet, men så testamentet ett år etter. Har jeg tapt fristen?", "a": "Nei. Fristen løper fra du visste om dødsfallet OG kjente innholdet. Fant du det ett år etter, starter fristen den dagen du fant det."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "44", "tittel": "Inhabilitet hos vitner", "available": True}, {"lov": "arveloven", "paragraf": "45", "tittel": "Ugyldighet ved utnyttelse", "available": True}],
    },
    {
        "number": "66", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Når faller arven, og hvem har rett til å arve?",
        "kategori": "arv",
        "description": "Arven er juridisk delt ut i det sekundet personen dør. For å arve må du leve i det øyeblikket — men et ufødt barn som er unnfanget vernes også.",
        "kort_svar": "Arven faller akkurat idet personen dør. For å arve må du være i live i det øyeblikket. Et ufødt barn arver også, forutsatt at det er unnfanget før dødsfallet og senere fødes levende.",
        "paragraftekst": "All arv skal anses falt ved arvelaterens død, hvis ikke noe annet er bestemt i loven eller i testament. Rett til arv etter loven eller testament har bare den som lever ved arvelaterens død, og den som ved arvelaterens død er unnfanget og senere fødes levende.",
        "hva_betyr_html": """<p>I det millisekundet legen erklærer en person død, skjer «arvefallet». Det juridiske eierskapet til formuen flyttes umiddelbart over til arvingene — selv om pengene på kontoen er frosset til skiftet er ferdig.</p>
<p>Dør du to timer <em>før</em> arvelateren, får du ingenting. Dør du to timer <em>etter</em>, var du i live ved arvefallet og arven inngår i ditt eget bo.</p>
<p>Et ufødt barn er vernet: er barnet unnfanget da arvelateren dør, arver det — forutsatt at det fødes levende. Puster barnet bare noen minutter, regnes det som levende født og rekker å arve.</p>""",
        "eksempler": [{"navn": "Sara og Håkon", "tekst": "Håkon dør i bilulykke kl. 14.00. Datteren Sara fraktes til sykehus og dør kl. 18.00. Sara overlevde faren sin med fire timer, så hun levde ved arvefallet. Arven etter Håkon tilfalt Sara. Når Sara dør, går denne arven inn i Saras bo og fordeles til Saras arvinger."}],
        "vanlige_feil": ["Tro at arven regnes fra tingretten stempler papirene — den faller ved dødstidspunktet", "Glemme rettighetene til et ufødt barn og begynne å tømme kontoer"],
        "hva_bor_du_html": "<p>Sørg for at ingen overfører penger fra den avdødes kontoer rett etter dødsfallet — formuen tilhører nå alle arvingene i fellesskap. Er noen gravid med avdøde, sett skiftet på pause til barnet er født.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om en arving lå i koma da arvelateren døde?", "a": "Koma er å leve. Så lenge personen pustet og hjertet slo, er de i live ved arvefallet og arver."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "67", "tittel": "Ukjent dødsrekkefølge", "available": True}, {"lov": "arveloven", "paragraf": "68", "tittel": "Fraværende arving", "available": True}],
    },
    {
        "number": "67", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Hvem arver når to personer dør i samme ulykke?",
        "kategori": "arv",
        "description": "Dør et ektepar i samme ulykke og ingen vet hvem som døde først? Loven har en klar løsning: ingen av dem arver hverandre.",
        "kort_svar": "Dør to personer i samme ulykke og rekkefølgen er ukjent, arver ingen av dem hverandre. De behandles juridisk som om de ikke overlevde hverandre. Dør de straks etter hverandre i samme hendelse, gjelder det samme.",
        "paragraftekst": "Hvis en arving er død og det er uvisst om arvingen overlevde arvelateren, skal arvingen regnes for ikke å ha overlevd arvelateren. Hvis en arving og en arvelater dør straks etter hverandre som følge av samme hendelse, skal arvingen uansett regnes for ikke å ha overlevd arvelateren.",
        "hva_betyr_html": """<p>Når rekkefølgen er ukjent, strykes de fra hverandres arvelister. Ektefelle A arver ikke ektefelle B. I stedet går arven etter A direkte til As familie, og arven etter B til Bs familie.</p>
<p>Dør de «straks etter hverandre» i samme ulykke — for eksempel kona kl. 15.00 og mannen kl. 15.05 i ambulansen — regnes det som «samtidig» etter loven. Han arver henne ikke i de fem minuttene.</p>
<p>Finner man ut lang tid etter, via obduksjon, at den ene faktisk levde vesentlig lenger og ikke av den akutte skaden, kan familien til den overlevende kreve arven tilbake.</p>""",
        "eksempler": [{"navn": "Eva og Thomas", "tekst": "Ekteparet Eva og Thomas dør i jordskred. Ingen felles barn. Eva har datter Kari fra før, Thomas har sine foreldre. Rekkefølgen er ukjent. Loven sletter ektefellearven mellom dem. Evas formuesandel → Kari. Thomas sin formuesandel → hans foreldre."}],
        "vanlige_feil": ["Pårørende bruker store advokatbeløp på å bevise at mannen levde to minutter lenger — loven stanser dette ved regelen om «samme hendelse»", "Utbetale alt til én side før ulykken er ferdig etterforsket"],
        "hva_bor_du_html": "<p>Vent på politiets og obdusentens konklusjon. Ikke tøm kontoer. Sett dere ned begge familiene og fordel boet uavhengig av hverandre — Evas andel til hennes folk, Thomas sin til hans.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om de dør av forskjellige ting men på samme dag?", "a": "Da er rekkefølgen kjent og loven gjelder ikke. Per dør av hjerteinfarkt kl. 10, kona dør i bilulykke kl. 16 — kona arver ham i seks timer før hun dør selv."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "66", "tittel": "Arvefall og livskravet", "available": True}, {"lov": "arveloven", "paragraf": "70", "tittel": "Tilbakeføring av arv", "available": True}],
    },
    {
        "number": "68", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Fraværende arving",
        "kategori": "arv",
        "description": "Hva skjer med arven hvis en arving er forsvunnet eller ikke kan finnes? Loven beskytter den fraværende — andelen settes av og kan kreves tilbake i inntil ti år.",
        "kort_svar": "Er en arving forsvunnet og det er uvisst om vedkommende lever, regnes de foreløpig for ikke å ha overlevd. Men andelen settes av i skifteoppgjøret — ikke deles ut. Dukker de opp igjen, kan de kreve arven tilbake innen ti år.",
        "paragraftekst": "Hvis det er uvisst om en arving lever og dermed ikke sikkert at han eller hun har overlevd arvelateren, skal arvingen regnes for ikke å ha overlevd arvelateren. Hvis arvingen er forsvunnet etter arvefallet eller er fraværende uten kjent oppholdssted, skal det settes av arv til arvingen i skifteoppgjøret.",
        "hva_betyr_html": """<p>To ulike situasjoner:</p>
<p><strong>Situasjon 1 — usikkert om arvingen levde ved arvefallet:</strong> Kanskje har kontakten vært brutt i årevis. Loven antar at vedkommende ikke overlevde — arven går videre til andre. Men hvis arvingen kan bevise at de faktisk var i live, kan de kreve arven tilbake innen ti år.</p>
<p><strong>Situasjon 2 — arvingen var definitivt i live, men er borte nå:</strong> Andelen settes av i boet og venter. Du kan ikke dele ut noe som tilhører noen som bare ikke er å finne for øyeblikket.</p>""",
        "eksempler": [{"navn": "Håkon", "tekst": "Håkon og broren Lars er eneste arvinger etter moren. Lars har vært borte i åtte år — ukjent adresse. Moren dør. Lars var åpenbart i live da moren døde. Andelen til Lars settes av. Håkon kan ikke ta alt. Pengene venter."}],
        "vanlige_feil": ["Anta at en forsvunnet arving automatisk mister arven sin", "Dele ut all arv selv om én arving er utilgjengelig"],
        "hva_bor_du_html": "<p>Vet du at en medarving er forsvunnet, ta det opp med tingretten tidlig. Arven skal settes av etter §§ 125 og 146 — ikke fordeles blant de andre.</p>",
        "dumme_sporsmal": [
            {"q": "Kan vi dele ut arven hvis vi ikke klarer å finne en arving?", "a": "Nei — andelen settes av og venter. Først hvis ti-årsfristen løper ut uten at arvingen har meldt seg, kan situasjonen vurderes på nytt."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "67", "tittel": "Ukjent dødsrekkefølge", "available": True}, {"lov": "arveloven", "paragraf": "69", "tittel": "Forbigått arving", "available": True}],
    },
    {
        "number": "69", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Forbigått arving",
        "kategori": "arv",
        "description": "Ble du glemt eller oversett i arveoppgjøret? Du har rett til å kreve din del tilbake innen ti år — selv om skiftet er avsluttet.",
        "kort_svar": "Er du utelatt fra arveoppgjøret uten at det er din skyld, har du rett til å kreve det du skulle hatt. Fristen er ti år fra arvelateren døde. Du krever pengene fra dem som fikk for mye.",
        "paragraftekst": "Hvis en arving med urette er forbigått ved skiftet eller har fått for liten del av arven, kan arvingen innen foreldelsesfristen i § 71 kreve arven fra dem som har mottatt den, etter reglene i § 70.",
        "hva_betyr_html": """<p>«Forbigått» betyr oversett, glemt eller urettmessig holdt utenfor. Det spiller ingen rolle om de andre allerede har fått pengene sine, brukt dem, eller fordelt dem videre. Er du arving og fikk for lite, kan du kreve differansen.</p>
<p>Du er forbigått «med urette» hvis oppgjøret ikke fulgte loven eller testamentet. Eksempler: et barn ble ikke kjent som arving i tide, et testament ble mistolket, noen lot være å varsle deg om skiftet.</p>
<p>Er du derimot utelatt fordi et lovlig testament utelukket deg, er du ikke forbigått med urette.</p>""",
        "eksempler": [{"navn": "Sofie", "tekst": "Morten dør med tre barn. De to eldste gjennomfører privat skifte uten å varsle Sofie som bodde i utlandet. Sofie finner ut to år etter. Hun har rett til sin tredjedel og kan kreve den fra søsknene innen ti år fra Morten døde."}],
        "vanlige_feil": ["Vente for lenge — ti-årsfristen løper fra dødsfallet, ikke fra du oppdaget feilen", "Tro at et avsluttet skifte er endelig og ikke kan angripes"],
        "hva_bor_du_html": "<p>Mistenker du at du er forbigått: ta kontakt med tingretten og spør om boet. Send et skriftlig krav til dem som mottok arv, og meld kravet til tingretten for å stoppe foreldelsesfristen.</p>",
        "dumme_sporsmal": [
            {"q": "Gjelder dette også hvis jeg fikk litt, bare for lite?", "a": "Ja. «Har fått for liten del» er eksplisitt nevnt i paragrafen. Du kan kreve differansen."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "70", "tittel": "Tilbakeføring av arv", "available": True}, {"lov": "arveloven", "paragraf": "71", "tittel": "Foreldelse av arverett", "available": True}],
    },
    {
        "number": "70", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Krav om tilbakeføring av arv",
        "kategori": "arv",
        "description": "Hvem betaler tilbake når arven er feilfordelt? Loven fordeler ansvaret mellom arvingene — og straffer den som visste at noen ble forbigått.",
        "kort_svar": "Har noen fått for mye arv, hefter de i forhold til hva de fikk. Den som visste at en arving ble forbigått, hefter solidarisk — for hele beløpet alene. Er arven brukt i god tro, kan kravet settes ned.",
        "paragraftekst": "De arvingene som har mottatt for mye i arv, er ansvarlige i samme forhold som deres andel av arven. Arvinger som kjente eller burde kjenne til at noen var forbigått, har solidarisk ansvar. Gjelder kravet arv som er avhendet eller forbrukt, er arvingen ansvarlig for arvens verdi på avhendelses- eller forbrukstidspunktet. Kravet kan settes ned eller falle bort når det etter forholdene ville være urimelig å svare fullt ut for midler som ikke lenger er i behold.",
        "hva_betyr_html": """<p><strong>Normal situasjon:</strong> Fikk du dobbelt så mye som en medarving, hefter du for dobbelt så mye av det forbigåtte beløpet. Forholdsmessig ansvar.</p>
<p><strong>Kjente til forbigåelsen:</strong> Da hefter du solidarisk for hele beløpet. Den forbigåtte kan kreve alt av deg, og du må selv inndrive fra de andre.</p>
<p><strong>Pengene er brukt:</strong> Du hefter for verdien da du brukte dem — ikke mer enn tilsvarende ting er verdt i dag. Brukte du dem i god tro og det ville være urimelig å kreve dem tilbake, kan kravet settes ned eller falle bort.</p>""",
        "eksempler": [{"navn": "Lars og Ingrid", "tekst": "Moren dør. Ingrid og Lars arver 600 000 kr (300 000 kr hver). Søsteren Eva var bortreist og ikke varslet. Eva krever sin tredjedel (200 000 kr). Lars visste ikke om Eva → hefter for sin andel: 100 000 kr. Ingrid visste om Eva → solidaransvar for hele 200 000 kr."}],
        "vanlige_feil": ["Tro at du slipper unna fordi pengene er brukt — god tro kan gi lavere krav, men sletter det ikke automatisk", "Selge videre en arvet gjenstand uten å sjekke om alle arvinger er med"],
        "hva_bor_du_html": "<p>Finner du ut at noen var forbigått: ta det opp umiddelbart med de andre arvingene eller tingretten. Jo lenger du venter, desto vanskeligere blir oppgjøret.</p>",
        "dumme_sporsmal": [
            {"q": "Hva betyr «solidarisk ansvar»?", "a": "Den forbigåtte kan velge hvem de vil rette kravet mot og kreve hele beløpet av én person. Den personen må selv inndrive fra de andre."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "69", "tittel": "Forbigått arving", "available": True}, {"lov": "arveloven", "paragraf": "71", "tittel": "Foreldelse av arverett", "available": True}],
    },
    {
        "number": "71", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Foreldelse av arverett",
        "kategori": "arv",
        "description": "Hvor lenge kan du vente med å kreve arv? Hovedregelen er ti år fra dødsfallet — men det finnes viktige unntak som kan forlenge fristen.",
        "kort_svar": "Du har normalt ti år fra arvelateren døde til å gjøre arvekravet gjeldende. Er boet under offentlig skifte, løper ingen frist. Sitter gjenlevende ektefelle i uskifte, begynner fristen først når vedkommende dør.",
        "paragraftekst": "Retten til å kreve arv foreldes når den ikke er gjort gjeldende innen ti år etter at arvelateren døde. Foreldelse hindres ved å melde kravet til tingretten, kreve offentlig skifte, eller reise søksmål. Krav på arv foreldes ikke så lenge boet er under offentlig skifte. Er boet overtatt av ektefelle eller samboer i uskifte, løper fristen først fra ektefellens eller samboerens død.",
        "hva_betyr_html": """<p><strong>Hovedregelen:</strong> Ti år fra dødsdatoen. Gjør du ikke kravet gjeldende i tide, er det foreldet — uansett om du opprinnelig hadde rett.</p>
<p><strong>Slik stopper du fristen:</strong> Meld kravet til tingretten. Krev offentlig skifte. Saksøk dem som har mottatt arven. Alternativt: de andre arvingene godkjenner kravet ditt skriftlig.</p>
<p><strong>Unntak:</strong> Er boet under offentlig skifte løper ingen frist. Sitter gjenlevende i uskifte, begynner fristen først ved uskiftets avslutning.</p>""",
        "eksempler": [{"navn": "Marius", "tekst": "Faren dør i 2015. Marius visste ikke om arven før i 2023. Fristen begynte i 2015 og løper ut i 2025. Marius melder kravet til tingretten i 2024 — fristen er avbrutt. Ventet han til 2026 ville kravet vært foreldet."}],
        "vanlige_feil": ["Tro at fristen starter fra du hørte om dødsfallet — den starter fra selve dødsdatoen", "Glemme at godkjenning fra de andre arvingene avbryter fristen"],
        "hva_bor_du_html": "<p>Er du usikker på om du har krav på arv: meld kravet til tingretten så snart som mulig. Det koster lite og stopper fristen. Vent ikke til du har full oversikt.</p>",
        "dumme_sporsmal": [
            {"q": "Løper fristen selv om jeg ikke visste om dødsfallet?", "a": "Ja, som hovedregel. Fristen løper fra dødsdatoen uavhengig av hva du visste."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "69", "tittel": "Forbigått arving", "available": True}, {"lov": "arveloven", "paragraf": "72", "tittel": "Fradømmelse av arverett", "available": True}],
    },
    {
        "number": "72", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Fradømmelse av arverett",
        "kategori": "arv",
        "description": "Kan du miste arveretten etter å ha begått en straffbar handling mot den du skal arve? Ja — domstolen kan fradømme deg arveretten helt eller delvis.",
        "kort_svar": "Er du dømt for en straffbar handling mot arvelateren, og arvelateren dør eller mister testasjonsevnen på grunn av handlingen, kan retten fradømme deg arveretten. Det krever en egen dom — det skjer ikke automatisk.",
        "paragraftekst": "Blir noen dømt for en straffbar handling mot den han eller hun skulle arve, og arvelateren dør eller mister testasjonsevnen på grunn av handlingen, kan gjerningspersonen helt eller delvis fradømmes retten til arv og uskifte. Gjelder også hvis dommen går ut på utilregnelighet. Avgjørelse treffes ved dom. Blir noen fradømt retten til arv, skal arven gå som om vedkommende var død før arven falt. Reglene er ikke til hinder for at arveretten blir gitt tilbake ved testament stadfestet av Kongen.",
        "hva_betyr_html": """<p>Tre situasjoner som kan føre til tap av arverett:</p>
<p><strong>1.</strong> Straffbar handling mot arvelateren selv som fører til dødsfallet eller tap av testasjonsevne.<br>
<strong>2.</strong> Straffbar handling mot en medarving som dør — du arver mer enn du ellers ville, og kan fradømmes retten.<br>
<strong>3.</strong> Handling som fører til at et unnfanget barn ikke fødes levende — barnet ville hatt minst like god arverett.</p>
<p>Gjelder også ved utilregnelighet — selv om du ikke kan straffes, kan arveretten fradømmes. Hvem som helst som ville arve mer om kravet tas til følge, kan fremme sak.</p>""",
        "eksempler": [{"navn": "Per", "tekst": "Per er straffedømt for grov vold mot sin far, som dør av skadene. De øvrige arvingene krever at Per fradømmes arveretten. Retten tar kravet til følge. Pers andel går videre til hans egne barn."}],
        "vanlige_feil": ["Tro at fradømmelse skjer automatisk ved domfellelse — det krever en egen dom om arverettstap", "Tro at arveretten er tapt for alltid — den kan gjenopprettes ved kongelig stadfestet testament"],
        "hva_bor_du_html": "<p>Er du pårørende og mener en medarving bør fradømmes arveretten: fremme krav overfor tingretten, enten i pågående straffesak eller i separat sak. Kontakt advokat — prosessen krever solid dokumentasjon.</p>",
        "dumme_sporsmal": [
            {"q": "Hva skjer med arven til barna mine hvis jeg mister arveretten?", "a": "Arven går som om du var død. Dine livsarvinger (barna dine) trer inn i din plass."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "55", "tittel": "Gjøre livsarving arveløs", "available": True}, {"lov": "arveloven", "paragraf": "71", "tittel": "Foreldelse av arverett", "available": True}],
    },
    {
        "number": "73", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Arvingens råderett over fremtidig og falt arv",
        "kategori": "arv",
        "description": "Kan du selge eller pantsette arv du ikke har fått ennå? Nei — fremtidig arv kan du ikke råde over. Men arv som allerede er falt er din å disponere.",
        "kort_svar": "Du kan ikke selge, pantsette eller disponere over fremtidig arv. Det er ulovlig — arven tilhører arvelateren så lenge de lever. Etter dødsfallet er falt arv din å råde over, men skifterettighetene kan du ikke overdra til andre.",
        "paragraftekst": "En avtale om å selge, pantsette eller foreta andre disposisjoner over fremtidig arv er ikke gyldig uten særskilt hjemmel i lov. Med fremtidig arv menes også retten til arv når arvelaterens ektefelle eller samboer sitter i uskifte. Etter arvefallet kan arvingen rå over arven. Arvingen kan likevel ikke overføre de rettighetene som tilkommer en arving under skiftet, på annen måte enn ved å gi avkall på arven. Arvingens kreditorer kan ta utleggspant i falt arv, men ikke i fremtidig arv.",
        "hva_betyr_html": """<p><strong>Fremtidig arv (arvelateren lever):</strong> Du eier ingenting ennå. Lån med fremtidig arv som sikkerhet? Ugyldig. Salg til søsken? Ugyldig. Gaveoverføring? Ugyldig. Arvingene kan derimot godt avtale seg imellom hvem som ønsker hytta og hvem som vil ha bilen — men avtalen binder bare dem, ikke arvelateren.</p>
<p><strong>Falt arv (arvelateren er død):</strong> Gjør som du vil med din andel — selg, gi bort, bruk. Men selve skifterettighetene (retten til å delta i oppgjøret) kan du ikke overdra til andre. Vil du ut av skiftet, er eneste vei å gi avkall (§ 74).</p>""",
        "eksempler": [{"navn": "Thomas", "tekst": "Thomas prøver å bruke fremtidig arv etter faren som sikkerhet for lån. Banken kan ikke ta det pantet. Avtalen er ugyldig — faren lever og arven er ikke Thomas sin ennå."}],
        "vanlige_feil": ["Tro at en muntlig avtale om fremtidig arv er bindende — den er ikke det", "Tro at kreditorer kan ta pant i fremtidig arv — det kan de ikke"],
        "hva_bor_du_html": "<p>Trenger du penger og venter på arv: vent. Ingen lovlig snarvei finnes. Har arven falt, er du fri til å disponere over din andel — men helst etter at skiftet er avsluttet og beløpet er avklart.</p>",
        "dumme_sporsmal": [
            {"q": "Hva hvis jeg har signert en ulovlig avtale om fremtidig arv?", "a": "Avtalen er ugyldig. Den andre parten kan ikke kreve oppfyllelse. Du er ikke bundet."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "74", "tittel": "Avkall på arv", "available": True}, {"lov": "arveloven", "paragraf": "75", "tittel": "Avkorting i arv", "available": True}],
    },
    {
        "number": "74", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Avkall på arv",
        "kategori": "arv",
        "description": "Kan du si fra deg arv du har krav på? Ja — enten før eller etter arvelateren dør. Avkall behandler deg som om du var død, og andelen går til dine egne arvinger.",
        "kort_svar": "Du kan gi avkall på arv — enten mens arvelateren lever (til arvelateren) eller etter dødsfallet (til boet). Gir du avkall, arver du ingenting. Andelen din går videre som om du var død før arvelateren.",
        "paragraftekst": "En arving kan gi helt eller delvis avkall på fremtidig eller falt arv. Arv som det er gitt avkall på, fordeles som om arvingen var død før arvelateren. En ektefelle eller samboer kan gi avkall på retten til uskifte. Avkall på fremtidig arv gis overfor arvelateren. Avkall på falt arv gis overfor dødsboet.",
        "hva_betyr_html": """<p>Et frivillig nei til arven din. Loven godtar det og behandler deg som om du aldri var i bildet.</p>
<p><strong>Andelen din:</strong> Går videre til dem som ville arvet etter deg. Er du barn av arvelateren og barnløs, går andelen til andre arvinger — ikke til søsknene dine.</p>
<p><strong>Mens arvelateren lever:</strong> Gi avkallet direkte til arvelateren. Ingen spesielle formkrav, men skriftlighet er sterkt anbefalt.</p>
<p><strong>Etter dødsfallet:</strong> Gi avkallet til boet. Du kan gi delvis avkall — ta halvparten og fraskrive deg resten.</p>""",
        "eksempler": [{"navn": "Kari og Anne", "tekst": "Søstrene Kari og Anne arver moren. Kari mottok et stort beløp fra moren mens hun levde og gir avkall på sin del av arven. Andelen hennes går til Karis barn — ikke til Anne. Anne arver ikke Karis del."}],
        "vanlige_feil": ["Tro at avkallet frigjør andelen til søsknene — den går til dine egne barn, ikke til søsknene", "Gi avkall muntlig og tro det holder — skriftlighet er avgjørende ved tvist"],
        "hva_bor_du_html": "<p>Tenk gjennom hvem som arver i ditt sted. Er du barnløs, kan andelen gå til fjerne slektninger du ikke kjenner. Skriv avkallet skriftlig og lever til riktig mottaker.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg ombestemme meg etter å ha gitt avkall?", "a": "Nei, som hovedregel. Avkall er endelig. Svært snevre unntak finnes ved ugyldige avkall — men det krever rettssak."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "73", "tittel": "Råderett over fremtidig og falt arv", "available": True}, {"lov": "arveloven", "paragraf": "75", "tittel": "Avkorting i arv", "available": True}],
    },
    {
        "number": "75", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Avkorting i arv",
        "kategori": "arv",
        "description": "Kan en gave fra foreldrene trekkes fra i arven din? Ja — men bare hvis avkorting var en uttrykkelig betingelse da du mottok ytelsen.",
        "kort_svar": "Har du fått en større gave fra arvelateren, kan den trekkes fra i arven din — men bare hvis avkorting var en uttrykkelig betingelse da du mottok gaven. Uten slik betingelse er gaven din og det skjer ingen avkorting.",
        "paragraftekst": "Har en livsarving mottatt en ytelse av økonomisk verdi fra arvelateren, skal ytelsen avkortes i livsarvingens arv hvis dette var satt som en betingelse for ytelsen. En betingelse om avkorting bør være skriftlig og gjort kjent for de andre livsarvingene. Avkortingsbeløpet settes til verdien av ytelsen da den ble mottatt. Avkorting kan aldri tvinge arvingen til å tilbakeføre noe til boet.",
        "hva_betyr_html": """<p>Avkorting betyr at en gave du fikk mens arvelateren levde trekkes fra din arvelodd — tanken er «forskudd på arv» som skal jevne seg ut mellom søsknene.</p>
<p>Det er <strong>ikke nok at foreldrene hadde slike tanker</strong>. Det må ha vært en uttrykkelig betingelse da ytelsen ble gitt — og loven sier den bør være skriftlig. Uten skriftlig dokumentasjon er betingelsen i praksis umulig å bevise.</p>
<p>Beløpet settes til verdien <em>da du fikk den</em> — ikke dagens verdi. Fikk du leilighet til 1 million i 2005 (nå verdt 4 mill), er avkortingsbeløpet 1 million. Avkorting kan aldri tvinge deg til å betale tilbake til boet — worst case er at du arver ingenting.</p>""",
        "eksempler": [{"navn": "Ola og Jonas", "tekst": "Foreldrene gir Jonas 500 000 kr med skriftlig betingelse om avkorting. Boet er 1,5 mill, to arvinger. Uten avkorting: 750 000 kr til hver. Med avkorting: Jonas' lodd reduseres med 500 000 kr. Jonas arver 250 000 kr. Ola arver 750 000 kr. Totalt har Jonas fått 750 000 kr — samme som Ola."}],
        "vanlige_feil": ["Tro at alle gaver automatisk avkortes — de gjør det ikke uten betingelse", "Gi bort store summer uten å skrive ned hva som er ment"],
        "hva_bor_du_html": "<p>Gir du bort noe med mening om avkorting: skriv det ned, dater det, og gjør det kjent for de andre livsarvingene. Uten dokumentasjon er betingelsen din ord mot de andres.</p>",
        "dumme_sporsmal": [
            {"q": "Kan foreldrene bestemme avkorting etter at de har gitt gaven?", "a": "Nei — betingelsen må ha vært satt da ytelsen ble gitt. En etterpå-erklæring holder ikke."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "74", "tittel": "Avkall på arv", "available": True}, {"lov": "arveloven", "paragraf": "50", "tittel": "Pliktdelsarven", "available": True}],
    },
    {
        "number": "76", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Ingen arvinger — formuen går til frivillig virksomhet for barn og unge",
        "kategori": "arv",
        "description": "Hva skjer med arven hvis den avdøde ikke har noen arvinger? Pengene går ikke til staten — de går til frivillig virksomhet for barn og unge.",
        "kort_svar": "Har den avdøde ingen arvinger etter loven og ingen testamentsarvinger, går nettoformuen til frivillig virksomhet for barn og unge. I særlige tilfeller kan nære slektninger eller venner søke departementet om å få hele eller deler av formuen.",
        "paragraftekst": "Hvis den avdøde ikke har arvinger etter loven eller etter testament, skal nettoformuen gå til frivillig virksomhet til fordel for barn og unge. I særlige tilfeller kan departementet etter søknad bestemme at hele eller deler av formuen skal gå til slektninger eller andre som har stått den avdøde nær.",
        "hva_betyr_html": """<p>Formuen går ikke til staten som en slags skatt. Den kanaliseres til frivillige organisasjoner — idrettslag, kulturorganisasjoner og lignende — som jobber for barn og unge.</p>
<p>Arveretten stopper ved tredje arvegangsklasse. Har du ingen livsarvinger, ektefelle, foreldre, søsken eller søskenbarn, har ingen lovlig arverett etter deg.</p>
<p><strong>Unntaket:</strong> Nære slektninger eller venner som stod deg nær kan søke departementet om å få formuen. Det er ikke en rettighet, men en mulighet i særlige tilfeller. Terskelen er høy.</p>""",
        "eksempler": [{"navn": "Eva", "tekst": "Eva er enslig, barnløs og uten søsken. Foreldrene er døde og ingen slektninger innen tredje arvegangsklasse lever lenger. Uten testament går hele formuen til frivillig virksomhet for barn og unge. Evas venninne Mette søker departementet om å få en del — men ingen garanti for at det innvilges."}],
        "vanlige_feil": ["Tro at staten tar pengene som skatt — det gjør den ikke", "Tro at fjerne slektninger automatisk arver — arveretten stopper ved tredje arvegangsklasse"],
        "hva_bor_du_html": "<p>Er du uten livsarvinger, ektefelle og nær slekt: opprett testament. Uten testament mister du all kontroll. Vil du støtte en bestemt venn, organisasjon eller formål — testament er det eneste sikre verktøyet.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg testamentere alt til venner?", "a": "Ja — er du uten livsarvinger, har du i utgangspunktet full frihet til å testamentere til hvem du vil, inkludert venner, naboer eller organisasjoner."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "77", "tittel": "Avgjørelser ved skifte uten arvinger", "available": True}, {"lov": "arveloven", "paragraf": "4", "tittel": "Første arvegangsklasse", "available": True}],
    },
    {
        "number": "77", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Avgjørelser ved skiftet når ingen arvinger finnes",
        "kategori": "arv",
        "description": "Hvem tar avgjørelsene i et dødsbo når den avdøde ikke har arvinger? Det er departementet — ikke tingretten og ikke arvingene.",
        "kort_svar": "Når det er fastslått at den avdøde ikke har arvinger, overtar departementet rollen som «arving» under skiftet. Departementet sørger for at begravelsen og bobehandlingen er betalt, og at det settes av penger til stell av graven.",
        "paragraftekst": "Når det er slått fast at den avdøde ikke har arvinger, treffer departementet de avgjørelsene under skiftet som ellers treffes av arvingene, slik som avgjørelser om salg av eiendeler. Departementet skal påse at utgiftene til bobehandling og gravferd blir dekket, og at det blir satt av midler til fremtidige utgifter til stell av graven.",
        "hva_betyr_html": """<p>Uten arvinger er det ingen til å ta avgjørelsene i et bo — hvem tar hva, hva selges, hva beholdes. Da fyller departementet denne rollen.</p>
<p>Departementet (eller den instansen de utpeker) tar stilling til salg av eiendeler, disponering av bankinnskudd og alle andre beslutninger for å avslutte boet.</p>
<p>To konkrete krav: utgifter til gravferd og bobehandling skal dekkes, og det skal settes av midler til fremtidig stell av graven. Den avdøde får en verdig avslutning, selv uten familie.</p>""",
        "eksempler": [{"navn": "Arne", "tekst": "Arne er barnløs og hans eneste slekt — en bror — døde for ti år siden. Arne har ikke opprettet testament. Tingretten fastslår at det ikke finnes arvinger. Departementet overtar skifteoppgavene: leiligheten selges, gravferden betales, og det settes av midler til gravstell."}],
        "vanlige_feil": ["Tro at tingretten tar alle avgjørelsene — skiftemyndigheten behandler boet formelt, men departementet har arvingerollen"],
        "hva_bor_du_html": "<p>Er du nærstående til noen som er død uten arvinger og vil bidra til gravferden eller gravstell: ta kontakt med tingretten tidlig. De kan veilede og eventuelt utpeke deg til å bistå.</p>",
        "dumme_sporsmal": [
            {"q": "Hvem betaler begravelsen hvis den avdøde ikke har penger?", "a": "Boet dekker begravelsesutgiftene først. Er boet tomt, er det egne regler i kommunehelselovgivningen om hvem som har ansvar."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "76", "tittel": "Ingen arvinger", "available": True}],
    },
    {
        "number": "78", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Lovvalg i internasjonale arveforhold",
        "kategori": "arv",
        "description": "Hvilken stats arvelov gjelder når den avdøde bodde i utlandet? Hovedregelen er at landet der vedkommende bodde ved dødsfallet avgjør dette.",
        "kort_svar": "Bodde den avdøde i et annet land da han eller hun døde, er det som regel det landets arvelov som gjelder — ikke norsk arvelov. Dette gjelder selv om den avdøde var norsk statsborger.",
        "paragraftekst": "Hvis ikke noe annet følger av overenskomst etter § 82, skal arveretten i den staten der arvelateren ved sin død hadde sitt vanlige bosted, anvendes.",
        "hva_betyr_html": """<p>Arverett er knyttet til <em>bosted</em>, ikke statsborgerskap. En norsk statsborger som bodde i Spania, er underlagt spansk arverett. En dansk statsborger som bodde i Norge, er underlagt norsk arverett.</p>
<p>«Vanlig bosted» betyr der du faktisk bodde fast — ikke feriested, ikke midlertidig opphold.</p>
<p>Viktig unntak: den nordiske arvekonvensjonen mellom Norge, Danmark, Finland, Island og Sverige kan gi andre regler enn det som følger av bostedet alene (se § 82).</p>""",
        "eksempler": [{"navn": "Ingrid", "tekst": "Ingrid er norsk statsborger, men har bodd fast i Portugal i 15 år. Da hun dør, er det portugisisk arvelov som gjelder. Barna hennes må forholde seg til portugisiske regler om pliktdelsarv og skiftebehandling."}],
        "vanlige_feil": ["Tro at norsk statsborger alltid arves etter norsk lov — det stemmer ikke", "Glemme å undersøke om det finnes en bilateral avtale mellom landene"],
        "hva_bor_du_html": "<p>Bor du i utlandet og er norsk statsborger: undersøk arveretten i landet du bor i. Ønsker du norsk arvelov å gjelde, kan du foreta lovvalg etter § 79 — men det krever testament.</p>",
        "dumme_sporsmal": [
            {"q": "Hva er den nordiske arvekonvensjonen?", "a": "En avtale mellom de nordiske landene om hvilken stats rett som gjelder og hvem som har kompetanse til å skifte boet når avdøde hadde tilknytning til flere nordiske land."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "79", "tittel": "Arvelaterens lovvalg", "available": True}, {"lov": "arveloven", "paragraf": "82", "tittel": "Overenskomst med fremmed stat", "available": True}],
    },
    {
        "number": "79", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Arvelaterens adgang til å foreta lovvalg",
        "kategori": "arv",
        "description": "Kan du bestemme hvilken stats arvelov skal gjelde etter deg? Ja — men bare hvis du ikke er norsk statsborger ved dødsfallet.",
        "kort_svar": "Du kan ved testament bestemme at arven skal fordeles etter arveloven i et land der du er eller har vært statsborger. Men er du norsk statsborger da du dør, er lovvalget ugyldig — norsk lov gjelder uansett.",
        "paragraftekst": "En arvelater kan bestemme at retten til arv etter ham eller henne skal avgjøres etter arveretten i den staten der han eller hun er eller har vært statsborger. Et slikt lovvalg er likevel ikke gyldig hvis arvelateren er norsk statsborger ved dødsfallet. Lovvalget skal være uttrykkelig og i testaments form. En ektefelles arverettigheter kan begrenses ved lovvalg bare hvis han eller hun har fått kunnskap om lovvalget før arvelaterens død.",
        "hva_betyr_html": """<p><strong>Hvem kan foreta lovvalg:</strong> Bare den som ikke er norsk statsborger ved dødsfallet. En tysk statsborger bosatt i Norge kan velge tysk arvelov. En norsk statsborger bosatt i Tyskland kan ikke velge tysk arvelov.</p>
<p><strong>Lovvalget må være i testaments form:</strong> Skriftlig, datert, underskrevet og bevitnet etter §§ 40-46. Muntlig eller i brev er ugyldig.</p>
<p><strong>Ektefellen må varsles:</strong> Et lovvalg kan ikke begrense ektefellens/samboerens arverettigheter uten at de har fått kunnskap om det før dødsfallet.</p>""",
        "eksempler": [{"navn": "Thomas", "tekst": "Thomas er tysk statsborger, bosatt i Norge i 20 år. Vil at tysk arvelov skal gjelde. Oppretter testament med uttrykkelig lovvalg og varsler sin norske ektefelle. Lovvalget er gyldig."}],
        "vanlige_feil": ["Tro at norske statsborgere kan velge bort norsk lov — det kan de ikke", "Gjøre lovvalget muntlig eller i et vanlig brev — det er ugyldig"],
        "hva_bor_du_html": "<p>Er du utenlandsk statsborger bosatt i Norge og ønsker å bruke lovvalgsadgangen: kontakt advokat med kompetanse på internasjonal privatrett. Dette er et komplekst område der feil formulering kan gi uønskede resultater.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg velge arveloven til et land jeg er statsborger i, men aldri har bodd i?", "a": "Ja — loven sier «er eller har vært statsborger». Tidligere statsborgerskap gir grunnlag for lovvalg."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "78", "tittel": "Lovvalg (utgangspunktet)", "available": True}, {"lov": "arveloven", "paragraf": "80", "tittel": "Formkrav for testamenter i utlandet", "available": True}],
    },
    {
        "number": "80", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Formkrav for testamenter opprettet i utlandet",
        "kategori": "arv",
        "description": "Er et testament opprettet i utlandet gyldig i Norge? Ja — hvis det oppfylte formkravene der det ble til, der du bodde, eller der du er statsborger.",
        "kort_svar": "Et utenlandsk testament trenger ikke følge norske formkrav for å være gyldig i Norge. Det holder at testamentet oppfylte formkravene i landet der det ble opprettet, der du bodde, eller der du var statsborger.",
        "paragraftekst": "Selv om et testament ikke oppfyller formkravene i kapittel 7, er det likevel formgyldig hvis det oppfyller formkravene: a. der testamentet ble opprettet, b. i en stat der testatoren var statsborger ved dødsfallet eller ved opprettelsen, c. der testatoren hadde domisil eller vanlig bosted ved dødsfallet eller opprettelsen, eller d. der fast eiendom ligger, for så vidt testamentet gjelder den eiendommen.",
        "hva_betyr_html": """<p>Norge aksepterer at folk har ulike måter å opprette testament på i forskjellige land. Et testament trenger ikke vitner hvis landet der det ble skrevet ikke krever det.</p>
<p>Fire alternative tilkoblingspunkter — det holder at <em>ett</em> av dem er oppfylt:</p>
<p>1. Der testamentet ble laget.<br>
2. Der du var statsborger — da du laget det eller da du døde.<br>
3. Der du bodde — da du laget det eller da du døde.<br>
4. Der en fast eiendom ligger, hvis testamentet gjelder den eiendommen.</p>""",
        "eksempler": [{"navn": "Sara", "tekst": "Sara er norsk statsborger og oppretter testament i Frankrike der hun bor midlertidig. Følger franske formkrav — notarialbekreftet, ingen vitner. Dør i Norge. Testamentet er gyldig fordi det oppfylte formkravene der det ble opprettet (Frankrike)."}],
        "vanlige_feil": ["Tro at testamenter fra utlandet alltid er ugyldige i Norge", "Tro at testamentet automatisk er gyldig bare fordi det er fra utlandet — ett av fire kriterier må oppfylles"],
        "hva_bor_du_html": "<p>Har du opprettet testament i utlandet og er usikker på om det gjelder i Norge: sjekk om det oppfylte formkravene der det ble laget, der du var statsborger, eller der du bodde. Er du usikker, vurder nytt testament i Norge etter §§ 40-46.</p>",
        "dumme_sporsmal": [
            {"q": "Kan et muntlig testament fra utlandet være gyldig i Norge?", "a": "Ja — hvis landet der det ble gitt tillater muntlige testamenter. Det er formkravene der og da som er avgjørende."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "42", "tittel": "Formkrav (norske krav)", "available": True}, {"lov": "arveloven", "paragraf": "79", "tittel": "Arvelaterens lovvalg", "available": True}],
    },
    {
        "number": "81", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Grunnleggende rettsprinsipper (ordre public)",
        "kategori": "arv",
        "description": "Kan utenlandsk arvelov alltid brukes i Norge? Nei — regler fra andre land som bryter med grunnleggende norske prinsipper, settes til side.",
        "kort_svar": "Selv om utenlandsk arvelov i utgangspunktet gjelder, vil norske domstoler ikke anvende den hvis resultatet er uforenlig med grunnleggende norske rettsprinsipper. Dette kalles ordre public.",
        "paragraftekst": "En regel i fremmed rett har virkning i Norge bare så langt den ikke leder til et resultat som er uforenlig med grunnleggende prinsipper i norsk rett.",
        "hva_betyr_html": """<p>Ordre public er en sikkerhetsventil. Bruken av utenlandsk rett gjelder — men ikke ubegrenset. Fører den til et resultat som er for langt fra norske grunnverdier, setter norske domstoler regelen til side.</p>
<p>Typiske eksempler: regler som diskriminerer basert på kjønn, religion eller etnisitet ved arvefordelingen. Regler som fratar et barn all arverett uten lovlig begrunnelse.</p>
<p>Terskelen er <em>høy</em>. At utenlandsk rett er annerledes enn norsk, er ikke nok. Det kreves at resultatet i den konkrete saken er direkte uforenlig med noe grunnleggende.</p>""",
        "eksempler": [{"navn": "Petter", "tekst": "Petter er statsborger i et land der sønner arver dobbelt så mye som døtre. Han bor og dør i Norge. Den konkrete diskrimineringsregelen kan settes til side som uforenlig med likestillingsprinsippet i norsk rett."}],
        "vanlige_feil": ["Tro at alle utenlandske arverettslige regler automatisk settes til side — terskelen er høy", "Tro at ordre public er et verktøy enkeltpersoner kan aktivere — det er en sikkerhetsventil for domstoler"],
        "hva_bor_du_html": "<p>Ordre public aktiveres av domstolene, ikke enkeltpersoner. Mistenker du at utenlandsk rett gir et grunnleggende urettferdig resultat: ta det opp med tingretten i forbindelse med skiftet.</p>",
        "dumme_sporsmal": [
            {"q": "Hvem avgjør hva som er «grunnleggende prinsipper»?", "a": "Det er domstolene som avgjør dette i den konkrete saken. Det er en skjønnsmessig vurdering."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "78", "tittel": "Lovvalg", "available": True}, {"lov": "arveloven", "paragraf": "82", "tittel": "Overenskomst med fremmed stat", "available": True}],
    },
    {
        "number": "82", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Overenskomst med fremmed stat",
        "kategori": "arv",
        "description": "Kan Norge inngå særlige avtaler med andre land om arv og skifte? Ja — og slike avtaler kan gå foran arvelovens vanlige regler.",
        "kort_svar": "Norge kan inngå internasjonale avtaler om arv og skifte med andre stater. Slike avtaler kan fravike arvelovens vanlige regler. Den viktigste er den nordiske arvekonvensjonen mellom Norge, Danmark, Finland, Island og Sverige.",
        "paragraftekst": "Det kan i overenskomst med fremmed stat fastsettes internasjonal-privatrettslige regler på arve- og skifterettens område. Når Norge har inngått en slik overenskomst, kan Kongen kunngjøre den som gjeldende med lovs kraft her i riket.",
        "hva_betyr_html": """<p>Paragrafen gir hjemmel for at internasjonale avtaler om arv kan ha samme virkning som norsk lov. Uten denne bestemmelsen ville slike avtaler ikke hatt lovs kraft i Norge.</p>
<p>Den nordiske arvekonvensjonen fra 1934 er det praktisk viktigste eksempelet. Den regulerer hvilket land som skifter boet og hvilken lov som gjelder når avdøde hadde tilknytning til flere nordiske land — og svaret kan bli annerledes enn det §§ 78-79 gir alene.</p>""",
        "eksempler": [{"navn": "", "tekst": "En norsk statsborger dør i Danmark. Den nordiske arvekonvensjonen kan regulere om norsk eller dansk rett gjelder — og svaret kan overraske deg hvis du bare leser §§ 78-79 isolert."}],
        "vanlige_feil": ["Tro at arvelovens regler alltid gjelder fullt ut for nordiske borgere — den nordiske konvensjonen kan gi andre resultater", "Glemme å undersøke om det finnes en relevant overenskomst i internasjonale arveforhold"],
        "hva_bor_du_html": "<p>Har du nær tilknytning til et annet land gjennom statsborgerskap, bosted, formue eller familie: undersøk om Norge har en arveoverenskomst med det landet. For nordiske land er det særlig aktuelt. Kontakt tingretten eller en advokat med internasjonal erfaring.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg si at overenskomsten ikke gjelder for meg?", "a": "Nei — overenskomster som er kunngjort med lovs kraft gjelder etter sin ordlyd. Du kan ikke velge dem bort."},
        ],
        "related": [{"lov": "arveloven", "paragraf": "78", "tittel": "Lovvalg", "available": True}, {"lov": "arveloven", "paragraf": "81", "tittel": "Grunnleggende rettsprinsipper", "available": True}],
    },
]

PARAGRAPHS = PARAGRAPHS + _ARVELOVEN_63_82

_ARVELOVEN_83_117 = [
    {
        "number": "83", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Skiftemyndigheten",
        "kategori": "arv",
        "description": "Hvem har myndighet til å behandle et dødsbo i Norge? Det er tingretten — og bare tingretten — som er skiftemyndighet.",
        "kort_svar": "Tingretten er skiftemyndighet. Det er tingretten som behandler dødsbo, åpner offentlig skifte, utsteder skifteattester og løser tvister mellom arvinger.",
        "paragraftekst": "Tingretten er skiftemyndighet. Kongen kan bestemme at skiftemyndigheten kan legges til en særskilt domstol.",
        "hva_betyr_html": "<p>Alt som skjer formelt rundt et dødsbo — fra melding om dødsfallet til utstedelse av skifteattest og åpning av offentlig skifte — skjer gjennom tingretten. Det er tingretten du kontakter for skifteattest, for å åpne offentlig skifte, og for å løse tvister mellom arvinger.</p>",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "<p>Dør noen i familien din: kontakt tingretten i rettskretsen der den avdøde bodde. De gir veiledning om neste steg. Du trenger ikke advokat for å ta første kontakt.</p>",
        "dumme_sporsmal": [],
        "related": [{"lov": "arveloven", "paragraf": "84", "tittel": "Skiftemyndighetens stedlige kompetanse", "available": True}, {"lov": "arveloven", "paragraf": "88", "tittel": "Delegasjon til saksbehandlere", "available": True}],
    },
    {
        "number": "84", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Skiftemyndighetens stedlige kompetanse",
        "kategori": "arv",
        "description": "Hvilken tingrett behandler et dødsbo? Vanligvis tingretten der den avdøde bodde — men det finnes viktige unntak for ektefeller og forsvunne arvinger.",
        "kort_svar": "Dødsboet behandles av tingretten der den avdøde hadde fast bosted. Er det ektefelle med felleseie som også skal skiftes, er det ektefellens bosted som avgjør. Partene kan ikke selv velge tingrett.",
        "paragraftekst": "Behandlingen av et dødsbo foretas av tingretten i den rettskretsen der arvelateren ved dødsfallet hadde sitt alminnelige verneting. Etterlater arvelateren seg ektefelle og det er et felleseie som skal skiftes, behandles boet av tingretten der ektefellen har sitt alminnelige verneting.",
        "hva_betyr_html": """<p><strong>Hovedregel:</strong> Den avdødes faste bosted — der vedkommende var folkeregistrert og faktisk bodde — avgjør hvilken tingrett som behandler boet.</p>
<p><strong>Ektefelle med felleseie:</strong> Er det felleseie som skal deles, er det ektefellens bosted som bestemmer hvilken tingrett som har ansvaret. Grunnen er praktisk: ektefellen har sterkest tilknytning til det pågående oppgjøret.</p>
<p><strong>Ingen norsk bosted:</strong> Bodde den avdøde i utlandet, men skiftet kan gjennomføres i Norge etter § 85, er det Oslo tingrett.</p>
<p>Partene kan ikke bli enige om en annen tingrett — det er lovens regler som gjelder.</p>""",
        "eksempler": [{"navn": "Mette", "tekst": "Mette bor i Oslo. Ektemannen Lars dør. De hadde felleseie. Det er Oslo tingrett som behandler boet — ikke tingretten i Lars' barndomshjem i Bodø."}],
        "vanlige_feil": ["Kontakte feil tingrett fordi man tror det er der gravstedet eller barndomshjemmet avgjør", "Tro at arvingene kan bli enige om en annen tingrett av praktiske grunner — det kan de ikke"],
        "hva_bor_du_html": "<p>Sjekk folkeregisteret for å finne der den avdøde var registrert bosatt, og kontakt tingretten som dekker den rettskretsen. Er du usikker, kan tingretten selv veilede deg.</p>",
        "dumme_sporsmal": [{"q": "Hva hvis den avdøde bodde på sykehjem ved dødsfallet — er det sykehjemmets adresse?", "a": "Nei — det er alminnelig verneting etter tvisteloven § 4-4 som avgjør. Det er normalt der personen var folkeregistrert, ikke midlertidig oppholdssted."}],
        "related": [{"lov": "arveloven", "paragraf": "83", "tittel": "Skiftemyndigheten", "available": True}, {"lov": "arveloven", "paragraf": "85", "tittel": "Skiftebehandling i Norge", "available": True}],
    },
    {
        "number": "85", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Skiftebehandling i Norge — lovvalg",
        "kategori": "arv",
        "description": "Når kan et dødsbo skiftes i Norge selv om den avdøde bodde i utlandet? Og hvilken lov gjelder for selve skiftebehandlingen?",
        "kort_svar": "Bodde den avdøde i Norge, kan det alltid kreves skifte her. Bodde vedkommende i utlandet, kan formue i Norge likevel skiftes her i visse tilfeller. Selve skiftebehandlingen følger alltid norsk lov.",
        "paragraftekst": "Det kan kreves skifte for norsk skiftemyndighet når arvelateren ved sin død hadde sitt vanlige bosted i Norge. Bodde arvelateren i utlandet og det ikke kreves skifte der, kan formue i Norge skiftes her hvis skiftemyndigheten finner det hensiktsmessig. Skiftebehandling for norsk skiftemyndighet gjennomføres etter norsk lov.",
        "hva_betyr_html": """<p><strong>Bosted i Norge:</strong> Retten til norsk skiftebehandling er absolutt — hvem som helst med rettigheter i boet kan kreve det.</p>
<p><strong>Bosted i utlandet:</strong> Er den avdøde norsk statsborger eller hadde norsk verneting, og det ikke pågår skifte i bostedslandet, kan norsk formue (og i noen tilfeller også utenlandsk formue) skiftes i Norge.</p>
<p><strong>Viktig skille:</strong> Selv om skiftet gjennomføres i Norge, er det ikke nødvendigvis norsk arvelov som bestemmer hvem som arver hva — det avgjøres etter § 78 (bostedslandet). Norsk lov styrer bare <em>prosessen</em>.</p>""",
        "eksempler": [{"navn": "Jonas", "tekst": "Jonas er norsk statsborger og bodde i Portugal. Han eier leilighet i Oslo. Han dør i Portugal uten at skifte åpnes der. En arving begjærer skifte av leiligheten ved Oslo tingrett. Skiftet gjennomføres etter norsk prosessrett — men arvefordelingen følger portugisisk arverett."}],
        "vanlige_feil": ["Tro at norsk arvelov alltid gjelder bare fordi skiftet skjer i Norge — arvefordelingen kan følge utenlandsk rett"],
        "hva_bor_du_html": "<p>Er du i en internasjonal arvesak: kontakt advokat med kompetanse på internasjonal privatrett. Skillet mellom arverett og skiftebehandling er avgjørende for utfallet.</p>",
        "dumme_sporsmal": [{"q": "Kan vi velge å skifte i et annet land selv om den avdøde bodde i Norge?", "a": "Nei — bodde den avdøde i Norge, kan enhver med rettigheter i boet kreve norsk skiftebehandling. Det kan ikke avtales bort."}],
        "related": [{"lov": "arveloven", "paragraf": "78", "tittel": "Lovvalg (hvem arver hva)", "available": True}, {"lov": "arveloven", "paragraf": "84", "tittel": "Hvilken tingrett som behandler boet", "available": True}],
    },
    {
        "number": "86", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Inhabilitet",
        "kategori": "arv",
        "description": "Kan en dommer som er i slekt med en arving behandle skiftesaken? Nei — inhabilitetsreglene gjelder fullt ut, også for bostyrere.",
        "kort_svar": "En dommer som er inhabil — fordi vedkommende er i familie med en arving eller har personlig interesse i boet — kan ikke behandle skiftesaken. Det samme gjelder bostyrere og vitner engasjert under skiftet.",
        "paragraftekst": "For dommeren i en skiftesak gjelder reglene om inhabilitet i domstolloven kapittel 6. De nevnte reglene gjelder så langt de passer også for bostyrere og for vitner som engasjeres etter § 91 tredje ledd.",
        "hva_betyr_html": "<p>Inhabilitetsreglene sikrer at den som treffer avgjørelser ikke har personlig interesse i utfallet. Nær slekt med en part, økonomisk interesse i saken, eller tidligere rolle i saken gjør en dommer inhabil. Det gjelder fullt ut i skiftesaker — og utvides til bostyrere og rettens vitner.</p><p>Mistenker du at dommeren eller bostyreren har upassende tilknytning til en arving, kan du ta det opp med tingretten. En inhabil dommer skal på eget tiltak vike sete.</p>",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "<p>Mistenker du inhabilitet: ta det opp skriftlig med tingretten. Forklar tilknytningen og be om at saken overtas av en annen dommer eller bostyrer.</p>",
        "dumme_sporsmal": [{"q": "Kan en bostyrer som kjenner familien behandle boet?", "a": "Det avhenger av nærheten. En vag bekjentskap er ikke inhabilitetsgrunn. Men er bostyreren i familie, forretningspartner eller har nær tilknytning til en arving, er det et problem."}],
        "related": [{"lov": "arveloven", "paragraf": "83", "tittel": "Skiftemyndigheten", "available": True}],
    },
    {
        "number": "87", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Rett til innsyn i testament hos tingretten etter arvelaterens død",
        "kategori": "arv",
        "description": "Hvem kan lese testamentet etter at noen er død? Lovarvinger og testamentsarvinger har rett til innsyn — men ikke nødvendigvis til hele dokumentet.",
        "kort_svar": "Er du arving etter loven — du ville arvet uten testament — kan du kreve å se testamentet hos tingretten. Er du nevnt i testamentet, kan du se den delen som gjelder deg. Retten sikrer at du kan vurdere dine egne rettigheter.",
        "paragraftekst": "Den som uten testamentet ville ha hatt rett til arv etter loven, kan kreve innsyn i testamentet hos tingretten. Den som er tilgodesett i testamentet, kan kreve innsyn i den delen av testamentet som gjelder hans eller hennes rettigheter i boet.",
        "hva_betyr_html": """<p>To grupper har klar innsynsrett:</p>
<p><strong>1. Lovarvinger</strong> (barn, foreldre, ektefelle) — kan kreve innsyn i hele testamentet.<br>
<strong>2. Testamentsarvinger</strong> — kan se den delen som gjelder deres egne rettigheter.</p>
<p>Gjensidig testament: er den ene ektefellen død, er innsynet begrenset til den delen som gjelder den avdødes del. Den gjenlevendes disposisjoner er foreløpig private.</p>
<p>Velger arvingene privat skifte, overleveres testamentet til dem — men tingretten beholder en kopi.</p>""",
        "eksempler": [{"navn": "Anne", "tekst": "Farens testament er innlevert til tingretten. Anne er datter og ville arvet etter loven. Hun vet ikke om testamentet begrenser hennes arv. Hun krever innsyn — tingretten viser henne testamentet. Nå kan Anne vurdere om pliktdelsreglene er overholdt."}],
        "vanlige_feil": ["Tro at testamentet er hemmelig etter dødsfallet — det er det ikke for lovarvinger", "Tro at testamentsarvinger har rett til hele dokumentet — bare til sin del"],
        "hva_bor_du_html": "<p>Mistenker du at det finnes et testament som påvirker dine rettigheter: kontakt tingretten og spør om et testament er innlevert. Er du lovarving, har du rett til innsyn.</p>",
        "dumme_sporsmal": [{"q": "Kan søsknene mine nekte meg å se testamentet?", "a": "Nei — innsynsretten gjelder overfor tingretten, ikke overfor søsknene. Du trenger ikke deres tillatelse."}],
        "related": [{"lov": "arveloven", "paragraf": "63", "tittel": "Oppbevaring av testament", "available": True}, {"lov": "arveloven", "paragraf": "65", "tittel": "Frister for testamentskrav", "available": True}],
    },
    {
        "number": "88", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Oppgaver som kan delegeres til saksbehandlere",
        "kategori": "arv",
        "description": "Trenger alle avgjørelser i et dødsbo å gå til dommeren? Nei — en rekke praktiske oppgaver kan delegeres til tingrettens saksbehandlere.",
        "kort_svar": "Domstollederen kan delegere praktiske oppgaver til saksbehandlere — som å utstede skifteattester, uskifteattester, formuesfullmakter og å oppnevne bostyrer. De fleste rutinesting skjer på kontoret, ikke hos dommeren.",
        "paragraftekst": "Domstollederen kan delegere til saksbehandler: å utstede formuesfullmakter og bankboksfullmakter, å utstede skifteattester og uskifteattester, å fastsette sikkerheten for skifteomkostningene, og å oppnevne bostyrer.",
        "hva_betyr_html": "<p>I praksis møter du sjelden dommeren selv når du kontakter tingretten etter et dødsfall. De fleste første steg — skifteattest, formuesfullmakt, bankboksfullmakt — håndteres av saksbehandlere. Avgjørelsene er like bindende som om dommeren tok dem. Mer komplekse spørsmål — tvister mellom arvinger — går til dommeren.</p>",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "<p>Ta kontakt med tingretten og forklar hva du trenger. Du vil normalt snakke med en saksbehandler som hjelper deg med rutineoppgavene. Er saken omtvistet, går den til dommeren.</p>",
        "dumme_sporsmal": [],
        "related": [{"lov": "arveloven", "paragraf": "92", "tittel": "Formuesfullmakter", "available": True}, {"lov": "arveloven", "paragraf": "118", "tittel": "Skifteattest", "available": True}],
    },
    {
        "number": "88a", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Digitalt skifte av dødsbo",
        "kategori": "arv",
        "description": "Kan du skifte et dødsbo digitalt? Ja — loven åpner for digitale offentlige tjenester som gjør skiftet enklere uten fysisk oppmøte.",
        "kort_svar": "Skifte av dødsbo kan gjennomføres digitalt gjennom offentlige tjenester. Banker, Folkeregisteret, Skatteetaten og tingretten kan dele opplysninger, slik at du ikke trenger å samle inn alt på papir.",
        "paragraftekst": "Oppgavene som følger av lovens tredje del, kan utføres gjennom offentlige tjenester for digitalt skifte av dødsbo. Offentlige og private virksomheter kan uten hinder av taushetsplikt dele opplysninger i forbindelse med gjennomføring av digitalt skifte.",
        "hva_betyr_html": "<p>Den digitale skiftetjenesten lar banker, Folkeregisteret, Skatteetaten og tingretten dele opplysninger om den avdøde uten at du som arving må samle inn alt på papir. Hele prosessen kan gjennomføres uten fysisk oppmøte ved tingretten.</p><p>Tjenesten er tilgjengelig gjennom domstol.no og bruker BankID for pålogging.</p>",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "<p>Skal du gjennomføre privat skifte: sjekk om den digitale skiftetjenesten passer for din situasjon. For ukompliserte boer er hele prosessen digital. Logg inn med BankID på domstol.no.</p>",
        "dumme_sporsmal": [{"q": "Kan alle boer skiftes digitalt?", "a": "Ikke nødvendigvis. Kompliserte boer med tvister, utenlandske eiendeler eller spesielle testamentariske bestemmelser kan kreve ordinær behandling ved tingretten."}],
        "related": [{"lov": "arveloven", "paragraf": "88", "tittel": "Delegasjon av oppgaver", "available": True}, {"lov": "arveloven", "paragraf": "98", "tittel": "Skifteformene", "available": True}],
    },
    {
        "number": "89", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Melding om dødsfall — opplysninger om den avdøde",
        "kategori": "arv",
        "description": "Hvem har plikt til å melde fra om et dødsfall til tingretten? Og hva plikter familien å opplyse om den avdødes økonomi og slekt?",
        "kort_svar": "Dødsfallet skal meldes til tingretten. Normalt gjøres det av legen via Folkeregisteret — men pårørende har selvstendig meldeplikt. Ektefelle, samboer og nærmeste slektninger plikter også å opplyse om den avdødes økonomi, slekt og eventuelle testament.",
        "paragraftekst": "Dødsfall skal straks meldes til tingretten. Ektefelle, samboer, de nærmeste slektningene og testamentsarvinger plikter å gi opplysninger om den avdødes formuesforhold, slektskapsforhold og andre spørsmål av betydning for bobehandlingen, herunder om de kjenner til at den avdøde har opprettet testament.",
        "hva_betyr_html": """<p><strong>Melding om dødsfallet:</strong> I praksis melder legen dødsfallet via Folkeregisteret, som varsler tingretten. Skjer det ikke — ved plutselig død uten legetilsyn — har pårørende selvstendig plikt til å melde direkte.</p>
<p><strong>Opplysningsplikten:</strong> Som ektefelle, samboer, nær slektning eller testamentsarving plikter du å opplyse om: den avdødes økonomi (eiendeler, gjeld, bankkonti, eiendom), slektskapsforhold (hvem er arvinger?), og om det finnes testament.</p>
<p>Er det barn som nå mangler foreldre med foreldreansvar, skal det særskilt opplyses om dette.</p>""",
        "eksempler": [{"navn": "Lars", "tekst": "Lars sin mor dør. Legen melder til Folkeregisteret. Tingretten ber Lars om opplysninger. Lars oppgir leilighetens verdi, sparepenger, gjeld og at han ikke kjenner til testament. Han sender inn det han vet."}],
        "vanlige_feil": ["Tro at legen alltid tar seg av alt — i noen tilfeller faller meldeplikten på pårørende", "Glemme å nevne alle arvinger — halvbrødre og halvsøstre som tingretten ikke vet om, er din plikt å opplyse om"],
        "hva_bor_du_html": "<p>Etter et dødsfall: sjekk at tingretten er varslet. Svar på brev fra tingretten så raskt og fullstendig som mulig. Vet du om testament — opplys om det med én gang.</p>",
        "dumme_sporsmal": [{"q": "Har jeg plikt til å opplyse om gjeld den avdøde skjulte?", "a": "Plikten gjelder det du vet om eller burde vite om. Skjult gjeld du ikke kjenner til, kan du ikke opplyse om — men vet du om det, har du plikt til å melde det."}],
        "related": [{"lov": "arveloven", "paragraf": "90", "tittel": "Tingrettens innledende behandling", "available": True}, {"lov": "arveloven", "paragraf": "92", "tittel": "Formuesfullmakter", "available": True}],
    },
    {
        "number": "90", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Tingrettens innledende behandling",
        "kategori": "arv",
        "description": "Hva gjør tingretten straks etter at noen dør? Den sjekker om det finnes testament, varsler arvinger og gir veiledning om rettigheter i boet.",
        "kort_svar": "Når tingretten mottar melding om et dødsfall, sjekker den umiddelbart om det finnes innlevert testament, og varsler de som kan ha krav på arv. Retten har plikt til å gi veiledning slik at arvingene kan ivareta sine interesser.",
        "paragraftekst": "Når tingretten mottar meldingen om dødsfallet, skal den kontrollere om den avdøde har innlevert testament til en domstol. Retten skal varsle dem som etter loven kan ha krav på arv. Er noen av arvingene mindreårige eller fratatt rettslig handleevne, skal retten varsle statsforvalteren. Retten skal gi nødvendig veiledning slik at de som kan ha rettigheter i boet, kan ivareta sine interesser.",
        "hva_betyr_html": """<p><strong>Testamentssjekk — det første tingretten gjør:</strong> Umiddelbart sjekkes om den avdøde har levert testament til oppbevaring. Er det registrert, hentes det frem og relevante parter varsles.</p>
<p><strong>Varsling av arvinger:</strong> Tingretten varsler dem som kan ha arverett. Er noen arvinger mindreårige, varsles statsforvalteren. Er det en stiftelse som skal opprettes, varsles Stiftelsestilsynet.</p>
<p><strong>Veiledningsplikt:</strong> Tingretten har aktiv plikt til å hjelpe deg. Ikke stå alene og prøv å forstå systemet — ring tingretten og spør om neste steg.</p>""",
        "eksempler": [{"navn": "Marius", "tekst": "Marius' far dør. Tingretten finner innlevert testament og varsler Marius og søsteren. Marius ringer tingretten som forklarer: de kan velge privat skifte og da skaffe skifteattest."}],
        "vanlige_feil": ["Vente på at tingretten tar all initiativ — du bør selv ta kontakt og spørre om veiledning", "Tro at tingretten automatisk finner alle arvinger — den er avhengig av opplysningene du gir"],
        "hva_bor_du_html": "<p>Vent ikke på brev alene. Ta kontakt med tingretten, forklar situasjonen og spør om neste steg. Tingretten er der for å hjelpe.</p>",
        "dumme_sporsmal": [{"q": "Hva hvis tingretten ikke finner testament, men vi tror det finnes ett?", "a": "Tingretten sjekker bare det nasjonale testamentregisteret. Et privat oppbevart testament — hjemme, hos advokat, i bankboks — er ditt ansvar å finne og levere."}],
        "related": [{"lov": "arveloven", "paragraf": "89", "tittel": "Melding om dødsfall", "available": True}, {"lov": "arveloven", "paragraf": "91", "tittel": "Registrering og sikring av boets eiendeler", "available": True}],
    },
    {
        "number": "91", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Registrering og sikring av boets eiendeler",
        "kategori": "arv",
        "description": "Er du redd for at eiendeler i boet forsvinner før skiftet er i gang? Du kan be tingretten om å registrere og sikre dem.",
        "kort_svar": "Enhver med rettigheter i boet kan be tingretten om å registrere og sikre eiendelene. Retten kan også gjøre dette av eget tiltak. Kostnaden dekkes av den som ber om det — men av boet ved offentlig skifte.",
        "paragraftekst": "Enhver som har rettigheter i boet, kan kreve at retten foretar en foreløpig registrering eller nødvendig sikring av boets eiendeler. Retten kan foreta dette av eget tiltak.",
        "hva_betyr_html": "<p>Mellom dødsfallet og det endelige skiftet er boets eiendeler sårbare. Noen kan ta ting uten tillatelse, eiendommer kan forringes, bankkonti kan tømmes. Hvem som helst med rettigheter i boet — arving, testamentsarving, kreditor — kan be tingretten om å registrere hva som finnes og sikre det.</p><p>Tingretten kan også bruke politiets bistand om nødvendig.</p>",
        "eksempler": [{"navn": "Sofie", "tekst": "Sofie mistenker at en medarving tok smykker og kontanter etter dødsfallet. Hun ber tingretten om foreløpig registrering. Tingretten sender representant som lager oversikt. Nå er det dokumentert hva som fantes."}],
        "vanlige_feil": ["Vente for lenge — eiendeler kan forsvinne raskt etter et dødsfall"],
        "hva_bor_du_html": "<p>Har du grunn til å tro at eiendeler er i fare: kontakt tingretten umiddelbart og be om registrering og sikring. Du trenger ikke vente til skifteform er valgt.</p>",
        "dumme_sporsmal": [{"q": "Hva skjer hvis noen allerede har tatt ting fra boet?", "a": "Registreringen dokumenterer hva som burde vært der — det danner grunnlag for krav om tilbakelevering eller erstatning under skiftet."}],
        "related": [{"lov": "arveloven", "paragraf": "90", "tittel": "Tingrettens innledende behandling", "available": True}, {"lov": "arveloven", "paragraf": "92", "tittel": "Formuesfullmakter", "available": True}],
    },
    {
        "number": "92", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Formuesfullmakter og bankboksfullmakter",
        "kategori": "arv",
        "description": "Kan du sjekke den avdødes økonomi og bankkonti før skiftet er ferdig? Ja — med formuesfullmakt fra tingretten. Ektefelle og samboer med felles barn har automatisk denne retten de første 60 dagene.",
        "kort_svar": "Tingretten kan gi deg fullmakt til å se inn i den avdødes økonomi — banksaldi, skattemelding, gjeld. Ektefelle og samboer med felles barn trenger ikke vente på fullmakt de første 60 dagene etter dødsfallet.",
        "paragraftekst": "Retten kan gi arvingene fullmakt til innsyn i arvelaterens formues- og gjeldsforhold. Fullmakt gir rett til innsyn i saldoen på bankkonti på dødsfallstidspunktet og transaksjonsdata de siste tre månedene. I de første 60 dagene kan arvelaterens ektefelle eller samboer med felles barn uten fullmakt kreve slikt innsyn.",
        "hva_betyr_html": """<p><strong>Formuesfullmakten:</strong> For å planlegge skiftet trenger arvingene å vite hva den avdøde hadde. Formuesfullmakten gir rett til å spørre banker, Skatteetaten og andre om den avdødes økonomi — inkludert banksaldo og de siste tre måneders transaksjoner.</p>
<p><strong>Ektefelle og samboer — 60 dager uten fullmakt:</strong> Er du ektefelle eller samboer med felles barn, kan du gå direkte til banken de første 60 dagene og be om innsyn. Praktisk viktig for å betale regninger og begravelsesutgifter.</p>
<p><strong>Bankboksfullmakt:</strong> Er det bankboks, kan tingretten gi fullmakt til gjennomgang. En bankansatt skal alltid være til stede.</p>""",
        "eksempler": [{"navn": "Kari", "tekst": "Karis mann dør. Hun er ektefelle med felles barn. Hun vet ikke om han hadde gjeld. De første 60 dagene går hun til banken og ber om innsyn uten å vente på tingretten. Etter 60 dager søker hun om formuesfullmakt som utstedes raskt."}],
        "vanlige_feil": ["Vente på skifteattest for å få oversikt over økonomi — formuesfullmakten er mye raskere", "Som ektefelle ikke vite om 60-dagersregelen", "Tro at du kan gå gjennom bankboks alene — bankansatt skal alltid være til stede"],
        "hva_bor_du_html": "<p>Søk om formuesfullmakt så snart som mulig etter dødsfallet. Er du ektefelle eller samboer med felles barn: gå til banken direkte — du trenger ikke vente.</p>",
        "dumme_sporsmal": [{"q": "Kan jeg bruke formuesfullmakten til å ta ut penger fra den avdødes konto?", "a": "Nei — fullmakten gir innsyn, ikke disposisjonsrett. For å disponere trenger du skifteattest."}],
        "related": [{"lov": "arveloven", "paragraf": "89", "tittel": "Melding om dødsfall", "available": True}, {"lov": "arveloven", "paragraf": "118", "tittel": "Skifteattest", "available": True}],
    },
    {
        "number": "93", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Proklama før skifteform er valgt",
        "kategori": "arv",
        "description": "Kan arvingene kunngjøre en frist for kreditorene allerede før de har valgt privat eller offentlig skifte? Ja — en arving kan kreve proklama på dette tidlige stadiet.",
        "kort_svar": "Selv før arvingene har valgt skifteform, kan en arving kreve at tingretten kunngjør en frist for kreditorene til å melde sine krav. Krav som ikke meldes innen fristen, faller bort.",
        "paragraftekst": "Før det er avgjort om boet skal skiftes privat eller offentlig, skal retten, hvis noen av arvingene krever det, kunngjøre en frist for kreditorene til å melde sine krav etter reglene om proklama i §§ 100 til 103.",
        "hva_betyr_html": "<p>Proklama er en offentlig kunngjøring som gir kreditorene seks uker til å melde sine krav mot den avdøde. Krav som ikke meldes innen fristen, faller bort — for godt.</p><p>Normalt utstedes proklama i forbindelse med privat eller offentlig skifte. Men loven tillater at det skjer enda tidligere — før skifteform er valgt — nyttig når det er mistanke om mange ubetalte regninger.</p>",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "<p>Mistenker du at den avdøde hadde ukjent gjeld: be tingretten om proklama tidlig. Én arving kan kreve dette alene, uten de andres samtykke.</p>",
        "dumme_sporsmal": [{"q": "Hva skjer med kreditorer som ikke melder innen fristen?", "a": "Kravet faller bort etter § 102. Men panterett og eiendomsrettskrav overlever proklamafristen."}],
        "related": [{"lov": "arveloven", "paragraf": "100", "tittel": "Utstedelse av proklama", "available": True}, {"lov": "arveloven", "paragraf": "102", "tittel": "Virkning av proklamaet", "available": True}],
    },
    {
        "number": "94", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Testamentarisk bestemmelse om opprettelse av stiftelse",
        "kategori": "arv",
        "description": "Hva skjer hvis testamentet sier at det skal opprettes en stiftelse? Tingretten innkaller til et forberedende rettsmøte.",
        "kort_svar": "Er det bestemt i testamentet at det skal opprettes en stiftelse, kaller tingretten inn arvingene til et forberedende rettsmøte. Bestrider noen arvingene stiftelsens arverett, åpnes det offentlig skifte.",
        "paragraftekst": "Går et testament ut på at det skal opprettes en stiftelse, skal arvingene innkalles til et forberedende rettsmøte. Bestrider noen av arvingene stiftelsens arverett, skal tingretten åpne offentlig skifte. Stiftelsestilsynet kan representere stiftelsen under privat og offentlig skifte hvis stiftelsen er uten et kompetent styre.",
        "hva_betyr_html": "<p>Å opprette en stiftelse gjennom testament krever særskilt behandling — stiftelsen eksisterer ikke ennå og skal opprettes ved hjelp av arven. Tingretten innkaller alle arvinger til et forberedende rettsmøte for å avklare situasjonen.</p><p>Stiftelsestilsynet kan trå til og representere stiftelsen hvis den ennå ikke har et fungerende styre.</p>",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "<p>Er du testamentsarving og testamentet sier stiftelse: kontakt tingretten for veiledning om prosessen, og undersøk om Stiftelsestilsynet bør kontaktes tidlig.</p>",
        "dumme_sporsmal": [],
        "related": [{"lov": "arveloven", "paragraf": "98", "tittel": "Skifteformene", "available": True}, {"lov": "arveloven", "paragraf": "40", "tittel": "Opprettelse av testament", "available": True}],
    },
    {
        "number": "95", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Fullmakt til å disponere i bo med eiendeler av liten verdi",
        "kategori": "arv",
        "description": "Hva skjer med et lite bo uten særlig verdi? Tingretten kan gi én person fullmakt til å rydde opp uten formelt skifte.",
        "kort_svar": "Er den avdødes eiendeler av liten verdi etter at begravelsen er betalt, kan tingretten gi den som ordnet begravelsen — eller en annen nær person — fullmakt til å disponere eiendelene. Sparer familien for formelt skifte.",
        "paragraftekst": "Hvis den avdødes brutto eiendeler etter at begravelsesutgiftene er dekket må antas å være av liten verdi, kan retten gi en person som har ordnet med begravelsen, eller en annen som har stått den avdøde nær, fullmakt til å disponere over eiendelene.",
        "hva_betyr_html": "<p>Ikke alle boer er store. Noen avdøde etterlater seg lite annet enn noen møbler og et bankinnskudd. Da er det unødvendig med hele skifteprosessen. Tingretten kan gi den som arrangerte begravelsen fullmakt til å rydde opp — tømme leiligheten, avslutte kontrakter, betale regninger, fordele det lille som er igjen.</p><p>Den som får fullmakten tar også ansvaret: de forplikter seg til at gjeld dekkes innenfor det som finnes.</p>",
        "eksempler": [{"navn": "Arne", "tekst": "Arnes bror dør alene. Boet ser ut til å bestå av noen møbler og 3 000 kr. Arne ordnet begravelsen. Han ber tingretten om fullmakt. Tingretten innvilger. Arne selger møblene, betaler strømregningen og beholder det som er igjen."}],
        "vanlige_feil": ["Disponere over den avdødes eiendeler uten noen form for fullmakt eller skifteattest — kan gi personlig ansvar overfor kreditorer"],
        "hva_bor_du_html": "<p>Har du ordnet begravelsen og boet ser lite ut: ta kontakt med tingretten og søk om fullmakt. Det er raskere og enklere enn privat skifte.</p>",
        "dumme_sporsmal": [{"q": "Kan fullmakten brukes til å selge fast eiendom?", "a": "Nei — eiendom krever hjemmel og tinglysing, noe som forutsetter skifteattest. Paragrafen er ment for enkle boer uten fast eiendom."}],
        "related": [{"lov": "arveloven", "paragraf": "92", "tittel": "Formuesfullmakter", "available": True}, {"lov": "arveloven", "paragraf": "98", "tittel": "Skifteformene", "available": True}],
    },
    {
        "number": "96", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Melding om uskifte",
        "kategori": "arv",
        "description": "Vil du sitte i uskifte etter ektefellen? Du må melde fra til tingretten innen 60 dager — og gi en oversikt over begge ektefellers økonomi.",
        "kort_svar": "Vil du bruke retten til uskifte, må du sende melding til tingretten innen 60 dager etter dødsfallet. Meldingen skal inneholde navn på arvingene og en oversikt over ektefellenes eiendeler og gjeld. Fristen kan forlenges.",
        "paragraftekst": "En ektefelle eller samboer som vil gjøre bruk av retten til uskifte, må sende melding til tingretten innen 60 dager etter dødsfallet. I meldingen skal det opplyses om navn på arvingene og gis en oppstilling over arvelaterens og den lengstlevende ektefellens eiendeler og forpliktelser.",
        "hva_betyr_html": """<p>Uskifte er retten til å overta avdødes del av boet uten å skifte med barna. For å bruke denne retten MÅ du melde fra til tingretten innen 60 dager.</p>
<p><strong>Hva skal meldingen inneholde?</strong> Navn og adresse på alle arvingene, og en rimelig god oversikt over begge ektefellers eiendeler og gjeld ved dødsfallet.</p>
<p><strong>Fristen kan forlenges:</strong> Er 60 dager for kort — fordi du sitter i sorg, er syk, eller trenger mer tid — kan tingretten forlenge. Be om det innen 60 dager er ute.</p>""",
        "eksempler": [{"navn": "Eva", "tekst": "Evas mann dør. De har tre barn. Eva ønsker uskifte. Hun kontakter tingretten innen 60 dager og sender melding med navnene på barna og oversikt over huset (3 mill, restgjeld 900 000) og felles bankinnskudd (350 000 kr). Prosessen med uskifteattest starter."}],
        "vanlige_feil": ["Glemme 60-dagersfristen — fristen løper fra dødsfallet, ikke fra du har funnet ut av alt", "Ikke be om fristforlengelse i tide — gjør det før 60 dager er ute"],
        "hva_bor_du_html": "<p>Bestem deg raskt om du vil ha uskifte. Er du usikker: kontakt tingretten innen 60 dager og be om veiledning. Er du klar: send meldingen. Er du ikke ferdig: søk om forlengelse.</p>",
        "dumme_sporsmal": [{"q": "Hva skjer hvis jeg glemmer 60-dagersfristen?", "a": "Da har du i utgangspunktet tapt retten til uskifte. Tingretten kan forlenge i særlige tilfeller — for eksempel sykdom — men det er ikke garantert."}],
        "related": [{"lov": "arveloven", "paragraf": "14", "tittel": "Ektefellers rett til uskifte", "available": True}, {"lov": "arveloven", "paragraf": "97", "tittel": "Uskifteattest", "available": True}],
    },
    {
        "number": "97", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Uskifteattest",
        "kategori": "arv",
        "description": "Hva er en uskifteattest og hva gir den deg rett til? Uskifteattesten legitimerer gjenlevende ektefelle eller samboer til å råde over den avdødes eiendeler.",
        "kort_svar": "Uskifteattesten bekrefter at du har rett til å sitte i uskifte. Med attesten kan du disponere over den avdødes eiendeler — selge, kjøpe, ta opp lån — som om du eide alt alene.",
        "paragraftekst": "Retten skal så snart vilkårene for uskifte er avklart, utstede en uskifteattest. Ved uskifteattesten blir den lengstlevende ektefellen eller samboeren legitimert til å rå over arvelaterens eiendeler.",
        "hva_betyr_html": """<p>Uskifteattesten er nøkkelen til uskifteboet. Med den er du legitimert overfor banker, Kartverket, Brønnøysundregistrene og alle andre som trenger å vite at du kan disponere den avdødes eiendeler.</p>
<p>Du kan vise frem uskifteattesten til banken for å disponere den avdødes konto, ved salg av eiendom som stod i den avdødes navn, og for å ta opp lån med eiendeler som sikkerhet.</p>
<p><strong>Viktig:</strong> Er det arvinger som ikke kan utestenges fra arven sin — typisk barn fra tidligere ekteskap — må disse enten samtykke til uskifte eller få sitt oppgjør på annen måte. Uskifteattesten utstedes ikke før dette er avklart.</p>""",
        "eksempler": [{"navn": "Ingrid", "tekst": "Ingrids mann dør. De har to felles barn som ikke kan nekte uskifte. Tingretten bekrefter vilkårene og utsteder uskifteattesten. Ingrid tar den med til banken og får tilgang til mannens konti."}],
        "vanlige_feil": ["Tro at du kan disponere den avdødes eiendeler med bare dødsmeldingen — du trenger uskifteattesten", "Glemme å presentere uskifteattesten ved salg av eiendom i den avdødes navn"],
        "hva_bor_du_html": "<p>Når tingretten har bekreftet vilkårene, be eksplisitt om at uskifteattesten utstedes. Ta vare på originalen — du vil trenge den gjentatte ganger.</p>",
        "dumme_sporsmal": [{"q": "Er uskifteattest og skifteattest det samme?", "a": "Nei. Uskifteattesten bekrefter at du sitter i uskifte og rår over boet. Skifteattesten (§ 118) bekrefter at arvingene har overtatt boet til privat skifte og fordeler det."}],
        "related": [{"lov": "arveloven", "paragraf": "96", "tittel": "Melding om uskifte", "available": True}, {"lov": "arveloven", "paragraf": "14", "tittel": "Ektefellers rett til uskifte", "available": True}],
    },
    {
        "number": "98", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Skifte av dødsbo — skifteformene",
        "kategori": "arv",
        "description": "Hva er et skifte, og hva er forskjellen på privat og offentlig skifte? § 98 gir deg definisjonen og de grunnleggende valgene etter et dødsfall.",
        "kort_svar": "Skifte betyr at den avdødes gjeld betales og eiendeler fordeles mellom arvingene. Det kan skje privat (arvingene ordner det selv) eller offentlig (tingretten styrer). Privat skifte er vanligst og forutsetter at minst én arving påtar seg personlig ansvar for gjelden.",
        "paragraftekst": "Med dødsbo menes alle eiendelene og forpliktelsene arvelateren etterlater seg. Med skifte av dødsbo menes oppgavene frem til forpliktelsene er dekket og eiendelene fordelt mellom arvingene. Et dødsbo kan skiftes privat eller offentlig. Et dødsbo kan skiftes privat bare hvis ansvaret for arvelaterens forpliktelser er overtatt etter reglene i § 116.",
        "hva_betyr_html": """<p><strong>Hva er et dødsbo?</strong> Alt den avdøde etterlater seg: hus, bil, bankinnskudd, verdipapirer — men også gjeld, ubetalte regninger og løpende forpliktelser.</p>
<p><strong>Privat skifte</strong> (det vanligste): Arvingene tar hånd om alt selv — lager oversikt, betaler gjeld, fordeler resten. Forutsetningen er at minst én arving påtar seg personlig ansvar for gjelden (se § 116).</p>
<p><strong>Offentlig skifte</strong>: Brukes når arvingene ikke blir enige, boet er insolvent, noen krever det, eller testator har bestemt det. Tingretten styrer hele prosessen med oppnevnt bostyrer.</p>
<p>Loven krever proporsjonalitet: kostnadene ved skiftet skal stå i forhold til verdiene. Et bo på 50 000 kr skal ikke koste 100 000 kr å skifte.</p>""",
        "eksempler": [{"navn": "Lars og Anne", "tekst": "Lars og Anne er eneste arvinger etter faren. Boet: leilighet (2 mill), sparepenger (200 000), billån (350 000). De er enige. Lars påtar seg gjeldansvaret og søker skifteattest. Privat skifte: selger leiligheten, innfrir lånet, fordeler resten likt."}],
        "vanlige_feil": ["Tro at du automatisk overtar boet uten å gjøre noe — du må aktivt velge skifteform og overholde frister", "Glemme at privat skifte innebærer personlig ansvar for gjelden"],
        "hva_bor_du_html": "<p>Er arvingene enige og boet er oversiktlig: gå for privat skifte. Er det konflikt, gjeld som overstiger verdiene, eller usikkerhet: vurder offentlig skifte.</p>",
        "dumme_sporsmal": [{"q": "Hva er fristen for å velge skifteform?", "a": "For privat skifte: ansvaret for gjelden må overtas innen 60 dager etter dødsfallet for å unngå at offentlig skifte åpnes automatisk (se § 117)."}],
        "related": [{"lov": "arveloven", "paragraf": "97", "tittel": "Uskifteattest", "available": True}, {"lov": "arveloven", "paragraf": "116", "tittel": "Ansvaret for forpliktelsene", "available": True}],
    },
    {
        "number": "99", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Testamentsfullbyrder",
        "kategori": "arv",
        "description": "Kan du i testament utpeke noen til å gjennomføre skiftet etter deg? Ja — men en testamentsfullbyrder er ikke bindende for ektefelle og livsarvinger.",
        "kort_svar": "Du kan i testament utpeke en navngitt person til å gjennomføre skiftet etter deg. Men livsarvinger, ektefelle og samboer med arverett er ikke bundet av dette valget og kan kreve offentlig skifte uavhengig av testamentet.",
        "paragraftekst": "Arvelateren kan i testament fastsette at en bestemt, navngitt person skal gjennomføre skiftet (testamentsfullbyrder). En slik bestemmelse er ikke bindende for arvelaterens livsarvinger, ektefelle eller samboer med arverett. Ved privat skifte opptrer testamentsfullbyrderen som fullmektig. Ved offentlig skifte oppnevnes testamentsfullbyrderen som bostyrer.",
        "hva_betyr_html": """<p>En testamentsfullbyrder er den du stoler på til å gjennomføre din siste vilje — en advokat, en god venn, eller et familiemedlem utenfor arvinggruppen. Utpekingen skjer i testamentet.</p>
<p><strong>Begrensning:</strong> Barna, ektefellen og samboer med arverett kan ikke tvinges til å akseptere testamentsfullbyrderen. Ønsker de kontroll over skiftet selv, kan de kreve offentlig skifte — der testamentsfullbyrderen da blir bostyrer.</p>""",
        "eksempler": [{"navn": "Sofie", "tekst": "Sofie utpeker advokat Tom som testamentsfullbyrder. Da Sofie dør, tar Tom over gjennomføringen. Datteren bestrider testamentets fordeling og krever offentlig skifte. Tom oppnevnes da som bostyrer under det offentlige skiftet."}],
        "vanlige_feil": ["Tro at testamentsfullbyrderbestemmelsen er absolutt — livsarvinger og ektefelle kan sette den til side via offentlig skifte"],
        "hva_bor_du_html": "<p>Vil du at en bestemt person skal styre skiftet: utpekingen MÅ skje i testamentet, og personen bør navngis eksplisitt. Avtal gjerne på forhånd at de aksepterer oppdraget.</p>",
        "dumme_sporsmal": [{"q": "Kan testamentsfullbyrderen selv arve noe?", "a": "Ja — det er ingen regel som forbyr det. Men det kan skape interessekonflikter."}],
        "related": [{"lov": "arveloven", "paragraf": "98", "tittel": "Skifteformene", "available": True}, {"lov": "arveloven", "paragraf": "116", "tittel": "Privat skifte", "available": True}],
    },
    {
        "number": "99a", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Frist for å overføre landbrukseiendom til ny eier",
        "kategori": "arv",
        "description": "Inngår det en gård i et dødsbo? Den må overføres til ny eier med tinglyst hjemmel innen tre år fra dødsfallet — ellers kan kommunen selge den.",
        "kort_svar": "Er det en landbrukseiendom i boet med minst 5 dekar jordbruksareal eller 25 dekar produktiv skog, må eiendommen overføres til ny eier med tinglyst hjemmel innen tre år fra dødsfallet. Oversittes fristen, kan kommunen tvangselge den.",
        "paragraftekst": "Hvis det i dødsboet inngår landbrukseiendom som består av minst fem dekar jordbruksareal eller minst 25 dekar produktiv skog, må eiendommen overføres fra dødsboet til en ny eier med tinglyst hjemmel innen tre år fra arvelaterens død. Oversittes fristen, kan kommunen la eiendommen selge etter konsesjonsloven § 19.",
        "hva_betyr_html": """<p>En landbrukseiendom kan ikke bli hengende uavklart i et dødsbo i årevis. Loven setter en tre-årsgrense for å tvinge frem en avgjørelse: hvem overtar gården?</p>
<p>Overføringen behøver ikke innebære salg — en arving kan overta, eller gjenlevende ektefelle kan overta. Det avgjørende er tinglyst eiendomsoverdragelse innen fristen.</p>
<p>Kommunen skal varsle boet innen ett år. Trenger dere mer tid — for eksempel ved tvist om hvem som skal overta — kan det søkes om forlengelse. Det krever særlige grunner.</p>""",
        "eksempler": [{"navn": "Per", "tekst": "Per dør og etterlater gård med 30 dekar jordbruksareal. Tre søsken strides om hvem som overtar. Kommunen varsler etter ett år. Etter 2,5 år søker søsknene om forlengelse. Kommunen gir seks måneder. Til slutt kjøper den eldste søsteren ut de to andre."}],
        "vanlige_feil": ["Tro at fristen løper fra skifteattesten er utstedt — den løper fra dødsfallet", "Glemme å søke om forlengelse i tide — søknaden må være inne før tre-årsfristen løper ut"],
        "hva_bor_du_html": "<p>Er det landbrukseiendom i boet: ta dette opp tidlig i skifteprosessen. Avklar hvem som har odel, hvem som ønsker å overta, og hva prisen skal være. Tre år går fort når det er uenighet.</p>",
        "dumme_sporsmal": [{"q": "Gjelder fristen også for skogteiger uten jordbruksareal?", "a": "Ja — 25 dekar produktiv skog utløser fristen alene, uavhengig av om det er jordbruksareal."}],
        "related": [{"lov": "arveloven", "paragraf": "98", "tittel": "Skifteformene", "available": True}, {"lov": "arveloven", "paragraf": "104", "tittel": "Rett til å overta eiendeler", "available": True}],
    },
    {
        "number": "100", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Utstedelse av proklama",
        "kategori": "arv",
        "description": "Hva er proklama og hvem kunngjøres det til? Proklamaet er den offisielle meldingen til den avdødes kreditorer om at de må melde sine krav innen seks uker.",
        "kort_svar": "Proklama er en offentlig kunngjøring som gir kreditorene seks uker til å melde sine krav mot den avdøde. Krav som ikke meldes innen fristen, faller bort. Kjente kreditorer i utlandet skal varsles særskilt.",
        "paragraftekst": "Arvelaterens kreditorer skal ved proklama gis melding om dødsfallet og oppfordring til å melde sine krav. Det skal ikke utstedes mer enn ett proklama for hvert bo. Kjente kreditorer med bopel utenfor Norge skal gis særlig melding.",
        "hva_betyr_html": "<p>Proklama setter en hard frist for alle kreditorer til å melde sine krav. Kreditorer som ikke melder innen seks uker fra siste kunngjøring, mister kravet sitt — for alltid, med noen unntak (panterett osv.).</p><p>Det er bare ett proklama per bo. Kjente utenlandske kreditorer (utenlandsk kredittkortselskap, utenlandsk bank) skal varsles direkte og personlig i tillegg til den offentlige kunngjøringen.</p>",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "<p>Er du arving og vil begrense risikoen for ukjente krav: be om proklama. Det koster litt, men gir trygghet mot at kreditorer dukker opp etter at skiftet er ferdig.</p>",
        "dumme_sporsmal": [{"q": "Hva med kreditorer den avdøde hadde glemt å nevne?", "a": "De er bundet av proklamafristen. Er de «ukjente» fordi de aldri kom med et krav mens den avdøde levde, mister de kravet."}],
        "related": [{"lov": "arveloven", "paragraf": "101", "tittel": "Proklamaets innhold og kunngjøring", "available": True}, {"lov": "arveloven", "paragraf": "102", "tittel": "Virkning av proklamaet", "available": True}],
    },
    {
        "number": "101", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Proklamaets innhold og kunngjøring",
        "kategori": "arv",
        "description": "Hva skal et proklama inneholde, og hvor kunngjøres det? Det kunngjøres i Norsk lysingsblad og i en lokal avis — og skal inneholde fristen for å melde krav.",
        "kort_svar": "Proklamaet skal inneholde den avdødes navn og fødselsnummer, oppfordring til kreditorer med fristen (seks uker), og opplysning om hvem krav skal meldes til. Kunngjøres i Norsk lysingsblad og i en lokal avis (to innrykk).",
        "paragraftekst": "Proklamaet skal inneholde: arvelaterens navn, fødselsnummer og bopel; oppfordring til kreditorene om å melde krav; fristen for å melde krav; og opplysninger om hvem krav skal meldes til. Proklamaet kunngjøres i Norsk lysingsblad og ved to innrykk i en lokal avis.",
        "hva_betyr_html": "<p>Proklamaet må oppfylle bestemte formkrav for at kravene som ikke meldes, skal falle bort. To kunngjøringer er obligatoriske: Norsk lysingsblad (statlig kunngjøringstjeneste) og en avis med stor dekning på stedet der den avdøde bodde — to ganger i avisen.</p><p>Fristen begynner fra den siste av de to kunngjøringene i avisen.</p>",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "<p>Er du kreditor og vet at noen skylder deg penger er død: sjekk norsklysingblad.no regelmessig. Ser du et proklama — meld kravet umiddelbart. Seks uker er kort tid.</p>",
        "dumme_sporsmal": [{"q": "Hvem betaler kunngjøringskostnadene?", "a": "Ved offentlig skifte: boet. Ved privat skifte eller uskifte: den som krever proklamaet."}],
        "related": [{"lov": "arveloven", "paragraf": "100", "tittel": "Utstedelse av proklama", "available": True}, {"lov": "arveloven", "paragraf": "102", "tittel": "Virkning av proklamaet", "available": True}],
    },
    {
        "number": "102", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Melding av krav og virkning av proklamaet",
        "kategori": "arv",
        "description": "Hva er fristen for å melde krav etter proklama — og hva skjer med krav som ikke meldes i tide? Fristen er seks uker, og krav som oversitter den, faller bort.",
        "kort_svar": "Kreditorer har seks uker fra siste kunngjøring til å melde sine krav. Krav som ikke meldes innen fristen, faller bort. Men panterett, tilbakeholdsrett og eiendomsrettskrav overlever proklamafristen.",
        "paragraftekst": "Fristen etter proklamaet for å melde krav er seks uker fra siste kunngjøring. Krav som ikke meldes innen fristen, faller bort. Proklamaet har ikke betydning for krav som bygger på eiendomsrett, tilbakeholdsrett og panterett.",
        "hva_betyr_html": """<p>Seks uker er en hard frist. Kreditorer som ikke rekker den, mister kravet mot boet — de kan ikke komme tilbake med det seinere.</p>
<p><strong>Hva overlever proklamafristen?</strong></p>
<p>1. <strong>Eiendomsrettskrav:</strong> En gjenstand i boet som egentlig tilhørte noen andre, kan eieren kreve tilbake uavhengig av fristen.<br>
2. <strong>Panterett:</strong> En bank med pant i boligen mister ikke pantet sitt fordi de ikke meldte innen seks uker. Pantet følger eiendommen.<br>
3. <strong>Tilbakeholdsrett:</strong> Den som lovlig holder tilbake en gjenstand som sikkerhet, beholder den retten.</p>""",
        "eksempler": [{"navn": "Marius", "tekst": "Marius dør med 50 000 kr i uoppgjort gjeld til en butikk som aldri sendte faktura. Proklamaet kunngjøres. Butikken leser ikke avisen og melder ikke kravet innen seks uker. Kravet faller bort. Arvingene trenger ikke betale det."}],
        "vanlige_feil": ["Som kreditor: ikke følge med på proklamakunngjøringer og miste fristen", "Tro at pant i fast eiendom faller bort — det gjør det ikke"],
        "hva_bor_du_html": "<p>Er du kreditor og vet at debitor er død: sjekk norsklysingblad.no umiddelbart. Seks uker er kort. Meld kravet skriftlig med én gang du ser proklamaet.</p>",
        "dumme_sporsmal": [{"q": "Kan vi som arvinger nekte å betale krav som er meldt for sent?", "a": "Ja — kravet er bortfalt, og du kan avvise det. Det er hele hensikten med proklamaet."}],
        "related": [{"lov": "arveloven", "paragraf": "100", "tittel": "Utstedelse av proklama", "available": True}, {"lov": "arveloven", "paragraf": "103", "tittel": "Forhold som tilsvarer å melde krav", "available": True}],
    },
    {
        "number": "103", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Forhold med samme virkning som å melde krav",
        "kategori": "arv",
        "description": "Trenger du alltid å melde kravet aktivt for å bevare det mot proklamafristen? Nei — i tre situasjoner overlever kravet selv uten aktiv melding.",
        "kort_svar": "Et krav overlever proklamafristen uten aktiv melding i tre situasjoner: arvingene erkjenner kravet, kravet er allerede meldt under gjeldsforhandling eller konkurs, eller kreditor har saksøkt arvingene.",
        "paragraftekst": "Samme virkning som å melde krav har det: a. at arvingene erkjenner kravets riktighet, b. at kravet er meldt under gjeldsforhandling eller konkurs i skyldnerens bo hvis dødsfallet fant sted før disse ble avsluttet, c. at sak er anlagt mot arvingene.",
        "hva_betyr_html": """<p>Tre situasjoner der kravet er tilstrekkelig klart uten formell melding:</p>
<p><strong>1. Erkjennelse:</strong> Sier arvingene eller bostyreren til en kreditor at «ja, vi erkjenner at den avdøde skyldte deg dette», er det samme som en melding.<br>
<strong>2. Allerede meldt i konkurs/gjeldsforhandling:</strong> Hadde den avdøde slike prosesser pågående da vedkommende døde og kravet er meldt der, trenger kreditor ikke melde på nytt.<br>
<strong>3. Søksmål:</strong> Har kreditor saksøkt arvingene — selv etter fristens utløp — er kravet bevart.</p>""",
        "eksempler": [],
        "vanlige_feil": ["Erkjenne et krav overfor en kreditor uten å forstå at det bevarer kravet — vær bevisst på hva du sier"],
        "hva_bor_du_html": "<p>Vær varsom med å erkjenne krav fra kreditorer under skiftet — det bevarer kravet deres mot boet selv om proklamafristen har gått ut.</p>",
        "dumme_sporsmal": [],
        "related": [{"lov": "arveloven", "paragraf": "100", "tittel": "Utstedelse av proklama", "available": True}, {"lov": "arveloven", "paragraf": "102", "tittel": "Virkning av proklamaet", "available": True}],
    },
    {
        "number": "104", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Rett til å overta eiendeler og rett til å kreve eiendeler solgt",
        "kategori": "arv",
        "description": "Kan du kreve å overta en bestemt eiendel i boet? Og kan du kreve at ting selges hvis de andre ikke vil? Ja — men begge deler har grenser.",
        "kort_svar": "En arving kan overta bestemte eiendeler fra boet hvis de andre ikke protesterer — eller hvis gode grunner taler for det og de andre ikke har rimelig grunn til å nekte. Enhver arving kan kreve at eiendeler det ikke er enighet om, selges.",
        "paragraftekst": "En arving kan overta bestemte eiendeler i boet hvis det ikke er noen av de andre arvingene som motsetter seg dette. Er det uenighet, kan arvingen overta eiendelen hvis gode grunner taler for det og det ikke er noen rimelig grunn for de andre til å motsette seg det. Enhver arving kan kreve at eiendeler som ikke blir overtatt, selges.",
        "hva_betyr_html": """<p><strong>Uten protest:</strong> Vil du overta hytta eller bilen og ingen protesterer, er den din. Enkel sak.</p>
<p><strong>Med uenighet:</strong> Da kreves to ting: gode grunner for at du skal overta, og at de andres motstand ikke er rimelig begrunnet. Eksempel på god grunn: du har bodd i leiligheten i 20 år. Rimelig motstand: eiendelen er svært verdifull og er sentral for hele arvefordelingen.</p>
<p><strong>Kreve salg:</strong> Hvis ingen vil overta noe, eller dere ikke er enige, kan én enkelt arving kreve at eiendelen selges på det åpne markedet.</p>""",
        "eksempler": [{"navn": "Ola og Anne", "tekst": "Ola og Anne arver etter faren. Anne vil overta hytta — hun har brukt den hvert år i 20 år. Ola protesterer fordi hytta er verdt mye. Retten vurderer: Annes lange bruk er en god grunn. Olas motstand kan være rimelig fordi verdien er stor. Utfallet avhenger av helheten."}],
        "vanlige_feil": ["Tro at en arving automatisk kan overta alt vedkommende vil — de andre kan protestere", "Glemme at man kan kreve salg hvis enighet ikke oppnås"],
        "hva_bor_du_html": "<p>Er det eiendeler du ønsker å overta: si fra tidlig i skiftet og begrunn ønsket. Er det dødlås: vurder om salg er bedre enn en langvarig konflikt.</p>",
        "dumme_sporsmal": [{"q": "Kan jeg overta eiendeler til under markedsverdi?", "a": "Nei — du overtar til verdien partene er enige om, eventuelt fastsatt ved skiftetakst etter § 106."}],
        "related": [{"lov": "arveloven", "paragraf": "105", "tittel": "Verdsettelse av eiendeler", "available": True}, {"lov": "arveloven", "paragraf": "106", "tittel": "Skiftetakst", "available": True}],
    },
    {
        "number": "105", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Verdsettelse av eiendeler",
        "kategori": "arv",
        "description": "Hva er en eiendel i boet verdt når en arving overtar den? Utgangspunktet er hva arvingene er enige om — og tidspunktet for overtakelsen er avgjørende.",
        "kort_svar": "Verdien av en eiendel fastsettes til det arvingene er enige om. Blir de ikke enige, begjæres skiftetakst etter § 106. Verdien settes til tidspunktet det bestemmes hvem som skal overta — ikke dødsfallstidspunktet.",
        "paragraftekst": "Eiendeler i boet overtas til den verdien arvingene er enige om. Når en arving skal overta en eiendel, er det verdien på det tidspunktet da det ble bestemt hvem som skal overta eiendelen, som skal legges til grunn for oppgjøret.",
        "hva_betyr_html": """<p><strong>Enighet er normen:</strong> Ingen krav om megler, takstmann eller domstol hvis alle er fornøyde med verdien.</p>
<p><strong>Tidspunkt: da det bestemmes hvem som overtar:</strong> Verdien settes ikke til dødsfallstidspunktet, men til det tidspunktet det faktisk ble bestemt hvem som overtar. Har det gått måneder eller år — og boligprisene steg — er det den høyere verdien som gjelder.</p>
<p>Jo lenger skiftet trekker ut, jo mer usikkerhet rundt verdien — og jo høyere kan betalingen til de andre arvingene bli.</p>""",
        "eksempler": [{"navn": "Lars", "tekst": "Lars overtar foreldrenes hytte. Da moren døde var hytta verdt 1,2 mill. Det tar to år å bli enige. Hytta har steget til 1,5 mill. Det er 1,5 mill som gjelder for oppgjøret — Lars må betale mer til søsknene enn om skiftet gikk raskt."}],
        "vanlige_feil": ["Tro at verdien låses til dødsfallstidspunktet — det gjør den ikke", "La skiftet trekke ut uten å avklare overtakelsesspørsmålet — det kan koste mer"],
        "hva_bor_du_html": "<p>Er det eiendeler du vil overta: avklar hvem som overtar og fastsett verdien tidlig. Jo lenger du venter, jo mer usikkerhet.</p>",
        "dumme_sporsmal": [{"q": "Kan vi bruke en uformell verdivurdering fra en bekjent megler?", "a": "Ja — arvingene kan avtale hvilken verdsettelse de vil bruke og om den er bindende. Er alle enige, holder en uformell takst."}],
        "related": [{"lov": "arveloven", "paragraf": "104", "tittel": "Rett til å overta eiendeler", "available": True}, {"lov": "arveloven", "paragraf": "106", "tittel": "Skiftetakst ved uenighet", "available": True}],
    },
    {
        "number": "106", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Verdsettelse ved skiftetakst",
        "kategori": "arv",
        "description": "Hva skjer hvis arvingene ikke blir enige om verdien av en eiendel? Da kan en av dem begjære skiftetakst — en formell verdsettelse ved tingretten.",
        "kort_svar": "Er arvingene uenige om verdien, kan en av dem begjære skiftetakst hos tingretten. Tre skjønnsmedlemmer fastsetter da omsetningsverdien. Kostnadene dekkes av boet. Er du uenig i taksten, kan du begjære overtakst.",
        "paragraftekst": "Blir arvingene ikke enige, verdsettes eiendelen ved skiftetakst. Taksten skal svare til eiendelens omsetningsverdi. Skiftetaksten hører under tingretten og holdes av tre skjønnsmedlemmer. Omkostningene ved skiftetaksten dekkes av boet. Overtakst holdes av fire skjønnsmedlemmer.",
        "hva_betyr_html": "<p>Skiftetakst er en formell, bindende verdsettelse under tingretten — ikke det samme som en privat takstmann. Tre skjønnsmedlemmer fastsetter omsetningsverdien: hva en kjøper på det åpne markedet ville betalt.</p><p>Er du sterkt uenig i taksten, kan du begjære overtakst. Da settes retten med en annen dommer og fire skjønnsmedlemmer. Overtaksten er endelig — ingen tredje runde.</p>",
        "eksempler": [{"navn": "Mette og Per", "tekst": "Mette vil overta foreldrenes leilighet. Per mener den er verdt 4 mill, Mette mener 3,4 mill. Per begjærer skiftetakst. Tre skjønnsmedlemmer fastsetter 3,7 mill — det er dette Mette betaler til boet for å overta."}],
        "vanlige_feil": ["Tro at man kan fortsette å forhandle etter at skiftetaksten er fastsatt — den er bindende", "Glemme å begjære overtakst innen fristen hvis man er sterkt uenig"],
        "hva_bor_du_html": "<p>Er du ikke enig i en verdi: begjær skiftetakst. Er du ikke enig i skiftetaksten: vurder overtakst, men husk at overtaksten er endelig.</p>",
        "dumme_sporsmal": [{"q": "Kan vi velge skjønnsmedlemmene selv?", "a": "Nei — de oppnevnes av tingretten fra et fast utvalg."}],
        "related": [{"lov": "arveloven", "paragraf": "105", "tittel": "Verdsettelse ved enighet", "available": True}, {"lov": "arveloven", "paragraf": "107", "tittel": "Oppgjøret etter overtakelse", "available": True}],
    },
    {
        "number": "107", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Oppgjør ved overtakelse av eiendeler",
        "kategori": "arv",
        "description": "Hva gjør du når eiendelen du overtar er verdt mer enn din arvelodd? Du betaler differansen til boet — eller kan utstede en pantobligasjon med sikkerhet i eiendommen.",
        "kort_svar": "Overtar du eiendeler som er verdt mer enn din arveandel, betaler du differansen til boet. For fast eiendom kan du i stedet utstede en pantobligasjon til de andre arvingene. Gammel gjeld til den avdøde avregnes fullt ut i din arv.",
        "paragraftekst": "Den som overtar eiendeler som overstiger verdien av den arven han eller hun har krav på, skal betale det overskytende til boet. Overtar en arving fast eiendom, kan denne arvingen i stedet utstede en fordring til de andre arvingene med pantesikkerhet i eiendommen. En arving må finne seg i at et krav som arvelateren hadde på ham eller henne, avregnes i arven med full verdi.",
        "hva_betyr_html": """<p><strong>Overtar du mer enn arveandelen din?</strong> Du betaler differansen til boet i kontanter, som fordeles på de andre arvingene.</p>
<p><strong>Pantobligasjon som alternativ:</strong> For fast eiendom trenger du ikke betale alt kontant. Du kan utstede en pantobligasjon (gjeldsbrev med pant) til de andre arvingene. Fleksibelt for den som ikke har likvide midler men har formue bundet opp i eiendommen. Obligasjonen kan sies opp av begge parter med seks måneders varsel.</p>
<p><strong>Begrensning:</strong> Pantobligasjon kan ikke brukes i den grad kontant betaling er nødvendig for å dekke den avdødes gjeld.</p>
<p><strong>Gammel gjeld til den avdøde:</strong> Skyldte du den avdøde penger? Det avregnes i din arv med full verdi — du kan ikke forhandle det ned.</p>""",
        "eksempler": [{"navn": "Jonas", "tekst": "Jonas overtar foreldrenes hus til 2 mill. Hans arvelodd er 1,4 mill. Han utsteder pantobligasjon på 600 000 kr til søsknene med sikkerhet i huset. Renten begynner å løpe. Søsknene kan si opp obligasjonen med seks måneders varsel."}],
        "vanlige_feil": ["Tro at man kan forhandle ned gammel gjeld til den avdøde — den avregnes fullt ut"],
        "hva_bor_du_html": "<p>Overtar du fast eiendom og mangler kontanter: avtal pantobligasjon med de andre arvingene. Pass på at tinglysingen er i orden. Søk veiledning hos tingretten.</p>",
        "dumme_sporsmal": [{"q": "Kan jeg bruke pantobligasjon for bil eller andre eiendeler?", "a": "Nei — pantobligasjon er forbeholdt fast eiendom, andel/aksje i boligselskap og lignende borettigheter."}],
        "related": [{"lov": "arveloven", "paragraf": "104", "tittel": "Rett til å overta eiendeler", "available": True}, {"lov": "arveloven", "paragraf": "105", "tittel": "Verdsettelse", "available": True}],
    },
    {
        "number": "108", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Særlige regler for odels- og åsetesrett",
        "kategori": "arv",
        "description": "Har du odels- eller åsetesrett til en eiendom i boet? Du kan kreve å overta den på skiftet — men du må melde fra i tide, og verdsettelsen følger odelsloven.",
        "kort_svar": "En arving med odels- eller åsetesrett kan kreve å overta eiendommen på skiftet. Verdsettelsen følger odelsloven — vanligvis lavere enn markedsverdi. Melder du ikke kravet innen fristen tingretten setter, taper du retten.",
        "paragraftekst": "En arving som har odels- eller åsetesrett, kan kreve å få overta eiendommen på skiftet. Under offentlig skifte kan tingretten sette en frist på inntil seks måneder for arvinger med odels- eller åsetesrett til å melde fra. Den som ikke melder innen fristen, taper retten til odelsløsning overfor den som eiendommen overføres til. Eiendom som overtas på grunnlag av odels- eller åsetesrett, verdsettes etter reglene i odelsloven.",
        "hva_betyr_html": """<p>Odelsrett og åsetesrett er særnorske rettigheter knyttet til landbrukseiendom. Odelsrett gir visse slektninger rett til å løse en eiendom til fastsatt pris. Åsetesrett gir den eldste nedadstigende arving rett til å overta gården på et arveoppgjør til en særskilt verdi.</p>
<p>På skiftet kan en arving med slik rett kreve å overta eiendommen — uavhengig av de andre arvingenes ønsker. Prisen er ikke markedsverdi, men den lavere verdien etter odelsloven.</p>
<p>Under offentlig skifte setter retten en frist — inntil seks måneder — for å melde kravet. Melder du ikke i tide, taper du retten.</p>""",
        "eksempler": [{"navn": "Håkon", "tekst": "Håkon er eldste sønn og har åsetesrett til farens gård. På skiftet krever han å overta gården etter åsetesreglene. Verdsettelsen etter odelsloven gir lavere pris enn markedsverdi. Han betaler differansen til søsknene som pantobligasjon med sikkerhet i gården."}],
        "vanlige_feil": ["Glemme å melde odels- eller åseteskrav innen fristen tingretten setter — du taper retten"],
        "hva_bor_du_html": "<p>Har du odels- eller åsetesrett og vil bruke den: meld kravet tidligst mulig i skifteprosessen. Kontakt advokat med kunnskap om odelsloven for å forstå hva retten gir deg og hva den koster.</p>",
        "dumme_sporsmal": [{"q": "Hva er forskjellen på odelsrett og åsetesrett?", "a": "Odelsrett er en rett til å løse en eiendom fra enhver eier — også ved salg utenfor familie. Åsetesrett gjelder spesifikt på arveoppgjøret og gir den eldste nedadstigende arving rett til å overta gården til særskilt pris."}],
        "related": [{"lov": "arveloven", "paragraf": "104", "tittel": "Rett til å overta eiendeler", "available": True}, {"lov": "arveloven", "paragraf": "99a", "tittel": "Frist for overføring av landbrukseiendom", "available": True}],
    },
    {
        "number": "109", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Delingen av felleseiet",
        "kategori": "arv",
        "description": "Hva skjer med felleseiet mellom ektefeller når den ene dør? Det deles etter ekteskapslovens regler — alltid før selve arveoppgjøret.",
        "kort_svar": "Felleseiet mellom den avdøde og gjenlevende ektefelle deles etter ekteskapslovens regler FØR arven fordeles. Gjenlevende tar ut sin halvdel. Avdødes halvdel er det som inngår i boet og arves.",
        "paragraftekst": "Felleseie mellom arvelaterens dødsbo og arvelaterens ektefelle deles beløpsmessig etter reglene i ekteskapsloven kapittel 15. Felleseiet deles før dødsboet skiftes. Var arvelateren insolvent, er det bare arvelaterens rådighetsdel av felleseiet som anses som hans eller hennes dødsbo.",
        "hva_betyr_html": """<p>To steg når ektefellen dør:</p>
<p><strong>Steg 1 — Del felleseiet:</strong> Gjenlevende ektefelle tar ut sin halvdel av felleseiet. Det som er igjen — avdødes halvdel — er det som inngår i boet og arves.</p>
<p><strong>Steg 2 — Fordel arven:</strong> Avdødes del fordeles mellom arvingene etter arveloven.</p>
<p>Særeie behandles annerledes: eiendeler med særeie deles ikke likt, men inngår direkte i arveoppgjøret for den avdødes del.</p>
<p>Insolvent avdød: er gjelden større enn eiendelene, er det bare avdødes rådighetsdel som er boet — gjenlevende ektefelles andel er beskyttet.</p>""",
        "eksempler": [{"navn": "Kari og Ola", "tekst": "Kari og Ola er gift med felleseie. Felles verdier 4 mill. Ola dør. Kari tar ut halvdelen — 2 mill. De resterende 2 mill er Olas del og inngår i dødsboet som fordeles mellom Kari og eventuelle barn."}],
        "vanlige_feil": ["Tro at all formuen er den avdødes arv — gjenlevende har krav på sin halvdel av felleseiet FØRST", "Glemme at særeie behandles annerledes og ikke deles likt"],
        "hva_bor_du_html": "<p>Er du gjenlevende ektefelle: sørg for at felleseieskiftet gjennomføres riktig FØR arveoppgjøret. Din halvdel av felleseiet er ikke arv — det er ditt eget.</p>",
        "dumme_sporsmal": [{"q": "Hva om vi hadde ektepakt om særeie på alt?", "a": "Da er det ingen felleseieskifte. Alt den avdøde eide inngår direkte i boet. Alt gjenlevende eier er sitt."}],
        "related": [{"lov": "arveloven", "paragraf": "113", "tittel": "Ektefellens rett til å overta eiendeler", "available": True}, {"lov": "arveloven", "paragraf": "14", "tittel": "Ektefellers rett til uskifte", "available": True}],
    },
    {
        "number": "110", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Fortegnelse over eiendeler og forpliktelser",
        "kategori": "arv",
        "description": "Kan tingretten kreve at gjenlevende ektefelle eller samboer lager en oversikt over sin økonomi? Ja — og de må opplyse om hva som er felleseie, særeie og sameie.",
        "kort_svar": "Hvis tingretten ber om det, må gjenlevende ektefelle eller samboer lage en fullstendig oversikt over sine egne eiendeler og forpliktelser, og opplyse om hva som er felleseie, særeie eller sameie.",
        "paragraftekst": "Hvis retten ber om det, skal ektefellen sette opp en fortegnelse over sine eiendeler og forpliktelser og opplyse om eiendelene er felleseie, særeie eller i sameie. Tilsvarende gjelder for gjenlevende samboer.",
        "hva_betyr_html": "<p>For å avklare hva som tilhørte hvem, kan tingretten kreve at gjenlevende setter opp en fullstendig oversikt. Dette er ikke frivillig. For ektefeller er det avgjørende for felleseieskiftet etter § 109. For samboere er det avgjørende å avklare hva som er i sameie.</p>",
        "eksempler": [],
        "vanlige_feil": ["Tro at du bare trenger å oppgi det du vil ha med i skiftet — fortegnelsen skal være fullstendig", "Utelate gjeld — forpliktelser er like viktige å opplyse om som eiendeler"],
        "hva_bor_du_html": "<p>Mottar du henvendelse fra tingretten om fortegnelse: vær grundig og ærlig. Utelater du verdier eller gjeld, kan det skape problemer og i verste fall personlig ansvar.</p>",
        "dumme_sporsmal": [],
        "related": [{"lov": "arveloven", "paragraf": "109", "tittel": "Delingen av felleseiet", "available": True}, {"lov": "arveloven", "paragraf": "91", "tittel": "Registrering og sikring av boets eiendeler", "available": True}],
    },
    {
        "number": "111", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Råderetten over eiendeler under skiftet og vederlag for bruk",
        "kategori": "arv",
        "description": "Kan gjenlevende ektefelle bruke den avdødes eiendeler mens skiftet pågår? Ja — men etter ett år kan det kreves vederlag.",
        "kort_svar": "Gjenlevende ektefelle eller samboer kan bruke egne og felles eiendeler gratis det første året etter dødsfallet. Etter ett år kan arvinger kreve vederlag for bruk av eiendeler som fullt ut tilhørte den avdøde. Felles bolig er gratis frem til det er avklart hvem som overtar.",
        "paragraftekst": "Ektefellen beholder vederlagsfritt råderetten over sine eiendeler under skiftet. Etter ett år kan det kreves vederlag for bruk av eiendeler som fullt ut var eid av arvelateren. Er det ikke avklart hvem som skal overta felles bolig ved utløpet av ettårsfristen, har ektefellen vederlagsfri bruksrett til boligen frem til dette er avklart.",
        "hva_betyr_html": """<p><strong>Det første året — gratis bruk:</strong> Gjenlevende kan bruke alle eiendeler — egne, avdødes og sameieeiendeler — uten vederlag. Rimelig beskyttelse for den som nettopp har mistet sin partner.</p>
<p><strong>Etter ett år:</strong> Arvingene kan kreve at gjenlevende betaler vederlag (leie) for bruk av eiendeler som fullt ut tilhørte den avdøde.</p>
<p><strong>Boligen er unntatt:</strong> Så lenge det ikke er avklart hvem som overtar felles bolig, kan gjenlevende bo der gratis uansett. Du kan ikke kastes ut mens skiftet pågår.</p>""",
        "eksempler": [{"navn": "Eva", "tekst": "Evas mann dør. De bodde i en leilighet i hans navn alene. Eva bor der under skiftet. Etter ett år krever barna vederlag. Eva betaler markedsleie frem til det er avklart hvem som overtar. Overtar Eva — stopper vederlaget."}],
        "vanlige_feil": ["Tro at gjenlevende kan bruke alt gratis i all evighet — etter ett år kan det kreves vederlag", "Tro at arvingene kan kaste ut gjenlevende fra boligen — ikke mens skiftet pågår og overtakelse ikke er avklart"],
        "hva_bor_du_html": "<p>Er du gjenlevende og skiftet trekker ut: avklar overtakelse av boligen og andre eiendeler raskt for å unngå krav om vederlag.</p>",
        "dumme_sporsmal": [{"q": "Kan vi avtale bort retten til å kreve vederlag?", "a": "Ja — paragrafen sier «om ikke noe annet avtales». Arvingene kan frivillig frasi seg vederlaget."}],
        "related": [{"lov": "arveloven", "paragraf": "109", "tittel": "Delingen av felleseiet", "available": True}, {"lov": "arveloven", "paragraf": "113", "tittel": "Ektefellens rett til å overta eiendeler", "available": True}],
    },
    {
        "number": "112", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Kreditorenes dekningsgrunnlag ved ekteskap",
        "kategori": "arv",
        "description": "Kan ektefellens kreditorer ta dekning mens skiftet pågår? Ja — men ikke i eiendeler som skal deles, for gjeld stiftet etter dødsfallet.",
        "kort_svar": "Ektefellens kreditorer kan kreve dekning i ektefellens egne eiendeler mens skiftet pågår. Men for gjeld ektefellen har stiftet etter dødsfallet, kan det ikke tas utlegg i eiendeler som skal deles.",
        "paragraftekst": "Ektefellens kreditorer kan frem til skiftet er avsluttet kreve dekning i hans eller hennes eiendeler. For forpliktelser som ektefellen har pådratt seg etter at arvelateren døde, kan det likevel ikke tas utlegg i eiendeler som skal deles.",
        "hva_betyr_html": "<p>Ektefellens egne kreditorer — gjeld ektefellen hadde fra før dødsfallet — kan fortsatt kreve dekning i ektefellens eiendeler. Men tar ektefellen opp ny gjeld etter at den avdøde er død, kan ikke de nye kreditorene ta utlegg i eiendeler som inngår i skifteoppgjøret. Det beskytter arvingene og den avdødes kreditorer mot at nye kreditorer sniker seg inn i boet.</p>",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "<p>Er du gjenlevende ektefelle og overveier å ta opp ny gjeld mens skiftet pågår: vær klar over at nye kreditorer ikke kan ta dekning i eiendeler som skal deles i skifteoppgjøret.</p>",
        "dumme_sporsmal": [],
        "related": [{"lov": "arveloven", "paragraf": "109", "tittel": "Delingen av felleseiet", "available": True}, {"lov": "arveloven", "paragraf": "116", "tittel": "Ansvaret for arvelaterens forpliktelser", "available": True}],
    },
    {
        "number": "113", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Retten til å overta eiendeler som er i felleseie",
        "kategori": "arv",
        "description": "Har gjenlevende ektefelle rett til å overta boligen og innboet — selv om den avdøde eide dem? Ja — loven gir ektefellen en sterk rett til å overta felles hjem.",
        "kort_svar": "Gjenlevende ektefelle har rett til å overta felles bolig og innbo uavhengig av hvem som eide dem — med mindre det er åpenbart urimelig. Ektefellen har også rett til å overta eiendeler vedkommende selv brakte inn i felleseiet.",
        "paragraftekst": "Ektefellen har rett til å overta bestemte eiendeler som han eller hun fullt ut eller for det vesentlige har brakt inn i felleseiet. Ektefellen har rett til å overta boligeiendom som har vært brukt som felles bolig, løsøre som har hørt til innboet i felles bolig, og løsøre ektefellen trenger til å fortsette sin næring — hvis det ikke vil være åpenbart urimelig. Ved salg til andre enn arvingene har ektefellen forkjøpsrett.",
        "hva_betyr_html": """<p><strong>To rettigheter:</strong></p>
<p>1. <strong>Eiendeler ektefellen brakte inn:</strong> Ting du selv eide og tok med inn i ekteskapet kan du overta — hvis ikke åpenbart urimelig.<br>
2. <strong>Felles bolig og innbo:</strong> Uavhengig av hvem som eide boligen, har du rett til å overta den hvis den var felles hjem. Du risikerer ikke å bli tvunget ut av hjemmet ditt bare fordi det stod i den avdødes navn.</p>
<p>Terskelen «åpenbart urimelig» er høy. Er boligen svært verdifull og arvingene (særlig barn fra tidligere ekteskap) ville bli sterkt skadelidende, kan retten begrenses.</p>""",
        "eksempler": [{"navn": "Mette", "tekst": "Mettes mann eide huset alene — kjøpt før ekteskapet. Mette har bodd der i 20 år. Hun har rett til å overta huset som felles bolig etter § 113, selv om hun aldri var medeier. Hun betaler differansen mellom husets verdi og sin arveandel til boet."}],
        "vanlige_feil": ["Tro at gjenlevende bare kan overta det vedkommende formelt eide — ektefellens rett er bredere", "Glemme at odels- og åsetesberettigede kan ha rettigheter som konkurrerer med ektefellens rett"],
        "hva_bor_du_html": "<p>Er du gjenlevende ektefelle og ønsker å overta boligen: meld dette tidlig i skiftet. Retten er sterk, men dokumenter at boligen faktisk har vært felles hjem.</p>",
        "dumme_sporsmal": [{"q": "Gjelder retten også for hytta?", "a": "Bare hvis hytta har vært brukt som felles bolig. En feriebytte som ikke er fast bosted, faller ikke inn."}],
        "related": [{"lov": "arveloven", "paragraf": "114", "tittel": "Rett til å overta ved særeie", "available": True}, {"lov": "arveloven", "paragraf": "107", "tittel": "Oppgjøret ved overtakelse", "available": True}],
    },
    {
        "number": "114", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Retten til å overta eiendeler ved særeie eller samboerskap",
        "kategori": "arv",
        "description": "Kan gjenlevende ektefelle overta boligen selv om den var den avdødes særeie? Ja — hvis ikke særlige grunner tilsier noe annet. Det samme gjelder noen samboere.",
        "kort_svar": "Selv om boligen og innboet var den avdødes særeie, kan gjenlevende ektefelle overta det — med mindre særlige grunner taler imot. For samboere gjelder tilsvarende rettigheter hvis forholdet dekkes av husstandsfellesskapsloven.",
        "paragraftekst": "Hvis ikke særlige grunner tilsier noe annet, har ektefellen rett til å overta bolig og løsøre som nevnt i § 113 som var arvelaterens særeie. Ved samboerskap som omfattes av husstandsfellesskapsloven § 1, kan den gjenlevende samboeren overta bolig og innbo etter husstandsfellesskapsloven § 2.",
        "hva_betyr_html": """<p><strong>Særeie hindrer ikke overtakelse:</strong> Har ektefellene avtalt særeie på boligen, inngår den i arven. Men gjenlevende har rett til å overta den likevel — terskelen er «særlige grunner», som er lavere enn «åpenbart urimelig» etter § 113. Den som vil nekte overtakelse, må begrunne det.</p>
<p><strong>Samboere:</strong> Samboere har ikke de samme lovfestede rettighetene som ektefeller. Men er samboerskapet av en viss varighet og karakter — slik at det faller inn under husstandsfellesskapsloven — gir loven gjenlevende samboer rett til å overta bolig og innbo.</p>""",
        "eksempler": [{"navn": "Anne", "tekst": "Annes mann arvet hytta som særeie. I 15 år brukte de den som felles sommerhjem. Mannen dør. Barna fra hans første ekteskap vil ha hytta. Anne krever å overta den etter § 114. Barna har ingen særlig grunn som tilsier at dette er urimelig. Anne overtar og betaler overskuddet til boet."}],
        "vanlige_feil": ["Tro at særeie alltid utelukker ektefellens rett til å overta — det gjør det ikke", "Som samboer tro at man har de samme rettighetene som ektefeller automatisk"],
        "hva_bor_du_html": "<p>Er du gjenlevende ektefelle og boligen er særeie: krev retten etter § 114 tidlig. Er du samboer: undersøk om forholdet faller inn under husstandsfellesskapsloven.</p>",
        "dumme_sporsmal": [{"q": "Kan gjenlevende ektefelle overta særeie-boligen mot arvingenes vilje?", "a": "Ja, hvis det ikke er særlige grunner mot det. Er arvingene uenige, kan det bli en tvist tingretten avgjør."}],
        "related": [{"lov": "arveloven", "paragraf": "113", "tittel": "Retten til å overta felleseiemidler", "available": True}, {"lov": "arveloven", "paragraf": "107", "tittel": "Oppgjøret ved overtakelse", "available": True}],
    },
    {
        "number": "115", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Tidspunktet for verdsettelse av eiendeler ved ektefelleskifte",
        "kategori": "arv",
        "description": "Hvilket tidspunkt gjelder for verdifastsettelsen av eiendeler i et ektefelleskifte? Det avhenger av om ektefellen beholder egne eiendeler eller overtar fra boet.",
        "kort_svar": "Beholder ektefellen sine egne eiendeler, brukes verdien ved dødsfallet. Overtar ektefellen eiendeler fra boet, brukes verdien på det tidspunktet det bestemmes hvem som overtar.",
        "paragraftekst": "Når ektefellen beholder egne eiendeler, er det verdien på tidspunktet for arvelaterens død som skal legges til grunn. I andre tilfeller er det verdien på det tidspunktet det blir bestemt hvem som skal overta eiendelen.",
        "hva_betyr_html": """<p>To ulike tidspunkter:</p>
<p><strong>Egne eiendeler (beholder):</strong> Verdien settes til dødsfallstidspunktet — det er det tidspunktet delingen av felleseiet gjøres opp etter.</p>
<p><strong>Overtakelse fra boet:</strong> Verdien settes til det tidspunktet det bestemmes at ektefellen skal overta. Det kan ha gått lang tid. Har boligen steget, betaler ektefellen mer.</p>
<p>Arvingene kan avtale et annet tidspunkt — er boet stort, kan det lønne seg å låse verdien tidlig for å unngå usikkerhet.</p>""",
        "eksempler": [],
        "vanlige_feil": ["Tro at alt verdsettes til dødsfallstidspunktet — det gjelder bare egne eiendeler", "La skiftet trekke ut uten å låse verdien tidlig"],
        "hva_bor_du_html": "<p>Er det eiendeler du vil overta: avklar hvem som overtar og fastsett verdien tidlig. Jo lenger du venter, jo mer usikkerhet om endelig pris.</p>",
        "dumme_sporsmal": [],
        "related": [{"lov": "arveloven", "paragraf": "105", "tittel": "Verdsettelse av eiendeler generelt", "available": True}, {"lov": "arveloven", "paragraf": "109", "tittel": "Delingen av felleseiet", "available": True}],
    },
    {
        "number": "116", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Ansvaret for arvelaterens forpliktelser ved privat skifte",
        "kategori": "arv",
        "description": "Hva skjer med den avdødes gjeld når du velger privat skifte? Minst én arving må påta seg personlig ansvar — og det ansvaret er ubegrenset.",
        "kort_svar": "For å gjennomføre privat skifte må minst én myndig arving påta seg personlig, ubegrenset ansvar for den avdødes gjeld. De andre arvingene hefter bare inntil verdien av sin arv. Er boet lite (under 3G), er ansvaret begrenset til boets eiendeler.",
        "paragraftekst": "Skal boet skiftes privat, må minst én av de myndige arvingene påta seg ansvaret for arvelaterens forpliktelser. Påtar flere arvinger seg dette ansvaret, er de fullt og solidarisk ansvarlige overfor kreditorene. De øvrige arvingene er ansvarlige bare inntil verdien av sin arv. Hvis boets eiendeler antas å være verdt mindre enn tre ganger grunnbeløpet i folketrygden, er ansvaret begrenset til boets eiendeler.",
        "hva_betyr_html": """<p><strong>Det store valget:</strong> Privat skifte forutsetter at noen tar ansvaret for den avdødes gjeld. Du MÅ aktivt erklære dette overfor tingretten.</p>
<p><strong>Personlig, ubegrenset ansvar:</strong> Påtar du deg ansvaret, hefter du med din private formue for all gjeld den avdøde etterlater — uavhengig av hva du arver. Har den avdøde mer gjeld enn verdier, kan du tape penger.</p>
<p><strong>De andre arvingene:</strong> Hefter bare inntil verdien av sin arv.</p>
<p><strong>Solidaransvar:</strong> Påtar flere seg ansvaret, hefter de solidarisk — kreditorene kan kreve hele beløpet fra hvem som helst av dem.</p>
<p><strong>Lite bo:</strong> Er boets eiendeler under ca. 370 000 kr (3G), er ansvaret begrenset til boets eiendeler. Du riskerer ikke egne penger.</p>""",
        "eksempler": [{"navn": "Lars", "tekst": "Lars påtar seg ansvaret for morens forpliktelser under privat skifte. Det viser seg at moren hadde ukjent gjeld på 180 000 kr til et inkassobyrå. Lars hefter for dette med sin private formue — selv om han bare arver 50 000 kr fra boet."}],
        "vanlige_feil": ["Påta seg ansvaret uten å undersøke om det kan finnes skjult gjeld", "Tro at alle arvingene automatisk hefter likt — bare de som aktivt påtar seg ansvaret hefter ubegrenset"],
        "hva_bor_du_html": "<p>FØR du påtar deg ansvaret: skaff full oversikt over den avdødes økonomi via formuesfullmakt (§ 92). Sjekk Gjeldsregisteret. Er det mistanke om stor ukjent gjeld: vurder offentlig skifte.</p>",
        "dumme_sporsmal": [{"q": "Hva skjer hvis ingen vil påta seg ansvaret?", "a": "Da kan ikke boet skiftes privat. Tingretten åpner offentlig skifte, der ingen arving hefter personlig utover arven sin."}],
        "related": [{"lov": "arveloven", "paragraf": "117", "tittel": "Fristen for privat skifte", "available": True}, {"lov": "arveloven", "paragraf": "118", "tittel": "Skifteattesten", "available": True}],
    },
    {
        "number": "117", "lov": "arveloven", "lov_display": "Arveloven",
        "title": "Frist for å kreve privat skifte",
        "kategori": "arv",
        "description": "Hvor lang tid har arvingene på å velge privat skifte? 60 dager fra dødsfallet — og gjøres det ikke, åpner tingretten offentlig skifte av eget tiltak.",
        "kort_svar": "En arving må påta seg ansvaret for den avdødes forpliktelser innen 60 dager etter dødsfallet for at boet skal skiftes privat. Gjøres ikke dette innen fristen, åpner tingretten offentlig skifte av eget tiltak.",
        "paragraftekst": "Innen 60 dager etter dødsfallet eller innen en annen frist som retten setter, må en arving ha påtatt seg ansvaret for arvelaterens forpliktelser etter § 116 første ledd hvis boet skal skiftes privat.",
        "hva_betyr_html": """<p>60 dager er ikke lang tid etter et dødsfall. Men fristen er avgjørende: innen den MÅ minst én arving ha erklært overfor tingretten at vedkommende påtar seg gjeldansvaret — og dermed utløst prosessen med privat skifte.</p>
<p>Gjør ingen det: tingretten åpner offentlig skifte av eget tiltak. Det er dyrere og arvingene mister kontrollen over prosessen.</p>
<p><strong>Fristen kan endres:</strong> Tingretten kan sette en kortere eller lengre frist. Trenger dere mer tid: ta kontakt med tingretten innen 60 dager og be om forlengelse.</p>""",
        "eksempler": [{"navn": "Marius", "tekst": "Faren dør 1. mars. Marius og søsknene bruker de første ukene på sorgarbeid og begravelse. 28. april — to dager før fristen — kontakter Marius tingretten og erklærer at han påtar seg ansvaret for farens forpliktelser. Privat skifte settes i gang."}],
        "vanlige_feil": ["Tro at 60-dagersfristen begynner fra begravelsen eller skifteoppstarten — den begynner fra dødsdatoen", "Vente med å kontakte tingretten til etter fristen — be heller om forlengelse i god tid"],
        "hva_bor_du_html": "<p>Straks etter dødsfallet: avklar hvem av arvingene som vil påta seg gjeldansvaret. Kontakt tingretten innen 60 dager — enten for å erklære ansvaret, eller for å be om forlengelse.</p>",
        "dumme_sporsmal": [{"q": "Hva om det er uenighet blant arvingene om hvem som skal påta seg ansvaret?", "a": "Én arving kan gjøre det alene — det krever ikke enstemmighet."}],
        "related": [{"lov": "arveloven", "paragraf": "116", "tittel": "Ansvaret for forpliktelsene", "available": True}, {"lov": "arveloven", "paragraf": "118", "tittel": "Skifteattesten", "available": True}],
    },
]

PARAGRAPHS = PARAGRAPHS + _ARVELOVEN_83_117



_ARVELOVEN_118_166 = [

    {'number': '118', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Utstedelse av skifteattest', 'kategori': 'arv', 'description': 'Hva er en skifteattest, og hvordan får du den? Skifteattesten er nøkkelen til boet ved privat skifte — den gir deg rett til å disponere den avdødes eiendeler.', 'kort_svar': 'Skifteattesten utstedes av tingretten etter at 60-dagersfristen er ute, og gir deg legitimasjon til å disponere den avdødes eiendeler. Den utstedes til arvingen som har påtatt seg gjeldansvaret — eller til testamentsfullbyrderen.', 'paragraftekst': 'Skifteattesten utstedes av tingretten etter at 60-dagersfristen er ute, og gir deg legitimasjon til å disponere den avdødes eiendeler. Den utstedes til arvingen som har påtatt seg gjeldansvaret — eller til testamentsfullbyrderen.', 'hva_betyr_html': '<p>Skifteattesten er dokumentet som formelt åpner for privat skifte. Med den i hånden kan du gå til banken og disponere den avdødes konti, tinglyse eiendomsoverdragelse, og avvikle avtaler i den avdødes navn.</p><p><strong>Hvem får skifteattesten?</strong> Den utstedes til arvingen som har påtatt seg gjeldansvaret. Er dere enige, kan dere utpeke én. Er det testamentsfullbyrder, utstedes attesten til vedkommende.</p><p><strong>Når?</strong> Normalt etter 60-dagersfristen — men er alle arvingene enige, kan den utstedes tidligere.</p><p>Skifteattesten gir deg selvstendig rett til innsyn i den avdødes skatteforhold og økonomi. Vesentlige feil kan kreves rettet. Avslag kan ankes.</p>', 'eksempler': [{'navn': 'Marius og Sofie', 'tekst': 'Marius påtar seg gjeldansvaret innen 60 dager. Tingretten utsteder skifteattesten til Marius. Med attesten går han til banken, får oversikt over konti og begynner å rydde opp.'}], 'vanlige_feil': ['Tro at du kan disponere den avdødes eiendeler uten skifteattest — bankene krever den', 'Søke om skifteattest uten å ha påtatt seg gjeldansvaret', 'Glemme at skifteattesten kan utstedes til én person selv om det er flere arvinger'], 'hva_bor_du_html': '<p>Innen 60 dager: påta deg gjeldansvaret overfor tingretten og be om skifteattesten. Haster det: be alle arvingene samtykke til tidlig utstedelse.</p>', 'dumme_sporsmal': [{'q': 'Kan jeg bruke skifteattesten til å ta ut penger?', 'a': 'Ja — men pengene tilhører boet og skal fordeles etter skiftet, ikke brukes til eget formål.'}, {'q': 'Kan skifteattesten trekkes tilbake?', 'a': 'Ja — oppdages det vesentlige feil, kan attesten rettes. Åpnes offentlig skifte etterpå, oppheves rettsvirkningene.'}], 'related': [{'lov': 'arveloven', 'paragraf': '116', 'tittel': 'Ansvaret for forpliktelsene', 'available': True}, {'lov': 'arveloven', 'paragraf': '117', 'tittel': 'Fristen for privat skifte', 'available': True}, {'lov': 'arveloven', 'paragraf': '97', 'tittel': 'Uskifteattest', 'available': True}]},

    {'number': '119', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Oppgaver ved gjennomføringen av et privat skifte', 'kategori': 'arv', 'description': 'Hva skal egentlig gjøres under et privat skifte? § 119 gir en detaljert sjekkliste over oppgavene arvingene må gjennomføre fra start til slutt.', 'kort_svar': 'Under et privat skifte skal arvingene kartlegge arvinger og eiendeler, betale gjeld, oppfylle testament, fordele eiendeler og overføre dem til de rette. Alt skal gjøres innen rimelig tid og dokumenteres.', 'paragraftekst': 'Under et privat skifte skal arvingene kartlegge arvinger og eiendeler, betale gjeld, oppfylle testament, fordele eiendeler og overføre dem til de rette. Alt skal gjøres innen rimelig tid og dokumenteres.', 'hva_betyr_html': '<p>Sjekklisten: (1) Kartlegg arvingene og arveretten. (2) Kartlegg økonomi — eiendeler og gjeld. (3) Oppfyll testamentet. (4) Ta vare på eiendelene — forsikre, hold boligen i stand. (5) Vurder proklama. (6) Avslutt løpende forpliktelser — abonnementer, strøm, forsikringer. (7) Lever skattemelding for inneværende og foregående år. (8) Dekk gjeld og fordel — betal, avklar, signer fordelingsavtale. (9) Overfør eiendeler — tinglys eiendom, omregistrer kjøretøy.</p>', 'eksempler': [{'navn': 'Anne', 'tekst': 'Anne og broren Lars gjennomfører privat skifte etter moren. De skaffer formuesfullmakt, sier opp abonnementer, leverer skattemeldingen, avtaler hvem som overtar hytta, signerer fordelingsavtalen. Anne tinglyser overdragelsen.'}], 'vanlige_feil': ['Glemme å si opp løpende abonnementer', 'Ikke levere skattemeldingen for avdøde — dette er en plikt', 'Ikke dokumentere fordelingen skriftlig', 'Glemme omregistrering av kjøretøy'], 'hva_bor_du_html': '<p>Lag en sjekkliste og kryss av punktene etter hvert. Dokumenter alt skriftlig, særlig fordelingsavtalen. Sørg for tinglysing og omregistrering før skiftet anses avsluttet.</p>', 'dumme_sporsmal': [{'q': 'Hva er «innen rimelig tid»?', 'a': 'Et år er normalt tilstrekkelig for enkle boer.'}, {'q': 'Må vi bruke advokat?', 'a': 'Nei — privat skifte er designet for å gjennomføres uten advokat i enkle boer.'}], 'related': [{'lov': 'arveloven', 'paragraf': '118', 'tittel': 'Skifteattesten', 'available': True}, {'lov': 'arveloven', 'paragraf': '122', 'tittel': 'Dekning av forpliktelser', 'available': True}, {'lov': 'arveloven', 'paragraf': '124', 'tittel': 'Oppfyllelse av testament', 'available': True}]},

    {'number': '120', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Krav om enighet for beslutninger under skiftet', 'kategori': 'arv', 'description': 'Må arvingene være enige om alt under et privat skifte? Ja — men det finnes unntak for arvinger som ikke svarer, og én arving kan handle alene i nødstilfeller.', 'kort_svar': 'Alle beslutninger under et privat skifte krever enighet mellom arvingene. Arvinger med ukjent adresse eller som ikke svarer holdes utenfor kravet. Én arving kan alltid handle alene for å verne verdier i boet.', 'paragraftekst': 'Alle beslutninger under et privat skifte krever enighet mellom arvingene. Arvinger med ukjent adresse eller som ikke svarer holdes utenfor kravet. Én arving kan alltid handle alene for å verne verdier i boet.', 'hva_betyr_html': '<p><strong>Enighet er normen:</strong> Under privat skifte bestemmer arvingene alt selv. Vil dere gjøre det enklere, gi én arving skriftlig fullmakt til å ta beslutninger på alles vegne.</p><p><strong>Unntak 1 — Arving som ikke svarer:</strong> Er en arving utilgjengelig, kan dere gå videre uten vedkommende. Vedkommende mister ikke arven sin; andelen settes av etter § 125.</p><p><strong>Unntak 2 — Nødstiltak:</strong> Haster noe kan én arving handle alene — begrenset til nødvendige og forholdsmessige tiltak.</p>', 'eksempler': [{'navn': 'Per og Jonas', 'tekst': 'Per og Jonas arver etter faren. Jonas bor i utlandet og svarer ikke. Per selger bilen for å dekke regninger. Etter gjentatte forsøk på kontakt beslutter Per salget alene — lovlig etter unntak for arving som ikke svarer.'}], 'vanlige_feil': ['Tro at én arving kan bestemme alt alene — enighet er normen', 'Tro at arving som ikke svarer mister arven sin — det gjør vedkommende ikke'], 'hva_bor_du_html': '<p>Er en medarving vanskelig å nå: dokumenter forsøkene. Etter tilstrekkelig forsøk kan du ta avgjørelser uten vedkommende. Haster noe: hold deg innenfor nødvendig og forholdsmessig.</p>', 'dumme_sporsmal': [{'q': 'Hva hvis tre er enige men én nekter?', 'a': 'Da er det ikke enighet. Løsningen er å kreve offentlig skifte.'}], 'related': [{'lov': 'arveloven', 'paragraf': '125', 'tittel': 'Arving som er forsvunnet', 'available': True}, {'lov': 'arveloven', 'paragraf': '127', 'tittel': 'Hvem kan kreve offentlig skifte', 'available': True}]},

    {'number': '121', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Proklama ved privat skifte', 'kategori': 'arv', 'description': 'Kan arvingene kunngjøre en frist for kreditorer under et privat skifte? Ja — én arving kan alene kreve proklama, og det kan gjøres selv etter at skiftet er avsluttet.', 'kort_svar': 'Under privat skifte kan én arving alene kreve at det kunngjøres en proklamafrist for kreditorer. Kreditorer som ikke melder krav innen seks uker, mister dem.', 'paragraftekst': 'Under privat skifte kan én arving alene kreve at det kunngjøres en proklamafrist for kreditorer. Kreditorer som ikke melder krav innen seks uker, mister dem.', 'hva_betyr_html': '<p>Proklama under privat skifte er frivillig — men én arving kan kreve det alene uten de andres samtykke. Kunngjøringen skjer i Norsk lysingsblad og lokal avis. <strong>Særtrekk:</strong> Proklama kan kunngjøres selv etter at privat skifte er avsluttet.</p>', 'eksempler': [], 'vanlige_feil': ['Anta at proklama er unødvendig fordi boet virker enkelt', 'Tro at alle arvingene må ønske proklama — én arving er nok'], 'hva_bor_du_html': '<p>Er du usikker på om den avdøde kan ha hatt ukjent gjeld: kunngjør proklama. Du kan gjøre det alene.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '100', 'tittel': 'Utstedelse av proklama', 'available': True}, {'lov': 'arveloven', 'paragraf': '102', 'tittel': 'Virkning av proklamaet', 'available': True}, {'lov': 'arveloven', 'paragraf': '122', 'tittel': 'Dekning av forpliktelser', 'available': True}]},

    {'number': '122', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Dekning av boets og arvelaterens forpliktelser', 'kategori': 'arv', 'description': 'Hva betales først når boet har gjeld? Loven setter en klar rekkefølge: begravelse, skiftekostnader, prioriterte krav — og til sist resten.', 'kort_svar': 'Arvingene skal sørge for at all gjeld betales under skiftet. Rekkefølgen er fastsatt: (1) begravelsesomkostninger, (2) skiftekostnader og massekrav, (3) fortrinnsberettigede krav, (4) øvrig gjeld.', 'paragraftekst': 'Arvingene skal sørge for at all gjeld betales under skiftet. Rekkefølgen er fastsatt: (1) begravelsesomkostninger, (2) skiftekostnader og massekrav, (3) fortrinnsberettigede krav, (4) øvrig gjeld.', 'hva_betyr_html': '<p>Rekkefølgen er obligatorisk når boet er insolvent: (1) Begravelse betales aller først. (2) Skiftekostnader og massekrav. (3) Fortrinnsberettigede krav etter dekningsloven — typisk lønnskrav. (4) Øvrig gjeld: banklån, kredittkort, private lån. Du betaler øverste nivå fullt ut og det som er igjen går til neste nivå. Arvingen som har påtatt seg gjeldansvaret hefter personlig for det resterende.</p>', 'eksempler': [{'navn': 'Lars', 'tekst': 'Boet har 180 000 kr. Begravelsen kostet 45 000 kr. Banklån 80 000 kr, kredittkortgjeld 60 000 kr. Etter begravelse og skiftekostnader er det 120 000 kr igjen — ikke nok til alt. Lars betaler banklånet fullt ut, kredittkortgjelden delvis. Differansen hefter Lars for personlig.'}], 'vanlige_feil': ['Begynne å dele ut arv uten å ha sikret at all gjeld er betalt', 'Betale tilfeldige kreditorer uten å følge prioriteringsrekkefølgen'], 'hva_bor_du_html': '<p>Skaff full oversikt over gjelden FØR noe deles ut. Betal i riktig rekkefølge. Er du usikker på solvens: kunngjør proklama og vent til fristen er ute.</p>', 'dumme_sporsmal': [{'q': 'Kan vi dele ut arv og la kreditorene vente?', 'a': 'Nei — gjelden skal dekkes før arven deles ut. Deler du ut og kreditorer går glipp av dekning, kan du bli personlig ansvarlig.'}], 'related': [{'lov': 'arveloven', 'paragraf': '116', 'tittel': 'Personlig ansvar for forpliktelsene', 'available': True}, {'lov': 'arveloven', 'paragraf': '123', 'tittel': 'Rett til å kreve dekning før utdeling', 'available': True}, {'lov': 'arveloven', 'paragraf': '124', 'tittel': 'Oppfyllelse av testament', 'available': True}]},

    {'number': '123', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Rett til å kreve at forpliktelsene dekkes før utdeling av arv', 'kategori': 'arv', 'description': 'Kan du kreve at gjelden betales før noen arving får utdelt noe? Ja — den som har påtatt seg gjeldansvaret kan stanse utdeling til gjelden er ordnet.', 'kort_svar': 'Arvingen som har påtatt seg gjeldansvaret kan kreve at all forfalt gjeld betales — og at det avsettes midler for fremtidig gjeld — FØR arven deles ut.', 'paragraftekst': 'Arvingen som har påtatt seg gjeldansvaret kan kreve at all forfalt gjeld betales — og at det avsettes midler for fremtidig gjeld — FØR arven deles ut.', 'hva_betyr_html': '<p>Du kan stoppe utdeling av arv inntil all gjeld er betalt eller sikret. For forfalt gjeld: den betales FØR noe deles ut. For fremtidig gjeld: det avsettes et beløp — unntak er gjeld som allerede er pantesikret.</p>', 'eksempler': [{'navn': 'Jonas', 'tekst': 'Jonas har påtatt seg gjeldansvaret. Søsteren Anne vil ta ut arveandelen sin nå. Jonas vet om en ubetalt faktura og et lån som forfaller om to måneder. Jonas krever at begge er betalt eller avsatt FØR Anne tar ut noe. Jonas har retten på sin side.'}], 'vanlige_feil': ['Som ansvarlig arving akseptere at de andre tar ut arv uten at gjelden er sikret — du hefter personlig for resten'], 'hva_bor_du_html': '<p>Har du påtatt deg gjeldansvaret: ikke la noen ta ut arv før all gjeld er betalt eller avsatt. Det er din rett og din beskyttelse.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '116', 'tittel': 'Personlig ansvar', 'available': True}, {'lov': 'arveloven', 'paragraf': '122', 'tittel': 'Dekning av forpliktelser', 'available': True}]},

    {'number': '124', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Oppfyllelse av bestemmelser i testament', 'kategori': 'arv', 'description': 'Når skal testamentariske krav oppfylles under et privat skifte? Etter at kreditorene er dekket — og før resten av arven fordeles mellom lovarvingene.', 'kort_svar': 'Testamentariske krav oppfylles etter at gjelden er betalt og sikret, men FØR resten av arven fordeles. Er det ikke nok midler, avkortes testamentariske krav forholdsmessig.', 'paragraftekst': 'Testamentariske krav oppfylles etter at gjelden er betalt og sikret, men FØR resten av arven fordeles. Er det ikke nok midler, avkortes testamentariske krav forholdsmessig.', 'hva_betyr_html': '<p>Rekkefølge: gjeld betales → testamentariske krav oppfylles → resten til lovarvingene. Er det ikke nok til alle testamentariske krav, avkortes de forholdsmessig. Unntak: arving som skal ha en bestemt ting, går foran arving som skal ha en pengesum.</p>', 'eksempler': [{'navn': 'Mette', 'tekst': 'Testamentet: 100 000 kr til en kreftorganisasjon og et maleri til venninnen Sofie. Boet er 600 000 kr etter gjelden. Organisasjonen får 100 000 kr. Sofie får maleriet. Resten til lovarvingene.'}], 'vanlige_feil': ['Fordele arven mellom lovarvingene uten å ha oppfylt testamentariske krav — feil rekkefølge'], 'hva_bor_du_html': '<p>Gjennomgå testamentet nøye tidlig i skiftet. List opp alle testamentariske krav og sørg for at de oppfylles etter at gjelden er betalt.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '122', 'tittel': 'Dekning av forpliktelser', 'available': True}, {'lov': 'arveloven', 'paragraf': '40', 'tittel': 'Opprettelse av testament', 'available': True}]},

    {'number': '125', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Arving som er forsvunnet eller uten kjent oppholdssted', 'kategori': 'arv', 'description': 'Hva gjøres med arven til en arving som er forsvunnet? Under privat skifte settes arven av og forvaltes etter reglene for offentlig skifte.', 'kort_svar': 'Er en arving forsvunnet eller uten kjent adresse etter arvefallet, skal andelen settes av i skifteoppgjøret. De andre arvingene kan ikke ta arven.', 'paragraftekst': 'Er en arving forsvunnet eller uten kjent adresse etter arvefallet, skal andelen settes av i skifteoppgjøret. De andre arvingene kan ikke ta arven.', 'hva_betyr_html': '<p>Er en arving umulig å finne, stopper ikke skiftet — men arvingen kan ikke ignoreres. Andelen settes av og forvaltes etter § 146. Dukker vedkommende opp, kan de kreve sin del innen ti år etter dødsfallet (§ 71).</p>', 'eksempler': [], 'vanlige_feil': ['Inkludere den fraværende arvingens andel i fordelingen mellom de andre — det er ulovlig'], 'hva_bor_du_html': '<p>Er det en arving du ikke kan finne: dokumenter forsøkene, sett av andelen formelt, og ta kontakt med tingretten for veiledning.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '68', 'tittel': 'Fraværende arving', 'available': True}, {'lov': 'arveloven', 'paragraf': '146', 'tittel': 'Forvaltning av arv satt av til forsvunnet arving', 'available': True}, {'lov': 'arveloven', 'paragraf': '71', 'tittel': 'Foreldelse av arverett', 'available': True}]},

    {'number': '126', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Tvister under privat skifte', 'kategori': 'arv', 'description': 'Hva skjer hvis arvingene tvistes om noe under et privat skifte? Boet har ikke partsevne — det er arvingene som saksøker hverandre etter tvistelovens vanlige regler.', 'kort_svar': 'Under privat skifte er det arvingene selv — ikke boet — som er parter i en tvist. Tvisten behandles etter tvistelovens regler. En rettskraftig avgjørelse binder alle med interesser i boet.', 'paragraftekst': 'Under privat skifte er det arvingene selv — ikke boet — som er parter i en tvist. Tvisten behandles etter tvistelovens regler. En rettskraftig avgjørelse binder alle med interesser i boet.', 'hva_betyr_html': '<p>Under privat skifte er det arvingene selv som saksøker eller saksøkes — boet er ikke et rettssubjekt. En rettskraftig dom binder alle i boet; én dom kan endre hele fordelingen. Er skiftet fastlåst: vurder offentlig skifte (§ 127).</p>', 'eksempler': [], 'vanlige_feil': ['Tro at man kan saksøke «boet» under privat skifte — det har ikke partsevne'], 'hva_bor_du_html': '<p>Er det uenighet om vesentlige spørsmål: prøv å løse det internt. Lykkes ikke det, kontakt advokat — eller vurder offentlig skifte.</p>', 'dumme_sporsmal': [{'q': 'Kan én arving kreve offentlig skifte midt i et privat skifte?', 'a': 'Ja — retten til å kreve offentlig skifte faller ikke bort fordi privat skifte er påbegynt, så lenge det ikke er avsluttet.'}], 'related': [{'lov': 'arveloven', 'paragraf': '127', 'tittel': 'Hvem kan kreve offentlig skifte', 'available': True}]},

    {'number': '127', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Hvem som kan kreve offentlig skifte', 'kategori': 'arv', 'description': 'Hvem har rett til å kreve at et dødsbo skiftes offentlig? Enhver arving kan gjøre det — og også visse kreditorer og statsforvalteren.', 'kort_svar': 'En arving kan alltid kreve offentlig skifte — alene, uten begrunnelse, uavhengig av hva de andre mener. Det samme kan visse kreditorer og statsforvalteren på vegne av arvinger under vergemål.', 'paragraftekst': 'En arving kan alltid kreve offentlig skifte — alene, uten begrunnelse, uavhengig av hva de andre mener. Det samme kan visse kreditorer og statsforvalteren på vegne av arvinger under vergemål.', 'hva_betyr_html': '<p><strong>Absolutt arvingerett:</strong> Enhver arving kan kreve offentlig skifte alene, uten begrunnelse, uavhengig av de andres mening.</p><p><strong>Kreditorer:</strong> Ingen tok privat skifte innen 60-dagersfristen, eller arvingene truer dekningen.</p><p><strong>Mindreårige og umyndige:</strong> Vergen krever offentlig skifte for å beskytte dem.</p><p><strong>Merk:</strong> Retten faller bort tre år etter dødsfallet (§ 130).</p>', 'eksempler': [{'navn': 'Jonas', 'tekst': 'Jonas mistenker at søsteren Anne skjuler eiendeler. Jonas krever offentlig skifte alene. Tingretten åpner det. Jonas trenger ikke Annes samtykke.'}], 'vanlige_feil': ['Tro at man trenger de andres samtykke for å kreve offentlig skifte — det gjør man ikke', 'Tro at retten varer evig — den faller bort tre år etter dødsfallet'], 'hva_bor_du_html': '<p>Er du arving og frustrert over et privat skifte som ikke fungerer: kontakt tingretten og krev offentlig skifte. Du trenger ikke advokat for å fremsette kravet.</p>', 'dumme_sporsmal': [{'q': 'Koster det noe å kreve offentlig skifte?', 'a': 'Du må stille sikkerhet for skifteomkostningene etter § 132 — med mindre boet åpenbart kan dekke dem selv.'}], 'related': [{'lov': 'arveloven', 'paragraf': '128', 'tittel': 'Testamentarisk bestemmelse om offentlig skifte', 'available': True}, {'lov': 'arveloven', 'paragraf': '130', 'tittel': 'Bortfall av retten til offentlig skifte', 'available': True}]},

    {'number': '128', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Arvelaterens adgang til å bestemme offentlig skifte', 'kategori': 'arv', 'description': 'Kan arvelateren i testamentet bestemme at boet skal skiftes offentlig? Ja — og det binder alle arvingene, også livsarvingene og ektefellen.', 'kort_svar': 'En arvelater kan i testament bestemme at boet skal gjennomgå offentlig skifte. Den bestemmelsen er bindende for alle arvingene — ingen kan velge privat skifte mot arvelaterens vilje.', 'paragraftekst': 'En arvelater kan i testament bestemme at boet skal gjennomgå offentlig skifte. Den bestemmelsen er bindende for alle arvingene — ingen kan velge privat skifte mot arvelaterens vilje.', 'hva_betyr_html': '<p>Velger arvelateren offentlig skifte i testamentet, er det bindende for absolutt alle. Typisk brukt der arvelateren frykter konflikt, vil at en nøytral tredjepart styrer fordelingen, eller ønsker å beskytte svakere arvinger.</p>', 'eksempler': [{'navn': 'Mette', 'tekst': 'Mette frykter konflikt mellom barna sine fra to ekteskap. Hun bestemmer offentlig skifte i testamentet. Selv om alle barna er enige om privat skifte, er bestemmelsen bindende. Tingretten overtar.'}], 'vanlige_feil': ['Tro at en testamentarisk bestemmelse om offentlig skifte kan settes til side av livsarvingene — det kan den ikke'], 'hva_bor_du_html': '<p>Frykter du at arveoppgjøret etter deg vil bli konfliktfylt: inkluder bestemmelse om offentlig skifte i testamentet.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '127', 'tittel': 'Hvem kan kreve offentlig skifte', 'available': True}, {'lov': 'arveloven', 'paragraf': '40', 'tittel': 'Opprettelse av testament', 'available': True}]},

    {'number': '129', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Tingrettens åpning av offentlig skifte av eget tiltak', 'kategori': 'arv', 'description': 'Kan tingretten åpne offentlig skifte uten at noen krever det? Ja — hvis ingen valgte privat skifte innen 60 dager.', 'kort_svar': 'Er 60-dagersfristen ute uten at noen har valgt privat skifte, åpner tingretten offentlig skifte av eget tiltak. For svært små boer kan staten hjelpe til inntil 50 ganger rettsgebyret.', 'paragraftekst': 'Er 60-dagersfristen ute uten at noen har valgt privat skifte, åpner tingretten offentlig skifte av eget tiltak. For svært små boer kan staten hjelpe til inntil 50 ganger rettsgebyret.', 'hva_betyr_html': '<p>Er 60 dager ute og ingen har valgt skifteform, griper tingretten inn automatisk — du mister muligheten til å velge privat skifte. For svært små boer kan staten dekke kostnadene slik at selv fattige boer behandles ordentlig.</p>', 'eksempler': [], 'vanlige_feil': ['Tro at et bo kan ligge og vente uten konsekvenser — tingretten griper inn etter 60 dager'], 'hva_bor_du_html': '<p>Er du arving og usikker: ta en beslutning innen 60 dager. Kontakt tingretten for veiledning.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '117', 'tittel': 'Fristen for privat skifte', 'available': True}, {'lov': 'arveloven', 'paragraf': '130', 'tittel': 'Bortfall av retten til offentlig skifte', 'available': True}]},

    {'number': '130', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Bortfall av retten til å kreve offentlig skifte', 'kategori': 'arv', 'description': 'Når er det for sent å kreve offentlig skifte? Normalt tre år etter dødsfallet — og aldri etter at privat skifte er avsluttet.', 'kort_svar': 'Retten til å kreve offentlig skifte faller bort tre år etter dødsfallet. Er privat skifte allerede avsluttet, er det normalt for sent.', 'paragraftekst': 'Retten til å kreve offentlig skifte faller bort tre år etter dødsfallet. Er privat skifte allerede avsluttet, er det normalt for sent.', 'hva_betyr_html': '<p>To stopptidspunkter: (1) <strong>Avsluttet privat skifte</strong> — er skiftet ferdig, er spillet over. Unntak for mindreårige/umyndige. (2) <strong>Tre-årsfristen</strong> — selv om privat skifte ikke er avsluttet, mister du retten etter tre år. For uskiftebo løper fristen fra uskiftet avsluttes.</p>', 'eksempler': [{'navn': 'Anne', 'tekst': 'Privat skifte er påbegynt men ikke formelt avsluttet. To år og åtte måneder etter dødsfallet krever Anne offentlig skifte. Hun er innenfor tre-årsfristen. Tingretten åpner offentlig skifte.'}], 'vanlige_feil': ['Vente i årevis med å handle og oppdage at fristen er ute', 'Tro at tre-årsfristen løper fra du hørte om dødsfallet — den løper fra dødsdatoen'], 'hva_bor_du_html': '<p>Er du misfornøyd med et pågående privat skifte: ikke vent. Tre år er kortere enn det virker.</p>', 'dumme_sporsmal': [{'q': 'Hva betyr «avsluttet» privat skifte?', 'a': 'Normalt når arvingene har signert fordelingsavtalen og eiendeler er overført.'}], 'related': [{'lov': 'arveloven', 'paragraf': '127', 'tittel': 'Hvem kan kreve offentlig skifte', 'available': True}, {'lov': 'arveloven', 'paragraf': '71', 'tittel': 'Foreldelse av arverett', 'available': True}]},

    {'number': '131', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Forberedende rettsmøte', 'kategori': 'arv', 'description': 'Hva skjer før offentlig skifte åpnes? Tingretten innkaller til et forberedende rettsmøte der partene møtes, får veiledning — og kanskje inngår forlik.', 'kort_svar': 'Før offentlig skifte åpnes, holder tingretten et forberedende rettsmøte med arvingene. Dommeren gir veiledning, prøver å avklare tvister og kan mekle. Partene kan inngå rettsforlik. Møtet er ikke offentlig.', 'paragraftekst': 'Før offentlig skifte åpnes, holder tingretten et forberedende rettsmøte med arvingene. Dommeren gir veiledning, prøver å avklare tvister og kan mekle. Partene kan inngå rettsforlik. Møtet er ikke offentlig.', 'hva_betyr_html': '<p>Det forberedende rettsmøtet er en mulighet til å rydde opp FØR det tunge maskineriet i offentlig skifte settes i gang. Kan partene inngå rettsforlik der og da — raskere og billigere enn fullt offentlig skifte. Den som krever offentlig skifte betaler gebyret; åpnes offentlig skifte, dekkes alt av boet.</p>', 'eksempler': [{'navn': 'Per og Jonas', 'tekst': 'Per krever offentlig skifte fordi han og Jonas strides om hytteverdien. I det forberedende rettsmøtet inngår de rettsforlik: Jonas overtar hytta til fastsatt verdi. Offentlig skifte åpnes ikke.'}], 'vanlige_feil': ['Ikke møte opp til det forberedende rettsmøtet — det er en viktig mulighet til å avklare ting tidlig'], 'hva_bor_du_html': '<p>Innkalles du: møt opp forberedt. Er du åpen for forlik — si det. Mange arveoppgjør avsluttes nettopp i slike møter.</p>', 'dumme_sporsmal': [{'q': 'Er det bindende hva som sies i møtet?', 'a': 'Bare hvis det inngås et rettsforlik. Alt annet er informasjonsutveksling.'}], 'related': [{'lov': 'arveloven', 'paragraf': '132', 'tittel': 'Sikkerhet for skifteomkostningene', 'available': True}, {'lov': 'arveloven', 'paragraf': '133', 'tittel': 'Åpning av offentlig skifte', 'available': True}]},

    {'number': '132', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Sikkerhet for skifteomkostningene', 'kategori': 'arv', 'description': 'Må den som krever offentlig skifte, stille sikkerhet for kostnadene? Ja — med mindre boet åpenbart kan dekke dem selv. Staten er unntatt.', 'kort_svar': 'Den som krever offentlig skifte, må stille sikkerhet for skifteomkostningene. Er det klart at boet kan dekke kostnadene selv, slipper du. Staten trenger aldri stille sikkerhet.', 'paragraftekst': 'Den som krever offentlig skifte, må stille sikkerhet for skifteomkostningene. Er det klart at boet kan dekke kostnadene selv, slipper du. Staten trenger aldri stille sikkerhet.', 'hva_betyr_html': '<p>Offentlig skifte koster penger. For å sikre at staten ikke ender med regningen, kreves garanti fra den som ber om det. Er boet åpenbart solid nok — typisk boer med fast eiendom — faller kravet om sikkerhet bort.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Vurderer du å kreve offentlig skifte: spør tingretten om du må stille sikkerhet. Er boet verdifullt, er det sjelden du trenger å legge ut noe.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '127', 'tittel': 'Hvem kan kreve offentlig skifte', 'available': True}, {'lov': 'arveloven', 'paragraf': '133', 'tittel': 'Åpning av offentlig skifte', 'available': True}]},

    {'number': '133', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Åpning av offentlig skifte', 'kategori': 'arv', 'description': 'Når åpner tingretten offentlig skifte, og hva skjer hvis det er tvil om vilkårene? Retten åpner skifte ved kjennelse og kan treffe midlertidige sikringstiltak.', 'kort_svar': 'Tingretten åpner offentlig skifte ved kjennelse. Er det tvil om hvem som er rettmessige arvinger, kan retten åpne midlertidig skifte og treffe sikringstiltak for å hindre at eiendeler forsvinner.', 'paragraftekst': 'Tingretten åpner offentlig skifte ved kjennelse. Er det tvil om hvem som er rettmessige arvinger, kan retten åpne midlertidig skifte og treffe sikringstiltak for å hindre at eiendeler forsvinner.', 'hva_betyr_html': '<p>Å åpne offentlig skifte er en formell rettskjennelse. Er det uklart hvem som er arvinger, kan retten åpne midlertidig og gjennomføre skiftet inntil spørsmålet løses. Tingretten kan treffe midlertidige forføyninger: fryse konti, sikre eiendom, forhindre fjerning av eiendeler.</p>', 'eksempler': [{'navn': 'Sofie', 'tekst': 'Sofie bestrider testamentets gyldighet og krever offentlig skifte. Brødrene vil ha privat skifte. Tingretten åpner offentlig skifte midlertidig. Tvisten om testamentets gyldighet prøves under skiftet mens boet holdes samlet.'}], 'vanlige_feil': ['Unnlate å be om sikringstiltak mens tvisten pågår'], 'hva_bor_du_html': '<p>Er du redd for at eiendeler forsvinner mens tvist pågår: be tingretten om midlertidige forføyninger.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '131', 'tittel': 'Forberedende rettsmøte', 'available': True}, {'lov': 'arveloven', 'paragraf': '134', 'tittel': 'Skiftebehandling ved bostyrer', 'available': True}]},

    {'number': '134', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Skiftebehandling ved tingretten eller ved bostyrer', 'kategori': 'arv', 'description': 'Hvem gjennomfører det offentlige skiftet? Normalt en bostyrer oppnevnt av tingretten — vanligvis en advokat.', 'kort_svar': 'Ved offentlig skifte oppnevner tingretten normalt en bostyrer — vanligvis en advokat — til å gjennomføre skiftet. Retten kan også selv styre prosessen, og kan i tillegg oppnevne revisor.', 'paragraftekst': 'Ved offentlig skifte oppnevner tingretten normalt en bostyrer — vanligvis en advokat — til å gjennomføre skiftet. Retten kan også selv styre prosessen, og kan i tillegg oppnevne revisor.', 'hva_betyr_html': '<p>I de fleste offentlige skifte oppnevner tingretten en bostyrer — oftest en advokat. Bostyreren tar over: kartlegger eiendeler og gjeld, avvikler eiendeler, betaler kreditorer og fordeler resten. Bostyrerens honorar dekkes av boet som massekrav.</p>', 'eksempler': [{'navn': 'Ola', 'tekst': 'Ola dør med to leiligheter, et aksjeselskap og gjeld til fire kreditorer. Tingretten oppnevner advokat Mette som bostyrer. Mette avvikler aksjeselskapet og selger leilighetene. Honoraret betales av boet.'}], 'vanlige_feil': ['Tro at du som arving kan bestemme hvem som blir bostyrer — det er rettens oppgave'], 'hva_bor_du_html': '<p>Er det åpnet offentlig skifte: ta kontakt med bostyreren og meld dine interesser.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '135', 'tittel': 'Formålet med det offentlige skiftet', 'available': True}, {'lov': 'arveloven', 'paragraf': '148', 'tittel': 'Bostyrerreglene', 'available': True}]},

    {'number': '135', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Formålet med det offentlige skiftet', 'kategori': 'arv', 'description': 'Hva er egentlig målet med et offentlig skifte? Å kartlegge boets eiendeler og hvem som er arvinger — og avslutte med et booppgjør som viser fordelingen.', 'kort_svar': 'Formålet med offentlig skifte er å kartlegge boets eiendeler og forpliktelser, avklare hvem arvingene er, og fordele verdiene gjennom et formelt booppgjør. Boets eiendeler skal forvaltes forsvarlig gjennom hele prosessen.', 'paragraftekst': 'Formålet med offentlig skifte er å kartlegge boets eiendeler og forpliktelser, avklare hvem arvingene er, og fordele verdiene gjennom et formelt booppgjør. Boets eiendeler skal forvaltes forsvarlig gjennom hele prosessen.', 'hva_betyr_html': '<p>Tre hovedelementer: (1) Kartlegging — full oversikt over eiendeler, gjeld og arvingenes identitet. (2) Forsvarlig forvaltning — boets eiendeler sikres og vedlikeholdes mens skiftet pågår. (3) Booppgjøret — det endelige dokumentet som viser hva som fantes, hva som er betalt og hva som fordeles.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er du arving under offentlig skifte: vær aktiv og hold deg i dialog med bostyreren.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '134', 'tittel': 'Bostyrer', 'available': True}, {'lov': 'arveloven', 'paragraf': '160', 'tittel': 'Booppgjøret', 'available': True}]},

    {'number': '136', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Skiftemyndighetens kompetanse og saksbehandlingsregler', 'kategori': 'arv', 'description': 'Hvilke regler styrer saksbehandlingen under offentlig skifte? Tvistelovens regler gjelder så langt de passer — og tvister avgjøres etter egne regler i §§ 168–174.', 'kort_svar': 'Tingretten behandler alle spørsmål under offentlig skifte etter arvelovens egne saksbehandlingsregler, supplert av tvisteloven der det passer. Tvister avgjøres etter §§ 168–174.', 'paragraftekst': 'Tingretten behandler alle spørsmål under offentlig skifte etter arvelovens egne saksbehandlingsregler, supplert av tvisteloven der det passer. Tvister avgjøres etter §§ 168–174.', 'hva_betyr_html': '<p>Arveloven har egne prosedyreregler for offentlig skifte, supplert av tvisteloven der det er hull. Tvister løses etter egne regler i §§ 168–174, tilpasset skiftets egenart.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er det en tvist under offentlig skifte: kontakt tingretten eller bostyreren og avklar hvilke regler som gjelder.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '134', 'tittel': 'Bostyrer og gjennomføring', 'available': True}]},

    {'number': '137', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Arvingenes rett til å uttale seg', 'kategori': 'arv', 'description': 'Har arvingene rett til å si sin mening under offentlig skifte? Ja — de skal som utgangspunkt gis anledning til å uttale seg før viktige avgjørelser treffes.', 'kort_svar': 'Under offentlig skifte skal arvingene så langt mulig gis anledning til å uttale seg før det treffes avgjørelser av betydning for forvaltningen av boet.', 'paragraftekst': 'Under offentlig skifte skal arvingene så langt mulig gis anledning til å uttale seg før det treffes avgjørelser av betydning for forvaltningen av boet.', 'hva_betyr_html': '<p>Selv om tingretten og bostyreren styrer offentlig skifte, er arvingene ikke passive tilskuere. De har rett til å bli hørt før viktige beslutninger tas om salg av eiendeler, godkjenning av kreditorkrav og verdivurderinger. «Så vidt mulig» betyr at der det haster kan beslutningen tas uten uttalelse.</p>', 'eksempler': [], 'vanlige_feil': ['Sitte stille og tro at bostyreren tar alt — vær aktiv og meld interesse for å bli hørt'], 'hva_bor_du_html': '<p>Er du arving: meld interesse for å bli hørt og hold kontakt med bostyreren. Er du ikke varslet om en beslutning du burde uttalt deg om: ta det opp med tingretten.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '134', 'tittel': 'Bostyrer', 'available': True}, {'lov': 'arveloven', 'paragraf': '138', 'tittel': 'Beslutninger under skiftet', 'available': True}, {'lov': 'arveloven', 'paragraf': '140', 'tittel': 'Skiftesamlingen', 'available': True}]},

    {'number': '138', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Beslutninger under offentlig skifte — krav om enighet', 'kategori': 'arv', 'description': 'Er tingretten og bostyreren bundet av arvingenes ønsker under offentlig skifte? Ja, hvis arvingene er enige — men ikke hvis boet er insolvent eller enigheten skader andre.', 'kort_svar': 'Er arvingene enige om et standpunkt, er tingretten og bostyreren som hovedregel bundet av det. Unntak: boet er insolvent, eller enigheten vil skade fraværende arvinger eller kreditorer.', 'paragraftekst': 'Er arvingene enige om et standpunkt, er tingretten og bostyreren som hovedregel bundet av det. Unntak: boet er insolvent, eller enigheten vil skade fraværende arvinger eller kreditorer.', 'hva_betyr_html': '<p>Offentlig skifte er ikke en situasjon der retten og bostyreren gjør hva de vil — det er fortsatt arvingenes bo. Er arvingene enige, er retten og bostyreren forpliktet til å følge det. Unntak der boet er insolvent (kreditorenes interesser er overordnede) eller der enigheten skader noen som ikke er til stede.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er arvingene enige: gjør det klart overfor bostyreren. Er bostyreren uenig: ta det opp med tingretten.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '137', 'tittel': 'Arvingenes rett til å uttale seg', 'available': True}, {'lov': 'arveloven', 'paragraf': '120', 'tittel': 'Enighet ved privat skifte', 'available': True}]},

    {'number': '139', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Stedfortreder for person under vergemål og upersonlige rettssubjekter', 'kategori': 'arv', 'description': 'Hvem representerer en mindreårig arving under offentlig skifte? Vergen — og mindreårige over 15 år har rett til å delta og bli informert.', 'kort_svar': 'Mindreårige arvinger representeres av vergen under offentlig skifte. Arvinger over 15 år har rett til å møte og bli informert om avgjørelser.', 'paragraftekst': 'Mindreårige arvinger representeres av vergen under offentlig skifte. Arvinger over 15 år har rett til å møte og bli informert om avgjørelser.', 'hva_betyr_html': '<p>Under offentlig skifte er det vergen — normalt foreldrene — som ivaretar en mindreårig arvingens interesser. Er barnet over 15 år, innkalles det til møter og informeres om beslutninger. De har rett til å møte, men ingen plikt.</p>', 'eksempler': [], 'vanlige_feil': ['Glemme å informere mindreårige arvinger over 15 år om møter og beslutninger'], 'hva_bor_du_html': '<p>Er du verge for en mindreårig arving: ta rollen på alvor. Er barnet over 15: inkluder det i prosessen.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '138', 'tittel': 'Beslutninger under skiftet', 'available': True}]},

    {'number': '140', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Skiftesamlingen', 'kategori': 'arv', 'description': 'Hva er en skiftesamling, og hvordan innkalles du til den? Det er et lukket rettsmøte der tingretten samler arvingene for å drøfte og avklare spørsmål under offentlig skifte.', 'kort_svar': 'Tingretten kan innkalle arvingene til skiftesamling med minst 14 dagers varsel. Det er et lukket rettsmøte — ikke offentlig.', 'paragraftekst': 'Tingretten kan innkalle arvingene til skiftesamling med minst 14 dagers varsel. Det er et lukket rettsmøte — ikke offentlig.', 'hva_betyr_html': '<p>Skiftesamlingen er tingrettens verktøy for å samle arvingene og avklare spørsmål. Møtet holdes på tingretten og er ikke offentlig. Innkallingen skal skje med minst 14 dagers varsel.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Mottar du innkalling: møt opp. Det er en viktig anledning til å fremme dine interesser.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '137', 'tittel': 'Arvingenes rett til å uttale seg', 'available': True}, {'lov': 'arveloven', 'paragraf': '154', 'tittel': 'Rett til å kreve skiftesamling', 'available': True}]},

    {'number': '141', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Registrering av boets eiendeler og forpliktelser', 'kategori': 'arv', 'description': 'Hva skjer med kartleggingen av boet under offentlig skifte? Eiendeler og gjeld skal registreres formelt.', 'kort_svar': 'Under offentlig skifte skal boets eiendeler og forpliktelser registreres formelt. Skiftes det mellom gjenlevende ektefelle og øvrige arvinger der én har tatt gjeldansvaret, kan registrering og proklama sløyfes ved enighet.', 'paragraftekst': 'Under offentlig skifte skal boets eiendeler og forpliktelser registreres formelt. Skiftes det mellom gjenlevende ektefelle og øvrige arvinger der én har tatt gjeldansvaret, kan registrering og proklama sløyfes ved enighet.', 'hva_betyr_html': '<p>Registrering er det formelle første steget — en systematisk dokumentasjon av alt boet inneholder. Unntaket for ektefelleskifte: skiftes det mellom gjenlevende ektefelle og barna, og én arving allerede har tatt gjeldansvaret, kan de sende en oversikt alle er enige i — uten formell registrering og proklama.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er du arving og ønsker å bidra: ta kontakt med bostyreren tidlig og gi en oversikt over eiendeler du kjenner til.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '91', 'tittel': 'Registrering og sikring av boets eiendeler', 'available': True}, {'lov': 'arveloven', 'paragraf': '142', 'tittel': 'Proklama ved offentlig skifte', 'available': True}]},

    {'number': '142', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Kunngjøring av frist for å melde krav (proklama) ved offentlig skifte', 'kategori': 'arv', 'description': 'Kunngjøres det alltid proklama ved offentlig skifte? Ja — det er obligatorisk, og utstedes av retten eller bostyreren.', 'kort_svar': 'Under offentlig skifte skal det alltid kunngjøres proklama — en 6-ukers frist for kreditorer til å melde krav. Det er obligatorisk, i motsetning til ved privat skifte der det er frivillig.', 'paragraftekst': 'Under offentlig skifte skal det alltid kunngjøres proklama — en 6-ukers frist for kreditorer til å melde krav. Det er obligatorisk, i motsetning til ved privat skifte der det er frivillig.', 'hva_betyr_html': '<p>Under offentlig skifte er proklama ikke et valg — det er en plikt. Det skjer automatisk. Alle kreditorer tvinges til å melde seg innen seks uker; krav som ikke meldes, faller bort. Er proklama allerede kunngjort, trenger det ikke gjentas.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Under offentlig skifte: sørg for at proklamaet kunngjøres tidlig i prosessen.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '100', 'tittel': 'Utstedelse av proklama', 'available': True}, {'lov': 'arveloven', 'paragraf': '102', 'tittel': 'Virkning av proklamaet', 'available': True}]},

    {'number': '143', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Dekning av boets og arvelaterens forpliktelser ved offentlig skifte', 'kategori': 'arv', 'description': 'Hvordan dekkes gjelden under offentlig skifte? Retten eller bostyreren sørger for betaling etter prioriteringsrekkefølge — og foreløpige utbetalinger kan bare skje etter proklamafristen.', 'kort_svar': 'Under offentlig skifte er det retten eller bostyreren som sørger for at gjelden betales i riktig rekkefølge. Foreløpig utbetaling til arvingene kan bare skje etter at proklamafristen er løpt ut.', 'paragraftekst': 'Under offentlig skifte er det retten eller bostyreren som sørger for at gjelden betales i riktig rekkefølge. Foreløpig utbetaling til arvingene kan bare skje etter at proklamafristen er løpt ut.', 'hva_betyr_html': '<p>Betalingsprosessen er kontrollert. Bostyreren betaler gjeld løpende der boet er solvent. Er solvensen usikker, låses pengene til booppgjøret er ferdig. Selve utdelingen til arvingene kan bare skje etter proklamafristen — seks uker etter siste kunngjøring.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er du arving og lurer på når du kan forvente utbetaling: normalt ikke før proklamafristen er ute og booppgjøret er fastsatt.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '122', 'tittel': 'Dekning av forpliktelser ved privat skifte', 'available': True}, {'lov': 'arveloven', 'paragraf': '142', 'tittel': 'Proklama ved offentlig skifte', 'available': True}]},

    {'number': '144', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Forsinkelsesrente og mellomrente', 'kategori': 'arv', 'description': 'Hva skjer med renter på krav under et skifte? Betales et krav for sent, løper forsinkelsesrente. Betales det for tidlig, trekkes en mellomrente fra.', 'kort_svar': 'Betales et krav etter forfallsdatoen, løper forsinkelsesrente. Betales et krav før forfall, trekkes en mellomrente fra — lik forsinkelsesrenten minus seks prosentpoeng. Mellomrenten brukes som standardrente flere steder i arveloven.', 'paragraftekst': 'Betales et krav etter forfallsdatoen, løper forsinkelsesrente. Betales et krav før forfall, trekkes en mellomrente fra — lik forsinkelsesrenten minus seks prosentpoeng. Mellomrenten brukes som standardrente flere steder i arveloven.', 'hva_betyr_html': '<p>For sen betaling: forsinkelsesrente til kreditor. For tidlig betaling: mellomrenten trekkes fra. Mellomrenten brukes som standardrente ved pantobligasjoner (§ 107) og andre steder i loven.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er du bostyrer: betal krav innen forfallsdato. Vil du betale tidlig: beregn mellomrenten og trekk fra.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '107', 'tittel': 'Oppgjør ved overtakelse av eiendeler', 'available': True}]},

    {'number': '145', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Oppfyllelse av bestemmelser i testament ved offentlig skifte', 'kategori': 'arv', 'description': 'Sørger retten eller bostyreren for at testamentariske krav oppfylles under offentlig skifte? Ja — det er en plikt.', 'kort_svar': 'Under offentlig skifte er det retten eller bostyreren som sørger for at testamentets bestemmelser oppfylles — etter at kreditorene er dekket og før resten fordeles til lovarvingene.', 'paragraftekst': 'Under offentlig skifte er det retten eller bostyreren som sørger for at testamentets bestemmelser oppfylles — etter at kreditorene er dekket og før resten fordeles til lovarvingene.', 'hva_betyr_html': '<p>Under offentlig skifte overtar det profesjonelle apparatet ansvaret for testamentsoppfyllelse. En fordel for testamentsarvinger: bostyreren har plikt til å oppfylle testamentets krav — de risikerer ikke å bli oversett.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er du testamentsarving under offentlig skifte: meld dine rettigheter til bostyreren tidlig.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '124', 'tittel': 'Oppfyllelse av testament ved privat skifte', 'available': True}, {'lov': 'arveloven', 'paragraf': '134', 'tittel': 'Bostyrer', 'available': True}]},

    {'number': '146', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Arving som er forsvunnet eller uten kjent oppholdssted ved offentlig skifte', 'kategori': 'arv', 'description': 'Hva skjer med andelen til en forsvunnet arving under offentlig skifte? Den settes av i booppgjøret og forvaltes etter lov om forsvunne personar.', 'kort_svar': 'Er en arving forsvunnet ved offentlig skifte, settes andelen av i booppgjøret. Er andelen under to ganger grunnbeløpet og arvingen har ektefelle eller livsarvinger som kan arve i stedet, trenger det ikke settes av.', 'paragraftekst': 'Er en arving forsvunnet ved offentlig skifte, settes andelen av i booppgjøret. Er andelen under to ganger grunnbeløpet og arvingen har ektefelle eller livsarvinger som kan arve i stedet, trenger det ikke settes av.', 'hva_betyr_html': '<p>Kan en arving ikke finnes, stopper ikke skiftet. Booppgjøret inneholder en post for den fraværende arvingens andel. For lave beløp (under 2G) med nær familie som kan arve videre, trenger det ikke settes av.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er du arving og vet om en annen arving som er forsvunnet: meld det til bostyreren. Andelen skal settes av formelt.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '68', 'tittel': 'Fraværende arving', 'available': True}, {'lov': 'arveloven', 'paragraf': '125', 'tittel': 'Fraværende arving ved privat skifte', 'available': True}]},

    {'number': '147', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Tvangsfullbyrdelse i boets eiendeler', 'kategori': 'arv', 'description': 'Kan kreditorer med dom mot den avdøde tvangsinndrive mot boets eiendeler? Ja — men de første seks månedene kreves samtykke fra tingretten.', 'kort_svar': 'En kreditor med tvangskraftig dom mot den avdøde kan tvangsinndrive mot boets eiendeler. De første seks månedene etter dødsfallet kreves det likevel samtykke fra tingretten.', 'paragraftekst': 'En kreditor med tvangskraftig dom mot den avdøde kan tvangsinndrive mot boets eiendeler. De første seks månedene etter dødsfallet kreves det likevel samtykke fra tingretten.', 'hva_betyr_html': '<p>En dom mot den avdøde overlever dødsfallet og kan rettes mot boet. Men de første seks månedene kreves tingretts samtykke — det gir boet tid til å skaffe seg oversikt og velge skifteform, uten at aggressive kreditorer tapper boet.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Mottar du varsler om tvangsinndrivelse mot boet i de første seks månedene: ta kontakt med tingretten umiddelbart. Retten må samtykke.</p>', 'dumme_sporsmal': [{'q': 'Kan en kreditor ta utlegg i min private formue fordi jeg er arving?', 'a': 'Bare hvis du har påtatt deg ansvaret for arvelaterens forpliktelser etter § 116.'}], 'related': [{'lov': 'arveloven', 'paragraf': '116', 'tittel': 'Personlig ansvar for forpliktelsene', 'available': True}, {'lov': 'arveloven', 'paragraf': '122', 'tittel': 'Dekning av forpliktelser', 'available': True}]},

    {'number': '148', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Virkeområde for bostyrerreglene', 'kategori': 'arv', 'description': 'Hvilke paragrafer gjelder spesifikt for bostyrer? §§ 148–157 regulerer situasjoner der tingretten har oppnevnt en bostyrer.', 'kort_svar': '§§ 148–157 gjelder spesifikt for tilfeller der tingretten har oppnevnt en bostyrer til å gjennomføre offentlig skifte.', 'paragraftekst': '§§ 148–157 gjelder spesifikt for tilfeller der tingretten har oppnevnt en bostyrer til å gjennomføre offentlig skifte.', 'hva_betyr_html': '<p>En ren avgrensningsbestemmelse: reglene gjelder bare når det faktisk er en bostyrer til stede. Gjennomfører tingretten skiftet selv uten bostyrer, gjelder de generelle reglene.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er det oppnevnt bostyrer i ditt bo: les §§ 149–157 for å forstå bostyrerens plikter og begrensninger.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '134', 'tittel': 'Skiftebehandling ved bostyrer', 'available': True}, {'lov': 'arveloven', 'paragraf': '149', 'tittel': 'Hvem kan være bostyrer', 'available': True}]},

    {'number': '149', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Hvem som kan oppnevnes som bostyrer', 'kategori': 'arv', 'description': 'Hvem kan bli bostyrer i et offentlig skifte? Normalt en advokat — men andre kan oppnevnes der tingretten finner det forsvarlig. Bostyreren må ha ansvarsforsikring.', 'kort_svar': 'Som bostyrer oppnevnes normalt en advokat. Andre fagpersoner kan oppnevnes hvis tingretten finner det ubetenkelig. Bostyreren må ha ansvarsforsikring som dekker mulig ansvar for feil under bobehandlingen.', 'paragraftekst': 'Som bostyrer oppnevnes normalt en advokat. Andre fagpersoner kan oppnevnes hvis tingretten finner det ubetenkelig. Bostyreren må ha ansvarsforsikring som dekker mulig ansvar for feil under bobehandlingen.', 'hva_betyr_html': '<p>En bostyrer er en profesjonell som tar over styringen av offentlig skifte. Normalt en advokat; i enkle boer kan tingretten oppnevne andre. Ansvarsforsikring er obligatorisk — bostyreren hefter personlig for feil. Premien dekkes av boet som skiftekostnad.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er du arving og lurer på hvem bostyreren er: spør tingretten.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '150', 'tittel': 'Bostyrerens oppgave og kompetanse', 'available': True}, {'lov': 'arveloven', 'paragraf': '156', 'tittel': 'Klage over bostyreren', 'available': True}]},

    {'number': '150', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Bostyrerens oppgave og kompetanse', 'kategori': 'arv', 'description': 'Hva kan bostyreren gjøre, og hva kan vedkommende ikke gjøre? Bostyreren har tingrettens kompetanse i praktiske saker, men kan ikke avgjøre rettstvister.', 'kort_svar': 'Bostyreren gjennomfører skiftet på tingrettens vegne og har den samme kompetansen som tingretten i praktiske saker. Men bostyreren kan ikke avgjøre rettstvister eller innkalle til skiftesamlinger.', 'paragraftekst': 'Bostyreren gjennomfører skiftet på tingrettens vegne og har den samme kompetansen som tingretten i praktiske saker. Men bostyreren kan ikke avgjøre rettstvister eller innkalle til skiftesamlinger.', 'hva_betyr_html': '<p>Bostyreren er tingrettens forlengede arm i praktiske saker. Men bostyreren er ikke en dommer. Oppstår rettstvister, må de løses av tingretten. Vil bostyreren ha skiftesamling, må vedkommende be retten om det etter § 154.</p>', 'eksempler': [], 'vanlige_feil': ['Tro at bostyreren kan avgjøre alle tvister — det kan bare retten'], 'hva_bor_du_html': '<p>Er du arving: ta kontakt med bostyreren tidlig. Er du misfornøyd: bruk klageadgangen i § 156.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '149', 'tittel': 'Hvem kan være bostyrer', 'available': True}, {'lov': 'arveloven', 'paragraf': '154', 'tittel': 'Rett til å kreve skiftesamling', 'available': True}, {'lov': 'arveloven', 'paragraf': '156', 'tittel': 'Klage over bostyreren', 'available': True}]},

    {'number': '151', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Protokoll og regnskap', 'kategori': 'arv', 'description': 'Må bostyreren dokumentere hva som skjer under bobehandlingen? Ja — bostyreren plikter å føre protokoll og regnskap, og boets midler skal holdes atskilt fra egne.', 'kort_svar': 'Bostyreren må føre protokoll over alle forhandlinger og beslutninger, og regnskap over boets midler. Boets midler skal holdes på egne konti — aldri blandet med bostyrerens private midler.', 'paragraftekst': 'Bostyreren må føre protokoll over alle forhandlinger og beslutninger, og regnskap over boets midler. Boets midler skal holdes på egne konti — aldri blandet med bostyrerens private midler.', 'hva_betyr_html': '<p>Dokumentasjonskravet er en grunnleggende beskyttelse for arvingene. Protokollen viser beslutningene. Regnskapet viser pengestrømmene. Boets penger skal alltid stå på egne konti — aldri blandes med bostyrerens egne. Brudd på dette er alvorlig.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Som arving kan du be bostyreren om innsyn i protokollen og regnskapet.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '150', 'tittel': 'Bostyrerens oppgave', 'available': True}, {'lov': 'arveloven', 'paragraf': '156', 'tittel': 'Klage over bostyreren', 'available': True}]},

    {'number': '152', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Innberetninger til tingretten', 'kategori': 'arv', 'description': 'Hvor ofte rapporterer bostyreren til tingretten? Innen tre måneder etter oppnevning — og deretter med fremdriftsrapporter og årlige innberetninger.', 'kort_svar': 'Bostyreren sender innberetning senest tre måneder etter oppnevning med oversikt over boets eiendeler, gjeld og plan for videre behandling. Er boet ikke avsluttet etter ett år, sendes full innberetning med regnskap — deretter minst én gang i året.', 'paragraftekst': 'Bostyreren sender innberetning senest tre måneder etter oppnevning med oversikt over boets eiendeler, gjeld og plan for videre behandling. Er boet ikke avsluttet etter ett år, sendes full innberetning med regnskap — deretter minst én gang i året.', 'hva_betyr_html': '<p>Rapporteringsstrukturen: 3 måneder: full innberetning. 6 og 9 måneder: korte fremdriftsrapporter. 1 år og deretter: full innberetning med regnskap, minst én gang i året. Er du arving og synes skiftet trekker ut: sjekk om bostyreren leverer disse. Gjør vedkommende ikke det, er det grunnlag for klage etter § 156.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Be bostyreren om kopi av innberetningene. Det er din rett å følge med på fremdriften.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '150', 'tittel': 'Bostyrerens oppgave', 'available': True}, {'lov': 'arveloven', 'paragraf': '156', 'tittel': 'Klage over bostyreren', 'available': True}]},

    {'number': '153', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Bomøter', 'kategori': 'arv', 'description': 'Hva er et bomøte, og har du rett til å delta? Bostyreren innkaller arvingene til et innledende bomøte for å presentere boets situasjon og høre arvingenes ønsker.', 'kort_svar': 'Bostyreren innkaller normalt arvingene til et innledende bomøte der boets eiendeler og gjeld presenteres, og arvingenes ønsker om fordeling og salg kartlegges.', 'paragraftekst': 'Bostyreren innkaller normalt arvingene til et innledende bomøte der boets eiendeler og gjeld presenteres, og arvingenes ønsker om fordeling og salg kartlegges.', 'hva_betyr_html': '<p>Bomøtet er bostyrerens viktigste verktøy for å samle alle arvingene. Her presenteres tallene og hvilke ønsker arvingene har — særlig om de vil overta eiendeler fremfor at de selges. Bomøter er uformelle (bostyrerens verktøy), i motsetning til skiftesamlinger (§ 140, rettens verktøy).</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Innkalles du til bomøte: møt opp forberedt med en liste over eiendeler du eventuelt ønsker å overta.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '140', 'tittel': 'Skiftesamlingen', 'available': True}, {'lov': 'arveloven', 'paragraf': '154', 'tittel': 'Rett til å kreve skiftesamling', 'available': True}]},

    {'number': '154', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Rett til å kreve skiftesamling', 'kategori': 'arv', 'description': 'Kan arvingene kreve at tingretten holder et formelt møte om boet? Ja — bostyreren eller et flertall av arvingene kan kreve skiftesamling etter § 140.', 'kort_svar': 'Bostyreren eller et flertall av arvingene kan kreve at tingretten holder skiftesamling — et formelt rettsmøte, i motsetning til bostyrerens uformelle bomøter.', 'paragraftekst': 'Bostyreren eller et flertall av arvingene kan kreve at tingretten holder skiftesamling — et formelt rettsmøte, i motsetning til bostyrerens uformelle bomøter.', 'hva_betyr_html': '<p>Bomøter (§ 153) er bostyrerens verktøy. Skiftesamlinger (§ 140) er rettens verktøy — et formelt rettsmøte der dommeren styrer og avgjørelser kan ha rettskraft. Typisk brukes dette når det er tvister bostyreren ikke kan løse, eller arvingene er misfornøyde med bostyrerens håndtering.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er det saker som trenger rettens avgjørelse: krev skiftesamling. Sørg for at et flertall av arvingene er med på kravet.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '140', 'tittel': 'Skiftesamlingen', 'available': True}, {'lov': 'arveloven', 'paragraf': '153', 'tittel': 'Bomøter', 'available': True}]},

    {'number': '155', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Utkast til booppgjør', 'kategori': 'arv', 'description': 'Når er bostyreren ferdig? Når vedkommende utarbeider et utkast til booppgjør — med forslag til fordeling og til eget honorar.', 'kort_svar': 'Når boet er klart for avslutning, utarbeider bostyreren et utkast til booppgjør. Forslag til bostyrerens godtgjørelse tas inn i utkastet.', 'paragraftekst': 'Når boet er klart for avslutning, utarbeider bostyreren et utkast til booppgjør. Forslag til bostyrerens godtgjørelse tas inn i utkastet.', 'hva_betyr_html': '<p>Booppgjøret er siste steg. Utkastet sendes til arvingene og gjenværende kreditorer, som gis minst to uker til å påpeke feil. Deretter oversendes det til tingretten som fastsetter ved kjennelse. Bostyrerens eget honorar er en del av utkastet.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Mottar du utkast: les det nøye og meld feil innen fristen. Dette er siste sjanse til å korrigere.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '160', 'tittel': 'Fastsettelse av booppgjøret', 'available': True}]},

    {'number': '156', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Klage over bostyreren', 'kategori': 'arv', 'description': 'Kan du klage hvis bostyreren ikke gjør jobben sin? Ja — enhver arving kan klage til tingretten. Beslutningen kan ikke ankes.', 'kort_svar': 'Er du arving og mener bostyreren mangler fremdrift eller tilliten er svekket, kan du klage til tingretten. Retten behandler klagen og kan be bostyreren om en redegjørelse. Beslutningen kan ikke ankes.', 'paragraftekst': 'Er du arving og mener bostyreren mangler fremdrift eller tilliten er svekket, kan du klage til tingretten. Retten behandler klagen og kan be bostyreren om en redegjørelse. Beslutningen kan ikke ankes.', 'hva_betyr_html': '<p>To klagegrunn: manglende fremdrift og svekkelse av tillit. Retten gir bostyreren mulighet til å forklare seg — deretter tar retten en endelig beslutning som ikke kan ankes videre.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Har du grunn til å klage: dokumenter konkret hva som har gått galt. Send skriftlig klage til tingretten. Vær saklig og konkret.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '150', 'tittel': 'Bostyrerens oppgave', 'available': True}, {'lov': 'arveloven', 'paragraf': '157', 'tittel': 'Tilbakekall av bostyrer', 'available': True}]},

    {'number': '157', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Tilbakekall av oppnevningen av bostyrer', 'kategori': 'arv', 'description': 'Kan tingretten fjerne en bostyrer som ikke fungerer? Ja — retten kan tilbakekalle oppnevningen ved uforsvarlig utførelse eller hvis bostyrer ikke lenger er nødvendig.', 'kort_svar': 'Tingretten kan tilbakekalle bostyrerens oppnevning hvis vedkommende ikke utfører oppgavene forsvarlig — eller hvis boet har kommet så langt at det ikke lenger er behov for bostyrer.', 'paragraftekst': 'Tingretten kan tilbakekalle bostyrerens oppnevning hvis vedkommende ikke utfører oppgavene forsvarlig — eller hvis boet har kommet så langt at det ikke lenger er behov for bostyrer.', 'hva_betyr_html': '<p>To situasjoner: (1) Uforsvarlig utførelse — etter klage etter § 156 eller på rettens eget initiativ. (2) Ikke lenger nødvendig — boet har kommet til et punkt der retten kan levere det tilbake til privat skifte.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er du misfornøyd med bostyreren: klag etter § 156. Er boet kommet langt og dere er enige: be tingretten vurdere tilbakelevering til privat skifte.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '156', 'tittel': 'Klage over bostyreren', 'available': True}, {'lov': 'arveloven', 'paragraf': '158', 'tittel': 'Tilbakelevering til privat skifte', 'available': True}]},

    {'number': '158', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Tilbakelevering av boet til privat skifte eller uskifte', 'kategori': 'arv', 'description': 'Kan et bo under offentlig skifte leveres tilbake til arvingene for privat skifte? Ja — hvis årsaken er bortfalt og alle er enige.', 'kort_svar': 'Er årsaken til det offentlige skiftet ikke lenger til stede og alle arvingene er enige, kan boet leveres tilbake til privat skifte. Tilbakeleveringen skjer ved kjennelse.', 'paragraftekst': 'Er årsaken til det offentlige skiftet ikke lenger til stede og alle arvingene er enige, kan boet leveres tilbake til privat skifte. Tilbakeleveringen skjer ved kjennelse.', 'hva_betyr_html': '<p>Offentlig skifte er ikke nødvendigvis en vei uten retur. Er årsaken borte og alle arvingene er enige, kan de ta boet tilbake og gjennomføre resten privat. Raskere og billigere. Unntak: er offentlig skifte krevd fordi arvingene truer kreditorenes dekning, må kreditorene betales eller sikres først.</p>', 'eksempler': [{'navn': 'Lars og Anne', 'tekst': 'Lars og Anne havnet i offentlig skifte på grunn av tvist om hytta. Tvisten er løst ved rettsforlik. Begge er enige om å ta resten privat. Tingretten tilbakelegger boet ved kjennelse.'}], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er konflikten løst og dere er enige: be tingretten om tilbakelevering til privat skifte.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '127', 'tittel': 'Hvem kan kreve offentlig skifte', 'available': True}, {'lov': 'arveloven', 'paragraf': '157', 'tittel': 'Tilbakekall av bostyrer', 'available': True}]},

    {'number': '159', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Innstilling av skiftebehandlingen', 'kategori': 'arv', 'description': 'Når innstilles et offentlig skifte? Hvis boet ikke har nok til å dekke skiftekostnadene — eller boet allerede er ferdigskiftet.', 'kort_svar': 'Skiftebehandlingen innstilles hvis boet ikke har nok til å dekke kostnadene ved skiftet og ingen stiller sikkerhet, eller hvis boet allerede er skiftet. Arvingene er da solidarisk ansvarlige for arvelaterens gjeld inntil boets verdi.', 'paragraftekst': 'Skiftebehandlingen innstilles hvis boet ikke har nok til å dekke kostnadene ved skiftet og ingen stiller sikkerhet, eller hvis boet allerede er skiftet. Arvingene er da solidarisk ansvarlige for arvelaterens gjeld inntil boets verdi.', 'hva_betyr_html': '<p>To situasjoner tvinger frem innstilling: (1) Tomt bo — eiendelene dekker ikke kostnadene. (2) Allerede skiftet — boet ble gjort privat uten at tingretten ble varslet. Etter innstilling er arvingene solidarisk ansvarlige for arvelaterens gjeld inntil boets verdi.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er boet lite og du er redd det ikke dekker kostnadene: ta kontakt med tingretten tidlig. Vurder statlig bistand etter § 129.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '129', 'tittel': 'Offentlig skifte av eget tiltak', 'available': True}, {'lov': 'arveloven', 'paragraf': '116', 'tittel': 'Personlig ansvar for forpliktelsene', 'available': True}]},

    {'number': '160', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Fastsettelse av booppgjøret', 'kategori': 'arv', 'description': 'Hvordan avsluttes et offentlig skifte formelt? Bostyreren utarbeider utkast, arvingene kommenterer, og tingretten fastsetter ved kjennelse.', 'kort_svar': 'Offentlig skifte avsluttes med et booppgjør fastsatt ved rettens kjennelse. Bostyreren utarbeider utkast, arvingene og gjenværende kreditorer får minst to uker til å kommentere, og retten fastsetter det endelig.', 'paragraftekst': 'Offentlig skifte avsluttes med et booppgjør fastsatt ved rettens kjennelse. Bostyreren utarbeider utkast, arvingene og gjenværende kreditorer får minst to uker til å kommentere, og retten fastsetter det endelig.', 'hva_betyr_html': '<p>Booppgjøret er sluttdokumentet. Prosessen: (1) Bostyreren utarbeider utkast. (2) Arvingene og gjenværende kreditorer får det tilsendt med minst to ukers frist til å påpeke feil. (3) Retten fastsetter ved kjennelse — bindende og endelig.</p>', 'eksempler': [{'navn': 'Mette', 'tekst': 'Mette oppdager at en bankkonto på 15 000 kr er utelatt fra utkastet. Hun melder fra innen toukersfristen. Bostyreren korrigerer. Retten fastsetter det korrigerte booppgjøret.'}], 'vanlige_feil': ['Ikke lese utkastet til booppgjør grundig — feil kan korrigeres nå, ikke etterpå', 'Vente for lenge med å melde inn feil — fristen er minimum to uker'], 'hva_bor_du_html': '<p>Mottar du utkast: les det nøye. Sjekk at alle eiendeler er med, at gjelden stemmer, og at din arveandel er riktig. Meld innsigelser skriftlig innen fristen.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '155', 'tittel': 'Utkast til booppgjør', 'available': True}, {'lov': 'arveloven', 'paragraf': '161', 'tittel': 'Oversendelse av kjennelsen', 'available': True}, {'lov': 'arveloven', 'paragraf': '162', 'tittel': 'Anke over booppgjøret', 'available': True}]},

    {'number': '161', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Oversendelse av kjennelsen om booppgjøret', 'kategori': 'arv', 'description': 'Hvem skal motta kjennelsen om booppgjøret? Alle arvingene og gjenværende kreditorer — og statsforvalteren i særlige tilfeller.', 'kort_svar': 'Kjennelsen om booppgjøret sendes straks til alle arvingene og de kreditorer som ikke allerede har fått fullt oppgjør. Er det arvinger under vergemål eller forsvunne arvinger, varsles også statsforvalteren.', 'paragraftekst': 'Kjennelsen om booppgjøret sendes straks til alle arvingene og de kreditorer som ikke allerede har fått fullt oppgjør. Er det arvinger under vergemål eller forsvunne arvinger, varsles også statsforvalteren.', 'hva_betyr_html': '<p>Varslingsplikten er bred — kjennelsen skal raskt ut til alle med interesser i boet slik at ankefristen begynner å løpe for alle samtidig. For sårbare arvinger er det egne varslingskrav.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Mottar du kjennelsen: les den umiddelbart og merk deg ankefristen på én måned. Er du uenig: kontakt advokat med én gang.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '160', 'tittel': 'Fastsettelse av booppgjøret', 'available': True}, {'lov': 'arveloven', 'paragraf': '162', 'tittel': 'Anke over booppgjøret', 'available': True}]},

    {'number': '162', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Anke over kjennelsen om booppgjøret', 'kategori': 'arv', 'description': 'Kan du anke booppgjøret? Ja — fristen er én måned fra kjennelsen ble avsagt. Retten kan også omgjøre det uten anke, så lenge det ikke krever tilbakebetaling.', 'kort_svar': 'Du kan anke kjennelsen om booppgjøret innen én måned. Retten kan også uten anke omgjøre booppgjøret hvis det ikke krever at noen betaler tilbake.', 'paragraftekst': 'Du kan anke kjennelsen om booppgjøret innen én måned. Retten kan også uten anke omgjøre booppgjøret hvis det ikke krever at noen betaler tilbake.', 'hva_betyr_html': '<p>Én måned fra kjennelsesdatoen er fristen. Anker du ikke i tide, er booppgjøret endelig. Omgjøring uten anke: er det en åpenbar teknisk feil som ikke krever tilbakebetaling, kan retten korrigere av eget tiltak.</p>', 'eksempler': [], 'vanlige_feil': ['Vente for lenge med å vurdere anke — én måned går raskt'], 'hva_bor_du_html': '<p>Les kjennelsen straks du mottar den. Er det noe du er uenig i: sett fristen i kalenderen og rådfør deg med advokat umiddelbart.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '160', 'tittel': 'Fastsettelse av booppgjøret', 'available': True}, {'lov': 'arveloven', 'paragraf': '163', 'tittel': 'Utdeling på grunnlag av booppgjøret', 'available': True}]},

    {'number': '163', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Utdelinger på grunnlag av booppgjøret', 'kategori': 'arv', 'description': 'Når kan arven faktisk utdeles etter et offentlig skifte? Normalt etter at kjennelsen om booppgjøret er rettskraftig — men i klare tilfeller kan det skje tidligere.', 'kort_svar': 'Arv utdeles normalt ikke før kjennelsen om booppgjøret er rettskraftig — etter at ankefristen er ute. Men i klare tilfeller kan en arving få sin del tidligere.', 'paragraftekst': 'Arv utdeles normalt ikke før kjennelsen om booppgjøret er rettskraftig — etter at ankefristen er ute. Men i klare tilfeller kan en arving få sin del tidligere.', 'hva_betyr_html': '<p>Rettskraft betyr at ankefristen er ute uten at noen har anket. Frem til da holdes eiendeler tilbake. Unntaket: er det helt klart hva en bestemt arving har krav på, og boets øvrige eiendeler åpenbart rekker til alle andre formål, kan bostyreren utdele til denne arvingen allerede nå.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er du arving og lurer på når du mottar din andel: normalt etter at ankefristen er ute. Er saken klar og uomtvistet: be bostyreren om foreløpig utdeling.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '160', 'tittel': 'Fastsettelse av booppgjøret', 'available': True}, {'lov': 'arveloven', 'paragraf': '162', 'tittel': 'Anke over booppgjøret', 'available': True}]},

    {'number': '164', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Eiendeler av ubetydelig verdi', 'kategori': 'arv', 'description': 'Hva gjøres med eiendeler av ubetydelig verdi i booppgjøret? De kan settes ut av betraktning hvis kostnaden ved å fordele dem overstiger verdien.', 'kort_svar': 'Eiendeler av ubetydelig verdi kan utelates fra booppgjøret hvis det ville medføre uforholdsmessig ulempe eller kostnad å ta dem med.', 'paragraftekst': 'Eiendeler av ubetydelig verdi kan utelates fra booppgjøret hvis det ville medføre uforholdsmessig ulempe eller kostnad å ta dem med.', 'hva_betyr_html': '<p>Ikke alt er verdt å fordele. Kostnaden ved å administrere overføringen kan overstige verdien — en gammel sofa, bruktbøker, en ødelagt sykkel. De kan kastes, gis bort eller avhendes uten formell behandling.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er det eiendeler med ubetydelig verdi: avtal med bostyreren at de kan settes ut av betraktning og disponeres praktisk.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '160', 'tittel': 'Fastsettelse av booppgjøret', 'available': True}]},

    {'number': '165', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Plikt til å sørge for tinglysing eller registrering', 'kategori': 'arv', 'description': 'Hvem sørger for at fast eiendom overføres og tinglyses korrekt etter et offentlig skifte? Det er rettens og bostyrerens plikt — kostnadene dekkes av boet.', 'kort_svar': 'Retten eller bostyreren plikter å sørge for at overføring av fast eiendom tinglyses i grunnboken. Panterettigheter skal registreres. Alle gebyrer dekkes av boet.', 'paragraftekst': 'Retten eller bostyreren plikter å sørge for at overføring av fast eiendom tinglyses i grunnboken. Panterettigheter skal registreres. Alle gebyrer dekkes av boet.', 'hva_betyr_html': '<p>Tinglysing er nødvendig for at eiendomsoverdragelsen er gyldig overfor tredjeparter. Under offentlig skifte er det retten og bostyreren som tar ansvaret — en klar fordel sammenlignet med privat skifte der arvingene selv må sørge for tinglysingen. Gebyrer dekkes av boet.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Er du arving og overtar eiendom: bekreft med bostyreren at tinglysingen er gjennomført. Be om bekreftet utskrift fra grunnboken.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '107', 'tittel': 'Oppgjøret ved overtakelse', 'available': True}, {'lov': 'arveloven', 'paragraf': '160', 'tittel': 'Booppgjøret', 'available': True}]},

    {'number': '166', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Eiendeler som dukker opp etter fastsettelsen av booppgjøret', 'kategori': 'arv', 'description': 'Hva skjer hvis det dukker opp eiendeler etter at booppgjøret er fastsatt? Retten sørger for fordeling — enten ved å fortsette skiftet, overføre til privat skifte, eller overlate til en arving.', 'kort_svar': 'Dukker det opp eiendeler etter at booppgjøret er fastsatt, skal retten sørge for at de fordeles — ved å fortsette det offentlige skiftet, overføre til privat skifte, eller overlate til én arving.', 'paragraftekst': 'Dukker det opp eiendeler etter at booppgjøret er fastsatt, skal retten sørge for at de fordeles — ved å fortsette det offentlige skiftet, overføre til privat skifte, eller overlate til én arving.', 'hva_betyr_html': '<p>Et booppgjør er ikke nødvendigvis siste ord. Retten har tre alternativer: (1) Fortsette offentlig skifte — for verdifulle og komplekse eiendeler. (2) Overføre til privat skifte — arvingene er enige. (3) Overlate til én arving — for lave beløp.</p>', 'eksempler': [], 'vanlige_feil': [], 'hva_bor_du_html': '<p>Dukker det opp eiendeler etter booppgjøret: meld fra til tingretten umiddelbart. Ikke prøv å fordele dem informelt.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '160', 'tittel': 'Fastsettelse av booppgjøret', 'available': True}, {'lov': 'arveloven', 'paragraf': '158', 'tittel': 'Tilbakelevering til privat skifte', 'available': True}]},

]

PARAGRAPHS = PARAGRAPHS + _ARVELOVEN_118_166

_ARVELOVEN_171_180 = [
    {'number': '171', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Partsevne under offentlig skifte', 'kategori': 'arv', 'description': 'Hvem er motparten når du krangler i et offentlig arveoppgjør? Det avhenger av hva krangelen gjelder.', 'kort_svar': 'Hvem du krangler med avhenger av hva krangelen gjelder. Kreditorkrav rettes mot boet. Krangler arvingene seg imellom, er de uenige arvingene motpart — ikke selve boet.', 'paragraftekst': 'Et dødsbo under offentlig skifte har partsevne. I tvist om krav mot boet er boet part. I tvist om krav fra en arving er de arvingene som bestrider kravet, motparter. I tvist om et krav fra eller mot en tredjeperson er de arvingene som engasjerer seg, parter.', 'hva_betyr_html': '<p>I jusen snakker man om «partsevne» — retten til å være saksøker eller saksøkt. Denne paragrafen forklarer hvem som har denne rollen under offentlig skifte.</p><p><strong>Kreditorkrav:</strong> Har avdøde en ubetalt regning og bostyreren nekter å betale den, må snekkeren saksøke selve boet — ikke arvingene personlig.</p><p><strong>Arving mot arving:</strong> Krangler dere om hvem som skal ha hytta, kan du ikke saksøke boet. Du må saksøke den eller de arvingene som er uenige med deg.</p><p><strong>Boet mot tredjeperson:</strong> Er det noen utenfor boet som påstår de eier noe av eiendelene, er det de arvingene som engasjerer seg i saken som formelt blir parter. Vinner de slik at boet får inn mer verdier, kan de få dekket saksomkostningene som massekrav.</p>', 'eksempler': [{'navn': 'Kari og Marius', 'tekst': 'Kari mener hun har krav på 200 000 kr fra boet fordi hun betalte morens sykehjemopphold. Marius bestrider kravet. Kari reiser skiftetvist — og det er Marius hun møter i retten som saksøkt, ikke «dødsboet».'}], 'vanlige_feil': ['Rette et søksmål mot «Dødsboet etter Hans Hansen» når krangelen handler om at de andre arvingene nekter deg en gjenstand', 'Tro at bostyreren automatisk fører alle rettssaker for dere — arvingene må selv kjempe og ta risikoen for egne advokatutgifter'], 'hva_bor_du_html': '<p>Når du skal reise tvist under et offentlig skifte, må du sette riktig motpart på papiret. Er du i konflikt med søsknene dine, er det deres navn som skal stå som saksøkte. Bruk advokat til å sette opp prosesskrivet — feil motpart kan føre til at saken avvises.</p>', 'dumme_sporsmal': [{'q': 'Får jeg dekket advokatutgiftene mine av dødsboet?', 'a': 'Som hovedregel nei. Krangler du med en annen arving, betaler hver av dere egne advokater. Du kan bare få dekket utgiftene av boet hvis du vant en tvist mot en utenforstående tredjeperson, og dette kom boet til gode.'}], 'related': [{'lov': 'arveloven', 'paragraf': '168', 'tittel': 'Skiftetvist', 'available': True}, {'lov': 'arveloven', 'paragraf': '172', 'tittel': 'Rettskraft', 'available': True}]},
    {'number': '172', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Rettskraft for avgjørelser under offentlig skifte', 'kategori': 'arv', 'description': 'Når tingretten tar en avgjørelse i et arveoppgjør, gjelder den for alle arvingene — også de som ikke deltok i rettssaken.', 'kort_svar': 'En avgjørelse under et offentlig skifte er bindende for boet og for absolutt alle med interesser i boet. Du kan ikke starte saken på nytt fordi du ikke deltok. Tingretten kan også bestemme at avgjørelsen skal brukes umiddelbart, før ankefristen er ute.', 'paragraftekst': 'Avgjørelser under skiftet gjelder for og mot boet og alle som har interesser i boet. Tingretten avgjør om en avgjørelse den eller andre domstoler har truffet under skiftet, skal legges til grunn for den videre skiftebehandlingen før avgjørelsen er blitt rettskraftig.', 'hva_betyr_html': '<p>Dommeren avgjør en konflikt under offentlig skifte — og avgjørelsen binder absolutt alle, ikke bare de som deltok i rettssaken.</p><p>Eksempel: To søsken tar en konflikt om testamentets gyldighet til retten. Det tredje søskenet deltok ikke. Vinner det ene søskenet, gjelder avgjørelsen likevel for alle tre. Det tredje søskenet kan ikke starte en ny rettssak om akkurat det samme.</p><p>I tillegg kan tingretten bestemme at en dom skal brukes umiddelbart for å komme videre med fordelingen — selv før ankefristen (normalt én måned) er ute.</p>', 'eksempler': [{'navn': 'Eva og brødrene', 'tekst': 'To brødre krangler om et bankinnskudd på 500 000 kr var lån eller gave. Eva blander seg ikke inn. Dommeren avgjør at det var lån som betales tilbake til boet. Eva er bundet av avgjørelsen — og tjener på den, fordi mer penger i boet gir henne mer i arv.'}], 'vanlige_feil': ['Tro at du «slipper unna» effekten av en dom hvis du bare lar være å møte opp', 'Tro at du kan anlegge en ny, identisk rettssak fordi du «ikke var part»'], 'hva_bor_du_html': '<p>Følg nøye med på hva de andre arvingene foretar seg under et offentlig skifte. Hvis noen reiser en skiftetvist som vil påvirke din andel, bør du vurdere å melde deg på i saken. Det hjelper ikke å klage i ettertid.</p>', 'dumme_sporsmal': [{'q': 'Kan retten dele ut penger før ankefristen har gått ut?', 'a': 'Tingretten kan legge dommen til grunn for videre skiftebehandling, men selve utdelingen til arvingene skjer normalt ikke før booppgjøret er helt rettskraftig.'}], 'related': [{'lov': 'arveloven', 'paragraf': '171', 'tittel': 'Partsevne under offentlig skifte', 'available': True}, {'lov': 'arveloven', 'paragraf': '163', 'tittel': 'Utdeling på grunnlag av booppgjøret', 'available': True}]},
    {'number': '173', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Behandling av skiftetvist ved allmennprosess', 'kategori': 'arv', 'description': 'Hvis krangelen under et arveoppgjør gjelder store beløp eller er svært komplisert, kan dommeren bestemme at den skal behandles som en fullverdig vanlig rettssak.', 'kort_svar': 'En skiftetvist er vanligvis en litt forenklet sak inne i arveoppgjøret. Men hvis det står om verdier over 250 000 kr, kan dommeren gjøre den om til en fullverdig vanlig rettssak (allmennprosess). Da settes en fast frist for å levere formell stevning — og saken hopper over forliksrådet.', 'paragraftekst': 'Hvis tvistesummen er over 250 000 kr, kan retten på begjæring eller av eget tiltak beslutte at kravet skal behandles ved allmennprosess. Tvist mot en tredjeperson skal behandles ved allmennprosess hvis tredjepersonen krever det. Saksøkeren gis en frist for å ta ut stevning. En tvist som overføres til allmennprosess, behandles ikke i forliksrådet.', 'hva_betyr_html': '<p>En skiftetvist kan gjøres litt enklere og raskere enn en vanlig rettssak. Men dommeren kan si: «Dette er for stort og vanskelig — vi behandler det som en vanlig rettssak (allmennprosess).»</p><p>To ting vurderes: (1) <strong>Beløp</strong> — krangelen må handle om verdier over 250 000 kr. (2) <strong>Behov</strong> — mange vitner, kompliserte juridiske spørsmål, eller stopper krangelen opp hele arveoppgjøret?</p><p>Krangler boet med en tredjeperson og beløpet er over 250 000 kr, har tredjepersonen <em>krav</em> på at saken blir en vanlig rettssak. Bommer du på fristen retten setter for stevning, taper du kravet.</p>', 'eksempler': [{'navn': 'Jonas og søsknene', 'tekst': 'Jonas påstår faren ga ham en hytte på 3 mill i gave to år før han døde. Søsknene krever hytta tilbake til boet. Fordi saken krever vitner, legejournaler og handler om store penger, bestemmer dommeren allmennprosess. Jonas får fire uker på seg til å levere stevning for å forsvare eierskapet sitt.'}], 'vanlige_feil': ['Tro at du kan skrive et vanlig klagebrev til dommeren — en stevning krever strenge juridiske formkrav', 'Ikke hyre advokat når saken blir en allmennprosess — risikoen for å måtte betale enorme saksomkostninger hvis du taper er reell'], 'hva_bor_du_html': '<p>Når du får beskjed om at retten vurderer allmennprosess eller gir deg frist for stevning: skaff advokat umiddelbart. Vurder om kravet ditt er sterkt nok til å tåle risikoen ved en full rettssak.</p>', 'dumme_sporsmal': [{'q': 'Må vi innom forliksrådet først?', 'a': 'Nei — loven slår uttrykkelig fast at skiftetvister som gjøres om til vanlig rettssak, går rett til tingretten.'}], 'related': [{'lov': 'arveloven', 'paragraf': '168', 'tittel': 'Skiftetvist', 'available': True}, {'lov': 'arveloven', 'paragraf': '170', 'tittel': 'Frister for å reise skiftetvist', 'available': True}]},
    {'number': '174', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Krangel om testamentarisk stiftelse', 'kategori': 'arv', 'description': 'Har avdøde bestemt i testamentet at pengene skal gå til å starte en stiftelse, og du mener dette er ugyldig? Da får du en kort frist til å gå til sak.', 'kort_svar': 'Sier testamentet at arven skal brukes til å opprette en stiftelse, og arvingene mener dette er ugyldig, setter retten en klar frist for å gå til sak. Går fristen ut uten at noen reiser sak, blir stiftelsen opprettet — og pengene går dit.', 'paragraftekst': 'Går et testament ut på at det skal opprettes en stiftelse, og noen av arvingene bestrider testamentets bestemmelse om stiftelsens arverett, skal tingretten gi vedkommende en frist for å reise skiftetvist. Er det ikke reist tvist innen fristen, legges testamentets bestemmelse om stiftelsen til grunn.', 'hva_betyr_html': '<p>Noen ganger etterlater folk seg et testament der formuen skal brukes til å opprette en stiftelse. For barna kan det bety at de mister mye penger. Mener de testamentet er ugyldig (for eksempel at mor var dement da hun skrev det), MÅ de ta affære.</p><p>Dommeren setter en klar frist. Reiser arvingene ikke sak innen fristen, anses testamentet som gyldig — og stiftelsen får pengene.</p><p><strong>Hvem er motparten?</strong> Stiftelsen eksisterer ikke ennå. Melder noen seg frivillig for å forsvare stiftelsen, blir den personen motpart. Melder ingen seg, går saken uten en formell motpart — dommeren vurderer bevisene likevel.</p>', 'eksempler': [{'navn': 'Lars', 'tekst': 'Lars er eneste arving etter en barnløs tante med 4 mill. Testamentet sier alt skal til en trebåt-stiftelse. Lars mener tanten var dement da hun skrev det. Tingretten setter frist. Lars leverer innen fristen. Ingen forsvarer stiftelsen. Retten ser på legejournalene, bekrefter at tanten manglet testasjonsevne, og kjenner testamentet ugyldig. Lars arver 4 millioner.'}], 'vanlige_feil': ['Tro at saken automatisk avsluttes til din fordel fordi stiftelsen ikke kan forsvare seg', 'Ikke ta fristen fra domstolen på alvor — glemmer du den, blir stiftelsen en realitet'], 'hva_bor_du_html': '<p>Mener du testamentet er ugyldig: samle inn bevis med én gang — legejournaler, vitneforklaringer fra helsepersonell. Skaff deg advokat. Tidsfrister i skiftetvister er absolutte.</p>', 'dumme_sporsmal': [{'q': 'Kan vi ikke bare bli enige om å ignorere testamentet?', 'a': 'Nei. Myndighetene vil passe på at avdødes ønske følges, med mindre dere beviser at testamentet faktisk er rettslig ugyldig i retten.'}], 'related': [{'lov': 'arveloven', 'paragraf': '170', 'tittel': 'Frister for å reise skiftetvist', 'available': True}, {'lov': 'arveloven', 'paragraf': '45', 'tittel': 'Ugyldighet på grunn av utnyttelse', 'available': True}]},
    {'number': '175', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Insolvent dødsbo — virkeområde', 'kategori': 'arv', 'description': 'Hva skjer når en som dør etterlater seg mer gjeld enn penger, og ingen arvinger vil ta ansvar for gjelden? Dødsboet settes under behandling som insolvent.', 'kort_svar': 'Har den avdøde mer gjeld enn eiendeler, og ingen arvinger har påtatt seg gjeldansvaret, behandles boet som et insolvent bo — omtrent som en konkurs. Arvingene arver ingenting, men arver heller ingen gjeld.', 'paragraftekst': '§§ 175 til 178 gjelder hvis eiendelene i boet ikke er tilstrekkelige til å oppfylle alle forpliktelsene etter arvelateren (insolvent dødsbo), og det ikke er noen av arvingene som har overtatt ansvaret for arvelaterens forpliktelser.', 'hva_betyr_html': '<p>Et «insolvent dødsbo» betyr rett og slett at kassa er tom. Gjelden er større enn formuen.</p><p>Når arvingene velger offentlig skifte og det bekreftes at det er mer gjeld enn verdier, styres alt videre av §§ 175–178. Det minner om konkursregler: Alle kreditorer melder inn kravene sine og får kanskje bare tilbake en liten prosentandel av det de krevde. Resten av gjelden slettes. Dere arvinger arver ingenting, men heller ingen gjeld.</p><p>Dette gjelder <em>bare</em> hvis ingen av arvingene har signert på at de tar over gjeldansvaret.</p>', 'eksempler': [{'navn': 'Petter', 'tekst': 'Faren etterlot 70 000 kr (konto + bil), men 800 000 kr i kredittkortgjeld. Petter velger offentlig skifte og fraskriver seg gjeldansvaret. Tingretten fastslår insolvent bo. Bostyrer selger bilen, bruker pengene til begravelse og skiftekostnader. Bankene får ingenting. Petter går videre uten gjeld.'}], 'vanlige_feil': ['Signere på at du «påtar deg ansvaret for gjelden» fordi du trodde du måtte — da gjelder ikke disse særreglene og du hefter personlig', 'Begynne å betale småregninger for avdøde fra din egen konto før du vet om boet er solvent'], 'hva_bor_du_html': '<p>Er du det minste i tvil om avdøde hadde mer gjeld enn penger: IKKE signer på at du overtar gjeldsansvaret. La boet gå til offentlig skifte. Kreditorene tar tapet — ikke du.</p>', 'dumme_sporsmal': [{'q': 'Får jeg noe av arven hvis boet er insolvent?', 'a': 'Nei. All gjeld skal dekkes før arvingene får én krone. Siden gjelden er større enn eiendelene, er det null igjen til arvingene.'}, {'q': 'Kan kreditorene komme etter meg senere?', 'a': 'Ikke hvis du har nektet å påta deg ansvaret og boet ble gjort opp som insolvent offentlig skifte.'}], 'related': [{'lov': 'arveloven', 'paragraf': '116', 'tittel': 'Ansvaret for arvelaterens forpliktelser', 'available': True}, {'lov': 'arveloven', 'paragraf': '176', 'tittel': 'Prøving av krav og omstøtelse', 'available': True}, {'lov': 'arveloven', 'paragraf': '177', 'tittel': 'Rettsvern og utlegg', 'available': True}]},
    {'number': '176', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Prøving av krav og omstøtelse i insolvent bo', 'kategori': 'arv', 'description': 'Hva skjer i et tomt dødsbo? Retten går gjennom alle regningene — og kan kreve tilbake gaver avdøde ga rett før de døde.', 'kort_svar': 'Når dødsboet har mer gjeld enn penger, sjekker bostyreren om alle kravene er ekte og gyldige. Domstolen kan også kreve tilbake store gaver eller overføringer som den avdøde gjorde rett før dødsfallet, for å sikre at kreditorene får det de har krav på.', 'paragraftekst': 'Kravene fra kreditorene skal undersøkes av bostyreren. Tingretten kan bestemme at overføringer og gaver gjort før dødsfallet kan gjøres ugyldige (omstøtes) etter reglene i dekningsloven kapittel 5.', 'hva_betyr_html': '<p>Når det ikke er nok penger til å dekke avdødes gjeld, jobber bostyreren som i en vanlig bedriftskonkurs.</p><p><strong>Prøving av krav:</strong> Advokaten sjekker om fakturaene faktisk stemmer. Kanskje noe er foreldet, eller regningen gjelder noe avdøde aldri bestilte.</p><p><strong>Omstøtelse:</strong> Hvis avdøde visste at de var på randen av personlig konkurs og overførte hytta til barnebarnet gratis rett før de døde, kan retten «omstøte» gaven — barnebarnet må levere tilbake hytta eller pengene, slik at verdiene brukes til å betale lovlig gjeld.</p>', 'eksempler': [{'navn': 'Håkon', 'tekst': 'Håkon er alvorlig syk og har en million i kredittkortgjeld. To uker før han dør, gir han bilen sin (verdt 300 000 kr) gratis til niesen. Etter Håkons død åpnes insolvent offentlig skifte. Bostyreren krever bilen tilbake fra niesen via omstøtelse. Bilen selges for å betale deler av kredittkortgjelden.'}], 'vanlige_feil': ['Tro at man trygt kan «redde» verdier ved å overføre dem til familien når man er syk og har mye gjeld', 'Tro at bostyreren bare betaler alt som ligger i postkassen uten å sjekke om kravene er reelle'], 'hva_bor_du_html': '<p>Ikke prøv å gjemme unna verdier hvis du vet at avdøde var tungt forgjeldet. Omstøtelse kan ramme deg som mottaker — du kan bli tvunget til å betale tilbake hele beløpet, selv om du allerede har brukt pengene.</p>', 'dumme_sporsmal': [{'q': 'Hvor langt tilbake i tid kan de hente gaver?', 'a': 'Vanligvis de siste ett til to årene før dødsfallet. I spesielle tilfeller, spesielt til nær familie, kan de gå enda lenger tilbake. Dekningsloven kapittel 5 regulerer dette.'}, {'q': 'Kan de ta tilbake vanlige julegaver?', 'a': 'Nei. Vanlige leilighetsgaver som ikke står i åpenbart misforhold til avdødes økonomi, blir ikke omstøtt.'}], 'related': [{'lov': 'arveloven', 'paragraf': '175', 'tittel': 'Insolvent dødsbo — virkeområde', 'available': True}, {'lov': 'arveloven', 'paragraf': '177', 'tittel': 'Rettsvern og utlegg', 'available': True}]},
    {'number': '177', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Rettsvern og utlegg i insolvente dødsbo', 'kategori': 'arv', 'description': 'Når et dødsbo er insolvent, fryses situasjonen. Kreditorer kan ikke ta nye pant i avdødes eiendeler etter at personen er død.', 'kort_svar': 'Når noen dør og har mer gjeld enn penger, setter loven en stopper for at kreditorer kan karre til seg verdier. Fra og med dødsdagen er det forbudt å ta tvangspant (utlegg) i avdødes eiendeler for gammel gjeld.', 'paragraftekst': 'Reglene om rettsvern i konkurs gjelder, og dødsdagen regnes som datoen for konkursåpning. Det er ikke lov til å ta utlegg i dødsboets eiendeler for krav og gjeld som oppsto før personen døde.', 'hva_betyr_html': '<p>I det øyeblikket en person dør med mer gjeld enn eiendeler, trykker loven på «frys»-knappen. Alle kreditorer skal behandles mest mulig rettferdig.</p><p>Normalt kan inkassoselskapet ta «utlegg» (tvangspant) i eiendeler hvis du ikke betaler. Men etter at personen er død, er dette forbudt. Kreditorer med ubetalte fakturaer fra før dødsfallet må stille seg i kø og melde inn kravet til bostyreren — de kan ikke snike seg forbi ved å ta pant i eiendelene.</p><p>Dødsdagen er den offisielle skjæringsdatoen (konkursåpningsdagen), selv om papirarbeidet for offentlig skifte skjer uker senere.</p>', 'eksempler': [{'navn': 'Ingrid', 'tekst': 'Ingrid dør med mye gjeld. To dager etter dødsfallet forsøker et inkassobyrå å ta pant i huset hennes via namsmannen. Siden boet er insolvent og dødsdagen er passert, avvises forsøket. Inkassobyrået må melde kravet i boet på lik linje med alle andre.'}], 'vanlige_feil': ['La en kreditor skremme deg med at de skal ta pant i avdødes eiendeler kort tid etter dødsfallet', 'Tro at du som arving må betale småregninger for å unngå at noen tar beslag'], 'hva_bor_du_html': '<p>Truer et inkassoselskap med utlegg i avdødes eiendeler etter dødsfallet: forholde deg rolig. Send dem kopi av dødsattesten og vis til at boet er til offentlig skifte som insolvent bo. Henvis dem direkte til tingretten eller bostyreren.</p>', 'dumme_sporsmal': [{'q': 'Hva hvis de rakk å ta pant i bilen uken FØR personen døde?', 'a': 'Da har de rettsvern og stiller lenger fremme i køen. Et gyldig pant fra før dødsfallet gjelder fortsatt.'}, {'q': 'Gjelder dette også lån med pant i boligen?', 'a': 'Banken har allerede tinglyst pant da boliglånet ble tatt opp — det pantet gjelder fortsatt. Paragrafen forbyr nye tvangspant for usikret gjeld etter at personen er død.'}], 'related': [{'lov': 'arveloven', 'paragraf': '175', 'tittel': 'Insolvent dødsbo — virkeområde', 'available': True}, {'lov': 'arveloven', 'paragraf': '176', 'tittel': 'Prøving av krav og omstøtelse', 'available': True}, {'lov': 'arveloven', 'paragraf': '178', 'tittel': 'Tvangsakkord', 'available': True}]},
    {'number': '178', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Tvangsakkord', 'kategori': 'arv', 'description': 'Arvinger kan tilby kreditorene en deal for å slette gjelden i et insolvent dødsbo. Sier flertallet ja, må resten av kreditorene godta tapet.', 'kort_svar': 'Har dødsboet enormt med gjeld, kan arvingene foreslå en tvangsakkord — de tilbyr kreditorene en prosentandel av det de krevde, mot å ta over boet. Sier flertallet ja, slettes resten av gjelden. Arvingene overtar boet, men er personlig ansvarlige for akkordbeløpet.', 'paragraftekst': 'Etter at fristen for å melde krav (proklama) har gått ut, kan arvingene foreslå en tvangsakkord for å slette deler av gjelden. Forutsetningen er at arvingene formelt påtar seg fullt personlig ansvar for å betale akkorden som inngås. Reglene om tvangsakkord i konkursloven gjelder for prosessen.', 'hva_betyr_html': '<p>En «tvangsakkord» er en juridisk avtale. Arvingene sier til retten: «Vi tilbyr å betale dere 500 000 kr av vår private formue hvis dere stryker resten av gjelden, slik at vi kan overta boet.»</p><p>Kreditorene stemmer. Er flertallet (målt etter gjeld, ikke antall) for, tvinges alle til å godta avtalen — også de som stemte nei.</p><p>Haken: Arvingene MÅ signere på fullt, personlig og ubegrenset ansvar for akkordbeløpet. De kan ikke trekke seg. Tingretten godkjenner og krever at det stilles sikkerhet.</p>', 'eksempler': [{'navn': 'Jonas og søsteren', 'tekst': 'Faren etterlot 4 mill i gjeld og et hus verdt 2 mill. Jonas vil redde huset. De tilbyr tvangsakkord: betaler 3 mill (har fått lån i sin bank). Bankene innser de ville fått mye mindre ved tvangssalg og stemmer ja. Tingretten godkjenner. Jonas og søsteren betaler 3 mill, restgjelden slettes, og de overtar huset privat.'}], 'vanlige_feil': ['Tilby mer enn dere egentlig har råd til personlig — husk at dere overtar ansvaret fullt ut', 'Tro at dere kan forhandle med bankene i skjul — alt må gå åpent gjennom domstolen'], 'hva_bor_du_html': '<p>Dette er ikke et gjør-det-selv-prosjekt. Vurderer du tvangsakkord, kontakt advokat med erfaring fra konkurs- og skifterett. Advokaten setter opp et realistisk tilbud og forhandler på dine vegne.</p>', 'dumme_sporsmal': [{'q': 'Hvorfor skulle bankene si ja til å slette gjeld?', 'a': 'Fordi alternativet er verre — mye penger går til advokatutgifter og salgskostnader. Kreditorene stemmer ja til akkord hvis tilbudet gir dem mer og raskere enn tvangssalg.'}, {'q': 'Hva skjer hvis en av bankene nekter?', 'a': 'Hvis flertallet av gjelden stemmer ja, kan domstolen tvinge mindretallet til å godta avtalen. Derav navnet tvangsakkord.'}], 'related': [{'lov': 'arveloven', 'paragraf': '175', 'tittel': 'Insolvent dødsbo — virkeområde', 'available': True}, {'lov': 'arveloven', 'paragraf': '100', 'tittel': 'Utstedelse av proklama', 'available': True}, {'lov': 'arveloven', 'paragraf': '116', 'tittel': 'Ansvaret for arvelaterens forpliktelser', 'available': True}]},
    {'number': '179', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Ikrafttredelse', 'kategori': 'arv', 'description': 'Arveloven vi bruker i dag begynte å gjelde fra 1. januar 2021. Den erstattet da to svært gamle lover om arv og skifte.', 'kort_svar': 'Arveloven trådte i kraft 1. januar 2021. Samtidig ble den gamle arveloven fra 1972 og skifteloven fra 1930 opphevet.', 'paragraftekst': 'Loven trer i kraft 1. januar 2021. Skifteloven fra 1930 og arveloven fra 1972 oppheves. Forskrifter gitt under de gamle lovene fortsetter å gjelde inntil videre.', 'hva_betyr_html': '<p>Jurister og domstoler trenger en bestemt dato for når de skal slutte å bruke en gammel bok og begynne å bruke en ny. Arveloven er klar på dette: 1. januar 2021. Siden vi tidligere hadde to lover for arveoppgjør (én om <em>hvem</em> som skulle arve, og én om den praktiske ryddejobben), var det praktisk å slå dem sammen til én.</p>', 'eksempler': [{'navn': 'Per', 'tekst': 'Pers mor døde 14. desember 2020 — da gjelder de gamle lovene fra 1972 og 1930. Døde hun 2. januar 2021, gjelder den nye loven for oppgjøret.'}], 'vanlige_feil': ['Bruke regler fra 2021 på et gammelt arveoppgjør — det er egne overgangsregler for slikt i § 180', 'Finne en artikkel fra 2018 og bruke den i et arveoppgjør i dag — pass på at informasjonen er oppdatert for loven fra 2021'], 'hva_bor_du_html': '<p>Er du i tvil om hvilken lov som gjelder i ditt tilfelle: sjekk dødsdatoen. Var det etter 1. januar 2021, gjelder den nye arveloven. Se § 180 for overgangsregler.</p>', 'dumme_sporsmal': [], 'related': [{'lov': 'arveloven', 'paragraf': '180', 'tittel': 'Overgangsregler', 'available': True}]},
    {'number': '180', 'lov': 'arveloven', 'lov_display': 'Arveloven', 'title': 'Overgangsregler', 'kategori': 'arv', 'description': 'Døde noen før 2021, eller sitter noen i et gammelt uskiftebo? Denne paragrafen forklarer om du skal bruke de gamle eller de nye arvereglene.', 'kort_svar': 'Dødsdatoen avgjør hvilken lov som gjelder. Døde de etter 1. januar 2021, bruker du den nye arveloven. Uskiftebo etter person som døde før 2021 skiftes etter den nye loven. Testamenter bedømmes etter reglene da de ble skrevet, men pliktdelsarven følger den nye loven.', 'paragraftekst': 'Loven gjelder for dødsfall som skjer etter at loven har begynt å gjelde (1. januar 2021). Et uskiftebo etter en person som døde før loven gjaldt, skal skiftes etter den nye loven hvis lengstlevende dør eller boet kreves skiftet etter ikrafttredelsen. Testamenter bedømmes ut fra reglene da de ble skrevet, men begrensningene i barns pliktdelsarv reguleres av den nye loven.', 'hva_betyr_html': '<p>Tre viktige kjøreregler:</p><p>1. <strong>Dødsdatoen avgjør:</strong> Døde faren din 20. desember 2020, er det den gamle arveloven fra 1972 som gjelder for oppgjøret hans, selv om papirarbeidet tas i 2025.</p><p>2. <strong>Uskiftet bo:</strong> Sitter moren din i uskifte etter faren som døde i 2010, og moren dør nå, skal <em>hele</em> boet fordeles etter den nye loven fra 2021.</p><p>3. <strong>Gamle testamenter:</strong> Formelle krav (underskrifter, vitner) bedømmes etter loven da testamentet ble skrevet. Men pliktdelsarven — hvor mye barna minst har krav på — følger den <em>nye</em> loven på dødstidspunktet. I den nye loven økte pliktdelsarven per barn fra 1 million til 15 ganger grunnbeløpet (ca. 1,9 millioner kr i 2025).</p>', 'eksempler': [{'navn': 'Anne', 'tekst': 'Faren skrev testament i 2015 og begrenset barnas pliktdelsarv til 1 mill kr. Han dør i mars 2021. Den nye loven gir barna rett til 15 ganger grunnbeløpet (ca. 1,9 mill). Anne får overkrevet den gamle begrensningen og mottar nesten 2 millioner. Røde Kors får resten.'}], 'vanlige_feil': ['Tro at foreldrenes testament fra 1990 kan nekte deg den nye, høye grensen for pliktdelsarv', 'Google arveregler og bruke en artikkel fra 2018 i et arveoppgjør i dag — sjekk at informasjonen er fra 2021 eller nyere'], 'hva_bor_du_html': '<p>Når du leser et eldre testament: husk at pliktdelsbeløpene er «oppgradert» av den nye loven. Er boet vanskelig: gi advokaten riktig dato for både dødsfallet og testamentets opprettelse.</p>', 'dumme_sporsmal': [{'q': 'Hva hvis testamentet ble skrevet feil på 90-tallet?', 'a': 'Formkravene bedømmes etter loven fra 1990. Var testamentet ugyldig skrevet den gangen, forblir det ugyldig i dag.'}, {'q': 'Gjelder den nye loven hvis vi fordeler uskifteboet nå?', 'a': 'Ja. Sitter moren din i uskifte etter faren som døde for lenge siden, og hun i dag velger å skifte, gjelder den nye loven.'}], 'related': [{'lov': 'arveloven', 'paragraf': '179', 'tittel': 'Ikrafttredelse', 'available': True}, {'lov': 'arveloven', 'paragraf': '50', 'tittel': 'Livsarvingenes pliktdelsarv', 'available': True}, {'lov': 'arveloven', 'paragraf': '14', 'tittel': 'Retten til uskifte', 'available': True}]},
]

PARAGRAPHS = PARAGRAPHS + _ARVELOVEN_171_180
