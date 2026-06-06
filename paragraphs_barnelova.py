"""Barnelova — paragraf-data for Rettsregel."""

PARAGRAPHS = [
    {
        "number": "1",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Fødselsmelding",
        "kategori": "familie",
        "description": "Hvem har ansvaret for å melde ifra til det offentlige om at et barn er født? Sykehuset gjør det vanligvis, men føder du hjemme må du melde fra selv.",
        "kort_svar": "Når et barn blir født, skal sykehuset automatisk sende en fødselsmelding til Folkeregisteret. Føder du hjemme eller et annet sted uten at helsepersonell er til stede, har du selv ansvaret for å melde fra innen én måned.",
        "paragraftekst": """Når eit barn er født, skal lækjaren eller jordmora gje fødselsmelding til folkeregistermyndigheita. I meldinga skal opplysast kven som er far til barnet i samsvar med § 3 eller § 4, eller kven mora har gjeve opp som far til barnet i tilfelle der farskapen enno ikkje er fastsett. I meldinga skal også opplysast om foreldra lever saman. Meldinga skal dessutan innehalde dei opplysningane som departementet fastset.

Når barnet er født utan at lækjar eller jordmor var til stades, skal mora sjølv gje fødselsmelding til folkeregistermyndigheita innan ein månad. Føder ho barnet medan ho mellombels held til i utlandet, skal ho gje melding til folkeregistermyndigheita innan ein månad etter at barnet er kome til Noreg.

Fødselsmelding skal også gjevast når barnet er dødfødt.

I tilfelle då farskapen enno ikkje er fastsett eller foreldra ikkje lever saman, skal fødselsmeldinga sendast både til folkeregistermyndigheita og tilskotsfuten.""",
        "hva_betyr_html": """<p>Loven sikrer at staten får beskjed hver gang en ny innbygger kommer til verden. Hvis du føder på et sykehus, eller har en jordmor eller lege hjemme under fødselen, er det helsepersonellet som gjør hele jobben med papirene. De sender fødselsmelding til Folkeregisteret (Skatteetaten). Du trenger ikke tenke på det.</p>
<p>Meldingen inneholder mer enn bare at et barn er født. Den skal også oppgi hvem som er faren eller medmoren. Hvis dere ikke er gift, og farskapet ikke er formelt bekreftet ennå, skal sykehuset notere hvem du oppgir at faren er. De skal også registrere om foreldrene bor sammen. Hvis dere ikke bor sammen, eller faren er ukjent, går det en egen kopi av meldingen til NAV (som loven kaller tilskotsfuten) slik at de kan sikre barnets rettigheter knyttet til barnebidrag og farskap.</p>
<p>Føder du derimot alene uten at lege eller jordmor er til stede, faller ansvaret på deg. Da må du ta kontakt med Skatteetaten (Folkeregisteret) og fylle ut fødselsmeldingen selv. Du har én måned på deg. Det samme gjelder hvis du føder under et midlertidig opphold i utlandet.</p>
<p>Regelen gjelder også ved dødfødsler. Dette sikrer at barnet blir riktig registrert og at foreldrene får de rettighetene de har krav på, for eksempel foreldrepenger og pleiepenger.</p>
<h3>Fødsel under ferie eller opphold i utlandet</h3>
<p>Mange kvinner drar på ferie eller studerer i utlandet mens de er gravide. Skulle fødselen skje der, får ikke det norske Folkeregisteret automatisk beskjed fra det utenlandske sykehuset. Du er da pliktig til å melde ifra til Folkeregisteret selv.</p>
<p>Fristen for å melde fra er én måned etter at du og barnet har kommet tilbake til Norge. Du må da ta med dokumentasjon fra sykehuset i utlandet som bekrefter at det er du som har født barnet.</p>""",
        "eksempler": [{"navn": "Sara", "tekst": "Sara er på hyttetur på fjellet. Fødselen starter plutselig fire uker før termin. Snøstorm gjør at ambulansen ikke rekker frem i tide, og Sara føder barnet alene på badet. Alt går bra med mor og barn. Siden ingen lege eller jordmor var til stede da barnet ble født, må Sara selv sende inn fødselsmelding til Skatteetaten (Folkeregisteret) i løpet av de neste ukene."}],
        "vanlige_feil": ["Foreldre prøver å sende inn skjemaer til Folkeregisteret etter en normal sykehusfødsel, noe som bare skaper dobbeltarbeid.", "Glemmer å melde fra til norske myndigheter etter å ha født i utlandet.", "Nekter å oppgi fars navn til sykehuset i tro om at saken stoppes. Den sendes bare videre til NAV."],
        "hva_bor_du_html": """<p>Har du en normal fødsel med helsepersonell til stede? Da gjør du ingenting. Sykehuset ordner papirene. Etter kort tid vil du få et brev fra Skatteetaten (ofte i Altinn) der du blir bedt om å velge navn til barnet.</p>
<p>Føder du uten lege eller jordmor, eller i utlandet? Kontakt Skatteetaten så raskt du er hjemme for veiledning om hvilke papirer de krever for å registrere barnet. Dette må gjøres før det har gått én måned.</p>""",
        "dumme_sporsmal": [
            {"q": "Får jeg fødselsattest automatisk i posten?", "a": "Nei, du får en forespørsel fra Skatteetaten om å velge navn. Når navnet er godkjent og registrert, får barnet et personnummer, og da kan du bestille fødselsattest via Altinn eller Skatteetatens nettsider."},
            {"q": "Hva skjer hvis jeg ikke vet hvem faren er når sykehuset spør?", "a": "Da sier du bare at faren er ukjent. Sykehuset sender fødselsmeldingen til Folkeregisteret og NAV. NAV vil deretter ta kontakt med deg i ettertid for å hjelpe med å finne ut hvem faren er, siden barnet har rett til å kjenne foreldrene sine."},
            {"q": "Må vi melde fra til sykehuset om at vi er samboere?", "a": "Ja, sykehuset spør vanligvis om sivilstand og bo-situasjon. De trenger dette til fødselsmeldingen for å sikre at barnebidrag og foreldreansvar fanges opp riktig i systemene til NAV og Folkeregisteret."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "2", "tittel": "hvem som regnes som mor", "available": True},
            {"lov": "barnelova", "paragraf": "3", "tittel": "farskap og medmorskap i ekteskap", "available": True},
            {"lov": "barnelova", "paragraf": "4", "tittel": "hvordan erklære farskap som samboer", "available": True},
        ],
    },
    {
        "number": "2",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Den som føder barnet er moren",
        "kategori": "familie",
        "description": "Hvem er juridisk sett mor til et barn? Loven slår fast at kvinnen som føder barnet alltid er mor, og surrogati-avtaler er ikke bindende i Norge.",
        "kort_svar": "Den kvinnen som fysisk føder barnet, blir alltid ansett som barnets mor i lovens forstand. Avtaler om surrogati (at en annen kvinne bærer frem barnet for deg) er ikke gyldige eller bindende i Norge.",
        "paragraftekst": """Som mor til barnet skal reknast den kvinna som har fødd barnet.

Avtale om å føde eit barn for ei anna kvinne er ikkje bindande.""",
        "hva_betyr_html": """<p>Paragrafen er kort, men den er grunnmuren i norsk familierett. Den sier at morskapet alltid knyttes til selve fødselen. Den som gjennomgår svangerskapet og føder barnet, blir registrert som juridisk mor i Folkeregisteret.</p>
<p>Dette gjelder helt uavhengig av hvem sine gener barnet har. Hvis en kvinne blir gravid ved hjelp av eggdonasjon, er det egget til en annen kvinne som brukes. Likevel er det kvinnen som bærer frem barnet og føder det, som blir barnets eneste rettmessige mor. Eggdonoren har ingen juridiske rettigheter eller plikter overfor barnet.</p>
<p>Det andre leddet forbyr bindende surrogatiavtaler i Norge. Surrogati betyr at en kvinne går med på å bli gravid og føde et barn med den klare hensikt å gi fra seg barnet til en annen person eller et par etter fødselen. I Norge sier loven at en slik avtale er null verdt juridisk. Den kvinnen som føder, kan ombestemme seg og beholde barnet, fordi loven anser henne som mor uansett hva papirene sier. De som "bestilte" barnet kan ikke bruke domstolene for å tvinge gjennom avtalen.</p>
<h3>Hva betyr dette for nordmenn som bruker surrogat i utlandet?</h3>
<p>Mange nordmenn reiser til land der surrogati er lovlig, for eksempel USA eller Colombia, for å få barn. Når de kommer tilbake til Norge med barnet, møter de det norske lovverket i døra.</p>
<p>Selv om det utenlandske sykehuset kanskje har skrevet de norske foreldrene på fødselsattesten der nede, ser norske myndigheter annerledes på det. Skatteetaten vil kreve å vite hvem som faktisk <em>fødte</em> barnet, og vil registrere den utenlandske surrogaten som barnets mor i Norge. For at den norske kvinnen (eller faren) som bestilte barnet skal bli juridisk mor i Norge, må hun gå gjennom en formell stebarnsadopsjon etter at barnet er kommet til Norge.</p>
<h3>Hva skjer hvis du gjør feil?</h3>
<p>Hvis du forsøker å omgå regelverket ved å late som om du selv har født barnet som du egentlig hentet via surrogat, gjør du deg skyldig i dokumentfalsk. Konsekvensen er straffeforfølgelse. Hvis du ikke formaliserer forholdet via adopsjon når du kommer hjem med et surrogatbarn, vil du stå uten juridiske rettigheter til barnet. Det betyr at du for eksempel ikke kan ta medisinske avgjørelser for barnet eller få lovpålagt arv.</p>""",
        "eksempler": [{"navn": "Kari", "tekst": "Kari kan ikke få egne barn, så hun og ektemannen reiser til utlandet og inngår en surrogatiavtale med en lokal kvinne, Maria. Maria blir gravid og føder barnet. Ektemannens sperm er brukt, så han oppretter farskap og tar med barnet hjem. Men Kari er ikke barnets mor ifølge norsk lov, selv om hennes befruktede egg ble brukt. I norske registre står surrogaten Maria oppført som mor. Kari må søke Bufdir om å få stebarnsadoptere barnet for å bli barnets juridiske mor."}],
        "vanlige_feil": ["Tro at DNA og genetikk bestemmer hvem som er mor i Norge (dette gjelder far, men ikke mor).", "Tro at en utenlandsk dom eller kontrakt om surrogati automatisk godtas av norske myndigheter.", "Legge til grunn at partneren blir juridisk forelder fra dag én etter surrogati i utlandet."],
        "hva_bor_du_html": """<p>Hvis du får barn ved hjelp av eggdonasjon på en godkjent klinikk, trenger du ikke gjøre noe. Du regnes som mor i det du føder.</p>
<p>Hvis du benytter surrogati i utlandet: Forbered deg på papirmøllen. Det er den genetiske faren som må reise ned, fastsette farskapet etter de utenlandske og norske reglene, få barnet til Norge, og deretter må den andre partneren søke om stebarnsadopsjon. Kontakt en norsk advokat med erfaring på surrogati i god tid før fødselen for å unngå problemer ved grensen.</p>""",
        "dumme_sporsmal": [
            {"q": "Kan vi skrive en kontrakt i Norge hvor min venninne lover å bære frem barnet for meg?", "a": "Dere kan skrive den, men den er ugyldig. Hvis venninnen din føder barnet, er hun juridisk mor. Hun har rett til å beholde barnet, og dere kan ikke kreve barnet utlevert basert på kontrakten."},
            {"q": "Hvis jeg bruker eggdonasjon, har eggdonoren rett på samvær med barnet senere?", "a": "Nei, overhodet ikke. Loven beskytter kvinnen som føder barnet. Eggdonoren har ingen juridiske bånd til barnet og regnes aldri som mor."},
            {"q": "Kan barnet ha to mødre og ingen far fra fødselen?", "a": "Ja, men det styres av reglene om *medmorskap* (se § 4 a), ikke denne paragrafen. Det er fortsatt kvinnen som føder som er \"mor\", mens partneren hennes blir \"medmor\"."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "3", "tittel": "farskap og medmorskap i ekteskap", "available": True},
            {"lov": "barnelova", "paragraf": "5", "tittel": "statens ansvar for å fastsette foreldreskap", "available": True},
        ],
    },
    {
        "number": "3",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Ektemann blir far automatisk",
        "kategori": "familie",
        "description": "Hvem regnes som far hvis mor er gift? Er du gift når barnet blir født, regnes mannen din automatisk som far. Dette kalles pater est-regelen.",
        "kort_svar": "Er du som mor gift med en mann når barnet fødes, regnes han automatisk som barnets far. Er du gift med en kvinne, kan hun automatisk bli medmor, men bare hvis barnet er unnfanget i godkjent helsestell (klinikk) og kona di har samtykket skriftlig i forkant.",
        "paragraftekst": """Som far til barnet skal reknast den mannen som mora er gift med ved fødselen.

Som medmor til barnet skal reknast den kvinna som mora er gift med ved fødselen når barnet er avla ved assistert befruktning innafor godkjent helsestell og med kvinna sitt samtykke til befruktninga. Ved assistert befruktning innafor godkjent helsestell i utlandet må identiteten til sædgiver vere kjent.

Var ektefellene ved fødselen separerte ved løyve eller dom, gjeld ikkje første og andre stykke.

Er mora enkje, skal ektefellen reknast som far eller medmor dersom mora kan ha blitt med barn før ektefellen døydde.""",
        "hva_betyr_html": """<p>Paragrafen regulerer det juristene kaller "pater est-regelen". Den skaper en praktisk snarvei for ektepar: Føder du et barn mens du er gift, trenger dere ikke fylle ut skjemaer eller ta farskapstester. Staten legger automatisk til grunn at ektemannen din er faren til barnet, og han føres rett inn i Folkeregisteret som far fra dag én.</p>
<p>Dette gjelder i utgangspunktet også for lesbiske ektepar, men med et viktig forbehold. For at konen din automatisk skal få tittelen "medmor", holder det ikke bare å være gift. Dere må kunne dokumentere at barnet er unnfanget ved hjelp av assistert befruktning (prøverør/inseminasjon) på en lovlig klinikk. Kona din må ha gitt skriftlig forhåndssamtykke til selve behandlingen. Gjør dere det på en klinikk i utlandet, er det også et krav at sæddonoren har åpen identitet (barnet skal ha rett til å vite hvem han er når det fyller 18 år). Lager dere barnet ved "hjemme-inseminasjon", slår ikke denne automatikken inn.</p>
<p>Er ekteparet separert før barnet blir født (ved gyldig bevilling fra Statsforvalteren eller dom), slutter automatikken å gjelde. Da må faren anerkjenne farskapet på samme måte som samboere må gjøre.</p>
<p>Hvis ektemannen eller ektefellen dør under svangerskapet, regnes den avdøde fremdeles som far eller medmor til barnet. Loven sier at enken får skrevet inn ektefellen som barnets andre forelder.</p>
<h3>Hva skjer hvis ektemannen ikke er den biologiske faren?</h3>
<p>Siden regelen er helt automatisk, spør ikke staten om hvem som <em>faktisk</em> har gjort deg gravid. Hvis du som gift kvinne har hatt et forhold til en annen mann og blir gravid, vil din ektemann likevel bli registrert som faren på papiret når barnet blir født.</p>
<p>For å rette opp i dette, må dere endre farskapet. Den egentlige faren kan da erklære farskap (med bekreftelse fra ektemannen og deg), eller noen av dere må kreve en DNA-test for å tvinge gjennom endringen i rettssystemet eller via NAV. Helt til papirarbeidet er ferdig behandlet, er ektemannen juridisk og økonomisk ansvarlig for barnet.</p>""",
        "eksempler": [{"navn": "Håkon", "tekst": "Håkon er gift med Mette. De har levd adskilt i åtte måneder fordi de krangler mye, men de har ikke søkt om formell separasjon hos Statsforvalteren. Mette har fått seg en ny kjæreste og blir gravid med ham. Siden Håkon og Mette formelt sett fremdeles er gift når barnet fødes, blir Håkon automatisk oppført som far i Folkeregisteret og han får krav om barnebidrag. For å slippe ut av dette, må Håkon få rettet farskapet."}],
        "vanlige_feil": ["Samboere tror denne regelen gjelder for dem også (samboere må alltid erklære foreldreskap skriftlig).", "Man flytter fra hverandre (samlivsbrudd) og tror farskapet ikke går automatisk på eksen. Ligger det ikke en formell separasjon i bunnen, er han far.", "Lesbiske ektepar tror hjemmeinseminasjon gir rett til automatisk medmorskap."],
        "hva_bor_du_html": """<p>Lever du i et normalt ekteskap der mannen din er far til barnet? Du trenger ikke gjøre noen ting. Alt skjer automatisk.</p>
<p>Er du gift med en kvinne og planlegger barn? Sørg for at dere benytter en godkjent klinikk (enten i Norge eller i utlandet med åpen donor) og bevarer kopi av samtykket dere signerte i forkant. Da går det glatt med Folkeregisteret.</p>
<p>Er du gift, men barnet tilhører noen andre? Gjør den egentlige faren klar til å erklære farskapet skriftlig før eller under fødselen, og sørg for at ektemannen din godkjenner det skriftlig, slik at NAV kan fikse papirene med én gang.</p>""",
        "dumme_sporsmal": [
            {"q": "Jeg og kona giftet oss to uker før termin. Gjelder regelen da?", "a": "Ja. Loven bryr seg ikke om når dere giftet dere, så lenge ekteskapet er inngått lovlig før den dagen barnet blir født."},
            {"q": "Hva om vi er registrert som separert tre dager før barnet fødes?", "a": "Da gjelder ikke regelen lenger. Er separasjonsbevillingen datert før fødselsdatoen, må faren erklære farskapet aktivt med signatur (BankID)."},
            {"q": "Kan sykehuset holde tilbake at ektemannen blir skrevet som far, hvis jeg forklarer situasjonen?", "a": "Nei, verken leger, sykehus eller Folkeregisteret har lov til å gjøre unntak. Er du gift, blir mannen far på papiret. Dere må selv rydde opp i den juridiske feilen via NAV i ettertid."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "4", "tittel": "hvordan ugifte foreldre erklærer farskap", "available": True},
            {"lov": "barnelova", "paragraf": "7", "tittel": "hvordan bytte ut farskapet fra én mann til en annen", "available": True},
        ],
    },
    {
        "number": "4",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Erklæring av farskap for ugifte",
        "kategori": "familie",
        "description": "Samboere og ugifte får ikke farskap automatisk. Her lærer du hvordan faren formelt erklærer farskap for å bli juridisk far, vanligvis med BankID.",
        "kort_svar": "Er mor og far ikke gift, får ikke mannen automatisk farskap, selv om dere bor sammen. Faren må formelt erklære farskapet sitt. I dag gjøres dette vanligvis digitalt under graviditeten med BankID, eller det kan gjøres fysisk hos jordmor eller NAV.",
        "paragraftekst": """Når farskap ikkje følgjer av reglane i § 3, kan faren erklære farskap under svangerskapet eller etter at barnet er født.

Faren skal erklære farskapen skriftleg, anten digitalt til arbeids- og velferdsetaten eller ved personleg frammøte for
a. jordmor eller lækjar ved svangerskapskontroll eller fødsel,
b. folkeregistermyndigheita,
c. tilskotsfuten, dommaren eller arbeids- og velferdsetaten, eller
d. utsend utanrikstenestetilsett, dersom faren er i utlandet.

Farskap kan òg erklærast ved retur av skjema frå Arbeids- og velferdsdirektoratet, jf. § 11 andre ledd. Arbeids- og velferdsdirektoratet må sende skjema i rekommandert brev eller ved bruk av elektronisk kommunikasjon dersom det er nytta ein betryggande metode for å sikre at skjemaet er mottatt. Erklæringa gjeld berre når ho er gjeven av den som mora har gjeve opp som far, eller når mora skriftleg har godteke erklæringa. Ved digital erklæring må både mor og far identifisere seg elektronisk på ein sikker måte. Den digitale erklæringa er berre gyldig dersom barnet vert født i Noreg.

Er den som vil erklære farskapen under 18 år, må også dei som har foreldreansvaret for han, skrive under på erklæringa.

Er eit barn fødd etter assistert befruktning, kan moras kvinnelege sambuar erklære medmorskap etter reglane i paragrafen her. Den assisterte befruktninga må ha skjedd innafor godkjent helsestell, og moras kvinnelege sambuar må ha gjeve samtykke til befruktninga. Berre myndige personar kan gi slikt samtykke. Regelen i § 3 andre ledd andre punktum gjeld tilsvarande.

Er det naudsynt for å fastslå farskapen til eit barn født i utlandet, kan myndigheita be om ei eigna prøve til DNA-analyse for barnet og for han som vil erklære seg som far, dersom
a. barnet, mora eller han som vil erklære seg som far, ikkje kan godtgjere identiteten sin, eller
b. det er grunn til å tru at det for å få norsk statsborgarskap til barnet er gitt urette opplysningar om kven som er far.
Det er òg eit vilkår at opplysningane i saka elles ikkje gir grunnlag for med rimeleg sikkerheit å fastslå farskapen. Dersom DNA-analyse godtgjer at mannen ikkje kan vere far til barnet, kan han ikkje erklære farskap. Det same gjeld om han avslår ei oppmoding om DNA-analyse.

Departementet kan ved forskrift gje utfyllande reglar om gjennomføring av reglane i femte ledd.""",
        "hva_betyr_html": """<p>Paragrafen gir oppskriften på hvordan ugifte menn blir juridiske fedre. Mens ekteskap gir mannen farskap helt automatisk (se § 3), må samboere ta affære. Du kan signere papirene allerede mens barnet er i magen. Lovens hovedregel er at det må gjøres skriftlig, og i praksis krever det at mor godkjenner det mannen gjør.</p>
<p>Det enkleste er å logge inn på Helsenorge / NAV med BankID. Mor fyller inn litt informasjon og velger faren, og deretter logger faren inn for å signere erklæringen digitalt. Begge to godkjenner hverandre. Da ligger farskapet klart til den dagen barnet blir født (så sant fødselen skjer på et norsk sykehus).</p>
<p>Vil dere ikke bruke BankID, kan dere fylle ut papirskjema. Da må faren møte opp personlig og vise legitimasjon for å skrive under. Det kan han gjøre på svangerskapskontrollen hos jordmor/lege, på sykehuset etter fødselen, eller på et NAV-kontor eller hos Skatteetaten.</p>
<p>Er far under 18 år? Da stoler ikke loven på at han er gammel nok til å forplikte seg alene, og foreldrene hans må signere ved siden av ham.</p>
<p>Er foreldrene to kvinner som er samboere (ikke gift), brukes nøyaktig samme prosess for å erklære medmorskap. Det krever at paret har brukt en godkjent fertilitetsklinikk og at medmoren har samtykket på forhånd.</p>
<p>Det siste leddet i paragrafen er en sikringsregel for tilfeller der et barn blir født i utlandet, men far og mor hevder farskap for å skaffe barnet norsk statsborgarskap. Hvis norske myndigheter (UDI eller politiet) tviler på identiteten til noen av partene, eller mistenker at farskapet er fabrikkert for å snike seg til opphold i Norge, kan de kreve DNA-test. Nekter faren å ta DNA-testen, eller viser testen at han ikke er faren, godtas ikke erklæringen.</p>
<h3>Hva skjer hvis du gjør feil?</h3>
<p>Hvis dere glemmer å erklære farskapet før fødselen, får barnet et fødselsnummer der far står oppført som ukjent. Mor vil da motta brev fra NAV som spør om hvem som er faren, og dere må ordne papirene i ettertid. Inntil erklæringen er godkjent, har far null rettigheter til barnet og ingen rettigheter ved samlivsbrudd, sykdom eller død. Dere får heller ikke delt foreldreansvar.</p>""",
        "eksempler": [{"navn": "Jonas og Sofie", "tekst": "Jonas og Sofie har vært kjærester i fire år og bor sammen. De er ikke gift. Sofie er gravid i uke 28. Hun logger inn på Helsenorge.no, går til \"Farskap\" og fyller inn at Jonas er far. Noen sekunder senere får Jonas en SMS. Han logger inn med sin BankID, leser erklæringen og trykker signer. Det var alt. Når barnet fødes to måneder senere, blir Jonas automatisk oppført som far i Folkeregisteret fordi erklæringen allerede lå klar."}],
        "vanlige_feil": ["Samboere tror farskapet skjer automatisk fordi de har samme folkeregistrerte adresse.", "Mor erklærer farskapet på nett, men glemmer å be far logge inn for å signere før fødselen.", "Tror det koster penger å erklære farskap (det er gratis).", "Tror DNA-test er obligatorisk (det kreves bare unntaksvis hvis noe skurrer med barn født i utlandet)."],
        "hva_bor_du_html": "<p>1. <strong>Gjør det i svangerskapet</strong> — Bruk Helsenorge.no eller NAVs nettsider i uke 22 eller senere. 2. <strong>Begge må ha BankID</strong> — Mor starter prosessen, far fullfører den. 3. <strong>Møt opp hvis BankID mangler</strong> — Be jordmor ta frem skjemaet på neste kontroll, og sørg for at faren er med for å signere. Husk legitimasjon (pass eller førerkort).</p>",
        "dumme_sporsmal": [
            {"q": "Hva skjer hvis jeg erklærer meg som far, men barnet viser seg å være en annens?", "a": "Hvis du skriver under, påtar du deg ansvaret. Hvis du senere får vite at du ikke er faren, må du kreve endring via domstolene eller NAV (se § 7), noe som ofte krever DNA-tester og papirarbeid. Er du usikker, la være å signere og krev heller en farskapstest etter at barnet er født."},
            {"q": "Trenger jeg mors tillatelse til å signere farskap?", "a": "Ja. Loven er bygget slik at en erklæring bare er gyldig hvis den mannen oppgir, faktisk er godkjent av mor (\"når mora skriftleg har godteke erklæringa\"). Er dere uenige, må du kontakte NAV slik at de kan kreve DNA-test for å få farskapet ditt registrert."},
            {"q": "Må vi være samboere for å fylle ut dette?", "a": "Nei. Du kan erklære farskap for ethvert barn, selv om dere aldri har bodd sammen, eller om det var et engangstilfelle. Så lenge mor og far er enige om farskapet, bruker dere samme fremgangsmåte."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "3", "tittel": "ekteskapsregelen (som sier at gifte ikke trenger dette)", "available": True},
            {"lov": "barnelova", "paragraf": "5", "tittel": "hva som skjer hvis ingen erklærer seg som far", "available": True},
        ],
    },
    {
        "number": "4a",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvem kan bli medmor for barnet?",
        "kategori": "familie",
        "description": "Slik regnes partneren som medmor til et barn unnfanget ved assistert befruktning.",
        "kort_svar": "En kvinnelig ektefelle eller samboer kan bli barnets juridiske \"medmor\" hvis paret har fått barn ved hjelp av assistert befruktning (inseminasjon/prøverør) i godkjent helsestell. En medmor har nøyaktig samme rettigheter og plikter som en far.",
        "paragraftekst": """Som medmor til barnet skal reknast moras kvinnelege ektefelle eller sambuar, dersom medmorskapen følgjer av ekteskap, erklæring eller dom.

Eit barn kan ikkje ha både ein far og ei medmor.

Reglar i lov eller forskrift som gjeld om eller for ein far, gjeld på same vis om eller for ei medmor. Reglane om etablering og endring av farskap i §§ 6 til 9 og kapitla 3 og 4 gjeld så langt dei høver for fastsetjing og endring av medmorskap.

Departementet kan ved forskrift gje utfyllande reglar om fastsetjing av medmorskap etter §§ 3 og 4 i denne lova.""",
        "hva_betyr_html": """<p>Da ekteskapsloven ble kjønnsnøytral i 2009, ble også barneloven oppdatert for å likestille lesbiske par med heterofile par. Tittelen "medmor" er kort fortalt den juridiske erstatningen for tittelen "far".</p>
<p>Dersom et kvinnepar får barn sammen ved å benytte en lovlig fertilitetsklinikk (assistert befruktning), kan partneren til kvinnen som føder, bli juridisk medmor. Er de gift, skjer dette automatisk akkurat som for en ektemann (se § 3). Er de samboere, må medmoren signere en erklæring på samme måte som en mannlig samboer (se § 4).</p>
<p>I tredje ledd sier loven det i klartekst: Alt som gjelder for en far i lovverket, gjelder automatisk for en medmor. Det betyr at hun må betale barnebidrag, har rett på samvær, får foreldreansvar, og barnet arver henne. Den eneste forskjellen mellom far og medmor er navnet loven bruker på rollen.</p>
<p>Det andre leddet slår fast et viktig prinsipp i Norge: Et barn kan ha maksimalt to juridiske foreldre. Barnet kan ha mor og far, eller to mødre. Det kan aldri ha tre foreldre, og kan dermed ikke ha både en juridisk far og en juridisk medmor. Selv om sæddonoren kanskje kjenner familien (ved kjent donor), må han gi avkall på foreldreretten for at medmoren skal kunne stå i papirene.</p>
<h3>Hva med hjemmeinseminasjon?</h3>
<p>Mange to-kvinne-par forsøker å lage barn hjemme ved at en mannlig venn gir dem sæd. Dette kalles hjemmeinseminasjon, og foregår utenfor "godkjent helsestell". I slike tilfeller faller muligheten for medmorskap helt bort.</p>
<p>Siden loven krever at unnfangelsen skjer via en offisiell klinikk, vil en kvinne som blir gravid hjemme, føde et barn der staten vil peke på donoren som far. For at partneren hennes skal bli barnets andre forelder, må paret gå den tunge veien om stebarnsadopsjon etter at barnet er født, og mannen må da skrive fra seg sine rettigheter.</p>""",
        "eksempler": [{"navn": "Anne og Eva", "tekst": "Anne og Eva er samboere og reiser til en klinikk i Danmark for å bli gravide med en åpen donor. Anne blir gravid. Før fødselen logger Eva inn på Helsenorge for å erklære foreldreskapet, akkurat som en mannlig samboer ville gjort. De legger ved dokumentasjonen fra den danske klinikken om at det ble brukt en åpen donor. Når barnet blir født, blir Anne registrert som mor og Eva registrert som medmor, med delt foreldreansvar fra første dag. Donoren i Danmark har ingenting med barnet å gjøre juridisk."}],
        "vanlige_feil": ["Tro at partneren blir medmor automatisk selv om hun ikke har signert et forhåndssamtykke på klinikken.", "Foreta inseminasjon hjemme, og så kreve tittel som medmor i Folkeregisteret.", "Benytte klinikk i utlandet med ukjent donor (anonym donor er ikke tillatt etter norsk lov og gir avslag på medmorskap)."],
        "hva_bor_du_html": "<p>1. <strong>Behold papirene fra klinikken</strong> — Skatteetaten vil kreve å se dokumentasjon på behandlingen. Særlig samtykket om assistert befruktning som dere skrev under på før behandlingen. 2. <strong>Krev åpen donor i utlandet</strong> — Hvis dere reiser utenlands for behandling, må dere forsikre dere om at klinikken registrerer donoren som \"åpen\", slik at barnet kan få vite identiteten ved fylte 18 år. Dette er et absolutt krav i Norge. 3. <strong>Meld ifra tidlig</strong> — Erklær medmorskapet digitalt på Helsenorge før fødselen for å sikre at begges rettigheter gjelder fra sykehuset.</p>",
        "dumme_sporsmal": [
            {"q": "Kan vi avtale med en venn som donerer sæd at han er far mens partneren min er medmor?", "a": "Nei. Paragrafen er veldig tydelig: \"Eit barn kan ikkje ha både ein far og ei medmor\". Dere må velge. Enten blir vennen juridisk far, ellers blir partneren din medmor. De kan ikke dele på det."},
            {"q": "Hvis min kone bærer frem barnet med mitt egg, blir jeg medmor da?", "a": "Ja. Fødselen gjør din kone til mor (etter § 2), mens din rolle utelukkende knyttes til ekteskapet og klinikk-kravene. Din genetiske knytning til egget gir deg ingen foreldrerett i seg selv; du blir medmor fordi dere er gift og oppfyller lovens krav til assistert befruktning."},
            {"q": "Hvorfor kalles det medmor i stedet for bare mor?", "a": "For å unngå forvirring i byråkratiet, og fordi loven lenge har reservert \"mor\" for den kvinnen som føder barnet. En medmor er den juridiske forelderen som ikke fødte barnet. I hverdagen er dere selvfølgelig to mammaer."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "2", "tittel": "definerer hvem som er mor", "available": True},
            {"lov": "barnelova", "paragraf": "3", "tittel": "regelen for gifte kvinner", "available": True},
            {"lov": "barnelova", "paragraf": "4", "tittel": "regelen for ugifte / samboere", "available": True},
        ],
    },
    {
        "number": "5",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "NAVs ansvar når far eller medmor mangler",
        "kategori": "familie",
        "description": "Hva skjer når en kvinne føder et barn uten at noen er oppført som far? Da slår loven inn og gir staten, ved NAV, plikt til å jakte på hvem faren er.",
        "kort_svar": "Barn har rett til å kjenne foreldrene sine. Fødes det et barn uten at en far eller medmor er registrert, har det offentlige (NAV) en lovpålagt plikt til å ta over saken og oppspore hvem faren er.",
        "paragraftekst": """Dersom barnet korkje har far eller medmor i samsvar med reglane i §§ 3 og 4, skal det offentlege ta seg av å få fastsett kven som er faren eller medmora, jf. kapittel 3 og 4.

Dersom ein utanlandsk farskap eller medmorskap ikkje vert lagt til grunn etter § 85, har det offentlege ansvar etter første stykket.

Det offentlege skal klargjere kven som er mor til barnet når dette ikkje er kjent.

Departementet kan ved forskrift gje utfyllande reglar om gjennomføring av reglane i paragrafen her.""",
        "hva_betyr_html": """<p>Paragrafen legger ansvaret over på det offentlige når et barn står uten to juridiske foreldre. Dette er for å verne barnet. Loven sier i praksis at farløshet er et unntak som staten ikke godtar uten videre.</p>
<p>Hvis sykehuset sender fødselsmelding og det står "ukjent" i feltet for far, vil maskineriet starte. Saken sendes fra Skatteetaten til NAV. NAV har da rett og plikt til å innkalle moren for å spørre hvem hun har hatt sex med i perioden hun ble gravid, og de kan ta kontakt med aktuelle menn.</p>
<p>Dette ansvaret inntrer også dersom en utenlandsk farskapserklæring (for eksempel fra ferieopphold eller flytting) ikke er godkjent i Norge. Da behandler Norge saken som om barnet er farløst, og NAV må finne og formalisere faren etter norske regler.</p>
<p>Det tredje leddet sier at staten også må finne moren hvis det er ukjent. Dette gjelder nesten utelukkende i de sjeldne tilfellene der et spedbarn blir etterlatt, eller "funnet" anonymt (hittebarn).</p>
<h3>Hva skjer hvis du gjør feil?</h3>
<p>Hvis en mor aktivt motarbeider NAVs undersøkelser (for eksempel ved å lyve om hvem som er far, eller nekte å stille til avhør), har ikke staten makt til å tvinge henne til å snakke. Loven gir ikke rom for å sette mor i fengsel for taushet. Men vedkommende saboterer barnets lovfestede rett til å kjenne opphavet sitt, og barnet taper all rett til barnebidrag, arv og kjennskap til farsslekten.</p>
<p>For mannen betyr det at NAV plutselig kan banke på døren måneder eller år etter hendelsen, ofte med krav om å avgi DNA-prøve. Nekter mannen, kan NAV ta saken til retten.</p>""",
        "eksempler": [{"navn": "Ida", "tekst": "Ida er singel og blir gravid etter en fuktig natt på byen. Hun vet fornavnet på faren, men orker ikke å ha noe med ham å gjøre, og nekter å fylle ut navnet hans på sykehuset. To uker etter fødselen får hun et brev fra NAV som ber henne møte til en samtale. NAV forklarer at barnet har rett til en far og at de trenger alle opplysninger hun har for å oppspore ham, slik at han kan ta DNA-test og eventuelt betale barnebidrag. Ida må samarbeide."}],
        "vanlige_feil": ["Kvinner tror de kan velge å krysse av for \"ukjent far\" for å være alene om barnet i fred.", "Menn tror de slipper unna barnebidrag fordi mor ikke ville ha navnet deres på papiret fra start.", "Tro at NAV gir opp hvis man sier \"vet ikke\"."],
        "hva_bor_du_html": "<p>Dersom du vet hvem faren er, sparer det begge parter for tid og frustrasjon at dere håndterer erklæringen før fødselen (se § 4). Hvis du ikke ønsker kontakt med faren på grunn av trusler, vold eller frykt, forklar dette tydelig for NAV når de kontakter deg. De håndterer slike saker diskret. De plikter fremdeles å finne faren, men kommunikasjonen vil gå gjennom NAV, ikke direkte mellom dere.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg ikke bare droppe farskap så lenge jeg er i stand til å forsørge barnet selv?", "a": "Nei. Staten godtar ikke argumentet om økonomi. Å ha en far handler om mer enn penger; det handler om medisinsk historie, arverettigheter og barnets identitet. NAV vil prøve å oppspore ham uansett hva du tjener."},
            {"q": "Hva gjør NAV hvis de finner flere menn som kan være faren?", "a": "Da vil NAV gi pålegg til samtlige menn om å avgi en spyttprøve til DNA-analyse. DNA-testing har gjort slike saker svært enkle å løse."},
            {"q": "Hva om faren bor i utlandet og nekter å svare NAV?", "a": "NAV vil bruke kanaler via utenriksstasjoner og internasjonale avtaler. Er han helt umulig å oppdrive, eller regimet i landet han befinner seg i nekter å samarbeide, kan saken til slutt bli henlagt, og barnet forblir uten formell far."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "11", "tittel": "mer om hvordan NAV avkrever DNA-test og forklaringer", "available": True},
            {"lov": "barnelova", "paragraf": "4", "tittel": "den normale måten å ordne farskap på for ugifte", "available": True},
            {"lov": "barnelova", "paragraf": "85", "tittel": "om godkjenning av farskap fastsatt i utlandet", "available": True},
        ],
    },
    {
        "number": "6",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvem kan reise sak for å endre farskap?",
        "kategori": "familie",
        "description": "Lurer du på om riktig mann er oppført som far? Barnet, mor, den registrerte faren og menn som mener de er faren, kan alltid reise sak for domstolen.",
        "kort_svar": "Barnet, moren, mannen som er oppført som far, eller en annen mann som mener han er den biologiske faren, kan når som helst ta saken til domstolen for å endre farskapet. Det finnes ingen tidsfrist for å reise en slik sak.",
        "paragraftekst": "Barnet, kvar av foreldra og tredjemann som meiner han er far til eit barn som allereie har ein far, kan alltid reise sak for domstolane om farskap etter ekteskap eller erklæring. Er barnet mindreårig, vert saka reist av oppnemnd verje. Er barnet fylt 15 år, kan verja ikkje reise sak utan samtykke frå barnet. Når særlege grunnar taler for det, kan Arbeids- og velferdsdirektoratet reise saka.",
        "hva_betyr_html": """<p>Paragrafen gir en sikkerhetsventil hvis feil mann er registrert som far i Folkeregisteret. Hvem som helst av de involverte partene kan ta saken til domstolen (tingretten) for å kreve en DNA-test og få fastslått den biologiske sannheten. Dette gjelder uansett om farskapet opprinnelig ble registrert fordi paret var gift, eller fordi en samboer skrev under på et skjema.</p>
<p>Loven sier at du "alltid" kan reise sak. Tidligere fantes det tidsfrister, men de er fjernet. Du kan reise sak om barnet er 2 år eller 40 år gammelt.</p>
<p>Hvis barnet er under 18 år (mindreårig), er det vergen (vanligvis mor, eller en oppnevnt verge hvis mor har interessekonflikt) som formelt reiser saken på vegne av barnet. Men loven gir barnet en egen stemme: Har barnet fylt 15 år, kan ikke vergen dra i gang en rettssak om farskap hvis barnet sier nei. En 15-åring har altså vetorett.</p>
<p>I helt spesielle tilfeller kan NAV (Arbeids- og velferdsdirektoratet) ta ut et søksmål på eget initiativ, for eksempel hvis de har sterke mistanker om trygdesvindel eller at det er oppgitt falsk far for å få oppholdstillatelse.</p>
<h3>Kan en helt fremmed mann kreve DNA-test?</h3>
<p>Ja, hvis han mener at han er faren til barnet. En "tredjemann" har en lovfestet rett til å reise sak for å kreve farskapet flyttet over til seg selv. Dette gjelder selv om mor og den nåværende juridiske faren er lykkelig gift og nekter for at noen andre kan være faren.</p>
<p>Gjør han alvor av dette, må han sende en stevning til tingretten. Dommeren vil da normalt pålegge alle parter å ta en DNA-test for å avklare spørsmålet én gang for alle. Viser testen at tredjemannen er faren, blir den gamle faren slettet, og den nye faren får alle rettigheter og plikter.</p>""",
        "eksempler": [{"navn": "Marius", "tekst": "Marius hadde en kort affære med Sara for ti år siden. Kort tid etter ble hun sammen med Peter, og da datteren Lise ble født, skrev Peter under på farskapet. Marius har alltid mistenkt at Lise egentlig er hans datter. Sara nekter å snakke med ham om det. Marius kontakter en advokat og reiser sak for tingretten etter § 6. Retten krever DNA-prøver. Testen viser at Marius er den biologiske faren. Tingretten avsier dom som endrer farskapet til Marius, selv om Sara og Peter var imot det."}],
        "vanlige_feil": ["Tro at det er for sent fordi barnet har blitt voksent.", "Tro at en \"tredjemann\" ikke kan blande seg i en etablert familie.", "Glemme at et barn over 15 år må samtykke før vergen kan kreve rettssak på barnets vegne."],
        "hva_bor_du_html": """<p>Mistenker du at du betaler barnebidrag for et barn som ikke er ditt, eller at du er far til et barn som har en annen registrert far?</p>
<p>Sjekk først om dere kan løse dette frivillig via NAV og en frivillig DNA-test (se § 7). Hvis mor eller den andre mannen nekter, er domstolen eneste utvei. Du må da ta kontakt med en advokat for å utforme en formell stevning til tingretten der barnet bor. Tingretten ordner det praktiske rundt selve DNA-testen når saken er i gang.</p>""",
        "dumme_sporsmal": [
            {"q": "Koster det penger å reise en slik sak?", "a": "Ja, å reise en sak for tingretten koster et rettsgebyr, og du må vanligvis betale din egen advokat. I farskapssaker har du imidlertid ofte rett til fri rettshjelp, avhengig av inntekten din, og selve DNA-testen betales av staten."},
            {"q": "Kan mor nekte å ta DNA-test av barnet når saken er i retten?", "a": "Nei. Hvis dommeren beslutter at det skal tas DNA-test, er det en bindende ordre. Nekter mor å møte opp med barnet hos legen, kan dommeren be om at politiet henter dem (se § 24)."},
            {"q": "Får mannen tilbakebetalt barnebidrag hvis det viser seg at han ikke var faren likevel?", "a": "Ja, som regel kan mannen kreve tilbakebetalt det han har betalt i barnebidrag, men han krever pengene tilbake fra NAV (folketrygden), ikke fra mor eller barnet (se § 80)."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "7", "tittel": "frivillig endring uten domstol", "available": True},
            {"lov": "barnelova", "paragraf": "9", "tittel": "vilkårene for å dømme en mann som far", "available": True},
            {"lov": "barnelova", "paragraf": "24", "tittel": "domstolens makt til å tvinge frem DNA-prøve", "available": True},
        ],
    },
    {
        "number": "6a",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Barnets rett til å vite hvem biologisk far er",
        "kategori": "familie",
        "description": "Har du fylt 18 år og lurer på hvem din egentlige far er? Du har rett til å kreve DNA-test uten at det endrer ditt juridiske farskap på papiret.",
        "kort_svar": "Når du fyller 18 år, har du rett til å få vite hvem din biologiske far er. Du kan kreve at NAV pålegger den du tror er faren, å ta en DNA-test. Dette endrer ikke noe på hvem som er faren din juridisk, det er kun for at du skal få vite sannheten.",
        "paragraftekst": """Barnet har frå det fyller 18 år rett til å skaffe seg kunnskap om kven som er den biologiske faren, jf. andre stykket, utan at dette endrar farskapen.

Barnet kan krevje at Arbeids- og velferdsdirektoratet gjev pålegg om å levere eigna prøve til DNA-analyse etter § 11 første stykket, og har rett til å få vite resultatet av analysene. Dersom nokon ikkje rettar seg etter pålegget, kan retten gjere vedtak etter § 24 tredje stykket.

Departementet kan ved forskrift gje utfyllande reglar om gjennomføring av reglane i paragrafen her.""",
        "hva_betyr_html": """<p>Mange vokser opp med en far de elsker, men finner kanskje senere i livet ut at en annen mann kan være deres biologiske opphav. Før denne regelen kom, måtte du gå til rettssak og slette den mannen som hadde oppdratt deg som juridisk far, hvis du bare ønsket å tvinge frem en DNA-test av den andre mannen. Det var en brutal prosess.</p>
<p>Paragraf 6 a gir deg, fra den dagen du fyller 18 år, rett til å få vite sannheten <em>uten</em> at papirene i Folkeregisteret endres. Den juridiske faren din forblir faren din. Arveretten forblir hos ham. Regelen handler utelukkende om din rett til å kjenne ditt eget biologiske opphav og din medisinske historie.</p>
<p>Hvis du vet om en mann som kan være din biologiske far, kan du be NAV (Arbeids- og velferdsdirektoratet) om hjelp. NAV sender da et bindende pålegg til denne mannen om at han må avgi en DNA-prøve. Du har rett til å få utlevert resultatet.</p>
<p>Nekter mannen å ta testen frivillig etter pålegget fra NAV, stopper ikke saken der. Saken kan sendes til domstolen, og dommeren kan i ytterste konsekvens be politiet om å hente ham slik at legen kan sikre et DNA-strykk fra munnhulen hans.</p>""",
        "eksempler": [{"navn": "Jonas", "tekst": "Jonas er 19 år. Han har vokst opp med Per som far, og de har et fantastisk forhold. Jonas' onkel forteller i en konfirmasjon at en mann som heter Lars mest sannsynlig er Jonas' biologiske far. Jonas ønsker ikke å miste Per som juridisk far, men han vil vite sannheten. Han sender et krav til NAV. NAV pålegger Lars å avgi DNA. Resultatet viser at Lars er den biologiske faren. Jonas får vite resultatet, får fred i sjelen, og livet går videre. Per står fremdeles oppført som Jonas' far i Folkeregisteret."}],
        "vanlige_feil": ["Tro at man må gå til rettssak og sparke ut sin gamle far for å få DNA-svar.", "Kreve denne testen før man har fylt 18 år (loven setter en absolutt aldersgrense).", "Den mulige biologiske faren tror han har rett til å nekte. Det har han ikke."],
        "hva_bor_du_html": "<p>Er du over 18 år og vil vite om en spesifikk mann er din biologiske far? Send en skriftlig henvendelse til NAV og henvis til barneloven § 6 a. Forklar kort hvorfor du tror denne mannen kan være faren din. Du må selv være villig til å ta en DNA-prøve (spyttprøve) slik at NAV har noe å sammenligne mannens prøve med.</p>",
        "dumme_sporsmal": [
            {"q": "Får den biologiske faren noen rettigheter til meg hvis testen er positiv?", "a": "Nei, overhodet ikke. Han blir verken juridisk far eller får krav på samvær, og du arver ham ikke. Resultatet er kun et stykke informasjon til deg."},
            {"q": "Må jeg informere den mannen jeg har vokst opp med som far?", "a": "Loven krever ikke at du informerer din juridiske far. Du gjør dette via NAV. Men det kan naturligvis være klokt å snakke med familien din for å unngå at det blir en ubehagelig hemmelighet."},
            {"q": "Kan biologisk far kreve at juridisk farskap endres etter at han har tatt denne testen?", "a": "Ja. Den biologiske faren har en egen selvstendig rett til å reise sak for domstolen om å bli juridisk far, etter § 6. Men hvis du er over 18 år, kan han aldri endre farskapet uten at du uttrykkelig samtykker til det."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "6", "tittel": "full rettssak for å endre juridisk farskap", "available": True},
            {"lov": "barnelova", "paragraf": "11", "tittel": "NAVs plikt til å håndtere DNA-tester", "available": True},
            {"lov": "barnelova", "paragraf": "24", "tittel": "politiets makt til å tvinge menn til prøvetaking", "available": True},
        ],
    },
    {
        "number": "7",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Endre farskap når en annen mann erklærer det",
        "kategori": "familie",
        "description": "Har dere funnet ut hvem som egentlig er far? Farskap kan endres frivillig og raskt, så lenge DNA-beviset er klart og alle parter skriver under.",
        "kort_svar": "Farskapet kan flyttes over til riktig mann uten å gå til domstolen, så lenge alle er enige. Det krever at den nye mannen tar en offisiell DNA-test som beviser at han er faren, og at både mor og den mannen som for øyeblikket står som far, godkjenner det skriftlig.",
        "paragraftekst": "Farskap i samsvar med § 3 eller § 4 kan endrast ved at ein annan mann erklærer farskapen i samsvar med § 4, når erklæringa er godteken skriftleg av mora og den som har vore rekna for far. Ei slik erklæring gjeld likevel berre når Arbeids- og velferdsdirektoratet finn at DNA-analyse godtgjer at den andre mannen er far til barnet. Dersom barnet er fylt 18 år, kan farskapen ikkje endrast etter denne paragrafen utan samtykke frå barnet.",
        "hva_betyr_html": """<p>Paragraf 7 er "fredstids-regelen" for å rydde opp i feil farskap. Den brukes når alle parter — mor, mannen som uheldigvis ble registrert som far, og den virkelige biologiske faren — er voksne og enige om å fikse papirene. Slik slipper man en langtekkelig og unødvendig runde i domstolen.</p>
<p>For at Folkeregisteret og NAV skal godta endringen, må fire strenge krav være oppfylt: 1. Den biologiske faren må formelt erklære at han er faren (akkurat som en nybakt samboer gjør). 2. Moren må skrive under på at hun godtar dette. 3. Den nåværende juridiske faren må skrive under på at han godtar å tre til side. 4. DNA-analysen må være gjennomført og offisielt godkjent av NAV. Det holder ikke å vise frem en "hjemmetest" fra et postordrefirma. Testen må være tatt i kontrollerte former.</p>
<p>Det kreves med andre ord 100 % enighet pluss et klinisk bevis. Mangler én av signaturene, nekter NAV å endre saken, og da må dere til tingretten etter § 6.</p>
<p>Hvis barnet har fylt 18 år når dere bestemmer dere for å rydde opp i dette, har barnet det avgjørende ordet. Da kan ikke farskapet endres med mindre barnet selv samtykker til det, uansett hva de voksne vil og uansett hva DNA-testen sier.</p>""",
        "eksempler": [{"navn": "Kari, Lars og Tom", "tekst": "Kari og Lars var gift da lille Emil ble født. Derfor ble Lars automatisk oppført som far, selv om paret var i ferd med å gå fra hverandre og Kari egentlig visste at Tom (hennes nye kjæreste) var faren. Seks måneder senere ønsker alle å ordne opp i papirene. Tom kontakter NAV og tar en offisiell DNA-test som bekrefter at han er far. Tom signerer en erklæring, og både Kari og Lars skriver under på at de godtar den. NAV flytter farskapet fra Lars til Tom i Folkeregisteret, og saken er løst uten advokater eller rettssal."}],
        "vanlige_feil": ["Tro at man kan endre farskap bare ved å levere et skjema der alle er enige (DNA-test er absolutt påkrevd i slike endringssaker for å forhindre trygdesvindel eller kjøp/salg av barn).", "Tro at en \"MyHeritage\" eller lignende hjemmetest er godt nok bevis for NAV.", "At den gamle faren nekter å skrive under fordi han er sint. (Hvis han nekter, er det ikke lenger en § 7-sak, men en rettssak)."],
        "hva_bor_du_html": "<p>Er alle parter enige om at feil mann står som far? 1. Kontakt NAV og si at dere vil gjøre en frivillig endring av farskap etter barneloven § 7. 2. NAV vil instruere dere om hvor den biologiske faren og barnet skal møte opp for å ta en offisiell, godkjent DNA-prøve. 3. Når resultatet foreligger, vil NAV be den nye faren, moren og den gamle faren signere på papirene. Da overføres farskapet.</p>",
        "dumme_sporsmal": [
            {"q": "Hva skjer med barnebidraget den gamle faren har betalt?", "a": "Når farskapet endres, slutter han å være bidragspliktig. Han kan da kreve tilbake det han urettmessig har innbetalt. Loven har egne regler om tilbakebetaling fra folketrygden for menn som feilaktig har blitt krevd for bidrag (se § 80)."},
            {"q": "Må vi i retten i det hele tatt hvis vi bruker denne paragrafen?", "a": "Nei, hele poenget med paragrafen er at NAV gjør papirarbeidet administrativt så lenge DNA-testen er på plass og alle tre er enige. Ingen domstol trengs."},
            {"q": "Hva om den gamle faren er død, kan vi fortsatt bruke denne regelen?", "a": "Nei. Hvis den gamle faren er død, kan han ikke signere på at han godtar endringen. Da må dere ta en formell runde i domstolen for å få opphevet hans farskap før den nye faren kan tre inn."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "6", "tittel": "hvis noen nekter å skrive under, må dere hit", "available": True},
            {"lov": "barnelova", "paragraf": "4", "tittel": "hvordan erklæring av farskap foregår rent praktisk", "available": True},
            {"lov": "barnelova", "paragraf": "80", "tittel": "tilbakebetaling av barnebidrag når farskapet flyttes", "available": True},
        ],
    },
    {
        "number": "8",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Farskap kan ikke endres som en del av andre saker",
        "kategori": "familie",
        "description": "Spørsmålet om hvem som er far, er så viktig at det må avgjøres i en egen sak. Du kan ikke kreve DNA-test som en del av en krangel om arv eller samvær.",
        "kort_svar": "Spørsmålet om hvem som er juridisk far eller medmor til et barn, må avgjøres i en egen særskilt farskapssak (etter §§ 6 eller 7 i barneloven). Farskapet kan ikke prøves eller overprøves som et sidespørsmål i en annen rettssak, som for eksempel en arvesak.",
        "paragraftekst": "Domstolar eller styringsorgan kan ikkje prøve farskapen eller medmorskapen i andre saker enn nemnt i §§ 6 og 7. Domstol eller styringsorgan kan ikkje i andre saker leggje til grunn at ein mann er faren eller ei kvinne medmora utan at det er fastsett etter lova her.",
        "hva_betyr_html": """<p>Loven setter opp en vanntett skott rundt hvem som er et barns forelder. Staten vil ha ryddige registre. Hvis en mann er oppført som far i Folkeregisteret, så <em>er</em> han far i alle sammenhenger. Et forvaltningsorgan, som Skatteetaten eller NAV, kan ikke plutselig bestemme at de tror noen andre er faren i en spesifikk sak de saksbehandler.</p>
<p>Det vanligste problemet oppstår i arveoppgjør. Et barn krever arv etter en avdød mann. Søsknene protesterer og sier: "Du er jo ikke hans biologiske sønn, se på ham, han ligner jo ikke!". De krever at skifteretten (domstolen som behandler arven) skal ta en DNA-test for å avvise barnet.</p>
<p>Denne paragrafen stopper slike krav. Den sier at domstolen i en arvesak ikke har lov til å røre farskapet. Står mannen oppført som far i Folkeregisteret, arver barnet ham. Vil søsknene bestride det, må de stanse arveoppgjøret, anlegge et helt nytt og eget søksmål om endring av farskap etter § 6, vinne den saken, og <em>først da</em> kan barnet slettes fra arverekkefølgen.</p>""",
        "eksempler": [{"navn": "Arvingene", "tekst": "Når rike Hans dør, dukker det opp en ukjent 30-åring, Per, som står oppført som sønnen hans fra et tidligere ekteskap. Hans sine andre barn nekter å gi Per arv, og sier at de vil bevise at mor til Per var utro den gangen. De krever farskapstest under selve arvesaken i tingretten. Dommeren avviser kravet og viser til barnelova § 8. Dommeren sier at Per er juridisk sønn, og får arv, fordi farskapet ikke kan bestrides som en del av arveoppgjøret. Arvingene måtte i så fall ha reist en egen, formell farskapssak før arven kunne fordeles."}],
        "vanlige_feil": ["Blande farskapskrangler inn i forhandlinger om samvær eller barnefordeling (først må farskapet bestrides i egen sak, inntil det er gjort, er mannen far).", "NAV-saksbehandlere som fatter vedtak om bidrag basert på hvem mor mener er faren, før farskapet er offisielt registrert etter lovens bokstav."],
        "hva_bor_du_html": "<p>Dersom du står midt i en konflikt om barnebidrag, arv eller omsorg, og du mener at farskapet er feil: Ikke bruk tid på å krangle om farskapet i de brevene du sender til tingretten om samvær eller arv. Du må sende en egen, isolert stevning som gjelder utelukkende \"Endring av farskap\" (etter § 6). Når du har fått medhold i den saken, vil det få umiddelbar effekt på de andre sakene dine.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg stoppe utbetaling av barnebidrag mens farskapssaken pågår?", "a": "Nei, normalt ikke. Så lenge du står som juridisk far, har du forsørgerplikt (se § 66). Du må betale inntil domstolen har avsagt dom om at du ikke er faren. Deretter kan du kreve å få pengene tilbakebetalt."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "6", "tittel": "hvordan en ekte farskapssak for domstolen gjøres", "available": True},
            {"lov": "barnelova", "paragraf": "7", "tittel": "hvordan farskapet endres hvis alle er enige", "available": True},
        ],
    },
    {
        "number": "9",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Når kan en domstol dømme en mann som far?",
        "kategori": "familie",
        "description": "DNA trumfer alt i farskapssaker. Men hva skjer hvis DNA mangler, eller barnet er laget på en klinikk med donor? Slik dømmer retten.",
        "kort_svar": "Domstolen legger en DNA-analyse til grunn som et absolutt bevis. Finnes det ingen DNA-test, kan en mann likevel dømmes til far hvis det er bevist at han hadde samleie med mor da hun ble gravid, og det er mest sannsynlig at han er faren. En sæddonor kan aldri dømmes til å være far.",
        "paragraftekst": """Dersom ein mann blir utpeikt som far etter DNA-analyse, skal dom seiast for at han er faren. Dersom det ikkje ligg føre DNA-analyse, eller det er grunn til å tru at det heftar feil ved DNA-analysen, eller dersom nærståande slektningar også framstår som mogelege fedre, gjeld reglane i andre og tredje stykket.

Har ein mann hatt samlege med mora på den tid ho kan ha blitt med barnet, skal dom seiast for at han er faren, dersom det ikkje er lite truleg at han er far til barnet.

Har mora hatt samlege med fleire menn i den tida ho kan ha blitt med barnet, skal dom for farskap likevel berre seiast når det er monaleg meir truleg at ein av dei er faren enn nokon av dei andre.

Er det utført assistert befruktning på mora, og ektemann eller sambuar har gitt sitt samtykke til dette, skal det seiast dom for at han er faren, dersom det ikkje er lite truleg at barnet er avla ved assistert befruktning.

Sædgiveren kan ikkje dømast til far. Dette gjeld likevel ikkje dersom assistert befruktning er gjort med sæd frå ektemann eller sambuar.""",
        "hva_betyr_html": """<p>Når en far nekter for at han er far, eller en annen mann krever å få bli far, havner saken i retten. Paragrafen her forteller dommeren nøyaktig hvilke bevisregler som gjelder.</p>
<p><strong>Hovedregelen er DNA</strong> Dagens teknologi gir dommeren en enkel jobb: Utpeker en sikker og godkjent DNA-analyse en bestemt mann som far (ofte med 99,99 % sikkerhet), så dømmer retten at han er far. Det finnes ingen vei unna for mannen.</p>
<p><strong>Hva hvis DNA mangler?</strong> Det hender at mannen dør før DNA kan sikres, eller rømmer landet, og barnet mangler DNA-materiale å teste mot. Da må dommeren bruke gamlemåten. Beviskravet er da: Hadde mannen samleie med mor i uken hun ble gravid? Hvis ja, skal han dømmes som far med mindre noe tyder på at det var fysisk umulig (for eksempel at han var steril).</p>
<p>Lå mor med flere menn den uken? Da må retten veie sannsynligheten. Retten vil bare dømme én mann til far hvis det er <em>betydelig mer sannsynlig</em> ("monaleg meir truleg") at det var ham enn de andre.</p>
<p><strong>Assistert befruktning</strong> For par som bruker fertilitetsklinikk er det et helt eget regelverk. Har ektemannen eller den mannlige samboeren signert et samtykke på at mor kan gjennomgå assistert befruktning med donorsæd, fanger bordet. Da dømmes <em>han</em> som faren, selv om han ikke har en eneste genetisk fellesnevner med barnet.</p>
<p>En anonym eller åpen sæddonor på en klinikk er totalfredet av loven. En kvinne kan aldri spore opp sæddonoren og dra ham for retten for å kreve barnebidrag. (Unntaket er naturligvis hvis paret leverte sin <em>egen</em> sæd til sykehuset — da er det ektemannen sin sæd, og han dømmes som far).</p>
<h3>Kan en donor dømmes til far?</h3>
<table class="rule-table"><thead><tr><th>Situasjon</th><th>Lov gjelder (kan bli far)</th><th>Lov gjelder ikke (fredet)</th></tr></thead><tbody><tr><td>Mann donerer sæd via godkjent klinikk</td><td></td><td>X</td></tr><tr><td>Ektemann samtykker til at kona insemineres med donorsæd</td><td>X (Han blir far)</td><td></td></tr><tr><td>Mann gir sæd privat ("hjemmeinseminasjon" i et glass)</td><td>X (Han blir far)</td><td></td></tr><tr><td>Mann har samleie som "tjeneste" for at kvinne skal bli gravid</td><td>X (Han blir far)</td><td></td></tr></tbody></table>""",
        "eksempler": [{"navn": "Ola og de to vennene", "tekst": "Ida ble gravid og husker at hun var intim med både Ola og Petter i løpet av samme helg. Begge nekter farskap. Saken havner i retten. Det tas DNA-test av barnet, Ola og Petter. Analysen utelukker Petter 100 %, og utpeker Ola med 99,99 % sikkerhet. Dommeren ser på DNA-testen og dømmer Ola til far. Ola har ingenting han skulle sagt — dommeren har plikt til å følge DNA-resultatet etter første ledd."}],
        "vanlige_feil": ["En venn går med på å donere sæd i et glass hjemme (\"kalkun-metoden\"), og tror han er fredet slik som klinikk-donorer. (Nei, han regnes som far og kan dømmes).", "En ektemann ombestemmer seg og vil skilles når kona er seks måneder på vei etter prøverør, og vil slette farskapet fordi barnet ikke er hans genetisk. (Umulig, har han samtykket, blir han far)."],
        "hva_bor_du_html": "",
        "dumme_sporsmal": [
            {"q": "Hva om DNA-testen sier at jeg er far, men det er min eneggede tvilling som lå med henne?", "a": "Dette er grunnen til at loven skriver: \"dersom nærståande slektningar også framstår som mogelege fedre, gjeld reglane i andre og tredje stykket\". DNA-tester mellom eneggede tvillinger sliter med å skille dem, og brødre kan ha likt DNA. Da må retten gå bort fra DNA som eneste bevis, og bruke den gamle regelen: Hvem av dere hadde faktisk samleie med henne den helgen? Bevisføring og vitner må til."},
            {"q": "Kan retten virkelig dømme meg hvis jeg rømmer og de aldri får tatt blodprøven min?", "a": "Ja. Hvis NAV og politiet ikke får tak i deg, kan dommeren til slutt fatte en avgjørelse (\"avsi dom i uteblivelse\") basert på mors vitnemål og bevis på at dere var sammen i perioden. Det lønner seg aldri å stikke av fra en farskapssak."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "6", "tittel": "selve rettssaken om endring av farskap", "available": True},
            {"lov": "barnelova", "paragraf": "24", "tittel": "rettens adgang til å tvinge frem DNA", "available": True},
        ],
    },
    {
        "number": "10",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "NAVs oppgaver når farskapet er ukjent",
        "kategori": "familie",
        "description": "Hva gjør NAV hvis et barn blir født uten at faren har signert papirene? De sender et brev og spør ham rett ut.",
        "kort_svar": "Når NAV (\"tilskotsfuten\") får beskjed om at et barn er født uten at en far har skrevet under, tar de kontakt med mannen moren har oppgitt som far. NAV vil oppfordre ham til å erklære farskapet frivillig, og informere begge om deres rettigheter og plikter overfor barnet.",
        "paragraftekst": """Når tilskotsfuten får fødselsmelding etter § 1 fjerde stykket fordi farskapen ikkje er fastsett, skal han melde frå til den oppgjevne faren. Erklærer han ikkje farskapen i samsvar med § 4, skal tilskotsfuten om råd få han til å seia kva han meiner om farskapsspørsmålet. Erklærer han farskapen, skal tilskotsfuten melde frå om det til folkeregistermyndigheita. Elles skal arbeids- og velferdsetaten handsame saka vidare.

Tilskotsfuten skal sjølvbedd gjere både mora og den oppgjevne faren kjend med kva for økonomiske og andre rettar og plikter dei har når det gjeld barnet.

Departementet peikar ut tilskotsfut.""",
        "hva_betyr_html": """<p>Paragrafen beskriver den praktiske byråkrati-løypa som starter når ugifte mødre føder et barn og mannen ikke allerede har signert farskapserklæringen på nett (etter § 4).</p>
<p>Barneloven bruker det gammeldagse ordet "tilskotsfuten". I dag betyr dette rett og slett NAV (nærmere bestemt enheten for bidrag).</p>
<p>Sykehuset oppgir på fødselsmeldingen hvem mor sier er faren. NAV sender deretter et brev til denne mannen. De sier: "Du er oppgitt som far til et barn født på denne datoen. Vil du signere farskapet frivillig?".</p>
<p>Svarer han ja og signerer, sender NAV saken videre til Folkeregisteret. Mannen er da formelt far, og saken er lukket.</p>
<p>Svarer han nei, eller nekter å svare i det hele tatt, har NAV plikt til å gå videre med saken. De vil da be ham redegjøre for sin versjon — mener han at mor lyver, eller krever han bare en DNA-test for å være sikker? Hvis saken stopper opp, vil det bli overført til avdelingen i NAV som håndterer DNA-pålegg (se § 11).</p>
<p>Loven pålegger også NAV en opplysningsplikt: Uten at mor eller far trenger å spørre, skal NAV sende dem informasjon om hva det betyr å være foreldre. Dette gjelder særlig informasjon om barnebidrag, foreldreansvar og samværsrett.</p>""",
        "eksempler": [{"navn": "Andreas", "tekst": "Hanne får et barn. Siden hun og Andreas slo opp under graviditeten, har ikke Andreas giddet å logge inn på Helsenorge for å signere farskapet. Hanne oppgir navnet hans på sykehuset. To uker senere dumper det ned et brev fra NAV i den digitale postkassen til Andreas. NAV informerer om at han er oppgitt som far, og ber ham signere skjemaet hvis han erkjenner dette. Andreas innser at han ikke kan rømme fra ansvaret. Han fyller ut skjemaet og sender det tilbake til NAV, som oppdaterer Folkeregisteret."}],
        "vanlige_feil": ["Faren kaster brevet fra NAV og tror problemet forsvinner hvis han ignorerer det (brevet er bare første steg, neste steg er pålegg om DNA).", "Mor tror at når hun har oppgitt faren på sykehuset, så er farskapet fastsatt og ferdig. Slik er det ikke — mannen må bekrefte det via NAV, ellers er han fremdeles ikke formelt far."],
        "hva_bor_du_html": "<p>Hvis du er mannen som mottar dette brevet fra NAV: Er du sikker på at du er faren? Signer skjemaet og returner det, slik at barnet ditt får det formelle på plass. Er du usikker på om du er faren? Svar NAV at du ikke vil erkjenne farskapet før det foreligger en DNA-test. NAV vil da sørge for at dere får tilbud om DNA-analyse helt gratis, slik at tvilen blir fjernet før du skriver under.</p>",
        "dumme_sporsmal": [
            {"q": "Hvorfor kaller loven NAV for tilskotsfuten?", "a": "I gamle dager fantes det en egen offentlig ansatt \"bidragsfogd\" i alle kommuner som hadde jobben med å sikre penger til uekte barn. Loven fra 1981 bruker fremdeles arvtaker-tittelen \"tilskotsfut\", men i dag styres alt dette av statlige NAV."},
            {"q": "Kan NAV tvinge meg til å betale barnebidrag med én gang de sender brevet?", "a": "Nei. Så lenge du ikke har signert farskapet, eller blitt dømt som far på grunnlag av en DNA-test, er du ikke far i juridisk forstand. NAV kan ikke kreve deg for barnebidrag før farskapet er endelig registrert. Men betaler du ikke frivillig og du senere blir påvist som far, kan bidraget bli krevd med tilbakevirkende kraft fra barnet ble født."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "11", "tittel": "hva NAV gjør når du nekter (DNA-pålegg)", "available": True},
            {"lov": "barnelova", "paragraf": "4", "tittel": "hvordan erklæringen av farskap ser ut", "available": True},
            {"lov": "barnelova", "paragraf": "5", "tittel": "statens plikt til å spore opp en far", "available": True},
        ],
    },
    {
        "number": "11",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "NAV kan pålegge mor og far å ta DNA-test",
        "kategori": "familie",
        "description": "Nekter den utpekte mannen å være far? Da kan NAV kreve at han, moren og barnet avgir DNA for å fastslå sannheten, helt gratis.",
        "kort_svar": "Hvis det er uenighet om hvem som er far, har NAV rett til å gi pålegg om at alle involverte (mor, barnet og de mulige fedrene) må ta en DNA-test. NAV kan også be partene om å forklare seg. Viser DNA-testen hvem som er faren, ber NAV ham om å signere farskapserklæringen.",
        "paragraftekst": """Arbeids- og velferdsdirektoratet kan krevje at mora og den eller dei som kan vere far til barnet, gjev forklaring, og kan gje pålegg om at dei og barnet skal gje frå seg ei eigna prøve til DNA-analyse. I særlege tilfelle kan den som kan vere far, bli pålagd å gje frå seg ei eigna prøve til DNA-analyse før barnet er født.

Arbeids- og velferdsdirektoratet skal oppmode den mannen som analysen utpeikar som far, til å erklære farskapen.

Døyr barnet kort tid etter fødselen eller andre sterke grunnar talar for det, kan Arbeids- og velferdsdirektoratet leggje bort saka når mora er samd i det.

Dersom Arbeids- og velferdsdirektoratet legg bort saka, kan barnet, mora eller den mannen som meiner at han er far til barnet, sjølv reise sak om farskapen for domstolane.

Departementet kan ved forskrift gje utfyllande reglar om prøvetaking, eigna biologisk materiale og DNA-analyse til bruk i saker om farskap eller slektskap.""",
        "hva_betyr_html": """<p>Paragrafen gir NAV skarpe verktøy for å rydde opp i rotete farskapssaker, slik at man unngår domstolen hvis mulig.</p>
<p>Hvis mannen som mor oppgir, sier "det er ikke mitt barn", kan NAV sende ut et offisielt pålegg om DNA-analyse. Dette pålegget går til alle parter. Mor må ta med barnet for å gi en prøve (vanligvis spyttprøve, noen ganger blodprøve), og den eller de mennene mor har oppgitt, må også møte opp hos lege og la seg teste.</p>
<p>I svært spesielle tilfeller (for eksempel hvis far er dødssyk, eller planlegger å forlate landet permanent), kan NAV kreve at mannen avgir sitt DNA allerede <em>før</em> barnet er født, slik at saken kan løses raskt etter fødselen.</p>
<p>Når DNA-svaret kommer tilbake fra laboratoriet, og det viser 99,99 % treff på en mann, sender NAV saken tilbake til ham. De sier: "Prøven er positiv, du er faren. Vær så snill å signer denne farskapserklæringen nå". Hvis han da signerer, er saken over.</p>
<p>Siste del av paragrafen handler om unntakene. Hvis barnet dør kort tid etter fødselen, er det ofte unødvendig traumatisk å jakte ned faren, med mindre moren sterkt ønsker det. Da kan NAV lukke saken, så fremt mor godtar det. NAV kan også lukke saker (gi opp) hvis faren befinner seg i et krigsherjet land der ingen svarer på post, og det er umulig å få DNA.</p>""",
        "eksempler": [{"navn": "Trine, Tom og Lasse", "tekst": "Trine vet ikke om Tom eller Lasse er faren til babyen hennes. Begge mennene avviser henne, og ingen vil ha ansvaret. Trine melder inn begge to til NAV. NAV innkaller Trine og ber om en forklaring (hvem hun var med og når). Deretter sender NAV et formelt pålegg om at Tom og Lasse må møte opp hos fastlegen sin og avgi en spyttprøve for farskapssaken. Resultatet utelukker Tom fullstendig, mens Lasse er en match. NAV sender Lasse et brev med oppfordring om å erklære farskapet."}],
        "vanlige_feil": ["En mann ignorerer DNA-innkallingen fra NAV i tro om at han kan \"gjemme seg\" for systemet. (Ignorerer man pålegget, sender NAV saken til domstolen, og da kobles politiet inn for å hente ham).", "Mor nekter å møte opp med barnet til testen fordi hun ombestemte seg og ikke vil vite hvem faren er likevel. (Mor har ikke lov til å nekte).", "Tro at testen koster penger. Alt dekkes av staten når NAV krever den."],
        "hva_bor_du_html": "<p>Mottar du et brev fra NAV om at du må møte opp for å avgi DNA i en farskapssak? 1. Bestill time hos legen slik brevet instruerer. 2. Ta med gyldig legitimasjon. 3. Vent på at NAV tar kontakt med resultatet. Det er den raskeste, rimeligste (gratis) og minst ubehagelige måten å få avklart tvilen på.</p>",
        "dumme_sporsmal": [
            {"q": "Hva skjer hvis DNA-testen er positiv, men jeg *fremdeles* nekter å skrive under på erklæringen?", "a": "Da har NAV gjort alt de kan, men du er fortsatt ikke far på papiret (siden en erklæring krever din frivillige signatur). NAV vil da automatisk sende saken videre til tingretten (se § 13). Der vil dommeren bruke NAVs DNA-test som bevis, og dømme deg som far ved en dom. Dommen tvinger gjennom farskapet ditt enten du vil eller ikke."},
            {"q": "Kan NAV kreve DNA fra broren min hvis jeg ikke kan møte?", "a": "Det er opp til forskriften, men normalt sett kreves DNA av den direkte mistenkte. Er mannen død eller umulig å finne, åpner loven i visse tilfeller for å teste biologiske slektninger for å avgjøre saken (se § 24)."},
            {"q": "Får jeg vite resultatet av de andre mennene sine prøver?", "a": "Nei. Du får bare beskjed om du er faren eller ikke. Hvem de andre mennene var, eller hvem av dem som fikk treff, er taushetsbelagt informasjon som bare angår mor, barnet og den faktiske faren."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "10", "tittel": "det opprinnelige forsøket fra NAV på å få frivillig signatur", "available": True},
            {"lov": "barnelova", "paragraf": "13", "tittel": "hva som skjer hvis du nekter å signere etter en positiv test", "available": True},
            {"lov": "barnelova", "paragraf": "24", "tittel": "domstolens rett til å innhente DNA med tvang", "available": True},
        ],
    },
    {
        "number": "13",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Når farskapssaken må sendes til tingretten",
        "kategori": "familie",
        "description": "Hva skjer hvis menn nekter å samarbeide med NAV i en farskapssak? Da pakker NAV sammen saken og sender den til domstolen, som tar over ansvaret.",
        "kort_svar": "Hvis mannen som NAV ber om å signere farskapet ikke gjør det, eller hvis mor nekter å godta mannens erklæring, sender NAV saken videre til tingretten. Da blir saken en ordinær rettssak hvor en dommer bestemmer utfallet.",
        "paragraftekst": """Arbeids- og velfersdirektoratet skal sende stemning til tingretten til avgjerd etter kapittel 4 dersom han som er oppgjeven som far, ikkje har erklært farskapen eller mora ikkje har godteke ei erklæring skriftleg, og saka ikkje er lagd bort etter § 11 tredje stykket.

Endar ei rettssak utan at farskapen vert fastsett, og han heller ikkje vert fastsett seinare, kan Arbeids- og velferdsdirektoratet sende saka til retten på nytt dersom det kjem fram nye opplysningar som tyder på at faren kan vere ein mann som tidlegare ikkje har vore part i saka.""",
        "hva_betyr_html": """<p>Denne paragrafen er overgangen fra det byråkratiske frivillige sporet i NAV, og over til det harde maktsporet i domstolene.</p>
<p>NAV har ikke lov til å tvinge gjennom et farskap på papiret. NAVs jobb er å informere, hente inn DNA, og spørre faren pent om han vil skrive under. Hvis mannen etter alt dette fortsatt nekter å sette navnet sitt på papiret, sier loven stopp for NAV. Da har NAV en plikt til å reise en offisiell rettssak mot faren. De sender en "stevning" (saksdokument) til den lokale tingretten. Tingretten vil deretter behandle saken etter reglene i Barnelovens kapittel 4.</p>
<p>Det samme gjelder hvis det er <em>mor</em> som er vanskelig, og hun nekter å godkjenne erklæringen fra den faren hun opprinnelig pekte ut.</p>
<p>Andre ledd sier at hvis rettssaken ender med at de to mennene retten testet ikke var far, så lukkes saken. Men skulle mor et par år senere huske navnet på en tredje mann hun hadde sex med, kan NAV starte en ny sak i domstolen mot denne tredje mannen.</p>""",
        "eksempler": [{"navn": "Tommy", "tekst": "Tommy har fått et brev fra NAV om at hans DNA er en match for et barn Siri har født. NAV ber Tommy logge inn og signere farskapet frivillig. Tommy er irritert over at han har fått barn, og velger å ignorere brevene fra NAV og sletter e-postene deres. NAV har nå ikke noe annet valg. De pakker saken, sender den til tingretten, og Tommy mottar et formelt søksmål fra domstolen."}],
        "vanlige_feil": ["Menn tror de kan kjøpe seg tid eller slippe unna barnebidrag ved å nekte å svare NAV (du oppnår bare at staten saksøker deg, og du blir dømt som far likevel).", "Mor tror at når hun har oppgitt faren, kan hun bare la være å signere godkjenningen i etterkant uten at det får konsekvenser (det resulterer i rettssak for å få det formelt fastslått)."],
        "hva_bor_du_html": "<p>Hvis du er 100 % sikker på at DNA-testen fra NAV er din, og at den er positiv, finnes det ingen gode juridiske grunner til å nekte å signere erklæringen frivillig. Hvis du tvinger NAV til å sende saken til tingretten, vil retten (se § 25) uansett avsi dom mot deg svært raskt, og du kaster bort tid og ressurser. Skriv under papirene NAV sender.</p>",
        "dumme_sporsmal": [
            {"q": "Får jeg saksomkostninger hvis NAV tar meg til retten og jeg blir dømt til far?", "a": "Nei, vanligvis ikke i farsskapssaker som det offentlige reiser, for reglene for kostnader (se § 29) sier at staten bærer sine egne kostnader og de kostnadene retten har for å opplyse saken. Du blir imidlertid stemplet som far, og barnebidraget vil begynne å løpe."},
            {"q": "Må jeg møte fysisk i tingretten hvis NAV sender saken dit?", "a": "Ofte slipper du det. Hvis DNA-testen allerede ligger i mappen fra NAV, kan dommeren fatte beslutningen (\"avsi dom\") uten at dere i det hele tatt trenger å møtes i retten, ifølge § 25. Rettssaken blir da bare en formalitet for å bytte ut din manglende signatur med en dom."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "11", "tittel": "prøvetakingen som leder opp til dette", "available": True},
            {"lov": "barnelova", "paragraf": "25", "tittel": "domstolen kan gi dom uten rettsmøte hvis DNA foreligger", "available": True},
            {"lov": "barnelova", "paragraf": "15", "tittel": "hvilken tingrett saken skal behandles i", "available": True},
        ],
    },
    {
        "number": "14",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvilke regler gjelder for retten i farskapssaker?",
        "kategori": "familie",
        "description": "Loven setter rammene for hvordan en domstol skal gjennomføre en farskapssak.",
        "kort_svar": "Når en farskapssak behandles i domstolen, er det reglene i barnelovens kapittel 4 som gjelder, sammen med de vanlige reglene i domstolloven og tvisteloven.",
        "paragraftekst": "For farskapssaker gjeld reglane i dette kapittel, domstolloven og tvisteloven.",
        "hva_betyr_html": "<p>Paragrafen er i stor grad en teknisk opplysning til advokater og dommere. Når NAV eller en privatperson drar en sak om farskap for tingretten, er det ikke et rent \"frivillig sirkus\". Det er en formell rettssak. Den følger rettens strenge spilleregler (som finnes i tvisteloven) om hvordan bevis føres og frister overholdes, supplert med domstolloven for hvordan domstolen fungerer. Men de helt spesielle unntakene som gjelder akkurat for farskap (som tvang for DNA-tester), finner man i resten av dette kapittelet i barneloven.</p>",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "<p>Skal du i retten i en farskapssak, bør du skaffe deg advokat. Advokaten vet hvordan de ulike lovene spiller sammen, og hva slags beviskrav dommeren må forholde seg til.</p>",
        "dumme_sporsmal": [
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "13", "tittel": "hvordan saken i det hele tatt kom til domstolen", "available": True},
            {"lov": "barnelova", "paragraf": "15", "tittel": "hvilken domstol som skal ta saken", "available": True},
        ],
    },
    {
        "number": "15",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvor skal en farskapssak føres for retten?",
        "kategori": "familie",
        "description": "Hvilken by skal rettssaken om farskap gå i? Hovedregelen er at saken reises der barnet bor. Hvis barnet bor i utlandet, skal saken gå der mor bor.",
        "kort_svar": "En rettssak om farskap skal som hovedregel føres i den tingretten der barnet er folkeregistrert (barnets verneting). Hvis barnet og mor bor i utlandet, går saken der den oppgitte faren bor. For barn på hemmelig adresse holdes saken i Oslo tingrett.",
        "paragraftekst": """Saka skal reisast ved det alminnelege vernetinget til barnet. Lever ikkje barnet eller bur det utanfor riket, skal saka reisast ved det alminnelege vernetinget til mora. Er også ho død eller busett utanfor riket, skal saka reisast ved det alminnelege vernetinget til den oppgjevne faren.

Dersom mora eller barnet bur på sperra adresse, jf. lov 9. desember 2016 nr. 88 om folkeregistrering med forskrifter, eller det er søkt om eller gjeve løyve til å nytte fiktive personopplysningar for mora eller barnet, jf. lov 4. august 1995 nr. 53 om politiet § 14 a, kan saka reisast for Oslo tingrett.""",
        "hva_betyr_html": """<p>I jussen heter det å "ha verneting" et sted. Det betyr at domstolen i det området har ansvaret for deg.</p>
<p>Denne paragrafen bestemmer rekkefølgen for hvor en farskapssak skal avholdes: 1. <strong>Førstevalg:</strong> Der barnet bor. Bor barnet i Bergen, skal saken føres i Hordaland tingrett. Dette gjelder selv om mannen som er stevnet, kanskje bor i Tromsø og må reise langt. 2. <strong>Andrevalg:</strong> Der mor bor. Hvis barnet har flyttet til Sverige, eller barnet døde kort tid etter fødselen, skal saken føres i domstolen der mor bor i Norge. 3. <strong>Tredjevalg:</strong> Der faren bor. Hvis både barnet og mor bor i utlandet (og det likevel er grunnlag for å kjøre saken i Norge, for eksempel fordi barnet er unnfanget her eller faren krever det), skal saken gå i tingretten der den oppgitte faren bor.</p>
<p>Det andre leddet gir et svært viktig unntak for voldsutsatte kvinner og barn. Hvis mor og barn lever på "sperret adresse" (strengt fortrolig eller fortrolig adresse) fordi de flykter fra vold, ville en rettssak i deres lokale tingrett røpe hvor i landet de befinner seg. Derfor slår loven fast at i slike beskyttelsessaker, holdes rettssaken alltid sentralt i Oslo tingrett for å skjerme familiens skjulested.</p>""",
        "eksempler": [{"navn": "Trond og Hanne", "tekst": "Trond bor i Kristiansand. Hanne bor i Trondheim. De har et felles barn som bor fast hos Hanne i Trondheim. Trond krever en farskapssak for å fjerne sitt farskap fordi han mistenker at barnet ikke er hans. Trond kan ikke sende papirene til Agder tingrett (i Kristiansand) der han selv bor. Han må sende stevningen til Trøndelag tingrett i Trondheim, fordi det er der barnet bor."}],
        "vanlige_feil": ["Sende stevningen til sin egen lokale domstol for å gjøre det enkelt for seg selv. Retten vil avvise saken, og du mister tid og penger."],
        "hva_bor_du_html": "<p>Finn ut hvilken tingrett barnet tilhører, og send papirene dit. Skal du saksøke staten eller en mor for å få avklart farskap, bør advokaten din sørge for at vernetinget blir helt riktig fra starten av.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om mor har flyttet barnet underveis i rettssaken?", "a": "Det er adressen på det tidspunktet saken (\"stevningen\") sendes inn til domstolen som teller. Flytter de etterpå, fortsetter saken vanligvis i den samme tingretten for å unngå forsinkelser."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "13", "tittel": "om at NAV sender saken til tingretten", "available": True},
            {"lov": "barnelova", "paragraf": "57", "tittel": "tilsvarende regel for hvor saker om foreldreansvar og samvær skal gå", "available": True},
        ],
    },
    {
        "number": "16",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvilke andre krav kan bakes inn i en farskapssak?",
        "kategori": "familie",
        "description": "Kan dommeren avgjøre barnebidraget samtidig som farskapet? Ja, loven tillater at domstolen tar opp ting som springer direkte ut av farskapssaken.",
        "kort_svar": "En farskapssak handler primært om hvem som er far. Men du kan be domstolen om å avgjøre andre uenigheter i samme slengen, forutsatt at disse uenighetene er en direkte konsekvens av selve farskapet — for eksempel barnebidrag, foreldreansvar eller samvær.",
        "paragraftekst": "I ei farskapssak kan andre tvistemål berre takast opp når dei gjeld ei følgje av farskapen eller av farskapssaka.",
        "hva_betyr_html": """<p>Normalt vil domstolen helst ha "rene" saker. Er saken en farskapssak, vil dommeren bare finne ut om mannen er far eller ikke.</p>
<p>Men for å unngå at foreldrene må reise en helt ny rettssak uken etter for å fordele samvær, sier denne paragrafen at de kan bake relaterte krav inn i den opprinnelige farskapssaken.</p>
<p>Siden barnebidrag er en direkte "følge" av hvem som dømmes som far, kan moren legge inn et krav om at retten også fastsetter bidraget hvis mannen dømmes. På samme måte kan faren kreve samværsrett hvis han blir dømt som far. Du kan derimot ikke bake inn krangler om hvem som eier bilen, eller hvem som skal betale kredittkortgjelden fra da dere var sammen — det har ingenting med farskapet å gjøre.</p>""",
        "eksempler": [{"navn": "Per", "tekst": "Nina saksøker Per for å få dom på at han er faren til datteren hennes. Per benekter dette. I samme stevning ber Nina retten fastsette at Per skal betale 5 000 kr i månedlig barnebidrag dersom han blir dømt. Dommeren tillater dette kravet i saken fordi bidragsplikten er en direkte konsekvens av at Per eventuelt blir faren."}],
        "vanlige_feil": ["Blande inn ren økonomisk uenighet (oppgjør etter samboerskap) i en farskapssak."],
        "hva_bor_du_html": "",
        "dumme_sporsmal": [
            {"q": "Vil domstolen alltid behandle samvær i en farskapssak hvis jeg ber om det?", "a": "Ikke nødvendigvis. Selv om loven tillater det, kan dommeren velge å dele opp saken (dele \"forhandlingene\"). Det betyr at dommeren først avgjør selve farskapet med DNA. Viser det seg at du er faren, kan dommeren behandle spørsmålet om samvær senere, eller be dere ta samværsspørsmålet via mekling hos familievernet før retten griper inn."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "8", "tittel": "man kan ikke ta opp farskap som en *del* av en arvesak (denne paragrafen går motsatt vei)", "available": True},
            {"lov": "barnelova", "paragraf": "56", "tittel": "når du saksøker kun for samvær eller foreldreansvar", "available": True},
        ],
    },
    {
        "number": "17",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvem er partene i en farskapssak?",
        "kategori": "familie",
        "description": "Hvem har egentlig noe de skulle ha sagt i en farskapssak for retten? Det er strenge regler for hvem som regnes som \"part\", og hva som skjer hvis noen dør.",
        "kort_svar": "I en farskapssak er det barnet, moren, og enhver mann som enten regnes for å være far, eller som *kan* være faren, som er parter. Hvis en mulig far er død, trer arvingene hans eller dødsboet inn som part i saken i hans sted.",
        "paragraftekst": """I farskapssaker er både barnet, mora og kvar mann som vert rekna for faren eller kan vere det, partar i saka.

Døyr ein mann som kan vere far til barnet, skal dødsbuet eller arvingane hans gjerast til part.

Kjem det fram opplysningar som tyder på at nokon annan kan vere faren, skal retten ved prosesskriv gjere han til saksøkt.""",
        "hva_betyr_html": """<p>Å være "part" i en rettssak betyr at du har rett til å uttale deg, føre bevis, stille spørsmål og få innsyn i alle saksdokumentene. Siden farskap handler om hvem et barn stammer fra, begrenser loven hvem som kan blande seg inn. Det er ikke åpent for at besteforeldre eller nysgjerrige tanter kan gjøre seg til part i saken.</p>
<p>De som automatisk har partsrettigheter er: 1. <strong>Barnet</strong> (ofte representert ved mor eller en verge) 2. <strong>Moren</strong> 3. <strong>Den nåværende juridiske faren</strong> (hvis det finnes en på papiret) 4. <strong>Den potensielle biologiske faren</strong> (mannen som hevder han er far, eller som mor mener er faren)</p>
<p>Et svært viktig poeng er hva som skjer hvis mannen dør før farskapet er avklart. Farskap handler om arv. Hvis en mann dør og etterlater seg et barn som kanskje er hans, vil dette barnet ha krav på sin del av arven. Derfor sier andre ledd at <strong>dødsboet eller arvingene</strong> blir parter. De andre barna til avdøde, eller enken hans, må da møte i retten. De representerer hans interesser, og har lov til å forsvare boet mot kravet om farskap hvis de tviler på at barnet er hans.</p>
<p>Hvis det plutselig under rettssaken dukker opp informasjon om at en helt ny, uventet mann kan være faren — for eksempel hvis mor bryter sammen i vitneboksen og innrømmer en affære ingen visste om — gir tredje ledd dommeren plikt til å gripe inn. Dommeren vil da formelt trekke denne nye mannen inn i saken som saksøkt, slik at også han må møte i retten og ta en DNA-test.</p>""",
        "eksempler": [{"navn": "Arven etter Tom", "tekst": "Tom dør i en ulykke. Han var en velstående mann og etterlater seg to voksne barn. En måned etter begravelsen mottar de et varsel fra tingretten. En 19 år gammel gutt, Jonas, har reist farskapssak og krever å bli anerkjent som Toms sønn for å få sin del av arven. Siden Tom er død, blir Toms to voksne barn (arvingene) gjort til parter i saken etter § 17. De får advokathjelp, får se Jonas sine bevis, og har rett til å delta i rettssaken og kreve DNA-test av Tom sitt lagrede medisinske materiale før dommeren fatter en beslutning."}],
        "vanlige_feil": ["En mulig far tror han kan nekte å være part ved å bare ignorere brevene fra domstolen (du er part uansett, og saken kjøres mot deg).", "Arvinger tror farskapssaker \"dør\" sammen med mannen (barnets rett til å vite og arve forsvinner ikke ved dødsfall).", "Mor tror hun kan utelate menn fra saken fordi hun ikke liker dem (dommeren skal trekke inn alle menn det er skjellig grunn til å tro kan være faren)."],
        "hva_bor_du_html": """<p>Hvis du blir trukket inn som part i en farskapssak, enten som mulig far eller som arving til en mulig far, må du ta saken på største alvor. Du bør kontakte en advokat umiddelbart. Du vil få innkalling til rettsmøter og et pålegg om DNA-test. Din status som part gir deg rett til å kreve at domstolen dekker kostnadene for din advokat gjennom ordningen for fri rettshjelp, dersom du oppfyller vilkårene for dette.</p>
<p>Er du arving og blir stevnet i en farskapssak etter din avdøde far, bør dere unngå å fordele arven (skiftet) før farskapssaken er endelig avgjort. Blir barnet dømt til å være din fars barn, har barnet krav på pliktdelsarv.</p>""",
        "dumme_sporsmal": [
            {"q": "Kan min nye ektemann være part i farskapssaken mot min eks?", "a": "Nei. Din nye ektemann har ingen biologisk eller juridisk tilknytning til saken. Han kan støtte deg følelsesmessig, men han får ikke uttale seg i retten eller lese de hemmelige dokumentene. Det er kun du, barnet og de mulige fedrene som er parter."},
            {"q": "Hva skjer hvis dommeren trekker inn en mann, og det viser seg at han var steril?", "a": "Mannen vil fortsatt være en part i saken frem til han er offisielt frifunnet (vanligvis ved en dom etter DNA-test ellerisinske bevis på sterilitet). Det faktum at han var steril er et bevis han må legge frem for retten, det fjerner ikke hans status som saksøkt før saken er avsluttet."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "18", "tittel": "hvordan barnets rettigheter sikres av en verge", "available": True},
            {"lov": "barnelova", "paragraf": "24", "tittel": "hvordan DNA testes (også av døde menn)", "available": True},
        ],
    },
    {
        "number": "18",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Når trenger barnet en egen \"setteverge\"?",
        "kategori": "familie",
        "description": "Hva skjer hvis mor nekter å si hvem faren er for å beskytte ham, samtidig som barnet har rett på en far? Da oppnevner staten en egen verge for barnet.",
        "kort_svar": "Hvis mor har en interessekonflikt — for eksempel ved at hun nekter å oppgi hvem som er far, eller prøver å beskytte en bestemt mann — kan hun ikke representere barnet i en farskapssak. Retten skal da oppnevne en \"setteverge\" (en uavhengig person) som kjemper for barnets rett til å få fastslått farskapet.",
        "paragraftekst": "Er det ikkje oppnemnd verje for barnet, skal retten syte for oppnemning av setteverje når mora ikkje gjev opp kven faren er, eller når det ligg føre opplysningar som tyder på at faren kan vere ein annan enn den mora har gjeve opp.",
        "hva_betyr_html": """<p>Normalt er foreldrene verger for barnet sitt. I en farskapssak er det vanligvis moren som reiser saken på vegne av det lille barnet for å få mannen dømt som far. Da representerer hun barnets interesser perfekt.</p>
<p>Men noen ganger kræsjer mors interesser med barnets interesser. Barneloven bygger på et knallhardt prinsipp: <em>Barnet har rett til å vite hvem faren er, uansett hva mor måtte mene.</em></p>
<p>Kanskje mor er gift med en ny, snill mann, og nekter å oppgi den biologiske faren fordi hun er redd for at han skal kreve samvær? Eller kanskje hun dekker over hvem faren er fordi det var et utroskap, eller faren er en person med makt?</p>
<p>I slike situasjoner kan ikke retten stole på at mor gjør det som er best for barnet i selve rettssaken. Dommeren vil da be Statsforvalteren om å oppnevne en "setteverge". Dette er en midlertidig og uavhengig verge — ofte en advokat — som trer inn i morens sted utelukkende for akkurat denne saken. Settevergens eneste jobb er å være barnets stemme og kreve DNA-tester og vitneavhør, slik at sannheten kommer frem, selv om moren misliker det sterkt.</p>""",
        "eksempler": [{"navn": "Trine og \"den ukjente\"", "tekst": "Trine får et barn, men nekter å oppgi faren til NAV. NAV mistenker at det er sjefen hennes, Lars, som er faren, og sender saken til tingretten. I retten nekter Trine fremdeles å si et ord om hvem faren er, fordi hun vil beskytte arbeidsforholdet sitt. Dommeren innser at Trine motarbeider barnets rett til en far. Retten sørger for at advokat Hansen blir oppnevnt som setteverge for babyen. Settevergen krever at Lars innkalles og testes. Settevergen vinner frem, Lars blir testet positivt, og babyen får fastslått farskap og barnebidrag. Trine kunne ikke stoppe settevergen."}],
        "vanlige_feil": ["Mor tror at siden hun har foreldreansvaret alene, kan hun bestemme om farskapssaken skal kjøres eller ikke (staten og settevergen overstyrer henne).", "En mulig far tror saken henlegges bare fordi mor er på hans side og nekter å samarbeide med retten."],
        "hva_bor_du_html": "<p>Hvis du er i en situasjon der en setteverge har blitt oppnevnt for barnet ditt, må du huske at settevergen ikke er din fiende, men lovens verktøy for å sikre barnet. Du må forholde deg til at saken vil bli ført uansett hvor lite du ønsker det. Settevergen har lov til å kreve inn medisinske bevis og vitneforklaringer på vegne av barnet. Samarbeid med retten heller enn å motarbeide dem.</p>",
        "dumme_sporsmal": [
            {"q": "Får settevergen ta over den daglige omsorgen for barnet mitt?", "a": "Nei, absolutt ikke. En setteverge i en farskapssak (etter § 18) er utelukkende oppnevnt for å føre saken for domstolen. Personen fungerer som barnets advokat. Når dommen har falt og faren er fastsatt, forsvinner settevergen ut av bildet. Du beholder foreldreansvaret og den daglige omsorgen hele veien."},
            {"q": "Hvem betaler for denne settevergen?", "a": "Det er staten som dekker kostnadene til en oppnevnt setteverge i farskapssaker. Hverken mor eller far får regningen for dette, ettersom det er en del av domstolens plikt til å opplyse saken."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "5", "tittel": "statens plikt til å finne faren", "available": True},
            {"lov": "barnelova", "paragraf": "11", "tittel": "NAV sin rett til å kreve DNA og forklaring", "available": True},
        ],
    },
    {
        "number": "19",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Navnet ditt holdes hemmelig ved innkalling",
        "kategori": "familie",
        "description": "Hva skjer hvis noen som skal stevnes for farskap har forsvunnet? Retten kan annonsere i avisen, men loven beskytter personvernet ditt og skjuler navnet.",
        "kort_svar": "Hvis retten ikke finner en person som skal innkalles i en farskapssak, kan de varsle via offentlige kunngjøringer (aviser/Norsk lysingsblad). Loven krever da at navnene på de andre partene (som mor og barn) holdes skjult i kunngjøringen for å beskytte personvernet, med mindre helt spesielle grunner krever at de navngis.",
        "paragraftekst": "Ved tilseiing for nokon etter domstollova § 181 skal namnet på andre partar berre gjerast kjent når retten fastset det av særlege grunnar.",
        "hva_betyr_html": """<p>Noen ganger stikker den mulige faren av. Kanskje han har dratt til et ukjent land, kanskje han har gått under jorden, eller han bare nekter å åpne døren for postbudet. I norske rettssaker løser man dette ved å bruke domstolloven § 181. Den sier at hvis retten overhodet ikke kan finne deg, kan de sette inn en annonse i for eksempel lokalavisen eller Norsk lysingsblad: "Marius Hansen innkalles herved til rettsmøte...".</p>
<p>Men farskapssaker er ekstremt sensitive. Det er dypt personlig hvem som har hatt samleie med hvem. Hvis retten hadde satt inn en annonse som sa: "Marius Hansen innkalles i sak der Kari Nordmann hevder han er far til hennes sønn", ville Karis intime privatliv blitt brettet ut for hele Norge.</p>
<p>Derfor setter barneloven § 19 en streng stopper for dette. Når domstolen tvinges til å etterlyse noen offentlig, skal navnene på mor, barnet og eventuelt andre menn holdes strengt hemmelig i annonsen. Kun den som letes etter, skal nevnes ved navn.</p>
<p>Unntaket ("særlege grunnar") brukes ekstremt sjelden, for eksempel hvis det er helt nødvendig for å få mannen til å forstå hvilken sak det gjelder og det ikke finnes noen annen måte å varsle ham på.</p>""",
        "eksempler": [{"navn": "Marius er forsvunnet", "tekst": "Sofie har anlagt farskapssak mot Johan, en mann hun møtte på ferie for et år siden. Retten klarer ikke å finne Johans nåværende adresse. Dommeren beslutter å varsle Johan via Norsk lysingsblad. Annonsen lyder: \"Johan Johansen, født 12.04.1985, innkalles til Oslo tingrett i en farskapssak den 15. oktober.\" Annonsen nevner ikke Sofie eller barnets navn med et eneste ord, slik § 19 krever. Ser Johan annonsen, må han selv kontakte domstolen for å få vite hvem saken gjelder."}],
        "vanlige_feil": ["Menn som har gått under jorden tror saken stopper opp (den gjør ikke det, retten etterlyser deg offentlig, og behandler deretter saken uten deg)."],
        "hva_bor_du_html": "<p>Dette er en sjelden situasjon, men hvis du opplever at en motpart i farskapssaken stikker av eller gjør seg utilgjengelig, ikke få panikk. Advokaten din og retten har verktøy for å sikre at saken fortsetter. Rettssaken kan i ytterste konsekvens avsluttes med en dom selv om mannen aldri dukket opp for å svare for seg (kalt uteblivelsesdom).</p>",
        "dumme_sporsmal": [
            {"q": "Betyr dette at hele farskapssaken i tingretten foregår i all hemmelighet?", "a": "Ja. Farskapssaker og alle andre saker etter barneloven (som samvær og foreldreansvar) går for lukkede dører. Pressen eller publikum har ikke lov til å sitte i salen, og dommene anonymiseres strengt hvis de i det hele tatt blir publisert i ettertid. Personvernet ditt er godt beskyttet i disse sakene."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "23", "tittel": "retten kan fortsette og avsi dom selv om du lar være å møte opp", "available": True},
            {"lov": "barnelova", "paragraf": "15", "tittel": "hvilken tingrett som skal ha saken", "available": True},
        ],
    },
    {
        "number": "21",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Du har plikt til å svare på intime spørsmål i retten",
        "kategori": "familie",
        "description": "Kan du nekte å svare i retten fordi du skammer deg over hvem du lå med? Nei. I farskapssaker fjerner loven retten din til å nekte å forklare deg om utroskap.",
        "kort_svar": "Både mor og mulige fedre har plikt til å fortelle sannheten i retten, under straffeansvar (som vitner). I normale rettssaker kan du nekte å svare hvis svaret vil ødelegge ditt sosiale omdømme, for eksempel ved å avsløre grovt utroskap. I en farskapssak er dette unntaket fjernet: Du *må* svare, uansett hvor flaut det er.",
        "paragraftekst": """Både mora og den som kan vere far til barnet, har plikt til å forklare seg i saka etter reglane for vitne og med same ansvar som vitne.

Retten avgjer om ein part skal få høyre på medan ein annan part forklarar seg under saksførebuinga.

I farskapssaker kan ingen nekte å svare på spørsmål fordi svaret kan føre til vesentleg tap av sosialt omdøme eller anna vesentleg velferdstap for vedkomande, jf. tvisteloven § 22-9.

Når eit vitne har forklara seg under saksførebuinga, treng det ikkje kallast inn til hovudforhandlinga når retten held nytt avhøyr for uturvande og partane ikkje krev nytt avhøyr.""",
        "hva_betyr_html": """<p>I rettssaker har vi en generell regel i Norge (tvisteloven § 22-9) som sier at du ikke trenger å svare på et spørsmål hvis svaret vil føre til at du mister "sosialt omdømme". Målet er at staten ikke skal tvinge deg til å henge deg selv ut foran alle for ting som er ekstremt skamfullt, men ikke ulovlig.</p>
<p>Men i farskapssaker setter loven denne regelen helt til side. Barnets rett til å få vite hvem faren er, veier tyngre enn de voksnes behov for å skjule sine feiltrinn. Det betyr at hvis du hadde en affære med naboen mens mannen din var på jobb, eller hvis du som mann lå med broren din sin kone, så kan du bli spurt om dette direkte av dommeren. Og du har forklaringsplikt. Nekter du å svare, eller lyver du, kan du straffes for falsk forklaring eller forakt for retten. Du avgir forklaringen din under vitneansvar.</p>
<p>Fordi slike saker er følelsesladde og vonde, gir det andre leddet dommeren lov til å kaste den ene parten på gangen mens den andre snakker. Kanskje tør ikke mor å fortelle detaljene hvis mannen hun var utro mot stirrer på henne. Da kan dommeren be ham vente utenfor.</p>""",
        "eksempler": [{"navn": "Eva og svigerbror", "tekst": "Eva er gift med Lars. Hun får et barn, men mistenker at barnet egentlig tilhører Lars sin bror, Petter, etter et feiltrinn på en hyttetur. Lars krever farskapssak da han ser at barnet ikke ligner. I retten spør dommeren Eva rett ut om hun har hatt samleie med Petter. Eva synes dette er så skamfullt at hun nekter å svare for å beskytte familiens ære. Dommeren minner henne på barneloven § 21. Eva kan ikke beskytte sitt sosiale omdømme her. Hun må svare ærlig for at retten skal kunne opplyse saken, ellers risikerer hun straff."}],
        "vanlige_feil": ["Lyve i retten for å skjule utroskap. (Dette er straffbart som mened/falsk forklaring, og DNA vil uansett avsløre sannheten til slutt).", "Tro at man kan påberope seg \"retten til å ikke inkriminere seg selv\" for ting som bare er flaut. Det gjelder bare for straffbare forhold, og utroskap er ikke straffbart."],
        "hva_bor_du_html": "<p>Hvis du skal vitne eller forklare deg i en farskapssak, forbered deg på at dommeren og advokatene vil stille nærgående, intime spørsmål om nøyaktig når du hadde sex og med hvem. Pust med magen og svar ærlig. Saken går for lukkede dører, noe som betyr at publikum og presse ikke er til stede. Det som sies i rommet, blir mellom dommeren og partene.</p>",
        "dumme_sporsmal": [
            {"q": "Må jeg sitte i samme rom som overgriperen min for å forklare meg?", "a": "Nei. Hvis barnet ble til ved en voldtekt eller overgrep, eller hvis du er redd for mannen, vil dommeren bruke regelen i andre ledd til å sørge for at du får forklare deg alene. Mannen vil få referert hva du har sagt i etterkant, slik at rettssikkerheten hans er ivaretatt."},
            {"q": "Kan jeg straffes hvis jeg sier jeg ikke husker hvem jeg lå med?", "a": "Hvis du oppriktig ikke husker, for eksempel på grunn av rus, kan du naturligvis si det. Men lyver du om at du ikke husker, og retten senere finner bevis (for eksempel meldinger der du diskuterer det), kan du bli straffeforfulgt for å ha løyet i retten."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "24", "tittel": "hvordan retten også kan tvinge deg til å avgi DNA", "available": True},
            {"lov": "barnelova", "paragraf": "17", "tittel": "om hvem som regnes som \"part\" i saken", "available": True},
        ],
    },
    {
        "number": "23",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Saken fortsetter selv om du nekter å møte opp",
        "kategori": "familie",
        "description": "Tror du at en rettssak forsvinner hvis du bare ignorerer innkallingen og blir hjemme under dyna? I farskapssaker kjører dommeren saken uansett.",
        "kort_svar": "Farskapssaken stopper ikke opp selv om du nekter å møte i retten. Hvis én eller alle partene velger å ikke dukke opp, fortsetter dommeren behandlingen og avsier dom basert på de bevisene (som DNA og tidligere forklaringer) som allerede finnes i mappen.",
        "paragraftekst": """Saka stoggar ikkje om nokon av partane eller alle partar let vere å møte.

Forklaring som er gjeve under saksførebuinga, kan lesast opp under hovudforhandlingane der vedkomande ikkje møter, om ikkje særlege grunnar taler mot.""",
        "hva_betyr_html": """<p>Å spille struts fungerer ikke i rettssystemet. Hvis NAV har sendt saken din til tingretten, og du får en innkalling til hovedforhandling (selve rettssaken), er det ditt ansvar å møte opp.</p>
<p>Noen menn tror at hvis de bare nekter å delta, så kan ikke retten bevise noe, og da slipper de unna barnebidrag. Dette avkrefter § 23 fullstendig. Loven sier i klartekst at "saka stoggar ikkje" (saken stopper ikke). Hvis du lar være å møte, mister du rett og slett bare muligheten til å forsvare deg. Dommeren vil ta avgjørelsen uansett.</p>
<p>Har du tidligere i prosessen forklart deg til NAV eller sendt inn et brev til domstolen, vil dommeren lese opp dette under rettsmøtet og bruke det som bevis, selv om du ikke er i rommet for å utdype det.</p>""",
        "eksempler": [{"navn": "Marius", "tekst": "Marius er stevnet som mulig far til Saras barn. Han nekter å godta dette og vil straffe Sara ved å ignorere hele prosessen. På dagen for rettssaken blir Marius hjemme og spiller TV-spill. Dommeren noterer at Marius er fraværende, men fortsetter saken med Sara. Siden DNA-testen fra NAV allerede ligger i saksmappen og viser at Marius er faren, avsier dommeren en dom som gjør Marius til juridisk far. Han får dommen tilsendt i posten noen dager senere."}],
        "vanlige_feil": ["La være å møte opp i retten fordi du vet du kommer til å tape og ikke orker ubehaget. (Du mister da sjansen til å ha innflytelse på saken).", "Tro at en uteblivelse betyr at saken blir henlagt på bevisets stilling."],
        "hva_bor_du_html": "<p>Møt opp når domstolen innkaller deg. Er du syk, må du skaffe en legeerklæring (sykmelding for retten) og sende den inn umiddelbart, slik at dommeren kan utsette saken. Uten gyldig fravær kjører toget uten deg.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om ingen av partene møter opp?", "a": "Da skjer akkurat det samme. Saken stopper ikke selv om \"alle partar let vere å møte\". Er det en DNA-test i mappen, vil dommeren avsi dom basert på den. Uten bevis kan saken i verste fall bli avvist, og barnet blir stående uten far — men retten vil gjøre alt for å unngå det."},
            {"q": "Kan jeg anke dommen hvis jeg ikke møtte?", "a": "Ja, du har fremdeles rett til å anke dommen til lagmannsretten innen fristen (vanligvis én måned), men du har satt deg selv i en veldig dårlig posisjon ved å ignorere første runde."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "25", "tittel": "hvordan dommeren kan droppe rettsmøtet helt hvis DNA er klart", "available": True},
            {"lov": "barnelova", "paragraf": "24", "tittel": "hvis du ikke har gitt DNA ennå, kan politiet hente deg", "available": True},
        ],
    },
    {
        "number": "24",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Domstolen kan bruke politiet for å hente DNA-et ditt",
        "kategori": "familie",
        "description": "Nekter du å ta DNA-test i en farskapssak? Dommeren kan beordre politiet til å pågripe deg og kjøre deg til legen med makt. Også døde fedre kan testes.",
        "kort_svar": "I en farskapssak har domstolen makt til å tvinge frem en DNA-test. Nekter en mann, en mor eller et barn å møte frivillig for å la seg teste, kan dommeren skrive en kjennelse som ber politiet hente dem med makt. Retten kan også kreve utlevert medisinsk vev fra en avdød mann for å teste DNA-et hans.",
        "paragraftekst": """Retten kan gje mora, barnet og kvar mann som er part i saka, pålegg om å gje frå seg ei eigna prøve til DNA-analyse. Er det grunn til å tru at ein mann som ikkje er part, har hatt samlege med mora på den tid ho kan ha blitt med barnet, kan retten vedta slik gransking også hos han når han først har fått sagt si meining. Kommunelækjaren peiker ut ein lækjar som har plikt til å ta dei prøvene som trengst.

Er ein som kan vere far til barnet død eller utilgjengeleg av annan grunn, kan retten som prov i ei farskapssak innhente og gjere bruk av biologisk materiale eller prøver som tidlegare er tatt av han.

Departementet kan ved forskrift gje utfyllande reglar om innhenting og bruk av slikt materiale.

Lèt nokon vere å rette seg etter påbod etter første stykket eller § 11 første stykket om å kome sjølv eller med barn vedkomande har omsorg for, til prøvetaking og DNA-analyse, kan retten i orskurd vedta at vedkomande skal gripast av politiet og førast til lækjar for prøvetaking.""",
        "hva_betyr_html": """<p>Paragraf 24 er musklene i barneloven. Siden rettssikkerheten til barnet (å få vite hvem far er) trumfer voksnes uvilje, har domstolen fått svært inngripende verktøy.</p>
<p>Første ledd gir dommeren lov til å beordre alle involverte parter til å ta en DNA-test. Selv menn som bare er "mistenkt" for å være faren, men som ikke formelt er dratt inn som part ennå, kan tvinges til å avgi DNA, så lenge de får uttale seg først. Kommunelegen har ansvaret for å peke ut en lege som <em>må</em> ta disse testene.</p>
<p>Andre ledd løser et klassisk problem: Hva om den mulige faren er død? DNA forsvinner ikke ved døden. Har mannen tidligere vært på sykehus for en operasjon, for å ta blodprøver, eller en biopsi, kan sykehuset ha lagret biologisk materiale (vev eller blod) fra ham i sine arkiver. Loven gir da dommeren rett til å overstyre taushetsplikten og beordre sykehuset til å utlevere dette vevet. Slik kan farskapet fastslås lenge etter mannens død, noe som ofte er kritisk for at barnet skal få sin rettmessige arv.</p>
<p>Fjerde ledd er det mest dramatiske. Hva skjer hvis en mann — eller en mor med babyen sin — får et pålegg om å møte hos legen for DNA-test, men bare ignorerer det? Da kan retten beslutte ("i orskurd") at politiet skal gripe inn. Politiet drar da hjem til personen, pågriper vedkommende, setter dem i politibilen og kjører dem rett til legen. Der må de sitte til legen har fått tatt en spyttprøve eller blodprøve.</p>""",
        "eksempler": [{"navn": "Johans motstand", "tekst": "Sara går til sak mot Johan. Dommeren beordrer DNA-test, men Johan dukker ikke opp på legekontoret de tre gangene han får time. Han svarer heller ikke på telefon. Dommeren blir lei og fatter en kjennelse om tvangsmessig fremstilling. To dager senere banker politiet på døren på Johans arbeidsplass. De forteller sjefen at Johan må bli med dem. Johan blir kjørt bak i en politibil til kommunelegen, hvor det blir tatt en spyttprøve, før han slippes fri. Testen viser at Johan er faren."}],
        "vanlige_feil": ["Tro at man kan \"unnslippe\" farskap ved å flykte fra NAVs DNA-krav. Domstolen og politiet finner deg til slutt.", "Mor som nekter å ta med barnet til test fordi hun hater faren. Politiet kan hente både mor og baby og kjøre dem til sykehuset.", "Tro at kremasjon sletter alt bevis. Selv om faren er kremert, finnes det nesten alltid prøver lagret i en sykehusfryser hvis han noen gang har vært innlagt for sykdom."],
        "hva_bor_du_html": "<p>Får du et pålegg fra retten om å avgi DNA, så møt opp frivillig. Prosessen hos legen tar fem minutter (ofte bare en vattpinne i munnen). Venter du til politiet henter deg, oppnår du ingenting annet enn at prosessen blir dypt ydmykende for deg selv, naboene ser politiet, og du mister kontrollen.</p>",
        "dumme_sporsmal": [
            {"q": "Gjør det vondt å ta prøven? Må jeg gi blod?", "a": "Nei, standard prosedyre for farskapstester i dag er å stryke en vattpinne mot innsiden av kinnet for å samle spytt og celler (munnavskrap). Det er helt smertefritt. Blodprøver brukes bare unntaksvis hvis spyttprøve ikke er mulig eller ikke gir godt nok resultat."},
            {"q": "Kan politiet holde meg i fengsel hvis jeg fremdeles nekter å åpne munnen hos legen?", "a": "Loven gir rett til å gripe deg og føre deg til legen. I praksis er det svært sjelden politiet må bruke fysisk makt (f.eks. bende opp munnen din). Alvoret av å sitte på et legekontor med to politifolk pleier å overbevise de aller fleste om at det er best å samarbeide."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "11", "tittel": "første runde med frivillig DNA-krav fra NAV", "available": True},
            {"lov": "barnelova", "paragraf": "25", "tittel": "hva dommeren gjør i det øyeblikket DNA-testen er klar", "available": True},
        ],
    },
    {
        "number": "25",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Retten kan dømme raskt når DNA-beviset er klart",
        "kategori": "familie",
        "description": "Har DNA-testen gitt et klart svar? Da trenger dere ikke møtes i retten for en langvarig rettssak. Dommeren kan felle dom skriftlig og avslutte saken.",
        "kort_svar": "Når en DNA-test med sikkerhet utpeker en mann som far, eller fullstendig utelukker ham, kan dommeren avsi dom uten å holde en hovedforhandling (rettssak i en rettssal). Partene får bare en frist til å sende inn en siste kommentar, og så avgjøres saken på papiret.",
        "paragraftekst": """Retten kan seie dom i farskapssak utan hovudforhandling når ein DNA-test anten utpeikar ein mann som far eller viser at han ikkje kan vere far til barnet, likevel slik at partane skal få høve til å uttale seg om føresetnaden for å seie dom utan at hovudforhandling ligg føre.

Med samtykke frå mor til barnet kan retten gje frifinningsdom for alle menn som er partar i saka, når retten etter at gransking av blodprøver og forklaring frå partar og vitne er tilendeført, finn det klart at det ikkje let seg gjere å gje dom for farskap.""",
        "hva_betyr_html": """<p>En vanlig rettssak er dyr og tidkrevende. Man må kalle inn vitner, advokater skal snakke, og alle må sitte i rettssalen en hel dag. I gamle dager, før DNA fantes, var dette nødvendig i farskapssaker for å kryssforhøre folk om hvem som hadde ligget med hvem.</p>
<p>I dag er det annerledes. Når rettsmedisinerne leverer en DNA-analyse som sier at det er 99,99 % sikkert at mannen er far (eller 0 % sjanse for at han er det), har verken mannen eller moren noe de skulle ha sagt som kan endre på det beviset.</p>
<p>Derfor sier loven at dommeren kan slå klubba i bordet og skrive dommen "utan hovudforhandling" – altså uten at partene møtes i retten. Dette kalles en forenklet domsbehandling.</p>
<p>Før dommeren gjør dette, må han sende et brev til partene: "Jeg har DNA-testen, og planlegger å avsi dom basert på den. Dere har én uke på å protestere hvis dere mener det har skjedd noe teknisk feil med testen." Har ingen noe fornuftig å komme med, faller dommen skriftlig.</p>
<p>Det andre leddet handler om "håpløse" saker. Hvis retten har testet alle de mulige mennene mor har oppgitt, og alle testene er negative (ingen er faren), og det ikke finnes flere spor å gå etter, kan dommeren frifinne alle mennene og avslutte saken. Dette krever at mor samtykker i at man gir opp jakten.</p>""",
        "eksempler": [{"navn": "Lasse gir opp", "tekst": "NAV sendte farskapssaken til tingretten fordi Lasse nektet å signere frivillig. I tingretten ble Lasse beordret til å ta en DNA-test. To uker senere dumper resultatet ned på dommerens pult. Det viser at Lasse er far. Dommeren sender et brev til Lasse: \"Retten vil dømme deg som far uten rettsmøte basert på dette beviset.\" Lasse innser at løpet er kjørt, og svarer ikke på brevet. Uken etter får han selve dommen i posten, og barnebidraget begynner å løpe. Han slapp å møte opp i retten for å tape saken."}],
        "vanlige_feil": ["Bli overrasket over å få en dom i posten uten å ha vært i rettssalen (dette er standard prosedyre når DNA-et er testet og levert).", "Protestere til dommeren på manglende rettssak med argumentet \"men hun sa at hun brukte p-piller\". (Hvordan barnet ble til er irrelevant for farskapet, så lenge DNA-et stemmer. Retten vil avvise protesten)."],
        "hva_bor_du_html": "<p>Når DNA-beviset foreligger og du får varsel om dom uten hovedforhandling, bør du lese varselet nøye. Med mindre du mistenker at sykehuset har forvekslet blodprøvene, eller at du har en enegget tvillingbror som kan være faren, har det ingen hensikt å bruke tusenvis av kroner på en advokat for å kreve en full rettssak. Det endelige resultatet vil bli nøyaktig det samme. Aksepter dommen skriftlig, så blir du ferdig med det.</p>",
        "dumme_sporsmal": [
            {"q": "Hva hvis mor fremdeles mener jeg er faren selv om DNA-testen utelukker meg?", "a": "Det spiller ingen rolle hva hun mener. Hvis den vitenskapelige analysen viser at du ikke er faren, vil dommeren bruke § 25 til å avsi en frifinnende dom for deg uten rettssak, og saken mot deg er overstått en gang for alle."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "9", "tittel": "lovens absolutte krav til at DNA skal avgjøre saken", "available": True},
            {"lov": "barnelova", "paragraf": "26", "tittel": "andre måter retten kan avslutte saken på", "available": True},
        ],
    },
    {
        "number": "26",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Når domstolen kan heve farskapssaken",
        "kategori": "familie",
        "description": "En farskapssak for domstolen kan noen ganger bare legges død før dom faller. Loven gir dommeren lov til å heve saken i to spesifikke tilfeller.",
        "kort_svar": "Dommeren kan avslutte (heve) farskapssaken uten en dom dersom mannen plutselig ombestemmer seg og signerer farskapserklæringen frivillig underveis i prosessen. Retten kan også heve saken hvis mannen bor i utlandet og det er umulig å få tak i nok informasjon til å bevise noe som helst.",
        "paragraftekst": """Retten kan heve saka i orskurd når
a. ein mann erklærer i samsvar med § 4 at han er far til barnet, eller
b. den oppgjevne faren bur i utlandet og det er uråd å få nok opplysningar til å fastsetje farskapen.""",
        "hva_betyr_html": """<p>Å "heve saken" betyr at retten bare stryker den fra listene sine, pakker bort papirene og sender alle hjem. Det felles ingen dom, og staten gir opp saken (i alle fall for denne gang).</p>
<p>Loven tillater dette i to praktiske situasjoner: <strong>1. Mannen kaster inn håndkleet (bokstav a).</strong> Kanskje nektet han å snakke med NAV, slik at NAV måtte saksøke ham. Når han får papirene fra tingretten og innser at dommeren vil tvinge ham til DNA-test, tenker han "greit, det er mitt barn". Da kan han logge inn på nett eller møte hos NAV og signere erklæringen formelt, slik han burde ha gjort fra starten. Når retten ser at papirene er signert, hever de saken fordi problemet er løst frivillig.</p>
<p><strong>2. Håpløse utenlandssaker (bokstav b).</strong> Noen ganger har kvinnen blitt gravid med en mann som bor i et annet land, kanskje på et ferieopphold eller en som har flyttet hjem igjen. Hvis norske domstoler prøver å kontakte mannen, men myndighetene i landet hans nekter å samarbeide, eller det er umulig å spore ham opp for å ta DNA, blir saken stående i stampe. Hvis det vurderes som helt umulig å samle nok bevis (kalt "uråd å få nok opplysningar"), kan dommeren velge å heve saken. Barnet blir da stående med "far ukjent".</p>""",
        "eksempler": [{"navn": "Jonas gir seg", "tekst": "Jonas nektet plent på at barnet var hans da NAV spurte. Saken havnet i retten. Men etter å ha snakket med advokaten sin og fått høre at politiet kunne hente ham med makt for DNA-testing, drar Jonas til NAV-kontoret. Han viser ID og signerer på at han er faren, og mor godtar det skriftlig. NAV melder fra til tingretten. Dommeren skriver en kjennelse (orskurd) om at farskapssaken er hevet, siden farskapet nå er etablert frivillig."}],
        "vanlige_feil": ["Mor tror hun kan droppe rettssaken bare fordi hun vil, ved å be dommeren heve saken. (Saken heves ikke bare fordi mor trekker seg; staten har ansvar for at barnet får en far).", "Faren tror at en hevet sak fra utlandet betyr at han er \"frikjent\". (Nei, saken er bare lagt på is. Flytter han noen gang til Norge og kan testes, kan saken gjenopptas)."],
        "hva_bor_du_html": "<p>Hvis du er saksøkt i en farskapssak og innser at du faktisk er faren, sparer du samfunnet og deg selv for mye tid ved å signere erklæringen raskest mulig (etter § 4). Da vil retten heve saken. Du slipper rettsmøter og du slipper et formelt domspapir på at du ble tvunget.</p>",
        "dumme_sporsmal": [
            {"q": "Hvis retten hever saken fordi faren bor i utlandet, får jeg barnebidrag fra noen andre?", "a": "Nei, du får ikke bidrag fra faren. Du kan ha rett på utvidet barnetrygd og eventuelt barnebidragsforskudd fra NAV fordi du er enslig forsørger med ukjent far, men selve jakten på den biologiske faren stanser."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "4", "tittel": "reglene for hvordan man frivillig erklærer farskap", "available": True},
            {"lov": "barnelova", "paragraf": "25", "tittel": "hvis han ikke signerer frivillig, feller dommeren dom istedenfor å heve saken", "available": True},
        ],
    },
    {
        "number": "27",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "En farsskapsdom gjelder for alle og overalt",
        "kategori": "familie",
        "description": "Når en domstol har slått fast hvem som er far, er det fasiten. Dommen binder alle samfunnets organer, fra Folkeregisteret og Skatteetaten til arv og bidrag.",
        "kort_svar": "Når en farskapssak er avgjort med en endelig dom i retten, gjelder denne avgjørelsen for absolutt alle — ikke bare for mor og far. Alle offentlige etater, domstoler, familiemedlemmer og arvinger må legge dommen til grunn som den absolutte sannheten.",
        "paragraftekst": "Ein rettskraftig dom i ei farskapssak gjeld for og mot alle og skal leggjast til grunn i alle tilhøve der farskapen har noko å seie.",
        "hva_betyr_html": """<p>I vanlig juss gjelder ofte en dom bare mellom de to personene som saksøkte hverandre (A og B). Hvis A vinner over B om hvor gjerdet skal stå, er det ikke sikkert at C er bundet av dommen.</p>
<p>Men farskap er annerledes. Når en dommer etter en DNA-test konkluderer med at "Marius er far til barnet" og ankefristen har gått ut (dommen er "rettskraftig"), blir dette et magisk dokument. Paragraf 27 slår fast at dommen har "utvidet rettskraft". Den binder hele samfunnet.</p>
<p>Det betyr at Marius ikke lenger kan diskutere dette med NAV når de krever barnebidrag. Han kan ikke be Skatteetaten la være å føre ham opp. Hvis Marius senere dør, kan ikke de andre barna hans nekte det nye barnet arv med begrunnelsen "vi tror ikke på dommen". Dommen trumfer alle tvil, i alle situasjoner, for alle myndigheter. Staten har fått en fasit.</p>
<p>Loven sier "gjeld for og mot alle". Det betyr at om du ble frikjent (dommen sa at du <em>ikke</em> var faren), så er også det et skjold som beskytter deg mot fremtidige anklager fra mor, barnet eller det offentlige.</p>""",
        "eksempler": [{"navn": "Skifteoppgjøret", "tekst": "Jonas ble dømt til å være far til Lise i en rettssak i 2015, basert på DNA. Han hadde ingen kontakt med Lise. I 2024 dør Jonas. Jonas sine foreldre er rike og etterlater seg mye penger, og når Jonas er død, skal Jonas sine barn arve sine besteforeldre. Resten av familien vil kaste Lise ut av arveoppgjøret, og hevder de har funnet brev som viser at mor løy. Dommeren i skifteretten ser på dommen fra 2015. Dommeren henviser til § 27: Dommen fra 2015 gjelder for og mot alle. Lise er Jonas sin datter. Familien kan ikke rippe opp i farskapet her. Lise får arven sin."}],
        "vanlige_feil": ["Tro at man kan overbevise NAV om å stoppe barnebidraget ved å hevde at \"domstolen gjorde en feil\". (NAV har ikke lov til å overprøve dommen, de *skal* legge den til grunn).", "Tro at en frifinnende dom bare gjelder mot den ene mora som saksøkte deg (den gjelder for alle, ingen kan saksøke deg for det samme barnet igjen)."],
        "hva_bor_du_html": "<p>Dersom du mottar en dom fra tingretten i en farskapssak, og du mener dommen er feil (for eksempel fordi sykehuset åpenbart har byttet om på prøvene, eller loven er brukt feil), MÅ du anke dommen før fristen går ut, vanligvis én måned. Så snart ankefristen utløper, smeller fellen igjen, og dommen blir låst (\"rettskraftig\"). Da gjelder den for resten av livet ditt.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om jeg finner ut 10 år etter dommen at sykehuset forfalsket DNA-prøven min?", "a": "Siden dommen er rettskraftig, kan du ikke bare starte en ny, vanlig farskapssak. Du må be om noe som heter *gjenåpning* av den gamle saken. Dette er svært vanskelig og krever tungtveiende, nye bevis (som bevis på at sykehuset forfalsket prøven). Se lovens § 28 a for reglene om gjenåpning."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "28", "tittel": "hvordan du klager (anker) før dommen blir endelig", "available": True},
            {"lov": "barnelova", "paragraf": "8", "tittel": "domstoler i andre saker kan ikke prøve farskapet på nytt", "available": True},
        ],
    },
    {
        "number": "28",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Slik fungerer anke i en farskapssak",
        "kategori": "familie",
        "description": "Er du uenig i dommen fra tingretten? Du kan anke til lagmannsretten. Slik avgjør loven hvem som blir med videre til neste instans.",
        "kort_svar": "Når en farskapssak blir anket fra tingretten til lagmannsretten, blir alle partene i utgangspunktet med videre som parter. Unntaket er en mann som tingretten frifant (f.eks. med DNA): Han får slippe å være med i ankesaken, med mindre han uttrykkelig blir trukket inn igjen.",
        "paragraftekst": "Alle partane i saka på første rettssteget held fram å vere partar i ankesaka. Den som er frifunnen etter § 25 første stykket, er likevel berre part når retten eller nokon av dei andre partane dreg han inn i saka. Tyder opplysningar som kjem fram i ankesaka på at nokon annan kan vere faren, skal retten anten gjere han til part i prosesskrift eller oppheve dommen og sende saka til ny forhandling i tingretten.",
        "hva_betyr_html": """<p>Når tingretten har sagt sitt (første rettsinstans), kan den som taper velge å anke saken inn for lagmannsretten.</p>
<p>Normalt er det slik at de samme personene som sloss i tingretten, fortsetter krangelen i lagmannsretten. Barneloven gjør et praktisk unntak for å skåne menn som allerede er fullstendig utelukket.</p>
<p>Tenk deg at Trine saksøkte både Ola og Per i tingretten for å finne faren. DNA-testen i tingretten utelukket Ola 100 %. Dommeren frifant Ola etter § 25, og dømte Per som far. Per er uenig og anker dommen til lagmannsretten fordi han mener blodprøven hans var forurenset.</p>
<p>I dette tilfellet sier paragraf 28 at Ola ikke trenger å være part i ankesaken. Han er sjekket ut av saken. Lagmannsretten vil behandle saken mellom Trine og Per. Ola kan slappe av hjemme. Men hvis Per i anken sin skriver: "Ola byttet blodprøven min med sin, han må tilbake inn i saken!", kan lagmannsretten beslutte å dra Ola inn som part igjen.</p>
<p>Loven sier også at hvis det under forberedelsene i lagmannsretten dukker opp opplysninger om en helt <em>tredje</em> mann som ingen visste om, kan lagmannsretten velge mellom to ting: De kan trekke ham direkte inn som part i saken sin, eller de kan kaste hele dommen fra tingretten i søpla (oppheve den) og kommandere tingretten til å kjøre hele saken på nytt fra starten av, nå med den nye mannen inkludert.</p>""",
        "eksempler": [{"navn": "Anken uten Pål", "tekst": "Saken mellom mor, Pål (mulig far 1) og Knut (mulig far 2) gikk for tingretten. DNA-testen utelukket Pål helt, og Knut nektet å ta testen. Tingretten frifant Pål og dømte Knut som far etter vitnebevis. Knut anker dommen. Siden Pål ble frikjent i første runde og anken kun handler om Knuts oppførsel, deltar ikke Pål i ankesaken for lagmannsretten. Han får et brev om at han ikke lenger er part."}],
        "vanlige_feil": ["En frikjent mann tror han må bruke tusenvis av kroner på advokat i ankesaken, selv om han ble utelukket av DNA i tingretten (han slipper).", "Du anker og glemmer å be om at en spesifikk mann dras inn igjen, og blir overrasket over at han ikke er med."],
        "hva_bor_du_html": """<p>Har du vunnet i tingretten og DNA-et sier at du <em>ikke</em> er faren? Da kan du i utgangspunktet ignorere ankesaken mellom de andre, så fremt du ikke mottar et formelt prosesskriv fra domstolen om at du er stevnet på ny. Er du i tvil, be advokaten din bekrefte om du er "ute" av saken.</p>
<p>Skal du anke fordi du mener en <em>annen</em> spesifikk mann er faren, må du sørge for at anken din (gjennom advokaten) retter seg eksplisitt mot å få ham dratt inn som part.</p>""",
        "dumme_sporsmal": [
            {"q": "Hvor lang er ankefristen?", "a": "Ankefristen er vanligvis én måned fra den dagen dommen fra tingretten ble forkynt (levert) for deg. Etter dette blir dommen endelig (rettskraftig). Fristene styres av tvisteloven, og det er ekstremt viktig å overholde dem."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "25", "tittel": "frifinnelse basert på DNA (som gjør at du slipper å bli med i anken)", "available": True},
            {"lov": "barnelova", "paragraf": "27", "tittel": "hva som skjer hvis ingen anker (dommen blir endelig)", "available": True},
        ],
    },
    {
        "number": "28a",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Gjenåpning av gamle farskapssaker med DNA",
        "kategori": "familie",
        "description": "Ble du dømt som far før DNA-testen fantes? Loven gir deg en særskilt rett til å få gjenåpnet gamle rettssaker for å bevise at du er uskyldig.",
        "kort_svar": "Hvis du ble dømt (eller frikjent) i en farskapssak i en tid der det ikke ble tatt DNA-test (før teknologien kom, eller det bare ble tatt blodtype-test), kan du kreve at saken gjenåpnes i domstolen. De vanlige tidsfristene for å gjenåpne gamle saker gjelder ikke her.",
        "paragraftekst": """Dersom det ikkje låg føre ein DNA-analyse i saka, kan ei rettskraftig avgjerd krevjast gjenopna utan omsyn til vilkåra i tvisteloven §§ 31-3 til 31-6. Vert det kravd gjenopning, skal retten gje pålegg om blodprøve og DNA-analyse. Når DNA-analysen ligg føre, gjeld regelen i § 25 første stykket.

I andre farskapssaker gjeld ikkje fristen i tvisteloven § 31-6 andre stykket for å krevje gjenopning av saka.""",
        "hva_betyr_html": """<p>Normalt kan du ikke rive opp i gamle dommer. Hvis du tapte i tingretten i 1985 og ikke anket, er du låst for alltid. Det norske rettssystemet (tvisteloven) har strenge frister (vanligvis maksimum 10 år) for når du kan be om "gjenåpning" av en lukket rettssak, uansett hvilke nye bevis du finner.</p>
<p>Men farskapssaker fra 1970-, 80- og tidlig 90-tall ble ofte avgjort på usikkert grunnlag. Menn ble dømt til å betale barnebidrag i 18 år utelukkende fordi blodtypen deres ikke passet helt dårlig, og fordi mor gråtende sverget i vitneboksen på at han var den eneste. Mange av disse mennene visste de var uskyldige. Da DNA-testen revolusjonerte bevisføringen, måtte Stortinget la dem rydde opp.</p>
<p>Paragraf 28 a sier at hvis det <em>ikke</em> forelå en DNA-test i den opprinnelige dommen fra retten, kan du når som helst kreve dommen gjenåpnet for å få tatt en DNA-test. 10-årsfristen fra tvisteloven er visket ut. Du kan be om gjenåpning i 2025 for en dom fra 1982.</p>
<p>Når du krever dette, har dommeren plikt til å beordre en DNA-test av deg, mor og det nå voksne barnet. Viser det seg at DNA-et utelukker deg, avsier dommeren raskt en ny dom der du blir slettet som far (frifunnet).</p>
<p>I det andre leddet gjør loven også en viktig presisering: Selv for andre farskapssaker (for eksempel saker hvor det kanskje <em>ble</em> tatt DNA, men hvor laboratoriet gjorde en skandale-feil), gjelder ikke den absolutte ti-årsfristen. Man kan rette opp feil farskap uansett hvor gammel dommen er.</p>""",
        "eksempler": [{"navn": "Kåres kamp", "tekst": "I 1984 ble Kåre dømt til å være far til Stian. Kåre nektet, men blodprøven (som ikke var DNA) viste ingenting annet enn at han hadde blodtype A, akkurat som Stian. Kåre betalte bidrag og levde med skammen, selv om han var sikker på at en av Karis andre kjærester var faren. I 2024, 40 år senere, sender Kåre et krav om gjenåpning av saken til tingretten og viser til § 28 a. Retten beordrer Stian (nå 40 år) og Kåre til å avgi DNA. Svaret fra sykehuset er krystallklart: Kåre er *ikke* faren. Tingretten gjenåpner dommen fra 1984 og frifinner Kåre."}],
        "vanlige_feil": ["Menn som betalte bidrag på 80-tallet og tror de for alltid er stemplet som far, og at tidsfristen gikk ut.", "Et voksent barn krever gjenåpning for å fjerne arven fra sin \"feilaktige\" far, men nekter selv å ta DNA-testen for å bevise det. (Retten krever at DNA-analyse skal gjennomføres)."],
        "hva_bor_du_html": "<p>Ble du dømt som far uten DNA-bevis? Du må sende en \"begjæring om gjenåpning\" til den tingretten som avsa den opprinnelige dommen. Det koster et rettsgebyr å sende inn. Bruk en advokat. I brevet påpeker du at dommen fra den gang manglet DNA-bevis, og at du krever at saken gjenåpnes etter barnelova § 28 a for at DNA-test kan foretas.</p>",
        "dumme_sporsmal": [
            {"q": "Hva skjer med barnebidraget jeg betalte på 80-tallet hvis jeg blir frikjent i dag?", "a": "Du kan ha rett på å kreve tilbakebetalt bidraget fra Folketrygden hvis det er åpenbart at du ikke burde vært dømt og du hadde god grunn til å kjempe mot det (se § 80). Men på grunn av foreldelsesregler og komplisert jus for tilbakevirkende kraft mange tiår senere, er det ikke garantert at du får tilbake alle pengene med renter. Advokaten din vil måtte fremme et erstatningskrav mot NAV."},
            {"q": "Kan barnet (som i dag er voksent) nekte å ta DNA-testen?", "a": "Ja, et voksent barn kan fysisk nekte. Men hvis barnet nekter å rette seg etter rettens pålegg om å avgi DNA-prøve i en gjenåpningssak, vil domstolen ofte vurdere dette til Kåres (den opprinnelige farens) fordel, og i ytterste konsekvens omgjøre dommen uten testen, basert på vegring. Men i praksis beordrer retten DNA, og kan til og med bruke politiet (se § 24)."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "25", "tittel": "domsbehandling uten rettssak når DNA-et omsider kommer", "available": True},
            {"lov": "barnelova", "paragraf": "80", "tittel": "tilbakebetaling av urettmessig barnebidrag", "available": True},
        ],
    },
    {
        "number": "29",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Staten betaler for farskapssaken i retten",
        "kategori": "familie",
        "description": "Hvem betaler regningen når en farskapssak havner i retten? Heldigvis sier loven at staten tar kostnadene for de bevisene retten trenger, som DNA-tester.",
        "kort_svar": "I en farskapssak skal staten dekke de utgiftene som domstolen har for å finne ut hvem som er faren. Dette inkluderer kostnader til blant annet DNA-tester, vitner retten kaller inn, og eventuelle sakkyndige.",
        "paragraftekst": "Staten ber den kostnaden som retten har med saka, også kostnaden med å få tak i opplysningar som retten finn naudsynte.",
        "hva_betyr_html": """<p>I vanlige sivile rettssaker (for eksempel hvis du saksøker naboen for å ha bygget garasjen for nær tomtegrensen), gjelder prinsippet om at "taperen betaler alt". Den som taper saken, må betale både sine egne og vinnerens advokatutgifter, samt alle gebyrer til retten.</p>
<p>Siden samfunnet har en overordnet interesse av at barn får riktig juridisk far (og for å sikre barnebidrag), ville det vært urettferdig om en blakk mor eller en uskyldig anklaget mann ble ruinert av rettssaken.</p>
<p>Derfor har vi § 29. Den sier at staten tar regningen for selve opplysningen av saken. Hvis dommeren beordrer tre menn, moren og barnet til å ta DNA-test hos legen, er det staten som betaler for legetimene og analysen på laboratoriet. Hvis dommeren må bruke penger på å finne en forsvunnet person (for eksempel en annonse i avisen), er det også staten som tar regningen.</p>""",
        "eksempler": [{"navn": "Karis mange mistenkte", "tekst": "Kari har gått til sak mot både Geir og Thomas. Retten krever DNA-tester av alle. Begge mennene tester negativt. Retten graver videre og finner en tredje mann, Pål, som også blir testet på statens regning. Totalt sett har DNA-testene, brev og innkallinger kostet titusener av kroner. Hverken Kari, Geir, Thomas eller Pål får fakturaen for dette i posten. Staten betaler, fordi det var nødvendig for retten å finne sannheten."}],
        "vanlige_feil": ["Tro at du må betale tusenvis av kroner for DNA-testen hvis du taper saken.", "Tro at \"staten betaler alt\" også betyr at staten betaler for den dyreste advokaten du kunne finne (staten betaler bare for *rettens* utgifter)."],
        "hva_bor_du_html": "<p>Du trenger ikke bekymre deg for kostnadene til DNA eller rettens saksbehandling. Det går av seg selv. Men du må være oppmerksom på advokatutgiftene (se \"Dumme spørsmål\").</p>",
        "dumme_sporsmal": [
            {"q": "Betyr dette at staten betaler advokaten min?", "a": "Nei, § 29 gjelder ikke advokatutgifter. Loven dekker \"den kostnaden som retten har med saka\". Advokaten din er *din* kostnad, ikke rettens. Skal du få staten til å betale advokaten din, må du søke om fri rettshjelp hos Statsforvalteren. Farskapssaker gir ofte rett til fri rettshjelp, men bare hvis du tjener under en viss grense. Tjener du mye, må du betale advokaten din selv, selv om du er helt uskyldig i anklagen."},
            {"q": "Hva om jeg vil ha inn et ekstra vitne som koster mye penger å fly opp fra Spania?", "a": "Hvis *du* krever et vitne, er det som hovedregel du som betaler reisen. Hvis *dommeren* mener vitnet er helt nødvendig for å opplyse saken (\"opplysningar som retten finn naudsynte\"), kan retten beslutte å dekke det, men det er opp til dommeren."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "24", "tittel": "retten beordrer DNA-testen (som de betaler for her)", "available": True},
            {"lov": "barnelova", "paragraf": "13", "tittel": "når saken sendes til retten av NAV", "available": True},
        ],
    },
    {
        "number": "30",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hva er foreldreansvar, og hva innebærer det?",
        "kategori": "familie",
        "description": "Hva betyr det egentlig å ha \"foreldreansvar\"? Det gir deg rett og plikt til å ta de store avgjørelsene i barnets liv, men også forbud mot å bruke vold i oppdragelsen.",
        "kort_svar": "Foreldreansvar er retten og plikten til å ta viktige, personlige avgjørelser på vegne av barnet frem til det er 18 år. Dette inkluderer blant annet å velge navn, melde barnet inn i trossamfunn, skaffe pass og samtykke til medisinsk behandling. I tillegg slår loven krystallklart fast at all bruk av vold mot barn, inkludert et \"klask på rumpa\", er strengt forbudt.",
        "paragraftekst": """Barnet har krav på omsut og omtanke frå dei som har foreldreansvaret. Dei har rett og plikt til å ta avgjerder for barnet i personlege tilhøve innanfor dei grensene som §§ 31 til 33 set. Har foreldra sams foreldreansvar, skal dei ta avgjerdene saman. Foreldreansvaret skal utøvast ut frå barnet sine interesser og behov.

Dei som har foreldreansvaret, er skyldige til å gje barnet forsvarleg oppseding og forsyting. Dei skal syte for at barnet får utdanning etter evne og givnad.

Barnet må ikkje bli utsett for vald eller på anna vis bli handsama slik at den fysiske eller psykiske helsa blir utsett for skade eller fare. Dette gjeld òg når valden brukast som ledd i oppsedinga av barnet. Bruk av vald og skremmande eller plagsam framferd eller annan omsynslaus åtferd overfor barnet er forbode.

Om retten til å ta avgjerd for barnet i økonomiske tilhøve gjeld reglane i vergemålsloven.""",
        "hva_betyr_html": """<p>I Norge skiller jussen strengt mellom "foreldreansvar" og "daglig omsorg". Du kan ha foreldreansvar selv om barnet ikke bor hos deg.</p>
<p>Foreldreansvar er en formell makt. Det gir deg rett til å bestemme over barnets "personlige forhold". Dette er de store tingene i livet:</p>
<ul><li>Utstede pass</li><li>Åpne bankkontoer</li><li>Melde barnet inn i et trossamfunn (f.eks. dåp) eller livssynsorganisasjon</li><li>Samtykke til tyngre medisinsk behandling (som ADHD-medisin, operasjoner)</li><li>Navnevalg og navneendring</li><li>Flytting utenlands</li></ul>
<p>Hvis dere har <em>felles (sams) foreldreansvar</em>, betyr det at dere må være enige om disse tingene. Den ene forelderen kan ikke ta med seg barnet til utlandet, endre etternavn, eller skrive ut pass uten den andres signatur. Krangler dere, låser saken seg frem til dere blir enige, eller en av dere går til domstolen for å overta foreldreansvaret alene.</p>
<p>Paragrafen legger også to viktige plikter på foreldrene. For det første skal dere sørge for at barnet får utdanning som passer deres evner. Du kan altså ikke la være å sende barnet på skolen fordi du ikke føler for det.</p>
<p>For det andre, og kanskje aller viktigst, inneholder tredje ledd det absolutte voldsforbudet. Mange foreldre fra andre kulturer – og noen norske – tror at "mild oppdragelsesvold" er tillatt. Det er det ikke. Loven nevner eksplisitt at vold som "ledd i oppsedinga" er forbudt. Et klask på rumpa, å trekke hardt i håret, lugging, risting av baby, kniping – alt er straffbart. I tillegg forbyr loven psykisk vold: Du har ikke lov til å skremme, plage eller oppføre deg hensynsløst mot barnet (som systematisk nedsettende kjefting, true med å forlate dem, eller stenge dem inne i et skap).</p>""",
        "eksempler": [{"navn": "Pass-krangelen", "tekst": "Morten og Hanne er skilt og har felles foreldreansvar for Sofie på 7 år. Sofie bor fast hos Hanne. Hanne planlegger en ferietur til Spania og finner ut at Sofies pass er utgått. Hun drar til politistasjonen, men politiet nekter å utstede nytt pass fordi hun mangler Mortens signatur. Hanne blir sint, siden Sofie bor hos henne. Men fordi de har felles foreldreansvar etter § 30, må begge godkjenne en passutstedelse. Morten må samtykke, enten fysisk eller digitalt."}],
        "vanlige_feil": ["Blande foreldreansvar med daglig omsorg (\"barnet bor hos meg 100 %, derfor kan jeg bestemme navnet alene\"). (Nei, har dere felles foreldreansvar, må dere bestemme det sammen).", "En pappa uten daglig omsorg (kun samvær) tror han ikke har noe han skulle ha sagt om barnet døpes eller skifter skole. (Er pappaen registrert med felles foreldreansvar, kan mor ikke gjøre disse valgene uten hans godkjenning).", "Tro at et \"lite dask\" for å lære barnet en lekse er lov (vold er absolutt forbudt)."],
        "hva_bor_du_html": """<p>Har du felles foreldreansvar med en eks-partner, må du inkludere dem i alle de store avgjørelsene. Send en e-post eller melding og spør: "Jeg tenker vi må bestille nytt pass, signerer du skjemaet?". Unngå å gjøre store inngrep (som å endre barnets navn hos Skatteetaten) i hemmelighet; det er ulovlig og blir reversert når den andre parten oppdager det og klager.</p>
<p>Lær deg grensen mellom hverdagsavgjørelser og foreldreansvarsavgjørelser. Du trenger ikke spørre eksen om barnet kan dra i bursdag, eller om barnet kan klippe håret. Slikt bestemmes av den barnet bor fast hos, eller den som har samvær den helgen (se § 37).</p>""",
        "dumme_sporsmal": [
            {"q": "Kan han stoppe at barnet får livsviktig medisin på sykehuset fordi han har foreldreansvar?", "a": "Nei. Ved akutte, livstruende situasjoner trenger sykehuset kun samtykke fra den av foreldrene som er til stede. Det er ved *planlagt*, ikke-akutt og tyngre behandling at legene vil kreve at begge foreldrene er enige. Nekter han at barnet får nødvendig behandling, kan barnevernet eller Statsforvalteren overstyre ham av hensyn til barnet."},
            {"q": "Vi klarer ikke å bli enige om navnet til barnet, og fristen for navnevalg (6 måneder) nærmer seg. Hva gjør vi?", "a": "Har dere felles foreldreansvar og nekter å fire på kravene deres, vil Skatteetaten til slutt bare gi barnet morens etternavn og la fornavnet stå blankt inntil videre, eller gi et tilfeldig administrativt navn. Dere må bli enige. Er det helt fastlåst, må den ene gå til domstolen og be om foreldreansvaret alene, slik at den personen kan velge navn."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "37", "tittel": "hva du kan bestemme alene fordi barnet bor hos deg", "available": True},
            {"lov": "barnelova", "paragraf": "31", "tittel": "plikten til å la barnet få si sin mening om disse store avgjørelsene", "available": True},
        ],
    },
    {
        "number": "30a",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Avtale om barneekteskap",
        "kategori": "familie",
        "description": "Kan foreldre binde et barn til et ekteskap i fremtiden? Svaret i norsk lov er et knallhardt nei. Slike avtaler er ugyldige.",
        "kort_svar": "Foreldre, slektninger eller andre kan ikke inngå avtaler som lover at et barn skal gifte seg. Eventuelle avtaler om barneekteskap har ingen juridisk gyldighet (er ikke bindende) i Norge.",
        "paragraftekst": "Ein avtale foreldre eller andre gjer om ekteskap på vegner av barnet, er ikkje bindande.",
        "hva_betyr_html": """<p>Noen kulturer praktiserer tradisjoner der foreldrene inngår en forlovelses- eller ekteskapsavtale for barnet mens barnet ennå er lite, ofte mot utveksling av penger, gaver (medgift) eller løfter. Loven gjør det tindrende klart at ingen eier barnet i Norge.</p>
<p>Et barn har frihet til å bestemme over sitt eget liv og hvem de vil gifte seg med (eller om de vil gifte seg i det hele tatt) når de er voksne. Foreldreansvaret strekker seg rett og slett ikke så langt som å kunne binde et barn til et ekteskap, selv om det er gjort "for barnets beste" ifølge familiens tradisjon.</p>
<p>Skulle foreldrene ha skrevet under på en papirkontrakt om at barnet skal gifte seg med en bestemt fetter, er det papiret ikke verdt noe som helst. Paret familien forsøkte å presse, kan trygt ignorere kontrakten. Forsøker noen å bruke tvang for å gjennomføre ekteskapet, går det over i alvorlig kriminalitet (straffelovens forbud mot tvangsekteskap).</p>""",
        "eksempler": [{"navn": "Kontrakten", "tekst": "Mens Amina (12) bodde i utlandet, inngikk foreldrene en skriftlig avtale med farens bror om at Amina skulle gifte seg med nevøen når hun ble 18. Nå bor de i Norge. Foreldrene viser frem papiret når Amina fyller 18 og sier at avtalen er underskrevet, så hun må gifte seg, ellers bryter de en kontrakt. Men § 30 a slår fast at avtalen er en nullitet. Den finnes ikke juridisk i Norge. Amina kan fritt avvise hele arrangementet, og den andre familien kan ikke kreve kontrakten innfridd i en domstol."}],
        "vanlige_feil": ["Jenter og gutter som vokser opp i visse miljøer, føler seg presset fordi de tror \"papiret\" far signerte har verdi. Det har null juridisk kraft."],
        "hva_bor_du_html": "<p>Hvis du er et barn som utsettes for press fordi foreldrene hevder de har lovet deg bort til et ekteskap, husk at staten og loven står på din side. Avtalen er verdiløs. Er du bekymret for å bli tvunget til å reise ut av landet for et slikt ekteskap, kan du ta kontakt med helsesykepleier på skolen, politiet, eller organisasjoner som Røde Kors (Røde Kors-telefonen om tvangsekteskap og æresrelatert vold). De kan hjelpe deg med å stoppe passet ditt og gi deg beskyttelse.</p>",
        "dumme_sporsmal": [
            {"q": "Straffes foreldrene bare fordi de skriver en slik avtale?", "a": "Selve *handlingen* med å skrive avtalen gjøres bare ugyldig (sivilrettslig) av denne paragrafen. Men hvis foreldrene deretter bruker trusler, psykisk press eller fysisk makt for å forsøke å *gjennomføre* avtalen, vil de bli siktet for tvangsekteskap eller menneskehandel etter straffeloven, noe som gir strenge fengselsstraffer."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "30", "tittel": "om at foreldreansvaret har grenser og vold er forbudt", "available": True},
            {"lov": "barnelova", "paragraf": "31", "tittel": "om at barnets egne meninger skal høres i alle viktige saker", "available": True},
        ],
    },
    {
        "number": "31",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Barnet har rett til å si sin mening (fra 7 og 12 år)",
        "kategori": "familie",
        "description": "Hvem bestemmer hvor barnet skal bo etter et brudd? Barn har en lovfestet rett til å bli hørt fra de er 7 år. Ved 12 år skal deres mening vektlegges sterkt.",
        "kort_svar": "Før du tar viktige avgjørelser om barnets liv (som hvem barnet skal bo fast hos, samvær eller flytting), har barnet rett til å få si sin mening. Når barnet er 7 år, *skal* det høres, og yngre barn skal høres hvis de forstår saken. Når barnet fyller 12 år, har barnets stemme stor makt, og dere skal legge \"stor vekt\" på hva barnet mener.",
        "paragraftekst": """Etter kvart som barnet blir i stand til å danne seg eigne synspunkt på det saka dreiar seg om, skal foreldra høyre kva barnet har å seie før dei tek avgjerd om personlege forhold for barnet. Dei skal leggje vekt på det barnet meiner alt etter kor gammalt og modent barnet er. Det same gjeld for andre som barnet bur hos eller som har med barnet å gjere.

Eit barn som er fylt sju år, og yngre barn som er i stand til å danne seg eigne synspunkt, skal få informasjon og høve til å seie meininga si før det blir teke avgjerd om personlege forhold for barnet, mellom anna om foreldreansvaret, kvar barnet skal bu fast og samvær. Meininga til barnet skal bli vektlagt etter alder og modning. Når barnet er fylt 12 år, skal det leggjast stor vekt på kva barnet meiner.""",
        "hva_betyr_html": """<p>Paragrafen er kjernen i barnets menneskerettigheter (Barnekonvensjonen). Tidligere trodde man at voksne alltid visste best, og man holdt barn utenfor diskusjoner om skilsmissen av "hensyn" til dem.</p>
<p>I dag sier loven at barna må involveres. Før dere signerer en avtale om at pappa skal ha barnet annenhver helg, eller at barnet skal bytte barneskole, har barnet rett til å uttale seg.</p>
<p><strong>7-årsregelen</strong> Når barnet har blåst ut 7 lys på kaken, har det en absolutt <em>rett</em> til å bli informert og hørt. (Ofte snakker man med yngre barn også, gjerne ned mot 4-5 år). Du skal gi barnet nøytral informasjon om at "mamma og pappa vurderer to ulike turnuser for deg, hva tenker du om det?".</p>
<p><strong>12-årsregelen</strong> Når barnet runder 12 år, er det nesten for en tenåring å regne. Da sier loven at det skal legges <em>stor vekt</em> på hva barnet mener. Hvis en 12-åring sier at hen nekter å sove hos far og vil bo fast hos mor, må det foreligge ekstremt tunge, skadelige grunner (for eksempel hvis mor er rusmisbruker) for at en domstol eller far skal kunne tvinge gjennom at 12-åringen må flytte til far. Som regel bestemmer 12-åringer i stor grad hvor de skal bo, og det er opp til far å bruke samværet (kafébesøk osv.) til å bygge en relasjon barnet frivillig vil bo i.</p>
<p>Husk: Dette er en rett barnet har til å uttale seg, <em>ikke en plikt</em>. Barnet skal aldri tvinges til å velge mellom mamma og pappa hvis de ikke vil svare.</p>""",
        "eksempler": [{"navn": "13-åringen bestemmer selv", "tekst": "Tom og Siri skal skilles. Siri vil flytte til en annen by, og vil at 13 år gamle Lukas skal bo fast hos henne der. Tom er uenig. Begge foreldrene setter seg ned med Lukas. Lukas er helt klar: Han vil fortsette å gå på ungdomsskolen der han bor nå, spille på det samme fotballaget, og vil derfor bo fast hos pappa Tom, med helgebesøk hos mor. Siri har ikke lyst til å gi fra seg den daglige omsorgen, men siden Lukas er 13 år (godt over 12 år-grensen), vil domstolen legge avgjørende vekt på hva han vil. Siri innser at hun taper hvis det blir rettssak, og går med på Lukas' ønske."}],
        "vanlige_feil": ["Foreldre skjermer en 8-åring helt fra at far skal flytte tre timer unna, og forteller det bare som et faktum til slutt. (Lovbrudd, 8-åringen har rett til å høres underveis i vurderingen).", "Kreve at dommeren tvinger en 14-åring til å bo annenhver uke hos seg når 14-åringen hater det. (Dette fungerer aldri. Barn over 12 blir hørt, og dommere utsteder ikke \"henteordre\" på sinte tenåringer).", "Blande høringsrett med at \"barnet får lov å velge alene\". Selv en 12-åring fatter ikke alltid rasjonelle valg; det er foreldrenes og dommerens jobb å veie barnets mening opp mot hva som faktisk er best for barnet."],
        "hva_bor_du_html": "<p>Når dere skal endre på samvær, bosted eller skole, hold et barne-møte: 1. Spør barnet på en trygg, ufarlig måte. Ikke spør: \"Vil du bo mest hos meg eller mamma?\", men heller \"Hvordan trives du med den ordningen vi har nå, og er det noe vi voksne kan endre for at ukene dine skal bli bedre?\". 2. Hører du at barnet over 12 år ikke vil ha ordningen du ønsker, respekter det. Konflikt tærer hardt på tenåringer. Bygg bro, ikke bygg en domstol-mur. 3. Hvis saken går til familievernet for mekling, kan meklingssenteret tilby en egen barnesamtale der barnet får snakke med en upartisk voksen. Takke ja til dette. Det hjelper ofte.</p>",
        "dumme_sporsmal": [
            {"q": "Har 12-åringen min full bestemmelsesrett til å kutte meg helt ut?", "a": "Loven sier at 12-åringen sin mening skal tillegges *stor vekt*, ikke at barnet bestemmer 100 %. Samværsretten består frem til barnet er 18 år. Hvis 12-åringen vil kutte deg ut fordi du krever at han gjør lekser, mens mor lar ham spille PlayStation døgnet rundt, vil ikke retten gi 12-åringen medhold, fordi det åpenbart ikke er til det beste for barnet. Det er domstolen/foreldrene som tar beslutningen, barnet har bare stemmerett. (Først når barnet fyller 15 år, får barnet egne selvstendige rettigheter til å melde seg ut av religiøse samfunn osv, se § 32)."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "32", "tittel": "avgjørelser 15-åringer kan ta helt alene", "available": True},
            {"lov": "barnelova", "paragraf": "33", "tittel": "barnets voksende selvbestemmelsesrett mot 18 år", "available": True},
            {"lov": "barnelova", "paragraf": "61", "tittel": "hvordan barn høres konkret inne i domstolen", "available": True},
        ],
    },
    {
        "number": "32",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hva kan en 15-åring bestemme helt alene?",
        "kategori": "familie",
        "description": "Når barnet fyller 15 år, mister du som forelder makten over to viktige ting. Ungdommen bestemmer selv over egen utdanning og religion.",
        "kort_svar": "Når barnet ditt fyller 15 år, får det absolutt bestemmelsesrett over sitt eget valg av utdanning og hvilke foreninger det vil være medlem av. Du kan ikke lenger tvinge barnet til å gå på en spesiell videregående skole, og du kan ikke tvinge det inn i eller ut av et trossamfunn.",
        "paragraftekst": "Barn som er fylt 15 år, avgjer sjølv spørsmål om val av utdanning og om å melde seg inn i eller ut av foreiningar.",
        "hva_betyr_html": """<p>Gjennom hele barndommen har du som forelder foreldreansvaret, og dermed makten til å ta store, personlige valg for barnet. Men ved 15-årsalderen kutter loven to viktige bånd. Loven gir ungdommen en tidlig myndighetsalder for to helt spesifikke områder.</p>
<p>For det første gjelder det skole og utdanning. Det er vanligvis det året barnet skal søke seg inn på videregående skole (VGS). Kanskje du har en drøm om at barnet skal bli lege og gå studiespesialisering, men 15-åringen vil gå yrkesfag for å bli tømrer. Paragraf 32 slår fast at det er 15-åringens valg som gjelder. Du kan verken logge inn på VIGO og endre søknaden deres lovlig, eller nekte dem å takke ja til plassen.</p>
<p>For det andre gjelder det medlemskap i foreninger. Dette betyr alt fra politiske ungdomspartier til idrettslag og religiøse trossamfunn. Hvis du er dypt religiøs og barnet ditt fyller 15 år og bestemmer seg for å melde seg ut av menigheten din, har barnet lov til det. Du kan ikke stoppe det. På samme måte kan en 15-åring melde seg inn i et politisk parti du er dypt uenig med.</p>""",
        "eksempler": [{"navn": "Jonas sitt skolevalg", "tekst": "Jonas (15) sine foreldre er begge advokater, og de forventer at han går på den lokale, prestisjetunge videregående skolen. Jonas hater teori og elsker biler. Han logger inn og søker kjøretøy-linjen på en skole i nabokommunen. Foreldrene blir rasende og kontakter fylkeskommunen for å få slettet søknaden fordi Jonas er mindreårig. Fylkeskommunen avviser foreldrene og viser til barnelova § 32. Jonas har fylt 15 år, og utdanningsvalget er hundre prosent hans."}],
        "vanlige_feil": ["Tro at man kan tvinge en 16-åring til å konfirmere seg i kirken.", "Som forelder logge inn med sin egen BankID og \"rette\" barnets VGS-søknad mot deres vilje (ugyldig og ulovlig).", "Idrettslag som nekter en 15-åring å melde seg ut før foreldrene har signert."],
        "hva_bor_du_html": "<p>Når barnet nærmer seg 15 år, må du endre foreldrerollen fra \"bestemmer\" til \"veileder\". Du har lov til å gi råd, argumentere og diskutere skolevalg og foreninger så mye du vil. Du kan fortelle dem hvorfor du mener det ene valget er bedre enn det andre. Men når diskusjonen er over og skjemaet skal sendes inn, må du respektere at loven har gitt ungdommen siste ord.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg nekte å betale for en dyr skole 15-åringen velger selv?", "a": "Dette er en interessant gråsone. Du har plikt til å forsørge barnet og gi det en utdanning i tråd med deres evner (etter § 66). Men du har ikke nødvendigvis plikt til å betale for en svindyr privatskole eller en idrettslinje som koster titusenvis av kroner ekstra, hvis det finnes et gratis offentlig alternativ og familien ikke har råd. Ungdommen bestemmer *valget* av retning, men dere må løse den økonomiske rammefinansieringen sammen."},
            {"q": "Hva med medisinske valg? Er de også frigitt ved 15 år?", "a": "Nei, denne paragrafen gjelder kun utdanning og foreninger. For helse og medisin gjelder pasient- og brukerrettighetsloven. Hovedregelen der er at barn blir \"helserettslig myndige\" ved 16 år, ikke 15 år (med noen unntak for lettere behandling)."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "31", "tittel": "retten til å bli hørt fra 7 og 12 år", "available": True},
            {"lov": "barnelova", "paragraf": "33", "tittel": "den generelle retten til økt frihet", "available": True},
            {"lov": "barnelova", "paragraf": "66", "tittel": "din plikt til å forsørge barnet under utdanning", "available": True},
        ],
    },
    {
        "number": "33",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Foreldre skal slippe taket gradvis frem mot 18 år",
        "kategori": "familie",
        "description": "Du kan ikke behandle en 17-åring som en 10-åring. Loven krever at du gir ungdommen din stadig mer frihet og selvbestemmelse frem mot myndighetsalder.",
        "kort_svar": "Som forelder har du en juridisk plikt til å gi barnet ditt stadig mer selvbestemmelsesrett etter hvert som det blir eldre. Innetider, klesvalg og lommepenger skal tilpasses barnets alder, helt frem til de blir voksne (18 år) og bestemmer alt selv.",
        "paragraftekst": "Foreldra skal gje barnet stendig større sjølvråderett med alderen og fram til det fyller 18 år.",
        "hva_betyr_html": """<p>Denne paragrafen er en av de mest "pedagogiske" i hele norsk lov. Den slår fast at overgangen fra maktesløst barn til myndig voksen ikke skal skje over natten på 18-årsdagen. Det skal være en glidende overgang.</p>
<p>Når barnet er 5 år, bestemmer du alt. Hva de spiser, når de sover, hvem de leker med. Når barnet er 13 år, skal du la dem ta mange hverdagsvalg selv. Når ungdommen er 17 år, sier loven at de skal ha nesten full råderett over sitt eget dagligliv.</p>
<p>Dette betyr at du som forelder bryter lovens ånd (og bokstav) dersom du er en "helikopterforelder" som styrer detaljene i en 17-årings liv med jernhånd. Ungdom har rett til privatliv og gradvis frihet til å forme seg selv, sine egne venner og sin egen fritid. Denne paragrafen brukes ofte i diskusjoner om innetider, mobilbruk, overnattinger hos kjærester og deltidsjobber.</p>
<p>Loven gir deg imidlertid et spillerom: Friheten skal tilpasses barnets modenhet. En umoden 16-åring som ruser seg, vil trenge strammere rammer enn en ansvarsbevisst 16-åring.</p>""",
        "eksempler": [{"navn": "Ingrid og innetiden", "tekst": "Ingrid (17) bor hjemme hos far. Faren er veldig streng og har bestemt at Ingrid må være inne på rommet sitt klokken 21.00 hver kveld, selv i helgene, og hun får ikke lov til å velge sine egne klær når hun skal på skolen. Ingrid tar kontakt med Barneombudet. Far opptrer i strid med barnelova § 33. En 17-åring har krav på betydelig sjølvråderett. Faren kan ikke rettferdiggjøre et slikt kontrollregime for en nesten voksen jente, og kan i verste fall risikere at barnevernet kontaktes for psykisk omsorgssvikt hvis det grenser til negativ sosial kontroll."}],
        "vanlige_feil": ["Foreldre som nekter 16-17-åringer å ha kjæreste.", "Kontrollere en eldre tenårings mobil, dagbok og private meldinger uten skjellig grunn (mistanke om fare).", "Tru med å kaste en 17-åring på gaten fordi de nekter å legge seg klokken 22.00."],
        "hva_bor_du_html": "<p>Bruk loven som en veileder i foreldreskapet ditt. Ta \"forhandlingsmøter\" med tenåringen din hvert år. \"Nå er du blitt 16, la oss snakke om innetider og penger\". La dem prøve og feile. Når du stoler på dem og slipper kontrollen bit for bit, oppfyller du ikke bare lovens krav, du skaper også en tryggere og mer selvstendig voksen.</p>",
        "dumme_sporsmal": [
            {"q": "Betyr denne paragrafen at 16-åringen kan nekte å rydde rommet?", "a": "Nei. Selvbestemmelse betyr ikke anarki. Så lenge de bor under ditt tak og du forsørger dem, har du lov til å sette husregler. At ungdommen har krav på personlig frihet, fjerner ikke plikten til å bidra til fellesskapet i hjemmet (som å rydde, ta ut søpla eller spise middag)."},
            {"q": "Kan jeg inndra mobilen til en 17-åring som straff?", "a": "Hvis du betaler abonnementet og eier telefonen, kan du teknisk sett gjøre det. Men hvis tenåringen har kjøpt telefonen for sine egne penger som de har tjent på en deltidsjobb, har de eiendomsrett til den. Da kan du ikke beslaglegge den. Det er ofte bedre å forhandle frem regler enn å bruke inndragelse for eldre tenåringer."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "31", "tittel": "plikten til å høre på barnets mening", "available": True},
            {"lov": "barnelova", "paragraf": "32", "tittel": "ungdommens fulle rett til å velge skole fra 15 år", "available": True},
        ],
    },
    {
        "number": "34",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Foreldreansvar når dere er eller har vært gift",
        "kategori": "familie",
        "description": "Får gifte foreldre felles foreldreansvar automatisk? Ja. Og fellesansvaret fortsetter nøyaktig som før, selv om dere velger å separeres eller skilles.",
        "kort_svar": "Er mor og far gift når barnet blir født, får begge automatisk felles foreldreansvar. Hvis dere senere separeres eller skilles, beholder dere felles foreldreansvar. Ingen mister ansvaret etter et brudd med mindre dere skriftlig avtaler det, eller en domstol bestemmer noe annet.",
        "paragraftekst": """Foreldre som er gifte, har foreldreansvaret saman for sams barn.

Foreldre som separerer eller skil seg, kan avtale at dei skal ha foreldreansvaret saman eller at ein av dei skal ha det aleine. Inntil avtale eller avgjerd om foreldreansvaret ligg føre, har dei ansvaret saman.""",
        "hva_betyr_html": """<p>Når et ektepar får barn, ordner det offentlige alt. Ektemannen registreres som far (§ 3), og begge to føres opp med "felles foreldreansvar" i Folkeregisteret.</p>
<p>Dere har da lik rett til å ta de store avgjørelsene for barnet, som å søke om pass, velge navn eller samtykke til tung medisinsk behandling. Den ene kan ikke overkjøre den andre.</p>
<p>Tidligere i historien var det mange som trodde at skilsmisse førte til at mor automatisk fikk foreldreansvaret alene. Slik er det ikke. Loven fastslår at felles foreldreansvar overlever samlivsbruddet. Flytter dere fra hverandre, fortsetter dere å være felles beslutningstakere i barnets liv.</p>
<p>Ønsker dere å endre dette ved skilsmissen — for eksempel fordi faren skal flytte til Australia og ikke kan være involvert — kan dere inngå en skriftlig avtale om at mor skal ha ansvaret alene. Denne avtalen må sendes til Skatteetaten (Folkeregisteret) for å bli gyldig. Klarer dere ikke å bli enige, og den ene <em>krever</em> ansvaret alene (f.eks. på grunn av vold eller samarbeidsnekt), må saken til domstolen. Inntil dommeren slår klubba i bordet, har dere felles ansvar.</p>""",
        "eksempler": [{"navn": "Pass og skilsmisse", "tekst": "Håkon og Mette er skilt. Sønnen Lukas (8 år) bor 100 % hos Mette, og Håkon har kun samvær annenhver helg. Mette planlegger en stor ferie til USA, men Lukas trenger nytt pass. Mette drar til politiet alene, men får beskjed om at hun ikke kan få ut passet. Selv om de er skilt, og selv om Mette har daglig omsorg, sier § 34 at de fremdeles har felles foreldreansvar. Håkon må derfor møte på politistasjonen eller gi skriftlig samtykke til at passet kan lages."}],
        "vanlige_feil": ["Mor tror hun har foreldreansvaret alene bare fordi far flyttet ut etter skilsmissen.", "Far tror han mister sine rettigheter til å bestemme over skole og helse bare fordi han betaler barnebidrag og har lite samvær.", "Tror at felles foreldreansvar betyr at barnet må bo 50/50 (felles foreldreansvar har ingenting med samværsbrøk å gjøre)."],
        "hva_bor_du_html": """<p>Har du vært gift, skal du legge til grunn at du har felles foreldreansvar med eksen for resten av barndommen. Det krever at dere snakker sammen før store valg tas (navn, flytting utenlands, bankkontoer).</p>
<p>Vil du sjekke hvem som har foreldreansvaret? Du kan logge inn på Skatteetaten.no og sjekke folkeregisteropplysningene for barnet ditt. Der står det svart på hvitt om ansvaret er felles eller ikke.</p>""",
        "dumme_sporsmal": [
            {"q": "Hva skjer hvis eksen nekter å skrive under på pass, og jeg har bestilt flybilletter?", "a": "Dette er et klassisk problem med felles foreldreansvar. Hvis eksen nekter totalt (uten god grunn, f.eks. at de frykter barnebortføring), kan du søke politiet om å utstede pass uten den andres samtykke. Men dette tar lang tid og er strengt. Hvis eksen systematisk saboterer felles foreldreansvar og nekter å skrive under på papirer for barnehage/skole/helse, kan du gå til retten for å kreve ansvaret alene for å få hverdagen til å fungere."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "30", "tittel": "definisjonen på hva foreldreansvar er", "available": True},
            {"lov": "barnelova", "paragraf": "35", "tittel": "tilsvarende regler for de som *ikke* er gift", "available": True},
            {"lov": "barnelova", "paragraf": "37", "tittel": "avgjørelser den barnet bor hos kan ta *alene*, uten eksen", "available": True},
        ],
    },
    {
        "number": "35",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvem får foreldreansvar når dere ikke er gift?",
        "kategori": "familie",
        "description": "Ugift når barnet ble født? En stor lovendring i 2020 gir nå felles foreldreansvar til alle nybakte foreldre, med en liten unntaksregel for alenemødre.",
        "kort_svar": "Er dere ugifte samboere (eller ikke bor sammen), får dere automatisk felles foreldreansvar fra 1. januar 2020. Men: Hvis dere *ikke* bor sammen når barnet blir født, har mor en rett til å kansellere fellesansvaret ved å sende melding til Folkeregisteret innen ett år. Faren kan gjøre det samme.",
        "paragraftekst": """Foreldre som ikkje er gifte, har foreldreansvaret saman for sams barn. Dersom foreldra ikkje bur saman, og mora ønskjer foreldreansvaret aleine, kan ho gje melding til folkeregistermyndigheita innan eitt år frå farskapen vart fastsett. Tilsvarande gjeld der faren ikkje ønskjer sams foreldreansvar. Når ein av foreldra har gjeve slik melding, får mora foreldreansvaret aleine.

For sambuande foreldre som flyttar frå kvarandre, gjeld reglane i § 34 andre leddet tilsvarande.""",
        "hva_betyr_html": """<p>Dette er en av de viktigste og nyeste endringene i norsk familierett. Før 2020 fikk ugifte mødre foreldreansvaret helt alene fra start (med mindre de signerte en samboererklæring for felles ansvar). Fedre måtte tigge om å få bli med. Det førte til store konflikter.</p>
<p>Nå har staten snudd bunken: <strong>Alle foreldre, enten de er kjærester, samboere eller engangspartnere, får felles foreldreansvar fra dag én.</strong> Forutsetningen er selvfølgelig at farskapet er signert (etter § 4).</p>
<p>Hvis dere bor sammen som samboere, er dere låst til felles ansvar, akkurat som ektepar. Skulle dere gjøre det slutt og flytte fra hverandre to år senere, fortsetter fellesansvaret upåvirket, akkurat som ved skilsmisse. Ingen mister makten.</p>
<p><strong>Unntaksregelen for de som ikke bor sammen</strong> Hva med kvinnen som blir gravid etter en tilfeldig natt på byen, og overhodet ikke har noe forhold til mannen? Staten gir automatisk mannen felles foreldreansvar. <em>Men</em>, siden paret ikke bor sammen, gir loven (i første ledd) moren en nødbrems. Hvis hun ønsker foreldreansvaret helt for seg selv, kan hun sende en skriftlig melding til Skatteetaten (Folkeregisteret) om at hun vil ha ansvaret alene. Hun trenger ikke oppgi noen grunn, og faren kan ikke stoppe henne der og da.</p>
<p>Det ligger to absolutte krav her: For det første må paret <em>ikke ha felles adresse</em>. For det andre må meldingen sendes <em>innen ett år</em> etter at mannen ble registrert som far.</p>
<p>Mannen har samme rett: Er han ikke interessert i felles ansvar med en kvinne han ikke bor med, kan han sende melding innen et år, og mor blir stående igjen med ansvaret alene.</p>
<h3>Hva skjer hvis du gjør feil?</h3>
<p>Glemmer mor (som ikke bor med far) fristen på ett år, blir fellesansvaret permanent. For å fjerne ham da, må hun gå den tunge veien gjennom familievernkontoret for mekling og deretter saksøke ham i tingretten, hvor hun må bevise at han er fullstendig uegnet.</p>""",
        "eksempler": [{"navn": "Sofie og \"One-night-stand\"", "tekst": "Sofie og Tom hadde en engangsgreie, og Sofie ble gravid. Tom skrev under på farskapet, men de to tåler ikke trynet på hverandre. Tom bor i Tromsø, Sofie i Oslo. Da babyen ble født (etter 2020), fikk begge felles foreldreansvar automatisk i Folkeregisteret. Sofie innser at hun må be om Toms signatur for pass og lege hele oppveksten, noe hun vet vil bli et mareritt. Siden de ikke bor sammen, sender hun et skjema til Skatteetaten da babyen er fire måneder gammel. Skatteetaten fjerner Tom fra foreldreansvaret, og Sofie har det alene. Vil Tom ha det tilbake nå, må han reise sak for tingretten."}],
        "vanlige_feil": ["Kvinner (som ikke bor med far) glemmer å sende inn meldingen innen 1-års fristen, og låser seg dermed til felles foreldreansvar for alltid (uten rettssak).", "Ugifte fedre tror de får foreldreansvar automatisk uten å signere selve *farskapet* først (farskapet må alltid fikses først etter § 4).", "Mødre som er samboere tror de kan fjerne fars foreldreansvar ved utflytting. (Feil, nødbremsen gjelder bare hvis dere aldri bodde sammen da barnet ble til/født)."],
        "hva_bor_du_html": "<p><strong>For mor:</strong> Er du gravid og vet at du ikke skal bo med faren, og frykter at felles ansvar vil bli umulig eller skadelig for barnet? Logg inn på Skatteetaten eller bruk Altinn umiddelbart etter at farskapet er registrert (eller etter fødsel) og krev foreldreansvaret alene. Husk fristen på 1 år. <strong>For far:</strong> Selv om du mister ansvaret fordi mor bruker nødbremsen, har du fremdeles full samværsrett (se § 42) og du skal betale bidrag (se § 66). Foreldreansvar og samvær er to forskjellige ting. Du kan saksøke for å få felles ansvar.</p>",
        "dumme_sporsmal": [
            {"q": "Får eldre barn plutselig felles foreldreansvar nå?", "a": "Nei, endringen fra 2020 gjelder ikke med tilbakevirkende kraft. Er barnet ditt født utenfor ekteskap før 1. januar 2020, og dere ikke sendte inn et eget samboerskjema for felles ansvar, er det kun mor som har det."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "34", "tittel": "regelen for gifte", "available": True},
            {"lov": "barnelova", "paragraf": "4", "tittel": "hvordan ugifte menn registrerer at de er far (først etter dette gjelder reglene om foreldreansvar)", "available": True},
            {"lov": "barnelova", "paragraf": "30", "tittel": "hva makt du faktisk gir fra deg (eller får) i foreldreansvaret", "available": True},
        ],
    },
    {
        "number": "36",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvor skal barnet bo fast? (Delt fast bosted)",
        "kategori": "familie",
        "description": "Ved et brudd kan foreldre velge \"delt fast bosted\" (at barnet bor fast hos begge), eller at barnet bor fast hos én. Er dere uenige, må en dommer bestemme.",
        "kort_svar": "Etter et samlivsbrudd kan foreldrene fritt avtale at barnet skal ha delt fast bosted (bu fast hos begge), eller at barnet skal ha fast bosted hos den ene og samvær med den andre. Klarer dere ikke å bli enige, må en domstol bestemme. Retten vil som hovedregel dømme at barnet skal bo fast hos én av dere, og ha samvær med den andre.",
        "paragraftekst": """Foreldra kan gjere avtale om at barnet skal bu fast hos begge eller hos ein av dei.

Er foreldra usamde, må retten avgjere at barnet skal bu fast hos ein av dei. Dersom det ligg føre særlege grunnar, kan retten likevel avgjere at barnet skal bu fast hos begge.""",
        "hva_betyr_html": """<p>Når et par går fra hverandre, reiser det seg et stort spørsmål i familieretten: Hvem av dere er "bostedsforelderen"?</p>
<p>Paragraf 36 handler om det juridiske bostedet ("fast bosted"). Det er den som barnet bor fast hos, som får ta de daglige avgjørelsene i barnets liv, for eksempel om barnet skal gå i barnehage, eller om barnet kan flytte til en annen by (se § 37). Den andre forelderen kalles da "samværsforelder".</p>
<p><strong>Delt fast bosted (50/50)</strong> Første ledd gir foreldrene full frihet. Vil dere avtale "delt fast bosted", er det helt supert. Da sidestilles dere juridisk. Dere må da ta alle de viktige hverdagsvalgene sammen, barnet er folkeregistrert med adresse hos én av dere, men har juridisk hjem to steder. Begge foreldre har vetorett mot at den andre flytter med barnet til en annen del av landet.</p>
<p><strong>Når dere må i retten</strong> Er dere bitre uvenner og havner i retten fordi begge krever at barnet skal bo hos seg? I slike konfliktsaker setter loven hardt mot hardt. Det andre leddet sier rett ut at dommeren (som hovedregel) skal peke ut én vinner. Barnet skal dømmes til å bo fast hos én av dere. Det er fordi delt fast bosted krever massivt, knirkefritt samarbeid mellom mor og far. Hvis dere hater hverandre så mye at dere er i en rettssal, er det vanligvis elendig for barnet å bli kastet frem og tilbake i et påtvunget 50/50-opplegg.</p>
<p>Derfor kan retten bare dømme dere til delt fast bosted dersom det foreligger "særlige grunner". For eksempel hvis dere bor i samme nabolag, barnet selv (spesielt hvis det er over 12 år) insisterer på 50/50, og dere til tross for krangelen samarbeider helt greit om fotballsko og matbokser.</p>
<h3>Hva er forskjellen på "Bosted" og "Foreldreansvar"?</h3>
<p>Dette er den vanligste misforståelsen i Norge:</p>
<ul><li><strong>Foreldreansvar (§ 30):</strong> Dette er makt over pass, religion og tunge inngrep. De fleste har dette <em>felles</em> (sammen), uansett hvor barnet bor.</li><li><strong>Fast bosted (§ 36):</strong> Dette er adressen og hverdagsmakten. Bor barnet bare hos mor, kan mor alene bestemme over barnehage, fritidsaktiviteter og flytting i Norge, selv om far har delt foreldreansvar.</li></ul>
<h3>Sammenligningstabell</h3>
<table class="rule-table"><thead><tr><th>Hva vil du gjøre?</th><th>Barnet bor fast hos meg</th><th>Barnet bor fast hos den andre</th><th>Barnet har delt fast bosted</th></tr></thead><tbody><tr><td>Melde barnet i fotball/kulturskole</td><td>Du kan bestemme</td><td>Du kan ikke bestemme</td><td>Begge må være enige</td></tr><tr><td>Flytte med barnet til en annen norsk by</td><td>Du kan bestemme</td><td>Du kan ikke bestemme</td><td>Begge må være enige</td></tr><tr><td>Sende barnet i barnehage/SFO</td><td>Du kan bestemme</td><td>Du kan ikke bestemme</td><td>Begge må være enige</td></tr></tbody></table>""",
        "eksempler": [{"navn": "Rettskampen", "tekst": "Kari og Tom er i tingretten. De har kranglet i ett år. Tom krever delt fast bosted 50/50 for deres 5 år gamle datter, og truer med at alt annet er urettferdig for ham. Kari krever at datteren bor fast hos henne, fordi de to voksne knapt klarer å snakke sammen uten å skrike, og bor én time fra hverandre. Dommeren lytter til partene og støtter seg til § 36. Siden de voksne er i konflikt og bor langt fra hverandre, finnes det ingen \"særlige grunner\" for å tvinge frem et delt bosted. Dommeren dømmer at datteren skal bo fast hos Kari, og gir Tom samvær hver andre helg."}],
        "vanlige_feil": ["Blande \"Delt fast bosted\" (som er en juridisk status hvor foreldrene deler hverdagsmakten) med ren \"50/50 samvær\" (som bare er antall netter overnatting). Du kan ha barnet 14 netter i måneden på samvær, men mor har likevel fast bosted alene på papiret.", "Tro at en dommer automatisk vil dele barnet 50/50 i en rettssak ut fra \"likestillingshensyn\". Loven sier tvert imot at dommeren skal velge én forelder som hovedregel, for å gi barnet ro."],
        "hva_bor_du_html": "<p>Prøv å lage en skriftlig avtale om delt fast bosted, og gi den et reelt forsøk. Hvis kommunikasjonen er god, er det ofte best for barnet at dere deler den daglige makten og ansvaret 50/50. Hvis dere ender i retten og du ønsker å kjempe for delt fast bosted, må du ikke fokusere på dine \"rettigheter som far/mor\". Du må bygge bevis for at dere bor nærme hverandre, at samarbeidet ikke er <em>så</em> ille som eksen skal ha det til, og at barnet vil tjene på det.</p>",
        "dumme_sporsmal": [
            {"q": "Hvor mye samvær får far hvis mor får fast bosted?", "a": "Det bestemmer foreldrene, og hvis ikke, bestemmer retten hva som er \"vanlig samvær\" (historisk definert i § 43 som annenhver helg pluss én dag i uka, pluss ferier) eller noe mer utvidet, alt etter hva som er best for barnet."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "37", "tittel": "all den makten du får hvis barnet bor fast hos deg", "available": True},
            {"lov": "barnelova", "paragraf": "42", "tittel": "retten til samvær når du ikke har fast bosted", "available": True},
        ],
    },
    {
        "number": "37",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Din makt når barnet bor fast hos deg (daglig omsorg)",
        "kategori": "familie",
        "description": "Hva kan du bestemme helt alene hvis barnet bor fast hos deg etter bruddet? Du kan bestemme barnehage, hvor i landet dere skal bo, og hverdagens små og store valg.",
        "kort_svar": "Hvis barnet har fast bosted (daglig omsorg) hos deg alene, har du lov til å ta alle de store hverdagsavgjørelsene alene. Dette gjelder selv om dere har felles foreldreansvar. Du kan fritt flytte med barnet hvor som helst i Norge, velge barnehage og SFO, og melde barnet på fritidsaktiviteter, uten at den andre forelderen kan stanse deg.",
        "paragraftekst": "Har foreldra sams foreldreansvar, men barnet bur fast saman med berre den eine, kan den andre ikkje setje seg mot at den barnet bur saman med, tek avgjerder som gjeld vesentlege sider av omsuta for barnet, m.a. spørsmålet om barnet skal vere i barnehage, kor i landet barnet skal bu og andre større avgjerder om dagleglivet.",
        "hva_betyr_html": """<p>Når vi snakker om barnefordeling, er denne paragrafen trumfkortet. Den beskriver makten som ligger i "fast bosted".</p>
<p>Mange foreldre inngår avtaler som sier: "Barnet bor fast hos mor. Far har vanlig samvær. Vi har felles foreldreansvar".</p>
<p>Hva betyr det i praksis? Det betyr at far MÅ skrive under på passet og navnebytter (på grunn av foreldreansvaret i § 30). Men når det gjelder alt annet, er det mor som styrer skuta alene, takket være § 37.</p>
<p>Loven gir bostedsforelderen vetorett og styringsrett i tre store, viktige kategorier: 1. <strong>Flytting innad i Norge:</strong> Mor kan pakke bilen og ta med seg barnet fra Oslo til Tromsø. Hun trenger ikke fars tillatelse. (Men husk varslingsplikten på 3 måneder i § 42 a, for å gi far tid til å forberede seg eller bringe saken for retten). 2. <strong>Barnehage og skolefritidsordning (SFO):</strong> Mor bestemmer alene om barnet skal gå i barnehagen eller være hjemme, og hvilken barnehage de skal søke på. 3. <strong>Fritidsaktiviteter:</strong> Skal barnet spille fotball tre kvelder i uken? Det bestemmer mor. Far kan ikke klage over at det spiser opp hans tid, så lenge det gjelder en vanlig, fornuftig aktivitet for barnets alder.</p>
<h3>Hva er forskjellen mellom delt fast bosted og fast bosted hos én?</h3>
<p>Dette er den kritiske forskjellen: Hvis dere hadde avtalt "delt fast bosted" (§ 36), ville Lars hatt vetorett mot Hannes flytting til Bergen, fordi makten i § 37 da deles mellom dem. Men fordi Hanne hadde fast bosted alene, bestemmer hun alene.</p>""",
        "eksempler": [{"navn": "Flyttingen til Bergen", "tekst": "Lars og Hanne er skilt. De har felles foreldreansvar, men datteren Emma bor fast hos Hanne. Lars har samvær annenhver helg. Hanne får tilbud om drømmejobben i Bergen og bestemmer seg for å flytte fra Stavanger. Lars blir rasende. Han krever at Hanne blir i Stavanger, og mener at siden de har \"felles foreldreansvar\", kan han stanse flyttingen. Han tar feil. Fordi Emma bor fast hos Hanne, har hun rett etter § 37 til å bestemme \"kor i landet barnet skal bu\". Hun varsler Lars 3 måneder før (etter reglene), og gjennomfører flyttingen lovlig. Vil Lars stanse det, må han gå til retten for å kreve fast bosted overført til seg selv, noe som er svært vanskelig."}],
        "vanlige_feil": ["Samværsfedre som tror \"felles foreldreansvar\" gir dem rett til å nekte eksen å flytte innenlands.", "Bostedsforeldre som tror de kan flytte ut av landet. (Utlandet dekkes *ikke* av denne regelen, utlandet krever begges samtykke, se § 40).", "Glemme å varsle den andre parten tre måneder i forveien før man flytter innenlands."],
        "hva_bor_du_html": """<p>Har barnet fast bosted hos deg, har du ryggdekning for å organisere hverdagen slik du mener er best. Du trenger ikke be eksen om tillatelse før du takker ja til en barnehageplass eller bytter by i Norge.</p>
<p>Du bør likevel handle klokt. Informer eksen om valgene dine for å holde temperaturen nede. Hvis du flytter langt av sted bare for å sabotere den andres samvær, og ikke av en god grunn som ny jobb, risikerer du at domstolen straffer deg ved å flytte barnet til den andre forelderen ved en senere anledning.</p>""",
        "dumme_sporsmal": [
            {"q": "Kan bostedsforelderen melde barnet på aktiviteter i helgen barnet er hos meg?", "a": "Ja, makten til å styre fritidsaktiviteter ligger hos den som har fast bosted. Mener mor at fotballturneringer i helgene er avgjørende for barnets miljø, må far som hovedregel sørge for at barnet kommer seg dit under samværshelgene. Men mor kan ikke bruke fritidsaktiviteter systematisk bare for å ødelegge samværet, man forventer rimelighet."},
            {"q": "Betyr \"flytte i landet\" at man kan flytte til Svalbard?", "a": "Svalbard regnes som en del av Norge, ja. Men alle store geografiske sprang vil føre til at samværsforelderen reagerer. Han vil sannsynligvis reise en ny rettssak for å kreve at barnet flyttes til ham, og da vil dommeren vurdere om det faktisk er best for barnet å rives opp med roten og flytte til Svalbard/Finnmark/Oslo, fremfor å bli boende i sin gamle by hos far."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "36", "tittel": "valget mellom ett bosted og delt fast bosted", "available": True},
            {"lov": "barnelova", "paragraf": "30", "tittel": "de beslutningene (som pass) du *ikke* kan ta alene", "available": True},
        ],
    },
    {
        "number": "38",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvem får barnet hvis en forelder dør?",
        "kategori": "familie",
        "description": "En grusom, men nødvendig lov. Hva skjer med foreldreansvaret for et barn hvis den ene forelderen dør? Svaret avhenger av hvem som bodde med barnet, og om det var drap.",
        "kort_svar": "Hvis én forelder dør, får den gjenlevende (som hadde felles foreldreansvar) automatisk ansvaret for barnet alene. Hadde avdøde foreldreansvaret alene, får den gjenlevende ansvaret bare dersom de alle bodde sammen. Hvis ikke, må staten (tingretten) avgjøre hvem som får barnet.",
        "paragraftekst": """Døyr den eine av foreldra som har foreldreansvaret saman, får den attlevande foreldreansvaret aleine. Dersom den attlevande er sikta eller tiltala for forsettleg å ha valda den andre forelderen sin død, skal retten ta førebels avgjerd om foreldreansvaret etter reglane i § 64 b.

Døyr ein forelder som har foreldreansvaret aleine, får den attlevande foreldreansvaret dersom barnet budde saman med begge ved dødsfallet. Dette gjeld ikkje i høve der den attlevande er sikta, tiltala eller dømd som nemnt i første stykket andre punktum.

Attlevande og andre kan krevje å få foreldreansvar etter reglane i §§ 64 til 64 d.""",
        "hva_betyr_html": """<p>Paragrafen sikrer en smidig og trygg overgang for barn som mister en forelder, slik at de ikke blir stående uten formelle verger midt i sorgen.</p>
<p>Loven deler det inn i to hovedsituasjoner:</p>
<p><strong>1. Dere hadde felles foreldreansvar</strong> Dette gjelder nesten alle som var gift eller ugifte og hadde registrert felles ansvar. Dør mor i en bilulykke, trenger ikke far gjøre noe som helst med papirene. Han står igjen med foreldreansvaret (100 %) helt automatisk. Dette gjelder selv om de var skilt, og barnet bodde mest hos mor. Far er nå den eneste foresatte.</p>
<p><strong>2. Avdøde hadde foreldreansvaret alene</strong> Kanskje mor hadde nektet far foreldreansvar, og han hadde ingenting med barnet å gjøre, og bodde i en annen by. Dør mor i en slik situasjon, får <em>ikke</em> far automatisk barnet. Da vil barnet stå uten foreldreansvar (etter at mor dør), og da er det domstolen (tingretten) som må holde et rettsmøte. Domstolen vil kalle inn barnevernet og vurdere: Er det best for barnet å flytte til far (som er en fremmed), eller bør mormor eller fosterforeldrene overta foreldreansvaret? (Dette utdypes i § 64). Men: Hvis far og mor faktisk bodde sammen da hun døde, og han var en del av hverdagen (til tross for manglende signatur på fellesansvaret), arver han foreldreansvaret automatisk.</p>
<p><strong>Partnerdrap - den mørke unntaksregelen</strong> Loven har en spesialregel for drap. Hvis mor dør, og far blir siktet eller tiltalt for å ha drept henne (forsettlig, ikke ved uhell), mister han automatisk og umiddelbart alt foreldreansvar. Retten vil ta en hastebeslutning (§ 64 b) og frata ham ansvaret for barnet med det samme, slik at han ikke lenger kan kontrollere barnets papirer, helse og arv fra cellen.</p>""",
        "eksempler": [{"navn": "Skilsmisse-tragedien", "tekst": "Jonas og Kine er skilt. De har felles foreldreansvar for 9 år gamle Elias, men Elias bor fast hos Kine. Kine dør brått av hjerteinfarkt. Kines søster rykker inn, mener at Jonas er en udugelig far, og krever å få omsorgen for Elias fordi hun og Kine var så nære. Hun har ingen støtte i loven. Etter § 38 (fordi de hadde felles ansvar) glir foreldreansvaret og bostedet automatisk og fullt ut over på Jonas. Han er nå eneste foresatte. Hvis søsteren mener Jonas er en fare for barnet, må hun enten varsle barnevernet eller reise sak for tingretten. Men inntil en dommer stopper ham, er Elias hans."}],
        "vanlige_feil": ["Tante/Mormor tror de har krav på å overta barnet fordi de var naboer med mor og bisto mye, og nekter å levere ut barnet til faren som dukker opp.", "Den gjenlevende forelderen (uten foreldreansvar) tror at fordi de er biologisk opphav, tilfaller barnet dem umiddelbart, og dukker opp for å \"hente\" barnet ved mors død (dette må via domstolen i sak etter § 64)."],
        "hva_bor_du_html": "",
        "dumme_sporsmal": [
            {"q": "Hva om mor har skrevet i testamentet sitt at søsteren hennes skal ha barnet, ikke far?", "a": "Mor kan skrive hva hun vil i et testamente, og domstolen skal legge vekt på hennes siste vilje hvis de må behandle en sak. Men barn er ikke gjenstander, og et testamente overstyrer aldri lovens automatikk i § 38. Hadde far felles foreldreansvar, går ansvaret til ham. Testamentet faller \"bort\"."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "64", "tittel": "prosessen i domstolen når staten må fordele et barn etter dødsfall", "available": True},
            {"lov": "barnelova§34og", "paragraf": "35", "tittel": "hvordan dere fikk felles foreldreansvar før dødsfallet", "available": False},
        ],
    },
    {
        "number": "39",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvordan avtaler du å dele eller overføre foreldreansvar?",
        "kategori": "familie",
        "description": "En muntlig avtale om hvem som har foreldreansvaret, har ingen verdi. For at det skal gjelde juridisk, må Skatteetaten få formell beskjed i et bestemt skjema.",
        "kort_svar": "Hvis dere blir enige om å endre hvem som har foreldreansvar (for eksempel overføre det fra bare mor til felles ansvar, eller fra felles til bare far), må denne avtalen meldes formelt til Folkeregisteret. Gjør dere ikke det, er avtalen ulovlig og ugyldig.",
        "paragraftekst": """Avtale eller norsk avgjerd om foreldreansvaret skal meldast til folkeregistermyndigheita. Avtale om foreldreansvar som ikkje er meldt til folkeregistermyndigheita, er ikkje gyldig. Dersom farskap eller medmorskap er fastsett, og foreldra er folkeregistrerte på same adresse her i landet eller erklærer i melding til folkeregistermyndigheita at dei bur saman her, skal folkeregistermyndigheita registrera at foreldra har foreldreansvaret saman.

Ei avtale etter første stykket må vere inngått i samsvar med norsk rett mellom foreldra og gjelde felles barn.""",
        "hva_betyr_html": """<p>Foreldreansvar er et verktøy du bruker mot tredjeparter: politiet (for pass), banken (for konto), og sykehuset (for medisinsk behandling). Disse organene sjekker Folkeregisteret før de lar deg gjøre noe.</p>
<p>Derfor sier § 39 at all pratingen, all kranglingen, og alle uformelle skriftlige kontrakter mellom mor og far, betyr ingenting. "Avtale om foreldreansvar som ikkje er meldt til folkeregistermyndigheita, er ikkje gyldig", står det i klartekst.</p>
<p>Det betyr at hvis mor (som kanskje fikk barnet i 2018 og hadde ansvaret alene) sender en e-post til far og sier "jeg går med på at vi har felles foreldreansvar fra i dag", og far tar med denne utskriften til banken, vil banken avvise ham. Paret må fylle ut det offisielle skjemaet for overføring/deling av foreldreansvar og sende det til Skatteetaten. Først når Skatteetaten har registrert det i systemet, har far fått den juridiske makten sin.</p>
<p>Paragrafen presiserer også (i tråd med § 35) at hvis foreldre med ukjent sivilstatus er registrert på samme adresse, vil Folkeregisteret automatisk slå sammen ansvaret til felles foreldreansvar, gitt at farskapet er bekreftet.</p>""",
        "eksempler": [{"navn": "Huslånet og banken", "tekst": "Lise og Tom er skilt og inngikk et forlik i retten i mars hvor Tom ga fra seg alt foreldreansvar til Lise. Advokatene ristet hender, men glemte å sende papirene til Skatteetaten. I august prøver Lise å åpne en ny BSU-konto til barnet for å sette inn konfirmasjonspenger. Banken sjekker systemet, ser at \"Tom og Lise har felles foreldreansvar\" (slik det var før skilsmissen), og krever Toms signatur. Lise drar frem en utskrift fra rettsforliket. Banken nekter, med henvisning til § 39. Rettsforliket er ikke gyldig overfor tredjepart før Skatteetaten har registrert det. Lise må ringe Skatteetaten, og mister verdifull tid."}],
        "vanlige_feil": ["Foreldre glemmer å sende inn meklingsprotokoller eller skilsmissepapirer som regulerer ansvaret, til riktig etat.", "Tro at et notat på helsekortet eller et Word-dokument signert av begge på kjøkkenbordet er nok.", "Tro at endring av \"fast bosted\" endrer foreldreansvaret (det er to helt forskjellige ting, pass på å krysse av for riktig ord på Skatteetatens skjema)."],
        "hva_bor_du_html": "<p>Har dere endret på noe som gjelder hvem som har foreldreansvar? Gå inn på Skatteetaten.no, søk etter \"Endre foreldreansvar\", logg inn med BankID og fyll ut den digitale meldingen derfra. Det er gratis, og det ordner biffen på noen få virkedager. Sjekk registeret etterpå for å sikre at oppdateringen ble godkjent.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om vi signerte papirene og sendte dem i posten, men eksen min ringte Skatteetaten og sa hun angret dagen etter?", "a": "Frem til Skatteetaten har gjort selve registreringen, anses ikke avtalen som endelig og gyldig. Skatteetaten vil stanse prosessen hvis en av foreldrene trekker samtykket sitt tilbake mens saken ligger til behandling (med mindre det er snakk om en bindende dom fra en rettssal, som Skatteetaten plikter å rette seg etter uansett)."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "30", "tittel": "minner deg på hva makten du nå prøver å overføre, faktisk er", "available": True},
        ],
    },
    {
        "number": "40",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Flytting til utlandet krever at dere er enige",
        "kategori": "familie",
        "description": "Kan du ta med deg barnet og flytte til Sverige eller Spania? Nei. Hvis dere har felles foreldreansvar, må den andre forelderen godkjenne utenlandsflyttingen.",
        "kort_svar": "Har dere felles foreldreansvar, har ingen av dere lov til å flytte med barnet ut av Norge (eller oppholde dere der lenge) uten at den andre samtykker. Har én av dere foreldreansvaret helt alene, kan den personen fritt flytte til utlandet, og den andre kan ikke stanse det.",
        "paragraftekst": """Har den eine av foreldra foreldreansvaret åleine, kan den andre ikkje setje seg imot at barnet flyttar ut av landet.

Dersom foreldra har foreldreansvaret saman, må begge samtykkje til at barnet skal flytte ut av landet eller ta opphald utanfor landet utover stuttare utanlandsferder, jf. § 41. Det same gjeld der eit avtalt opphald blir forlenga eller endra, til dømes der barnet blir etterlate.

Barn som er fylt 12 år, må samtykkje til ei avgjerd etter første og andre stykket dersom barnet flyttar eller tek opphald utan ein forelder med foreldreansvar.

Er foreldra usamde om kven som skal ha foreldreansvaret, flytting med barnet ut av landet, eller kven barnet skal bu fast saman med, må barnet ikkje flytte ut av landet før saka er avgjort.""",
        "hva_betyr_html": """<p>Paragraf 40 er en av de mest rigide beskyttelsesreglene i norsk familierett. Den hindrer den ene forelderen i å rive barnet fullstendig opp med roten og ta det ut av norsk jurisdiksjon for godt.</p>
<p>Vi minner om maktforholdet fra § 37 (innenlands flytting): Har du barnet boende fast hos deg, kan du flytte til Finnmark uten eksens samtykke.</p>
<p>Men i det sekundet du planlegger å flytte til Strömstad i Sverige, eller Marbella i Spania, slår § 40 inn. Hvis dere har <strong>felles foreldreansvar</strong>, mister du retten til å bestemme alene. Da <em>kreves</em> det at eksen (som kanskje bare har helgesamvær) signerer og godkjenner utenlandsflyttingen.</p>
<p>Godkjenner ikke eksen det, og du reiser likevel, begår du barnebortføring etter loven. (Straumstraff og politietterforskning kan iverksettes, og Haag-konvensjonen vil brukes for å hente barnet hjem).</p>
<p>Dette gjelder ikke bare permanent flytting. Reiser du på ferie med avtale om to uker, og bare velger å bli der i seks måneder ("etterlater barnet"), bryter du loven på nøyaktig samme måte. Hvert langtidsopphold utover normal ferie krever samtykke.</p>
<p><strong>Når du har ansvaret alene:</strong> Det er her den store fordelen med å ha foreldreansvaret alene viser seg (første ledd). Er det bare mor som har foreldreansvar for barnet (og far for eksempel har blitt fratatt det i en dom, eller mistet det etter § 35), kan hun flytte til Spania med barnet i morgen, og far kan ikke løfte en finger for å stoppe selve flyttingen.</p>
<p><strong>Når en konflikt har startet:</strong> Hvis du aner uråd og tenker "jeg stikker til Sverige før han rekker å gå til sak", så stopper det fjerde leddet deg. Hvis det allerede ligger en pågående konflikt (mekling, stevning til retten om bosted eller foreldreansvar) og krangler om hvem som skal ha hva, har dere midlertidig utreiseforbud til saken er endelig avgjort av dommeren.</p>""",
        "eksempler": [{"navn": "Flukten til Spania", "tekst": "Maria og Petter er skilt og har felles foreldreansvar. Barna bor fast hos Maria, og Petter har samvær én helg i måneden. Maria får seg spansk kjæreste, selger huset, tar med seg barna og flytter til Torrevieja uten å fortelle Petter det før de har landet. Petter kontakter advokat. Siden de hadde felles foreldreansvar, krever utenlandsflytting samtykke fra begge etter § 40. Maria har begått en ulovlig handling (barnebortføring). Petter saksøker henne og vinner saken. Norske domstoler krever at barna tilbakeføres til Norge umiddelbart."}],
        "vanlige_feil": ["Mødre som er skilt fra utenlandske menn, og tror de kan flytte tilbake til \"hjemlandet sitt\" med barna uten nordmannens godkjennelse.", "Tro at en \"studietur på 8 måneder\" er lovlig fordi det ikke er en permanent flyttemelding i Folkeregisteret. (Det regnes som \"opphold\" og krever signatur).", "Foreldre uten foreldreansvar, som tror de kan stoppe eksen (med ansvar) fra å flytte fordi det ruinerer samværet."],
        "hva_bor_du_html": """<p>Ønsker du å flytte utenlands, og eksen sier nei? Du har bare én lovlig vei ut av det. Du må reise en sak for tingretten. Du må be dommeren om å oppheve det felles foreldreansvaret og gi det til deg alene.</p>
<p>Du må argumentere for at det er til barnets aller beste å flytte (kanskje på grunn av en eksepsjonell jobbmulighet, storfamilie som gir nettverk, barnet sitt eget sterke ønske, og eksens manglende samværshistorikk). Det er en tøff sak å vinne. Vinner du, og får ansvaret alene, kan du deretter flytte.</p>""",
        "dumme_sporsmal": [
            {"q": "Hva om barnet (15) ønsker å dra på utvekslingsår i USA uten meg, må vi godkjenne det?", "a": "Ja. Det tredje leddet gjelder akkurat dette. Hvis 15-åringen skal bo på utveksling (altså uten en forelder med foreldreansvar), kreves det at 15-åringen selv, og begge dere foreldre, er hundre prosent enige om turen."},
            {"q": "Vil jeg slippe å betale barnebidrag hvis hun tar ansvaret alene og flytter til USA?", "a": "Absolutt ikke. Samboerplikten (§ 66) omfatter alle barn, overalt. NAV sin utenlandsavdeling vil sørge for at du betaler barnebidrag selv om barnet er i USA og du knapt ser det."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "41", "tittel": "Hvor lenge du kan reise på en \"normal ferie\"", "available": True},
            {"lov": "barnelova", "paragraf": "37", "tittel": "Kontrasten: Du kan flytte innenlands (nesten) fritt", "available": True},
        ],
    },
    {
        "number": "41",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hva er reglene for utenlandsferier? (Reiseforbud)",
        "kategori": "familie",
        "description": "Kan du ta med barnet på sydenferie? Ja. Men frykter den andre at du vil bortføre barnet til utlandet, kan politiet beslaglegge barnets pass og nekte dere utreise.",
        "kort_svar": "Har dere felles foreldreansvar, kan begge fritt ta med barnet på \"kortere\" ferieturer til utlandet. Men hvis det er en reell frykt for at du ikke vil komme tilbake med barnet, kan domstolen og politiet nedlegge utreiseforbud, trekke tilbake barnets pass, og setteppe ferien. Mangler du foreldreansvar, kan du ikke reise utenlands i det hele tatt uten godkjennelse.",
        "paragraftekst": """Den som har sams foreldreansvar, kan ta med eller sende barnet på stuttare utanlandsferder. Har foreldra sams foreldreansvar, kan retten i orskurd setje forbod mot utanlandsferd for barnet, dersom det er uvisst om barnet vil kome attende. Forbodet kan gjelde ei enkelt reise eller ålment, og kan også setjast i ei sak om foreldreansvaret, kven barnet skal bu fast saman med, eller samværsrett. Retten kan ta førebels avgjerd for tida fram til saka er endeleg avgjord.

I sak der det vert nedlagt reiseforbod, skal barnet førast ut av passet til den som vil forlate landet, eller barnet sitt pass skal trekkjast attende, eller barnet kan setjast bort til andre på forsvarleg måte til saka er avgjord.

Dersom det er fare for at barnet ikkje vil kome attende, kan politiet leggje ned førebels utreiseforbod fram til saka kan handsamast av retten. Andre stykket gjeld tilsvarande. Eit førebels utreiseforbod kan ikkje påklagast.

Den av foreldra som ikkje har foreldreansvaret, kan ikkje reise ut av landet med barnet utan samtykkje frå den som har foreldreansvaret. Retten kan likevel etter krav frå den som vil reise, gje samtykkje til utanlandsferd med barnet når det er openbert at barnet vil kome attende. Første stykket tredje og fjerde punktum gjeld tilsvarande for samtykkjet.

Barn som er fylt 12 år, må samtykkje i ei avgjerd om å dra på utanlandsferd utan ein forelder med foreldreansvar.""",
        "hva_betyr_html": """<p>Paragrafen balanserer frihet mot barnebortføring. Hvis dere (som de fleste nordmenn) har felles foreldreansvar, sier første punktum at du fritt kan kjøpe en tur til Gran Canaria, pakke kofferten for deg og barnet, og reise på sommerferie, uten å spørre eksen om lov. Dette kalles "kortere utenlandsferder" (som regel noen dager opp til noen uker).</p>
<p>Men loven har en "rød knapp".</p>
<p>Hvis pappa (for eksempel fra Midtøsten) planlegger en ferietur med barnet til sitt hjemland, og mamma finner bevis (kanskje meldinger til venner) for at han har tømt bankkontoene, sagt opp leiligheten og solgt bilen i Norge, betyr det at han ikke har tenkt å returnere. Han planlegger en barnebortføring.</p>
<p>Mamma kan da ta saken til tingretten for å få et <strong>utreiseforbud</strong>. Beviser hun at det er uvisst om barnet kommer tilbake, vil dommeren forby reisen. Og for å være sikker på at pappa ikke bare trosser forbudet og flykter likevel, kan politiet inndra (ta fra ham) barnets pass.</p>
<p>Siden domstoler tar lang tid (kanskje ukene før flyet går), sier tredje ledd at politiet har makt til å nedlegge et hasteforbud (førebels utreiseforbod) akutt, direkte på flyplassen om nødvendig, mens de venter på at retten skal se på saken.</p>
<p>Det fjerde leddet gjelder menn (eller kvinner) som <em>mangler</em> foreldreansvar (kanskje fordi mor tok det etter § 35). De har ingen rettigheter til å dra på svenskehandel eller sydenferie i sine samværshelger uten mors godkjennelse.</p>""",
        "eksempler": [{"navn": "Passbeslaget", "tekst": "Ali (med felles foreldreansvar) har kjøpt flybilletter for seg og sønnen til Irak for en fireukers sommerferie. Mor får vite at Ali nettopp har sluttet i jobben sin i Norge og har pakket ned alle sønnens vinterklær. Hun blir livredd og frykter han vil bli i Irak. Hun tar kontakt med politiet og en advokat. Politiet nedlegger et førebels (midlertidig) utreiseforbud (tredje ledd). Politiet banker på hos Ali, inndrar sønnens pass, og saken sendes til tingretten. Ali får ikke reist, og må overbevise dommeren om at han ikke planla barnebortføring for å få passet tilbake."}],
        "vanlige_feil": ["Nekter eksen å ta barnet på ferie til Syden bare fordi det er urettferdig (\"det er jo min samværshelg midt inni der!\"). Ferien regnes ikke som ulovlig utenlandsreise. Konflikt om ferieuker må dere løse, men det utløser ikke rettens utreiseforbud.", "Politiets grensekontroll tror at en mor med felles foreldreansvar trenger en signert erklæring fra far for å dra til London. Loven sier at ferier er tillatt uten samtykke, og pass holder som bevis for norsk borger.", "Reiser på ferie til Sverige med barnet mens man har mistet foreldreansvaret, i god tro om at naboland ikke teller. (Utenlandsgrensen er absolutt)."],
        "hva_bor_du_html": """<p>Er du redd for at eksen vil bortføre barnet til utlandet og aldri komme tilbake? Ikke vent på domstolen. Ring politiet på 02800 eller 112 og be om krisehjelp. Politiet kan vedta utreiseforbud i løpet av minutter og slette passets gyldighet (varsle passkontrollene). Deretter ringer du advokat for å sikre et permanent forbud i domstolen.</p>
<p>Vil du reise med et barn, og du ikke har foreldreansvar, men eksen din nekter deg en ferie for å være fæl? Da gir fjerde ledd deg en rett til å klage eksen inn for domstolen. Du kan be dommeren om tillatelse til å ta en sydenferie, og dommeren gir deg det hvis han anser fluktfaren som "helt usannsynlig".</p>""",
        "dumme_sporsmal": [
            {"q": "Hvor går grensen mellom en \"ferie\" og en \"flytting\"?", "a": "Grensen er ikke bare ukene, men formålet. En to-måneders backpacking kan være en ferie, mens en én-måneds tur der barnet begynner på lokal skole, kan regnes som flytting. En god tommelfingerregel fra domstolene er at ferier over tre til fire uker ofte krever godkjennelse."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "40", "tittel": "den absolutte regelen om at permanent flytting krever samtykke", "available": True},
            {"lov": "barnelova", "paragraf": "60", "tittel": "hvordan retten fatter \"midlertidige/haste\"-avgjørelser", "available": True},
        ],
    },
    {
        "number": "42",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Barnets absolutte rett til samvær med begge foreldre",
        "kategori": "familie",
        "description": "Hvem har egentlig rett til samvær, foreldrene eller barnet? Loven slår fast at det er barnets rett å se foreldrene sine. Slik fungerer samværsretten.",
        "kort_svar": "Barnet har rett til samvær (kontakt og tid) med begge foreldrene sine, selv om foreldrene ikke bor sammen. Den forelderen som har barnet på samvær, har fulle fullmakter til å ta daglige omsorgsavgjørelser for barnet (som måltider, leggetider og klær) mens samværet pågår.",
        "paragraftekst": """Barnet har rett til samvær med begge foreldra, jamvel om dei lever kvar for seg. Foreldra har gjensidig ansvar for at samværsretten vert oppfyld.

Barnet har krav på omsut og omtanke frå den som er saman med barnet. Den som er saman med barnet, kan ta avgjerder som gjeld omsuta for barnet under samværet.""",
        "hva_betyr_html": """<p>Mange foreldre krangler om sine rettigheter etter et samlivsbrudd: "Jeg har rett til å se datteren min". Men loven ser motsatt på saken: "Det er <em>barnet</em> som har en lovfestet rett til å se deg". Dette rettighetsperspektivet i første ledd av § 42 gjelder for alle barn, uansett om foreldrene var gift, samboere, eller bare tilbrakte en natt sammen for åtte år siden.</p>
<p>Samværsrett er selve ryggraden i familieretten. Den gjelder frem til barnet er 18 år. Selv om faren mangler foreldreansvar (ikke kan bestemme pass eller kirke, se § 30) og mangler fast bosted (ikke kan velge barneskole, se § 37), så fjerner ikke det hans rett og barnets behov for vanlig, fysisk samvær.</p>
<p>Begge foreldrene har et <em>gjensidig</em> ansvar for å få samværet til å fungere praktisk og følelsesmessig. Bostedsforelderen kan ikke aktivt sabotere ved å si at "det passer aldri", og samværsforelderen kan ikke utebli gang etter gang uten konsekvenser.</p>
<p><strong>Når barnet er hos samværsforelderen</strong> Det andre leddet beskytter samværsforelderen fra en pirkete eks-partner. Når barnet er hos deg fra fredag til søndag, er det <em>du</em> som bestemmer reglene i ditt eget hus. Mor kan ikke sende med deg en regelbok som sier at "gutten skal spise vegansk kl. 17.00 og være i seng kl. 19.30", hvis du foretrekker pølser og la ham være oppe til 21.00. (Mindre det gjelder sterke medisinske behov som allergier). Du har rettighetene til den <em>daglige omsorgen</em> for de timene eller dagene barnet er i din varetekt.</p>""",
        "eksempler": [{"navn": "Reglene hos far", "tekst": "Tobias (6 år) bor fast hos mor. Mor er ekstremt opptatt av at Tobias skal skjermes for TV-spill og usunn mat. Når det er pappas samværshelg, sender hun ham hundrevis av SMS-er for å styre pappas helg, krever bildebevis av middagen, og krever at han slår av TV-en. Pappa henviser til § 42. Når Tobias er hos ham, bestemmer han alene over de daglige omsorgstingene under selve samværet. Han serverer pizza, de spiller TV-spill og han legger sønnen kl. 20.00, og han har sin fulle rett til dette."}],
        "vanlige_feil": ["Bostedsforeldre som bruker samværet som et maktmiddel. (Nekter eksen samvær fordi eksen \"ikke har betalt barnebidrag\". Økonomi og samvær har juridisk ingenting med hverandre å gjøre).", "Samværsforeldre som tror de kan unndra seg det *gjensidige* ansvaret (\"Jeg gidder ikke hente i helgen fordi bilen knirker\").", "Bostedsforeldre som prøver å nekte tenåringer å dra på samvær, uten å la ungdommen få et ord med i laget."],
        "hva_bor_du_html": """<p>Strek deg langt for å støtte opp under at barnet har et godt forhold til den andre forelderen, uansett hvor sur du er på dem personlig. Viser du at du motarbeider lovens utgangspunkt (barnets rett til far og mor), vil du i en domstol bli ansett som en svak forelder (sabotør), og i verste fall risikerer du at domstolen flytter barnets bosted til eksen din.</p>
<p>Respekter at den andre forelderen har andre oppdragelsesmetoder, regler og vaner enn deg i deres hjem (se § 42, andre ledd). Så lenge barnet ikke blir utsatt for omsorgssvikt eller fare, må du lukke øynene for det meste.</p>""",
        "dumme_sporsmal": [
            {"q": "Kan jeg miste samværsretten helt?", "a": "Ja, men det skal svært, svært mye til. Selv om en forelder har vært voldelig i fortiden, vil domstolen ofte vurdere *beskyttet samvær* (med en vakt til stede, se § 43 a) fremfor å fjerne retten helt. Kun hvis selve samværet er en alvorlig fysisk eller psykisk fare for barnet, vil retten avsagt en kjennelse om at samværsretten \"oppheves\"."},
            {"q": "Må jeg levere barnet til samvær selv om barnet gråter og sier de ikke vil dra?", "a": "For små barn (under 12 år) må du gjøre alt som står i din makt (oppmuntre, trøste, lage positiv stemning) for å gjennomføre samværet. Du kan ikke bruke barnets motvilje som en \"lovlig\" grunn til å avlyse hver gang. Nekter en 15-åring, har barnet derimot så stor selvbestemmelse at verken du eller politiet vil tvinge 15-åringen inn i bilen."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "43", "tittel": "definisjonen på hvor *ofte* vanlig samvær skal være", "available": True},
            {"lov": "barnelova", "paragraf": "65", "tittel": "hvordan retten tvangs-gjennomfører et samvær ved hjelp av bøter", "available": True},
        ],
    },
    {
        "number": "42a",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Plikten til å varsle (og mekle) før du flytter innenlands",
        "kategori": "familie",
        "description": "Du kan flytte innenlands med barnet, men du har en streng plikt til å varsle eksen 3 måneder i forveien. Er dere uenige, tvinges dere til familiemekling.",
        "kort_svar": "Før en av foreldrene flytter med et barn i Norge (eller til utlandet), krever loven at du gir den andre forelderen skriftlig varsel senest 3 måneder (12 uker) før flyttingen faktisk skjer. Dersom den andre parten er uenig i at barnet skal flyttes, må den forelderen som ønsker å flytte, bestille time hos familievernkontoret for obligatorisk mekling.",
        "paragraftekst": """Dersom ein av foreldra vil flytte i Noreg eller ut av landet, og det er avtale eller avgjerd om samvær, skal den som vil flytte, varsle den andre seinast tre månader før flyttinga.

Er ikkje foreldra samde om flytting, må den av foreldra som vil flytte med barnet krevje mekling etter § 51.""",
        "hva_betyr_html": """<p>Paragraf 37 gir deg rett til å flytte med barnet innenfor Norges grenser. Denne paragrafen, 42 a, er sikkerhetsventilen som beskytter den forelderen som blir sittende igjen. Hvis du vil flytte fra Oslo til Trondheim, kan du ikke bare kjøpe en billett, melde flytting i Folkeregisteret og forsvinne over helgen.</p>
<p>Tre-måneders-fristen er absolutt. Loven ble skjerpet (fra tidligere seks uker) nettopp for å gi samværsforelderen et skikkelig vindu til å reagere. Tiden skal brukes til å tenke, snakke sammen, finne ut av nye reiseordninger, eller — i verste fall — reise en hastesak i tingretten for å stoppe flyttingen (krav om overføring av daglig omsorg/fast bosted før flyttelasset pakkes).</p>
<p>Og loven stopper ikke ved varselet: Hvis du gir beskjed ("Hei, vi flytter til Trondheim 1. oktober"), og faren sender en melding tilbake: "Nei, det godtar jeg ikke, det ødelegger barnets liv og mitt samvær", så slår ledd to inn. Da er det <em>du</em> (den som vil flytte) som har ansvaret for å kontakte det lokale familievernkontoret for å kreve mekling.</p>
<p>Dere må da møte opp hos en terapeut og diskutere saken. Du får ikke lov til å endre barnets bostedsadresse hos Skatteetaten før meklingen er gjennomført.</p>
<h3>Hva skjer hvis du gjør feil?</h3>
<p>Det er ingen "straff" i form av bøter eller fengsel for å bryte fristen på tre måneder (for innenlands flytting). Men det gir deg to kjempeproblemer: For det første vil et brudd på § 42 a se elendig ut i en eventuell rettssak; dommeren vil vurdere deg som en sabotør som mangler "foreldreevne til samarbeid". Det kan tippe en dommer til å la barnet bo hos faren i stedet. For det andre har ikke Skatteetaten lov til å endre folkeregistrert adresse på barnet hvis de får vite at meklingen mangler.</p>""",
        "eksempler": [{"navn": "Varsel og mekling", "tekst": "Hanne (bostedsmor) og Tom (samværsfar) bor i Bergen. Hanne forelsker seg i Per, som bor i Kristiansand. I mai sender hun Tom en e-post om at hun og barna skal flytte til Kristiansand innen skolestart i august. Tom protesterer vilt. Siden de er uenige, har Hanne en plikt til å kalle inn til mekling. Hun ringer Familievernkontoret og får en time om tre uker. Der krangler de, men klarer å bli enige om en ny, dyr samværsavtale der Tom flyr til dem to ganger i måneden, med avtale om reisekostnader. Flyttingen er lovlig varslet og håndtert, og hun kan reise."}],
        "vanlige_feil": ["Flytte først, og fortelle det til eksen etterpå. (Bryter loven, anses som konfliktfremmende adferd).", "Varsle fire uker før man flytter. (Tre måneder er et absolutt minimum).", "Den som vil flytte overser kravet om mekling, og bare reiser når eksen er uenig."],
        "hva_bor_du_html": """<p>Straks du begynner å lukte på muligheten for å flytte, bør du varsle skriftlig (e-post, melding). Formuler varselet hyggelig og saklig. Oppgi spesifikk dato for utflytting, ny by og konsekvenser.</p>
<p>Er du samværsforelder som mottar et slikt varsel og du er knusende uenig: Si ifra skriftlig umiddelbart ("jeg protesterer"). Da overfører du ansvaret for å oppsøke familievernkontoret over på eksen.</p>""",
        "dumme_sporsmal": [
            {"q": "Må jeg varsle 3 måneder før selv om jeg bare skal flytte fem gater opp i samme bydel?", "a": "Hvis du bare bytter fra en gate til en annen innenfor samme nabolag/skolekrets, påvirkes verken samvær, skolehverdag eller rutiner på noen meningsfylt måte. Hensikten med loven er å fange opp reelle geografiske forflytninger. Domstolene anser normalt ikke et hopp på et par kilometer (som ikke trigger buss/tog-behov for eksen) som en reell \"flytting\" i barnelovens forstand. Du bør uansett sende en SMS av høflighet, men mekling inntrer neppe for noe slikt."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "37", "tittel": "selve retten til å faktisk flytte som bostedsforelder", "available": True},
            {"lov": "barnelova", "paragraf": "40", "tittel": "den mye strengere regelen for å flytte ut av landet (som krever samtykke, ikke bare varsling)", "available": True},
            {"lov": "barnelova", "paragraf": "51", "tittel": "selve meklingsprosessen dere må igjennom", "available": True},
        ],
    },
    {
        "number": "43",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hva er vanlig samvær (omfanget)?",
        "kategori": "familie",
        "description": "Hvor mange dager skal barnet være hos far eller mor? Loven overlater detaljene til dere, men definerer i detalj hva en \"vanlig samværsrett\" består av.",
        "kort_svar": "Foreldrene avtaler selv hvor ofte barnet skal ha samvær (alt fra ingenting til 50/50). Loven har en ferdig, klassisk definisjon på hva som er \"vanlig samværsrett\": En ettermiddag i uken pluss overnatting annenhver helg, tre uker i sommerferien, og annenhver ferie (jul, påske og høst/vinter).",
        "paragraftekst": """Den av foreldra som barnet ikkje bur saman med, har rett til samvær med barnet om ikkje anna er avtala eller fastsett. Omfanget av samværsretten bør avtalast nærare. Dersom samvær ikkje er til beste for barnet, må retten avgjere at det ikkje skal vere samvær.

Foreldra avtalar sjølve omfanget av samværsretten på bakgrunn av kva dei meiner er best for barnet. § 31 andre stykket gjeld for foreldra. I avtale eller avgjerd om samvær skal det mellom anna leggjast vekt på omsynet til best mogleg samla foreldrekontakt, kor gammalt barnet er, i kva grad barnet er knytt til nærmiljøet, reiseavstanden mellom foreldra og omsynet til barnet elles. Vert det avtala eller fastsett «vanleg samværsrett», gjev det rett til å vere saman med barnet ein ettermiddag i veka med overnatting, annakvar helg, til saman tre veker i sommarferien, og annankvar haust-, jule-, vinter- og påskeferie.

Det kan i avtale eller i dom setjast vilkår for samvær. Dersom tilsyn blir sett som vilkår, kan retten utpeike ein person som skal føre tilsyn under samværet, eller be foreldra gjere det. Den av foreldra som skal ha samvær, dekkjer kostnadene til tiltaka som er sett som vilkår for samvær etter denne føresegna.

Den andre av foreldra skal få melding i rimeleg tid føreåt når samværet ikkje kan finne stad som fastsett, eller når tida for samværet må avtalast nærare.

Dersom den som har foreldreansvaret eller som barnet bur hos hindrar at ein samværsrett kan gjennomførast, kan den som har samværsretten krevje ny avgjerd av kven som skal ha foreldreansvaret eller kven barnet skal bu saman med, jf. § 63.""",
        "hva_betyr_html": """<p>Paragrafen ramser opp rammene for hvordan man koker sammen en samværsavtale i praksis.</p>
<p>Loven bygger på avtalefrihet (andre ledd). Foreldrene setter seg ned, ser på barnet, og bestemmer hva som er best. En 1-åring tåler kanskje ikke overnatting. En 15-åring vil kanskje bo hos far fem dager og mor ni dager. Reiser en av foreldrene to timer med buss hver vei for å jobbe skift, må samværet speile det.</p>
<p>Men ofte vet ikke foreldre hvor de skal starte. Kanskje signerer de bare et dokument som sier "Samvær etter loven" eller "Vanlig samvær". Denne paragrafen fyller slike uklare setninger med en skreddersydd kalender for dere. "Vanlig samvær" er fra og med 2018-endringene i barneloven utvidet. En "vanlig" samværsavtale gir nå den andre forelderen:</p>
<ul><li>Annenhver helg (typisk fredag til søndag)</li><li>Én ettermiddag med overnatting i løpet av uken (hver uke, hele året)</li><li>3 hele uker sommerferie</li><li>Halvparten av alle feriene som jul (annenhver jul), påske (annenhver) pluss høst- og vinterferie.</li></ul>
<p>Paragrafens fjerde ledd minner dere på å være voksne folk. Skal far avlyse helgen, må han sende melding til mor "i rimeleg tid" — han kan ikke sitte på hendene til klokken blir fem over fire på fredag.</p>
<p>Det femte leddet er "Sabotasje-regelen". Hvis en bitter mor over lang tid bevisst gjør seg utilgjengelig, gjemmer barnet, eller bare sier "barnet er sykt" hver gang det er pappas helg, har pappaen en drastisk lovlig utvei. Da sier loven rett ut at han kan gå til domstolen og si: "Hun saboterer samværet, flytt daglig omsorg (fast bosted) til meg i stedet." Sabotasje er en av de få feilene en bostedsforelder kan gjøre som får en dommer til å bruke tvang for å flytte et barn.</p>""",
        "eksempler": [{"navn": "Standardavtalen i NAV", "tekst": "Morten og Lise bor tre minutter fra hverandre i samme by. Lise mener 50/50 er best, Morten vil ha barnet 100 %. De møtes på familievernkontoret. Mekleren råder dem til å falle ned på noe midt i mellom (slik at barnet får bo ett sted) som de kan starte med, og drar frem § 43 \"vanlig samvær\". De signerer. Uken til barnet ser slik ut for Morten (bosted): Barnet sover hos ham hver dag, bortsett fra hver tirsdag, pluss at fredag-søndag faller bort annenhver helg. Morten merker snart at samværet er forvirrende for barnet (\"overnatter jeg her i dag?\"), og de prøver heller å samle nettene til én stor samværsbolk senere. Loven gir dem frihet til å endre avtalen når de vil."}],
        "vanlige_feil": ["Bostedsforelderen nekter samvær og tror domstolen bare vil hente inn purringer. (Sabotasje kan koste deg hele barnet).", "Bruke \"vanlig samvær\" for små babyer og småbarn, der overnatting to steder ikke anbefales av psykologer i det hele tatt, istedenfor hyppige, korte dagsbesøk."],
        "hva_bor_du_html": """<p>Bruk den "vanlige" avtalen (annenhver helg, en overnatting, 3 uker ferie) som et utgangspunkt når dere tegner avtaler. Er avstanden stor, dropp den faste ukenatten med overnatting og legg kanskje til en inneklemt langhelg en gang i måneden i stedet.</p>
<p>Hvis eksen din avlyser gjentatte ganger (fjerde ledd), ikke begynn å skrike i telefonen. Send en bekreftende SMS: "Forstår at du avlyser igjen, synd". Dette skaper en datert logg du kan bruke hvis saken går til domstolen for brudd på pliktene.</p>""",
        "dumme_sporsmal": [
            {"q": "Hvorfor står det at forelderen som skal ha samvær, dekker kostnaden for samvær med tilsyn (tredje ledd)? Hva koster en vakt?", "a": "Settes det et vilkår om at foreldrene betaler et familiemedlem eller en uavhengig person som vakt under samvær, legges kostnaden på den som krever samværet. I dag benyttes oftest offentlig tilsyn fra barnevernet/staten i slike saker (se § 43 a), og da er tilsynet gratis."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "63", "tittel": "saksgang for å flytte bostedet hvis eksen din saboterer", "available": True},
        ],
    },
    {
        "number": "43a",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Samvær med tilsyn (vakt)",
        "kategori": "familie",
        "description": "Frykter du for barnets sikkerhet hvis det har samvær med den andre forelderen? En domstol kan pålegge at det brukes en vakt, kalt beskyttet eller støttet tilsyn.",
        "kort_svar": "Hvis det er vurdert som en risiko (f.eks. på grunn av vold eller rus) for barnet å være alene med en forelder på samvær, men retten mener samvær likevel er best, kan de sette \"tilsyn\" som vilkår. Barnevernet eller staten utnevner da en person som passer på (beskyttet tilsyn) eller støtter faren/moren (støttet tilsyn) mens samværet pågår. Dette er gratis.",
        "paragraftekst": """Dersom tilsyn blir sett som vilkår for samværet, kan retten i særlege høve og der omsynet til barnet sine behov talar for det, påleggje kommunal barnevernsteneste eller departementet å oppnemne ein person som skal føre tilsyn under samvær. Retten kan gje pålegg om beskytta tilsyn eller støtta tilsyn.

Pålegget skal fastsetje dei nødvendige vilkåra for samværet, under dette timetalet og avgrensa varigheit.

Den kommunale barnevernstenesta oppnemner dei personane som skal føre tilsyn, og følgjer opp saka ved pålegg om beskytta tilsyn. Departementet oppnemner dei personane som skal føre tilsyn, og følgjer opp saka ved støtta tilsyn.

Før avgjerda blir fatta, skal retten hente inn ei konkret vurdering frå den kommunale barnevernstenesta eller departementet om korleis pålegget kan gjennomførast.

Eit pålegg kan følgje av ein dom, ei førebels avgjerd etter § 60 eller av eit rettsforlik. Dom og førebels avgjerd skal retten grunngi som nemnt i tvisteloven § 19-6. Om rettsavgjerda blir heva ved rettsforlik, skal retten gjere greie for føremålet med tilsynet og behovet til barnet.

Det offentlege dekkjer kostnadene til tiltaka etter denne føresegna.

Den som skal oppnemnast til å føre tilsynet etter andre ledd, skal leggje fram tilfredsstillande politiattest som nemnt i politiregisterloven § 39 første ledd.

Departementet kan gje forskrifter med nærare føresegner om mellom anna oppnemning av personar som skal føre tilsynet, utøvinga av tilsynet, godtgjering, rapportering og kravet om politiattest.""",
        "hva_betyr_html": """<p>Paragrafen tar for seg sakene der det er farlig eller svært utrygt for barnet å treffe far eller mor. Kanskje faren ruser seg, kanskje mor har vært psykotisk, eller kanskje en forelder har utøvd vold tidligere. Hovedregelen sier da egentlig "nei til samvær".</p>
<p>Men av og til vurderer dommeren at det er skadelig for barnet å miste kontakten med forelderen fullstendig. Da velger retten et kompromiss: Tilsyn. Tilsyn betyr at samværet gjennomføres, men under streng kontroll og i et begrenset antall timer (for eksempel 16 timer i året).</p>
<p>Loven opererer med to nivåer av tilsyn, basert på hvor høy risikoen er:</p>
<p><strong>1. Beskyttet tilsyn</strong> Dette er det strengeste. Beskyttet tilsyn brukes når barnet direkte må beskyttes mot vold, seksuelle overgrep eller bortføring. Det kommunale barnevernet gjennomfører dette. En trent barnevernsvakt (ofte flere) overvåker hvert eneste sekund og avbryter fysisk hvis forelderen sier noe stygt, griper fatt i barnet, eller forsøker å gå mot døren.</p>
<p><strong>2. Støttet tilsyn</strong> Dette er for foreldre som ikke utgjør en akutt sikkerhetsrisiko, men som er ujevne. Kanskje en far med mild rusavhengighet som sliter med å trøste babyen, eller en mor som er deprimert. Da oppnevner staten (Bufdir/Departementet) en tilsynsperson. Denne personens jobb er å sitte i sofaen sammen med dem, støtte forelderen, rettlede dem i samværet, og sørge for at barnet har det bra.</p>
<p>For å unngå at barnevernet kveles av slike saker, sier loven at et pålegg om tilsyn aldri er evigvarende. Dommeren må sette en absolutt grense, for eksempel "Tilsyn i to timer hver tredje uke, i maksimalt ett år". Når året er gått, må samværet enten opphøre (hvis forelderen fortsatt er farlig), eller fungere normalt uten vakt.</p>
<p>Kostnadene tar det offentlige. Den som utfører tilsynet (vakten) må også kunne fremlegge politiattest, slik at man er sikker på at personen som skal beskytte barnet, selv har rent rulleblad.</p>""",
        "eksempler": [{"navn": "Samvær med mor etter rusavrusning", "tekst": "Lise er rusavhengig. Datteren Emma bor hos faren sin, Pål. Lise ønsker samvær, men Pål nekter, av frykt for at Lise skal møte opp ruset og skremme jentungen. Saken går til retten. Retten mener Lise har vist stor forbedring og trenger kontakt, men er enig med Pål i risikoen. Dommeren pålegger *støttet tilsyn* for Lise. Lise får se datteren fire timer annenhver måned på et nøytralt samværssenter. Bufdir stiller med en barnevernspedagog som overvåker møtet og hjelper Lise. Siden pålegget gis av retten, kan ikke Pål lenger nekte Lise denne typen samvær."}],
        "vanlige_feil": ["Bostedsforeldre som påstår eksen er \"farlig\", og nekter å levere barnet til samvær uten tilsyn. Husk: Du kan ikke kreve offentlig tilsyn privat. Tilsyn etter § 43 a kan kun iverksettes hvis det står i en domstolskjennelse eller i et rettsforlik etter en rettssak (se femte ledd)."],
        "hva_bor_du_html": "<p>Dersom du mener at eksen din er farlig, men du også forstår at dommeren sannsynligvis vil tvinge gjennom samvær uansett, er det bedre at du, via advokaten din, aktivt foreslår tilsyn i retten fremfor å bare be om null samvær og tape hele saken. Går du i rettsforlik (enighet med dommeren i rommet), kan dere skrive en avtale om tilsyn med én gang, så lenge dommeren begrunner hvorfor. Barnevernet må kontaktes før blekket tørker.</p>",
        "dumme_sporsmal": [
            {"q": "Hvor møtes de? På gaten?", "a": "Nei, for beskyttet tilsyn har Bufetat og barnevernet spesielle samværslokaler utstyrt for formålet (med låste dører, sofagrupper, leker og kamera). For støttet tilsyn kan det noen ganger være i offentligheten (en isbar, lekeplass) avhengig av hva dommeren tillot."},
            {"q": "Betyr støttet tilsyn at vakten kan si fra hvis faren kjefter?", "a": "Ja, vakten kan, og skal, avbryte samværet umiddelbart og fjerne barnet hvis forelderen oppfører seg uforsvarlig. Tilsynsføreren skriver deretter en rapport om det som skjedde, og dette legges ved en eventuell senere rettssak."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "60", "tittel": "dommerens \"førebels avgjerd\" (midlertidige dom) hvor slikt tilsyn settes inn mens rettssaken pågår", "available": True},
            {"lov": "barnelova", "paragraf": "43", "tittel": "frivillig betalt tilsyn fra f.eks. besteforeldre (hvis foreldrene vil unngå barnevernet)", "available": True},
        ],
    },
    {
        "number": "43b",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Kan du ha samvær hvis du har kontakt- eller besøksforbud?",
        "kategori": "familie",
        "description": "Har politiet eller domstolen gitt den ene forelderen et forbud mot å oppsøke barnet? Da gjelder forbudet over alt annet, også gamle samværsavtaler.",
        "kort_svar": "Hvis en forelder har fått et strafferettslig kontaktforbud eller besøksforbud mot barnet sitt, mister den forelderen umiddelbart all rett til samvær. Dette gjelder selv om de hadde en gyldig samværsavtale i barneloven før forbudet ble ilagt.",
        "paragraftekst": "Den som har forbod mot kontakt med eit barn etter straffeloven § 57 eller straffeprosessloven § 222 a, kan ikkje ha samvær med barnet etter avtale eller avgjerd. Dette gjeld likevel ikkje om forbodet etter nærare føresegner gjev høve til det.",
        "hva_betyr_html": """<p>Noen ganger foregår familieretten (barneloven) og strafferetten (politi og domstol) parallelt, og de krasjer.</p>
<p>Tenk deg at far fikk samvær i en rettssak. Seks måneder senere slår han barnet eller utøver vold mot mor mens barnet ser på. Politiet rykker ut, sikter far for vold, og gir ham et "besøksforbud etter straffeprosessloven § 222 a" mot sin egen familie for å beskytte dem i tre måneder mens de etterforsker.</p>
<p>Da får vi et paradoks. Far vifter med barneloven og sier: "Jeg har en dom her som sier jeg skal ha barnet denne helgen!". Paragraf 43 b løser floken én gang for alle: Besøksforbudet fra politiet/straffedomstolen knuser samværsavtalen fra familieretten. Faren "kan ikkje ha samvær", og han bryter loven hvis han prøver å møte opp, uansett hva familiedommeren mente et halvår tidligere.</p>
<p><strong>Unntaket for spesifikke samvær</strong> I straffesaken kan dommeren der (som ila forbudet) noen ganger bygge inn en liten åpning. Dommeren kan skrive: "Besøksforbud mot mor og datter på et år, men med unntak for støttet samvær med barnevernet etter barneloven § 43 a hver fjerde uke". Slike unntak respekteres av loven.</p>""",
        "eksempler": [{"navn": "Forbudet ved skolen", "tekst": "Thomas har en gyldig dom på \"vanlig samvær\" med datteren sin. Etter gjentatte drapstrusler mot ekskona, fatter politiet et besøksforbud som inkluderer datteren, slik at Thomas må holde seg minst 100 meter unna datterens skole og hus. På fredag parkerer Thomas 105 meter unna skolen og sender datteren en melding: \"Kom hit, det er samværshelg\". Han bryter § 43 b fordi samværet har forfalt, og han vil bli arrestert for brudd på besøksforbudet hvis mor ringer politiet."}],
        "vanlige_feil": ["Truet bostedsforelder sender barnet til far i samværshelgen av frykt for å bli beskyldt for \"samværssabotasje\", selv om hun nettopp har fått politiet til å ilegge faren besøksforbud. (Mor må holde barnet hjemme).", "Samværsfar anmelder mor for samværssabotasje under et løpende kontaktforbud. Anmeldelsen vil henlegges umiddelbart."],
        "hva_bor_du_html": "<p>Har du fått innvilget et besøksforbud eller kontaktforbud som inkluderer barnet? Da trenger du ikke gjøre noe mer med samværsavtalen foreløpig. Du overholder bare forbudet, stanser samværet og holder barnet hjemme. Strafferetten gir deg ryggdekning. Du kan imidlertid, når roen har lagt seg, starte en sak i domstolen for å få avtalen slettet permanent i en dom etter barneloven, for når politiets besøksforbud (ofte 3-6 mnd) utløper, blusser samværsplikten formelt sett opp igjen.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om besøksforbudet gjelder meg (mor), men far vil at jeg skal hente barnet på SFO?", "a": "Gjelder besøksforbudet kun at far ikke får nærme seg *deg* (mor), men det inkluderer ikke barnet? Da har faren faktisk fremdeles rett på samvær med barnet sitt. Det må bare arrangeres på en måte hvor dere to ikke møtes, for eksempel at faren henter i barnehagen eller hos en venn. Hvis politiet mener faren er farlig for deg, men helt trygg for barnet, kan de skille de to."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "43", "tittel": "den vanlige retten til samvær", "available": True},
        ],
    },
    {
        "number": "44",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvem skal betale for reisen når barnet skal på samvær?",
        "kategori": "familie",
        "description": "Samvær koster penger når foreldrene bor i hver sin by. Lovens hovedregel er at mor og far skal dele reiseutgiftene ut fra hva de tjener.",
        "kort_svar": "Foreldrene skal dele de nødvendige reisekostnadene barnet (og en følgeperson) har ved samvær. Dere deler utgiftene forholdsmessig etter hvor mye dere tjener. Tjener du 60 % av foreldrenes totale inntekt, betaler du 60 % av flybilletten. Er dere uenige, kan dere la NAV fastsette brøken og kreve inn pengene.",
        "paragraftekst": """Reisekostnadene ved samvær skal delast mellom foreldra etter storleiken på inntektene deira der foreldra ikkje blir samde om noko anna. Kostnadene som skal delast, er kostnader til barnet si reise, foreldra sine nødvendige kostnader til reise i samband med å hente eller bringe barnet til samværet og samværsforelderen sine kostnader til eiga reise når samværet skjer der barnet bur. Reglane i § 70 sjuande ledd gjeld så langt dei høver.

Dersom særlege grunnar gjer det rimeleg, kan retten fastsetje ei anna fordeling av reisekostnadene. Er foreldra samde om det, kan sak om reisekostnadene i staden gå til arbeids- og velferdsetaten. Har barnet fylt 15 år, kan sak om reisekostnader gå til arbeids- og velferdsetaten jamvel om berre ein av foreldra ber om det. Reglane i § 63 gjeld tilsvarande. Arbeids- og velferdsetaten sitt vedtak er tvangsgrunnlag for utlegg.

Når begge foreldra ber om det, kan arbeids- og velferdsetaten fastsetje at ei skriftleg avtale om deling av reisekostnader skal kunne tvangsfullførast ved utlegg etter tvangsfullbyrdelsesloven kapittel 7.""",
        "hva_betyr_html": """<p>Paragraf 44 rydder opp i en enormt vanlig krangel: "Det var <em>du</em> som valgte å flytte til Alta, jeg bor i Oslo, du får faen meg betale for flybilletten hans selv".</p>
<p>Loven sier at kostnaden for at barnet reiser til samvær (tog, fly, bensin) ikke er samværsforelderens problem alene. Kostnadene skal splittes. Regelen er "brøkdeling etter inntekt". Tjener far mye, og mor lite, skal far betale nesten hele togbilletten, uavhengig av hvem som flyttet.</p>
<p>Utgifter som kan deles:</p>
<ul><li>Billetten til barnet</li><li>Forelderens flybillett hvis barnet (under 12-15 år) ikke kan reise alene, og forelderen reiser tur-retur som "eskokte".</li><li>Pappas flybillett hvis barnet er i barnehage og nekter å sove borte, og pappa må fly opp til barnets hjemby for å ha "dagsamvær" på lekeland.</li></ul>
<p>Det andre leddet har et unntak ("særlege grunnar"): Hvis mor flyttet til Alta ene og alene fordi hun hatet far og ville ødelegge samværet, selv om hun ikke hadde jobb der oppe, <em>kan</em> retten nekte å la far betale for Hannes barnslige flukt. Da kan retten dømme mor til å dekke hele billetten for barnet sitt.</p>
<p>Blir dere ikke enige, trenger dere ikke advokat. NAV (Arbeids- og velferdsetaten) kan beregne en fast inntektsbrøk for dere, slik at regningen blir ferdig delt hver måned.</p>""",
        "eksempler": [{"navn": "Billetten til Tromsø", "tekst": "Pappa bor i Tromsø, og barna bor med mor i Trondheim. Barna reiser opp til Tromsø en gang i måneden, noe som koster 4 000 kroner per tur. Pappa tjener 800 000 kr i året (80 % av totalinntekten), mor tjener 200 000 kr i året (20 % av totalinntekten). Pappa legger ut for billetten. Deretter krever han inn 800 kroner fra mor (20 % av 4000) for at de skal være i tråd med § 44. Mor kan ikke nekte. Nekter mor å betale de 800 kronene, kan pappa klage til NAV, som gjør et tvangsinntrekk i mors lønn etter bestemmelsen i tredje ledd."}],
        "vanlige_feil": ["Bostedsforelder nekter å betale, med argumentet \"han har råd til det\". (Brøken regnes ut, en millionærfar vil betale mye, men du slipper sjelden unna med *null* med mindre du lever under fattigdomsgrensen).", "Samværsfar sender regning for kaffe og pølser på flyplassen (loven dekker kun *reisekostnader*, ikke forbruk).", "Legge alt opp i statens hender for bilkjøring. (Hver gang man krysser bygrensen oppstår tvist om bompenger og km-pris — avtal et sjablongbeløp på forhånd)."],
        "hva_bor_du_html": """<p>Prøv først å lage en privat avtale. Regn ut fjorårets bruttoinntekter på kalkulatoren, og del opp prosenten. Er pappa for lat til å kjøre frem og tilbake hver helg selv, men krever at mor som jobber skift skal levere i Oslo? Husk at loven kun fastsetter hvem som <em>betaler</em> for reisen, ikke hvem som skal <em>kjøre</em> (stå for selve bringingen). (Praksis er at samværsforelder normalt henter og bringer).</p>
<p>Trenger dere hjelp, gå til NAVs kalkulator for reisekostnader.</p>""",
        "dumme_sporsmal": [
            {"q": "Får jeg trekt fra reisekostnadene mine direkte på barnebidraget mitt?", "a": "Dette gjøres ofte praktisk, men de to er juridisk sett to adskilte regnestykker. I utregningen av barnebidrag hos NAV settes det opp et fast \"samværsfradrag\" etter antall dager barnet er hos deg. Reisekostnader er en egen utgift der NAV kan lage et tilleggsvedtak. Er din andel av reisen 3 000 kr, men hun nekter å betale, vil NAV trekke henne, ikke barnebidraget ditt direkte."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "43", "tittel": "antall turer du faktisk har rett på", "available": True},
            {"lov": "barnelova", "paragraf": "70", "tittel": "barnebidragskostnaden regnes ofte med den samme inntektsbrøken", "available": True},
        ],
    },
    {
        "number": "45",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Rett til samvær for besteforeldre og andre slektninger",
        "kategori": "familie",
        "description": "Har besteforeldre krav på å se barnebarna sine etter en skilsmisse? Normalt nei, men loven åpner to dører der besteforeldre kan få samvær i en domstol.",
        "kort_svar": "Som hovedregel har ikke besteforeldre en selvstendig rett til samvær i Norge. Men, hvis én eller begge av barnets foreldre er døde, kan besteforeldre kreve samvær gjennom domstolen. I tillegg, hvis foreldrene krangler og én forelder nektes samvær, kan den nektede forelderen kreve at besteforeldrene får samvær i stedet.",
        "paragraftekst": """Når den eine av foreldra eller begge er døde, kan slektningane til barnet eller andre som er nær knytte til barnet, krevje at retten fastset om dei skal ha rett til å vere saman med barnet, og kva for omfang samværsretten skal ha.

I sak om samværsrett mellom foreldra, kan ein forelder som vert nekta samvær krevje at avgjerdsorganet fastset om hans eller hennar foreldre skal ha rett til å vere saman med barnet og kva for omfang samværsretten skal ha. Samvær for besteforeldra kan berre fastsetjast på vilkår av at den som er nekta samvær ikkje får møte barnet.

Reglane i kap. 7 gjeld også for desse sakene. Det krevst ikkje at partane har vore til mekling før dei går til sak.""",
        "hva_betyr_html": """<p>Paragraf 45 er en unntaksregel. Det store prinsippet i barneloven er at barnet har rett til kontakt med mor og far (§ 42). Farmor eller farfar har ingen juridiske rettigheter til å blande seg inn i familien bare fordi svigerdatteren holder dem unna etter et samlivsbrudd. En "vanlig" farmor har ikke rett til å gå til domstolen og kreve samvær med barnebarnet sitt hvis barnets foreldre lever.</p>
<p>Loven gir kun to unntak:</p>
<p><strong>1. Dødsfall (første ledd)</strong> Dersom barnets mor dør, og far overtar ansvaret og nekter mormor (morens mor) å se barnet, mener loven at mormor må få hjelp. Barnets bånd til den avdøde morens familie står i fare for å bli brutt. I dette tilfellet (hvor en forelder er død), kan besteforeldrene, tanter, eller en steforelder som var nær barnet, saksøke den gjenlevende faren. Retten vil da fastsette en begrenset samværsrett (for eksempel én helg i måneden).</p>
<p><strong>2. Substitutt-samvær for nektet forelder (andre ledd)</strong> Dette gjelder ved samlivsbrudd. Far drar til retten og krever samvær med barnet sitt. Mor peker på at faren er tungt rusmisbruker. Dommeren sier seg enig: Faren er for farlig, og nektes alt samvær. Da kan faren reise seg opp og kreve: "Greit, jeg kan ikke ha barnet. Men jeg krever at foreldrene mine (besteforeldrene) skal få se barnet". Dommeren kan da innvilge samvær til farmor og farfar, slik at barnet i det minste får kjenne farsslekten. Men: Dommeren setter det som et absolutt vilkår at faren selv ikke får oppholde seg i huset til besteforeldrene når barnet er der ("surrogat-samvær").</p>
<p>Det siste leddet gjør saken enklere for besteforeldre ved at de slipper å gå til mekling (på familievernkontoret) før de saksøker eks-svigerbarnet sitt. De kan gå rettens vei.</p>""",
        "eksempler": [{"navn": "Mormors rett", "tekst": "Siri (mor til lille Emma) og Tom er gift. Siri omkommer i en ulykke. Tom faller sammen, blir bitter på Siris foreldre (mormor og morfar), og stenger dem helt ute av Emmas liv. Seks måneder senere stevner mormor Tom for tingretten og påberoper seg § 45 første ledd. Siden Siri er død, kan slektningene kreve samvær. Dommeren konkluderer med at det er sunt for Emma å kjenne morsslekten sin, og dømmer Tom til å la Emma besøke mormor annenhver søndag."}],
        "vanlige_feil": ["Besteforeldre sender advokatbrev til svigerdatteren fordi hun nekter dem å se barnet etter skilsmissen. (Koster penger, svigerdatteren kan bare kaste brevet; besteforeldre har ikke lov til å saksøke så lenge sønnen deres lever og kan kjempe kampen selv).", "Faren som fikk \"substitutt-samvær\" til sine foreldre, sitter i sofaen hos foreldrene sine hver gang barnet er der. (Ulovlig, han bryter dommen, og mor vil fjerne besteforeldrenes samvær umiddelbart i neste rettsinstans)."],
        "hva_bor_du_html": """<p>Er du en farmor eller mormor som blir stengt ute etter en normal skilsmisse? Din eneste juridiske vei inn, er at sønnen eller datteren din krever tid med barna gjennom sin egen samværsrett. Hvis de vinner frem, kan dere be dem om å legge besøkene til deres hus.</p>
<p>Er barnet etterlatt etter et dødsfall og du frykter at faren/moren vil fryse dere ut, ikke vent for lenge med å opprette kontakt via advokat og rettssystem. Barnets tilknytning blekner fort.</p>""",
        "dumme_sporsmal": [
            {"q": "Kan besteforeldre kreve samvær hvis barnevernet har tatt barnet?", "a": "Ja, men da er ikke barneloven lenger den riktige lovboken. Da reguleres barnets situasjon av barnevernsloven, som har egne og svært strenge regler (barnevernsloven § 7-2) for at barnevernet kan innvilge slektninger \"kontakt\" med et fosterbarn, så lenge det ikke ødelegger fosterhjemsplasseringen."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "38", "tittel": "hvem som automatisk får barnet ved dødsfall (slik at besteforeldre vet hvem de må saksøke)", "available": True},
            {"lov": "barnelova", "paragraf": "64", "tittel": "regelen om at besteforeldre noen ganger kan saksøke for å få foreldreansvaret helt og holdent", "available": True},
        ],
    },
    {
        "number": "46",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Plikt til å høre samværsforelderen før store hindringer lages",
        "kategori": "familie",
        "description": "Har barnet fast bosted hos deg? Selv om du bestemmer mye, har du plikt til å la samværsforelderen si sin mening før du gjør samværet vanskeligere.",
        "kort_svar": "Før bostedsforelderen tar en stor avgjørelse som vil gjøre det vanskelig, eller umulig, for den andre forelderen å ha samvær med barnet (for eksempel bytte til en skole langt unna, eller flytte fritidsaktiviteter til pappas helger), skal samværsforelderen få uttale seg først.",
        "paragraftekst": "Den som har samværsrett med barnet, skal så langt råd er, få uttale seg før den som har foreldreansvaret, tek avgjerder som vil gjere det umogeleg eller vesentleg vanskelegare å utøve samværsretten.",
        "hva_betyr_html": """<p>Paragraf 37 gir en bostedsforelder veldig mye makt. Bostedsforelderen kan, alene, velge å bytte barnets skole eller fritidsaktiviteter. Paragraf 46 setter opp et lite gjerde rundt denne makten.</p>
<p>Gjerdet heter "uttalerett". Det betyr at hvis handlingen din kommer til å knuse eksens samværshelger — kanskje du vil melde barnet på en korpsøvelse som krever at barnet øver hver eneste lørdag kl. 10.00 — kan du ikke bare gjøre det i skjul.</p>
<p>Loven krever at du, "så langt råd er" (så fremt det er praktisk mulig), sender en e-post eller ringer faren og sier: "Jeg planlegger å melde Truls på dette korpset. Hva tenker du?".</p>
<p>Mange blander uttalerett med vetorett. Faren har <em>ikke</em> vetorett. Han kan ikke nekte deg å gjøre det. Hans makt stopper ved at han får si meningen sin. Skriver han tilbake "Det hater jeg, da rekker vi aldri hytteturen vår", kan du som bostedsforelder notere deg at han hater det, og likevel signere korps-kontrakten. Men ved å høre ham ut, har du fulgt loven, og du har kanskje åpnet for et kompromiss (kanskje pappa kjører til korpset på lørdager).</p>""",
        "eksempler": [{"navn": "Bytte av fotballklubb", "tekst": "Tom (far og samværsforelder) henter Siri (10 år) på fotballtrening i hjembygden kl. 17 hver torsdag, og de drar hjem til ham for å overnatte. Siri bor fast hos Hanne. Hanne vil bytte Siri til et elitelag en times kjøretur unna. Det vil gjøre det umulig for Tom å rekke treningen etter sin egen jobb. Før Hanne melder overgang, ringer hun Tom. Han protesterer, men Hanne tar beslutningen likevel. Hanne har fulgt § 46 (hun hørte ham først), og hun har retten på sin side etter § 37 (hverdagsmakt). Det er nå opp til Tom å reise saken for retten hvis han mener endringen er til skade for datteren."}],
        "vanlige_feil": ["Som bostedsforelder å melde barnet på cuper på pappas helger uten å fortelle ham det før terminlisten er spikret.", "Som samværsfar tro at denne paragrafen gir deg makt til å sette foten ned og stoppe flyttingen (uttalerett er ikke beslutningsrett)."],
        "hva_bor_du_html": "<p>Vil du bevare freden? Opprett en WhatsApp-gruppe eller bruk en app for deleforeldre, og skriv all viktig informasjon der. Når du skal bytte en fritidsaktivitet som berører samværshelgen, still et åpent spørsmål. Du oppfyller loven med ett tastetrykk.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om han nekter å ta telefonen eller svare på e-post, og fristen for påmelding går ut?", "a": "Loven sier \"så langt råd er\". Hvis du har gjort et reelt, ærlig forsøk på å kontakte ham (sendt en mail to uker i forveien), og han forblir taus, kan du trygt ta avgjørelsen. Loven krever ikke at du står og dunker på døren hans."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "37", "tittel": "selve makten til å bytte skole/aktiviteter", "available": True},
        ],
    },
    {
        "number": "47",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Retten til å få informasjon fra skolen og helsevesenet",
        "kategori": "familie",
        "description": "Nekter eksen å fortelle deg hvordan det går med barnet på skolen? Loven gir deg rett til å kreve utskrifter fra skole, lege og politi uavhengig av eksen din.",
        "kort_svar": "Som forelder (også uten foreldreansvar) har du krav på å få vite hvordan det går med barnet ditt. Du har rett til å få opplysninger direkte fra skolen, barnehagen, helsevesenet og politiet. Lærer og lege har plikt til å svare deg. Eneste unntak er hvis informasjonen kan sette barnet i fare.",
        "paragraftekst": """Foreldre som har foreldreansvar, har rett til opplysningar om barnet når dei bed om det. Har den eine av foreldra foreldreansvaret aleine, skal denne gje den andre opplysningar om barnet når det blir bede om det. Den andre har også rett til å få opplysningar om barnet frå barnehage, skule, helse- og sosialvesen og politi, om ikkje teieplikta gjeld andsynes foreldra. Slike opplysningar kan nektast gjeve dersom det kan vere til skade for barnet.

Avslag på krav om opplysningar etter første stykket tredje punktum kan påklagast til statsforvaltaren. Foreldre med foreldreansvar har tilsvarande klagerett. Reglane i forvaltningslova kapittel VI gjeld så langt dei høver, jamvel om avslaget er gjeve av private.

I særlege høve kan statsforvaltaren avgjere at den som ikkje har foreldreansvaret, skal tape opplysningsretten etter paragrafen her.""",
        "hva_betyr_html": """<p>Paragraf 47 er gullet til alle fedre (og mødre) som føler seg holdt utenfor etter et brudd. Kanskje eksen stenger deg ute, "glemmer" å videresende vitnemålet, eller nekter å si hva legesjekken viste.</p>
<p>Loven gir deg rett til å omgå eksen.</p>
<p><strong>For foreldre MED foreldreansvar:</strong> Siden du har full, juridisk bestemmelsesmakt, har skolen og helsestasjonen plikt til å gi deg alt de har. Ringer du kontaktlæreren og spør hvordan karakterene var, plikter skolen å gi deg svaret. Du har rett på kopi av alt som sendes i posten hjem.</p>
<p><strong>For foreldre UTEN foreldreansvar:</strong> Her er det mer komplisert. Har mor ansvaret alene, har hun for det første en personlig, lovfestet plikt til å fortelle deg hva som skjer i barnets liv hvis du spør. Svarer hun ikke, gir loven (tredje setning i første ledd) deg lov til å gå direkte til barnehage, skole, BUP og politiet. Du har ikke rett til å "bestemme" noe der (du mangler jo foreldreansvar), men du har rett til å få <em>fakta</em>. Er gutten ofte syk? Sliter han i matte? Men du får bare det du spesifikt spør om — skolen har ikke plikt til å automatisk sette deg på kopilisten for alle ukebrev, slik de må med de som <em>har</em> foreldreansvar.</p>
<p><strong>Unntaket for skade (teieplikt)</strong> Skole og helsevesen kan stenge døren for deg hvis du utgjør en fare. Mistenker legen at du har begått overgrep mot barnet, eller frykter rektor at du vil rømme med barnet hvis du får vite hvilken barnehage de er skjult på, har de lov til (og plikt til) å påberope seg "skade for barnet", og avslå forespørselen din. Gjør de det, kan du klage til Statsforvalteren. Finner Statsforvalteren at du er en reell trussel (tredje ledd), kan de fjerne informasjonsretten din for godt.</p>""",
        "eksempler": [{"navn": "Skolemeldingen", "tekst": "Tom har ikke foreldreansvar for Emma (7), men han har samvær hver onsdag. Emma sliter med skriving. Tom kontakter læreren for å få vite hvordan de jobber med lesing på skolen. Moren til Emma, som har ansvaret alene, har ringt skolen tidligere og krevd at læreren skal slette Toms nummer og nekte å snakke med ham fordi \"han har ingenting med det å gjøre\". Læreren slår opp i barneloven § 47, og ser at mor tar feil. Selv foreldre uten foreldreansvar har krav på fakta om skolegangen. Læreren svarer Tom, uavhengig av mors trusler."}],
        "vanlige_feil": ["Mor nekter rektor å informere far (mor har ikke den makten).", "Far krever at skolen alltid skal ringe ham når barnet er sykt, selv om han mangler foreldreansvar (skolen har opplysningsplikt når han spør, men de varsler primært bostedsforelderen).", "Ansatte i kommunen er livredde for GDPR og nekter faren med felles ansvar adgang til barnets journal. (GDPR overstyrer ikke barneloven her, forelderen har rett til innsyn)."],
        "hva_bor_du_html": "<p>Hvis eksen kveler informasjonsflyten: Finn kontaktinfo til barnets hovedlærer eller fastlege. Send en høflig, kort e-post. Vis direkte til \"Barnelova § 47\" i mailen, for mange lærere er ikke jurister og blir redde når de står i midten av en krangel. Spør konkret: \"Jeg ber herved om en kopi av min sønns utviklingssamtale, slik jeg har krav på etter barneloven\". Får du avslag, klag gratis til Statsforvalteren.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg få utlevert psykologjournalen til 16-åringen min?", "a": "Nei, da slår helselovgivningen (Pasientrettighetsloven) inn. Når barnet er over 16 år, gjelder taushetsplikten strengt mellom barnet (pasienten) og legen, og \"teieplikta gjeld andsynes foreldra\" (se lovteksten). Etter 16 år bestemmer ungdommen selv om du får vite hva de snakker med BUP om."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "30", "tittel": "foreldreansvaret i sin helhet", "available": True},
        ],
    },
    {
        "number": "48",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "\"Barnets beste\" er lovens viktigste regel",
        "kategori": "familie",
        "description": "Hvorfor taper mødre og fedre saker de trodde de hadde \"rett\" på? Fordi domstolen ikke bryr seg om dine rettigheter. Det eneste som teller, er hva som er best for barnet.",
        "kort_svar": "Når domstolen, barnevernet eller familievernet skal ta en avgjørelse om hvor barnet skal bo, samvær eller foreldreansvar, er det kun ett prinsipp som styrer valget: Hva som er til det beste for barnet. Barnets trygghet, inkludert beskyttelse mot vold og psykisk skade, trumfer alltid foreldrenes ønsker.",
        "paragraftekst": """Avgjerder om foreldreansvar, flytting med barnet ut av landet, kven barnet skal bu fast saman med og samvær, og handsaminga av slike saker, skal først og fremst rette seg etter det som er best for barnet.

Ved avgjerda skal det takast omsyn til at barnet ikkje må bli utsett for vald eller på anna vis bli handsama slik at den fysiske eller psykiske helsa vert utsett for skade eller fare.""",
        "hva_betyr_html": """<p>I all annen juss handler det om hva de voksne har krav på. Kjøper du en ødelagt bil, har du "rett" på pengene tilbake. Men i familieretten har du som voksen ingen "rett" til å eie et barn. Lovverket roterer utelukkende rundt barnet.</p>
<p>Denne paragrafen (sammen med Grunnloven § 104) kalles "Barnets beste-prinsippet". Den feier vekk alle dine egne argumenter i retten hvis de bare handler om rettferdighet for deg.</p>
<p>Hvis en far argumenterer: "Hun har hatt barnet i tre år, nå er det min tur til å ha barnet like mye, for likestillingens skyld!" – vil dommeren avvise argumentet. Likestilling betyr ingenting her. Det eneste dommeren spør om, er: "Vil barnet få et bedre liv av å bytte bosted nå?". Hvis svaret er nei, taper far, selv om det føles dypt urettferdig for ham.</p>
<p><strong>Voldsvernet (Andre ledd)</strong> Det andre leddet understreker at barnets sikkerhet er fundamentet i "barnets beste". Dommeren har en streng plikt til å sjekke om det foreligger vold (også psykisk vold og skremmende oppførsel). Har en far eller mor slått barnet, eller slått den andre forelderen foran barnet, er det i utgangspunktet ikke til barnets beste med samvær, uansett hvor mye barnet savner forelderen. Risikovurderingen står over alt annet.</p>""",
        "eksempler": [{"navn": "Flyttingen og stabiliteten", "tekst": "Kari og Tom er skilt. Sønnen Lukas (8) bor fast hos Kari i Kristiansand og har det fint der med fotball, skole og venner. Kari ønsker å flytte til Tromsø på grunn av en ny kjæreste. Tom krever da at fast bosted flyttes til ham i Kristiansand slik at Lukas slipper å flytte. Kari argumenterer i retten: \"Jeg er barnets mor, og barn har det best hos sin mor\". Dommeren slår opp i § 48. Myten om \"mors-presumpsjonen\" (at mor er best) ble fjernet fra norsk rett for mange tiår siden. Dommeren ser at \"barnets beste\" i dette tilfellet er stabilitet — å beholde skolen, kompisene og nærmiljøet. Dommeren flytter bostedet over til Tom, fordi det å rykke Lukas opp med roten ene og alene for mors kjærlighetsliv, ikke er til barnets beste."}],
        "vanlige_feil": ["Blande \"barnets beste\" med \"barnets vilje\". (Et barn kan ha lyst til å bo hos en pappa som lar dem spille Fortnite i stedet for å gjøre lekser, men dommeren vil anse det som skadelig og dømme barnet til å bo hos den strenge, strukturerte moren. Se forskjell på § 31 og § 48).", "Tro at retten \"straffer\" den som har vært utro eller slem i parforholdet. (Dommeren bryr seg ikke om hvem som hadde skylden for skilsmissen. De bryr seg bare om hvem som er den beste oppdrageren fremover)."],
        "hva_bor_du_html": "<p>Når du skriver brev til eksen, barnevernet eller domstolen, må du lære deg å \"snakke barneloven\". Stryk ord som \"jeg har rett til...\", \"jeg krever...\" og \"det er urettferdig for meg at...\". Skriv heller: \"Dette vil sikre at Emma får den stabiliteten hun trenger\", \"Gutten profitterer på å ha nærhet til skolen\" og \"Dette minsker konfliktnivået for jenta vår\". Bygg alle argumentene dine på hvorfor ditt forslag gir barnet et bedre liv, ikke hvorfor du fortjener å vinne. Da tenker du som en dommer.</p>",
        "dumme_sporsmal": [
            {"q": "Hvis barnets beste er det eneste som gjelder, hvorfor mister far ofte saker om små barn?", "a": "Det er ikke fordi loven favoriserer mor, men fordi psykologene (som rådgir dommeren) ofte mener at \"barnets beste\" for spedbarn og småbarn (under 3 år) er biologisk og psykologisk stabilitet hos den primære omsorgspersonen (som oftest er mor, spesielt ved amming). Å stykke opp barnets uke i 50/50 ansees ofte som direkte skadelig for barnets tilknytning før en viss alder."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "31", "tittel": "retten barnet har til å uttale seg, som veies tungt i vurderingen av barnets beste", "available": True},
            {"lov": "barnelova", "paragraf": "60", "tittel": "hastetiltakene retten kan sette inn (som besøksforbud) hvis voldsaspektet er akutt", "available": True},
        ],
    },
    {
        "number": "49",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Advokater plikter å vurdere forlik og mekling",
        "kategori": "familie",
        "description": "Advokater lever av å kjøre saker i retten. Men i familieretten sier loven at advokatene har plikt til å dytte foreldrene mot en fredelig, utenrettslig løsning.",
        "kort_svar": "Før en sak om barn havner i retten, skal advokater som er involvert i saken fortløpende vurdere om konflikten kan løses ved forlik (avtale). Advokaten plikter også å opplyse deg om at det er mulig å mekle hos Familievernet.",
        "paragraftekst": "Advokatar som har saker etter kapitlet her, bør vurdere om det er mogeleg for partane å kome fram til ei avtaleløysing. Advokaten skal opplyse foreldra om høvet til mekling.",
        "hva_betyr_html": """<p>Rettssaker ødelegger familier. Hvis en konflikt dras inn i rettssalen, og foreldrene kaster dritt på hverandre gjennom aggressive advokatdokumenter i 12 måneder, er det ekstremt vanskelig å samarbeide om å oppdra et barn etterpå.</p>
<p>Loven ønsker å stoppe saken lenge før den når dommerens pult. Derfor har lovgiverne skrevet § 49. Den legger et press på advokatene. En advokat kan ikke bare si: "Flott, la oss saksøke ham og ruinere ham!". Advokaten skal fungere som en brannslukker, ikke en pyroman. Advokaten skal aktivt foreslå kompromisser for dere. "Hva om du tilbyr ham en ekstra overnatting mot at du får beholde skolekretsen?"</p>
<p>Advokaten din plikter også å informere deg om det offentlige Familievernet. Dette er et gratis tilbud i kommunen, der psykologer og familieterapeuter hjelper foreldre med å snakke sammen. Familievernet er stedet der nesten alle barnefordelingssaker burde løses.</p>""",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "<p>Hvis du leier en advokat som umiddelbart vil skrive en krass stevning til retten uten engang å spørre deg om dere kan forhandle, bør du vurdere en annen advokat. En god familieadvokat ser på rettssalen som den absolutt siste og verste utveien, og vil bruke timevis på å forsøke å inngå forlik med motparten før stevningen sendes.</p>",
        "dumme_sporsmal": [
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "51", "tittel": "den lovpålagte, tvungne meklingen alle *må* igjennom før retten", "available": True},
        ],
    },
    {
        "number": "50",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Teieplikt for meklere og advokater",
        "kategori": "familie",
        "description": "Er du redd for at det du sier under mekling skal bli brukt mot deg i retten? Slapp av. Det er streng taushetsplikt for alt som foregår bak lukkede dører.",
        "kort_svar": "De som meagler i konflikter mellom foreldre (ofte på familievernkontoret), har streng taushetsplikt om det som kommer frem. Sakkyndige psykologer som bistår dommeren har også taushetsplikt, men dommeren kan oppheve den hvis det er nødvendig for at advokatene skal få se papirene i rettssaken.",
        "paragraftekst": """Den som meklar etter § 51 og § 61 første stykket nr. 2 har teieplikt om det som kjem fram om personlege forhold i samband med oppdraget. Lov 19. juni 1997 nr. 62 om familievernkontorer §§ 6, 7, 9 og 10 gjeld tilsvarande.

Den som gjer teneste etter § 61 første stykket nr. 1, 3, 4 eller 7 har teieplikt om det som kjem fram om personlege forhold i samband med oppdraget. Han kan utan hinder av teieplikta gje oppdragsgjevar dei opplysningar han har fått i samband med oppdraget. Lov 19. juni 1997 nr. 62 om familievernkontorer §§ 6, 7, 9 og 10 gjeld tilsvarande.

Den som gjer tjeneste etter § 61 første stykket nr. 5 har teieplikt om det som kjem fram om personlege forhold i samband med oppdraget. Retten kan oppheve teieplikta etter krav frå advokaten eller representanten.""",
        "hva_betyr_html": """<p>Når du sitter på Familievernkontoret sammen med eksen din for å prøve å unngå rettssak, er temperaturen ofte høy. Kanskje du gråter, kanskje du innrømmer at du har et temperamentproblem og at du sliter med depresjon etter bruddet.</p>
<p>Grunnen til at meklingsmøter noen ganger fungerer, er at det er et trygt rom ("safe space"). Paragraf 50 garanterer for dette. Mekleren har knallhard taushetsplikt. Hvis meklingen bryter sammen og dere havner i tingretten, kan ikke advokaten til eksen din kalle inn mekleren som vitne for å si "Jo, far innrømmet på kontoret mitt at han var en dårlig far." Alt som sies i rommet, blir i rommet (med unntak av opplysninger om alvorlig omsorgssvikt eller vold, der meldeplikten til barnevernet slår inn).</p>
<p>Det samme gjelder for de sakkyndige (ofte psykologer) som dommeren noen ganger henter inn (i sak etter § 61). Hvis dommeren ber en psykolog om å veilede foreldrene, har psykologen taushetsplikt overfor verden utenfor. Men psykologen <em>må</em> rapportere tilbake til dommeren (oppdragsgiveren sin) om hvordan veiledningen gikk. Slik får retten fakta på bordet.</p>""",
        "eksempler": [{"navn": "Vitnet som uteble", "tekst": "Siri og Tom er i tingretten. De har vært i mekling i tre uker tidligere på året, men ble ikke enige. Toms advokat sier til dommeren at han vil kalle inn familievernmekler Hansen som vitne, for Hansen hørte Siri skrike og oppføre seg psykopatisk under meklingsmøtet. Dommeren avviser vitneførselen umiddelbart og viser til § 50. Mekleren har taushetsplikt om det som skjedde under forhandlingene."}],
        "vanlige_feil": ["Tro at man kan skjule overgrep på grunn av taushetsplikten. (Alle som jobber med barn og familie har en lovfestet *opplysningsplikt* til barnevernet hvis de får høre om vold eller alvorlig svikt. Denne trumfer taushetsplikten).", "Gjøre opptak av meklingsmøtet i hemmelighet på telefonen for å bruke i retten. (Dette anses som et ekstremt tillitsbrudd og vil tale kraftig mot deg i en barnefordelingssak)."],
        "hva_bor_du_html": "<p>Snakk ærlig under meklingen, ellers kommer dere ingen vei. Innrøm svakheter og vis at du er villig til å kompromisse. Taushetsplikten beskytter deg mot at forsøkene dine på forlik brukes mot deg senere.</p>",
        "dumme_sporsmal": [
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "51", "tittel": "den obligatoriske meklingen dette gjelder for", "available": True},
            {"lov": "barnelova", "paragraf": "61", "tittel": "hvordan dommeren bruker sakkyndige under rettssaken", "available": True},
        ],
    },
    {
        "number": "51",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvem MÅ møte til mekling, og når?",
        "kategori": "familie",
        "description": "Du kan ikke skille deg eller gå til rettssak om barnet uten å gå innom Familievernkontoret først. Mekling er statens obligatoriske fartsdump.",
        "kort_svar": "Alle foreldre som har felles barn under 16 år, har en lovfestet, absolutt plikt til å møte opp til en times mekling (samtale på familievernkontoret) ved samlivsbrudd (skilsmisse/separasjon), før man flytter med barnet (hvis man er uenige), eller før man får lov til å saksøke den andre i domstolen om barnefordeling.",
        "paragraftekst": """Foreldre med felles barn under 16 år må møte til mekling før det vert reist sak om foreldreansvar, flytting med barnet ut av landet, kvar barnet skal bu fast eller om samvær.

Gifte foreldre med felles barn under 16 år må for å få separasjonsløyve eller skilsmisseløyve etter ekteskapslova §§ 20 og 22, ha møtt til mekling på familievernkontor eller hos annan godkjend meklar jf. ekteskapslova § 26.

Sambuarar med felles barn under 16 år skal ved samlivsbrot møte til mekling.

Foreldre som ikkje er samde om at barnet skal flytte, må møte til mekling.

Departementet kan gje forskrifter om mekling, også om unntak frå møteplikta i særlege høve.""",
        "hva_betyr_html": """<p>Når et par med felles barn under 16 år går fra hverandre, er statens største skrekk at barna skal bli ofre for en kaotisk skilsmisse. Derfor har lovgiverne bygd inn en "fartsdump". Før du får de papirene du vil ha, må dere sitte i samme rom som en terapeut i minst én time og snakke om barna.</p>
<p>Mekling er <strong>obligatorisk</strong> i tre hovedtilfeller:</p>
<p>1. <strong>Ved samlivsbrudd:</strong> Du får rett og slett ikke separasjonspapirene dine fra Statsforvalteren hvis du ikke legger ved en "meklingsattest" (se § 54). Også samboere "skal" møte (selv om samboere, i motsetning til gifte, ikke trenger papirer på bruddet sitt, må de likevel ha meklingsattest for å utløse aleneforsørger-ytelser hos NAV). 2. <strong>Før du saksøker eksen:</strong> Ønsker du å ta samværssaken eller foreldreansvaret til tingretten? Dommeren kaster saken din rett ut av vinduet hvis det ikke ligger en meklingsattest øverst i bunken. Du kan ikke kaste bort rettens tid før dere har forsøkt å snakke sammen (attesten må være mindre enn 6 måneder gammel). 3. <strong>Før flytting (ved uenighet):</strong> Som beskrevet i § 42 a: Hvis du har varslet at du flytter til nabobyen og eksen protesterer, kan du ikke endre barnets adresse før dere har meklet.</p>
<p>Hvis du har vært utsatt for vold eller overgrep, og det er umulig eller farlig for deg å sitte i samme rom som eksen, finnes det unntak (femte ledd). Mekleren kan frita dere, eller dere kan møte hver for dere.</p>""",
        "eksempler": [{"navn": "Hannes skilsmisse", "tekst": "Hanne er lei av ekteskapet og vil ha separasjon. De har en felles datter på 4 år. Hanne går inn på statsforvalteren.no for å søke om separasjon. I skjemaet står det at hun må laste opp en gyldig meklingsattest siden de har barn under 16 år. Hanne ringer ektemannen Lars og sier at de må møtes på familievernkontoret. Lars møter motvillig opp. Terapeuten snakker med dem i en time om hvordan de skal fordele datteren. Enten de ble enige eller ikke: Når den ene timen er over, skriver terapeuten ut meklingsattesten. Nå kan Hanne fullføre separasjonssøknaden sin."}],
        "vanlige_feil": ["En part nekter å møte opp på familievernkontoret for å \"sabotere\" den andres skilsmisse. (Hvis eksen ikke dukker opp til innkalt time, får du likevel meklingsattesten din. Du straffes ikke for eksens uvilje, og eksen har ingenting igjen for det).", "Tror at mekleren er en dommer som kan ta avgjørelser eller tvinge gjennom en fordeling 50/50. (Mekleren har null formell makt, de leder kun samtalen)."],
        "hva_bor_du_html": "<p>Ring familievernkontoret i kommunen din og bestill time så raskt bruddet er et faktum. Ofte er det flere ukers ventetid. Møt opp med et åpent sinn, men husk at du ikke har plikt til å signere en bindende avtale under meklingen hvis du føler deg presset eller usikker. Du kan alltid si \"jeg vil gjerne tenke på dette forslaget og få advokaten min til å se på det\" før du signerer. Så lenge du har sittet tiden ut, får du meklingsattesten.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om vi er perlevenner og 100 % enige om at barna skal bo hos meg, må vi likevel kaste bort tid på mekling for å få skilsmisse?", "a": "Ja. Loven gir ingen unntak fra 1-times regelen for vennlige brudd. Alle må innom (hvis barna er under 16 år) for at staten skal forsikre seg om at barna faktisk har det bra, og at den underliggende avtalen ikke er urettferdig for en av partene. Men for de som er enige, tar dette møtet ofte under 20 minutter."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "54", "tittel": "selve meklingsattesten du trenger for å gå videre", "available": True},
            {"lov": "barnelova", "paragraf": "56", "tittel": "når du skal reise sak for retten", "available": True},
        ],
    },
    {
        "number": "52",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hva er egentlig poenget med mekling?",
        "kategori": "familie",
        "description": "Hva snakker man om under den obligatoriske meklingen? Målet er at dere skal lage en skriftlig plan for barnet og forstå de økonomiske konsekvensene av den.",
        "kort_svar": "Hele formålet med å dra på familievernkontoret er å få hjelp til å skrive en bindende, skriftlig avtale om hvem som skal ha foreldreansvar, hvem barnet skal bo fast hos, og hvor mye samvær det skal være. Mekleren skal også sørge for at dere skjønner hva avtalen betyr for lommeboken.",
        "paragraftekst": "Føremålet med meklinga er å få foreldra til å kome fram til ei skriftleg avtale om foreldreansvaret, om kvar barnet skal bu fast og om samvær. Partane bør gjerast kjende med dei viktigaste økonomiske konsekvensane som avtala fører med seg.",
        "hva_betyr_html": """<p>Paragraf 52 er instruksen til mekleren, men den gir også foreldrene en klar forventning til hva møtet skal handle om.</p>
<p>Mekling er ikke psykoterapi eller parterapi for å lappe sammen forholdet deres. Dere skal ikke diskutere hvem som var utro, hvem som eier oppvaskmaskinen, eller hvordan dere skal dele boliglånet. Målet er krystallklart: Barnets fremtid.</p>
<p>Mekleren vil lose dere gjennom de tre store temaene: 1. Skal dere ha felles foreldreansvar (§ 30)? (Nesten alle ender på ja). 2. Hvor skal barnet bo fast (§ 36)? (Skal det være delt fast bosted, eller hos én av dere?). 3. Hvor ofte skal dere ha samvær (§ 43)?</p>
<p>Målet er at dere etter møtet sitter igjen med en <em>skriftlig samværsavtale</em>. Dette er et viktig papir i hverdagen deres.</p>
<p>I den andre setningen gir loven mekleren en viktig oppgave: Penger. Svært mange foreldre velger for eksempel "50/50 delt bosted" fordi de tror det er rettferdig, uten å vite at det kan stoppe retten til overgangsstønad fra NAV, påvirke barnebidrag, og utløse doble regninger for fritidsutstyr. Mekleren skal forklare dere grovt sett hva de økonomiske konsekvensene er før dere signerer papiret, slik at ingen blir lurt.</p>""",
        "eksempler": [{"navn": "Papiret som ordnet alt", "tekst": "Hanne og Tom går til mekling. De krangler mye. Mekleren stopper dem og sier: \"Fokus på barna. Kan vi bli enige om at datteren bor hos Hanne, siden skolen hennes er i den gata?\". De blir enige. Mekleren fyller ut et ferdig skjema for samværsavtale, hvor Tom får annenhver helg. Mekleren opplyser om at siden Emma bor hos Hanne, må Tom betale barnebidrag, men at samværet hans gir ham fradrag i bidraget. De signerer begge avtalen der og da, og forlater kontoret med papiret i hånden, klare for den nye hverdagen."}],
        "vanlige_feil": ["Blande inn økonomisk oppgjør (som hvem som skal betale barnehageregningen eller kredittkortgjelden) i samtalen (mekleren har verken lov til eller kunnskap om å hjelpe dere med det).", "Møte uforberedt og signere på noe man ikke forstår."],
        "hva_bor_du_html": "<p>Før du drar til meklingsmøtet: Sett deg ned hjemme og lag et skisse-forslag til en turnuskalender (ukedager, helger, ferier). Hvis du har noe konkret å vise frem på møtet, sparer dere mye tid og unngår emosjonelle omveier. Bruk gjerne Bufdir (Barne-, ungdoms- og familiedirektoratet) sine maler for samværsavtale, som ligger gratis på nett, så vet du hva mekleren forventer å fylle ut.</p>",
        "dumme_sporsmal": [
            {"q": "MÅ vi inngå en skriftlig avtale under dette møtet?", "a": "Nei. Du kan si nei til alt og nekte å signere noe som helst. Men siden bruddet er et faktum, vil en manglende avtale bare skape totalt kaos uken etter, når barnet ikke vet hvor det skal bo. Nekter du konsekvent, ender dere sannsynligvis i domstolen til slutt. Men du skal aldri signere på noe som du oppriktig mener er farlig for barnet."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "30", "tittel": "foreldreansvar (hva dere avtaler)", "available": True},
            {"lov": "barnelova", "paragraf": "36", "tittel": "hvem barnet skal bo hos (hva dere avtaler)", "available": True},
            {"lov": "barnelova", "paragraf": "51", "tittel": "selve plikten til å møte opp", "available": True},
        ],
    },
    {
        "number": "53",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Du må møte opp personlig til meklingen",
        "kategori": "familie",
        "description": "Gruer du deg til å sitte i samme rom som eksen? Loven krever personlig oppmøte. Men mekleren kan skille dere i to rom hvis det er uforsvarlig å møtes.",
        "kort_svar": "Loven krever at både mor og far møter opp personlig og samtidig til meklingsmøtet. Du kan vanligvis ikke sende en advokat i ditt sted. Hvis det er tungtveiende grunner for det (som frykt, overgrep, vold), kan mekleren bestemme at dere møter hver for dere. I spesielle tilfeller kan du ha med en advokat inn.",
        "paragraftekst": "Foreldra skal møte personleg og samstundes til mekling. Den som meklar kan likevel avgjere at dei skal møte kvar for seg dersom det er tenleg. Meklaren kan i særlege høve gje løyve til at ein eller begge partar møter saman med ein fullmektig.",
        "hva_betyr_html": """<p>Paragrafen stenger et smutthull for unnasluntrere. Hvis du prøver å unngå ubehaget ved skilsmissen ved å nekte å delta på meklingen, eller bare vil sende advokaten din, sier loven nei. "Foreldra skal møte personleg og samstundes". Konflikten gjelder deres felles barn, og staten mener dere voksne må sitte ansikt til ansikt (med en terapeut i rommet) for å rydde opp i det.</p>
<p>Men staten tvinger ikke voldsutsatte til å sitte på utstilling for overgriperen sin.</p>
<p>Det andre punktumet er svært viktig: "Meklaren kan [...] avgjere at dei skal møte kvar for seg". Ring familievernkontoret i forkant og si: "Han har slått meg" eller "Hun har besøksforbud mot meg". Da vil familievernkontoret booke dere inn til forskjellige tider, på forskjellige dager. Du får meklingsattesten din uten å måtte se ansiktet til eksen.</p>
<p>I noen sjeldne, "særlege høve" – ofte hvis partene er ekstremt ujevne i styrkeforhold og ressurssterke (kanskje en part har lærevansker eller er språklig svak) – kan terapeuten tillate at du tar med deg advokaten din ("fullmektig") inn i rommet som en krykke. Men dette skjer sjelden.</p>""",
        "eksempler": [{"navn": "Skremt, men må møte", "tekst": "Hanne har tatt med barna og flyttet til et krisesenter på grunn av psykisk vold fra Lars. For å saksøke Lars og få foreldreansvaret alene, trenger Hanne en meklingsattest. Hun får innkalling og ser at Lars er kalt inn til samme time (samstundes). Hun får panikk og ringer Familievernkontoret. Terapeuten viser til § 53, og deler umiddelbart timen i to. Hanne møter kl. 10 på tirsdag, og Lars møter kl. 10 på torsdag. Begge har da \"møtt personlig\" (kvar for seg), og Hanne får attesten hun trenger."}],
        "vanlige_feil": ["Droppe timen fordi man tror eksen uansett blir hysterisk, og at det ikke har noe poeng (møter du ikke, bryter *du* loven, og eksen kan innkassere poengene).", "Møte opp med onkel Kjell eller ny kjæreste som \"støttespiller\" uten å ha avtalt dette med mekler i forkant. (Kun fullmektig/advokat kan tillates i særskilte tilfeller, terapeuter vil ofte kaste den nye kjæresten på gangen fordi det eskalerer konflikten ekstremt)."],
        "hva_bor_du_html": "<p>Bruk den timen for det den er verdt. Har du kommunikasjonsproblemer med eksen, så husk at terapeuten er trent i å dempe gemyttene. Føler du deg utrygg før timen, gi beskjed tidlig. Familievernkontorene i Norge tar slike advarsler på dypeste alvor.</p>",
        "dumme_sporsmal": [
            {"q": "Får eksen attesten sin hvis jeg møter opp, men bare sitter der og ser i bordet en hel time?", "a": "Ja. Loven sier at dere \"skal møte\", ikke at dere skal \"lykkes i å bli enige\". Har dere pustet luften i rommet i 60 minutter, er plikten utført, og mekleren vil skrive ut attesten til dere begge, slik at dere kan søke separasjon eller gå til domstolen."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "54", "tittel": "hva du får utdelt når timen er over (meklingsattesten)", "available": True},
        ],
    },
    {
        "number": "53a",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Mekleren skal ha ren vandel (politiattest)",
        "kategori": "familie",
        "description": "For å beskytte barn må de som fungerer som godkjente meklere i barnefordelingssaker bevise at de ikke har rulleblad for overgrep eller vold.",
        "kort_svar": "Alle som skal jobbe som godkjente meklere (som regel ansatte på Familievernkontoret eller godkjente advokater) må fremvise en barneomsorgsattest (politiattest) uten anmerkninger. Dette er for å sikre at de som håndterer familiers krise ikke selv er straffedømt for forhold mot barn.",
        "paragraftekst": """Den som skal godkjennast som meklar, skal leggje fram politiattest som nemnd i politiregisterloven § 39.

Departementet kan i forskrift gje nærare reglar om kravet om politiattest.""",
        "hva_betyr_html": """<p>Paragrafen er en kontrollmekanisme rettet mot statens egne ansatte og systemer. Familievernet er et sted med dype hemmeligheter og svært sårbare familier. Loven slår fast at før noen i det hele tatt kan få status som "godkjent meklar" (slik at de har lov til å skrive ut de livsviktige meklingsattestene foreldrene trenger for å gå i retten eller skilles), må staten sjekke vandel.</p>
<p>Politiregisterloven § 39 er paragrafen for barneomsorgsattest. Den avslører om personen tidligere er dømt for sedelighetsforbrytelser (overgrep mot barn), grov vold eller narkotikakriminalitet. Hvis en person har noe slikt på rullebladet sitt, får de ikke lov til å mekle i barnefordelingssaker.</p>
<p>Som forelder merker du ingenting til dette i praksis. Det er en byråkratisk forsikring for at du møter trygge fagfolk.</p>""",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "",
        "dumme_sporsmal": [
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "51", "tittel": "selve meklingsordningen", "available": True},
        ],
    },
    {
        "number": "54",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Meklingsattesten er gullbilletten din",
        "kategori": "familie",
        "description": "Målet med mekling er å få en meklingsattest. Uten dette papiret kommer du ingen vei verken hos statsforvalteren (for separasjon) eller i domstolen.",
        "kort_svar": "Når du har fullført én time med obligatorisk mekling, skriver terapeuten ut en meklingsattest. Denne attesten er et offisielt dokument som beviser at dere har forsøkt å løse konflikten. Blir dere ikke enige etter én time, oppfordres dere til å fortsette inntil syv timer totalt, men det er frivillig. Attesten er gyldig i 6 måneder.",
        "paragraftekst": """Det skal skrivast ut meklingsattest når partane har møtt til ein times mekling hos ein meklar. Dersom foreldra ikkje er samde, skal dei verte oppfordra til å mekle i inntil tre timar. Dei kan få tilbod om mekling i ytterlegare tre timar dersom meklaren finn at dette kan føre til at partane kan kome fram til ein avtale.

Meklingsattesten er gyldig i seks månader.""",
        "hva_betyr_html": """<p>Paragrafen beskriver den nøyaktige tidslinjen for det obligatoriske meklingssystemet i Norge.</p>
<p>Kravet staten stiller (for å gi deg lov til å skilles eller saksøke eksen for barnefordeling), er <strong>nøyaktig én time (60 minutter)</strong> i samme rom som terapeuten. Når klokken slår 60 minutter, plikter mekleren å skrive ut "Meklingsattesten" og gi den til deg. Du har da oppfylt lovens minimumskrav.</p>
<p>Men hva hvis dere ikke ble enige om samværsavtalen på den korte timen? Da sier loven at mekleren skal <em>oppfordre</em> dere til å ta tre nye timer. Disse påfølgende timene er frivillige. Mange foreldre velger å si ja til dette, fordi det er gratis terapi og gir rom for å finne en løsning uten å betale advokater 3000 kroner timen. Hvis mekleren ser at dere gjør fremskritt, kan staten tilby ytterligere tre timer på toppen (totalt 7 timer).</p>
<p>Når du har fått meklingsattesten i hånden, tikker klokken. <strong>Attesten er bare gyldig i 6 måneder.</strong> Hvis du legger den i skuffen, og først ett år senere bestemmer deg for å saksøke eksen for å få flyttet barnet over til deg, vil domstolen kaste stevningen din (avvise saken). Attesten har utløpt. Du må da ringe familievernkontoret og starte prosessen helt på nytt med en ny times mekling.</p>""",
        "eksempler": [{"navn": "Stevningen som ble avvist", "tekst": "Lars og Kari kranglet stygt under bruddet i januar, og de gjennomførte den obligatoriske meklingen 15. februar. Lars fikk meklingsattesten, men de bestemte seg for å prøve å ordne opp privat og avventet rettssak. I november eskalerer konflikten og Kari nekter Lars å se barna. Lars drar til advokaten sin og de sender en stevning til tingretten. Dommeren mottar papirene, ser at meklingsattesten er fra februar (9 måneder gammel), og avviser hele saken umiddelbart. Lars tapte både tid og advokatutgifter, og må begynne på nytt med innkalling til ny mekling."}],
        "vanlige_feil": ["Sende søknad om separasjon eller stevning til tingretten uten å legge ved meklingsattesten som vedlegg. (Staten behandler ingenting før beviset ligger i bunken).", "Glemme gyldighetsfristen på 6 måneder.", "Tro at man MÅ gå syv timer til mekling, og fortsette å møte opp uke etter uke selv om eksen er fullstendig urimelig og man vet at forlik er umulig. (Du kan lovlig avslutte prosessen etter én time)."],
        "hva_bor_du_html": """<p>Når du får meklingsattesten, ta et bilde av den på telefonen, lagre den som PDF, og legg originalen i en trygg mappe. Dette er "gullbilletten" din til rettssystemet det neste halvåret.</p>
<p>Føler du at eksen aldri vil gi seg, og en rettssak er unngåelig? Da er det ingen skam å takke pent nei til tilbudet om timer 2 og 3, og ta saken rett til advokaten din i det timen er over.</p>""",
        "dumme_sporsmal": [
            {"q": "Får eksen min attesten sin hvis det var JEG som avbrøt meklingen og stormet ut etter 60 minutter?", "a": "Ja. Loven sier \"når partane har møtt til ein times mekling\". Så lenge dere begge har fullført de påkrevde 60 minuttene, får begge parter attesten sin og har dermed \"lov\" til å gå videre til domstolen, uansett hvem som valgte å ikke delta i de frivillige rundene etterpå."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "51", "tittel": "selve kravet om å møte opp", "available": True},
            {"lov": "barnelova", "paragraf": "56", "tittel": "når du bruker attesten for å dra saken til tingretten", "available": True},
        ],
    },
    {
        "number": "55",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Kan fylkesnemnda/statsforvalter bestemme over avtalen deres?",
        "kategori": "familie",
        "description": "Har dere skrevet en samværsavtale som eksen aldri følger? Da kan Statsforvalteren gi avtalen tvangskraft, slik at du kan bruke namsmannen for å hente barnet.",
        "kort_svar": "Hvis foreldrene er helt enige, kan de be Statsforvalteren (fylkesmannen) om å gi en skriftlig avtale om barnets bolig og samvær \"tvangskraft\". Det betyr at avtalen blir like kraftig som en dom fra retten. Bryter noen avtalen etter dette, kan du bruke tvangsbøter for å sikre samværet. Dette krever at dere har en meklingsattest fra før.",
        "paragraftekst": """Når begge foreldra ber om det, kan statsforvaltaren fastsetje at ei skriftleg avtale om foreldreansvar, bustad og samvær skal kunne tvangsfullførast etter reglane i § 65. Vilkåret er at avtala først og fremst rettar seg etter det som er best for barnet. Trengst det, bør sakkunnige, barnevernstenesta eller sosialtenesta uttale seg før statsforvaltaren avgjer spørsmålet.

Eit vilkår for å bringe ei sak inn for statsforvaltaren etter første stykket er at foreldra kan leggje fram gyldig meklingsattest.

Saka må bringast inn for den statsforvaltaren der barnet har alminneleg verneting på den tida saka vert reist.""",
        "hva_betyr_html": """<p>Mange inngår en hjemmesnekret samværsavtale på kjøkkenbordet. Hva skjer hvis mor etter to måneder slutter å levere barnet på fredager? Svaret er ingenting. Politiet vil le av deg hvis du viser dem en hjemmelaget lapp. For å bruke politiet eller tvangsbøter for å få se barnet ditt (etter § 65), trenger du en formell dom fra en domstol. En rettssak er dyr.</p>
<p>Paragraf 55 gir dere en gratis bakdør for å skape fred og ro.</p>
<p>Hvis <strong>begge foreldrene ber om det sammen</strong>, kan dere sende den skriftlige samværsavtalen deres til Statsforvalteren i barnets fylke. Statsforvalteren leser gjennom den. Er avtalen god (dvs. til "barnets beste", og ikke skadelig for barnet), setter Statsforvalteren et formelt stempel på avtalen. Den får da <em>tvangskraft</em>.</p>
<p>Får avtalen tvangskraft, er den sidestilt med en rettsdom. Slutter eksen å levere barnet, kan du da sende papiret rett til namsmannen/tingretten og kreve "tvangsfullbyrdelse" (for eksempel bøter per dag samværet nektes).</p>
<p>For å bruke denne gratistjenesten hos Statsforvalteren, er det to absolutte krav: 1. Dere må legge ved en gyldig meklingsattest (fra familievernkontoret). 2. Dere må begge være 100 % enige (hvis dere er uenige, hjelper ikke Statsforvalteren dere, da må dere til tingretten for en rettssak).</p>""",
        "eksempler": [{"navn": "Sikring for fremtiden", "tekst": "Tom og Siri ble enige om at 50/50 er best for sønnen. De skriver en flott avtale hos mekler og får meklingsattest. Men Tom, som husker at Siri brøt avtalen deres da de hadde hund, stoler ikke på henne i lengden. Han foreslår: \"La oss sende avtalen til Statsforvalteren etter barnelova § 55, så vi vet at den er spikret fast for begge to\". Siri er med. De sender den inn, Statsforvalteren stempler den. Ett år senere nekter Siri å la sønnen bo hos Tom på hennes \"uker\". Tom slipper å gå til rettssak for å saksøke henne. Han bruker den stemplede avtalen for å kreve tvangsbøter hos tingretten umiddelbart, og Siri gir seg fordi det blir for dyrt."}],
        "vanlige_feil": ["En fortvilet pappa sender inn avtalen til Statsforvalteren alene og ber dem fikse den, fordi mor saboterer. (Saken blir avvist. Statsforvalteren kan KUN gi tvangskraft hvis *begge foreldre* (i fellesskap) sender den inn og ber om det).", "Glemme meklingsattesten, slik at Statsforvalteren avviser saken."],
        "hva_bor_du_html": "<p>Dette er en sjelden brukt paragraf i Norge, fordi det krever full enighet fra foreldre som åpenbart tviler på at den andre vil holde avtalen. Men, hvis du har en eks som ofte \"glemmer\" seg bort, og dere i et lyst øyeblikk akkurat har blitt enige hos familievernkontoret, kan du foreslå at dere stempler avtalen hos Statsforvalteren for sikkerhets skyld. Da sparer du deg for advokatregningen i fremtiden hvis eksen snur.</p>",
        "dumme_sporsmal": [
            {"q": "Kan vi be politiet hente barnet når avtalen har fått dette stempelet?", "a": "Grovt sett: Nei, ikke i Norge (med noen få akutte unntak). Selv om avtalen får tvangskraft, bruker vi ikke politiet til å dra barn ut av morens armer. Tvangskraft i samværssaker i Norge handler nesten utelukkende om *tvangsmulkt* (pengebøter), der namsmannen trekker eksen for penger (f.eks. 1500 kr pr dag) inntil hun leverer barnet (se § 65)."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "65", "tittel": "reglene for tvangsfullføring og tvangsbøter", "available": True},
            {"lov": "barnelova", "paragraf": "54", "tittel": "meklingsattesten du trenger som vedlegg", "available": True},
        ],
    },
    {
        "number": "56",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Når du velger å saksøke eksen for foreldreansvar eller samvær",
        "kategori": "familie",
        "description": "Når all prating feiler, og eksen nekter deg tid med barnet, er domstolen eneste utvei. Slik reiser du sak, men husk at meklingsattesten må ligge i stevningen.",
        "kort_svar": "Er dere uenige om hvem som skal ha foreldreansvar, hvor barnet skal bo fast, eller hvor mye samvær det skal være, kan du reise en sak for retten (tingretten). Det absolutte vilkåret for å få starte rettssaken er at du legger ved en gyldig meklingsattest fra familievernkontoret.",
        "paragraftekst": """Er foreldra usamde om kven som skal ha foreldreansvar, kven barnet skal bu fast saman med, eller samvær, kan kvar av dei reise sak for retten. Ein forelder kan også reise sak om foreldreansvar når det er uråd å kome fram til ei avtale fordi den andre forelderen ikkje bur i landet og ikkje lar seg oppspore. Sak om flytting med barnet ut av landet kan reisast av forelder med foreldreansvar eller av forelder som samstundes reiser sak om foreldreansvar.

Eit vilkår for å reise sak etter første stykket er at foreldra kan leggje fram gyldig meklingsattest. Dette gjeld ikkje der ein forelder er dømd for alvorleg vald eller overgrep mot eigne barn etter straffeloven eller i slike høve er overført til tvungent psykisk helsevern eller idømt tvungen omsorg. Departementet kan ved forskrift gje utfyllande reglar om hvilke høve som er omfatta av unntaket i andre punktum.""",
        "hva_betyr_html": """<p>Paragraf 56 er porten inn til det mest dramatiske i norsk familierett: En barnefordelingssak.</p>
<p>Når dere har prøvd mekling og pratet dere varme, men far fremdeles krever at barnet bor hos ham 50/50, og mor krever at han bare skal få helgesamvær, stanser systemet opp. Da gir denne loven en av foreldrene (vanligvis den som er misfornøyd med situasjonen slik den er i dag) rett til å sende en "stevning" (et søksmål) til tingretten.</p>
<p>Du kan saksøke eksen for tre ting: 1. <strong>Foreldreansvar:</strong> Kreve å få det alene, eller kreve å få felles ansvar. 2. <strong>Fast bosted (daglig omsorg):</strong> Kreve at barnet skal bo mesteparten av tiden hos deg, eller kreve 50/50. 3. <strong>Samvær:</strong> Kreve mer tid med barnet (eller at eksen skal få mindre tid).</p>
<p>En smart detalj i første ledd gjelder uansvarlige foreldre i utlandet: Hvis du har felles foreldreansvar med en mann som reiste tilbake til hjemlandet sitt for tre år siden og sluttet å ta telefonen, vil du slite med å fornye barnets pass (siden pass krever begges signatur). Paragraf 56 gir deg da rett til å reise en formell sak for retten for å ta foreldreansvaret fra ham på grunn av "forsvinning", slik at du kan drive hverdagen alene i Norge.</p>
<p><strong>Vilkåret for å saksøke:</strong> Dommeren nekter å ta i saken hvis du ikke har en fersk, gyldig <strong>meklingsattest</strong> (som omtalt i § 51 og § 54). Har du ikke attesten, vil dommeren avvise søksmålet.</p>
<p><strong>Unntaket fra mekling:</strong> Det andre leddet har et kritisk unntak, laget for ofre for alvorlig kriminalitet. Hvis eksen din er formelt <em>dømt</em> (ikke bare siktet) for alvorlig vold eller seksuelle overgrep mot sine egne barn, slipper du å møte ham til mekling på familievernkontoret. Da kan du gå rett til advokaten og saksøke ham direkte i tingretten for å fjerne foreldreansvaret og samværet.</p>""",
        "eksempler": [{"navn": "Stevningen for å flytte", "tekst": "Kari vil flytte til Tromsø med datteren Emma (8). Tom nekter å la Kari ta med datteren vekk fra Oslo. De møtes hos Familievernkontoret, får en times mekling, men forblir bitre fiender. Tom innser at siden Kari er registrert som bostedsforelder, har hun lov til å flytte (etter § 37). Tom kontakter advokaten sin. De skriver en stevning der Tom reiser sak etter § 56, og krever at fast bosted flyttes over til ham, og at Emma nektes å flytte fra Oslo. De legger ved meklingsattesten Kari og Tom akkurat fikk. Tingretten godkjenner saken og starter prosessen."}],
        "vanlige_feil": ["En fortvilet mor prøver å stevne far for barnebidrag med denne paragrafen. (Bidrag går ikke gjennom domstolen, det er det utelukkende NAV som beregner).", "Droppe å sende inn meklingsattesten og tenke at \"advokaten fikser det\".", "Tror at du slipper mekling fordi eksen \"klyp\" barnet. (Unntaket krever en rettskraftig *straffedom* for *alvorlig* vold, hvis han bare er under etterforskning, gjelder ikke unntaket, og du må mekle)."],
        "hva_bor_du_html": "<p>Å reise sak etter § 56 er et enormt skritt. Det koster ofte over 150 000 kroner i advokatutgifter (med mindre du har fri rettshjelp), tar ett til to år, og barna lider ofte sterkt under konflikten. Du bør kun sende en stevning når eksens adferd direkte skader barnet, eller når eksen saboterer helt vesentlige deler av barnets samvær uten grunn.</p>",
        "dumme_sporsmal": [
            {"q": "Kan en bestemor saksøke foreldrene etter denne paragrafen?", "a": "Nei. Paragraf 56 sier eksplisitt \"kvar av *dei*\" (foreldrene). Besteforeldre har ingen søksmålskompetanse under vanlige brudd, de må bruke særreglene sine i § 45 (hvis en forelder er død) eller i verste fall i en barnevernssak."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "51", "tittel": "hvem som er pliktig til å gjennomføre meklingen", "available": True},
            {"lov": "barnelova", "paragraf": "57", "tittel": "hvilken by (domstol) du skal sende stevningen til", "available": True},
            {"lov": "barnelova", "paragraf": "60", "tittel": "hvordan du kan få en midlertidig hastedom mens rettssaken står på", "available": True},
        ],
    },
    {
        "number": "57",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvilken by skal rettssaken om barnet gå i?",
        "kategori": "familie",
        "description": "Vil du saksøke eksen for barnefordeling, men dere bor i hver deres ende av landet? Loven krever at du sender stevningen til tingretten der barnet bor.",
        "kort_svar": "En rettssak om foreldreansvar, fast bosted eller samvær skal reises i den tingretten som hører til stedet der barnet er folkeregistrert. Lever barnet i skjul (på strengt fortrolig adresse) for å unnslippe vold, skal saken alltid føres sentralt i Oslo tingrett for å beskytte barnets gjemmested.",
        "paragraftekst": "Sak etter § 56 må reisast for den domstolen der barnet har alminneleg verneting på den tida saka vert reist. Dersom saka gjeld søsken med ulikt alminneleg verneting, kan felles sak for barna reisast der eitt av barna har alminneleg verneting. Dersom barnet bur på sperra adresse, jf. lov 9. desember 2016 nr. 88 om folkeregistrering med forskrifter, eller det er søkt om eller gjeve løyve til å nytte fiktive personopplysningar for barnet, jf. lov 4. august 1995 nr. 53 om politiet § 14 a, kan saka reisast for Oslo tingrett.",
        "hva_betyr_html": """<p>Paragrafen handler om det domstolene kaller "verneting" (hvor saken hører hjemme). Hovedregelen er enkel: Barna er sentrum i saken, derfor skjer rettssaken i deres lokalsamfunn.</p>
<p>Bor barnet hos mor i Tromsø, og far (som bor i Kristiansand) vil saksøke henne for å få mer samvær, må far sin advokat sende papirene til Nord-Troms og Senja tingrett (i Tromsø). Far må altså sette seg på flyet og reise opp dit hver gang det er rettsmøte. Dette gjør staten bevisst for at dommeren lett skal kunne oppnevne lokale barnespsykologer (sakkyndige) og hente inn erklæringer fra barnets lokale barnehage/skole uten reisekostnader.</p>
<p>Har paret to felles barn, og de utrolig nok har klart å splitte dem før rettssaken (en tenåring hos far, en lillebror hos mor), sier loven at advokatene kan samle hele røkla og la saken gå i én av byene. Retten tillater "felles sak".</p>
<p><strong>Voldsvernet - Sperret adresse</strong> Det viktigste i loven er det tredje punktumet. Kvinner og barn på flukt fra voldelige fedre bor på hemmelig, sperret adresse (Kode 6 eller Kode 7). Skulle en voldelig far (i for eksempel Bergen) få lov å stevne mor, og varselet fra domstolen plutselig kom fra "Salten tingrett", ville faren umiddelbart skjønt at "Aha, de gjemmer seg i Nord-Norge!".</p>
<p>For å skjule sporet fullstendig, har barneloven bestemt at alle barnefordelingssaker som involverer et barn på strengt fortrolig adresse, uansett hvor i landet de faktisk bor, sluses rett inn i Oslo tingrett. Slik beskyttes adressen.</p>""",
        "eksempler": [{"navn": "Trond reiser sak", "tekst": "Trond i Kristiansand krever delt fast bosted for sønnen sin. Sønnen har vært folkeregistrert i Stavanger (der mor bor) det siste året. Trond ber advokaten sin kjøre saken i Kristiansand, fordi han kjenner en god dommer der, og det er billigere for ham. Advokaten rister på hodet og viser til § 57. Stevningen må sendes til Sør-Rogaland tingrett. Trond må belage seg på å reise til Stavanger for rettsmøtene."}],
        "vanlige_feil": ["Mor flytter til Trondheim 1. juni, og far sender stevning 5. juni til Oslo fordi \"barnet bodde der i forrige uke\". (Det er adressen \"på den tida saka vert reist\" som gjelder. Endrer Folkeregisteret adressen før stevningen sendes, må du følge etter til den nye byen).", "Prøve å tvinge Oslo tingrett til å ta en helt vanlig sak for to foreldre som bor i Drøbak, bare fordi advokaten holder til i Oslo. (Avvises)."],
        "hva_bor_du_html": "<p>Før du saksøker: Gå inn på Domstol.no og slå opp postnummeret der barnet ditt er folkeregistrert. Da ser du nøyaktig hvilken domstol du må sende saken til.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om mor snik-flytter og endrer adressen tre dager *etter* at domstolen i Oslo har mottatt stevningen min?", "a": "Da gjelder en regel i tvisteloven (\"perpetuatio fori\") som sier at domstolen låses til det stedet saken startet. Oslo tingrett vil da beholde saken helt til dommen faller, uansett hvor mor flytter underveis, for å forhindre \"forum-shopping\" og trenering fra bostedsforelderen."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "56", "tittel": "retten din til i det hele tatt å reise stevning", "available": True},
            {"lov": "barnelova", "paragraf": "15", "tittel": "samme vernetingsregel gjelder for rene farskapssaker", "available": True},
        ],
    },
    {
        "number": "58",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Slik skal papirene til tingretten se ut (stevning og tilsvar)",
        "kategori": "familie",
        "description": "Hva må stå i stevningen når du saksøker eksen for barnefordeling? Og hva må eksen svare? Loven krever kort og presis skriving.",
        "kort_svar": "Når du går til retten i en barnefordelingssak, sender du en \"stevning\". Den må inneholde en kort forklaring på hva dere er uenige om og hva du krever, pluss meklingsattesten. Retten sender denne til den andre forelderen, som må skrive et \"tilsvar\" som svarer kort på kravene og presenterer sitt eget krav.",
        "paragraftekst": """Stemnemålet skal innehalde namn og adresse til foreldra og barna, og skal vise om usemja gjeld foreldreansvaret, flytting med barnet ut av landet, kvar barnet skal bu fast eller samværet, og gje ei kort utgreiing om grunnlaget for usemja og saksøkjarens påstand. Meklingsattest skal leggjast ved. Stemnemålet kan setjast fram på godkjent skjema.

Retten skal forkynne stemnemålet for saksøkte. Tilsvaret skal gjere greie for kva for tvistepunkt det er usemje om, og gje ei kort utgreiing om korleis saksøkte ser på saka. I tillegg må tilsvaret innehalde den saksøktes påstand. Tilsvaret kan setjast fram på godkjent skjema.

Retten kan be om nærare utgreiing av saka frå partane dersom det trengst for å få saka godt nok opplyst.""",
        "hva_betyr_html": """<p>Paragrafen er "bruksanvisningen" for startskuddet i en barnefordelingsrettssak.</p>
<p>Lovgiverne er drita lei av bitre advokater som skriver seksti siders lange stevninger der de drar frem at far ikke vasket opp i 2018 og at mor har stygge sko. Derfor understreker denne paragrafen ordet "kort".</p>
<p><strong>Stevningen (fra saksøker):</strong> Den som vil i retten (saksøker), skriver et stevningsdokument. Du må fortelle hvem dere er (med adresse for mor, far og barn), hva dommeren skal avgjøre (er det krangel om samvær, fast bosted eller pass?), og din "påstand" (ditt krav, f.eks.: "Jeg krever at barnet bor fast hos meg"). Og selvsagt: Du må legge ved meklingsattesten. Legger du ikke ved den, avvises stevningen.</p>
<p><strong>Tilsvaret (fra saksøkte):</strong> Når domstolen har lest gjennom stevningen og ser at alt er i orden, sender de papirene i posten/digitalt til den andre forelderen (den saksøkte). Domstolen gir eksen din en streng frist (vanligvis 2-3 uker) til å skrive et "tilsvar". Dette er eksens sjanse til å si: "Jeg er dypt uenig, her er kort min versjon, og mitt krav er at barnet fortsetter å bo hos meg 50/50".</p>
<p>Dommeren avslutter paragrafen med å gi seg selv makten til å be om mer informasjon (tredje ledd). Hvis advokatene har skrevet for lite, kan dommeren be dem utdype hva barnets fastlege egentlig mente i den journalen de la ved.</p>""",
        "eksempler": [{"navn": "Farens korte stevning", "tekst": "Jonas (far) engasjerer advokat for å få mer samvær. Advokaten fyller ut et standardskjema (som godkjent av domstolen). Han skriver \"Krav: Utvidet samvær etter loven\". I begrunnelsen skriver advokaten kun tre avsnitt: \"Foreldrene har vært på mekling uten hell. Far mener det nåværende samværet (annenhver helg) er for lite for at den sterke tilknytningen til sønnen skal vedvare. Mor motsetter seg økning fordi hun hevder avstanden til skolen er for lang. Saksøker mener avstanden på 20 min kjøring er uproblematisk. Meklingsattest er vedlagt.\" Det er alt dommeren trenger. Stevningen sendes, mor får 3 ukers frist til tilsvar, og saken ruller."}],
        "vanlige_feil": ["Blande inn irrelevant skittkasting i stevningen for å \"sverte\" eksen. (Dommeren gjennomskuer det umiddelbart og blir bare irritert over at regelen om \"kort utgreiing\" brytes).", "Å ikke formulere en krystallklar \"påstand\" i bunnen av papiret.", "Saksøkte tenker \"dette er bare tull\" og kaster stevningen i søpla uten å skrive tilsvar. (Ignorerer du fristen for tilsvar, vinner den andre parten ofte automatisk)."],
        "hva_bor_du_html": "<p>Bruk advokat. Til tross for at loven sier du <em>kan</em> bruke et ferdig godkjent skjema og gjøre det selv, er domstols-systemet for komplekst for de fleste privatpersoner. Gjør du en teknisk feil i stevningen, kan du tape saken din. Får du et slikt dokument i postkassen (\"Stevning\"), ring advokatvakten eller en familierettsadvokat samme dag. Fristen er knallhard.</p>",
        "dumme_sporsmal": [
            {"q": "Får jeg lov å legge ved barnevernets dokumenter i stevningen?", "a": "Ja, du kan (og bør) legge ved relevante bevis, som legeerklæringer, SMS-er som viser trusler, eller barnevernets konklusjoner. Men husk at selve saksfremstillingen (teksten du skriver) skal være kort."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "59", "tittel": "hva dommeren gjør med papirene etter at de er sendt inn", "available": True},
            {"lov": "barnelova", "paragraf": "56", "tittel": "vilkårene for å i det hele tatt få sende stevningen (meklingsattesten)", "available": True},
        ],
    },
    {
        "number": "59",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Dommeren skal skynde seg og forsøke å forlike dere",
        "kategori": "familie",
        "description": "Barnefordelingssaker i retten fungerer ikke som straffesaker på film. Her er dommerens hovedoppgave å få dere to til å snakke sammen og inngå et forlik.",
        "kort_svar": "En dommer som får en barnefordelingssak (barnelovsak) på pulten sin, har to strenge ordrer fra loven: Behandle saken raskt (prioritert i køen), og bruk hver eneste anledning til å prøve å få foreldrene til å inngå en frivillig avtale (forlik) i stedet for å avsi en brutal dom.",
        "paragraftekst": """Dommaren skal påskunde saka så mykje som mogeleg.

Dommaren skal på kvart trinn i saka vurdere om det er mogeleg å oppnå forlik mellom partane, og leggje tilhøva til rette for det.

Domstolloven og tvisteloven gjeld for retten si handsaming av saker etter kapitlet her, så langt ikkje anna følgjer av reglane her.""",
        "hva_betyr_html": """<p>Paragraf 59 styrer tempoet og stemningen inne i domstolen.</p>
<p>I vanlige tvister, som en nabokrangel om trær, kan domstolene la saken ligge i skuffen i et halvt år. Men loven er livredd for at barn skal lide ("leve i limbo") mens foreldrene kriger. Derfor sier første ledd at dommeren "skal påskunde saka". Det betyr at barnefordelingssaker skal snike i køen og få dato for rettsmøter så raskt som domstolen overhodet makter. Målet er å skape ro for barnet snarest mulig.</p>
<p>Andre ledd snur rollen til dommeren på hodet. Normalt sitter en dommer taus, hører på bevis, trekker seg tilbake og slår klubba i bordet. I barnelovsaker har dommeren plikt til å forsøke å bli overflødiggjøre seg selv. Dommeren fungerer mer som en mektig familieterapeut (ofte med hjelp fra en sakkyndig psykolog).</p>
<p>Under hvert eneste saksforberedende møte (se § 61) vil dommeren spørre: "Er dere sikre på at vi må slåss? Hva om far henter på torsdag i stedet, vil du godta det, mor?". Dette gjøres fordi et rettsforlik (en avtale skrevet i retten) nesten alltid gir lavere konfliktnivå i etterkant enn en hard dom der den ene får stempelet som "taper".</p>""",
        "eksempler": [{"navn": "Dommerens press", "tekst": "Pål krever datteren 100 %, mens Anne krever henne 50/50. I det første møtet i tingretten ser dommeren at begge er skikkelige folk, og at konflikten mest bunner i sjalusi etter bruddet. Istedenfor å bestille hovedforhandling (stor rettssak med vitner), sier dommeren (med hjemmel i § 59): \"Jeg beordrer en sakkyndig psykolog til å snakke med dere i to måneder. Deretter møtes vi her igjen for å se om vi kan inngå et forlik.\" De setter seg sammen med psykologen, isfronten tiner, og i neste rettsmøte signerer de frivillig en avtale om at datteren bor mest hos Anne, men med god samværsrett for Pål. Saken avsluttes lykkelig."}],
        "vanlige_feil": ["Som saksøker bli sint fordi dommeren \"tvinger\" frem forhandlinger (forlik) i stedet for å bare høre vitnene dine rakke ned på eksen. (Dette er dommerens lovpålagte jobb).", "Signere et forlik i retten fordi du føler deg presset (\"dommeren mente dette var best\"), for så å angre neste uke. Et rettsforlik er en bindende dom, du kan ikke klage på det senere."],
        "hva_bor_du_html": "<p>Involver deg konstruktivt i rettsmøtene. Dommeren noterer seg mentaliteten til partene. Hvis du blankt avviser alle forsøk på forlik og insisterer på at eksen er djevelen (uten bevis for overgrep), vil dommeren og psykologen krysse deg av som konflikt-eskalerende. Vis at du er løsningsorientert og tar innspillene dommeren og den sakkyndige gir i prosessen.</p>",
        "dumme_sporsmal": [
            {"q": "Hva skjer hvis forliket (pratingen) slår helt feil og eksen nekter å rikke seg en millimeter?", "a": "Dommeren plikter kun å \"vurdere om det er mogeleg\" å forlike dere. Er eksen klin gæren og nekter alt kompromiss, konkluderer dommeren med at forlik er umulig. Dommeren bestiller da en \"hovedforhandling\". Det er den klassiske, strenge rettssaken der advokater prosedyrer, vitner avhøres i vitneboksen, og dommeren deretter feller en ufravikelig, skriftlig dom."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "61", "tittel": "selve \"verktøykassen\" dommeren bruker under rettssaken (oppnevning av psykologer og test-perioder)", "available": True},
        ],
    },
    {
        "number": "60",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Domstolen kan ta en \"midlertidig\" avgjørelse",
        "kategori": "familie",
        "description": "En rettssak tar lang tid. Må du sikre barnet mot vold eller bortføring i dag? Loven gir deg rett til å be om en \"førebels\" (midlertidig) hasteavgjørelse.",
        "kort_svar": "En vanlig rettssak tar mange måneder. Hvis du ikke har tid til å vente – fordi eksen truer med å flytte ut av landet, du frykter vold, eller barnet blir holdt tilbake ulovlig – kan du be domstolen om en midlertidig avgjørelse. Denne fattes svært raskt av dommeren, og gjelder helt frem til selve rettssaken er overstått.",
        "paragraftekst": """Retten kan etter krav frå ein part ta førebels avgjerd om foreldreansvar, flytting med barnet ut av landet, kven barnet skal bu fast saman med, og samvær. Sak om førebels avgjerd om flytting med barnet ut av landet kan reisast av forelder med foreldreansvar og av forelder som samstundes reiser sak om foreldreansvar. Slik avgjerd kan gjelde for ei viss tid eller til saka er endeleg avgjord. Retten kan også ta førebels avgjerd før saka er reist, dersom særlege grunnar talar for det. Etter krav frå ein part skal retten i alle høve ta førebels avgjerd dersom det er ein risiko for at barnet blir utsett for vald eller på anna vis handsama slik at den fysiske eller psykiske helsa blir utsett for skade eller fare.

Retten kan samstundes forby den andre av foreldra å kome til den eigedommen eller det bustadhuset der barnet held til. Dersom det ikkje trengst avgjerd straks, skal retten så langt råd er gje den andre høve til å uttale seg.

Når avgjerd er teken før sak er reist, skal retten setje ein frist for å reise søksmål. Fristen kan forlengjast ved avgjerd av dommaren. Er det ikkje teke ut søksmål innan fristen, fell tekne avgjerder bort.

Avgjerdene vert tekne i orskurd. Det er ikkje nødvendig å halde munnleg forhandling på førehand.""",
        "hva_betyr_html": """<p>Paragraf 60 er familierettens nødbrems. Når konflikter oppstår, kan det ta opptil et år fra du sender en stevning til dommeren har avsagt en endelig dom. Men et barn kan ikke leve i limbo, fare eller kaos i et helt år.</p>
<p>Derfor kan advokaten din be retten om en "førebels avgjerd" (midlertidig kjennelse). Dette er en lynrask avgjørelse dommeren tar, som regel uten å innkalle til noen stor rettssak med vitner (fjerde ledd). Dommeren leser bare dokumentene og tar et valg som gjelder fra dags dato og frem til den ordentlige rettssaken er ferdig.</p>
<p>Dette verktøyet brukes for å fryse en farlig eller kaotisk situasjon. Du kan be om midlertidig avgjørelse på alle de store tingene: Hvem skal ha barnet boende hos seg akkurat nå? Skal samværet stoppes midlertidig? Skal eksen nektes å reise til utlandet med barnet?</p>
<p>Loven gir dommeren en streng plikt: Hvis du beviser at det er en reell risiko for at barnet blir utsatt for vold, overgrep eller psykisk skade hos eksen, <em>skal</em> dommeren fatte en midlertidig avgjørelse som beskytter barnet umiddelbart. I slike ekstreme tilfeller kan dommeren til og med nedlegge et forbud mot at den voldelige forelderen i det hele tatt får lov til å nærme seg huset der barnet bor (andre ledd).</p>
<p>Du kan be om en midlertidig avgjørelse selv om du ikke har sendt inn hovedsøksmålet (stevningen) ennå. Men hvis du gjør det, vil dommeren gi deg en tidsfrist. Hvis du ikke sender den ordentlige stevningen innen fristen, slettes den midlertidige avgjørelsen.</p>""",
        "eksempler": [{"navn": "Nekter å levere tilbake", "tekst": "Sara og Petter har delt fast bosted for sønnen Tobias (6). Etter sommerferien ringer Petter og sier: \"Tobias blir boende hos meg på heltid, jeg kjører ham ikke tilbake til deg\". Sara fortviler, for Tobias sin skole starter om to dager hos henne. En rettssak vil ta måneder. Sara kontakter advokat og krever en \"midlertidig avgjørelse\" etter § 60. Dommeren ser på saken i løpet av to dager. Siden de hadde en fungerende 50/50-avtale, og Petter tok seg til rette med makt (selvtekt), skriver dommeren en midlertidig kjennelse: \"Tobias skal bo fast hos Sara frem til hovedrettssaken er avgjort, og Petter pålegges å levere ham umiddelbart.\" Petter må bøye seg for dommeren."}],
        "vanlige_feil": ["Foreldre prøver å be om \"midlertidig avgjørelse\" bare fordi de er irriterte over småting, for eksempel at eksen gir barnet for mye sukker. (Dommeren avviser dette; hasteverktøyet er kun for alvorlige eller fastlåste situasjoner).", "Holde tilbake barnet med makt og tro at man tjener på det. (Domstolen slår som regel knallhardt ned på foreldre som tar loven i egne hender. Den midlertidige avgjørelsen går da nesten alltid i favør av den som ble frastjålet barnet)."],
        "hva_bor_du_html": "<p>Står du i en akutt krise? Har eksen tatt barnet og nektet å levere tilbake, eller truer med å flytte ut av landet i morgen? Da må du ringe en advokat øyeblikkelig. Advokaten vil skrive en begjæring (et krav) om midlertidig avgjørelse. Sørg for å ha bevis klare – SMS-er, e-poster, uttalelser fra skole/barnehage – for at situasjonen er akutt og skadelig for barnet.</p>",
        "dumme_sporsmal": [
            {"q": "Får eksen min lov til å forsvare seg før dommeren bestemmer noe?", "a": "Hovedregelen er ja. Dommeren vil sende kravet ditt til eksen og gi en ekstremt kort frist (ofte bare noen dager) til å skrive et tilsvar. Men, hvis det er snakk om akutt livsfare for barnet, eller fare for at faren setter barnet på et fly til utlandet samme kveld, kan dommeren skrive kjennelsen bak lukkede dører før eksen i det hele tatt vet at saken har startet."},
            {"q": "Varer den midlertidige kjennelsen for alltid?", "a": "Nei, den dør i det øyeblikket hovedrettssaken er ferdig og den endelige dommen faller. Den endelige dommen kan komme frem til akkurat det samme, eller dommeren kan ha endret mening etter å ha hørt på vitner og psykologer."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "56", "tittel": "hvordan du reiser hovedrettssaken som hører til", "available": True},
            {"lov": "barnelova", "paragraf": "61", "tittel": "hvordan selve hovedsaken skal kjøres (mens den midlertidige kjennelsen gjelder)", "available": True},
        ],
    },
    {
        "number": "61",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Rettens mektige verktøykasse under barnefordeling",
        "kategori": "familie",
        "description": "Hvordan fungerer en barnefordelingssak i retten? Dette er paragrafen som styrer alt. Lær hvordan dommeren bruker psykologer, barnevern og test-perioder for å finne ut hva som er best for barnet.",
        "kort_svar": "En rettssak om barn handler om å finne den beste løsningen. Derfor har dommeren fått en stor verktøykasse. I stedet for en vanlig rettssak, starter man med \"saksforberedende møter\". Her kan dommeren kalle inn en barnepsykolog (sakkyndig), be foreldrene prøve ut en ny samværsavtale, snakke med barnet, eller be barnevernet om en rapport. Alt for å unngå en brutal dom.",
        "paragraftekst": """Retten fastset tid for hovudforhandling straks eller etter at eitt eller fleire av tiltaka i nr. 1 til 7 nedanfor er gjennomført.

1. Retten skal som hovudregel innkalle partane til eitt eller fleire førebuande møte for mellom anna å klarleggje tvistepunkta mellom dei, drøfte vidare handsaming av saka og eventuelt mekle mellom partane der saka er eigna for det. Retten kan oppnemne ein sakkunnig til å vere med i dei saksførebuande møta. Retten kan jamvel be den sakkunnige ha samtalar med foreldra og barna og gjere undersøkingar for å klarleggje tilhøva i saka, med mindre foreldra set seg i mot dette. Retten fastset kva den sakkunnige skal gjere, etter at partane har fått høve til å uttale seg. 2. Retten kan vise partane til mekling hos godkjend meklar eller annan person med innsikt i dei tvistepunkta saka gjeld. §§ 52 og 53 gjeld tilsvarande. Dersom meklaren kjem fram til at partane ikkje kan nå fram til ein avtale gjennom vidare mekling, skal han straks melde frå til retten om dette. 3. Der det trengst, bør retten oppnemne sakkunnig til å uttale seg om eitt eller fleire av spørsmåla som saka reiser. Der det er sett fram påstandar om vald, overgrep, rus eller psykisk liding og saka ikkje er tilstrekkeleg opplyst på anna måte, kan retten oppnemne ein sakkunnig. 4. Dommaren kan gjennomføre samtalar med barnet, jf. § 31. Retten kan oppnemne ein sakkunnig eller annan eigna person til å hjelpe seg, eller la ein sakkunnig ha samtale med barnet aleine. Der barnet har formidla meininga si, skal dommaren eller den dommaren peiker ut orientere barnet om utfallet av saka og korleis meininga til barnet har blitt teke omsyn til. 5. Retten kan i særlege høve, mellom anna når det er grunn til å tru at barnet er utsett for vald eller på anna vis blir handsama slik at den fysiske eller psykiske helsa blir utsett for skade eller fare, oppnemne ein advokat eller annan representant til å ta vare på interessene til barnet i samband med søksmålet. Den som er oppnemnd, kan samtale med barnet og skal gje slik informasjon og støtte som er naturleg. Advokaten eller representanten skal få saksdokumenta. Han kan kome med framlegg om handsaminga av saka og skriftleg eller i rettsmøte gje råd om korleis sakshandsaminga best kan ta vare på interessene til barnet. Retten avgjer om og eventuelt kor lenge han skal vere til stades under rettsmøta i saka. Når advokaten eller representanten er til stades i rettsmøta, kan han stille spørsmål til partar og vitne. 6. Retten bør innhente fråsegner frå barnevernet og sosialtenesta der det trengst. 7. Retten kan gje partane høve til å prøve ut ei førebels avtale for ei nærare fastsett tid. Retten kan oppnemne ein sakkunnig eller annan eigna person til å rettleie foreldra i prøvetida. 8. Retten kan gje dom utan hovudforhandling så framt partane samtykkjer til det og retten ser det som forsvarleg.

Staten ber kostnadene til dei tiltaka som er nemnde i første stykket nr. 1, 2, 3, 4, 5 og 7. Sakkunnig som vert oppnemnd etter første stykket skal godtgjerast etter lov 21. juli 1916 nr. 2 om vidners og sakkyndiges godtgjørelse m.v. Dersom det skal oppnemnast ein advokat for barnet etter første stykket nr. 5, har barnet rett på fri sakførsel utan behovsprøving jf. rettshjelpsloven § 16 første ledd nr. 6. Departementet kan ved forskrift fastsetje reglar om godtgjering til andre som gjer teneste etter paragrafen her.

Sakkunnig som vert oppnemnd av domstolen etter denne paragrafen, skal leggje fram politiattest som nemnd i politiregisterloven § 39. Det same gjeld advokatar eller andre som blir oppnemnde som representantar for barnet. Hastar oppnemninga, kan oppnemning skje før det er innhenta politiattest.""",
        "hva_betyr_html": """<p>Glem alt du har sett av amerikanske advokatskuespillere i rettssalen. Når du sender en barnefordelingssak til tingretten, er det § 61 som bestemmer hva som faktisk skjer.</p>
<p>Dommeren bruker det vi kaller "den konfliktdempende modellen". Målet er å unngå en full rettssak. I stedet kaller dommeren inn deg, eksen og advokatene deres til et "saksforberedende møte". Dette er ofte et litt uformelt møte rundt et bord inne i tinghuset.</p>
<p>For å finne ut hva som er barnets beste (se § 48), gir loven dommeren 8 konkrete verktøy:</p>
<p><strong>1. Den sakkyndige psykologen:</strong> Dommeren kan be en psykolog om å bli med på møtet. Denne psykologen kan (hvis dere godtar det) dra hjem til dere for å se hvordan dere samhandler med barnet, og gi råd til dommeren. <strong>2. Mer mekling:</strong> Dommeren kan sende dere tilbake til en terapeut hvis dommeren tror dere egentlig kan bli enige. <strong>3. Full psykologisk utredning:</strong> Hvis du anklager eksen for vold, rus eller alvorlige psykiske problemer, kan dommeren be en sakkyndig om å gjøre en full utredning for å sjekke om anklagene stemmer. <strong>4. Snakke med barnet:</strong> Loven krever at barn over 7 år skal bli hørt (se § 31). Dommeren eller psykologen snakker med barnet i enerom, og må etterpå fortelle barnet hva dommeren bestemte og hvorfor. <strong>5. Egen advokat for barnet:</strong> Hvis foreldrene kriger så hardt at barnet utsettes for fare, kan barnet få sin helt egen advokat betalt av staten, for å sikre at noen står på barnets side mot gale foreldre. <strong>6. Rapport fra barnevernet:</strong> Hvis barnevernet kjenner familien, kan dommeren hente ut alle mappene deres. <strong>7. Prøveordninger:</strong> Hvis dommeren er usikker på hvem som har rett, kan han si: "Vi prøver ut fars forslag i tre måneder, så møtes vi her igjen i oktober og ser hvordan det gikk for barnet." En psykolog vil overvåke hvordan det går i denne prøveperioden. <strong>8. Skriftlig dom:</strong> Er dere helt enige på slutten, kan dommeren bare skrive en dom eller godkjenne forliket uten noen videre prosess.</p>
<p>Fungerer ingenting av dette? Hvis dere har hatt tre slike saksforberedende møter over ti måneder og fremdeles hater hverandre like mye, pakker dommeren vekk verktøykassen. Da kaller dommeren inn til en hovedforhandling (vanlig rettssak), hører på alle bevisene, og feller en endelig dom.</p>
<p>Alt av psykologer og barnets advokat betales hundre prosent av staten, uansett inntekten din.</p>""",
        "eksempler": [{"navn": "Hvordan prøveordningen reddet familien", "tekst": "Tom og Lise er i tingretten. Lise vil ha barna 100 % fordi Tom angivelig ikke takler stresset med to småbarn. Tom vil ha 50/50. Dommeren bruker § 61 nr. 7. Han bestemmer at de skal ha en prøveordning: \"I tre måneder skal Tom ha barna 50/50. Den oppnevnte barnepsykologen skal besøke Tom to ganger og se hvordan han håndterer stresset.\" Tre måneder senere møtes de i tingretten igjen. Psykologen legger frem en rapport som viser at Tom var en ypperlig, rolig far, og at barna stortrivdes med 50/50. Lise innser at bekymringen hennes var ubegrunnet, og de inngår et frivillig rettsforlik (enighet) i retten der Tom får 50/50. De slapp en grusom rettssak."}],
        "vanlige_feil": ["Nekte å la den sakkyndige psykologen besøke hjemmet ditt eller snakke med barnet fordi du er \"redd de skal vri på ordene\". (Å motarbeide sakkyndig vurderes nesten alltid som et enormt svakhetstegn og ødelegger troverdigheten din).", "Bryte reglene i prøveordningen. Gjør du det, beviser du at du ikke evner å samarbeide, og du vil tape hovedsaken."],
        "hva_bor_du_html": "<p>Ditt viktigste fokus i de saksforberedende møtene er å virke lyttende, rolig og barn-orientert. Dommeren og psykologen ser på alt du gjør. Tilbyr dommeren en \"prøveordning\" (selv om den ikke er akkurat slik du vil ha den), er det ofte smart å godta den for å vise at du er fleksibel. Pass på å samarbeide godt med den sakkyndige psykologen; dommeren hører nesten alltid på hva den sakkyndige anbefaler.</p>",
        "dumme_sporsmal": [
            {"q": "Får barnet vite hva jeg har sagt om dem til dommeren?", "a": "Nei, barnet blir skånet for skittkastingen. Barnet har en uformell samtale med dommeren eller psykologen, og de voksne får et referat av hva barnet har sagt. Mange dommere og psykologer er svært forsiktige for å ikke presse barnet til å \"velge\"."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "60", "tittel": "hvordan dommeren fastsetter noe midlertidig hvis det brenner", "available": True},
            {"lov": "barnelova", "paragraf": "31", "tittel": "selve lovregelen om barnets rett til å bli hørt", "available": True},
            {"lov": "barnelova", "paragraf": "48", "tittel": "grunnprinsippet (barnets beste) som dommeren styrer etter", "available": True},
        ],
    },
    {
        "number": "61a",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Barnevernet fritas fra taushetsplikt overfor domstolen",
        "kategori": "familie",
        "description": "Barnevernet har streng taushetsplikt. Men hvis du ligger i rettssak om barnefordeling, kan dommeren hente ut papirene deres uansett for å beskytte barnet.",
        "kort_svar": "Vanligvis har barnevernet en streng lovpålagt taushetsplikt om sine klienter. Paragraf 61 a fungerer som en nøkkel for domstolen: Den lar barnevernet gi alle opplysninger de sitter på, rett til dommeren i en barnefordelingssak, uten at foreldrene kan stanse dem.",
        "paragraftekst": "Barnevernstenesta kan uhindra av teieplikta etter barnevernsloven § 13-1 gi opplysningar til domstolen i sak om foreldreansvar, kvar barnet skal bu fast og samvær.",
        "hva_betyr_html": """<p>Når mor og far kjemper om hvem barnet skal bo hos (etter § 61), er dommerens største frykt å gi barnet til en forelder som er skadelig for barnet. Ofte sitter barnevernet på nøkkelen til sannheten, fordi de kanskje har undersøkt fars rusproblem eller mors sinneutbrudd tidligere.</p>
<p>Normalt har de som jobber i barnevernet absolutt taushetsplikt. Hvis en advokat ringer og spør, får de ikke svare.</p>
<p>Denne regelen i barneloven knuser den taushetsplikten i disse konkrete rettssakene. Den sier at barnevernet har full rett til å oversende rapporter, bekymringsmeldinger og referater direkte til domstolen når saken gjelder foreldreansvar, bosted eller samvær. Hverken mor eller far trenger å samtykke til (godkjenne) at dommeren får papirene.</p>
<p>Dette sikrer at dommeren (og den sakkyndige psykologen) ikke dømmer i blinde, men vet nøyaktig hva barnevernet allerede har vurdert som farlig for barnet.</p>""",
        "eksempler": [{"navn": "Den skjulte mappen", "tekst": "Far saksøker mor for å få fast bosted. I retten fremstår mor som rolig, hyggelig og ressurssterk. Far hevder at hun drikker og at barnevernet har vært inni bildet. Mor nekter, og nekter å oppheve taushetsplikten for barnevernet for å bevise det. Dommeren bruker § 61 a og ber det lokale barnevernskontoret sende over mappen. Uten mors samtykke dumper dokumentene ned på dommerens bord, og avslører tre alvorlige undersøkelser på grunn av fyll. Dommeren gir far medhold i at barnet flyttes, fordi dokumentene fra barnevernet viste sannheten."}],
        "vanlige_feil": ["En forelder tror at de kan \"nekte\" dommeren tilgang til barnevernets dokumenter for å skjule en dårlig fortid.", "Advokater glemmer å be domstolen innhente papirene fra barnevernet i en sak der bekymringsmeldinger er et kjernetema."],
        "hva_bor_du_html": """<p>Har eksen din et rulleblad hos barnevernet som beviser at de ikke bør ha den daglige omsorgen? Be din advokat fremsette et formelt krav til dommeren (i stevningen) om at domstolen må innhente disse dokumentene etter barneloven § 61 a.</p>
<p>Er det <em>du</em> som har en historie hos barnevernet? Vær ærlig om det med en gang overfor dommeren og den sakkyndige. Dommeren vil få vite det uansett, og hvis du lyver om at barnevernet aldri har vært involvert, vil du ødelegge din egen troverdighet totalt.</p>""",
        "dumme_sporsmal": [
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "48", "tittel": "hensynet til barnets beste, som krever all tilgjengelig informasjon", "available": True},
        ],
    },
    {
        "number": "61b",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Forskrifter om oppdraget til psykologen",
        "kategori": "familie",
        "description": "Staten setter strenge regler for hva psykologene (de sakkyndige) skal gjøre i rettssalen, slik at de oppfører seg riktig og rettferdig.",
        "kort_svar": "Paragrafen er en teknisk fullmakt. Den gir departementet lov til å lage detaljerte regler for hvordan en sakkyndig psykolog (som oppnevnes av retten) skal skrive rapportene sine, og hvilke grenser de har for arbeidet sitt.",
        "paragraftekst": "Departementet kan gje forskrift om utforminga av mandata til dei sakkunnige og utgreiingane deira.",
        "hva_betyr_html": """<p>I svært mange barnefordelingssaker brukes en "sakkyndig" (en spesialist, oftest psykolog) for å gi råd til dommeren. Noen foreldre opplever at disse psykologene tar for stor makt, sjekker ting de ikke burde, eller skriver rotete rapporter som feller feil forelder.</p>
<p>For å hindre "ville vesten" blant sakkyndige, har staten skrevet denne regelen. Den gir Barne- og familiedepartementet lov til å utstede strenge forskrifter. Forskriftene sier blant annet hva slags "mandat" (oppdrag) dommeren kan gi dem, og hvordan rapporten de leverer inn må se ut for å være lovlig. Som forelder vil du ikke merke mye til selve denne paragrafen, men det er den som sikrer at psykologens arbeid er faglig kvalitetssikret.</p>""",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "",
        "dumme_sporsmal": [
        ],
        "related": [
        ],
    },
    {
        "number": "61c",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Barnesakkunnig kommisjon kvalitetssjekker psykologen",
        "kategori": "familie",
        "description": "Føler du at psykologen i rettssaken din tok helt feil og skrev en elendig rapport? En uavhengig kommisjon kvalitetssikrer alle rapporter før dommeren får bruke dem.",
        "kort_svar": "Når en psykolog (sakkyndig) har skrevet en rapport for domstolen i din barnefordelingssak, må denne rapporten sendes til Barnesakkunnig kommisjon for en kvalitetskontroll. Dommeren har ikke lov til å bygge dommen sin på rapporten før kommisjonen har sjekket og godkjent den.",
        "paragraftekst": """Barnesakkunnig kommisjon skal vurdere kvaliteten på utgreiingar frå sakkunnige som er oppnemnde av retten etter § 61 første stykket nr. 3 og utgreiingar frå sakkunnige som ein part har engasjert.

Ein sakkunnig som er oppnemnd av retten etter § 61 første stykket nr. 3 skal sende utgreiinga til kommisjonen med kopi til retten. Er den sakkunnige engasjert av ein part, skal parten sende inn utgreiinga på same måten. Kommisjonen skal sende si vurdering til retten og den sakkunnige.

Retten kan berre leggje til grunn ei sakkunnig utgreiing som har vore vurdert av kommisjonen etter denne paragrafen.

Departementet nemner opp medlemmene i kommisjonen og kan gje forskrift om korleis kommisjonen skal vere organisert, kva oppgåver han skal ha, og korleis han skal handsame sakene.""",
        "hva_betyr_html": """<p>I rettssaker om barn veier psykologens (den sakkyndiges) ord ekstremt tungt. Sier psykologen at far er den beste omsorgspersonen, dømmer dommeren ofte i favør av far.</p>
<p>Men hva hvis psykologen var partisk, hadde dårlig faglig kunnskap, eller overhodet ikke begrunnet hvorfor mor var dårligere? For å forhindre justismord i barnefordeling, finnes Barnesakkunnig kommisjon. Dette er et panel av Norges beste barnepsykologer og spesialister.</p>
<p>Når "din" psykolog er ferdig med å utrede familien og har skrevet rapporten, kan han ikke bare gi den til dommeren og kreve at saken lukkes. Han <strong>må</strong> (andre ledd) sende den inn til kommisjonen.</p>
<p>Kommisjonen leser rapporten med kritisk blikk: Har psykologen gjort jobben sin skikkelig? Er konklusjonen logisk ut fra observasjonene? Er den faglig holdbar? Hvis de mener rapporten er slurvete eller mangelfull, sender de den tilbake med knallhard kritikk ("betydelige mangler").</p>
<p>Tredje ledd er det viktigste for rettssikkerheten din: Dommeren har ikke lov til å avsi dom basert på psykologens rapport før Barnesakkunnig kommisjon har lagt ved sin bedømmelse. Får psykologen slakt, vil advokaten din sørge for at dommeren ignorerer psykologens konklusjoner helt.</p>
<p>Det gjelder også hvis <em>du selv</em> har betalt en privat psykolog (sakkyndig "engasjert av en part") for å skrive en rapport som støtter deg. Den slipper heller ikke gjennom uten å passere kommisjonen først.</p>""",
        "eksempler": [{"navn": "Rapporten med vesentlige mangler", "tekst": "Mors advokat reagerer sterkt på rapporten den rettsoppnevnte psykologen har skrevet. Rapporten hevder mor er uegnet til å ha barnet fordi hun er reservert, men psykologen har bare snakket med mor i tjue minutter. Rapporten sendes til Barnesakkunnig kommisjon. Kommisjonen returnerer saken til tingretten med bemerkningen: \"Vesentlige mangler. Den sakkyndige mangler vitenskapelig grunnlag for å konkludere med uegnethet\". Dommeren avskilter psykologen, legger rapporten til side, og utnevner en ny, bedre sakkyndig til saken. Mor er reddet fra et mulig justismord."}],
        "vanlige_feil": ["Å prøve å snike inn en skriftlig uttalelse fra barnets fastlege eller en \"vanlig\" terapeut i bunken og kreve at det vektlegges like tungt. (Det blir ansett som bevis, men det er ikke en full \"sakkyndig utredning\" underlagt denne kommisjonens stempel).", "Bli fortvilet hvis psykologen skriver noe negativt om deg, uten å vente på kommisjonens knusende kontroll av metoden."],
        "hva_bor_du_html": "<p>Får den sakkyndige psykologen i saken din sterk kritikk av Barnesakkunnig kommisjon, og kritikken rammer deler av rapporten som gikk i din ulempe? Da må du og advokaten din hamre løs på dette under selve rettssaken (hovedforhandlingen), og be dommeren se bort ifra psykologens vurderinger fullstendig. Hvis kommisjonen tvert imot sier at rapporten \"har ingen bemerkninger\" (den er godkjent), må du forberede deg på at dommeren nesten garantert kommer til å følge psykologens råd.</p>",
        "dumme_sporsmal": [
            {"q": "Kan jeg klage til kommisjonen og be dem lese rapporten?", "a": "Nei, du trenger ikke gjøre noen ting for at dette skal skje. Kravet om innsendelse er automatisk lovpålagt. Psykologen har selv ansvar for å sende inn rapporten. Du får kopi av hva kommisjonen mener når de er ferdige (ofte tar det tre uker)."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "61", "tittel": "om selve utnevnelsen av den sakkyndige psykologen", "available": True},
        ],
    },
    {
        "number": "61d",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Barnesakkunnig kommisjon og personopplysninger",
        "kategori": "familie",
        "description": "Kommisjonen som sjekker arbeidet til psykologene i retten, har lov til å håndtere svært sensitive personopplysninger om deg og barnet ditt.",
        "kort_svar": "Barnesakkunnig kommisjon har lov til å lese og lagre sensitive opplysninger om familien din. Dette gjør de for å kunne kvalitetssikre de psykologiske rapportene som brukes i rettssaken deres.",
        "paragraftekst": "Personopplysningsloven gjeld for Barnesakkunnig kommisjon. Kommisjonen kan handsame personopplysningar, medrekna personopplysningar som nemnde i personvernforordninga artikkel 9 og 10, når det er naudsynt for å utføre oppgåver etter § 61 c eller forskrift i medhald av § 61 c fjerde stykket.",
        "hva_betyr_html": """<p>Dette er en teknisk personvernregel (GDPR). Når du er i en rettssak om barnefordeling, vil psykologene (de sakkyndige) grave dypt i livet ditt. De skriver rapporter om din psykiske helse, eventuelle rusproblemer, voldshistorikk og barnets traumer.</p>
<p>Som forklart i § 61 c, skal en egen kommisjon lese gjennom disse rapportene for å sjekke at psykologen har gjort en god jobb, før dommeren får bruke rapporten.</p>
<p>Paragraf 61 d slår simpelthen fast at denne kommisjonen har full juridisk rett til å håndtere disse ekstremt private opplysningene (det loven kaller artikkel 9 og 10-opplysninger: helse, straffedommer, genetikk). De bryter ikke personvernet ditt ved å lese dem, for de har en lovpålagt oppgave å utføre for å sikre at domstolen tar riktige avgjørelser for barnet ditt.</p>""",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "",
        "dumme_sporsmal": [
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "61", "tittel": "reglene for bruk av psykolog i retten", "available": True},
        ],
    },
    {
        "number": "62",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Kan du klage på dommerens valg underveis i saken?",
        "kategori": "familie",
        "description": "Er du uenig i at dommeren vil bruke en psykolog i barnefordelingssaken? Du må nesten alltid godta dommerens verktøy, for loven nekter deg å anke.",
        "kort_svar": "Som hovedregel kan du ikke anke de praktiske valgene dommeren tar mens rettssaken forberedes (for eksempel at dommeren innkaller dere til forhandlingsmøter eller oppnevner en sakkyndig psykolog). Du må bare delta. Unntaket er hvis dommeren *nekter* å hente inn barnevernet eller nekter å bruke psykolog, da kan du anke.",
        "paragraftekst": "Rettens val av tiltak etter § 61 første stykket kan ikkje ankast. Unntak gjeld for avgjerd om å nekte å oppnemne sakkunnig etter § 61 første stykket nr. 3 og avgjerd om å nekte å innhente fråsegner som nemnd i § 61 første stykket nr. 6.",
        "hva_betyr_html": """<p>En rettssak om barn kan ta mange måneder. I denne perioden (saksforberedelsen) har dommeren en stor "verktøykasse" i barneloven § 61. Dommeren kan be om at dere møtes til uformelle samtaler, eller at en psykolog skal observere deg og eksen sammen med barnet.</p>
<p>Kanskje du hater tanken på at en psykolog skal vurdere deg, og ber advokaten din om å anke (klage) dommerens beslutning inn for lagmannsretten.</p>
<p>Paragraf 62 sier stopp. For å unngå at foreldre trenerer og forsinker rettssaker med evigvarende klager på småting, har staten bestemt at dommerens valg av tiltak er endelige. Sier dommeren at en psykolog skal inn i saken, så blir det slik. Du kan ikke anke det.</p>
<p>Men det finnes to kritiske unntak. Hvis du mener at eksen din er farlig, og du trygler dommeren om å oppnevne en sakkyndig psykolog for å bevise det, eller ber dommeren hente inn dokumentene fra barnevernet, og dommeren sier <em>nei</em> – da har du lov til å anke det avslaget til en høyere domstol. Staten vil heller at en sak forsinkes enn at farlige foreldre slipper unna granskning.</p>""",
        "eksempler": [{"navn": "Psykologen Tom ikke ville ha", "tekst": "Saken mellom Tom og Siri har startet i tingretten. Dommeren bestemmer at en barnepsykolog skal ha fire samtaler med paret. Tom synes dette er noe tull og vil bare ha en rask rettssak. Han instruerer advokaten sin om å anke beslutningen om å bruke psykolog. Advokaten nekter og viser til § 62: De har ikke lov til å anke rettens bruk av saksforberedende tiltak. Tom må bite tennene sammen og møte opp hos psykologen."}],
        "vanlige_feil": ["Bli sint på sin egen advokat for at de \"ikke gjør noe\" for å stoppe dommerens tette oppfølging i saksforberedelsene.", "Kaste bort tid på å protestere skriftlig til dommeren over at prosessen tar en retning man ikke liker."],
        "hva_bor_du_html": "<p>Godta at i barnefordelingssaker er det dommeren som styrer prosessen og tempoet. Din jobb er å samarbeide så godt du kan med de personene dommeren setter inn i saken. Det tjener saken din best i lengden.</p>",
        "dumme_sporsmal": [
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "61", "tittel": "hele listen over de tiltakene dommeren kan tvinge dere gjennom", "available": True},
            {"lov": "barnelova", "paragraf": "59", "tittel": "dommerens plikt til å forsøke å forlike dere underveis", "available": True},
        ],
    },
    {
        "number": "63",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Når kan du ta opp igjen en gammel barnefordelingssak?",
        "kategori": "familie",
        "description": "Har du allerede en dom eller avtale fra retten? Du kan ikke saksøke eksen på nytt bare fordi du er misfornøyd. Loven krever at det har skjedd noe viktig.",
        "kort_svar": "Selv om dere har en dom fra retten om hvem barnet skal bo hos, kan dere fritt endre dette hvis dere blir enige om det. Hvis dere derimot *ikke* er enige, og du vil saksøke eksen for å endre en eksisterende dom eller et rettsforlik, må du bevise at det foreligger \"særlige grunner\" (betydelige endringer) for å i det hele tatt få starte en ny rettssak.",
        "paragraftekst": """Foreldra kan gjere om avtale eller avgjerd om foreldreansvaret, om flytting med barnet ut av landet, om kven barnet skal bu hos fast og om samværsretten.

Vert foreldra ikkje samde, kan kvar av dei reise sak for retten, jf. § 56. Dom, rettsforlik og avtale med tvangskraft kan likevel berre endrast når særlege grunnar talar for det. Førebels avgjerd etter § 60 kan endrast på same vilkår av den domstolen som har hovudsaka. Dersom ein av foreldra har flytta med barnet utan at foreldra var samde, kan den andre av foreldra reise ny sak for retten.

Dersom det er openbert at det ikkje ligg føre slike særlege grunnar som nemnt i andre stykket, kan retten avgjere saka utan hovudforhandling.""",
        "hva_betyr_html": """<p>I mange typer konflikter i samfunnet er en dom fra domstolen endelig. Du kan ikke prøve saken på nytt tre år senere. Slik er det ikke med barn. Et barn forandrer seg, foreldre flytter, og hverdagen endres. Derfor sier paragraf 63 at avtaler og dommer om barn aldri er støpt i betong. Dere foreldre kan når som helst kaste den gamle dommen og avtale noe helt annet, så lenge dere er enige (første ledd).</p>
<p>Men hva hvis dere ikke er enige? Kanskje far tapte saken i 2022 og barnet bor hos mor. Nå i 2025 vil han saksøke mor igjen for å få 50/50.</p>
<p>For å beskytte barn mot foreldre som gjør rettssaler til en evig slagmark, bygger loven en mur: Kravet om <strong>"særlege grunnar"</strong>. Dommeren vil ikke røre den gamle dommen med mindre far kan bevise at det har skjedd noe vesentlig siden sist.</p>
<p>Særlige grunner kan være:</p>
<ul><li>Barnet var 8 år ved forrige dom, men er nå 13 år og sier tydelig at hen vil bo hos far i stedet.</li><li>Mor (som har daglig omsorg) har begynt å ruse seg eller blitt alvorlig syk.</li><li>Mor saboterer samværet systematisk og nekter far å se barnet. (Sabotasje er en klassisk "særlig grunn" til å flytte barnet).</li><li>En av foreldrene flyttet plutselig til en annen kant av landet mot den andres vilje.</li></ul>
<p>Hvis far sender en ny stevning og bare skriver "Jeg har lyst til å ha barnet mer fordi jeg savner henne", så avviser dommeren saken. Tredje ledd sier rett ut at hvis saken åpenbart mangler nye, tunge grunner, kan dommeren bare slenge døra i ansiktet på deg skriftlig ("utan hovudforhandling"), og du taper saken før den har begynt.</p>""",
        "eksempler": [{"navn": "Det nye søksmålet", "tekst": "I 2021 signerte Hanne og Lars et rettsforlik. Hanne fikk daglig omsorg, Lars fikk samvær annenhver helg. I 2023 var Lars misfornøyd og saksøkte Hanne fordi han ville ha en uke ekstra i måneden, men han hadde ingen andre argumenter enn at det var \"urettferdig\". Retten avviste saken hans umiddelbart etter § 63 tredje ledd; det fantes ingen \"særlige grunner\". I 2025 flytter Hanne plutselig med barnet til en by åtte timer unna, til tross for Lars sine protester. Lars saksøker Hanne igjen. Nå sier dommeren ja til å behandle saken. En stor geografisk flytting regnes som en særlig grunn for å revurdere den gamle avtalen."}],
        "vanlige_feil": ["Bytte advokat etter et tap i retten, for så å saksøke på nytt måneden etter fordi den nye advokaten er \"tøffere\". (Du kommer ikke forbi kravet om at situasjonen må ha endret seg betydelig siden dommen falt).", "Tro at en \"privat\" avtale skrevet på kjøkkenbordet krever særlige grunner for å endres. (Nei, det er bare formelle avtaler: dom, rettsforlik og avtaler stemplet av Statsforvalteren som beskyttes av dette strenge kravet)."],
        "hva_bor_du_html": "<p>Har du tapt en sak i tingretten, må du la saken hvile. Ikke fyll hodet ditt med tanker om ny rettssak neste år. Fokuser på å være den beste samværsforelderen du kan være. Først når barnet blir betydelig eldre og får en egen sterk mening (§ 31), eller eksen din begår grove feil som skader barnet (som vold, rus eller massiv samværssabotasje), bør du ta kontakt med en advokat for å vurdere et nytt søksmål.</p>",
        "dumme_sporsmal": [
            {"q": "Hvor lenge må jeg vente før barnet er \"gammelt nok\" til at det regnes som en særlig grunn?", "a": "Det finnes ingen fast fasit, men domstolene regner sjelden ett eller to år som nok i seg selv for små barn. Men spranget fra barneskole (f.eks. 9 år ved dom) til ungdomsskole (13 år) utløser nesten alltid en ny rett til å prøve saken, siden barneloven § 31 gir en 12-13-åring lovfestet rett til å bli sterkt vektlagt."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "56", "tittel": "grunnregelen for å reise sak første gang", "available": True},
            {"lov": "barnelova", "paragraf": "55", "tittel": "Statsforvalterens stempel, som gir en avtale samme vern som en dom", "available": True},
        ],
    },
    {
        "number": "64",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hva skjer i domstolen når foreldreansvaret er tomt etter dødsfall?",
        "kategori": "familie",
        "description": "Når en forelder med foreldreansvar dør, er det ikke hvem som helst som kan ta over. Tingretten avgjør hvem som får ansvaret og hvor barnet skal bo.",
        "kort_svar": "Hvis en gjenlevende forelder manglet foreldreansvar og ikke bodde med barnet da den andre forelderen døde, får de ikke barnet automatisk. Den gjenlevende kan da reise sak for tingretten for å kreve ansvaret. Tingretten vurderer saken grundig og kan velge å gi barnet til faren, eller til andre i barnets krets (som besteforeldre) hvis det er best for barnet.",
        "paragraftekst": """Dersom den attlevande som får foreldreansvaret etter § 38 første stykket, ikkje budde saman med barnet på tidspunktet for dødsfallet, kan andre reise sak med krav om å få foreldreansvaret. Fristen for å reise sak er seks månader etter dødsfallet. Retten kan ta førebels avgjerd etter § 60.

Dersom den attlevande er sikta, tiltala eller dømd for forsettleg å ha valda den andre forelderen sin død, kan andre reise sak med krav om å få foreldreansvaret. Fristen for å reise sak er seks månader etter at siktinga eller tiltala er fråfallen eller dom i straffesaka er rettskraftig. Den attlevande kan også reise slik sak.

Retten skal leggje vekt på om den attlevande ønskjer foreldreansvaret. Retten bør også leggje vekt på den avdøde sine ønskjer, særleg når de er uttrykt skriftleg. Er den attlevande sikta, tiltala eller dømd for forsettleg å ha valda den andre forelderen sin død, kan den attlevande berre få eller framleis ha foreldreansvaret dersom dette klart er til det beste for barnet.

Retten skal avgjere spørsmålet om foreldreansvar ved dom. Retten bør innhente fråsegner frå den kommunale barnevernstenesta der det trengst. Retten bør gje dei næraste slektningane til barnet eller dei som barnet bur saman med, høve til å uttale seg, med mindre dette er uturvande.

Retten kan la ein person få foreldreansvaret aleine eller la gifte eller sambuande få det saman. Retten kan la ein forelder få eller framleis ha foreldreansvaret sjølv om andre får foreldreansvar. Retten kan setje som vilkår for avgjerda at barnet i ei viss tid ikkje skal måtte flytte frå heimen der det bur, dersom flyttinga kan vere uheldig for barnet, og det ikkje er rimeleg grunn til å flytte.

Når fleire får foreldreansvar, skal retten også ta avgjerd om kven barnet skal bu fast saman med. Retten kan alltid ta avgjerd om samvær for den attlevande. For den eller dei som får foreldreansvar, gjeld reglane i kapittel 5 og 6.

Retten skal gje melding til den kommunale barnevernstenesta og statsforvaltaren dersom ingen har vendt seg til retten etter § 64 a, eller dersom dommen fører til at ingen har foreldreansvar for barnet. Barnevernstenesta skal plassere og følgje opp barnet etter reglane i barnevernsloven.""",
        "hva_betyr_html": """<p>Paragraf 64 er den lange prosedyre-regelen for hva som skjer i retten når en forelder dør, og det er strid om hvem som skal overta barnet.</p>
<p><strong>Situasjon 1: Mor dør, far hadde felles ansvar (Første ledd)</strong> Etter § 38 vet vi at hvis mor dør, og far hadde felles ansvar, så får far barnet automatisk. MEN: Hva hvis far bor i en annen by, og barnet har bodd 100 % hos mor og en stefar de siste fem årene? For å hindre at barnet blir revet brutalt vekk fra alt det kjenner, gir loven stefaren (eller besteforeldre) en frist på 6 måneder etter dødsfallet til å saksøke faren. Stefaren kan kreve å få foreldreansvaret i stedet. Retten må da vurdere om faren skal få beholde sitt automatiske ansvar, eller om barnets trygghet hos stefaren veier tyngre.</p>
<p><strong>Situasjon 2: Partnerdrap (Andre og tredje ledd)</strong> Hvis den gjenlevende er siktet for å ha drept den andre forelderen, mister de retten til å få barnet på vanlig måte. Da kan tanter, onkler eller fosterforeldre saksøke for å ta over. Terskelen for at en partnerdraps-tiltalt skal få tilbake barnet sitt, er enormt høy. Loven sier at de bare kan få ansvaret hvis det "klart er til det beste for barnet".</p>
<p><strong>Hvordan tenker dommeren? (Fjerde og femte ledd)</strong> Dommeren skal ikke gjette. Dommeren skal hente inn barnevernet for en vurdering. Videre sier loven at dommeren bør se på hva den avdøde skrev før de døde (f.eks. i et testamente). Testamentet er ikke bindende, men det veier tungt i vurderingen. Dommeren har stor frihet i dommen:</p>
<ul><li>Retten kan gi barnet til faren.</li><li>Retten kan gi barnet til mormor og morfar sammen.</li><li>Retten kan sette et vilkår: "Far får barnet, men barnet skal bo hos stefar i to år til for å fullføre barneskolen før det flytter til far".</li></ul>
<p>Finner ikke retten noen egnet kandidat blant slekt og venner, overlates problemet til staten. Retten gir da barnevernet beskjed om å plassere barnet i et offentlig fosterhjem (sjuende ledd).</p>""",
        "eksempler": [{"navn": "Saken om onkel og pappa", "tekst": "Maria dør av kreft. Sønnen Tobias (7) har bodd alene hos mor hele livet. Faren, Pål, mistet foreldreansvaret i retten for tre år siden på grunn av rus. Når Maria dør, står Tobias alene. Marias bror (onkel) går til tingretten og ber om foreldreansvaret for Tobias. Pål møter også opp og sier at han nå er rusfri, og vil ha sønnen sin. Retten henter inn rapporter fra barnevernet og ser at Maria i sitt testamente skrev at broren var den tryggeste omsorgspersonen. Siden Pål var fraværende, og Tobias elsker onkelen sin, dømmer retten (etter § 64) foreldreansvaret og det faste bostedet til onkelen. Retten gir imidlertid Pål samværsrett annenhver helg."}],
        "vanlige_feil": ["Slektninger venter 7 måneder etter dødsfallet med å saksøke den gjenlevende forelderen (Fristen i første ledd er absolutt 6 måneder for å angripe det automatiske ansvaret).", "Tro at et testamente sikrer at stefar får beholde barnet (Testamentet er bare rådgivende for dommeren, den biologiske faren står sterkt)."],
        "hva_bor_du_html": """<p>Dersom du som far/mor står uten foreldreansvar og eksen din dør, må du handle umiddelbart. Kontakt retten der barnet bor for å reise sak og krev ansvaret for barnet ditt.</p>
<p>Er du en steforelder eller nær slektning som har hatt den daglige omsorgen før dødsfallet, og du ser at barnets liv vil bli knust hvis det flyttes til en fjern biologisk forelder: Kontakt advokat den uken dødsfallet skjer for å sende en stevning med krav om "førebels avgjerd" (hastevedtak), slik at barnet blir der det er inntil rettssaken er over.</p>""",
        "dumme_sporsmal": [
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "38", "tittel": "hvem som i utgangspunktet fikk ansvaret den dagen døden inntraff", "available": True},
        ],
    },
    {
        "number": "64a",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hva skjer hvis ingen ber om å få et foreldreløst barn?",
        "kategori": "familie",
        "description": "Hvis et barn blir helt foreldreløst, og verken faren eller slekten tar kontakt, har domstolen en plikt til å rydde opp og skaffe barnet en verge av seg selv.",
        "kort_svar": "Fører et dødsfall til at ingen lenger har foreldreansvar for et barn, og ingen slektninger tar kontakt, skal tingretten ta saken i egne hender. Retten må sørge for at saken blir behandlet og barnets fremtid blir avklart.",
        "paragraftekst": """Retten skal av eige tiltak og utan ugrunna opphald handsame sak om foreldreansvaret når den får melding etter arvelova § 89 andre ledd andre punktum om at eit dødsfall fører til at ingen lenger har foreldreansvaret for eit barn.

Den som ønskjer foreldreansvaret, kan vende seg til retten der barnet bur om dette.

Reglane i § 64 gjeld så langt dei høver.""",
        "hva_betyr_html": """<p>Noen barn har bare én forelder, for eksempel hvis far er ukjent. Hvis den eneste forelderen dør i en ulykke, er barnet plutselig foreldreløst i lovens øyne. Ingen har juridisk makt til å bestemme over det, signere skolepapirer eller åpne en bankkonto for livsforsikringen.</p>
<p>Normalt driver ikke domstoler oppsøkende virksomhet (de venter på at noen saksøker hverandre). Men her pålegger loven domstolen å reagere "av eget tiltak".</p>
<p>Når skifteretten (den delen av tingretten som håndterer arv og dødsbo) ser at et dødsfall etterlater et foreldreløst barn, skal domstolen automatisk starte en barnefordelingssak. De venter ikke på en advokat.</p>
<p>Tingretten varsler familien, annonserer ofte behovet, og involverer barnevernet. Enhver som da ønsker å ta ansvar for barnet (en gudmor, en eldre søster, en tante), kan bare ta kontakt med domstolen direkte (andre ledd), og dommeren vil vurdere dem etter reglene i den forrige paragrafen (§ 64).</p>""",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "",
        "dumme_sporsmal": [
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "64", "tittel": "reglene dommeren bruker for å avgjøre hvem som er egnet", "available": True},
            {"lov": "barnelova", "paragraf": "38", "tittel": "hvem som får barnet automatisk (hvis det er aktuelt)", "available": True},
        ],
    },
    {
        "number": "64b",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Midlertidig hastetiltak ved partnerdrap",
        "kategori": "familie",
        "description": "Er en forelder anklaget for å ha drept den andre? Domstolen slår umiddelbart inn og fjerner alle rettigheter og samvær med barnet mens politiet etterforsker.",
        "kort_svar": "Hvis en forelder er siktet eller tiltalt for å ha drept barnets andre forelder med vilje, tar retten en lynrask avgjørelse uten vanlig rettssak. Den siktede fratas foreldreansvaret umiddelbart, og barnet skjermes. Den siktede får verken ha samvær eller bo med barnet så lenge den midlertidige kjennelsen gjelder.",
        "paragraftekst": """Retten skal av eige tiltak og utan ugrunna opphald ta førebels avgjerd om foreldreansvaret når den får melding om at den attlevande er sikta eller tiltala for forsettleg å ha valda den andre forelderen sin død, og den attlevande har eller krev å få foreldreansvaret.

Retten treff avgjerda ved orskurd. Det er ikkje nødvendig med munnleg forhandling på førehand.

Så lenge ei førebels avgjerd om å frata foreldreansvaret gjeld, skal den attlevande ikkje ha samvær eller bu fast saman med barnet.

Reglane i § 64 gjeld så langt dei høver.""",
        "hva_betyr_html": """<p>Dette er en krise-paragraf som kom inn i loven for å hindre absurde situasjoner. Tidligere i historien kunne en far drepe barnets mor, og deretter (fordi de var gift) styre barnets barnehageplass, penger og hvor barnet skulle bo, fra varetektscellen sin, frem til en langvarig rettssak tok fra ham makten mange måneder senere.</p>
<p>Nå skjer følgende: I det øyeblikket politiet sikter faren for forsettlig (villet) drap på moren, går det en alarm til tingretten. Dommeren har en absolutt plikt ("skal av eige tiltak") til å ta en hasteavgjørelse (førebels avgjerd).</p>
<p>Dommeren trenger ikke kalle faren inn til et rettsmøte eller høre hans advokat snakke i timevis (andre ledd). Dommeren skriver ut en kjennelse ("orskurd") som umiddelbart suspenderer farens foreldreansvar og overfører det til noen andre (som regel barnevernet eller familie).</p>
<p>Tredje ledd er knallhardt: Så lenge denne hastedommen gjelder, er døren lukket. Den siktede faren har forbud mot å kreve samværsbesøk i fengselet, og han kan ikke bo med barnet.</p>""",
        "eksempler": [{"navn": "Arresteres for drap", "tekst": "Mor blir funnet drept i hjemmet. Politiet arresterer far samme kveld og sikter ham for drapet. Dagen etter fatter tingretten en midlertidig beslutning (etter § 64 b) om å frata far foreldreansvaret og gi det til barnevernet, som plasserer barna hos mormor. Far har ingen rett til å se barna i varetekten. Om to år, hvis far blir endelig dømt for drapet, vil domstolen omgjøre det midlertidige vedtaket til en permanent dom. (Skulle han bli frikjent, vil han derimot kreve å få ansvaret tilbake)."}],
        "vanlige_feil": [],
        "hva_bor_du_html": "",
        "dumme_sporsmal": [
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "38", "tittel": "hvor det står at partnerdrap stopper den \"automatiske\" overtakelsen av ansvaret", "available": True},
        ],
    },
    {
        "number": "64c",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Avslutte saken etter en midlertidig draps-beslutning",
        "kategori": "familie",
        "description": "Har domstolen fratatt noen foreldreansvaret midlertidig etter et drap, men ingen slektninger har reist en permanent sak? Da må staten fikse det selv.",
        "kort_svar": "Retten har en plikt til å sørge for at barnet får en *permanent* løsning etter at de har tatt en midlertidig avgjørelse (hastevedtak) i en drapssak. Hvis verken barnevernet, faren eller slektninger selv tar initiativ til et permanent søksmål, skal domstolen sette i gang rettssaken av seg selv.",
        "paragraftekst": """Retten skal av eige tiltak og utan ugrunna opphald ta avgjerd om foreldreansvar når det er teke ei førebels avgjerd og ingen har teke ut søksmål etter § 64. Dette gjeld ikkje dersom retten etter § 64 b har tatt avgjerd om at ingen skal ha foreldreansvaret, og gitt melding til den kommunale barnevernstenesta og statsforvaltaren.

Reglane i §§ 64 og 64 b tredje stykket gjeld så langt dei høver.""",
        "hva_betyr_html": """<p>Paragrafen stenger et byråkratisk hull. I forrige paragraf (§ 64 b) lærte vi at dommeren skriver et hastevedtak for å fjerne foreldreansvaret fra en drapssiktet forelder over natten. Men en hastebeslutning ("førebels avgjerd") er nettopp bare midlertidig. Den kan ikke vare evig. Lovsystemet krever en skikkelig, endelig dom.</p>
<p>Vanligvis forventes det at noen (mormor, farbror eller en verge) sender inn en formell stevning for å få den permanente dommen i orden. Men hvis ingen gjør det – kanskje fordi familien er i sjokk, eller de ikke har råd til advokat – sier loven at domstolen må ordne opp ("av eige tiltak"). Dommeren starter da en full sak for å sikre barnet en permanent juridisk løsning.</p>
<p>Unntaket er hvis den midlertidige kjennelsen bare sa: "Ingen får ansvaret, vi overlater det helt til barnevernet". Da har staten tatt over barnet fullt ut i et annet system (barnevernsloven), og da trenger ikke dommeren bruke tid på flere barnelovssaker.</p>""",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "",
        "dumme_sporsmal": [
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "64", "tittel": "reglene for selve den permanente rettssaken", "available": True},
        ],
    },
    {
        "number": "64d",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Kan man kreve å få barnet tilbake etter et dødsfall/drap?",
        "kategori": "familie",
        "description": "Hva skjer hvis en partnerdraps-tiltalt frikjennes i retten? Loven gir dem rett til å reise sak for å få tilbake foreldreansvaret fra fosterhjemmet eller slekten.",
        "kort_svar": "En gjenlevende forelder som har mistet barnet etter et dødsfall eller etter anklager om drap, kan saksøke den som har barnet (for eksempel mormor) for å endre avgjørelsen. Som alltid for å endre en eksisterende dom, krever det at det foreligger \"særlige grunner\" (som at siktelsen ble henlagt eller man ble frifunnet).",
        "paragraftekst": """Den attlevande forelderen kan reise sak for retten med krav om endring av avgjerd etter §§ 64, 64 a og 64 c. Ei avgjerd skal berre endrast dersom særlege grunnar talar for det. Den attlevande forelderen og andre kan på same vilkår reise sak om endring av ei førebels avgjerd etter § 64 b. Sak om endring etter tredje punktum skal reisast for den domstolen som tok den førebelse avgjerda.

Dersom det er openbert at det ikkje ligg føre særlege grunnar, kan retten avgjere saka utan hovudforhandling.""",
        "hva_betyr_html": """<p>Når domstolen dømmer foreldreansvaret til mormor fordi pappaen var siktet for drapet på mammaen, slår dommeren fast hverdagen til barnet. Men i strafferetten er man uskyldig til det motsatte er bevist.</p>
<p>Kanskje politiet etterforsket saken i ett år, og så konkluderte de med at moren døde i en tragisk fallulykke i trappen, og ikke ble dyttet. Siktelsen mot pappaen henlegges. Da står han igjen som uskyldig, men uten barnet sitt.</p>
<p>Paragraf 64 d gir ham rett til å saksøke mormoren (eller barnevernet) for å få omgjort (endret) den gamle dommen og kreve foreldreansvaret tilbake.</p>
<p>Men igjen møter vi muren i familieretten: <strong>"Særlege grunnar"</strong>. Barnet har kanskje bodd to år hos mormor og har slått rot der. Pappaen vinner ikke automatisk bare fordi han er frikjent for drapet. Dommeren vil vurdere frifinnelsen som en særlig grunn for å <em>åpne</em> saken, men vil deretter gjøre en streng vurdering av "barnets beste" (§ 48) før de river barnet ut av sitt nye hjem og gir det tilbake til ham.</p>
<p>Som i § 63 gjelder regelen om at hvis mannen åpenbart ikke har noen ny, god grunn til å mase på domstolen, vil dommeren avvise saken i posten ("utan hovudforhandling") for å skjerme barnet fra unødvendige rettssaker.</p>""",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "",
        "dumme_sporsmal": [
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "63", "tittel": "den generelle regelen for å endre gamle dommer", "available": True},
        ],
    },
    {
        "number": "65",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hva skjer når en forelder bryter samværsavtalen og saboterer?",
        "kategori": "familie",
        "description": "Nekter eksen å utlevere barnet til samvær? I Norge henter vi ikke barn med politi, men namsmannen kan knuse sabotøren økonomisk med daglige tvangsbøter.",
        "kort_svar": "Når noen saboterer en rettskraftig dom eller avtale om barnets bosted eller samvær, kan man kreve tvangsfullbyrdelse i tingretten. Nekter mor å levere til samvær, fastsetter dommeren tvangsbøter som løper hver dag barnet holdes tilbake. Kun når barnet skal flyttes for godt til sin faste bostedsadresse, kan man i ytterste konsekvens bruke makt for å hente barnet. Tvang skal ikke brukes hvis det utsetter barnet for fare, eller hvis et modent barn setter seg sterkt imot det.",
        "paragraftekst": """For tvangsfullføring av avgjerd om og anna særleg tvangsgrunnlag for foreldreansvaret, kvar barnet skal bu fast, og samværsrett gjeld tvangsfullbyrdelsesloven kapittel 13, likevel slik at § 13-8 femte ledd ikkje gjeld. Vedtak av statsforvaltaren om tvangskraft for avtaler etter § 55 er særleg tvangsgrunnlag. Førebels avgjerd etter § 60 er tvangskraftig sjølv om avgjerda ikkje er rettskraftig.

Avgjerd eller avtale med tvangskraft om foreldreansvar og kvar barnet skal bu fast, kan tvangsfullførast ved henting eller tvangsbot. Avgjerd eller avtale med tvangskraft om samværsrett kan berre tvangsfullførast ved tvangsbot. Tingretten kan fastsetje ei ståande tvangsbot som for ei viss tid skal gjelde for kvar gong samværsretten ikkje vert respektert. Eit krav om tvangsfullføring skal setjast fram for tingretten i distriktet der saksøkte har sitt alminnelege verneting. Reglane i § 15 andre leddet gjeld tilsvarande.

Det skal ikkje fastsetjast tvangsbot dersom oppfylling av samværsretten er umogleg, til dømes der det er risiko for at barnet blir utsett for vald eller på anna vis handsama slik at den fysiske eller psykiske helsa blir utsett for skade eller fare. Det same gjeld ved tvangsfullføring av foreldreansvar og kvar barnet skal bu fast.

Barnet skal få høve til å seie meininga si før det blir teke avgjerd. Meininga til barnet skal bli vektlagt etter alder og modning. Tvangsfullføring skal ikkje skje mot barnet sin vilje, med mindre retten kjem til at det er naudsynt av omsyn til barnet.

For å leggje til rette for gjennomføring av fastsett samvær kan retten gjere praktiske endringar i avgjerda der det er formålstenleg, til dømes å endre tida for henting og levering.

Innkrevjingsmyndigheita krev inn tvangsbota. Innkrevjing skal berre skje når den som har retten, ber om det. Bota går til statskassa. Bota skal ikkje krevjast inn for meir enn åtte veker om gongen. Lar den som har retten etter lova det gå lenger tid med inndrivinga, lauper inga vidare bot før den bota som allereie er forfallen til betaling, er betalt eller det er tatt utlegg for den.""",
        "hva_betyr_html": """<p>Paragraf 65 er straffesystemet i familieretten. Den trer i kraft når en dommer har sagt "far skal ha annenhver helg", og mor bare låser døren og drar for gardinene når han kommer for å hente.</p>
<p>Det viktigste skillet i loven er hva slags tvang som er lov:</p>
<p><strong>1. Brudd på samvær \\= Pengebøter (mulkt)</strong> I Norge henter man <em>aldri</em> barn med makt for en vanlig samværshelg. Å la politiet bære et skrikende barn ut i en bil for en helg, er ansett som et overgrep mot barnet. I stedet straffer staten bostedsforelderen på lommeboken. Faren sender en klage (en tvangsbegjæring) til tingretten. Dommeren skriver en kjennelse: "Hver dag samværet nektes fra nå av, får mor 2 000 kroner i bot". Dette kalles "ståande tvangsbot". Pengene går ikke til far, de går til statskassen (Innkrevingen styres av Statens innkrevingssentral). Å ruinere sabotøren er statens metode for å presse frem samarbeid.</p>
<p><strong>2. Fast bosted \\= Kan hentes med makt</strong> Dersom en dommer har bestemt at barnet skal flytte permanent (bo fast) hos far, men mor nekter å levere barnet fra seg, stiller saken seg annerledes. Siden dette gjelder barnets permanente hjem, tillater loven "henting" ved namsmannens og politiets hjelp i ytterste konsekvens, selv om bøter oftest prøves først.</p>
<p><strong>Når slipper sabotøren straff? (Tredje og fjerde ledd)</strong> Det finnes to "lovlige" grunner til å holde igjen et barn:</p>
<ul><li><strong>Umulighet (Fare):</strong> Mor kan ikke bøtelegges hvis hun kan bevise for dommeren at samværet vil skade barnet. Eksempel: Far møtte opp ruset, eller far utøvde vold fredagen før. Da er oppfyllelsen ansett som umulig og farlig.</li><li><strong>Barnets vilje:</strong> Retten hører på barnet. Nekter en 13-åring å reise til far, uansett hva mor sier, vil dommeren avvise farens krav om å bøtelegge mor. Tvang skal ikke brukes mot eldre barns egen frie vilje.</li></ul>
<p>Til slutt: Den som samværet holdes unna for (for eksempel far), må selv aktivt be Statens Innkrevingssentral om å faktisk inndrive bøtene. Gjør han ikke det, stopper inndrivingen etter 8 uker for å hindre at regningen vokser i all uendelighet uten at problemet løses i bunn.</p>""",
        "eksempler": [{"navn": "Stående tvangsbot", "tekst": "Lars har en fersk dom fra lagmannsretten som sier at han skal ha datteren (6) onsdag til søndag annenhver uke. Ekskona Hanne hater avgjørelsen og lyver på seg at datteren har omgangssyke tre ganger på rad. Lars sender en \"begjæring om tvangsfullbyrdelse\" til tingretten. Dommeren kaller dem inn. Hanne hevder barnet er sykt, men har ingen legeerklæring. Dommeren setter en stående tvangsbot: \"For hver dag Lars' samvær ikke respekteres fremover, skal Hanne betale 1 500 kr til staten\". Neste onsdag leverer Hanne barnet punktlig, fordi hun vet at namsmannen vil trekke 7 500 kr rett fra lønnskontoen hennes den helgen."}],
        "vanlige_feil": ["En far som krever politiets hjelp til å slå inn døren en fredagskveld for å få helgesamværet sitt. (Politiet har ingen myndighet til dette. Klagen må sendes tingretten på dagtid).", "Tro at en \"privat\" samværsavtale uten stempel fra Statsforvalteren kan gi bøter. (Tvangsfullføring krever at avtalen har tvangskraft etter § 55 eller dom).", "Bostedsforelderen holder igjen barnet fordi \"pappa sliter på jobben og virker stresset\". Dette holder ikke som bevis for \"fare\" — og bøtene vil hagle."],
        "hva_bor_du_html": """<p><strong>For deg som blir sabotert:</strong> Før logg. Send SMS hver fredag kl. 16.00: "Jeg står utenfor, er dere der?". Lagre svarene. Kontakt advokat som sender begjæring til domstolen.</p>
<p><strong>For deg som nekter levering:</strong> Du må ha dokumentasjon. Har barnet fortalt om overgrep hos faren, må du kontakte barnevern eller politi umiddelbart slik at etterforskningen kan legges frem for namsmannen som bevis for at det foreligger en risiko (tredje ledd), slik at du slipper bøter.</p>""",
        "dumme_sporsmal": [
            {"q": "Får jeg pengene fra bøtene siden samværet mitt ble ødelagt?", "a": "Nei. Det sjette leddet er krystallklart: \"Bota går til statskassa\". Tvangsbøter er ikke erstatning for din tapte tid, det er statens ris bak speilet for å gjenopprette lov og orden i rettssystemet. Vil du ha erstatning for ubrukte flybilletter, må du saksøke henne sivilt i en helt annen sak."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "55", "tittel": "hvordan en privat avtale kan få det magiske \"tvangskraft\"-stempelet", "available": True},
        ],
    },
    {
        "number": "65a",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Mekler og sakkyndig brukes før tvangsbøtene ilegges",
        "kategori": "familie",
        "description": "Dommeren slenger sjelden ut tvangsbøter på første dag i retten. Før straffen settes inn, sender retten ofte en psykolog hjem til dere for å løse knuten frivillig.",
        "kort_svar": "Når noen krever tvangsbøter for brudd på samvær, kan retten stanse prosessen og heller sende inn en psykolog, sakkyndig eller familieterapeut for å snakke med foreldrene. Målet er å forsøke å løse saboteringen frivillig før de økonomiske straffene settes i verk.",
        "paragraftekst": """Før retten tek avgjerd om tvangsfullføring, kan den oppnemne ein sakkunnig, godkjend meklar eller ein annan tilsett ved familieverntenesta for å mekle eller ha samtalar med foreldra. Føremålet med meklinga eller samtalane er å få foreldra til å oppfylle pliktane sine frivillig. Retten kan fastsetje eit mandat for utføring av oppdraget.

Retten skal setje ein frist for utføringa av oppdraget, normalt ikkje lenger enn to veker etter oppnemninga. Fristen kan forlengjast om retten meiner ei frivillig løysing mellom foreldra er mogeleg om meklinga eller samtalane held fram.

Den som har fått oppdrag etter første leddet, skal innan fristen levere ei utgreiing med opplysningar om kva for tiltak som er sette i verk mv. Opplysningar om andre vesentlege omstende for saka skal gå fram av utgreiinga.

I saker om tvangsfullføring gjeld § 61 første leddet nr. 3 tilsvarande.""",
        "hva_betyr_html": """<p>Straff løser sjelden de underliggende problemene i en splittet familie. Hvis mor bøtelegges med 2 000 kr dagen (etter § 65), kan hatet hennes mot far bare vokse, og hun snakker kanskje stygt om far til barna sine for å straffe ham psykologisk.</p>
<p>For å unngå dette, er domstolene pålagt (og oppfordret til) å bruke § 65 a. Før dommeren starter "bøtemaskinen", trykker de på pause. Dommeren sier til mor og far: "Ok, jeg ser at du saboterer, mor. Men før jeg gjør deg personlig konkurs, sender jeg hjem en erfaren barnepsykolog (sakkyndig) for å snakke med dere i to uker".</p>
<p>Psykologen vil da sette seg ned og spørre: "Hvorfor nekter du å levere? Hva er det som skjer under hentingen?". Kanskje det bare handler om at mor ikke tåler synet av fars nye kjæreste som alltid sitter i bilen. Psykologen vil da forsøke å mekle frem en mikroløsning — "Ok, far henter på skolen i stedet for på døren til mor." Går mor med på det, løses knuten frivillig, og dommeren slipper å bruke tvangsmulkt.</p>
<p>Terapeutens oppdrag er raskt. Fristen er på "normalt to veker", slik at samværsforelderen (som har ventet på barna sine i ukesvis) ikke skal måtte vente enda lenger på rettferdighet hvis terapeuten ikke kommer noen vei. Viser utredningen at mor fremdeles er totalt vrangvillig, starter dommeren tvangsbøtene etter at de to ukene er over.</p>""",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "",
        "dumme_sporsmal": [
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "65", "tittel": "reglene for selve tvangsbøtene (straffen)", "available": True},
            {"lov": "barnelova", "paragraf": "61", "tittel": "hvordan sakkyndige vanligvis brukes under rettssakene", "available": True},
        ],
    },
    {
        "number": "66",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Grunnregelen for barnebidrag: Du har plikt til å forsørge barnet",
        "kategori": "familie",
        "description": "Hvem betaler for at et barn eksisterer i Norge? Det er foreldrene. Loven sier at du har plikt til å forsørge barnet ditt etter hvor mye du evner å tjene.",
        "kort_svar": "Begge foreldre har en ufravikelig plikt til å bære kostnadene for å forsørge og utdanne barnet sitt. Hvor mye hver av dere må betale, deles innbyrdes basert på hvor mye dere tjener. Tjener du mest, betaler du mesteparten av regningen.",
        "paragraftekst": """Foreldra skal bere utgiftene til forsyting og til utdanning av barnet etter evne og givnad og etter dei økonomiske kåra til foreldra, når barnet sjølv ikkje har midlar til det. Innbyrdes har begge foreldre skyldnad til å skyte til det som trengst etter evne.

Reglane om fostringsplikt for foreldra etter dette kapitlet gjeld tilsvarande for andre som har fått foreldreansvaret etter at begge foreldra er døde.""",
        "hva_betyr_html": """<p>Dette er bærebjelken for alt som handler om barnebidrag ("fostringsplikt") i Norge. Det betyr i praksis to ting:</p>
<p>1. <strong>Staten betaler ikke for barnet, DU gjør det.</strong> Det er du og den andre forelderen som har satt barnet til verden. Dere har ansvaret for mat, klær, husleie, strøm, SFO og utstyr. Hvis barnet har egen formue (for eksempel en stor arv og penger på konto), skal først og fremst foreldrene betale for utgiftene, "når barnet sjølv ikkje har midlar til det", noe de aller færreste barn har.</p>
<p>2. <strong>Delt etter evne.</strong> Barneoppdragelse er et spleiselag. Loven sier "etter evne". Det betyr at staten beregner hva et gjennomsnittsbarn koster i måneden (for eksempel 8 000 kr). Er foreldrene millionærer, koster kanskje barnet mer ("etter dei økonomiske kåra"). Men andelen dere betaler, splittes etter inntekt. Tjener far tre ganger så mye som mor, skal han brødfø tre fjerdedeler av barnets totale kostnad, mens mor betaler en fjerdedel.</p>
<p>Denne skyldnaden til å forsørge barnet forsvinner aldri (frem til de er 18, eller ferdig på skole). Den gjelder enten dere er gift, samboere, eller du bare betaler barnebidrag fordi barnet bor hos den andre. Selv om du mangler foreldreansvar og aldri har sett barnet ditt, har du nøyaktig like stor økonomisk "skyldnad".</p>
<p>Det andre leddet sikrer at hvis begge foreldrene dør, og tante tar over foreldreansvaret i en rettssak (etter § 64), så overtar tante også denne underholdsplikten. Hun må brødfø barnet, men får da tilgang til barnets arv, trygd og stønader for å klare det.</p>""",
        "eksempler": [{"navn": "Den rike og den fattige", "tekst": "Sofie er student og jobber deltid. Hun tjener 200 000 kr i året. Pappaen til barnet, Lars, er toppleder og tjener 1,8 millioner kr i året. Lars klager over at han betaler \"alt\" for barnet og krever at Sofie spytter inn 50 % av kostnadene på barnehage og klær. Han tar feil. Barnelova § 66 slår fast at de skal \"skyte til det som trengst etter evne\". Siden Lars har en voldsom evne, og Sofie en ekstremt lav evne, blir den lovmessige fordelingen at Lars betaler nesten hele gildet, enten han liker det eller ikke."}],
        "vanlige_feil": ["En forelder krever at utgiftene til barnet alltid skal deles på midten, 50/50, selv om de har ulik inntekt. (Du deler etter evne/brøk, ikke 50/50, hvis den ene krever NAV-fastsettelse).", "Tro at man kan si fra seg farskapet fordi man ikke har råd til barnebidrag. (Fostringsplikt kan aldri velges bort med en avtale).", "Barnefaren betaler ingenting med argumentet: \"Sønnen fikk jo nettopp 500 000 kr på konto i arv etter farfar\". Barnets egne penger skal i hovedsak ikke spises opp til hverdagsmat så lenge foreldrene har lønn."],
        "hva_bor_du_html": "",
        "dumme_sporsmal": [
            {"q": "Fritar delt fast bosted (50/50) meg for underholdsplikten/barnebidrag?", "a": "Dette er kanskje den vanligste myten i Norge. Mange kjemper for 50/50 for å \"slippe bidrag\". Men plikten i § 66 gjelder uavhengig av hvor barnet sover. Har du barnet nøyaktig halvparten av tiden, betaler du for maten og klærne i ditt hjem (din halvpart). MEN: Hvis du tjener en million i året, og mor tjener 300 000, er din *evne* (din andel av ansvaret for at barnet har et godt liv) fremdeles mye større enn hennes. Da sier reglene i NAV at du fremdeles skal betale et barnebidrag over til henne, slik at barnet har tilnærmet lik levestandard i begge de to hjemmene. Det blir riktignok lavere enn ved vanlig samvær, men du slipper ikke unna."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "67", "tittel": "selve regelen om pengetilskuddet (barnebidraget) over til den andre", "available": True},
            {"lov": "barnelova", "paragraf": "68", "tittel": "fristen: dette varer til de er 18 eller ferdig på videregående", "available": True},
        ],
    },
    {
        "number": "67",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Barnebidraget i praksis (og særtilskudd for regulering og konfirmasjon)",
        "kategori": "familie",
        "description": "Bor ikke barnet hos deg? Da krever loven at du sender et fast pengebeløp (barnebidrag) hver måned. Du kan også bli pålagt å dele regningen for konfirmasjon.",
        "kort_svar": "Hvis barnet ikke bor sammen med deg, skal du betale et fast barnebidrag (fostringstilskot) hver måned. Du kan ikke fraskrive deg denne plikten, og barnet har rett på pengene. I tillegg kan du pålegges å betale engangssummer (særtilskudd) for ekstraordinære utgifter som tannregulering, konfirmasjon eller briller.",
        "paragraftekst": """Der ein eller begge foreldra ikkje bur saman med barnet, skal vedkomande betale faste pengetilskot til forsyting og utdanning. Også foreldre som bur saman med barnet, kan påleggjast å yte pengetilskot når dei forsømer fostringsplikta si etter § 66. Ingen kan gje avkall på den retten barnet har etter dette stykket.

Til særlege utlegg så lenge underhaldsplikta varer, kan foreldra påleggjast å yte særtilskot. Det er eit vilkår at utlegga er rimelege og naudsynte og ikkje går inn under dei utgiftene som det løpande fostringstilskotet skal dekke. Krav om særtilskot må setjast fram innan eit år etter at dei særlege utlegga kom på. Departementet kan ved forskrift gje utfyllande reglar om særtilskot.

Det er barnet som har rett til tilskotet. Når ikkje noko anna er fastsett, skal det betalast på forskot for kvar månad til den barnet bur saman med fast. Tilskotet skal betalast frå og med den kalendermånaden kravet oppstår og ut den kalendermånaden vilkåra for tilskot fell bort.""",
        "hva_betyr_html": """<p>Paragraf 67 gjør oppfostringsplikten i forrige paragraf om til kalde, harde penger. Loven kaller det "fostringstilskot" og "pengetilskot", men på vanlig norsk snakker vi om <strong>barnebidrag</strong>.</p>
<p><strong>Barnebidraget (første ledd)</strong> Bor barnet fast hos mor, må far kompensere ved å sende penger over til mor for å dekke husleie, strøm og mat. Loven er nådeløs mot de som prøver å snike seg unna. Det står at "Ingen kan gje avkall på den retten barnet har". Hvis mor signerer en "vanntett" skriftlig avtale med far der hun sier: "Jeg vil ikke ha pengene dine, la meg bare være i fred, så slipper du barnebidrag", er avtalen ulovlig og ugyldig. Det er <em>barnets</em> penger. Mor har ikke lov til å gi dem bort på barnets vegne, og staten kan kreve bidraget inn uansett.</p>
<p>Enda mer ekstremt: Bor mor, far og barn under samme tak, og mor er en luksusfelle-deltaker som sløser bort all lønnen sin på kasino i stedet for å kjøpe klær til barnet (hun forsømmer fostringsplikten i § 66), kan staten ilegge henne et formelt barnebidrag. Deler av lønnen hennes trekkes da direkte og gis til far, selv om de er gift og bor sammen!</p>
<p><strong>Særtilskudd (andre ledd)</strong> Det faste månedlige barnebidraget skal dekke vanlige ting som klær og mat. Men plutselig får barnet behov for tannregulering til 30 000 kroner, briller til 5 000 kroner, eller en konfirmasjon til 20 000 kroner. Slike ting kalles "særlige utlegg" og faller utenfor det vanlige bidraget. Paragraf 67 sier at du (selv om du betaler vanlig bidrag) kan pålegges av NAV å betale "særtilskudd". Regningen for brillene deles da på dere to etter inntekt (samme brøk som alltid). Men her er det en knallhard frist: Mor må fremme kravet om særtilskudd <strong>innen ett år</strong> etter at utgiften oppsto. Kommer hun viftende med kvitteringer for fotballcuper fra 2021 i 2025, har kravet forfalt (foreldet), og du slipper å betale. Det må også være utgifter som var "rimelige og nødvendige". Et konfirmasjonsselskap er nødvendig. Et luksuscruise i gave til konfirmanten er ikke det.</p>
<p><strong>Betalingen (tredje ledd)</strong> Loven krever forutsigbarhet. Barnebidraget skal stå på kontoen <em>på forskudd</em> hver måned. Bor barnet hos mor, er det mor som fysisk mottar pengene (siden barnet er under 18 og ikke kan styre egen konto).</p>""",
        "eksempler": [{"navn": "Brillesmellen", "tekst": "Lars betaler 3 000 kr i barnebidrag til Mia hver måned. En onsdag ringer Mia og sier at datteren (12) trenger spesialbriller for å kunne se tavlen på skolen. Brillene koster 8 000 kr totalt. Mia kjøper dem, sender kvitteringen til Lars og ber om 4 000 kr (Lars og Mia tjener nøyaktig like mye). Lars nekter og sier at barnebidraget hans skal dekke slike ting. Mia sender krav til NAV. NAV ser i § 67 at briller er en uventet, spesifikk engangsutgift (særtilskudd). NAV fatter vedtak og tvinger Lars til å betale de 4 000 kronene til Mia, utenom det vanlige barnebidraget."}],
        "vanlige_feil": ["Mor og far lager privat avtale om at far sier fra seg samvær, mot at mor \"sletter gjelden\" hans og aldri krever barnebidrag. (Ulovlig, barnets rett til forsørgelse kan ikke brukes som byttemiddel).", "Spare på kvitteringer for konfirmasjon, briller og bunad i skuffen, for så å kreve eksen for alt samtidig tre år senere. (Fristen er ETT ÅR fra betalingsdato. Du taper alt).", "Kreve særtilskudd fordi man kjøpte barnet en 12 000-kroners Canada Goose-jakke. (Kravet om \"nødvendig og rimelig\" stopper luksus)."],
        "hva_bor_du_html": """<p>Har du fått en kjempe-regning for noe ekstraordinært (regulerings-tannlege er det klassiske eksempelet)? Ikke vent. Send en hyggelig melding med et bilde av kvitteringen, og be om at det deles etter brøk. Nekter vedkommende, sender du umiddelbart skjema for "krav om særtilskudd" til NAV. Alt foregår digitalt.</p>
<p>For løpende barnebidrag oppfordrer staten foreldrene til å lage "private avtaler" om hvor mye som skal sendes i måneden, fordi NAV tar høye gebyrer hvis de må blandes inn (se § 70). Bruk NAVs bidragskalkulator på nett, skriv ut beløpet, og lag faste trekk i nettbanken.</p>""",
        "dumme_sporsmal": [
            {"q": "Får jeg slettet barnebidraget for juli fordi jeg har barnet i tre uker i sommerferien da?", "a": "Nei. Barnebidraget du betaler til mor (hvis hun har fast bosted), er fordelt og slettet ut over alle årets 12 måneder (inkludert fradragene for at du har barnet i helger og ferier). Du skal betale den samme summen i juli som i november, med mindre dere (utenom NAV) har skrevet en privat avtale der dere spesifiserer en betalingsfri sommer-måned. Betaler du via NAV Innkreving, trekker de blankt 12 måneder i året."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "70", "tittel": "hvordan dere beregner den private avtalen (og NAVs innblanding)", "available": True},
            {"lov": "barnelova", "paragraf": "68", "tittel": "når dette marerittet av fakturaer endelig slutter", "available": True},
        ],
    },
    {
        "number": "68",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvor lenge må du betale barnebidrag? (Skolegang etter 18 år)",
        "kategori": "familie",
        "description": "Barnebidraget stopper vel når ungen blir myndig på 18-årsdagen? Feil. Går barnet fremdeles på videregående skole, må du fortsette å betale til skolen er ferdig.",
        "kort_svar": "Som hovedregel stopper barnebidraget den måneden barnet fyller 18 år. Men hvis barnet fortsatt går på normal videregående skole (VGS) når det er 18, har barnet krav på bidrag helt til utdanningen er fullført. Dette gjelder også annen videreutdanning hvis det vurderes som \"rimelig\".",
        "paragraftekst": """Skyldnaden til foreldra etter §§ 66 og 67 varer til barnet er 18 år når ikkje anna er avtala eller fastsett etter paragrafen her.

Vil barnet etter fylte 18 år halde fram med slik skulegang som må reknast som vanleg, har det krav på pengetilskot for den tid skulegangen varer ved. Det skal fastsetjast ei tidgrense for krav på tilskot etter denne regelen.

Foreldra kan også påleggjast å yte tilskot til anna vidareutdanning dersom det er rimeleg etter interessene og givnaden til barnet, høvet til å skaffe seg midlar til vidareutdanninga på anna vis og tilhøva elles. Det skal fastsetjast ei tidgrense for krav på slike tilskot.""",
        "hva_betyr_html": """<p>En seiglivet myte i Norge er at dagen man kjøper marsipankake med tallet 18, kan man logge inn i nettbanken og slette barnebidraget for godt.</p>
<p>Det stemmer at hovedregelen er 18 år. De vanlige "barnereglene" faller da bort. Men loven vet at nesten ingen i Norge er økonomisk uavhengige på 18-årsdagen. De fleste går i andre eller tredje klasse på videregående skole, og bor hjemme på pikerommet.</p>
<p>Derfor strekker paragraf 68 ut forsørgerplikten. "Slik skulegang som må reknast som vanleg" betyr vanlig videregående skole. Barnet (nå ungdommen) har da et rettslig krav på at du og eksen din fortsetter å forsørge hen til russetiden er over.</p>
<p>Et viktig poeng: Siden ungdommen nå er voksen og myndig (18 år), skal ikke pengene lenger sendes til <em>mor eller far</em>. Kravet eies av ungdommen. Barnebidraget skal sendes direkte til 18-åringens egen bankkonto, med mindre ungdommen bor hjemme hos mor og inngår avtale om at pengene betales dit i stedet som "husleie/kost og losji".</p>
<p>For å unngå at du må betale for en "evighetsstudent" som stryker hvert år og går om igjen og om igjen, sier loven at NAV skal sette en sluttdato (en "tidgrense") i vedtaket, for eksempel "Ut juni 2026, da skolen normalt avsluttes".</p>
<p>Det tredje leddet gjelder høyskoler, fagskoler og universitet. Du er <em>normalt</em> ikke forpliktet til å betale bidrag for en datter som studerer medisin i Bergen, for hun kan (og bør) ta opp studielån fra Lånekassen (skaffe midler på annet vis). Men unntak gjøres noen ganger hvis Lånekassen ikke dekker nok, og foreldrene tjener svært mye, og barnets evner tilsier at utdanningen er spesielt viktig.</p>""",
        "eksempler": [{"navn": "Russen krever bidrag", "tekst": "Tobias bor hos mor og går i tredjeklasse på VGS. I mars fyller han 18 år. Hans far, Geir, ringer NAV og sier at de kan stoppe lønnstrekket fordi sønnen er myndig. Tobias er pengelens og vet at han trenger mat før eksamen. Tobias sender et eget skjema til NAV der han krever \"barnebidrag etter fylte 18 år\" under utdanning, henvist til § 68. NAV vurderer Tobias sin egen inntekt (ingen deltidsjobb), og fastsetter at far og mor skal betale et månedlig beløp direkte inn på Tobias sin brukskonto frem til skoleåret avsluttes tre måneder senere i juni."}],
        "vanlige_feil": ["Pappa stanser overføringene på 18-årsdagen uten å sjekke barnets status, og får en inkasso-smell fra NAV seks måneder senere med krav om etterbetaling.", "Mor (bostedsforelder) krever å fortsatt få bidraget for en 18-åring. (Saken er nå mellom ungdommen og far. Ungdommen må kreve det selv).", "Kreve barnebidrag for et friår/folkehøyskole (som regel ikke ansett som \"vanlig skulegang\")."],
        "hva_bor_du_html": "<p>Når barnet er 17 og et halvt år, sett dere ned med barnet og lag en \"voksenavtale\". Spør om de trenger at du fortsetter bidraget frem til skoleslutt. Du kan inngå en privat avtale med ungdommen direkte: \"Jeg betaler deg 3 000 kr i måneden til juni neste år, så lenge du faktisk går på skolen og ikke dropper ut.\" Dere unngår da gebyrer hos NAV, og du holder styringen på økonomien din.</p>",
        "dumme_sporsmal": [
            {"q": "Betaler jeg dette direkte til barnet, eller kan hun bo hos mamma og jeg sender pengene til mamma slik at de kan brukes til felles middagsmat?", "a": "Dette er fritt for dere å avtale privat. Det enkleste og mest populære for 18-åringer i VGS, er at dere skriver en privat avtale hvor ungdommen aksepterer at ditt bidrag sendes direkte til moren (der hen bor) som et bidrag til husleie og mat i hverdagen. NAV kan også bestemme det."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "67", "tittel": "selve systemet med barnebidrag og engangsbeløp", "available": True},
        ],
    },
    {
        "number": "69",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Barnevern og fostringstilskudd",
        "kategori": "familie",
        "description": "Hva skjer med barnebidraget hvis barnevernet overtar omsorgen for barnet ditt? Barneloven gir slipp, og du betaler i stedet \"oppfostringsbidrag\" til staten.",
        "kort_svar": "Når et barn blir plassert i fosterhjem eller på institusjon av barnevernet, faller den vanlige ordningen for barnebidrag bort. Fra den dagen skal du betale etter reglene i barnevernsloven. Du må fortsatt betale for barnet ditt, men pengene går da til staten/kommunen i stedet for til den andre forelderen.",
        "paragraftekst": "Fostringstilskot som er fastsette etter lova her fell bort frå det tidspunktet tilskot kan fastsetjast etter barnevernsloven § 15-12 første ledd.",
        "hva_betyr_html": """<p>Dette er en ren "trafikkregel" mellom to store lovbøker.</p>
<p>Hvis pappa har barnet boende hos seg, betaler mamma barnebidrag til pappa (etter § 67). Men hvis barnevernet en dag banker på døren og mener at pappa ikke kan ha omsorgen, og plasserer barnet i et fosterhjem hos en fremmed familie, sier loven stopp.</p>
<p>I det øyeblikket barnet tas under offentlig omsorg (etter barnevernsloven), kutter staten det private pengebåndet. Mamma slutter å betale bidrag til pappa. Pappa mister barnetreadyttelsen. I stedet vil kommunen/barnevernet nå regne ut hva både pappa og mamma må betale inn til barnevernet for å "sponse" fosterhjemmet, for plikten til å brødfø barnet ditt (se § 66) forsvinner ikke selv om staten bytter bleiene.</p>""",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "",
        "dumme_sporsmal": [
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "67", "tittel": "reglene som styrer barnebidrag mellom foreldre i vanlige saker", "available": True},
        ],
    },
    {
        "number": "70",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvordan fastsettes barnebidraget, og når tar NAV gebyr?",
        "kategori": "familie",
        "description": "Foreldre bør avtale barnebidrag privat. Blir dere ikke enige, eller dere vil ha NAVs hjelp til å regne ut og kreve inn pengene, tar NAV et gebyr for jobben.",
        "kort_svar": "Foreldre står helt fritt til å avtale hvor stort barnebidraget skal være på egenhånd. Blir dere ikke enige, eller nekter den andre å betale det dere avtalte, kan dere koble inn NAV (tilskotsfuten). For at NAV skal gjøre jobben, må man betale et statlig gebyr (1 278 kr pr 2024 per part). Noen få saker må avgjøres i domstolen.",
        "paragraftekst": """Foreldra kan gjere avtale om fostringstilskot til barnet.

Dersom dei ikkje vert samde, kan kvar av dei krevje at tilskotsfuten tek avgjerd om tilskotet. Dette kan dei gjere jamvel om dei opphavleg har gjort avtale om tilskotet, men slik at løpande tilskot berre skal endrast dersom reglane i lova vil medføre ei endring på meir enn 12 prosent. Departementet kan gje forskrift om gebyr der tilskotsfuten tek avgjerd om fastsetjing og endring av fostringstilskot.

Spørsmålet skal likevel avgjerast av domstolane
a. når nokon av foreldra bed om at det vert gjort i samband med ekteskapssak eller rettssak om foreldreansvar, om kven barnet skal bu saman med eller om samværsrett,
b. når tilskotsfuten viser partane til domstolane, fordi det er meir tenleg etter den karakter saka har.

Når det gjeld tilskot etter § 68 andre og tredje stykket til barn som har fylt 18 år, er det barnet sjølv som gjer avtale eller er part i saka.

Dersom foreldra ikkje lever saman når barnet vert født, og dei ikkje har gjort avtale om tilskotet, skal tilskotsfuten av eige tiltak fastsetje fostringstilskot til barnet.

Får den tilskotspliktige forsytartillegg frå Forsvaret i samband med avtening av førstegangsteneste eller sivilteneste, eller har rett til anna yting frå det offentlege der barnetillegg er ein del av stønaden, kan tilskotsfuten av eige tiltak fastsetje fostringstilskot til barnet for den tida slikt tillegg vert utbetalt.

Foreldra har plikt til å opplyse det organet som skal handsame fastsetjinga av tilskotet, om kva arbeid, utdanning, inntekt og formue dei har, og elles om alt anna som kan ha noko å seie for fastsetjinga av fostringstilskotet. For å fastsetje tilskotet kan organet utan omsyn til teieplikta krevje dei opplysningane som trengst frå arbeidsgjevarar, likningsstell, arbeids- og velferdsetaten og forsikringsselskap, bankar og andre som forvarer eller forvaltar formueverdiar. For å fastsetje tilskot etter at barnet har fylt 18 år, kan organet utan omsyn til teieplikta krevje opplysningar frå utdanningsinstitusjonar om skulegangen er i gang, held fram eller er avslutta og om fagleg progresjon.""",
        "hva_betyr_html": """<p>Paragrafen forklarer "kundereisen" i det norske bidragssystemet.</p>
<p><strong>Steg 1: Privat avtale (gratis)</strong> Staten ønsker at dere ordner opp selv. Dere kan sette dere ned, bruke NAVs utmerkede bidragskalkulator på nett, skrive ut tallet, signere, og overføre pengene hver måned den 1. i måneden. Det er gratis, lovlig og fleksibelt.</p>
<p><strong>Steg 2: NAV griper inn (mot betaling)</strong> Klarer dere ikke å bli enige? Eksen mener han skal betale 1 000 kroner, du mener 4 000 kroner? Da trer andre ledd inn. Enhver av dere kan kreve at NAV ("tilskotsfuten") regner ut et formelt, bindende vedtak. Staten tar seg betalt for dette med et <em>gebyr</em> (tilsvarer ett rettsgebyr pr forelder).</p>
<p>Men loven har en "plageskjerming": Hvis dere <em>har</em> en fungerende avtale, og du plutselig blir sur på ham fordi han fikk ny, fin bil, kan du ikke be NAV lage nytt vedtak bare for å skvise ut hundre kroner ekstra. NAV sjekker systemet sitt og sier: Vil det nye beløpet endre bidraget med <strong>mer enn 12 %</strong> (opp eller ned)? Hvis det bare endres med 5 %, avviser NAV søknaden og beholder den gamle avtalen. (Det kreves at den som krever endring også betaler gebyret, og hvis det blir avvist kan det være tapte penger).</p>
<p><strong>Barnet over 18 år</strong> Som vi husker fra § 68: Når barnet går på videregående, dytter loven deg (bostedsforelderen) ut. Avtalen og en eventuell sak hos NAV må da reises av ungdommen selv.</p>
<p><strong>Overvåkningen og opplysningsplikten</strong> Det siste leddet gir NAV voldsom makt. Lyver en far (som jobber svart eller gjemmer unna penger) på inntekten sin i et NAV-skjema for å slippe billig unna? Da gir loven NAV rett til å knuse bankenes og skatteetatens taushetsplikt. De går rett inn og henter lønnsslipper, sjekker likningen og overstyrer løgnen din for å fastsette riktig bidrag. For 18-åringer i skole kan NAV ringe rektor ("uten omsyn til teieplikta") for å sjekke om russen faktisk møter opp i timen (faglig progresjon) før de fortsetter bidraget.</p>""",
        "eksempler": [{"navn": "Skjule penger for eksen", "tekst": "Tom driver et murerfirma. Når Hanne krever barnebidrag gjennom NAV, sender Tom inn et skjema der han hevder han er nesten konkurs og kun tar ut 200 000 kr i lønn. Hanne vet at han eier fire leiligheter og nylig kjøpte en Porsche. Hanne varsler saksbehandleren i NAV. Med hjemmel i § 70 sjuende ledd, bryter NAV gjennom bankens taushetsplikt og avdekker store leieinntekter på sperrede kontoer. NAV beregner barnebidraget basert på hans reelle formue og inntekt, ignorerer løgnen hans, og tvinger ham til å betale et høyt bidrag, i tillegg til gebyret."}],
        "vanlige_feil": ["Kreve NAVs hjelp for \"prinsippets skyld\" når forskjellen på hva dere vil er minimal. Gebyret på 1278 kr (pr part) spiser opp den lille gevinsten uansett.", "Sende saken til NAV og glemme å gi dem beskjed om samværet ditt (NAV gir deg fradrag for netter du har barnet, glemmer du det, betaler du altfor mye).", "Tro at en privat avtale \"aldri kan endres\". Selv om du signerte på noe for 5 år siden, har du full rett til å ta det til NAV nå hvis 12 %-grensen er nådd."],
        "hva_bor_du_html": """<p><strong>Unngå gebyret.</strong> Gå inn på nav.no/barnebidrag. Bruk kalkulatoren deres i fellesskap med eksen. Hvis dere fyller ut nøyaktige tall for lønn, samværsnetter og barnehagekostnader, spytter kalkulatoren ut det nøyaktige tallet en saksbehandler ville kommet frem til. Avtal det tallet.</p>
<p>Hvis du vet at eksen din ikke kommer til å overføre pengene frivillig hver måned selv om dere er enige: Du kan inngå en privat avtale for beløpet, og <em>bare</em> be NAV om å kreve inn pengene (Innkreving). Det er en egen tjeneste som er billigere.</p>""",
        "dumme_sporsmal": [
            {"q": "Hvorfor blir saken sendt til domstolen (tredje ledd) hvis jeg ba om NAV?", "a": "Dette skjer hvis dere allerede har en pågående rettssak om hvem som skal ha daglig omsorg (fast bosted). Hvis dommeren skal bestemme hvor datteren bor, vil advokaten ofte be dommeren inkludere barnebidraget i den samme dommen, fordi bidraget (som du husker) utløses av hvem hun bor hos. Da slipper dere å kjøre to parallelle spor i staten. Men som oftest tar domstolen bare selve fordelingen, og dytter tallknusingen tilbake til NAV når dommen foreligger."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "67", "tittel": "plikten til å i det hele tatt betale", "available": True},
            {"lov": "barnelova", "paragraf": "71", "tittel": "hvordan selve \"utregningsformelen\" ser ut (hva som regnes med)", "available": True},
        ],
    },
    {
        "number": "71",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Regnestykket for barnebidrag: Hvordan teller staten kronene?",
        "kategori": "familie",
        "description": "Hvorfor betaler naboen mer i barnebidrag enn deg, selv om dere tjener likt? Fordi NAV bruker en kompleks formel som trekker fra samvær og sjekker boligutgifter.",
        "kort_svar": "Når NAV regner ut barnebidrag, gjør de tre ting: De finner ut hva barnet koster. De deler denne kostnaden mellom dere basert på hvor mye hver av dere tjener (deres andel). Så trekker de ifra for antall netter (samvær) du har barnet hos deg. Ingen kan tvinges til å betale mer i bidrag enn det de har råd til for å leve selv.",
        "paragraftekst": """Tilskotsfuten skal fastsetje tilskotet slik at fastsette utlegg til forsyting av barnet etter barnet sin alder (underhaldskostnadene) vert delte mellom foreldra etter storleiken på inntekta deira. Tilskotet skal likevel ikkje fastsetjast til eit høgare tilskot enn at tilskotspliktige har att fastsette midlar til eige underhald mv. (bidragsevnevurderinga). Tilskotet skal som hovudregel reduserast for munnleg eller skriftleg avtalt eller offentleg fastsett samvær. Har foreldra avtala delt bustad etter lova § 36, gjeld særskilte reglar.

Tilskotsfuten skal av eige tiltak regulere fostringstilskotet når barnet går over til ei ny aldersgruppe om ikkje anna er fastsett i forskrift etter tredje ledd.

Departementet kan ved forskrift gje utfyllande reglar om utmåling av fostringstilskot etter lova her.""",
        "hva_betyr_html": """<p>Paragrafen oppsummerer "bidragsmodellen" (matematikken) som Stortinget har vedtatt, og som ligger til grunn for NAVs kalkulator.</p>
<p>Modellen har fire logiske byggeklosser:</p>
<p><strong>1. Hva koster et barn?</strong> Først finner NAV ut "underholdskostnaden". Staten har tabeller for hva en 4-åring og en 16-åring koster i mat og klær (kalt forbruksutgifter), pluss barnets andel av husleien til mor, pluss barnets SFO- eller barnehageregning. For eksempel: Barnet koster 10 000 kr i måneden å holde i live.</p>
<p><strong>2. Hvem skal betale hva?</strong> Så sammenlignes inntektene. Far tjener 600 000 kr, mor tjener 400 000 kr. Den totale inntekten er 1 million. Fars "andel" er dermed 60 %. Hans "brøk" er å betale 60 % av de 10 000 kronene, altså 6 000 kr i måneden.</p>
<p><strong>3. Samværsfradraget</strong> Loven belønner foreldre som har barna sine mye. Siden barnet koster strøm og mat når det sover i din seng, får far et "samværsfradrag". Hvis faren har barnet annenhver helg, sier statens tabeller at dette kanskje gir et fradrag på 1 500 kr. Regnestykket for faren blir da: 6 000 kr (hans andel) minus 1 500 kr (samværsfradrag) \\= 4 500 kr i endelig barnebidrag.</p>
<p><strong>4. Evnevurdering ("fattigdomsgrensen")</strong> Loven passer på at ingen går personlig konkurs. Hvis du er trygdet eller jobber i en svært lavtlønnet jobb, vil NAV trekke ut "midler til eget underhold" fra ligningen din. De sier: "Du må ha penger til å betale din egen husleie og kjøpe mat". Hvis regnestykket i punkt 3 resulterte i et bidrag på 4 500 kr, men du ikke har penger igjen til å leve for, vil NAV justere bidraget ned (kanskje til 1 500 kr), eller frita deg helt. Du betaler altså maksimalt det du har <em>evne</em> til.</p>
<p>(Det andre leddet sier at NAV automatisk sjekker om barnet har gått over en aldersgrense som gjør at det koster mer penger, og justerer bidraget ditt i takt med at barnet blir eldre, uten at eksen trenger å betale gebyr for ny klage).</p>""",
        "eksempler": [{"navn": "Delt bosted og ingen bidrag?", "tekst": "Hanne og Thomas har delt fast bosted (50/50). Thomas tjener mye mer enn Hanne. Hanne krever barnebidrag, men Thomas mener at \"vi har dem jo 50/50, ingen betaler til noen\". Thomas feiler på matematikken. Første ledd sier \"gjelder særskilte regler\". NAV regner ut \"hva barnet koster\". Thomas har 70 % av inntektene. Han skal altså betale 70 % av kostnaden, men han har dem bare 50 % av tiden. Fordi hans andel av kostnaden er større enn det han tar ut i samvær, pålegger NAV Thomas å betale et barnebidrag til Hanne, selv ved 50/50 bosted. Beløpet blir lavere enn om Hanne hadde dem fulltid, men det nulles ikke ut."}],
        "vanlige_feil": ["Svart arbeid. (Nekter du å jobbe, eller \"gjemmer\" deg for å redusere inntekten din for å unnslippe bidrag, har NAV en funksjon der de bruker \"skjønnsfastsatt inntekt\" — de later som om du tjener det du normalt *burde* tjent, og du får et høyt bidrag basert på en fiktiv lønn).", "Samværsfar tenker at han skal redusere utgiftene for bidrag ved å bare betale \"mindre\" i feriene. (Samværsfradraget og feriene er allerede matematisk spredt tynt utover de 12 månedene)."],
        "hva_bor_du_html": "",
        "dumme_sporsmal": [
            {"q": "Får jeg mindre barnebidrag hvis den nye mannen min tjener mye penger?", "a": "Nei, den nye mannen din er ikke barnets far (han har ingen underholdsplikt etter § 66). Hans lønnsslipp legges ikke direkte inn i beregningen. Imidlertid er en parameter hos NAV \"boutgifter\" for barnet. Hvis du deler bolig med ny mann, reduseres dine egne boutgifter fordi dere deler på husleien. Dermed blir din totale underholdskostnad litt lavere, som kan slå bittelitt ut på brøken mot barnefar."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "66", "tittel": "grunnlaget for fordelingen", "available": True},
            {"lov": "barnelova", "paragraf": "70", "tittel": "at NAV kan gå inn i ligningen din for å sjekke om tallene stemmer", "available": True},
        ],
    },
    {
        "number": "72",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Kan du kreve barnebidrag med tilbakevirkende kraft?",
        "kategori": "familie",
        "description": "Har eksen sluppet unna barnebidrag i mange år fordi du ikke orket å ta saken? Loven setter en streng grense. Du kan bare kreve penger inntil tre år tilbake i tid.",
        "kort_svar": "NAV kan fastsette barnebidrag med tilbakevirkende kraft, men ikke lenger enn tre år bakover i tid fra det tidspunktet du sendte inn kravet ditt. For å få penger mer enn ett år tilbake i tid, kreves det i tillegg en veldig god begrunnelse for hvorfor du ventet så lenge med å kreve dem inn.",
        "paragraftekst": "Det kan fastsetjast fostringstilskot også for tid som har gått, men likevel ikkje for lengre tid enn tre år før kravet vart sett fram for avgjerdsorganet. Skal fastsetjing skje for meir enn eitt år attende, er det eit vilkår at parten har hatt særleg grunn for forseininga med å setje fram kravet.",
        "hva_betyr_html": """<p>Mange mødre (eller fedre med hovedomsorgen) prøver å være greie. De lar eksen slippe barnebidrag mens hen studerer, eller de lar være å sende inn krav fordi de frykter trusler og dårlig stemning. Kanskje de tenker "jeg klarer meg selv" i flere år.</p>
<p>Så ryker tålmodigheten. Eksen får seg kjempejobb og ny Tesla, og betaler fremdeles ingenting. Da vil bostedsforelderen saksøke for "alt han skylder meg de siste syv årene".</p>
<p>Her rykker paragraf 72 ut for å beskytte eksen mot økonomisk ruin. Lovgiver mener at hvis du har klart deg uten pengene i fem år, var de kanskje ikke så kritiske, og den andre forelderen må beskyttes mot å få en plutselig milliongjeld av staten.</p>
<p>Loven gir deg rett til å kreve penger med tilbakevirkende kraft (for "tid som har gått"), men med knallharde tidsgrenser:</p>
<ul><li><strong>Ett år:</strong> Hvis du krever tilbake for alt inntil 12 måneder tilbake i tid, går det som regel greit uten at NAV stiller så mange spørsmål.</li><li><strong>Tre år (absolutt maksgrense):</strong> Hvis du ber om penger inntil tre år tilbake, må du ha en "særlig grunn" til hvorfor du ventet. En særlig grunn kan være at farskapssaken og DNA-testen tok to år, at eksen truet deg, eller at eksen holdt adressen sin skjult i utlandet.</li><li><strong>Mer enn tre år:</strong> Forbudt. Det er fysisk umulig for NAV å ilegge barnebidrag lenger tilbake enn 36 måneder før kravet ble sendt inn (stempelet på konvolutten/digital mottaksdato). Pengene for år fire og fem er tapt for alltid.</li></ul>""",
        "eksempler": [{"navn": "Karis fem tapte år", "tekst": "Kari har oppdratt Truls alene fra han var 1 år til han var 6 år. Faren, Jens, har aldri betalt ei krone. Kari orket ikke ta kampen med NAV, siden Jens var arbeidsledig. Når Jens vinner i Lotto og får god jobb, sender Kari inn krav om bidrag, og krysser av for \"fra Truls ble født for fem år siden\". NAV svarer med § 72. Kari får maksimalt etterbetalt for tre år tilbake, og bare hvis hun kan begrunne at Jens for eksempel truet henne til å ikke kreve pengene før. Klarer hun ikke det, får hun penger kun ett år tilbake. De resterende årene forsvinner i intet. Jens får en regning for 12 måneder tilbake, pluss løpende bidrag fremover."}],
        "vanlige_feil": ["Bostedsforeldre som \"venter\" med å kreve inn penger, i troen på at \"jeg sparer opp gjelden hans på en konto i hodet mitt\". (Staten anerkjenner ikke gjelden før skjemaet er levert inn til dem).", "Tro at en far slipper barnebidrag automatisk fordi mor ikke gidder kreve. Hvis staten fatter at mor og barn lider økonomisk og hun mottar overgangsstønad, trer staten inn som kreditor og krever faren for tre år bakover uansett hva mor vil."],
        "hva_bor_du_html": "<p>Har du fått hovedomsorgen, og eksen overfører ikke penger frivillig (slik dere avtalte privat): Ikke la månedene gå i håp om at han \"finner ut av det\". Du trenger ikke kreve formelt NAV-vedtak umiddelbart (siden det koster gebyr), men i det dere passerer seks måneder uten en krone, må du sende inn kravet til NAV før du mister retten til de eldste månedene.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om vi signerte en avtale om at han skylder meg penger fra åtte år tilbake?", "a": "Hvis dere frivillig oppretter en sivil gjeldsavtale (et gjeldsbrev) med to vitner, er det et avtale-rettslig papir, ikke \"barnebidrag\". Da kan du bruke inkasso mot ham på vanlig måte for den gjelden. Men NAV vil ikke tvangsinndrive 8 år gammelt barnebidrag gjennom barnebidragssystemet sitt, de grensene er absolutte."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "70", "tittel": "hvordan du faktisk krever pengene (ved å sende inn søknad)", "available": True},
        ],
    },
    {
        "number": "73",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Barnebidraget justeres i takt med prisene (indeksregulering)",
        "kategori": "familie",
        "description": "Barnebidraget vokser av seg selv hver sommer for å holde tritt med prisveksten i samfunnet. Slik fungerer indeksreguleringen.",
        "kort_svar": "Faste barnebidrag økes litt én gang i året for å holde tritt med inflasjonen (at mat og klær blir dyrere). Denne justeringen kalles indeksregulering, og følger den generelle prisveksten i samfunnet (konsumprisindeksen). Den trer automatisk i kraft hver juni måned.",
        "paragraftekst": """Alle faste fostringstilskot til barn skal indeksregulerast etter reglane i denne paragrafen dersom ikkje anna er fastsett i avgjerda eller avtalen.

Indeksreguleringa gjeld også for beløpet som er fastsett etter forskotteringsloven § 5 første stykket, med mindre Stortinget gjer vedtak om noko anna.

Reguleringa er knytta til endringane i konsumprisindeksen frå Statistisk sentralbyrå. Tilskota skal regulerast kvart år ut i frå endringa i konsumprisindeksen for januar månad i høve til indeksen ved førre regulering. Kvar regulering gjeld berre for tilskotsterminar som forfell i juni eller seinare.

Tilskota skal regulerast med den prosentsats som konsumprisindeksen er endra med, rekna ut på næraste tidel. Tilskotssummen vert avrunda til næraste heile ti kroner.

Tilskotsfuten reknar om tilskot som skal krevjast inn etter lova om innkrevjing av fostringstilskot.

Departementet kan gje forskrifter om gjennomføring og utfylling av reglane i paragrafen her.""",
        "hva_betyr_html": """<p>Et barnebidrag fastsatt til 3 000 kroner i 2012, var verdt mye mer i matbutikken den gang enn det er i dag. For å hindre at barnebidragets kjøpekraft fordamper, har staten bestemt at alle barnebidrag har automatgir.</p>
<p><strong>Sommerens lønnsoppgjør:</strong> Hver juni måned (tredje ledd) sjekker staten hvor mye prisene i Norge har steget det siste året, ved hjelp av Statistisk Sentralbyrås konsumprisindeks (KPI) for januar det samme året. Hvis prisene har steget med 4 %, legger staten automatisk 4 % på toppen av det barnebidraget du betaler eller mottar.</p>
<p>Har NAV ansvaret for innkrevingen din, merker du ikke dette utover at du plutselig blir trukket (eller mottar) 3 120 kr i stedet for 3 000 kr på sommeren. Dette rundes alltid av til nærmeste tikroner (fjerde ledd).</p>
<p>Har du laget en <em>privat</em> avtale med eksen, ligger ballen hos deg. Da må du huske å be eksen (eller endre overføringen din) om å justere beløpet hver sommer for å følge loven. Eneste unntak (første ledd) er om du og eksen i den private avtalen uttrykkelig skrev under på: "Dette beløpet skal være statisk og aldri indeksreguleres". Dette er lovlig, men svært ugunstig for barnet (mottakeren).</p>""",
        "eksempler": [{"navn": "Sommerbrevet fra NAV", "tekst": "Tom betaler 4 000 kroner til Siri. I mai får Tom et brev fra NAV (\"tilskotsfuten\"): \"Fra og med juni reguleres barnebidraget i henhold til konsumprisindeksen. Årets vekst er 3,2 %. Ditt nye bidrag fra 1. juni er 4 130 kr\". Tom trenger ikke protestere eller kreve ny utregning, dette ligger innbakt i lovverket. Siri vil se at det tikker inn mer penger på konto for å dekke de økte matvareprisene."}],
        "vanlige_feil": ["Samværsfar tenker at han kan senke bidraget sitt fordi eksen fikk seg ny jobb, og sletter indeksreguleringen manuelt i nettbanken. (Gjelden vil hobe seg opp, indeksreguleringen har ingenting med partenes inntekt å gjøre).", "Bostedsforeldre som har private avtaler \"glemmer\" å oppjustere kravet hver sommer i årevis, og taper tusenvis av kroner de egentlig hadde krav på fordi kjøpekraften sank."],
        "hva_bor_du_html": "<p>Har dere en privat avtale? Lag et varsel på telefonen din hver juni: \"Sjekk NAV for årets barnebidrag-sats\". Dere kan bruke NAVs egen priskalkulator for å justere avtalen deres opp de få prosentene det utgjør. Loven avrunder til nærmeste tier, noe som gjør hoderegningen enklere.</p>",
        "dumme_sporsmal": [
            {"q": "Får jeg indeksregulert beløpet hvis konsumprisindeksen går i minus (deflesjon)?", "a": "Teoretisk sett ja, selv om det er ekstremt sjelden i norsk økonomi at samfunnet opplever deflasjon (prisnedgang). Men bidraget er uløselig knyttet til levekostnadene, så hvis brød og melk blir mye billigere, følger matematikken etter nedover."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "70", "tittel": "hvordan det opprinnelige, private beløpet ble regnet ut", "available": True},
        ],
    },
    {
        "number": "74",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Særskilt endring (nedsettelse eller ettergivelse) av barnebidrag",
        "kategori": "familie",
        "description": "Har du mistet jobben og står i gjeld til NAV for barnebidrag du ikke klarer å betale? Loven gir en sikkerhetsventil der staten kan slette eller sette ned gjelden din.",
        "kort_svar": "Har du havnet i dyp krise (f.eks. sykdom eller konkurs) og har bygget opp massiv barnebidragsgjeld som du umulig kan betale, gir loven staten lov til å stryke (ettergi) deler av, eller hele, gjelden. Også løpende bidrag kan avsluttes. Dette gjelder spesielt der gjelden er et krav som staten eier (ikke privat krav til eksen).",
        "paragraftekst": """Tilskot som er fastsett av administrativt organ eller domstol, kan krevjast endra dersom særlege grunnar talar for det. Departementet kan i forskrift gje utfyllande reglar om slik endring.

Også tilskot som er eller skulle ha vore betalt då kravet om endring vart framsett, kan setjast ned, setjast opp eller ettergjevast dersom sterke grunnar talar for det. Departementet kan i forskrift gje utfyllande reglar om ettergjeving av slik gjeld. Reglane i § 72 andre punktum gjeld tilsvarande.

Vert det teke avgjerd om å setje ned tilskot som alt skulle vere betalt, skal private og offentlege krav i tilskotet for perioden som endringa gjeld, fastsetjast på nytt under omsyn til den nye tilskotssatsen.

Reglane i § 70 andre og tredje stykket gjeld tilsvarande om kven det høyrer under å ta avgjerd om særskilt endring.

Reglane i § 70 sjette stykket om at tilskotsfuten kan fastsetje fostringstilskot av eige tiltak gjeld tilsvarande ved endring av tilskot.""",
        "hva_betyr_html": """<p>I vanlig kontraktsrett blir du trukket til siste trevl hvis du skylder penger. Men barnebidragsgjeld kan bli livsvarig. En mann som går på en psykisk smell og blir ufør i tre år, mens NAV fortsetter å regne ut 4 000 kr i bidrag hver måned (kanskje basert på en gammel lønn han aldri varslet om at var borte), vil ende med over 100 000 kroner i statlig gjeld og lønnstrekk resten av livet.</p>
<p>Paragraf 74 er lovens tilgivelse.</p>
<p><strong>Ting i fremtiden (Første ledd)</strong> Når som helst (forutsatt "særlige grunner", altså at inntekten din er knust eller samværet er endret), kan du kreve at den faste summen endres (slettes eller settes ned). Du betaler da det magiske NAV-gebyret for omgjøring (som vi lærte om i § 70), og de sjekker om du treffer den magiske "12 %" endrings-grensen.</p>
<p><strong>Gammel gjeld (Andre og tredje ledd)</strong> Dette er det viktigste. Hvis du allerede skylder NAV penger (f.eks. fordi NAV betalte bidragsforskudd til mor, og nå krever deg for de pengene fordi du aldri betalte), kan du søke om å få "ettergitt" (slettet) denne gjelden. Kravet er ekstremt strengt: "sterke grunnar". Sterke grunner betyr som regel at du har vært uhelbredelig syk, eller varigt ufør, slik at du beviselig aldri vil klare å betale regningen uansett hvor mye namsmannen truer med tvang. Sletter staten gjelden, slipper du å starte det nye livet ditt i total ruin. Hvis gjelden tilhører den andre forelderen privat, er terskelen for at staten skal blande seg inn og slette hennes krav mot deg vesentlig høyere, men det kan skje ved ny utregning tilbake i tid.</p>""",
        "eksempler": [{"navn": "Gjelden som ble slettet", "tekst": "Lars tjente bra i mange år og betalte 8 000 kr i bidrag for to barn. Han kom ut for en alvorlig arbeidsulykke i 2022 og havnet i koma, og deretter på AAP. Fordi ingen (heller ikke Lars) var i stand til å fylle ut \"endringskjema for barnebidrag\" til NAV, fortsatte taksameteret å løpe på 8 000 kr pr måned i to år. Gjeld: 192 000 kr. Når Lars blir frisk nok i 2024, søker han ettergjeving av gjeld (§ 74 andre ledd). NAV og departementet ser at ulykken var utenfor hans kontroll (sterk grunn). NAV sletter hele gjelden for toårs-perioden, og justerer deretter (første ledd) fremtidsbidraget ned til et par hundre kroner tilpasset hans uføretrygd."}],
        "vanlige_feil": ["Bli permittert fra jobben og \"vente\" med å sende melding til NAV fordi \"jeg betaler bare når jeg får ny jobb neste år\". (Barnebidrag forfaller fortløpende. En permittering alene gir sjelden \"sterke grunner\" for å slette en stor gjeld du i ren latskap unnlot å varsle NAV om. Du blir sittende med en gjeldsbombe).", "Bostedsforelder tror hun taper de pengene staten allerede har betalt henne i bidragsforskudd hvis eksen får slettet sin bidragsgjeld til staten. (Nei, hun beholder de pengene hun fikk i forskudd, det er staten som tar tapet når mannen får slettet regress-gjelden)."],
        "hva_bor_du_html": """<p>Har du barnebidragsgjeld hos Statens Innkrevingssentral som kveler deg? Du må fylle ut skjemaet for "Søknad om ettergivelse av bidragsgjeld" på NAV.no. Du må dokumentere helsetilstand og restarbeidsevne svært grundig. Bevis at de "sterke grunnene" var utenfor din kontroll (sykdom), fremfor noe som skyldtes ditt eget økonomiske rot (gikk konkurs med bitcoinfirma).</p>
<p>Enda viktigere: Hver gang inntekten din faller drastisk (langvarig permittert, sykepenger), oppdater NAV med <em>en eneste gang</em> etter § 70. Ikke bygg deg opp gjeld i det hele tatt.</p>""",
        "dumme_sporsmal": [
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "70", "tittel": "rutinen for hvordan du klager/ber om endring (gebyrene)", "available": True},
            {"lov": "barnelova", "paragraf": "72", "tittel": "begrensningene på tilbakevirkende kraft", "available": True},
        ],
    },
    {
        "number": "75",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "NAV kan gi deg flere regninger enn du og eksen forventet",
        "kategori": "familie",
        "description": "Har du avtalt at du ikke skal betale for konfirmasjonen, men ble pålagt det likevel? Loven gir NAV lov til å overstyre kravene deres hvis de mener det er riktig for barnet.",
        "kort_svar": "Når en barnebidragssak (både faste bidrag og særtilskudd som konfirmasjon) først ligger på bordet til NAV, har de full makt til å endre beløp og typer tilskudd, selv om verken mor eller far har bedt om akkurat det. Har du flere barn med flere forskjellige mødre, har NAV i tillegg plikt til å kutte bidragene slik at det blir litt penger på alle, uten at du ruineres.",
        "paragraftekst": """I klagesaker og i saker om endring av tilskot etter § 74 kan avgjerdsorganet gå utanfor det partane gjer påstand om. Avgjerdsorganet kan også endre andre tilskot etter barnelova og forsytingstilskot til ektemake endå om ingen av partane krev det.

Der tilskotspliktige med fleire barn ikkje har full tilskotsevne eller samla tilskotsplikt er høgare enn ein viss prosent av inntekta eller oppfostringstilskot er fastsett etter lov 17. juli 1992 nr. 100 § 9-2, kan avgjerdsorganet av eige tiltak foreta samla forholdsmessig fastsetjing av tilskota til barna. Dette gjeld i alle typar saker der det kjem minst eitt krav om førstegongsfastsetjing, klage eller endring eller der tilskotsfuten av eige tiltak kan ta opp eit krav. Regelen gjeld uavhengig av om tilskotspliktige har barn med same tilskotsmottakar eller fleire tilskotsmottakarar. Lova §§ 70 andre stykket og 74 første stykket gjeld tilsvarande. Departementet kan ved forskrift gje utfyllande reglar om samla forholdsmessig fastsetjing av tilskot.""",
        "hva_betyr_html": """<p>Paragrafen gir et byråkratisk unntak for forvaltningen (NAV). I en normal rettssak eller klageprosess i Norge er dommeren/saksbehandleren bundet av "partenes påstand". Ber du om 500 kroner i erstatning, kan ikke dommeren kaste 2 000 kroner på deg.</p>
<p>Men når det gjelder barn, er staten (avgjørelsesorganet/NAV) ikke bundet av foreldrenes ønsker (første ledd).</p>
<p>Hvis mor sender inn en klage der hun bare ber om 200 kroner ekstra i måneden for SFO, kan NAV se på papirene, riste på hodet, og felle et vedtak som sier: "Denne pappaen tjener to millioner. Han skal ikke bare betale 200 kroner mer, han skal betale 3 000 kroner mer for SFO, og han skal i tillegg betale for konfirmasjonen, selv om mor ikke ba om det." NAV har lov til å overkjøre kravene for å sikre at barnet får det loven bestemmer.</p>
<p><strong>Barnekull-kollisjonen (Andre ledd)</strong> Det andre leddet er "seriefar-regelen". Hva skjer hvis en pappa med gjennomsnittlig inntekt (f.eks 500 000 kr) har tre barn med mor A, ett barn med mor B og to barn med mor C? Alle tre mødrene krever fullt barnebidrag fra NAV. Hvis NAV bare behandlet mor A sin klage blindt, ville pappaen fått et krav på 6 000 kr. Deretter krever mor B 3 000 kr. Til slutt ville han sittet igjen med 15 000 kr i samlet bidragskrav per måned, noe som sprenger evnen hans. Loven pålegger derfor NAV å "samordne" gjelden hans "av eige tiltak" (automatisk). Får NAV inn én klage fra mor C, har NAV plikt til å åpne alle de andre gamle sakene fra mor A og mor B, selv om verken A eller B har klaget. NAV legger hele mannens liv i potten, setter et tak på hvor stor del av lønnen hans som kan trekkes, og så kutter de bidragene til de seks barna jevnt ("forholdsmessig"). Mor A, B og C må alle tåle at de får mindre penger enn de trodde, fordi faren ikke har evne til å fullfinansiere barnekullene.</p>""",
        "eksempler": [{"navn": "Seriefaren", "tekst": "Trond betaler fullt barnebidrag (4 000 kr) for en sønn i Trondheim. Nå har Trond fått tvillinger med en kvinne i Oslo, som han nylig skilte seg fra. Tvillingmoren søker NAV om barnebidrag. Hvis Trond må betale 8 000 kr for tvillingene pluss 4 000 kr for gutten i Trondheim, knekker økonomien hans. NAV (med hjemmel i § 75) henter inn alle tre barna i samme beregning. De setter et tak på Tronds betalingsevne til 9 000 kr. NAV dytter automatisk barnebidraget til Trondheims-sønnen ned fra 4 000 kr til 3 000 kr, slik at tvillingene kan få 6 000 kr på deling. Moren i Trondheim mottar et vedtak om kutt, selv om hun aldri ba om noen endring."}],
        "vanlige_feil": ["En klagende mor blir sjokkert fordi hun fikk redusert det *hun allerede hadde*, da hun sendte inn klage for å få *enda mer*. (Sender du saken til NAV, kaster du terningen. De går gjennom alt med lupe).", "Fedre som sliter fordi de tror de må sende inn tre separate gebyr-søknader for å få ned justert sine tre forskjellige barnekull-krav. (NAV har plikt til å sjekke om din totale tilskuddsplikt er over maksgrensen når de håndterer deg)."],
        "hva_bor_du_html": """<p>Har du barn med flere forskjellige partnere og sliter økonomisk? Be NAV om en total samordning av bidragene dine (forholdsmessig fastsettelse).</p>
<p>Vær forsiktig med å kreve små-justeringer (f.eks SFO) for ett bestemt barn hos NAV hvis du vet at inntekten din har økt betydelig siden sist. Ved å åpne døren for NAV til én sak, tvinger du dem ofte til å saumfare alle inntektene dine opp mot evne-grensen din, og da kan du ende opp med store tilleggskrav på alle barna.</p>""",
        "dumme_sporsmal": [
            {"q": "Får barn av samme mor prioritert over barn av andre mødre?", "a": "Nei, staten gjør ingen forskjell på hvem barna har som mødre. En krone er en krone. \"Forholdsmessig fastsetjing\" betyr at kuttet fordeles prosentvis likt mellom alle barna basert på hva hvert barn rent matematisk \"koster\" ut ifra alder og statens standardtabeller."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "71", "tittel": "hvordan utregningen i seg selv gjøres", "available": True},
            {"lov": "barnelova", "paragraf": "74", "tittel": "reglene for klage og endring av tilskudd", "available": True},
        ],
    },
    {
        "number": "76",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Midlertidig avgjørelse om barnebidrag",
        "kategori": "familie",
        "description": "Haster det å få fastsatt barnebidrag? NAV kan lage et midlertidig vedtak uten å vente på at den andre forelderen svarer. Slik fungerer det.",
        "kort_svar": "Hvis det haster med å få på plass barnebidrag, kan NAV fatte et midlertidig vedtak raskt. De trenger ikke engang å vente på at den andre forelderen får uttalt seg. Vedtaket gjelder fra måneden du søkte, og pengene kan kreves inn umiddelbart mens saken behandles ferdig.",
        "paragraftekst": """Tilskotsfuten kan utan opphald fatsetje eit førebels tilskot. Hastar det, kan slik avgjerd takast utan at motparten får seie si meining.

Tilskotsfuten kan etter krav ta førebels avgjerd om å setje ned tilskot utan at motparten får seie si meining. Dette gjeld dersom tilskotsfuten finn det klårt at vilkåra for det er til stades.

Førebels avgjerd etter første og andre stykket gjeld frå og med den månaden kravet om fastsetjing eller endring vart sett fram. Slik avgjerd kan fullførast straks om ikkje anna er fastsett, og gjeld berre til det ligg føre ei endeleg avgjerd i saka.""",
        "hva_betyr_html": """<p>Loven bruker ordet "tilskotsfuten". I dag er dette NAV. Paragrafen handler om situasjoner der barnet og forelderen trenger penger til livsopphold raskt, og ikke har tid til å vente på lang saksbehandling.</p>
<p>Normalt har begge foreldre rett til å uttale seg, sende inn dokumentasjon på inntekt og samvær, og sjekke regnestykket før et barnebidrag (fostringstilskot) blir fastsatt. Dette kan ta flere måneder. Hvis situasjonen er akutt, gir loven NAV lov til å hoppe over denne ventetiden. De kan sette et foreløpig bidrag umiddelbart.</p>
<p>Dette gjelder også andre veien. Hvis du betaler bidrag og plutselig mister inntekten din, for eksempel på grunn av sykdom eller arbeidsledighet, kan du be om at bidraget midlertidig settes ned. NAV kan gjøre dette raskt, uten å spørre den andre forelderen først, hvis det er åpenbart at du har krav på det.</p>
<p>Uansett om bidraget blir satt opp eller ned, vil den midlertidige avgjørelsen gjelde fra den måneden du sendte inn kravet. Avgjørelsen er gyldig frem til NAV har behandlet saken ferdig og fattet et endelig vedtak.</p>
<h3>Kan NAV bestemme barnebidraget umiddelbart?</h3>
<p>Ja, i tilfeller der det haster, kan NAV fatte et midlertidig vedtak. Dette er en sikkerhetsventil for å sikre at barnet blir forsørget.</p>
<p>I praksis betyr dette at NAV bruker de opplysningene de allerede har. De kan se på skatteoppgjøret, inntektsregisteret og det de vet om hvem barnet bor hos. Ut fra dette regner de ut et foreløpig beløp.</p>
<p>Når det foreløpige vedtaket er fattet, er det bindende. Det betyr at pengene må betales med en gang, og at NAV Innkreving kan begynne å trekke penger fra lønnen til den som skal betale, dersom regningen ikke blir betalt frivillig. Når saken senere er ferdig behandlet, blir det gjort et sluttoppgjør. Har noen betalt for mye eller for lite, rettes dette opp.</p>
<h3>Hva skjer hvis du gjør feil?</h3>
<p>Hvis du ignorerer et foreløpig vedtak og lar være å betale, vil gjelden vokse raskt. NAV Innkreving vil starte tvangsinnkreving, for eksempel ved å ta trekk i lønnen din eller trekke penger direkte fra bankkontoen din.</p>""",
        "eksempler": [{"navn": "Sara", "tekst": """Sara har nettopp flyttet fra samboeren sin. Hun har hovedomsorgen for deres felles barn på tre år, men hun har veldig lav inntekt. Eks-samboeren tjener godt, men nekter å samarbeide om en avtale for barnebidrag. Sara har ikke penger til å betale husleien denne måneden.

Hun kontakter NAV og forklarer den akutte situasjonen. NAV ser i systemene at faren har høy inntekt, og de fatter et midlertidig vedtak om barnebidrag etter paragraf 76. De gjør dette uten å gi faren tre ukers frist til å uttale seg. Bidraget kreves inn umiddelbart, og Sara får penger til å dekke barnets utgifter mens den fulle saken behandles."""}],
        "vanlige_feil": ["Å tro at du ikke trenger å betale et midlertidig vedtak fordi det \"ikke er endelig\". Det må betales.", "Å slutte å betale det gamle bidraget mens du venter på behandling av søknad om å sette det ned.", "Å vente i flere måneder med å søke. Et midlertidig vedtak gjelder kun fra den måneden du søker."],
        "hva_bor_du_html": """<p>Står du i en akutt økonomisk krise fordi du ikke får barnebidraget du har krav på, kontakt NAV. Forklar hvorfor det haster, og be dem vurdere et midlertidig vedtak. Sørg for at du leverer søknaden elektronisk så raskt som mulig – datoen for søknaden er startskuddet for kravet ditt.</p>
<p>Er du den som betaler, og inntekten din har rast i bunn? Send inn dokumentasjon på inntektstapet (for eksempel oppsigelse eller legeerklæring) til NAV i dag. Be dem om et midlertidig vedtak om å sette ned bidraget, slik at du ikke bygger deg opp uoverkommelig gjeld mens saken ligger i kø hos NAV.</p>""",
        "dumme_sporsmal": [
            {"q": "Hva skjer hvis det endelige bidraget blir lavere enn det midlertidige?", "a": "Hvis NAV krever inn et foreløpig bidrag på 4 000 kr i måneden, og det endelige vedtaket viser at du bare skulle betalt 3 000 kr, har du betalt for mye. Dette vil rettes opp. Det overskytende beløpet vil som regel bli trukket fra på fremtidige bidrag."},
            {"q": "Kan jeg klage på et midlertidig vedtak?", "a": "Et midlertidig vedtak i seg selv er en foreløpig løsning og kan ofte ikke påklages på samme måte som et endelig vedtak, nettopp fordi den endelige avgjørelsen allerede er under arbeid. Du må rette innsigelsene dine mot det endelige vedtaket når det kommer."},
            {"q": "Må vi møte til megling for å få et midlertidig vedtak?", "a": "Nei. Avgjørelser om barnebidrag krever ikke at dere har vært til megling på familievernkontoret. Megling gjelder foreldreansvar, hvem barnet skal bo hos, og samvær."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "77", "tittel": "Klage på vedtak om barnebidrag", "available": True},
            {"lov": "barnelova", "paragraf": "78", "tittel": "Tvangsinnkreving av barnebidrag", "available": True},
            {"lov": "barnelova", "paragraf": "67", "tittel": "Plikten til å betale barnebidrag (fostringstilskot)", "available": True},
        ],
    },
    {
        "number": "77",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvordan klage på vedtak om barnebidrag",
        "kategori": "familie",
        "description": "Mener du at NAV har regnet feil på barnebidraget? Loven gir deg rett til å klage på avgjørelsen. Lær hvilke vedtak du kan klage på og hvordan prosessen fungerer.",
        "kort_svar": "Du har full rett til å klage hvis NAV har bestemt barnebidraget og du mener vedtaket er feil. Saken din går da til NAV Klageinstans. Unntaket er automatiske endringer fordi barnet skifter aldersgruppe — disse kan du ikke klage på.",
        "paragraftekst": "Avgjerd om fostringstilskot til barn fastsett av tilskotsfuten kan klagast inn for næraste overordna organ eller det organ som Arbeids- og velferdsdirektoratet bestemmer. Klageretten gjeld ikkje avgjerd som berre gjeld regulering ved overgang til ny aldersgruppe etter § 71 andre stykket.",
        "hva_betyr_html": """<p>Når NAV ("tilskotsfuten" i lovteksten) beregner og fastsetter et barnebidrag, gjør de det basert på informasjon om begge foreldrenes inntekt, hvem barnet bor hos, og hvor mye samvær det er. Hvis du mottar vedtaket og mener tallene er feil eller at NAV har misforstått situasjonen, kan du klage.</p>
<p>Når du klager, skal en ny og uavhengig avdeling se på saken din. I dag er dette NAV Klageinstans ("overordna organ").</p>
<p>Det finnes bare ett fast unntak fra klageretten i denne paragrafen. Barns utgifter stiger etter hvert som de blir eldre. NAV har faste aldersgrupper for dette (0-5 år, 6-10 år, 11-14 år og 15-18 år). Når et barn passerer en aldersgrense, for eksempel fyller 11 år, kan bidraget automatisk bli oppjustert. Du kan ikke sende inn en formell klage bare på at dette aldershoppet skjer.</p>
<h3>Hvordan klager du på vedtak om barnebidrag?</h3>
<p>Du må alltid sende klagen skriftlig til NAV. Fristen for å klage på et slikt vedtak er normalt seks uker fra du mottok vedtaket i posten eller digitalt.</p>
<p>Når du klager, må du peke helt konkret på hva du mener NAV har gjort feil. Er det brukt feil inntekt for den andre parten? Har de lagt til grunn feil samværsklasse? Har de oversett dokumentasjon du sendte inn om høye boutgifter eller særkullsbarn? Jo mer presis du er, jo lettere er det for NAV Klageinstans å rette feilen.</p>
<p>Før klagen sendes videre til klageinstansen, vil kontoret som fattet vedtaket se på saken din en gang til. Hvis de innser at de har gjort en åpenbar feil basert på opplysningene dine, kan de faktisk omgjøre sitt eget vedtak umiddelbart. Gjør de ikke det, går saken videre til formell klagebehandling.</p>
<h3>Hva skjer hvis du gjør feil?</h3>
<p>Hvis du slutter å betale det fastsatte bidraget mens du venter på svar på klagen din, vil du bygge opp bidragsgjeld. NAV Innkreving stopper ikke automatisk innkrevingen bare fordi du har sendt en klage.</p>""",
        "eksempler": [{"navn": "Thomas", "tekst": "Thomas betaler barnebidrag for datteren sin. Han mottar et nytt vedtak fra NAV hvor bidraget har økt betydelig. Når han leser vedtaket, ser han at NAV har beregnet ut fra at han har null netters samvær i måneden, selv om datteren er hos ham to helger i måneden (4-8 netter). Thomas leverer en klage skriftlig til NAV, og legger ved den signerte samværsavtalen med barnets mor. NAV oppdager feilen, gir ham medhold, og endrer vedtaket slik at bidraget blir riktig."}],
        "vanlige_feil": ["Å klage på at \"bidraget er for høyt\" uten å peke på en konkret utregningsfeil.", "Å la være å klage innen seks ukers fristen. Da blir vedtaket endelig.", "Å tro at du kan slutte å betale mens klagen behandles. Du må betale løpende bidrag helt til et nytt vedtak foreligger."],
        "hva_bor_du_html": """<p>Les vedlegget som heter "Beregning av barnebidrag" nøye. Sjekk de tre viktigste faktorene: 1. Er din inntekt satt riktig? 2. Er den andre forelderens inntekt satt rimelig riktig? 3. Stemmer antall samværsnetter per måned?</p>
<p>Finner du feil, logg inn på nav.no og send en klage via deres digitale klageskjema. Legg ved all nødvendig dokumentasjon som beviser at NAVs tall er feil. Er du i tvil, ring NAV og be dem forklare tallene i beregningen før du klager.</p>""",
        "dumme_sporsmal": [
            {"q": "Får jeg pengene tilbake hvis jeg vinner klagesaken?", "a": "Ja. Hvis du har betalt for mye mens klagen ble behandlet, vil dette rettes opp. Måten det gjøres på, er normalt at du får et lavere trekk de neste månedene helt til det du har betalt for mye, er spist opp."},
            {"q": "Kan mor klage på at bidraget har gått opp på grunn av alder?", "a": "Nei. Automatisk justering fordi barnet har fylt for eksempel 11 eller 15 år, kan man ikke klage på. Men hvis inntekten til en av foreldrene samtidig har endret seg vesentlig, kan du heller kreve en *ny fastsettelse* (endring) av bidraget etter paragraf 74."},
            {"q": "Koster det noe å klage?", "a": "Nei, selve klagen er gratis. Men merk at å be NAV regne ut bidraget for dere i første omgang (fastsettelse) medfører et engangsgebyr for hver av foreldrene."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "70", "tittel": "Hvordan barnebidraget fastsettes", "available": True},
            {"lov": "barnelova", "paragraf": "71", "tittel": "Automatiske endringer (indeksregulering og alder)", "available": True},
            {"lov": "barnelova", "paragraf": "74", "tittel": "Krav om endring av allerede fastsatt barnebidrag", "available": True},
        ],
    },
    {
        "number": "78",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Tvangsinnkreving av barnebidrag",
        "kategori": "gjeld",
        "description": "Hva skjer når barnebidraget ikke blir betalt? NAV Innkreving tar saken og kan trekke pengene rett fra lønnen til den som skylder penger.",
        "kort_svar": "Barnebidrag blir alltid krevd inn av NAV Innkreving hvis dere ikke har en privat avtale dere håndterer selv. Betales ikke regningen innen fristen på tre dager, har NAV rett til å tvangsinndrive pengene direkte — for eksempel ved å trekke fra lønn, konto eller ytelser.",
        "paragraftekst": """Fostringstilskot krevjast inn av Innkrevjingsmyndigheita.

Avgjerd i tilskotssak er tvangsgrunnlag for utlegg. Avgjerda har rettsverknader og kan fullførast før ho er endeleg, om ikkje anna er fastsett. Oppfyllingsfristen er tre dagar, om ikkje annan frist er fastsett.

Ei skriftleg avtale om tilskot er tvangsgrunnlag for utlegg når tilskot etter avtala vert kravd inn etter reglane i innkrevingsloven. Det same gjeld ei avgjerd om gebyr som nemnd i § 70 andre stykket.

Vert tilskot som er gjort opp, sett ned etter § 70 andre stykket, § 74 eller § 76 eller etter klage, kan den tilskotspliktige krevje at Innkrevjingsmyndigheita gjer frådrag i fostringstilskotet på den måten og for dei terminane som Innkrevjingsmyndigheita finn rimeleg. Avgjerd om frådrag i fostringstilskot kan påklagast etter reglane i forvaltningslova kapittel VI.""",
        "hva_betyr_html": """<p>Paragrafen handler om muskler. Staten sørger for at barnebidrag (fostringstilskot) faktisk blir betalt. Det er NAV Innkreving ("Innkrevjingsmyndigheita") som håndterer dette.</p>
<p>For det første: Hvis NAV har regnet ut og fastsatt bidraget, er dette vedtaket i seg selv et "tvangsgrunnlag". Det betyr at NAV ikke trenger å gå til retten eller namsmannen for å kreve inn pengene. Hvis regningen forfaller, kan de starte tvangsinnkreving direkte. Loven setter en usedvanlig kort frist: Bare tre dager, om ikke NAV setter en annen dato (normalt har NAV fast forfallsdato hver måned).</p>
<p>For det andre gjelder dette også hvis foreldrene har laget en egen privat skriftlig avtale, og den som skal betale, slutter å overføre pengene. Den andre forelderen kan da sende avtalen til NAV Innkreving, og NAV vil bruke samme makt for å drive inn pengene.</p>
<p>Til slutt regulerer paragrafen hva som skjer hvis du har betalt for mye. La oss si at bidraget ditt var 5 000 kr. Du klager, og saken tar tre måneder. Du får medhold, og bidraget blir satt ned til 3 000 kr med tilbakevirkende kraft. Da har du betalt 6 000 kr for mye. NAV Innkreving vil da justere de neste månedlige regningene dine ned, slik at du får fradrag inntil alt er rettet opp.</p>
<h3>Hva skjer hvis barnebidraget ikke blir betalt?</h3>
<p>NAV Innkreving har noen av de sterkeste innkrevingsverktøyene i staten. De sender ikke bare purringer. Hvis du ignorerer regningen for barnebidrag, vil de ilegge trekk i lønn.</p>
<p>Trekk i lønn (påløpstrekk) betyr at NAV pålegger arbeidsgiveren din å holde tilbake en del av lønnen din før den i det hele tatt utbetales til deg. Pengene sendes rett fra sjefen din til NAV Innkreving. NAV kan også ta trekk i trygdeytelser du mottar, eller i skatteoppgjøret ditt.</p>
<p>Barnebidrag er høyt prioritert gjeld. Hvis du har kredittkortgjeld, billån og bidragsgjeld, vil staten sørge for at barnet får pengene sine først.</p>
<h3>Hva skjer hvis du gjør feil?</h3>
<p>Bidragsgjeld er vanskelig å bli kvitt og slettes i utgangspunktet aldri. I tillegg til lønnstrekk kan alvorlig bidragsgjeld føre til pant i huset ditt eller beslag på kontoen din. Gjelden samler også opp forsinkelsesrenter.</p>""",
        "eksempler": [{"navn": "Lars", "tekst": "Lars og Ingrid har en privat, skriftlig avtale om at Lars skal betale 4 500 kr i måneden i barnebidrag til Ingrid. I tre måneder på rad betaler ikke Lars. Ingrid trenger ikke å leie advokat. Hun sender inn den skriftlige avtalen til NAV Innkreving og ber dem ta over. Fordi avtalen er skriftlig, fungerer den som tvangsgrunnlag. NAV sender Lars en regning, og da han ikke betaler, legger de inn et trekk i lønnen hans for både de løpende månedene og gjelden han har bygget opp."}],
        "vanlige_feil": ["Å tro at du kan stoppe innbetalingen av bidrag mens du er i en konflikt med eksen om samvær. Du må betale uansett.", "Å ha muntlige avtaler. En muntlig avtale om bidrag kan ikke brukes av NAV Innkreving. Det må være skriftlig.", "Å ignorere brev fra NAV Innkreving. Det fører kun til tvangstrekk og gebyrer."],
        "hva_bor_du_html": """<p>Hvis du er den som skal betale: Legg barnebidraget inn som fast trekk i banken på lønningsdagen. Mister du jobben eller blir sykemeldt slik at du ikke klarer regningen, søk umiddelbart om å få bidraget satt ned (endring). NAV sletter ikke gjeld som allerede har bygget seg opp mens du ventet med å søke.</p>
<p>Hvis du skal motta, og eksen ikke betaler: La NAV Innkreving ta over jobben. Ikke bruk energi på å krangle på SMS. Logg inn på NAV, be dem kreve inn bidraget for deg. Det fjerner konflikten fra hverdagen din.</p>""",
        "dumme_sporsmal": [
            {"q": "Hva skjer hvis barnefaren jobber svart eller ikke har penger på konto?", "a": "NAV Innkreving kan bare trekke penger fra lovlig, registrert inntekt eller trygd. Hvis han overhodet ikke har inntekt å trekke fra, bygger han opp en statlig gjeld som venter på at han en dag får inntekt. I mellomtiden kan du søke om bidragsforskudd fra NAV (se § 79)."},
            {"q": "Kan jeg nekte ham å treffe barna når han ikke betaler?", "a": "Nei. Penger og samvær er juridisk sett to helt atskilte ting. Selv om han skylder hundretusenvis av kroner i barnebidrag, har han fremdeles rett til det samværet som er avtalt."},
            {"q": "Må jeg betale et gebyr for at NAV skal kreve inn pengene?", "a": "Nei, selve innkrevingen via NAV Innkreving er gratis for deg som mottaker. Hvis NAV også skal *regne ut* bidraget først, må begge parter normalt betale et fastsettelsesgebyr (ca. én rettsgebyr, drøyt 1 200 kr)."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "76", "tittel": "Midlertidig avgjørelse om bidrag", "available": True},
            {"lov": "barnelova", "paragraf": "67", "tittel": "Plikten til å forsørge barnet", "available": True},
            {"lov": "forsinkelsesrenteloven", "paragraf": "2", "tittel": "Renter på utestående gjeld", "available": False},
        ],
    },
    {
        "number": "79",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Får du penger hvis den andre forelderen ikke betaler?",
        "kategori": "familie",
        "description": "Nekter eksen å betale barnebidrag? Eller har hen ikke inntekt? Du kan søke staten om bidragsforskudd. Her er reglene.",
        "kort_svar": "Hvis du ikke får barnebidraget du har krav på, eller den andre forelderen tjener for lite til å betale, kan du få et månedlig bidragsforskudd fra staten. Størrelsen på forskuddet avhenger av din egen inntekt.",
        "paragraftekst": "Om utbetaling av forskot på tilskot gjeld reglane i lov 17. februar 1989 nr. 2 om bidragsforskott (forskotteringsloven).",
        "hva_betyr_html": """<p>Denne paragrafen i barneloven er ekstremt kort. Den fungerer bare som et gateskilt som peker mot en helt annen lov: Forskotteringsloven. Sammen utgjør de sikkerhetsnettet for aleneforeldre i Norge.</p>
<p>Systemet kalles "bidragsforskudd". Det betyr at NAV går inn og utbetaler et fast beløp til deg hver måned, uavhengig av om den andre forelderen faktisk betaler regningen sin eller ikke. Staten "forskotterer" pengene til barnet. Deretter er det NAV Innkreving sitt problem å kreve inn de utestående pengene fra den andre forelderen — det er ikke lenger ditt problem.</p>
<p>Bidragsforskudd gjelder i to hovedsituasjoner. Den vanligste er at faren eller moren ikke har evne til å betale (lav inntekt, student, fengsel, trygd). Den andre situasjonen er at de faktisk har penger, men nekter å betale, og at NAV ennå ikke har klart å tvangsinndrive beløpet. Barnets løpende behov skal ikke lide på grunn av de voksnes konflikter eller manglende evne.</p>
<h3>Hvem får bidragsforskudd og hvor mye?</h3>
<p>Du får ikke automatisk det fulle barnebidraget som eksen egentlig skulle betalt. Bidragsforskuddet er statlige penger, og det er behovsprøvd mot <em>din</em> inntekt.</p>
<p>Tjener du veldig godt, for eksempel over en bestemt grense (som justeres årlig, ofte rundt 500.000–600.000 kr), får du ingenting i forskudd. Da mener staten at du klarer å forsørge barnet alene. Har du lav inntekt, får du et høyere beløp. Det opereres normalt med ulike satser (forhøyet, ordinært, eller redusert forskudd).</p>
<p>For å få bidragsforskudd må tre grunnleggende vilkår være oppfylt: Barnet må bo fast hos deg, barnet må være under 18 år, og NAV Innkreving må ha ansvaret for å kreve inn barnebidraget i saken deres. Du kan ikke be om forskudd hvis dere har en privat ordning og dere ikke har latt NAV ta over saken.</p>
<h3>Hva skjer hvis du gjør feil?</h3>
<p>Hvis du mottar forhøyet bidragsforskudd basert på at du bor alene med lav inntekt, og du lar være å melde fra til NAV om at du har fått en samboer, regnes dette som trygdesvindel. Da vil NAV kreve pengene tilbakebetalt senere.</p>""",
        "eksempler": [{"navn": "Anne", "tekst": "Anne bor alene med to barn. Faren til barna har flyttet til utlandet, sluttet å svare på meldinger, og betaler ikke det månedlige bidraget på 3 000 kr per barn. Anne jobber deltid og har dårlig råd. Hun kontakter NAV og ber dem kreve inn bidraget, og søker samtidig om bidragsforskudd. Siden Annes egen inntekt er lav, innvilger NAV henne forskudd. Hun får pengene fast inn på konto fra staten hver måned. NAV jobber parallelt for å kreve inn pengene fra faren i utlandet, men Anne påvirkes ikke lenger økonomisk av om han betaler eller ikke."}],
        "vanlige_feil": ["Å tro at forskuddet er like stort som barnebidraget. Det er det sjelden.", "Å ha en privat innkrevingsavtale og klage over manglende betaling. (Forskudd krever offentlig innkreving).", "Å glemme å gi beskjed til NAV hvis du gifter deg eller får samboer. Dette kan påvirke retten din til forskudd."],
        "hva_bor_du_html": """<p>Hvis den andre forelderen er notorisk dårlig på å betale, eller har veldig ustabil inntekt: Gå inn på nav.no. Søk først om at NAV Innkreving skal overta all innkreving av barnebidraget. Send deretter umiddelbart inn en egen søknad om bidragsforskudd.</p>
<p>Selv om du tjener for mye til å få selve forskuddet, vil du da i alle fall være sikret at NAV tar ansvaret for tvangsinndrivelsen (lønnstrekk) fra den andre parten.</p>""",
        "dumme_sporsmal": [
            {"q": "Får eksen slettet gjelden sin når staten betaler forskudd?", "a": "Absolutt ikke. Forskuddet gis til barnet, men den forelderen som egentlig skulle betalt, bygger fortsatt opp en massiv gjeld til staten, som blir inndrevet hensynsløst over tid."},
            {"q": "Hva om faren er ukjent?", "a": "Hvis farskapet ikke er fastslått, eller hvis den andre forelderen er død (og barnet ikke får barnepensjon), gjelder det egne regler som sikrer at barnet får bidragsforskudd fra staten uansett."},
            {"q": "Kan jeg få etterbetalt forskudd for årene han ikke betalte?", "a": "Du kan få etterbetalt forskudd for inntil 3 måneder før du søkte. Men ikke for flere år tilbake. Søk derfor med en gang problemet oppstår, ikke vent."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "78", "tittel": "Innkreving og tvang", "available": True},
            {"lov": "barnelova", "paragraf": "80", "tittel": "Tilbakebetaling hvis farskapet endres", "available": True},
            {"lov": "barnelova", "paragraf": "66", "tittel": "Foreldres plikt til å forsørge", "available": True},
        ],
    },
    {
        "number": "80",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Få tilbake barnebidrag hvis du ikke er faren",
        "kategori": "familie",
        "description": "Har du betalt barnebidrag, men en DNA-test viser at du ikke er faren? Slik krever du pengene tilbakebetalt fra staten.",
        "kort_svar": "Hvis en DNA-test beviser at du ikke er far til barnet likevel, kan du kreve å få tilbakebetalt det du har betalt i barnebidrag. Du krever pengene fra folketrygden (NAV), ikke fra barnet eller moren. Beløpet justeres for prisvekst, men det trekkes fra 20 prosent fordi du tidligere har hatt skattefordeler av å betale bidrag.",
        "paragraftekst": "Vert nokon som har betalt pålagt eller avtala fostringstilskot til eit barn, seinare friteken for farskapen til barnet, kan han krevje summen betalt attende frå folketrygda. Summen skal indeksregulerast i samsvar med konsumprisindeksen frå Statistisk sentralbyrå frå tilskotet vart betalt, og til det vert betalt attende. Ei indeksregulering skal likevel først gjerast etter at det er teke omsyn til frådraga den frikjende faren tidlegare har fått i skattefastsetjinga si for betalt tilskot. Fordelen av det tidlegare frådraget i skattefastsetjinga skal setjast til 20 prosent. Kravet kan setjast ned eller falle bort dersom det er klart at han ikkje hadde rimeleg grunn til å vedgå eller erklære farskapen, eller at han burde ha reist sak til endring tidlegare.",
        "hva_betyr_html": """<p>Noen ganger betaler en mann barnebidrag i flere år, før en DNA-test avslører at han faktisk ikke er den biologiske faren. Loven gir deg da rett til å få disse pengene tilbake.</p>
<p>Du skal ikke kreve pengene direkte fra barnet, fra moren, eller fra den biologiske faren. Det ville skapt umulige situasjoner for familiene. I stedet krever du pengene tilbake fra staten gjennom folketrygden (NAV). Staten tar regningen overfor deg, og NAV håndterer saken.</p>
<p>Når du får pengene tilbake, skal beløpet oppjusteres i takt med prisveksten i samfunnet (konsumprisindeksen). Men du får ikke tilbake absolutt alt. Fordi du har fått fradrag på skatten for barnebidraget i årene du betalte det, gjør loven et standardisert trekk på 20 prosent av summen.</p>
<p>Det er ett viktig unntak for å få pengene tilbake: Du kan ikke ha visst, eller hatt sterk grunn til å tro, at du ikke var faren, uten å gjøre noe med det. Hvis du visste at du ikke var faren, men likevel valgte å betale i mange år før du gikk til sak, kan kravet ditt reduseres eller falle helt bort.</p>
<h3>Hvor mye penger kan du få tilbake?</h3>
<p>Du får tilbake summen av alle bidrag du faktisk har betalt. Siden penger var verdt mer for ti år siden enn i dag, justeres beløpet for prisstigning. Deretter trekker NAV fra 20 prosent for å veie opp for den skattefordelen du allerede har hatt.</p>
<p>Har du for eksempel betalt 100 000 kroner over noen år, vil summen først justeres opp litt for inflasjon, før NAV fjerner en femtedel. Du ender da grovt regnet opp med rundt 80 000 kroner utbetalt.</p>""",
        "eksempler": [{"navn": "Marius", "tekst": "Marius har betalt 3 000 kroner i måneden i barnebidrag for en gutt i seks år. Da gutten er seks, kommer det frem at moren hadde et annet forhold på samme tid, og en DNA-test viser at Marius ikke er faren. Farskapet blir endret i domstolen. Marius sender et krav til NAV om å få tilbakebetalt bidraget. NAV regner ut totalbeløpet (over 200 000 kroner), justerer for prisvekst, trekker fra 20 prosent for tidligere skattefradrag, og overfører pengene til Marius sin konto."}],
        "vanlige_feil": ["Å kreve pengene tilbakebetalt direkte fra moren", "Å tro at du får tilbake på øret nøyaktig det du betalte inn (grunnet 20-prosent-regelen)", "Å vente i mange år med å ta DNA-test hvis du har en sterk mistanke"],
        "hva_bor_du_html": "<p>1. <strong>Få farskapet offisielt endret</strong> — Du kan ikke bare slutte å betale eller kreve penger basert på en privat DNA-test. Farskapet må endres formelt gjennom domstolen eller NAV først. 2. <strong>Send krav til NAV</strong> — Så snart farskapet er endret og du er slettet som far, sender du et formelt krav til NAV om tilbakebetaling av fostringstilskott (barnebidrag). 3. <strong>Legg ved dokumentasjon</strong> — Sørg for at vedtaket om at du ikke er faren, ligger vedlagt.</p>",
        "dumme_sporsmal": [
            {"q": "Kan moren bli straffet og måtte betale tilbake til NAV?", "a": "Loven sier at du (mannen som betalte) krever pengene fra NAV. NAV kan i noen svært spesielle tilfeller vurdere om noen andre har opptrådt svikaktig, men som hovedregel er dette statens tap, og du slipper å krangle med moren om pengene."},
            {"q": "Hva hvis det er jeg som er den egentlige faren — må jeg betale for de årene den andre mannen betalte?", "a": "Den mannen som feilaktig betalte, får pengene fra folketrygden. Loven sier at han ikke kan søke pengene direkte fra den virkelige faren. NAV vil deretter forholde seg til deg for fremtidige barnebidrag."},
            {"q": "Får jeg renter på pengene?", "a": "Du får ikke renter i vanlig forstand, men beløpet oppjusteres etter konsumprisindeksen (inflasjon). Dette sikrer at pengene har samme kjøpekraft i dag som da du betalte dem inn."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "6", "tittel": "Endring av farskap i domstolen", "available": True},
            {"lov": "barnelova", "paragraf": "70", "tittel": "Hvordan barnebidrag fastsettes", "available": True},
            {"lov": "barnelova", "paragraf": "24", "tittel": "Prøvetaking og DNA-analyse", "available": True},
        ],
    },
    {
        "number": "81",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Når kan farskap fastsettes i Norge?",
        "kategori": "familie",
        "description": "Hvilke regler gjelder når foreldrene bor i forskjellige land? Sjekk om det er norske myndigheter som skal fastsette farskapet til barnet.",
        "kort_svar": "Farskap og medmorskap kan avgjøres av norske myndigheter hvis barnet, moren eller den oppgitte faren har fast adresse i Norge. Men hvis familien har mye sterkere tilknytning til et annet land, og saken løses bedre der, kan norske domstoler nekte å behandle saken.",
        "paragraftekst": "Farskap og medmorskap kan fastsetjast i Noreg etter [§ 4, § 7 og kapitla 3 og 4",
        "hva_betyr_html": """<p>Når folk flytter på tvers av landegrenser, oppstår det fort spørsmål om hvilket lands system som skal brukes. Paragraf 81 bestemmer i hvilke internasjonale situasjoner Norge kan og skal rydde opp i hvem som er far eller medmor til et barn.</p>
<p>Norske myndigheter (NAV eller domstolene) tar saken hvis ett av tre krav er oppfylt: 1. Moren bodde i Norge da barnet ble født. 2. Barnet har flyttet til Norge og bor fast her nå. 3. Mannen (eller medmoren) som hevdes å være forelder, bor fast i Norge.</p>
<p>Oppfylles ett av disse kravene, regnes saken som "norsk nok" til at våre myndigheter kan ta i den.</p>
<p>Men det finnes en sikkerhetsventil. Selv om ett av kravene er oppfylt, kan norske myndigheter si nei hvis saken opplagt hører hjemme i et annet land. Hvis for eksempel mor og barn bor i Sverige, faren oppholder seg litt i Norge, men alle bevis, vitner og det meste av familiens liv er i Sverige, bør saken gå for en svensk domstol.</p>
<h3>Kan du endre et farskap i Norge?</h3>
<p>Reglene for å endre et farskap som allerede er fastsatt, ligner. En sak om å fjerne en far og eventuelt få inn en ny, kan reises for en norsk domstol hvis den som saksøker bor i Norge, eller hvis det opprinnelige farskapet ble fastsatt etter norske regler. Bor alle partene i utlandet og farskapet opprinnelig ble fastsatt i utlandet, vil ikke norske domstoler ta saken.</p>""",
        "eksempler": [{"navn": "Tom", "tekst": "Tom bor i Norge. Han har hatt et forhold til en kvinne som bor i Danmark, og hun får et barn der. Hun oppgir Tom som far. Fordi Tom har fast bosted i Norge, kan spørsmålet om han er far til barnet avgjøres av norske myndigheter, selv om barnet og moren bor i Danmark."}],
        "vanlige_feil": ["Å tro at barnet må ha norsk statsborgerskap for at saken kan gå i Norge. Det er hvor du bor (\"vanleg bustad\") som teller, ikke passet ditt.", "Å tro at du kan \"shoppe\" mellom land for å finne den domstolen som er snillest med deg. Loven krever reell tilknytning til Norge."],
        "hva_bor_du_html": "<p>Hvis du er usikker på hvem som er far, og noen av partene bor i utlandet: 1. Sjekk hvem som bor hvor. Hvis mor, barn eller oppgitt far er folkeregistrert og faktisk bor i Norge, kan NAV hjelpe deg. 2. Ta kontakt med NAV Foreldrepenger og bidrag, og forklar at det er en internasjonal sak. De kan innkalle til DNA-test internasjonalt og samarbeide med myndigheter i andre land.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om mannen flytter fra Norge underveis i saken?", "a": "Hvis han hadde vanlig bosted i Norge da saken startet, beholder Norge normalt saken. Du kan ikke stoppe en farskapssak bare ved å pakke kofferten og flytte til utlandet."},
            {"q": "Gjelder det samme for medmorskap?", "a": "Ja, reglene for å fastsette medmorskap over landegrenser følger nøyaktig de samme kriteriene som for farskap."},
            {"q": "Kan Norge bare bestemme farskapet uten videre?", "a": "Norge kan bruke sitt system til å fatte et vedtak, men avgjørelsen må ofte baseres på avtaler og samarbeid med det andre landet for å få gjennomført en DNA-test, spesielt hvis partene i utlandet ikke samarbeider frivillig."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "4", "tittel": "Erklæring av farskap", "available": True},
            {"lov": "barnelova", "paragraf": "85", "tittel": "Godkjenning av utenlandsk farskap", "available": True},
            {"lov": "barnelova", "paragraf": "82", "tittel": "Hvilket land bestemmer over barnefordelingen", "available": True},
        ],
    },
    {
        "number": "81a",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Når kan norsk rett avgjøre hvem som er mor?",
        "kategori": "familie",
        "description": "Bor barnet eller moren i Norge? Da kan norske domstoler avgjøre saker om hvem som er barnets juridiske mor.",
        "kort_svar": "Spørsmål om hvem som er juridisk mor til et barn, kan avgjøres i Norge hvis barnet bor her, hvis moren bodde her da barnet ble født, eller hvis hun senere har flyttet hit. Dette gjelder særlig i saker om surrogati eller forveksling av barn.",
        "paragraftekst": "Ei sak om morskap kan handsamast etter kapittel 4A og § 5 tredje stykket",
        "hva_betyr_html": """<p>Hovedregelen i norsk rett er at kvinnen som føder barnet, er barnets mor. Men med moderne internasjonale forhold, og særlig bruk av surrogatiutvikling i andre land, oppstår det situasjoner hvor det må slås fast formelt hvem som er barnets mor.</p>
<p>Paragraf 81 a forteller ganske enkelt i hvilke internasjonale tilfeller Norge har lov til å ta i en slik sak. Norske myndigheter og domstoler kan behandle saken hvis: 1. Barnet bor i Norge. 2. Moren bodde i Norge da barnet ble født. 3. Moren har flyttet til Norge i ettertid.</p>
<p>Hvis ingen av disse kravene er oppfylt, og hele familien for eksempel er britiske statsborgere bosatt i London, kan ikke en norsk domstol blande seg inn i hvem som er mor, selv om de er på ferie i Norge.</p>""",
        "eksempler": [{"navn": "Ingrid", "tekst": "Ingrid og partneren hennes har brukt en surrogatmor i utlandet for å få barn. Når barnet er født, bringer de barnet til Norge, og barnet får vanlig bosted her sammen med faren sin. Norske myndigheter nekter først å anerkjenne Ingrid som mor, fordi norsk lov sier at kvinnen som fødte er mor. Ingrid ønsker å adoptere barnet eller få avklart foreldreskapet juridisk. Siden barnet nå bor i Norge, har norske domstoler myndighet til å behandle saken og finne en juridisk løsning for morskapet."}],
        "vanlige_feil": ["Å blande biologisk morskap med juridisk morskap i Norge. Avtaler om surrogati er ikke bindende i Norge, selv om de er det i landet barnet ble født i.", "Å tro at saken kan løses i Norge bare fordi man har norsk pass — man må faktisk bo (\"ha vanleg bustad\") her."],
        "hva_bor_du_html": "<p>Står du i en vanskelig internasjonal situasjon om morskap, for eksempel etter surrogati, trenger du profesjonell hjelp. Fordi norsk rett anser kvinnen som føder som mor uansett hva en utenlandsk kontrakt sier, må du gå gjennom adopsjon eller spesielle søknadsprosesser via norske myndigheter for at en annen kvinne skal bli anerkjent som juridisk mor. Start med å kontakte Barne-, ungdoms- og familiedirektoratet (Bufdir) for veiledning.</p>",
        "dumme_sporsmal": [
            {"q": "Hvorfor trenger vi egne regler om morskap i utlandet, er det ikke bare kvinnen som føder som er mor?", "a": "I Norge, ja. Men i noen land (som visse stater i USA eller Ukraina) kan en surrogatmor signere fra seg morskapet før fødselen, slik at den norske kvinnen står på den utenlandske fødselsattesten. Når familien kommer hjem til Norge, kolliderer dette med norsk lov. Da må vi ha regler som sier at Norge faktisk har lov til å rydde opp i floken."},
            {"q": "Hva betyr \"vanleg bustad\"?", "a": "Det betyr stedet der barnet eller moren faktisk bor og har sitt senter for livsinteressene sine. Å bare være på en tre måneders ferie er ikke \"vanleg bustad\"."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "2", "tittel": "Hvem som er mor til barnet", "available": True},
            {"lov": "barnelova", "paragraf": "81", "tittel": "Når kan farskap fastsettes i Norge?", "available": True},
            {"lov": "barnelova", "paragraf": "85", "tittel": "Godkjenning av utenlandsk farskap", "available": True},
        ],
    },
    {
        "number": "82",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvilket land bestemmer over barnefordelingen?",
        "kategori": "familie",
        "description": "Hvem bestemmer hvor barnet skal bo etter samlivsbrudd når familien er internasjonal? Saken kan bare gå i Norge hvis barnet bor fast her.",
        "kort_svar": "En sak om foreldreansvar, fast bosted eller samvær kan bare behandles av norske domstoler hvis barnet har fast adresse (vanlig bosted) i Norge. Hvis barnet bare er i Norge på en kort ferie eller på besøk, kan Norge bare ta en midlertidig kriseavgjørelse.",
        "paragraftekst": "Sak om foreldreansvar, flytting med barnet ut av landet, kven barnet skal bu fast saman med eller samvær kan reisast for norsk domstol dersom barnet har vanleg bustad i Noreg. Det same gjeld i sak som statsforvaltaren skal handsame etter § 55.",
        "hva_betyr_html": """<p>I internasjonale barnefordelingssaker kan foreldrene fort krangle om <em>hvor</em> rettssaken skal holdes. Mor vil kanskje ha saken i Norge fordi hun bor her, mens far vil ha saken i Spania hvor han bor.</p>
<p>Paragraf 82 gir en glassklar regel for å unngå dette kaoset: Det er barnets faste bosted som avgjør.</p>
<p>Hvis barnet har flyttet til Norge og fått det loven kaller "vanleg bustad" her, er det norske domstoler som skal avgjøre hvor barnet skal bo fast, hvem som har foreldreansvar, og hvordan samværet skal fungere. Bor barnet fast i Tyskland, er det Tyskland som skal dømme i saken. Det spiller ingen rolle om en av foreldrene gjerne vil at en norsk dommer skal se på saken.</p>
<p>Dette forhindrer at foreldre flykter til et annet land med barnet ("barnebortføring") for å få en rettssak med lover som passer dem bedre.</p>
<h3>Hva skjer i en akuttsituasjon?</h3>
<p>Noen ganger kan et barn befinne seg i Norge bare midlertidig, for eksempel på en sommerferie, og så oppstår det en alvorlig krise. Loven sier at i slike tilfeller kan norske domstoler ta en <em>midlertidig avgjørelse</em> for å beskytte barnet (for eksempel å si hvem som midlertidig skal ha omsorgen). Men den endelige, langsiktige rettssaken må uansett tas i det landet der barnet egentlig bor fast.</p>""",
        "eksempler": [{"navn": "Jonas og Eva", "tekst": "Jonas (norsk) og Eva (svensk) bor fast i Sverige med sitt felles barn. De går fra hverandre, og Jonas flytter tilbake til Norge. Jonas ønsker at barnet skal bo fast hos ham, og tar ut søksmål for en norsk domstol. Norsk domstol avviser saken og viser til § 82. Siden barnet bor fast i Sverige, må Jonas reise sak i Sverige og la en svensk domstol avgjøre spørsmålet."}],
        "vanlige_feil": ["Å tro at ditt eget norske statsborgerskap gir deg rett til en norsk rettssak. Retten bryr seg primært om hvor *barnet* har sitt faste liv.", "Å ta med seg barnet til Norge ulovlig i håp om å starte en rettssak her. Dette er barnebortføring, og domstolen vil nekte å ta saken."],
        "hva_bor_du_html": "<p>1. <strong>Ikke hold tilbake barn i feil land</strong> — Hvis du tar med barnet til Norge uten samtykke fra den andre forelderen i håp om å få en norsk domstol til å bestemme, bryter du internasjonal lov (Haag-konvensjonen). 2. <strong>Bruk advokat</strong> — Internasjonale barnefordelingssaker er ekstremt kompliserte. Før du sender papirer til noen som helst domstol, bør du ha en advokat med ekspertise i internasjonal familierett. 3. <strong>Møt til mekling</strong> — Uansett hvilket land dere er i, prøver systemet alltid å få dere til å inngå en frivillig avtale først.</p>",
        "dumme_sporsmal": [
            {"q": "Barnet er født i Norge, men har bodd fire år i USA. Kan saken gå i Norge?", "a": "Nei. Fødeland eller pass er ikke avgjørende. Etter fire år i USA har barnet \"vanlig bosted\" der, og saken må gå for en amerikansk domstol."},
            {"q": "Hva betyr \"vanleg bustad\" i praksis?", "a": "Det betyr sentrum for barnets liv. Man ser på hvor barnet går i barnehage eller skole, hvor lenge det har bodd der, og hvor barnet har sine venner og sosiale liv."},
            {"q": "Vi har signert en avtale på at en norsk domstol skal bestemme. Gjelder det?", "a": "Nei. Dere kan ikke inngå en privat avtale for å overstyre regelen om at saken tilhører barnets faste bostedsland. Barnets bosted trumfer private kontrakter mellom foreldrene."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "36", "tittel": "Hvor barnet skal bo fast", "available": True},
            {"lov": "barnelova", "paragraf": "40", "tittel": "Flytting av barnet ut av landet", "available": True},
        ],
    },
    {
        "number": "83",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Når kan NAV eller norske domstoler fastsette barnebidrag?",
        "kategori": "familie",
        "description": "Barnebidrag over landegrenser kan være komplisert. Loven bestemmer når NAV eller en norsk domstol har lov til å kreve barnebidrag.",
        "kort_svar": "Krav om barnebidrag (fostringstilskot) kan behandles i Norge av NAV eller norske domstoler hvis barnet, eller en av foreldrene, bor fast i Norge. Det kan også gjøres hvis bidragskravet er en del av en eksisterende norsk sak om farskap, bosted eller foreldreansvar.",
        "paragraftekst": "Spørsmålet om fostringstilskot kan handsamast av tilskotsfuten eller norsk domstol",
        "hva_betyr_html": """<p>Barnebidrag er penger for å dekke barnets utgifter. Når mor bor i ett land, far i et annet, og kanskje barnet i et tredje, må man vite hvem som skal sitte med kalkulatoren og beregne hvem som skal betale hva.</p>
<p>§ 83 sier at Norge har rett til å bestemme dette i to tilfeller:</p>
<p>Det første tilfellet er hvis det allerede pågår en relatert sak her. Hvis foreldrene uansett sitter i en norsk rettssal for å bestemme hvem barnet skal bo hos, eller hvem som er faren, kan domstolen like gjerne ta avgjørelsen om barnebidrag med det samme. Det er praktisk og sparer tid.</p>
<p>Det andre tilfellet handler om adresse. Hvis den som krever bidrag (oftest den barnet bor hos), barnet selv, <em>eller</em> den som skal betale bidraget, bor fast i Norge — da kan saken tas her.</p>""",
        "eksempler": [{"navn": "Lars", "tekst": "Lars er norsk og har flyttet til Spania. Ekskona og datteren på fem år bor fortsatt i Norge. Fordi barnet og mor har \"vanleg bustad\" (fast adresse) i Norge, kan mor kreve at NAV i Norge regner ut og fastsetter hvor mye Lars skal betale i barnebidrag hver måned. Det spiller ingen rolle at Lars nå bor i utlandet."}],
        "vanlige_feil": ["Å tro at man slipper barnebidrag bare fordi man flytter fra Norge.", "Å tro at utenlandske myndigheter alltid må blandes inn for å beregne bidraget. NAV kan beregne det, selv om far bor i Spania, så lenge barnet bor i Norge."],
        "hva_bor_du_html": "<p>1. <strong>Søk via NAV</strong> — Er det en internasjonal sak der en av dere bor i Norge, trenger du ikke finne ut av jussen alene. Søk om fastsettelse av bidrag gjennom NAVs nettsider. 2. <strong>Oppgi alle detaljer</strong> — Pass på at NAV får informasjon om at den andre forelderen bor i utlandet. NAV Internasjonalt har egne saksbehandlere som jobber med bidragssaker på tvers av grensene.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om faren bor i et land der inntektene er veldig lave, bruker NAV norske satser?", "a": "Når NAV beregner bidrag, bruker de den bidragspliktiges *faktiske* inntekt der vedkommende bor. Hvis faren bor i et lavkostland med lav lønn, vil bidraget regnes ut fra det han faktisk har evne til å betale, ikke ut fra en fiktiv norsk snittlønn."},
            {"q": "Kan NAV kreve inn pengene hvis faren bor i utlandet og nekter å betale?", "a": "Å *fastsette* at noen skylder penger, og å faktisk *få inn* pengene, er to forskjellige ting. Men ja, Norge har avtaler med svært mange land om gjensidig innkreving av barnebidrag, så Statens innkrevingssentral kan be myndighetene i fars land om å trekke pengene fra lønnen hans."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "70", "tittel": "Hvordan fostringstilskot (barnebidrag) beregnes", "available": True},
            {"lov": "barnelova", "paragraf": "81", "tittel": "Om fastsettelse av farskap", "available": True},
        ],
    },
    {
        "number": "83a",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Utveksling av informasjon med andre land i bidragssaker",
        "kategori": "familie",
        "description": "Nekter eksen i utlandet å oppgi inntekten sin? NAV kan samarbeide med andre land for å hente ut skatte- og inntektstall til bidragssaken.",
        "kort_svar": "NAV kan utveksle opplysninger om partenes inntekt, formue, identitet og adresse med myndighetene i andre land, forutsatt at Norge har en formell avtale med dette landet. Dette gjør det mulig å fastsette og kreve inn barnebidrag selv om en av foreldrene bor utenlands og nekter å samarbeide.",
        "paragraftekst": "Når avtaler med framand stat med heimel i § 85 andre stykket i lova her eller i bidragsinnkrevingsloven § 2 har reglar om utveksling av informasjon, kan Arbeids- og velferdsetaten utan hinder av teieplikt gi andre medlemsland opplysningar om identitet, adresse eller inntekts- og formuestilhøve for partane i ei bidragssak, eventuelt etter at opplysningane er henta etter § 70 sjuande stykket i lova her eller etter bidragsinnkrevingsloven kapittel 3.",
        "hva_betyr_html": """<p>For å regne ut riktig barnebidrag, må NAV vite nøyaktig hva begge foreldrene tjener. Når begge bor i Norge, logger NAV seg bare inn i de norske skattesystemene og finner tallene. Men hva skjer hvis far bor i Tyskland eller mor i USA?</p>
<p>Tidligere kunne dette stoppe opp hvis personen i utlandet bare sluttet å svare på brev. Paragraf 83 a gir Arbeids- og velferdsetaten (NAV) rett til å bryte sin egen taushetsplikt for å samarbeide med det andre landets myndigheter.</p>
<p>Norge kan sende informasjon om deg og saken til det andre landet, og be om å få tilbake opplysninger om den andre forelderens inntekt, adresse eller penger i banken. Regelen gjelder bare med land Norge har en avtale med (typisk gjennom Haag-konvensjonene eller nordiske avtaler).</p>
<h3>Hva skjer hvis du gjør feil?</h3>
<p>Gjemmer du deg i utlandet og nekter å sende inn inntektsbevis, vil myndighetene til slutt finne tallene dine uansett. Da mister du muligheten til å dokumentere ekstra utgifter du har (som kunne gjort bidraget lavere), og NAV fastsetter beløpet kun basert på de offisielle inntektstallene de mottar.</p>""",
        "eksempler": [{"navn": "Håkon", "tekst": "Håkon bor i Norge og har et barn. Moren til barnet har flyttet til Sverige og betaler ikke barnebidraget hun skal. Hun ignorerer alle skjemaer fra NAV om å oppgi inntekten sin. Fordi Norge og Sverige har en avtale, tar NAV kontakt med svenske myndigheter (Försäkringskassan og Skatteverket) og får hentet ut opplysninger om inntekten hennes. NAV kan da beregne et korrekt barnebidrag og be Sverige kreve det inn, helt uten at moren trenger å løfte en finger."}],
        "vanlige_feil": ["Å tro at du kan gjemme formue ved å flytte til et naboland. NAV har sterke avtaler for informasjonsutveksling med andre land.", "Å la være å svare på NAVs brev i håp om at saken dør ut. Det gjør den ikke, NAV innhenter bare tallene på egen hånd og fastsetter bidraget uten ditt innspill."],
        "hva_bor_du_html": "<p>Samarbeid med NAV. Hvis du bor i utlandet og får krav om å dokumentere inntekt, send inn lønnsslipper og skattemeldinger frivillig. Det gir deg kontroll over situasjonen, og du sikrer at NAV ikke fatter vedtak basert på gamle eller ufullstendige tall de har fått fra utlandet.</p>",
        "dumme_sporsmal": [
            {"q": "Kan NAV kreve informasjon fra absolutt alle land i verden?", "a": "Nei. Loven gjelder utelukkende land Norge har inngått en internasjonal avtale med. Men dette dekker hele Europa, USA, og mange andre store land i verden."},
            {"q": "Kan NAV sende mine norske skattetall til utlandet?", "a": "Ja. Hvis en utenlandsk myndighet prøver å fastsette barnebidrag der, og du bor i Norge, kan NAV oversende opplysningene om inntekten din til dem, slik at barnet i utlandet får riktig bidrag."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "83", "tittel": "Om når Norge kan fastsette tilskudd", "available": True},
            {"lov": "barnelova", "paragraf": "70", "tittel": "Plikt til å oppgi inntekt for barnebidrag", "available": True},
        ],
    },
    {
        "number": "83b",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvordan kreve inn en privat bidragsavtale i utlandet?",
        "kategori": "familie",
        "description": "Har du og eksen laget en privat avtale om barnebidrag, men nå bor hen i utlandet og slutter å betale? NAV kan godkjenne avtalen så pengene kan drives inn der.",
        "kort_svar": "Hvis du har en privat, skriftlig avtale om barnebidrag, og den som skal betale flytter til utlandet og slutter å betale, kan du be NAV om hjelp. NAV kan stemple (godkjenne) avtalen som tvangskraftig, noe som betyr at Norge kan be det utenlandske landet om å kreve inn pengene med tvang.",
        "paragraftekst": "Når ein part med heimel i ei avtale med framand stat ber om innkrevjing av ei avtale om tilskot etter [§ 70 første stykket, skal avtala sendast Arbeids- og velferdsetaten for godkjenning. Arbeids- og velferdsetaten skal kontrollere at vilkåra for innkrevjing av avtala etter norske reglar er oppfylte. Om vilkåra er oppfylte, skal Innkrevjingsmyndigheita gi skriftleg fråsegn om at avtala er godkjent og tvangskraftig i Noreg.",
        "hva_betyr_html": """<p>Mange foreldre velger å droppe offentlig utregning fra NAV, og skriver heller en privat kontrakt seg imellom: "Far betaler 4 000 kroner i måneden til mor".</p>
<p>Så lenge begge bor i Norge, kan man enkelt gå til NAV eller namsmannen for å kreve inn pengene hvis far slutter å betale. Men hvis far flytter til Polen, kan man ikke uten videre sende en håndskrevet, privat norsk kontrakt til polske myndigheter og forvente at de trekker ham i lønn.</p>
<p>Det § 83 b gjør, er å bygge en bro for disse private avtalene. Du sender den private avtalen til NAV (Arbeids- og velferdsetaten). NAV sjekker om avtalen er gyldig etter norske regler. Hvis den er det, gir NAV en skriftlig bekreftelse på at avtalen har "tvangskraft". Med dette offentlige beviset i hånden, kan avtalen sendes til utlandet (hvis de er med i riktig konvensjon), og myndighetene der vil kreve inn pengene for deg.</p>""",
        "eksempler": [{"navn": "Sara", "tekst": "Sara og eksmannen skrev en privat avtale for tre år siden om at han skulle betale 3 500 kr i barnebidrag. Eksmannen har nå flyttet til Tyskland og sluttet å overføre penger. Sara sender den private kontrakten til NAV Internasjonalt. NAV går gjennom papirene, bekrefter skriftlig at avtalen er bindende og oppfyller norske krav for inndriving. Deretter ber norske myndigheter de tyske myndighetene om å drive inn pengene fra eksmannens tyske bankkonto. Tyskland godtar dette fordi NAV har gitt sin garanti."}],
        "vanlige_feil": ["Å inngå kun en muntlig avtale om barnebidrag. En muntlig avtale kan aldri sendes til utlandet for tvangsinnkreving.", "Å tro at du må reise en dyr rettssak i utlandet for å få pengene. Så lenge Norge og det andre landet har en avtale, er det papirarbeid NAV og myndighetene gjør for deg."],
        "hva_bor_du_html": "<p>1. <strong>Lag alltid skriftlig avtale</strong> — Hvis dere inngår en privat avtale om barnebidrag, skriv den ned og la begge signere. 2. <strong>Søk hjelp fra NAV</strong> — Hvis betalingene stopper og personen er i utlandet, kontakt NAV Innkreving / NAV Internasjonalt. Ikke prøv å hyre en tysk eller polsk advokat på egen hånd — systemet finnes for å gjøre dette gratis for deg. 3. <strong>Ha tålmodighet</strong> — Selv om NAV stempler avtalen fort, tar det ofte måneder før saken har gått gjennom byråkratiet i mottakerlandet.</p>",
        "dumme_sporsmal": [
            {"q": "Hva skjer hvis eksen bor i et land Norge ikke har avtale med?", "a": "Da kan ikke NAV hjelpe deg via dette systemet. Regelen gjelder bare der Norge har internasjonale avtaler om innkreving (først og fremst Europa og USA). Bor eksen i et land uten slik avtale, må du hyre lokal advokat der og bruke det landets rettssystem, noe som ofte ikke lønner seg."},
            {"q": "Koster det noe å få NAV til å godkjenne avtalen?", "a": "Nei, NAV gjør denne vurderingen og skriver ut tvangskraftsbekreftelsen uten gebyr."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "70", "tittel": "Inngåelse av privat avtale om fostringstilskot", "available": True},
        ],
    },
    {
        "number": "84",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Lovvalget: Hvilket lands regler skal dommeren bruke?",
        "kategori": "familie",
        "description": "Selv om en rettssak går i Norge, er det ikke garantert at norsk lov skal gjelde. Les når dommeren skal bruke reglene i barneloven.",
        "kort_svar": "Når norske domstoler eller NAV behandler saker om farskap, morskap eller barnebidrag etter barneloven, skal de bruke norsk rett (norske regler). Unntaket er hvis Norge har forpliktet seg til noe annet i en avtale (konvensjon) med et annet land.",
        "paragraftekst": "Saker som høyrer under norsk avgjerdsmakt etter §§ 81 til 83, skal avgjerast etter norsk rett, med mindre anna følgjer av overeinskomst med annan stat.",
        "hva_betyr_html": """<p>I jussen skiller man mellom <em>hvem</em> som skal dømme (hvilket land saken går i), og <em>hva slags regler</em> de skal dømme etter (lovvalget). Det er ikke en selvfølge at en dommer i Oslo tingrett må bruke norske lover hvis saken gjelder to dansker på ferie.</p>
<p>Paragraf 84 skjærer igjennom for spesifikke saker i barneloven: Saker som gjelder farskap (§ 81), morskap (§ 81 a), og barnebidrag (§ 83) som behandles i Norge, skal bedømmes etter de norske reglene. Norsk dommer bruker norsk lov.</p>
<p>Dette er viktig fordi land har ulike regler. I noen land mister far foreldreansvaret helt ved skilsmisse, i andre land varer barnebidraget til barnet er 21 år. Ved å slå fast at norsk rett gjelder, vet alle parter hva de har å forholde seg til.</p>
<p>Den eneste haken er "med mindre anna følgjer av overeinskomst med annan stat". Dette betyr at hvis Norge har signert en internasjonal traktat (for eksempel Haag-konvensjonen) som uttrykkelig sier at saken skal vurderes etter hjemlandets lov, så gjelder den traktaten foran barneloven.</p>""",
        "eksempler": [{"navn": "Per og Sara", "tekst": "Sara er fransk statsborger, Per er norsk. De bor i Oslo, og barnet deres er født her. De går til sak om barnebidrag for en domstol i Norge. Sara mener at franske regler for barnebidrag bør brukes fordi de er mer gunstige for henne. Paragraf 84 slår fast at siden saken går for norsk rettsvesen og faller inn under de nevnte paragrafene, er det den norske barnelovens kalkulator og regler som skal brukes."}],
        "vanlige_feil": ["Å tro at du kan kreve reglene fra ditt eget hjemland bare fordi du beholder statsborgerskapet ditt mens du bor i Norge. Bor du i Norge, gjelder i utgangspunktet norsk lov for farskap og barnebidrag."],
        "hva_bor_du_html": "",
        "dumme_sporsmal": [
            {"q": "Hvorfor gjelder ikke paragraf 84 for saker om foreldreansvar og samvær (barnefordeling)?", "a": "Fordi dette er skilt ut i en egen lovparagraf (den neste, § 84 a), som er bundet av Haag-konvensjonen fra 1996. Den har et litt annet internasjonalt regelverk for barnefordeling enn det vi har for farskap og penger."},
            {"q": "Kan jeg reise sak i hjemlandet mitt i stedet, for å få de lovene der?", "a": "Kanskje, men da må du se på paragrafene 81, 82 og 83 for å se om saken din lovlig kan flyttes. Hvis for eksempel barnet har fast adresse i Norge, vil domstolene i hjemlandet ditt mest sannsynlig avvise saken og be deg reise den i Norge."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "81", "tittel": "Om norske domstoler kan ta saken", "available": True},
            {"lov": "barnelova", "paragraf": "83", "tittel": "Saker om fostringstilskot", "available": True},
        ],
    },
    {
        "number": "84a",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hvilket lands lov gjelder for foreldreansvar?",
        "kategori": "familie",
        "description": "Har barnet bodd i utlandet? Her er reglene som avgjør om det er norsk eller utenlandsk lov som gjelder for foreldreansvaret når dere flytter til Norge.",
        "kort_svar": "Norsk lov gjelder for hvem som har foreldreansvaret når barnet bor fast i Norge. Har dere flyttet til Norge fra utlandet, beholder dere vanligvis det foreldreansvaret dere hadde i det forrige landet, forutsatt at Norge har en konvensjon (avtale) med dette landet.",
        "paragraftekst": "Reglane i §§ 34, 35 og 38 gjeld for barn som har vanleg bustad i Noreg. Det same gjeld § 39 om avtalar.",
        "hva_betyr_html": """<p>Når familier flytter på tvers av landegrenser, kan det bli forvirrende å vite hvilke regler som gjelder. Barneloven har egne regler for foreldre som er gift, samboere, eller som får foreldreansvar etter dødsfall. Paragraf 84 a slår fast at disse norske reglene gjelder for alle barn som har fast adresse ("vanleg bustad") i Norge.</p>
<p>Men loven tar også hensyn til at dere kanskje har med dere juridiske rettigheter fra landet dere flyttet fra. Hvis en forelder hadde foreldreansvaret i det forrige hjemlandet, vil Norge normalt anerkjenne og videreføre dette ansvaret når barnet flytter hit. Dette forutsetter at det forrige landet er med i Haag-konvensjonen fra 1996 om beskyttelse av barn.</p>
<p>Hvis en forelder <em>ikke</em> hadde foreldreansvar i det landet barnet bodde før, får de det ikke automatisk bare fordi de krysser grensen til Norge. Norsk lov deler ikke ut nye rettigheter med tilbakevirkende kraft bare fordi dere melder flytting hit.</p>
<h3>Får jeg automatisk foreldreansvar når barnet flytter hit?</h3>
<p>Nei, ikke nødvendigvis. Hvis du flytter til Norge, og barnet tidligere bodde i et annet land, får du ikke foreldreansvar bare fordi den norske barneloven i utgangspunktet gir gifte eller samboende foreldre felles ansvar.</p>
<p>Du kan bli tildelt foreldreansvaret etter at barnet har fått vanlig bosted i Norge, men det er de faktiske omstendighetene da dere kom til landet som legges til grunn i starten.</p>""",
        "eksempler": [{"navn": "Jonas", "tekst": "Jonas og Maria har bodd i Tyskland med barnet sitt. Etter tysk lov på den tiden, hadde Maria foreldreansvaret alene. De flytter sammen til Norge. Jonas krever felles foreldreansvar umiddelbart, fordi norsk barnelov sier at samboere som får barn har felles ansvar. Paragraf 84 a sier at situasjonen de hadde i Tyskland (landet de flyttet fra) legges til grunn. Jonas får derfor ikke automatisk foreldreansvar bare ved å flytte til Norge. Han må inngå en ny avtale med Maria om felles ansvar etter de norske reglene etter at de har bosatt seg her."}],
        "vanlige_feil": ["Å tro at du får tildelt foreldreansvar automatisk i det du viser det norske passet ditt på Gardermoen.", "Å tro at foreldreansvaret fra utlandet blir ugyldig bare fordi Norge har andre standardregler.", "Å blande \"lovvalg\" (hvilke regler som gjelder) med \"verneting\" (hvilken domstol som skal dømme)."],
        "hva_bor_du_html": "<p>1. <strong>Sjekk Haag-konvensjonen</strong> — Hvis landet dere flytter fra er med i 1996-konvensjonen, er det mye enklere å få det eksisterende foreldreansvaret anerkjent. 2. <strong>Inngå ny avtale i Norge</strong> — Hvis du mangler foreldreansvar når dere kommer hit, og dere er enige om å dele det, kan dere enkelt sende inn en avtale om felles foreldreansvar til Skatteetaten (Folkeregisteret). 3. <strong>Behold utenlandske papirer</strong> — Ta vare på rettsavgjørelser eller fødselsattester fra landet dere bodde i. De er beviset på at du faktisk har foreldreansvaret.</p>",
        "dumme_sporsmal": [
            {"q": "Hva skjer hvis Norge ikke har en avtale med landet vi flyttet fra?", "a": "Da er det ikke automatisk sikkert at det utenlandske foreldreansvaret videreføres etter Haag-konvensjonen. Men norske myndigheter vil i praksis ofte gjøre en konkret vurdering for å finne den beste løsningen for barnet, og ofte vil det være å videreføre det eksisterende ansvaret."},
            {"q": "Gjelder dette også barnebidrag?", "a": "Nei, denne paragrafen gjelder spesifikt for hvem som har foreldreansvaret. Lovvalget for barnebidrag er regulert i § 84."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "34", "tittel": "Foreldreansvaret når foreldrene er eller har vært gifte", "available": True},
            {"lov": "barnelova", "paragraf": "35", "tittel": "Foreldreansvaret når foreldrene ikke er gifte", "available": True},
        ],
    },
    {
        "number": "84b",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Gjelder en utenlandsk dom om barnefordeling i Norge?",
        "kategori": "familie",
        "description": "Har du en dom fra utlandet om hvor barnet skal bo? Slik avgjør loven om dommen gjelder direkte i Norge, eller om dere må i en norsk domstol.",
        "kort_svar": "En utenlandsk dom om foreldreansvar, hvem barnet skal bo hos, samvær eller flytting gjelder direkte i Norge bare hvis Norge har en formell avtale med det aktuelle landet. Hvis en slik avtale mangler, er dommen ikke bindende i Norge.",
        "paragraftekst": "Avgjerd om foreldreansvar eller tilsvarande myndigheitsforhold, flytting med barnet ut av landet, kven barnet skal bu fast saman med eller samvær skal berre leggjast til grunn i Noreg direkte i kraft av lova når dette følgjer av overeinskomst med annan stat.",
        "hva_betyr_html": """<p>Hvis du har vært gjennom en lang og slitsom rettssak i et annet land for å få omsorgen for barnet ditt, forventer du nok at denne dommen respekteres hvis dere flytter til Norge.</p>
<p>Men Norge som land kan ikke automatisk godta alt som besluttes i utenlandske rettssaler, siden rettssystemer er svært forskjellige. Paragraf 84 b setter et strengt og klart krav: Den utenlandske dommen legges til grunn i Norge <em>kun</em> hvis dette er bestemt i en internasjonal overenskomst (konvensjon) som Norge har signert.</p>
<p>Den viktigste avtalen Norge har på dette området er Haag-konvensjonen av 1996 (pluss Europaråds- og nordiske konvensjoner). Har dommen falt i et land som er med i dette samarbeidet, vil Norge respektere den.</p>
<h3>Hva skjer hvis dommen er fra et land uten avtale?</h3>
<p>Hvis dommen din kommer fra et land uten avtale med Norge, har du i praksis ikke et rettskraftig papir her. Den andre forelderen kan da ta barnet med seg til Norge og kreve en helt ny rettssak for en norsk domstol. Den norske dommeren kan lese den utenlandske dommen for å se historikken, men er ikke bundet av den og vil avgjøre saken på nytt etter hva som er best for barnet i dag.</p>""",
        "eksempler": [{"navn": "Kari", "tekst": "Kari bor i Storbritannia og har vunnet hovedomsorgen for datteren sin i en britisk domstol. Hun og barnet flytter til Norge. Eksmannen kommer til Norge og prøver å hente barnet. Kari viser den britiske dommen til norsk politi og norske myndigheter. Fordi både Norge og Storbritannia har signert relevante konvensjoner om barnefordeling, er dommen gyldig og kan legges til grunn (\"godkjennes\") i Norge. Kari beholder omsorgen uten at saken må opp i norsk rett."}],
        "vanlige_feil": ["Å tro at en stolt og stemplet dom fra et hvilket som helst land er nok bevis i Norge. Uten en konvensjon er dokumentet ofte lite verdt.", "Å ikke sjekke om hjemlandet ditt faktisk har en konvensjon med Norge før dere melder flytting."],
        "hva_bor_du_html": "<p>1. <strong>Sjekk landlisten</strong> — Gå inn på Regjeringens eller Bufdirs nettsider og sjekk om landet dommen kommer fra, har tiltrådt Haag-konvensjonen 1996 eller tilsvarende avtaler. 2. <strong>Søk om anerkjennelse</strong> — I noen tilfeller må du søke norske myndigheter (ofte Fylkesmannen/Statsforvalteren eller domstolene) om å få dommen formelt anerkjent og gjort tvangskraftig i Norge. 3. <strong>Få hjelp fra advokat</strong> — Hvis dommen er fra et land uten avtale, må du forberede deg på at den andre forelderen kan åpne saken på nytt. Skaff en advokat med kompetanse på internasjonal barnerett.</p>",
        "dumme_sporsmal": [
            {"q": "Jeg har fått en dom i USA. Gjelder den?", "a": "USA har signert flere konvensjoner med Norge, blant annet om barnebortføring, men de ulike delstatene har ulik praksis for barnefordelingsdommer. Ofte kreves det spesielle skritt for å få en amerikansk samværsdom anerkjent direkte her. Du bør sjekke konkret for delstaten dommen kom fra."},
            {"q": "Hvis den utenlandske dommen ikke er gyldig her, har jeg ingenting jeg skulle ha sagt?", "a": "Nei. Hvis dere må ta saken på nytt i Norge, vil dommeren høre på deg og ofte se på de samme bevisene som ble brukt i utlandet. Det viktigste i Norge er \"barnets beste\", og om dommen i utlandet reflekterer det, vil Norge ofte ende på et lignende resultat — men saken må altså behandles formelt."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "82", "tittel": "Når sak om barnefordeling kan tas i Norge", "available": True},
            {"lov": "barnelova", "paragraf": "36", "tittel": "Hvor barnet skal bo fast", "available": True},
        ],
    },
    {
        "number": "85",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Blir utenlandsk farskap godkjent i Norge?",
        "kategori": "familie",
        "description": "Hvis et farskap eller medmorskap ble avgjort i utlandet, er det vanligvis gyldig også her i landet. Lær mer om hvordan dette fungerer i praksis.",
        "kort_svar": "Et farskap eller medmorskap som er lovlig fastsatt etter reglene i et annet land, blir automatisk godkjent som gyldig i Norge. Men hvis noen bestrider farskapet med en norsk DNA-test og går til domstolen her, kan det utenlandske farskapet bli endret.",
        "paragraftekst": "Fylgjer farskapen eller medmorskapen til eit barn beinveges av utanlandsk lov som skal nyttast etter rettsreglane i vedkomande land, skal dette leggjast til grunn i Noreg, så lenge anna ikkje er fastsett etter §§ 6 og 7.",
        "hva_betyr_html": """<p>Hvert år flytter mennesker til Norge med barn som ble født i andre land. På fødselsattesten fra hjemlandet står det som regel navnet på faren eller medmoren. Paragraf 85 sier at Norge stoler på disse dokumentene.</p>
<p>Norge legger direkte til grunn at farskapet er gyldig, forutsatt at det fulgte det aktuelle landets lover da det ble registrert. Dette gjelder uansett om mannen var gift med moren (pater est-regelen) eller om han erkjente farskapet på et kontor i utlandet.</p>
<p>Sikkerhetsventilen her er paragraf 6 og 7 i barneloven, som handler om endring av farskap. Hvis det oppstår tvil, kan faren, moren, eller barnet gå til en norsk domstol og kreve DNA-test. Hvis DNA-testen beviser at den utenlandske mannen <em>ikke</em> er faren, kan den norske domstolen slette farskapet, selv om det opprinnelig ble fastsatt i utlandet.</p>
<p>Regjeringen har også lov til å lage egne, detaljerte regler (forskrifter) eller egne avtaler med andre land for spesielle tilfeller av farskap og medmorskap.</p>""",
        "eksempler": [{"navn": "Ali", "tekst": "Ali ble født i Tyrkia, og foreldrene var gift der da han ble født. Etter tyrkisk lov er mannen da registrert som faren. Familien flytter til Norge når Ali er fire år. Folkeregisteret og NAV i Norge registrerer ektemannen som far automatisk. Norske myndigheter krever ikke at de skal ta en ny norsk farskapstest eller erklæring, fordi det utenlandske farskapet var gyldig opprettet etter tyrkisk lov."}],
        "vanlige_feil": ["Å tro at du må bekrefte et farskap på nytt i Norge hvis du er gift og flytter hit fra utlandet med barnet.", "Å tro at surrogatikontrakter automatisk omfattes av denne enkle regelen. Barn født av surrogatmor i utlandet har helt spesielle regler og krever mye papirarbeid for å få foreldreskapet godkjent i Norge."],
        "hva_bor_du_html": "<p>1. <strong>Lever dokumentasjon</strong> — Når du flytter til Norge, ta med original, stemplet (gjerne med apostille-stempel) fødselsattest eller bekreftelse på farskap fra hjemlandet. 2. <strong>Lever til Folkeregisteret (Skatteetaten)</strong> — Du melder inn det utenlandske farskapet til Folkeregisteret i forbindelse med innflytting. De registrerer relasjonen i de norske systemene. 3. <strong>Mistenker du feil far?</strong> — Hvis du har flyttet til Norge og tror at farskapet fastsatt i utlandet er feil, kan du bestille DNA-analyse og reise sak for en norsk tingrett.</p>",
        "dumme_sporsmal": [
            {"q": "Hva om mannen ble tvunget til å erklære farskapet i utlandet?", "a": "Hvis farskapet er åpenbart uriktig, eller ble oppnådd ved tvang i strid med grunnleggende norske verdier, kan norske myndigheter nekte å godkjenne det. Det enkleste er å kreve saken endret via DNA-test i Norge."},
            {"q": "Gjelder dette for medmødre også?", "a": "Ja. Hvis dere er to kvinner som fikk medmorskapet gyldig og lovlig fastsatt i et annet land, anerkjennes det i utgangspunktet på lik linje i Norge."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "4", "tittel": "Erklæring av farskap eller medmorskap i Norge", "available": True},
            {"lov": "barnelova", "paragraf": "6", "tittel": "Endring av farskap ved domstolene", "available": True},
            {"lov": "barnelova", "paragraf": "81", "tittel": "Når Norge kan behandle en sak om farskap", "available": True},
        ],
    },
    {
        "number": "85a",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Henting av opplysninger fra Folkeregisteret",
        "kategori": "familie",
        "description": "Folkeregisteret har taushetsplikt, men de kan dele nødvendige opplysninger med myndighetene for å avklare farskap, barnebidrag eller foreldreansvar.",
        "kort_svar": "Myndigheter som håndterer saker i barneloven, for eksempel domstoler, NAV eller tilskuddsfogden, har rett til å få de opplysningene de trenger fra Folkeregisteret. Dette gjelder selv om informasjonen egentlig er taushetsbelagt.",
        "paragraftekst": "Folkeregistermyndigheita skal, utan hinder av teieplikt, gje dei opplysingane som er naudsynte for utføring av oppgåver etter lova her.",
        "hva_betyr_html": """<p>I Norge beskyttes informasjonen om hvor du bor, sivilstatus og familierelasjoner av taushetsplikt gjennom Folkeregisteret (Skatteetaten). Du skal slippe at hvem som helst kan ringe inn og sjekke hvem du er i familie med.</p>
<p>Men når det gjelder barn, er det helt nødvendig for staten å ha korrekte opplysninger. Paragraf 85 a er en praktisk arbeidsregel for de som jobber i stat og kommune. Hvis for eksempel NAV trenger å vite hvor faren bor for å kunne kreve inn barnebidrag, eller hvis en domstol skal innkalle til en sak om foreldreansvar, gir denne paragrafen dem en "nøkkel" til å se forbi taushetsplikten.</p>
<p>De kan bare hente ut de opplysningene som faktisk er nødvendige for oppgaven de skal gjøre. De kan ikke rote rundt i livene deres uten grunn.</p>""",
        "eksempler": [{"navn": "Anne", "tekst": "Anne krever at barnebidraget fra eksmannen Petter settes opp. Petter svarer ikke på brev, og Anne vet ikke hvor han har flyttet. NAV, som behandler kravet, bruker paragraf 85 a til å slå opp Petter i Folkeregisteret. De finner hans nye, skjulte adresse og hans sivilstatus. De kan dermed behandle bidragssaken videre, uten at Petter kan stoppe dem ved å henvise til at adressen er privat."}],
        "vanlige_feil": ["Å tro at du kan unndra deg farskap eller barnebidrag ved å be Folkeregisteret hemmeligholde informasjonen din. Barnets rettigheter trumfer taushetsplikten her."],
        "hva_bor_du_html": "<p>Som privatperson er det ikke noe spesielt du trenger å foreta deg på grunn av denne paragrafen. Det er en regel for byråkratene. Men husk at du alltid er pliktig til å melde adresseendringer og endringer i sivilstatus til Folkeregisteret uansett. Hvis du oppgir feil opplysninger dit, vil domstolen og NAV også jobbe ut ifra de feilaktige opplysningene, noe som kan gå utover saken din.</p>",
        "dumme_sporsmal": [
            {"q": "Får eksen min tilgang til den hemmelige adressen min nå?", "a": "Nei. Denne paragrafen gir *myndighetene* (Folkeregistermyndigheten) lov til å dele infoen med *myndighetene* (NAV/Domstolen). Hvis du bor på hemmelig/sperret adresse (\"kode 6\" eller \"kode 7\" på grunn av trusler), har NAV strenge systemer for å sørge for at eksen din aldri ser adressen på dokumentene de sender ut."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "1", "tittel": "Fødselsmelding og Folkeregisteret", "available": True},
        ],
    },
    {
        "number": "86",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Regjeringens rett til å lage forskrifter",
        "kategori": "familie",
        "description": "Selve barneloven dekker de store linjene. Denne paragrafen gir regjeringen lov til å lage detaljerte praktiske regler for hvordan ting skal gjøres.",
        "kort_svar": "Denne paragrafen gir Kongen (regjeringen) tillatelse til å lage detaljerte bestemmelser, såkalte forskrifter. Forskriftene fungerer som bruksanvisninger for hvordan barneloven skal fungere i praksis.",
        "paragraftekst": "Kongen kan gje dei forskrifter som trengst til gjennomføring av lova.",
        "hva_betyr_html": """<p>En lov vedtatt av Stortinget kan ikke inneholde alle små detaljer — da ville boken blitt umulig å lese. Stortinget bestemmer de store linjene, for eksempel at "barnebidrag skal betales".</p>
<p>Paragraf 86 delegerer makt. Den sier at regjeringen kan skrive de mer detaljerte "forskriftene". En forskrift er juridisk bindende på samme måte som en lov, men kan endres raskere fordi det gjøres i et regjeringsmøte, i stedet for å måtte stemmes over på Stortinget.</p>
<p>Forskriftene bestemmer for eksempel helt presist hvilket skjema en lege skal fylle ut på sykehuset, eller nøyaktig hvilken matematisk formel NAV skal bruke når de regner ut barnebidrag.</p>""",
        "eksempler": [{"navn": "Forskriften om barnebidrag", "tekst": "Stortinget har i barneloven bestemt at foreldre har forsørgerplikt. Gjennom paragraf 86 har regjeringen gitt Barne- og familiedepartementet lov til å fastsette den detaljerte \"Forskrift om fastsetjing og endring av fostringstilskot\". Her står de nøyaktige prosentsatsene som bestemmer om du får 10 % eller 15 % samværsfradrag på bidraget ditt, avhengig av hvor mange dager i måneden du har barnet."}],
        "vanlige_feil": ["Å tro at forskrifter bare er \"retningslinjer\" du kan velge å se bort fra. En forskrift har akkurat samme styrke som loven den hører til."],
        "hva_bor_du_html": "<p>Du skal som regel ikke forholde deg direkte til forskrifter; det er det NAV, sykehusene, Folkeregisteret og domstolene som gjør. Men hvis du lurer på utregninger eller tekniske detaljer i barnebidraget, må du gjerne sjekke \"forskrift om fostringstilskot\" på Lovdata — der finner du de virkelige regnestykkene.</p>",
        "dumme_sporsmal": [
            {"q": "Hvorfor kalles det \"Kongen\" i lovteksten? Sitter kong Harald og skriver forskrifter?", "a": "Nei. Når loven sier \"Kongen\", betyr det regjeringen (\"Kongen i statsråd\"). I praksis er det statsråden (ministeren) for Barne- og familiedepartementet som utarbeider disse reglene og legger dem frem."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "1", "tittel": "Regler om fødselsmelding (som styres av forskrifter)", "available": True},
            {"lov": "barnelova", "paragraf": "70", "tittel": "Hvordan fostringstilskuddet beregnes (der formlene står i en forskrift)", "available": True},
        ],
    },
    {
        "number": "87",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Når loven begynte å gjelde",
        "kategori": "familie",
        "description": "Dette er en rent formell paragraf som bestemte fra hvilken dato barneloven trådte i kraft. Loven erstattet tidligere eldre lover fra 1956.",
        "kort_svar": "Barneloven trådte i kraft den datoen Kongen (regjeringen) bestemte. Loven ble vedtatt i 1981, og ble satt i kraft 1. januar 1982.",
        "paragraftekst": "Lova her tek til å gjelde frå den tid Kongen fastset.​1",
        "hva_betyr_html": """<p>Når Stortinget vedtar en ny lov, begynner den sjelden å gjelde samme dag. Sykehus, politi, domstoler og NAV må ha tid til å oppdatere datamaskinene sine, trykke nye skjemaer og lære opp de ansatte.</p>
<p>Derfor er det standard å skrive i en lov at regjeringen ("Kongen") får bestemme nøyaktig hvilken dato loven trykkes på startknappen. For denne spesifikke barneloven skjedde oppstarten den 1. januar 1982. Den samlet da de gamle reglene for barn født i og utenfor ekteskap til én felles barnelov.</p>
<p>Dette er en "sovende" paragraf i dag, men den var helt nødvendig da loven ble innført.</p>""",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "<p>Ingenting. Dette er historie, og paragrafen har ingen praktisk betydning for ditt foreldreskap eller barnebidrag i dag.</p>",
        "dumme_sporsmal": [
            {"q": "Kommer det en ny barnelov snart?", "a": "Det jobbes kontinuerlig med endringer i barneloven. En helt ny barnelov har vært foreslått, og vedtas og innføres gradvis. Når en helt ny lov trer i kraft, vil den gamle barneloven (fra 1981) slettes, og den nye får en tilsvarende paragraf om når den skal begynne å gjelde. Denne prompten er oppdatert til 2026-situasjonen."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "88", "tittel": "Hva med barn født før 1982?", "available": True},
            {"lov": "barnelova", "paragraf": "89", "tittel": "Endringer i andre lover", "available": True},
        ],
    },
    {
        "number": "88",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Hva med barn som er født før 1982?",
        "kategori": "familie",
        "description": "Hva skjer med rettighetene til et barn født i 1975? Barneloven gjelder for dem også, men noen gamle avtaler respekteres fortsatt.",
        "kort_svar": "Barneloven gjelder også for barn født før 1. januar 1982. Unntaket er at et farskap som ble bestemt etter gamle regler fra før 1982, fremdeles er gyldig. Også gamle avtaler om foreldreansvar og samvær holdes i live, inntil de eventuelt blir oppdatert.",
        "paragraftekst": "Lova gjeld også barn som er født før lova tek til å gjelde. Frå dette er gjort fylgjande unntak:",
        "hva_betyr_html": """<p>Da den "nye" barneloven kom i 1982, oppstod et praktisk problem: Hva skjer med de hundretusenvis av barna som allerede fantes? Skulle foreldrene fylle ut papirene på nytt?</p>
<p>Paragraf 88 slår fast at alle barn, uansett hvor gamle de er, er dekket av barneloven. Men det gjelder noen praktiske unntak for ikke å skape kaos:</p>
<p>For det første: Hvis noen ble fastslått å være far etter de gamle lovene (for eksempel "lov om born utanom ekteskap" fra 1956), så forblir han far under den nye barneloven. Ingen trengte å signere på nytt i 1982.</p>
<p>For det andre: Avtaler eller dommer om samvær, barnebidrag eller hvem barnet bodde hos fra før 1982, gjelder fremdeles. Domstolen nullstilte ikke gamle avtaler. Men hvis du ønsker å <em>endre</em> en slik gammel avtale i dag, skal du bruke dagens regler i barneloven.</p>""",
        "eksempler": [{"navn": "Arne", "tekst": "Arne er født i 1978. Foreldrene hans var ikke gift, og faren erklærte farskapet under den gamle 1956-loven. I 2026 lurer Arne på om han har krav på å få vite navnet på faren i henhold til dagens barnelov. Ja, barneloven gjelder for ham. Det opprinnelige farskapet som ble etablert i 1978 er fortsatt gyldig i statens øyne. Skulle Arne i voksen alder oppdage at denne mannen likevel ikke var hans biologiske far, må han reise en farskapssak for å endre dette etter dagens regler (barneloven § 6)."}],
        "vanlige_feil": ["Å tro at du ikke omfattes av moderne regler (for eksempel om retten til å vite hvem biologisk far er) bare fordi du ble født på 60- eller 70-tallet.", "Å tro at gamle barnebidragsavtaler er låst for alltid. Du kan kreve dem endret etter dagens regler hvis vilkårene har forandret seg."],
        "hva_bor_du_html": "<p>Ingenting, med mindre du står i en helt spesiell arve- eller farskapssak knyttet til en sak fra før 1982. Da må du forholde deg til dagens domstoler og dagens barnelov.</p>",
        "dumme_sporsmal": [
            {"q": "Har de som ble født før 1982 dårligere rettigheter?", "a": "Tidligere (mange tiår siden) var det forskjell på barn født i ekteskap (ekte barn) og utenfor ekteskap (uekte barn), særlig når det gjaldt arv. Hele poenget med 1981-barneloven var å fjerne disse skillene helt. I dag har alle nøyaktig samme rettigheter, uavhengig av om de er født i 1960 eller 2025."},
            {"q": "Gjelder barnebidragsavtalen fra 1979 fortsatt?", "a": "Ja, hvis barnet fremdeles mottar utvidet barnebidrag (noe som er ekstremt usannsynlig siden personen vil være over 40 år gammel i dag), ville den gamle avtalen i teorien vært i live til noen krevde den endret."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "6", "tittel": "Endring av farskap for domstolene", "available": True},
            {"lov": "barnelova", "paragraf": "87", "tittel": "Når loven startet", "available": True},
            {"lov": "barnelova", "paragraf": "42", "tittel": "Barnets rett til samvær", "available": True},
        ],
    },
    {
        "number": "89",
        "lov": "barnelova", "lov_display": "Barnelova",
        "title": "Endringer i andre lover",
        "kategori": "familie",
        "description": "En ren teknisk paragraf. Da barneloven ble innført i 1981, måtte lovgiveren slette gamle lover for å unngå at de kræsjet.",
        "kort_svar": "Paragrafen er et teknisk ryddeverktøy. Den sørget for at eldre lover som kolliderte med den nye barneloven, ble opphevet eller endret da loven trådte i kraft.",
        "paragraftekst": "Frå den tid lova tek til å gjelde, vert gjort slike brigde i andre lover: – – –",
        "hva_betyr_html": """<p>Juridisk ryddejobb. Før barneloven kom i 1981, hadde Norge to hovedlover for barn: én lov for barn født innenfor ekteskap, og én lov for barn født utenfor ekteskap. Fordi poenget med den nye barneloven var å gi alle barn samme rettigheter i én samlet lov, måtte de to gamle lovene (fra 1956) kastes i søpla.</p>
<p>Paragraf 89 er mekanismen som formelt strøk de gamle lovene ut av det norske lovverket, slik at de ikke lenger fantes. I tillegg inneholdt den en liste med småord som ble oppdatert i en rekke andre lover for at alt skulle henge sammen.</p>
<p>Paragrafen har ingen betydning for ditt liv i dag.</p>""",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "<p>Du skal bare overse denne paragrafen.</p>",
        "dumme_sporsmal": [
            {"q": "Hvorfor er paragrafen så kort i lovteksten?", "a": "I den opprinnelige utskriften av loven i 1981 var dette en lang paragraf full av punkter som sa \"I lov X strykes ordet Y\". Når disse endringene faktisk ble utført i de andre lovene i 1982, ble den detaljerte teksten fjernet fra lovboken for å spare plass, siden ryddejobben var ferdig. Derfor står det bare \"---\" (bindestreker) i selve loven i dag."},
        ],
        "related": [
            {"lov": "barnelova", "paragraf": "87", "tittel": "Ikrafttredelse av loven", "available": True},
            {"lov": "barnelova", "paragraf": "88", "tittel": "Overgangsregler for de som ble født før 1982", "available": True},
        ],
    },
]
