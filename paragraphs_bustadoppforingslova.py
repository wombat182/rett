# -*- coding: utf-8 -*-
"""Bustadoppføringslova — paragraf-data for Rettsregel."""

LOV = "bustadoppforingslova"
LOV_DISPLAY = "Bustadoppføringslova"
KAT = "bolig"

def _p(*args):
    return "".join(f"<p>{a}</p>" for a in args)

PARAGRAPHS = [
{
    "number": "1",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Loven gjelder når du skal bygge ny bolig",
    "description": "Skal du bygge nytt hus, hytte eller kjøpe bolig under oppføring? Denne loven sikrer rettighetene dine i møte med utbygger.",
    "kort_svar": "Bustadoppføringslova er loven som gjelder når du som privatperson gjør en avtale med en proff utbygger om å bygge en helt ny bolig eller hytte. Den gjelder også hvis du kjøper en ny bolig som ikke er ferdig bygget ennå (prosjektbolig), eller hvis du gjør en total ombygging av et eldre hus.",
    "paragraftekst": "Lova gjeld avtalar mellom entreprenør og ein forbrukar om oppføring av ny eigarbustad. Oppføring av ny eigarbustad omfattar òg oppføring av fritidshus. Eigarseksjon vert rekna som eigarbustad. Full ombygging skal reknast likt med oppføring.",
    "hva_betyr_html": _p(
        "Paragrafen forteller i hvilke situasjoner denne loven gjelder. Loven er skrevet for å beskytte deg når du skal gjøre en av ditt livs største investeringer: å bygge et nytt hjem.",
        "Loven gjelder når du eier en tomt og leier inn et firma for å bygge et hus for deg — både selve huset og arbeid som henger direkte sammen med det, for eksempel graving av grunnmur eller rørleggerarbeid.",
        "Loven gjelder også det vi kaller «prosjektboliger» — når du kjøper både tomt og hus samlet fra en utbygger, men huset ikke er bygget ferdig den dagen du skriver under på kontrakten.",
        "Loven gjelder dessuten når du bygger hytte («fritidshus»), og når du river alt utenom reisverket på et gammelt hus og bygger det helt opp igjen («full ombygging»). Skal du derimot bare pusse opp badet eller bytte tak, er det håndverkertjenesteloven som gjelder.",
    ),
    "eksempler": [{"navn": "Jonas", "tekst": "Jonas har kjøpt en tomt på fjellet og inngår en avtale med et lokalt byggefirma om å sette opp en nøkkelferdig hytte. Siden han bygger et nytt fritidshus med et profesjonelt firma, er kontrakten hans regulert av bustadoppføringslova. Det betyr at byggefirmaet må følge strenge regler for garantier, tidsfrister og feil."}],
    "vanlige_feil": [
        "Blande sammen håndverkertjenesteloven og bustadoppføringsloven når man skal gjøre store renoveringer",
        "Tro at loven gjelder når man kjøper et splitter nytt hus som allerede er ferdig bygget (da gjelder avhendingsloven)",
        "Glemme at hyttedrømmen også er beskyttet av lovens strenge garantikrav",
    ],
    "hva_bor_du_html": _p(
        "Når du skal signere en kontrakt for bygging av bolig eller hytte, sjekk alltid hvilken lov som er nevnt. Entreprenøren har ikke lov til å velge en annen lov for å slippe unna ansvaret sitt.",
        "Bruk alltid standardkontrakter. Norsk Standard (NS 3425) er tilpasset bustadoppføringslova og brukes ofte ved bygging på egen tomt.",
    ),
    "dumme_sporsmal": [
        {"q": "Gjelder loven hvis jeg leier inn folk svart?", "a": "Nei. Jobber utført svart gir deg ingen juridisk trygghet hvis noe går galt."},
        {"q": "Jeg kjøper en leilighet i et borettslag som skal bygges. Gjelder loven?", "a": "Ja. Loven gjelder også for borettslagsleiligheter og eierseksjoner under oppføring."},
        {"q": "Hva om jeg bygger huset selv sammen med familien?", "a": "Hvis du er selvbygger og bygger ditt eget hus, gjør du ikke en avtale med en entreprenør. Da gjelder ikke loven. Leier du inn en rørlegger, gjelder håndverkertjenesteloven for akkurat det arbeidet."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "1a", "tittel": "Gjelder også for nye borettslagsleiligheter", "available": True},
        {"lov": LOV, "paragraf": "2", "tittel": "Hvem regnes som forbruker?", "available": True},
        {"lov": LOV, "paragraf": "3", "tittel": "Loven kan ikke endres til din ulempe", "available": True},
    ],
},

{
    "number": "1a",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Gjelder også for nye borettslagsleiligheter",
    "description": "Kjøper du en ny bolig i et borettslag under oppføring? Da beskytter denne paragrafen deg på lik linje med selveiere.",
    "kort_svar": "Kjøper du en leilighet under oppføring i et borettslag, har du nøyaktig de samme rettighetene og beskyttelsene som de som kjøper selveierbolig. Kontrakten din skal tydelig vise hva du betaler i kontanter (innskudd) og hva som er din del av borettslagets fellesgjeld.",
    "paragraftekst": "Reglane om rett til fast eigedom med eigarbustad gjeld tilsvarande for avtale mellom forbrukar og bustadbyggjelag om rett til bustad knytt til andel i burettslag, dersom arbeid som er omfatta av avtalen ikkje er fullført på avtaletida. Avtalen skal opplyse om kontantvederlag, andel fellesgjeld i burettslaget og den samla summen av desse beløpa.",
    "hva_betyr_html": _p(
        "Paragrafen slår fast at selskapsformen boligen bygges i, ikke skal ha noe å si for rettighetene dine. Enten du kjøper et prosjektert rekkehus som selveier, eller en leilighet i sjuende etasje i et nytt borettslag, er du dekket av loven.",
        "Økonomien i et borettslag er delt i to: du betaler et innskudd (kontanter), og i tillegg overtar du en andel av den gjelden borettslaget har tatt opp (fellesgjeld). Loven krever at utbygger er krystallklar i kontrakten — du skal se nøyaktig hva innskuddet er, hva din del av fellesgjelden er, og hva totalprisen faktisk blir.",
        "Paragrafen sier også at styret i borettslaget kan klage til utbygger på feil i fellesarealene på vegne av alle. Du trenger ikke krangle med utbyggeren om oppgangen alene.",
    ),
    "eksempler": [{"navn": "Sara", "tekst": "Sara kjøper en 3-roms leilighet i et boligprosjekt som borettslag. I kontrakten takket være § 1a: innskudd 1 500 000 kr, andel fellesgjeld 2 500 000 kr, totalpris 4 000 000 kr. Balkongene er ikke levert i henhold til tegningene — styret sender inn klage og krever erstatning, slik at Sara slipper å gjøre det på egenhånd."}],
    "vanlige_feil": [
        "Å bare se på innskuddet, og overse hvor mye fellesgjeld som følger med leiligheten",
        "Å tro at man som beboer selv må fikse og reklamere på feil utenfor sin egen inngangsdør",
    ],
    "hva_bor_du_html": _p(
        "Se på feltet for «Totalpris» i kontrakten og salgsoppgaven. Det er dette tallet som avgjør om boligen er et godt kjøp.",
        "Sjekk også hvor lenge borettslaget har avdragsfrihet på fellesgjelden — mange nye prosjekter har 5–10 års avdragsfrihet, og når den perioden er over, vil de månedlige felleskostnadene stige kraftig.",
    ),
    "dumme_sporsmal": [
        {"q": "Hva skjer med fellesgjelden hvis naboen ikke betaler sin del?", "a": "De fleste nye borettslag er med i en sikringsordning som dekker manglende innbetalinger. Spør utbygger om borettslaget er tilknyttet en slik ordning."},
        {"q": "Kan jeg klage hvis parketten min inne i leiligheten har skader?", "a": "Ja. Feil inne i din leilighet er ditt ansvar å klage på. Styrets rolle gjelder kun fellesområdene som ganger, tak og heis."},
        {"q": "Når er boligen egentlig min?", "a": "Boligen er offisielt overført til deg når du har signert overtakelsesprotokollen og andelen er registrert i ditt navn."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "1", "tittel": "Hva loven gjelder for", "available": True},
        {"lov": LOV, "paragraf": "1b", "tittel": "Tilsvarende regler for eierseksjonssameier", "available": True},
        {"lov": LOV, "paragraf": "12", "tittel": "Utbyggers plikt til å stille garanti", "available": True},
    ],
},
{
    "number": "1b",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Sameiets rett til å klage på fellesarealer",
    "description": "Kjøper du leilighet i et nytt sameie? Styret kan klage til utbygger på feil i fellesområdene på vegne av alle.",
    "kort_svar": "Hvis du kjøper en prosjektleilighet i et eierseksjonssameie, og det er byggefeil i fellesarealene (heisen, bakgården eller taket), har styret i sameiet rett til å klage og kreve retting fra utbyggeren.",
    "paragraftekst": "Styret i eit eigarseksjonssameige kan gjere gjeldande krav som knyter seg til fellesareal etter reglane i eierseksjonsloven § 60.",
    "hva_betyr_html": _p(
        "Paragrafen gjør det enkelt: Styret i sameiet har fullmakt til å ta kampen med utbyggeren på vegne av alle som eier leiligheter der. Styret representerer hele bygget samlet.",
        "Hvis gulvet inne hos deg knirker, er det din egen avtale med utbyggeren som gjelder — du må selv klage. Men hvis heisen stopper hele tiden, asfalten sprekker opp, eller det lekker i garasjekjelleren, er dette fellesarealer som styret håndterer.",
    ),
    "eksempler": [{"navn": "Marius", "tekst": "Marius kjøper en ny selveierleilighet. Etter noen måneder begynner malingen i trappeoppgangen å flasse av. Marius sender en e-post til sameiets styre, som tar saken videre og krever at entreprenøren fikser malingen på sin regning."}],
    "vanlige_feil": [
        "Å prøve å forhandle om fellesareal-feil på egen hånd ved sin egen ettårsbefaring",
        "Å tro at feil på taket ikke angår deg fordi du bor i første etasje",
    ],
    "hva_bor_du_html": _p(
        "Når du overtar leiligheten, fokuser på det som skjer innenfor din egen inngangsdør. Men følg nøye med i gangene, uteområdene og parkeringskjelleren. Ta bilde av alt som ser uferdig ut og send det til styret.",
        "Pass på at dere velger et aktivt styre tidlig, slik at klagefristene mot utbygger ikke løper ut mens bygget står uten formell ledelse.",
    ),
    "dumme_sporsmal": [
        {"q": "Hva regnes egentlig som fellesareal?", "a": "Som hovedregel er alt utenfor din inngangsdør fellesareal: tak, yttervegger, trappeoppgang, heis, felles utearealer og sykkelboder."},
        {"q": "Kan utbygger nekte å snakke med styret?", "a": "Nei. Paragraf 1b gir styret formell rettighet til å fremme disse kravene. Utbygger er pliktig til å forholde seg til styret."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "1a", "tittel": "Tilsvarende rettigheter for borettslag", "available": True},
        {"lov": LOV, "paragraf": "1", "tittel": "Hva loven gjelder for", "available": True},
    ],
},

{
    "number": "2",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Hvem regnes som forbruker?",
    "description": "Gjelder loven for deg? Ja, så lenge du bygger for å bo der privat og utbyggeren er profesjonell. Lær grensen mellom proff og privat.",
    "kort_svar": "For å få beskyttelse av denne loven må to ting være på plass: Du må opptre som privatperson (forbruker), og utbyggeren eller håndverkerfirmaet må opptre som en profesjonell næringsdrivende.",
    "paragraftekst": "Som forbrukar vert rekna ein fysisk person som ikkje hovudsakleg handlar som ledd i næringsverksemd. Lova gjeld berre dersom entreprenøren har gjort avtalen som ledd i næringsverksemd.",
    "hva_betyr_html": _p(
        "Hele poenget med bustadoppføringsloven er å rette opp ubalansen som oppstår når en vanlig person, som kanskje bygger ett hus i hele sitt liv, skal skrive kontrakt med et firma som bygger hundre hus i året.",
        "For at loven skal gjelde for deg må du være en fysisk person som ikke kjøper huset for å drive business. Bygger du for å bo der selv, eller hytte for familien, er du i lovens øyne en forbruker — selv om du kanskje skal leie ut hytta noen uker på Airbnb.",
        "På den andre siden av bordet må utbyggeren være en proff næringsdrivende. Kommuner eller foreninger som bygger boliger for salg mot betaling, regnes også som proffe utbyggere.",
    ),
    "eksempler": [{"navn": "Håkon", "tekst": "Håkon eier en stor tomt og bestemmer seg for å bygge en tomannsbolig. Den ene halvdelen skal han bo i selv, den andre leie ut. Han leier inn «Lokal Bygg AS». Selv om Håkon skal drive utleie, bygger han i hovedsak privat for seg selv. Han regnes som forbruker, og kontrakten styres av bustadoppføringslova."}],
    "vanlige_feil": [
        "Å kjøpe hytta gjennom sitt eget investeringsfirma (AS) i stedet for på seg selv privat — da mister man alt forbrukervern",
        "Å inngå avtale med naboen som bygger hobbyprosjekter på si, og forvente at loven dekker feil automatisk",
        "Proffe utbyggere som bruker kontrakter laget for næringsdrivende mot en privatkunde",
    ],
    "hva_bor_du_html": _p(
        "Pass på at kontrakten inngås mellom deg som privatperson (med ditt navn og personnummer), og entreprenøren (med selskapsnavn og organisasjonsnummer).",
        "Ikke la utbygger bruke standardkontrakter ment for proff-markedet (som NS 8405) — som forbruker skal kontrakten bygge på NS 3425 eller NS 3427, eller det skal stå at bustadoppføringslova gjelder.",
    ),
    "dumme_sporsmal": [
        {"q": "Jeg skal bygge hus for å selge det umiddelbart og tjene penger. Er jeg forbruker da?", "a": "Det er en gråsone. Driver du aktivt og systematisk med kjøp, bygging og salg, kan domstolene vurdere deg som profesjonell. Da mister du lovens beskyttelse."},
        {"q": "Hva hvis byggefirmaet går konkurs underveis?", "a": "At du regnes som forbruker sikrer at entreprenøren skal ha stilt en bankgaranti (§ 12). Selv om de går konkurs, har du lovfestet rett på disse pengene."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "1", "tittel": "Hva loven gjelder for", "available": True},
        {"lov": LOV, "paragraf": "3", "tittel": "Loven kan ikke endres til din ulempe", "available": True},
    ],
},
{
    "number": "3",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Loven er på din side og kan ikke endres til din ulempe",
    "description": "Kan utbygger putte inn egne regler i kontrakten som fjerner dine rettigheter? Nei. Bustadoppføringsloven er ufravikelig.",
    "kort_svar": "Bustadoppføringsloven er ufravikelig. Det betyr at ingen utbygger, entreprenør eller håndverker kan skrive en kontrakt som gir deg dårligere rettigheter enn de som står i loven. Enhver slik linje i kontrakten er ugyldig. I tillegg har du rett til å kreve at avtalen gjøres skriftlig.",
    "paragraftekst": "Det kan ikkje avtalast eller gjerast gjeldande vilkår som er dårlegare for forbrukaren enn det som følgjer av føresegnene i lova her. Partane kan krevje at avtalen vert sett opp skriftleg.",
    "hva_betyr_html": _p(
        "Dette er kanskje den viktigste setningen i hele lovboken når du skal bygge hus. Utbyggere har ofte lange, kompliserte kontrakter. Hvis noe i den kontrakten fjerner rettigheter du har etter bustadoppføringsloven, gjelder det rett og slett ikke.",
        "Eksempel: Loven sier du har 5 års klagefrist på et nytt hus. Hvis entreprenøren skriver i kontrakten at «Kjøper godtar at det gis maksimalt 2 års garanti», er det brudd på paragraf 3. Da gjelder 5 år, uansett hvor mange ganger du har signert.",
        "De kan derimot gi deg bedre vilkår enn loven sier — for eksempel 10 års garanti. Loven er et gulv for rettighetene dine, ikke et tak.",
        "Videre sier paragrafen at du når som helst kan kreve å få avtalen skriftlig. Selv om dere bare ble enige over en kaffekopp, kan og bør du kreve dette inn i et papir med signaturer.",
    ),
    "eksempler": [{"navn": "Ingrid", "tekst": "Ingrid kjøper en leilighet på tegnebrettet. I kjøpekontrakten står det at «Kjøper gir avkall på retten til å holde tilbake penger ved mangler ved overtagelse». Overtagelsesdagen mangler badet fliser på én vegg. Ingrid nekter å betale de siste 100 000 kronene. Utbygger viser til kontrakten. Ingrid kan holde seg rolig og vise til paragraf 3 — kontraktspunktet er ugyldig."}],
    "vanlige_feil": [
        "Tro at man er låst fast til dårlige vilkår fordi man «har skrevet under på det»",
        "Akseptere muntlige avtaler om endringer i byggeprosjektet underveis",
        "La være å klage fordi utbygger påstår garantitiden deres har gått ut",
    ],
    "hva_bor_du_html": _p(
        "Ikke få panikk om utbygger vifter med kontrakten når en konflikt oppstår. Slå alltid opp i bustadoppføringsloven først. Hvis loven sier du har en rettighet, har du den.",
        "Krev alltid at endringer underveis bekreftes skriftlig på e-post med nøyaktig pris og tidspåvirkning spesifisert.",
    ),
    "dumme_sporsmal": [
        {"q": "Hva om jeg var fullstendig klar over vilkåret da jeg signerte?", "a": "Det spiller ingen rolle. Loven beskytter deg mot deg selv. Selv om utbygger sa «Du får huset 100 000 kr billigere hvis du fraskriver deg retten til dagbøter», gjelder lovens regler om dagbøter likevel. Avtalen er ugyldig."},
        {"q": "Gjelder e-post som skriftlig avtale?", "a": "Ja. En vanlig e-post er i dag ansett som juridisk bindende og skriftlig. SMS kan også fungere, men e-post er ryddigere for større avtaler."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "9", "tittel": "Endringer og tilleggsarbeid", "available": True},
        {"lov": LOV, "paragraf": "12", "tittel": "Bankgarantien", "available": True},
    ],
},

{
    "number": "4",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Hvilken lov gjelder når?",
    "description": "Kjøper du tomt separat? Denne paragrafen rydder opp i når bustadoppføringsloven slutter og kjøpsloven eller avhendingsloven tar over.",
    "kort_svar": "Kjøper du bare løse materialer uten arbeid, gjelder kjøpsloven. Kjøper du en ren tomt av en annen enn utbyggeren, gjelder avhendingsloven (eller tomtefesteloven) for selve tomtekjøpet.",
    "paragraftekst": "Føresegnene i lova her gjeld berre så langt ikkje anna følgjer av lov om kjøp. For avtale om rett til fast eigedom som ikkje er omfatta av § 1, gjeld lov om avhending av fast eigedom eller lov om tomtefeste.",
    "hva_betyr_html": _p(
        "Paragrafen fungerer som en trafikkdirigent. Kjøper du treverk, vinduer eller fliser for å bygge noe selv, er det kjøpsloven (og forbrukerkjøpsloven) som gjelder for materialene. Bustadoppføringsloven gjelder bare når et firma selger deg både materialer og arbeid.",
        "Mange kjøper en tomt først, og leier inn et byggefirma etterpå. Kjøpet av selve grunnen reguleres da av avhendingsloven. Leier du grunnen (fester), er det tomtefesteloven som gjelder for den biten. Selve byggingen reguleres av bustadoppføringsloven.",
    ),
    "eksempler": [{"navn": "Kari", "tekst": "Kari kjøper en hyttetomt direkte av en lokal grunneier, og later signerer en kontrakt med «Fjellhytter AS» for å bygge hytta. Tomtekjøpet følger avhendingsloven. Kontrakten for oppføringen følger bustadoppføringsloven. Feil på tomta: klag til grunneieren. Feil vinduer: klag til Fjellhytter AS."}],
    "vanlige_feil": [
        "Å prøve å bruke bustadoppføringsloven mot en privatperson man har kjøpt en tom tomt av",
        "Å klage til husleverandøren på feil som gjelder grunnen (når tomten er kjøpt separat)",
        "Glemme at løse materialer du kjøper selv, ikke er dekket av utbyggers garanti",
    ],
    "hva_bor_du_html": _p(
        "Når du kjøper tomt og hus fra to forskjellige parter, er det viktig å ha vanntette kontrakter. Pass spesielt på ansvaret for graving og grunnarbeid — hvem har ansvaret hvis dere støter på fjell som må sprenges?",
    ),
    "dumme_sporsmal": [
        {"q": "Gjelder kjøpsloven for parketten hvis byggefirmaet legger den?", "a": "Nei. Hvis byggefirmaet skaffer parketten og legger den, inngår begge deler i bustadoppføringsloven. Det er byggefirmaet du klager til."},
        {"q": "Hva om snekkeren ber meg kjøpe materialene selv for å spare penger?", "a": "Kjøper du materialene selv, gjelder forbrukerkjøpsloven for varene. Viser de seg å være råtne, må du dra tilbake til byggevarehuset og klage. Snekkeren har bare ansvar for selve timene."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "1", "tittel": "Lovens bruksområde", "available": True},
        {"lov": LOV, "paragraf": "2", "tittel": "Hvem som regnes som forbruker", "available": True},
    ],
},
{
    "number": "5",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Risikoen for at meldinger kommer frem",
    "description": "Hva skjer hvis e-posten du sender for å klage, havner i utbyggers søppelpost? Loven beskytter deg: sendt er levert.",
    "kort_svar": "Hvis du sender en klage eller viktig beskjed til utbyggeren på en normal og forsvarlig måte (som e-post), har du ditt på det tørre. Forsinkes e-posten eller havner den i søppelposten, regnes beskjeden uansett som levert innen fristen.",
    "paragraftekst": "Dersom ein part gjev melding i samsvar med lova og sender ho på forsvarleg måte, og ikkje anna framgår, kan sendaren gjere gjeldande at meldinga er gjeven i tide sjølv om ho vert forseinka eller på annan måte ikkje kjem fram slik ho skulle.",
    "hva_betyr_html": _p(
        "I byggeprosjekter er frister enormt viktige. Kanskje du har en garanti som går ut klokken 23:59 i kveld, og du må sende en klage på at gulvet har sprukket opp.",
        "Denne paragrafen fjerner risikoen for ting du ikke kan kontrollere. Så lenge du gjør din del av jobben og sender meldingen «på forsvarlig måte», gjelder den — selv om serveren til byggefirmaet krasjer og e-posten ikke lander i innboksen deres før dagen etter.",
        "Forsvarlig måte betyr e-post til adressen utbyggeren normalt bruker, brev i posten, eller bruk av utbyggerens kundeportal.",
    ),
    "eksempler": [{"navn": "Tom", "tekst": "Tom oppdager fukt 4 år og 11 måneder etter innflytting. Klagefristen er 5 år. Tom sender e-post med bilder to dager før fristen. Dagen etter krasjer entreprenørens e-postserver. Entreprenøren avviser klagen og sier fristen er utløpt. Tom viser til at han sendte forsvarlig før fristen — han har retten på sin side."}],
    "vanlige_feil": [
        "Å ikke ta vare på e-poster i Sendt-mappen som bevis på at klage ble sendt",
        "Å sende viktige frist-meldinger via Facebook Messenger",
        "Tro at utbygger må ha «godkjent» e-posten for at fristen skal være holdt",
    ],
    "hva_bor_du_html": _p(
        "Send klager alltid skriftlig på e-post. Be om lesebekreftelse, eller avslutt med: «Vennligst bekreft mottak av denne e-posten». Lagre e-posten i en egen mappe.",
    ),
    "dumme_sporsmal": [
        {"q": "Hva om jeg skriver feil e-postadresse med et uhell?", "a": "Da har du ikke sendt meldingen på «forsvarlig måte». Feilstavet adresse er din feil, og forsinkelsen er ditt ansvar. Sjekk alltid at adressen stemmer med kontrakten."},
        {"q": "Utbygger sier brevet kom frem to dager etter at fristen gikk ut. Hva gjør jeg?", "a": "Det holder at brevet er postlagt (stemplet av Posten) før fristen gikk ut — det er fordelen din med paragraf 5."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "6a", "tittel": "Bruk av elektronisk kommunikasjon", "available": True},
        {"lov": LOV, "paragraf": "3", "tittel": "Loven kan ikke endres til din ulempe", "available": True},
    ],
},

{
    "number": "6",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Erstatning ved personskade eller tingskade",
    "description": "Hva skjer hvis snekkeren mister en takstein på bilen din? Loven slår fast at entreprenøren ikke kan fraskrive seg ansvaret for å ødelegge dine private ting.",
    "kort_svar": "Bustadoppføringsloven bestemmer ikke erstatning ved personskade eller tap i næring — det reguleres av generell erstatningsrett. Men loven slår strengt fast at entreprenøren aldri kan fraskrive seg ansvaret hvis de ødelegger dine private ting (for eksempel bilen din).",
    "paragraftekst": "Føresegnene om skadebotansvar gjeld ikkje for tap som følgje av personskade eller for tap i næring. For slikt tap gjeld allmenne skadebotreglar. Ein entreprenør kan ikkje fråskrive seg ansvar for tap utanfor næring som forbrukaren lir på grunn av tingskade.",
    "hva_betyr_html": _p(
        "Paragrafen tegner en grense for hva bustadoppføringsloven blander seg opp i. Loven er laget for å håndtere avtalebrudd — at huset er forsinket, taket lekker, eller varmepumpen mangler.",
        "Hvis noen blir fysisk skadet på byggeplassen, løses dette etter Norges generelle erstatningsrett. Det samme gjelder hvis byggefeilen gjør at du må stenge frisørsalongen du driver («tap i næring»).",
        "Det viktigste for deg: «Tingskade» betyr at noe fysisk du eier privat blir ødelagt. Entreprenøren har forbud mot å skrive i kontrakten at «Vi tar ikke ansvar for biler parkert på tomten». Rygger graveren i din bil, har de plikt til å erstatte det.",
    ),
    "eksempler": [{"navn": "Eva", "tekst": "Eva leier inn et firma for å bygge et tilbygg. En håndverker mister et spann med maling ned fra taket og treffer Evas bil. I kontrakten har firmaet skrevet «Vi tar ikke ansvar for skader på ting som befinner seg på byggeplassen». Takket være § 6 er denne setningen ugyldig — Eva eier bilen privat, og byggefirmaet må erstatte skaden."}],
    "vanlige_feil": [
        "Entreprenører som henger opp skilt om at all parkering skjer «på eget ansvar», og tror at det frigjør dem fra erstatningsansvar",
        "Forbrukere som krever erstatning for tapt omsetning i firmaet fordi huset ble forsinket — det gir ikke bustadoppføringsloven rett til",
    ],
    "hva_bor_du_html": _p(
        "Hvis byggefirmaet skader tingene dine underveis, krev at de oppgir forsikringsselskapet sitt. Alle seriøse entreprenører har ansvarsforsikring. Rapporter inn skaden og ta bilder.",
    ),
    "dumme_sporsmal": [
        {"q": "Hva skjer hvis en håndverker blir skadet på min eiendom?", "a": "Som byggherre har du ikke automatisk skylden for dette. Entreprenøren skal sørge for egen HMS og forsikre sine ansatte."},
        {"q": "Gir loven meg erstatning hvis jeg må bo på hotell fordi huset er forsinket?", "a": "Hotellopphold er et tap som følge av avtalebrudd — og dét dekkes av bustadoppføringsloven via reglene om dagmulkt (§ 18), ikke denne paragrafen."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "3", "tittel": "Loven kan ikke endres til din ulempe", "available": True},
    ],
},
{
    "number": "6a",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "E-post og SMS er godkjent skriftlig kommunikasjon",
    "description": "Du trenger ikke lenger sende papirbrev. Bustadoppføringsloven godkjenner e-post og SMS, så lenge dere er enige om det.",
    "kort_svar": "Loven krever at visse avtaler og beskjeder skal være «skriftlige». Denne paragrafen slår fast at elektroniske meldinger — som e-post, SMS eller kundeportaler — regnes som skriftlige, så lenge du som forbruker har godtatt å bruke det.",
    "paragraftekst": "Krav i lova her om at avtale eller melding mv. skal vere skriftleg, er ikkje til hinder for bruk av elektronisk kommunikasjon om forbrukaren uttrykkeleg har godtatt dette.",
    "hva_betyr_html": _p(
        "Gjennom hele bustadoppføringsloven står det at ting skal skje «skriftleg». Loven ble opprinnelig skrevet før e-post var vanlig. Denne paragrafen ble lagt til for å modernisere reglene. Å bruke elektroniske løsninger er 100 % lovlig og sidestilt med blekk på papir.",
        "Det eneste kravet er at du «uttrykkelig» har godtatt det. I praksis løses dette nesten alltid ved at du oppgir e-postadressen din i kontrakten, eller at kontrakten signeres med BankID.",
    ),
    "eksempler": [{"navn": "Per", "tekst": "Per bygger hus og kommuniserer via e-post gjennom hele prosjektet. Entreprenøren sender e-post med krav om forlenget frist. Per krever dagmulkt later og argumenterer med at han aldri fikk varselet «skriftlig» i posten. Entreprenøren viser til at e-posten er gyldig skriftlig varsel siden Per brukte e-post som kontaktpunkt. Per taper saken."}],
    "vanlige_feil": [
        "Slette SMS-er eller e-poster i affekt under en konflikt",
        "Ta diskusjoner om penger og endringer på telefon, uten å be om e-post-bekreftelse etterpå",
        "Glemme å sjekke søppelpost-mappen under et byggeprosjekt",
    ],
    "hva_bor_du_html": _p(
        "Når du inngår byggekontrakten, avtal hvilken kanal som gjelder for beskjeder. Det beste er å skrive i avtalen at «all prosjektkommunikasjon tas via e-post til [din e-postadresse]». Ta vare på all skriftlig korrespondanse til huset har vært gjennom femårs-befaringen.",
    ),
    "dumme_sporsmal": [
        {"q": "Utbygger bruker en egen app/kundeportal for prosjektet. Er det gyldig?", "a": "Ja, hvis du har takket ja til dette. Pass på at du laster ned alle viktige dokumenter til din egen PC før prosjektet er ferdig."},
        {"q": "Kan jeg kreve å få ting på papir?", "a": "Ja. Siden paragrafen sier «om forbrukaren uttrykkeleg har godtatt dette», har du i teorien rett til å si nei til e-post og kreve at varsler sendes som brev."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "5", "tittel": "Meldingen gjelder fra tidspunktet den sendes forsvarlig", "available": True},
        {"lov": LOV, "paragraf": "9", "tittel": "Krav til skriftlighet ved endringer", "available": True},
    ],
},

{
    "number": "7",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Arbeidet skal gjøres skikkelig og med gode materialer",
    "description": "Entreprenøren skal levere et solid og fagmessig stykke arbeid. Lær hva det betyr at bygget må ha «vanlig god kvalitet».",
    "kort_svar": "Entreprenøren må gjøre jobben profesjonelt og fagmessig. De skal passe på dine interesser og levere materialer av normalt god standard. De må også gi deg råd underveis hvis forholdene tilsier det.",
    "paragraftekst": "Entreprenøren skal utføre arbeidet på fagleg godt vis og elles vareta forbrukarens interesser med tilbørleg omsut. Så langt tilhøva gjev grunn til det, skal entreprenøren samrå seg med eller rettleie forbrukaren. Materialane skal ha vanleg god kvalitet med mindre annan kvalitet er avtalt.",
    "hva_betyr_html": _p(
        "Arbeidet skal utføres på «fagleg godt vis». Det betyr at arbeidet skal følge bransjens egne normer for godt håndverk. Byggforsk-serien og Norsk Standard er ofte fasiten domstolene bruker. Blir flisene lagt skjevt med ujevne fuger, er det et brudd på denne paragrafen.",
        "Utbygger kan ikke kjøpe det billigste skrapet de finner. Loven krever «vanlig god kvalitet» på materialene.",
        "Til slutt sier loven at entreprenøren skal «veilede» deg. De er proffe, du er amatør. Hvis de ser at valget du gjør vil fungere dårlig i praksis, har de plikt til å snakke med deg om det.",
    ),
    "eksempler": [{"navn": "Sofie", "tekst": "Sofie bygger et nøkkelferdig hus. Når malerne er ferdige, renner malingen og det er skjoldete. Utbygger hevder de bare har brukt «økonomisk standard». Sofie klager og viser til § 7. At malingen er lagt uten stygge renner er et krav til «fagleg godt vis», uavhengig av priskategori. Entreprenøren må pusse ned og male på nytt gratis."}],
    "vanlige_feil": [
        "Å akseptere et dårlig resultat fordi man bygger et «billig-hus» — faglig utførelse kreves uansett",
        "Å tro at man selv må kjøpe inn spiker og fugemasse — entreprenøren har plikt til å holde materialer",
        "Entreprenører som ser at en tegning er dårlig, men utfører den uansett uten å veilede kunden",
    ],
    "hva_bor_du_html": _p(
        "Merker du at arbeidet ser slurvete ut underveis, si ifra umiddelbart — ikke vent til huset er ferdig.",
        "Skal du ha ekstra høy kvalitet på noe (spesialimportert eikegulv), skriv det tydelig ned i kontrakten. Ellers får du «vanlig god kvalitet».",
    ),
    "dumme_sporsmal": [
        {"q": "Er det ulovlig at gulvet knirker litt?", "a": "Her går grensen mellom perfeksjon og «faglig godt vis». Litt knirk i treverk kan være akseptert fordi tre er et levende materiale, men høy knirkelyd over hele stua er et avvik fra fagmessig utførelse."},
        {"q": "Hva skjer hvis jeg bestiller et kjempedyrt kjøkken, men entreprenøren setter inn et IKEA-kjøkken?", "a": "Hvis kontrakten sier at et spesifikt kjøkken skal leveres, og de leverer noe annet, er det mangel. Hvis kontrakten bare sier «Kjøkken inkludert», holder det med et kjøkken av «vanlig god kvalitet»."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "8", "tittel": "Entreprenørens plikt til å fraråde dårlige løsninger", "available": True},
        {"lov": LOV, "paragraf": "3", "tittel": "Loven kan ikke endres til din ulempe", "available": True},
    ],
},
{
    "number": "8",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Entreprenøren må advare deg hvis du gjør et dumt valg",
    "description": "Har du kommet med en idé snekkeren vet ikke vil fungere? Da har de streng plikt til å fraråde deg å gjøre det.",
    "kort_svar": "Entreprenøren er fageksperten. Hvis du ber dem bygge noe som de faglig sett vet blir dårlig, for dyrt, eller uhensiktsmessig for deg, har de plikt til å si stopp. Gir de ikke en slik advarsel, kan de miste retten til å få betalt for arbeidet.",
    "paragraftekst": "Må entreprenøren ut frå sin fagkunnskap sjå at forbrukaren ikkje er tent med å få arbeidet utført etter avtalen, skal entreprenøren seie frå om det. Arbeidet skal stansast til entreprenøren får samrådd seg med forbrukaren, dersom det må reknast å gagne forbrukaren. Har entreprenøren ikkje sagt frå, skal krav på vederlag ikkje vere større enn det ville ha vore dersom entreprenøren hadde oppfylt plikta.",
    "hva_betyr_html": _p(
        "Paragraf 8 er din sikkerhetsventil mot at byggeprosjektet går fullstendig galt på grunn av din egen mangel på kunnskap. Loven kaller det «plikt til fråråding».",
        "La oss si du bestiller teppegulv på badet. Entreprenøren vet at teppe på bad fører til fuktskader og mugg. De kan ikke bare gjøre jobben og sende fakturaen. De skal stoppe og gi deg beskjed om at dette er en ekstremt dårlig idé.",
        "Gjør de jobben uansett uten å ha advart deg, slår loven hardt ned. Du slipper da å betale for det ubrukelige arbeidet, eller kan kreve prisavslag.",
    ),
    "eksempler": [{"navn": "Jonas", "tekst": "Jonas ber entreprenøren fjerne en bærevegg og bytte den ut med et stort billig stuevindu. Entreprenøren ser at vinduet ikke tåler vekten, men sier ingenting og monterer det. Taket begynner å sige og vinduet knuser. Fordi entreprenøren ikke frarådet Jonas, sitter de med ansvaret for å rette opp skadene og får ikke betalt for den ubrukelige monteringen."}],
    "vanlige_feil": [
        "Håndverkere som utfører dumme løsninger for å «gjøre kunden fornøyd» og ender opp i erstatningsansvar",
        "Forbrukere som krever teknisk dårlige løsninger og blir sinte når snekkeren nekter",
    ],
    "hva_bor_du_html": _p(
        "Hvis du er snekker: Skriv advarselen ned! Send e-post: «Vi fraråder sterkt denne takløsningen fordi det ikke vil tåle snølast. Hvis du likevel krever det utført, fraskriver vi oss garantiansvaret for dette punktet.»",
        "Hvis du er forbruker: Lytt til fagfolkene. Frarådingsplikten er der for å beskytte hjemmet ditt og lommeboken din.",
    ),
    "dumme_sporsmal": [
        {"q": "Hva om entreprenøren rådet meg fra noe, men jeg tvang dem til å gjøre det likevel?", "a": "Da har entreprenøren ryggen fri. Hvis de kan dokumentere at de frarådet deg tydelig, og du likevel insisterte, bærer du selv hele ansvaret og regningen."},
        {"q": "Gjelder plikten bare tekniske ting, eller også utseende?", "a": "Den gjelder primært funksjon, tekniske krav, sikkerhet og pris. Entreprenøren har ingen plikt til å fraråde deg å male huset knallrosa."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "7", "tittel": "Fagmessig utførelse", "available": True},
        {"lov": LOV, "paragraf": "9", "tittel": "Din rett til å kreve endringer", "available": True},
    ],
},

{
    "number": "9",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Din rett til å kreve endringer underveis",
    "description": "Du kan ombestemme deg og kreve endringer mens huset bygges. Men det finnes en grense for hva du kan pålegge entreprenøren.",
    "kort_svar": "Du har lov til å kreve endringer og tilleggsarbeid mens boligen bygges, for eksempel et ekstra vindu eller en annen type parkett. Utbyggeren plikter å utføre dette. Men du kan ikke kreve endringer som forandrer hele prosjektets karakter, eller som skaper urimelig store problemer for entreprenøren.",
    "paragraftekst": "Forbrukaren kan krevje endringar i arbeidet og påleggje entreprenøren å utføre tilleggsarbeid som står i samanheng med den ytinga som er avtalt, og som ikkje i omfang eller karakter skil seg vesentleg frå denne. Det kan avtalast at forbrukaren ikkje kan krevje endringar som vil endre vederlaget med 15 prosent eller meir. Entreprenøren kan krevje at tinging på endringar blir gjord skriftleg.",
    "hva_betyr_html": _p(
        "Det er helt normalt å justere planene når man ser huset ta form. Denne paragrafen gir deg en lovfestet rett til å pålegge entreprenøren å utføre slike endringer.",
        "Men loven setter to viktige grenser: Tilleggsarbeidet må henge sammen med det opprinnelige prosjektet. Og utbygger har lov til å skrive i kontrakten at du ikke kan kreve endringer som totalt øker prisen med mer enn 15 prosent av opprinnelig kontraktssum.",
        "Dessuten er det urimelig å be om store endringer altfor sent i byggeprosessen — da kan entreprenøren nekte.",
    ),
    "eksempler": [{"navn": "Kari", "tekst": "Kari bygger enebolig. Halvveis innser hun at kjøkkenet blir for mørkt. Hun sender e-post og krever et ekstra vindu og bytte fra fliser til herdet glass over kjøkkenbenken. Veggen er ikke lukket ennå. Dette er innenfor lovens rammer — entreprenøren må godta endringen."}],
    "vanlige_feil": [
        "Muntlige bestillinger — «kan du bare slenge opp en lettvegg der?» er oppskriften på krangel om pris",
        "Tro at tilleggsarbeid er inkludert i den opprinnelige fastprisen",
        "Å be om store endringer altfor sent i byggeprosessen",
    ],
    "hva_bor_du_html": _p(
        "Du skal alltid bestille endringer skriftlig. Be entreprenøren sende en e-post med: 1. Hva som skal gjøres. 2. Nøyaktig hva det vil koste. 3. Hvor mange dager ekstra tid de trenger. Svar «Godkjent» på e-posten — da har du ryggen fri.",
    ),
    "dumme_sporsmal": [
        {"q": "Entreprenøren nekter å ta på seg en liten endring fordi de «ikke har tid». Er det lov?", "a": "Nei. Så lenge endringen er innenfor lovens rammer og bestilles i tide, er dette en del av deres plikt. De kan kreve at overtakelsesdatoen skyves tilsvarende."},
        {"q": "Hva om jeg vil ta ut noe av kontrakten — for eksempel legge gulvet selv?", "a": "Dette er også en endring. Du kan kreve å ta ut arbeid, og summen du sparer skal trekkes fra totalprisen."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "11", "tittel": "Rett til utsatt frist ved endringer", "available": True},
        {"lov": LOV, "paragraf": "8", "tittel": "Frarådingsplikten", "available": True},
    ],
},
{
    "number": "10",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Huset skal være ferdig til avtalt tid",
    "description": "Du har rett til en klar tidsplan. Loven forteller hva som gjelder hvis dere har en nøyaktig dato, og hva som skjer hvis fristen er uklar.",
    "kort_svar": "Entreprenøren plikter å overholde alle avtalte frister. Hvis dere ikke har avtalt en bestemt dato, krever loven at de starter opp arbeidet så snart som mulig og bygger huset ferdig med «rimelig framdrift» uten unødvendige pauser.",
    "paragraftekst": "Entreprenøren skal overhalde fristar som er avtalte for overtaking og for fullføring av arbeidet. Er det ikkje avtalt fristar, skal entreprenøren ta til med arbeidet snarast råd etter at forbrukaren har sagt frå om det. Arbeidet skal deretter utførast med rimeleg framdrift og utan unødig avbrot.",
    "hva_betyr_html": _p(
        "Har dere en konkret dato i kontrakten, gjelder denne strengt. Klarer ikke entreprenøren fristen, har du rett på dagmulkt.",
        "Hva hvis det bare står «ferdigstilles etter nærmere avtale» eller kontrakten mangler en dato? Da sier loven at entreprenøren må starte opp straks du ber om det og holde på effektivt. De kan ikke jobbe i to dager, forsvinne til et annet prosjekt i tre uker, og så komme tilbake.",
    ),
    "eksempler": [{"navn": "Ola", "tekst": "Ola glemte å kreve en fast dato i kontrakten. De første ukene jobber tre tømrere, men så blir det stille — huset står uten tak i fire uker mens tømrerne bygger en garasje et annet sted. Ola sender varsel om «unødig avbrot» og krever at arbeidet gjenopptas. Entreprenøren må stille opp igjen."}],
    "vanlige_feil": [
        "Å godta vage frister som «Ferdig ca. høsten 2026»",
        "Å tro at man ikke kan klage på forsinkelse bare fordi man mangler en sluttdato",
        "Ikke avtale del-frister hvis du har egne folk som skal gjøre oppgaver underveis",
    ],
    "hva_bor_du_html": _p(
        "Du bør alltid kreve en konkret, fastsatt dato for overtakelse. Ikke godta estimater. Hvis utbygger krever «10 måneder fra byggestart», må du kreve at «byggestart» defineres som en konkret dato.",
    ),
    "dumme_sporsmal": [
        {"q": "Gir «rimelig framdrift» meg rett til dagmulkt hvis de er trege?", "a": "Ja, men det er mye vanskeligere å bevise enn om du har en fast dato i kalenderen."},
        {"q": "De vil overlevere huset, men badet mangler dusj. Er fristen holdt?", "a": "Nei. For at fristen skal være overholdt, må arbeidet være så komplett at det er klart til å tas i normal bruk."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "11", "tittel": "Når utbygger kan be om ekstra tid", "available": True},
        {"lov": LOV, "paragraf": "14", "tittel": "Dagen du tar over boligen", "available": True},
    ],
},

{
    "number": "11",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Når kan entreprenøren få utsette fristen?",
    "description": "Entreprenøren kan ikke bare skylde på været for å utsette innflyttingen din. Her er de strenge reglene for når de har rett på mer tid.",
    "kort_svar": "Entreprenøren har kun rett på ekstra tid (tilleggsfrist) hvis forsinkelsen er din feil, hvis du har bestilt masse ekstraarbeid, eller hvis det skjer noe helt ekstremt og uforutsett som de ikke kunne kontrollere (force majeure). De må i tillegg varsle deg umiddelbart.",
    "paragraftekst": "Entreprenøren kan krevje lenging av avtalte fristar dersom a. forbrukaren krev endringar som seinkar arbeidet, b. arbeidet blir seinka fordi forbrukaren ikkje medverkar i samsvar med avtalen, eller c. arbeidet blir seinka på grunn av ei hindring utanfor entreprenørens kontroll, og det ikkje er rimeleg å vente at entreprenøren kunne ha rekna med hindringa på avtaletida. Entreprenøren har berre krav på fristlenging dersom melding er gjeven forbrukaren utan ugrunna opphald.",
    "hva_betyr_html": _p(
        "Loven stenger døren for de fleste vanlige unnskyldninger. Entreprenøren har utelukkende rett på mer tid i tre spesifikke situasjoner: (a) Du har bestilt endringer. (b) Du forsinker dem. (c) Force majeure — ting de overhodet ikke kan kontrollere, som global materialmangel, landsomfattende streik eller ekstremvær.",
        "Vanlig dårlig vær (selv mye regn), normal sykdom hos ansatte, eller at bilen deres bryter sammen, gir dem IKKE rett på ekstra tid. Det er deres egen risiko.",
        "Det aller viktigste: Entreprenøren må gi deg beskjed uten ugrunnet opphold. De kan ikke vente til huset skal leveres i desember med å si at de ble forsinket av en storm i april.",
    ),
    "eksempler": [{"navn": "Anne", "tekst": "Anne skal ta over huset 1. september. I juli sender entreprenøren e-post og sier at rørleggeren har dobbeltbooket seg og de mangler fliser fra leverandøren. De vil utsette til 1. oktober. Anne sjekker § 11: Rørleggerplanlegging og vanlig materialmangel er ting de styrer selv — ikke force majeure. Anne nekter tilleggsfrist og varsler krav om dagmulkt."}],
    "vanlige_feil": [
        "Å akseptere dårlig vær eller underleverandør-trøbbel som gyldig grunn til å flytte innflyttingsdatoen",
        "At entreprenøren varsler om tilleggsfrist først på overtakelsesmøtet — altfor sent",
        "Å tro at en uke med snøstorm automatisk gir tre ukers utsettelse",
    ],
    "hva_bor_du_html": _p(
        "Når du får et krav om tilleggsfrist, krev at de dokumenterer hvorfor det har skjedd, og hvilken del av § 11 de mener gir dem rett.",
        "Ikke svar automatisk «ok» hvis du er uenig. Skriv tilbake: «Mottatt, men vi bestrider at dette gir rett til tilleggsfrist etter bustadoppføringslova § 11, og opprettholder den avtalte sluttdatoen.»",
    ),
    "dumme_sporsmal": [
        {"q": "Hva om underentreprenøren deres streiker?", "a": "En lovlig organisert streik regnes normalt som force majeure. Da har entreprenøren krav på tilleggsfrist."},
        {"q": "Varselet kom én måned etter at stormen var ferdig. Er det for sent?", "a": "Ja. «Uten ugrunna opphold» betyr vanligvis innen noen få dager etter at de innså at problemet kom til å forsinke dem."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "10", "tittel": "Huset skal være ferdig til avtalt tid", "available": True},
        {"lov": LOV, "paragraf": "9", "tittel": "Din rett til å kreve endringer (som kan gi tilleggsfrist)", "available": True},
    ],
},
{
    "number": "12",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Bankgarantien som beskytter deg mot konkurs",
    "description": "Dette er din aller viktigste sikkerhet. Utbygger MÅ stille en bankgaranti. Du skal ikke betale én krone til utbygger før du har fått bevis på at garantien finnes.",
    "kort_svar": "Entreprenøren er lovpålagt å opprette en bankgaranti (§ 12-garanti) med en gang dere inngår avtalen. Garantien skal dekke 10 % av kjøpesummen mens huset bygges, og 5 % i fem år etter at du har tatt over boligen. Du skal ikke betale én krone til utbygger før du har fått bevis på at garantien finnes.",
    "paragraftekst": "Entreprenøren skal stille garanti for oppfyllinga av avtalen. Garantien skal gjelde fram til fem år etter overtakinga og dekkje ein sum som minst svarer til ti prosent av vederlaget. For krav gjort gjeldande på eit seinare tidspunkt enn ved overtakinga, kan garantisummen vere fem prosent av vederlaget. Til det er dokumentert at det ligg føre garanti, har forbrukaren rett til å halde att alt vederlag.",
    "hva_betyr_html": _p(
        "Hvert år går norske byggeselskaper konkurs og etterlater familier med halvferdige hus. For å hindre at du mister alle sparepengene dine, har loven pålagt utbyggerne å stille en § 12-garanti.",
        "En garanti betyr at utbyggeren må få banken sin til å love at de vil betale deg ut hvis utbyggeren går konkurs, stikker av, eller nekter å fikse en grov feil. Bygger du hus på din egen tomt, garanteres 10 % av kontraktsummen i byggetiden. Kjøper du tomt og hus samlet, er garantien 3 % i byggetiden.",
        "Når huset er ferdig og du har flyttet inn, synker garantiens størrelse til 5 %, og den forblir gjeldende i fem hele år.",
        "Det siste leddet i paragrafen er din makt: Du har rett til å fryse all betaling inntil utbyggeren fysisk har gitt deg garantibeviset fra banken.",
    ),
    "eksempler": [{"navn": "Petter", "tekst": "Petter signerer en byggekontrakt på 6 millioner kroner. Entreprenøren sender garantibevis fra banken på 600 000 kroner (10 %). Huset reises, men før innvendig arbeid slår utbyggeren seg konkurs. Petter kontakter banken og legger frem avtalen og konkursbekreftelsen. Banken utbetaler de 600 000 kronene — Petter tapte ingen penger."}],
    "vanlige_feil": [
        "Å betale første faktura før man har fått garantibeviset i hendene",
        "Å godta at byggefirmaets sjef signerer en «personlig garanti» — loven krever garanti fra offisiell bank",
        "Å glemme garantien helt til år 6 da feilene dukker opp (fristen er 5 år)",
    ],
    "hva_bor_du_html": _p(
        "Spør om § 12-garantien i det sekundet du signerer kontrakten. Sier utbyggeren at «den kommer senere», svarer du: «Den er grei, men jeg holder igjen alle betalinger inntil jeg har beviset.»",
        "Sjekk at garantidokumentet har stempel og signatur fra en norsk bank, og at beløpet stemmer med prosentsatsene i loven.",
    ),
    "dumme_sporsmal": [
        {"q": "Må vi ha garanti for et lite tilbygg?", "a": "Nei, loven krever ikke bankgaranti hvis arbeidet koster mindre enn 2G (to ganger grunnbeløpet i folketrygda)."},
        {"q": "Entreprenøren sier banken nekter å gi dem garanti fordi de har dårlig kreditt. Hva da?", "a": "Løp. Dette er et knallrødt flagg. Hvis ikke banken stoler på at entreprenøren har økonomi til å overleve prosjektet, bør heller ikke du gjøre det. Du kan da heve avtalen."},
        {"q": "Utbygger sier jeg må betale gebyret for garantien. Stemmer det?", "a": "Nei. Det er entreprenørens lovpålagte plikt å stille garantien — de betaler bankens gebyr for dette."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "3", "tittel": "Loven kan ikke endres til din ulempe", "available": True},
        {"lov": LOV, "paragraf": "14", "tittel": "Dagen du tar over boligen", "available": True},
    ],
},

{
    "number": "13",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Dette skal være med i et ferdighus",
    "description": "Hva betyr egentlig «nøkkelferdig»? Loven slår fast at entreprenøren må levere et hus du faktisk kan bo i, og at de må forsikre det underveis.",
    "kort_svar": "Kjøper du en ny bolig der entreprenøren står for det meste, må de levere alt som trengs for at du kan flytte rett inn, med mindre dere har avtalt noe annet. De skal også dekke strøm, rigg og søppel under byggingen, og de er pålagt å forsikre huset fram til du tar over.",
    "paragraftekst": "Dersom eigedomsdelar eller faste innretningar som trengst for å ta bustaden i vanleg bruk ikkje høyrer med til det entreprenøren skal yte, skal desse nemnast særskilt i avtaledokumentet. Er ikkje det gjort, skal slike delar reknast å høyre med. Er ikkje anna avtalt, skal entreprenøren syte for tilkomst til byggjeplassen, byggjestraum, fjerning av restar og avfall. Er ikkje anna avtalt, skal entreprenøren halde arbeidet trygda fram til overtakinga.",
    "hva_betyr_html": _p(
        "Denne paragrafen rydder opp i hva du har krav på å få levert. Vil utbyggeren at du skal kjøpe kjøkkenet eller dusjkabinettet selv, må de skrive det med store, tydelige bokstaver i kontrakten. Står det ingenting, har du rett på et normalt kjøkken — siden et hus ikke kan tas «i vanleg bruk» uten et kjøkken.",
        "Tredje ledd er kjempeviktig for å unngå skjulte kostnader. Entreprenører prøver ofte å sende regning for containere og avfallshåndtering, eller be deg betale strømregningen (byggestrøm) mens de bygger. Med mindre kontrakten uttrykkelig legger disse kostnadene på deg, er det entreprenøren som tar regningen.",
        "Til slutt: Entreprenøren skal forsikre huset. Brenner huset ned før du overtar, skal byggforsikringen deres dekke det.",
    ),
    "eksempler": [{"navn": "Sara", "tekst": "Sara kjøper en nøkkelferdig leilighet. Utbyggeren sender en faktura på 20 000 kr for «Bortkjøring av avfall og containerleie». Det sto ingenting om søppel i kontrakten. Etter § 13 tredje ledd må utbyggeren trekke fakturaen — det er deres ansvar å betale."}],
    "vanlige_feil": [
        "Å ikke lese leveransebeskrivelsen nøye — hvis det faktisk står «Ekskludert: gulv og maling» er det gyldig",
        "Å betale strømregningen for varmeovner som står på i råbygget hele vinteren",
    ],
    "hva_bor_du_html": _p(
        "Gå gjennom leveransebeskrivelsen i kontrakten med lupe. Se hva som uttrykkelig er utelatt. Spør om å få kopi av byggeplassforsikringen. Paragrafen gir deg rett til å holde igjen alle betalinger til du får bevis på at huset er forsikret.",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg med hvitevarer automatisk?", "a": "Ikke nødvendigvis. Hvitevarer anses ofte som løsøre du typisk tar med deg. Kjøkkeninnredning (skap og benk) faller derimot under det du forventer er der."},
        {"q": "Hva om jeg har kjøpt dyre dører som jeg legger på byggeplassen, og så brenner huset ned?", "a": "Entreprenørens forsikring skal også gjelde materialer som er tilført eiendommen. Be snekkeren bekrefte at de tar imot dørene og oppbevarer dem trygt."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "12", "tittel": "Garantien du skal kreve bevis på", "available": True},
        {"lov": LOV, "paragraf": "7", "tittel": "Fagmessig utførelse og materialer", "available": True},
    ],
},
{
    "number": "14",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Dagen du tar over boligen",
    "description": "Overtakelsen er et magisk tidspunkt. Fra denne dagen flyttes risiko, forsikring og alle tidsfrister fra utbyggeren over til deg.",
    "kort_svar": "Overtakelsen skjer gjennom et formelt møte (overtakelsesforretning). Når du formelt har tatt over boligen, flyttes risikoen over til deg. Det betyr også at klagefristene begynner å løpe, dagmulkten stopper, og utbyggeren har rett på sluttoppgjøret.",
    "paragraftekst": "Overtaking skjer ved overtakingsforretning. Er arbeidet fullført og forbrukaren har flytta inn i bustaden, er ytinga overteke sjølv om det ikkje er halde overtakingsforretning. Ved overtakinga går vågnaden for ytinga over frå entreprenøren til forbrukaren, tek reklamasjonsfristane til, stansar eventuell dagmulkt, og får entreprenøren krav på sluttoppgjer.",
    "hva_betyr_html": _p(
        "Overtakelsesdagen er den viktigste datoen i hele byggeprosjektet. Fire dramatiske juridiske endringer skjer i det sekundet overtakelsesprotokollen signeres: 1. Risikoen for huset går til deg. 2. Klagefristen på 5 år starter. 3. Dagmulkten stopper. 4. Entreprenøren kan sende sluttfakturaen.",
        "Men loven lukker et smutthull: Hvis du lurer deg til å flytte alle møblene dine inn og begynner å bo der, regnes huset som overtatt uansett om det er holdt et møte eller ikke.",
    ),
    "eksempler": [{"navn": "Tom", "tekst": "Huset til Tom var tre uker forsinket — 30 000 kr i dagmulkt. Entreprenøren innkaller til overtakelsesforretning 1. september. Tom og entreprenøren går gjennom huset, Tom får nøklene og signerer. Nøyaktig da stopper dagmulkten, 5-årsgarantien begynner, og entreprenøren kan sende sluttregningen."}],
    "vanlige_feil": [
        "Å flytte inn esker og møbler før den formelle overtakelsen — dette kan avbryte dagmulkten du har krav på",
        "Å glemme å kjøpe egen husforsikring fra og med overtakelsesdatoen",
        "Å overta et hus med alvorlige feil fordi man «trenger et sted å bo»",
    ],
    "hva_bor_du_html": _p(
        "Tegn bygningsforsikring fra den dagen dere skal ha overtakelsesforretning.",
        "Ikke flytt inn noe som helst, eller krev å få nøkkelen «bare for å sette inn sofaen», før det formelle møtet er ferdig.",
    ),
    "dumme_sporsmal": [
        {"q": "Entreprenøren sier jeg kan flytte inn selv om de ikke er helt ferdige. Er det trygt?", "a": "Risikabelt. Flytter du inn, er bygget formelt overtatt og dagmulkten stanser. Vil du flytte inn tidlig, lag en skriftlig avtale om at «innflytting ikke utgjør formell overtakelse»."},
        {"q": "Hva om badet mangler sluk, og de krever overtakelse?", "a": "Du har rett til å nekte å overta hvis manglene er så store at huset ikke er brukbart. Da er huset ikke overtatt og dagmulkten løper videre."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "15", "tittel": "Slik fungerer selve overtakelsesforretningen", "available": True},
        {"lov": LOV, "paragraf": "12", "tittel": "Bankgarantien som varer 5 år etter overtakelse", "available": True},
    ],
},

{
    "number": "15",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Slik fungerer overtakelsesforretningen",
    "description": "Du skal gå befaring før du får nøkkelen. Men dukker du ikke opp, kan utbyggeren overlevere huset til deg likevel.",
    "kort_svar": "Entreprenøren må gi deg minst 7 dagers varsel. Dere møtes, går gjennom huset og skriver en protokoll. Uteblir du uten gyldig grunn, kan de holde møtet alene — noe som betyr at du mister klagefristen på synlige feil. Har huset alvorlige feil, kan du nekte å ta over.",
    "paragraftekst": "Kvar av partane kan med minst sju dagars varsel kalle inn til overtakingsforretning. Let den eine parten vere å møte utan gyldig grunn, kan den andre parten gjennomføre overtakingsforretning åleine. Forbrukaren kan nekte å overta ytinga dersom det ligg føre mangel som gjev rimeleg grunn til nektinga. Ved overtakingsforretninga bør det førast protokoll som begge partane får eit underskrive eksemplar av.",
    "hva_betyr_html": _p(
        "Du har krav på 7 dagers skriftlig varsel. Benytt tiden til å leie inn en uavhengig takstmann for å være med deg på befaringen.",
        "Hvis du glemmer å møte opp, kan entreprenøren gå gjennom huset alene. Huset er da juridisk overtatt av deg, og synlige riper i parketten er ikke lenger utbyggers problem.",
        "Du kan nekte å overta. Hvis strømmen ikke virker og trappen mangler trinn, har du «rimeleg grunn» til å si nei. Mindre feil gir deg ikke rett til å nekte — da overtar du, skriver opp feilen i protokollen, og holder tilbake penger.",
    ),
    "eksempler": [{"navn": "Eva", "tekst": "Entreprenøren sender formelt varsel 10 dager i forveien med advarsler om hva som skjer hvis Eva ikke møter opp. Eva glemmer og drar på hytta. Entreprenøren går gjennom bygget alene og noterer overtakelse. Mandag oppdager Eva en stor ripe i inngangsdøren — men entreprenøren har loven på sin side siden Eva uteble."}],
    "vanlige_feil": [
        "Å signere på at huset er «feilfritt» for å få nøkkelen fort",
        "Nekte å overta fordi det er litt malingssøl på et vindu — dette er ikke nektingsgrunn",
        "Ikke skrive ned absolutt alle skavanker, riper og feil i overtakelsesprotokollen der og da",
    ],
    "hva_bor_du_html": _p(
        "Ha alltid med deg en ekstern bygningskyndig (takstmann) på overtakelsesbefaringen. Bruk tid. Krev at de fører protokoll, og at hver eneste ripe skrives ned med en konkret frist for utbedring.",
        "Skriv i protokollen at du holder tilbake penger for det som står på mangellisten.",
    ),
    "dumme_sporsmal": [
        {"q": "Jeg oppdaget en diger sprekk i flisa på badet i går, og vi hadde befaring for to uker siden. Er det for sent?", "a": "Antagelig ja. Skader i overflater er noe du «burde ha oppdaget» på selve overtakelsesforretningen. Utbygger vil nesten alltid påstå at sprekken oppstod etter at du flyttet inn."},
        {"q": "Utbygger har nektet å holde tilbake penger i kontrakten. Kan jeg likevel kreve det skrevet i protokollen?", "a": "Ja. Loven er ufravikelig. Du har rett til å holde tilbake penger uansett hva som står i kontrakten."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "14", "tittel": "Konsekvensene av overtakelsen", "available": True},
        {"lov": LOV, "paragraf": "16", "tittel": "Rett til ettårsbefaring", "available": True},
    ],
},
{
    "number": "16",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Ettårsbefaringen er din andre sjanse",
    "description": "Har huset satt seg og listene begynt å sprekke opp? Ett år etter innflytting kan du kreve at entreprenøren kommer på ny gjennomgang.",
    "kort_svar": "Når det har gått ett år siden du overtok boligen, har du rett til å kreve en ny, formell gjennomgang (ettårsbefaring). Du må be om dette selv — utbyggeren har ikke plikt til å kalle inn av seg selv.",
    "paragraftekst": "Kvar av partane kan krevje at det blir halde ei synfaring av entreprenørens yting når det er gått om lag eitt år etter overtakinga.",
    "hva_betyr_html": _p(
        "Et nytt hus beveger seg. Treverket tørker og krymper gjennom den første vinteren, og grunnmuren «setter seg». Huset kan få tørkesprekker i gipsen, knirk i parketten og dører som binder i karmen.",
        "Denne paragrafen gir deg rett til å kreve at snekkeren kommer tilbake ett år etter overtakelse. Da går dere en runde og sjekker feilene som har oppstått det siste året. Er de et resultat av byggefeil eller unormalt stor setning, skal entreprenøren fikse det.",
        "Men det er «kan kreve» — utbyggeren er ikke automatisk pålagt å kalle inn. Du må ta initiativet og sende kravet til utbygger når det har gått ca. 11 måneder.",
    ),
    "eksempler": [{"navn": "Ingrid", "tekst": "Ingrid overtok rekkehuset i august i fjor. Det første året fikk gipsen stygge sprekker i tre hjørner og en stikkontakt sluttet å fungere. I juli sender Ingrid e-post: «Viser til bustadoppføringslova § 16. Jeg krever at det holdes en ettårsbefaring av boligen. Ta kontakt for å avtale tidspunkt.» Utbyggeren er forpliktet til å møte opp."}],
    "vanlige_feil": [
        "Å vente på at utbyggeren skal ringe deg og avtale befaring — du må ta initiativet selv",
        "Sende klager på småting fortløpende hele året — mye bedre å samle opp alle tørkeskader til ettårsbefaringen",
    ],
    "hva_bor_du_html": _p(
        "Når du tar over boligen, sett et varsel i kalenderen nøyaktig 10 måneder frem i tid. Gå gjennom boligen uken før varselet går av, lag en ryddig liste over alt som skurrer, og send e-posten til utbygger med krav om synfaring.",
        "Det er lov og vanlig å samle opp ikke-kritiske feil til ettårsbefaringen. Går vannrøret lekk på dag fire, krev det utbedret straks — men en treg dør kan fint vente.",
    ),
    "dumme_sporsmal": [
        {"q": "Fristen for å klage på mangler er 5 år. Hvorfor bry seg om ettårsbefaringen?", "a": "Fordi det er mye enklere å bevise at feilen er utbyggerens skyld det første året. Etter fire år vil de ofte påstå at barn har hengt i dørhåndtaket."},
        {"q": "Jeg glemte det. Det har gått 18 måneder. Kan jeg kreve befaring nå?", "a": "Nei, da har du overskredet muligheten for «ettårsbefaring». Fra nå av må du oppdage og klage på feilene én og én innen rimelig tid (ca. to måneder fra du oppdaget feilen)."},
        {"q": "Skal jeg betale for utbedringene etter befaringen?", "a": "Nei. Hvis feilen skyldes håndverket, skal all retting etter ettårsbefaringen være gratis."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "15", "tittel": "Overtakelsesforretningen", "available": True},
        {"lov": LOV, "paragraf": "14", "tittel": "Dagen du tar over boligen", "available": True},
    ],
},
{
    "number": "17",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Hva skjer når huset er forsinket?",
    "description": "Har overtakelsesdatoen passert, og boligen er ikke ferdig? Her er de fire lovfestede våpnene du kan bruke mot utbyggeren.",
    "kort_svar": "Ytelsen er forsinket hvis du ikke får ta over boligen til den fristen dere har avtalt. Når forsinkelsen er et faktum, gir loven deg fire konkrete rettigheter: Du kan kreve dagmulkt, holde tilbake betaling, kreve erstatning, eller i verste fall heve hele avtalen.",
    "paragraftekst": "Ytinga er forseinka dersom overtaking ikkje kan skje til den tida forbrukaren har rett til å krevje etter §§ 10 og 11. Det same gjeld dersom arbeidet eller delar av arbeidet ikkje er fullført eller heimelsoverføring ikkje skjer til dei tidene forbrukaren har rett til å krevje. Er ytinga forseinka, kan forbrukaren a) krevje dagmulkt etter § 18, b) heve avtalen etter § 20, c) krevje skadebot etter § 19 eller § 22, d) halde attende vederlag etter § 24. Dersom entreprenøren ikkje i tide oppfyller andre plikter etter avtalen, gjeld føresegnene om forseinking tilsvarande så langt dei høver, likevel ikkje føresegnene om dagmulkt.",
    "hva_betyr_html": _p(
        "Dette er lovens introduksjon til hva du kan gjøre når utbyggeren bryter tidsplanen.",
        "Første avsnitt slår fast <em>når</em> det er en forsinkelse. Hovedregelen er at forsinkelsen starter dagen etter den avtalte overtakelsesdatoen. Den gjelder også hvis de er ferdige med å bygge, men de ikke har overført skjøtet (hjemmelen) til deg i tide.",
        "Når forsinkelsen er i gang, lister andre avsnitt opp «verktøykassen» din. Først og fremst kan du kreve dagmulkt, som er et fastsatt kronebeløp for hver dag de er for sene. Du kan også nekte å betale sluttoppgjøret for å sikre at du faktisk får disse pengene (holde tilbake vederlag). Har du store økonomiske tap, kan du kreve erstatning (skadebot). Og hvis forsinkelsen blir helt ekstrem, kan du sparke entreprenøren og avbryte kontrakten (heve avtalen).",
        "Det aller vanligste — og enkleste — er dagmulkt. Dagmulkt er en automatisk straff entreprenøren må betale deg. Du trenger ikke bevise at du har tapt penger på å bo lenger i den gamle leiligheten. Forsinkelsen i seg selv er nok til at pengene begynner å løpe.",
    ),
    "eksempler": [{"navn": "Marius", "tekst": "Marius skulle overta sitt nye rekkehus 1. september. På grunn av rot med elektrikeren, blir ikke huset klart for overtakelse før 15. september. Huset er forsinket etter § 17. Marius ser i verktøykassen i paragrafen og velger bokstav a og d. Han krever dagmulkt for de 14 dagene forsinkelsen varte, og han holder tilbake dette beløpet fra den siste fakturaen entreprenøren sender ham. Entreprenøren må akseptere trekket."}],
    "vanlige_feil": [
        "Å godta muntlige unnskyldninger (vi ble litt forsinket med materialene) uten å registrere det formelt som en forsinkelse",
        "Å betale den siste fakturaen i sin helhet, og tro at utbyggeren vil vippse dagmulkten tilbake til deg etterpå (gjør de sjelden)",
    ],
    "hva_bor_du_html": _p(
        "Dagen etter at fristen for overtakelse er brutt, sender du en e-post til entreprenøren. Skriv: «Jeg viser til at avtalt overtakelsesdato var [dato]. Boligen er ikke klar. Jeg varsler med dette om at boligen er forsinket etter bustadoppføringslova § 17, og at det vil bli krevd dagmulkt frem til gyldig overtakelse finner sted.» Da har du sikret rettighetene dine svart på hvitt.",
        "Hvis du betaler hele sluttoppgjøret uten å trekke fra kravet ditt om dagmulkt, mister du det sterkeste pressmiddelet du har. Da må du i verste fall trekke entreprenøren for retten for å få pengene utbetalt i etterkant.",
    ),
    "dumme_sporsmal": [
        {"q": "Må jeg bevise at jeg har tapt penger for å bruke § 17?", "a": "Nei, ikke for dagmulkt (bokstav a). Den løper uansett om du bor gratis hos foreldrene dine. Vil du derimot kreve ekstra erstatning (bokstav c), må du kunne bevise et faktisk økonomisk tap."},
        {"q": "Huset er ferdig, men de har ikke tinglyst skjøtet ennå. Er det forsinkelse?", "a": "Ja. Paragrafen sier uttrykkelig at manglende hjemmelsoverføring også utgjør en forsinkelse."},
        {"q": "Entreprenøren sier jeg ikke kan holde igjen penger fordi det ikke står i kontrakten. Har de rett?", "a": "Absolutt ikke. Loven er ufravikelig. Retten til å holde tilbake penger for forsinkelse er lovfestet i bokstav d, og entreprenøren kan ikke avtale den bort."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "18", "tittel": "Hvordan du regner ut dagmulkten", "available": True},
        {"lov": LOV, "paragraf": "24", "tittel": "Din rett til å holde tilbake betaling", "available": True},
        {"lov": LOV, "paragraf": "10", "tittel": "Reglene for når fristen egentlig går ut", "available": True},
    ],
},
{
    "number": "18",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Slik regner du ut dagmulkten",
    "description": "Lær nøyaktig hvor mange kroner du har krav på for hver dag entreprenøren er forsinket. Loven gir deg en fast sats.",
    "kort_svar": "Dagmulkten er en automatisk økonomisk straff til utbyggeren når de er forsinket. Bygger du på egen tomt, er satsen 1 promille av kontraktssummen per dag. Kjøper du tomt og hus samlet, er satsen 0,75 promille per dag. Du kan kreve dagmulkt i maksimalt 100 dager.",
    "paragraftekst": "Dersom overtaking ikkje kan skje til den tida forbrukaren har rett til å krevje etter §§ 10 og 11, kan forbrukaren krevje dagmulkt for kvar dag forseinkinga varer. Dersom ikkje høgare mulkt er avtalt, skal dagmulkta vere 1 promille av det samla vederlaget entreprenøren skal ha. Omfattar avtalen eigedomsrett til grunnen, skal lågaste sats likevel vere 0,75 promille. Dagmulkta skal ikkje i noko tilfelle vere mindre enn ein halv prosent av grunnsummen i folketrygda på det tidspunktet forseinkinga oppstod. Dagmulkt kan ikkje krevjast for meir enn 100 dagar. Forbrukaren kan krevje dagmulkt utan omsyn til økonomisk tap.",
    "hva_betyr_html": _p(
        "Dette er formelen for hvor mye penger du har krav på ved forsinkelser. Du trenger ikke samle på kvitteringer for ekstra husleie eller leiebil — dagmulkten er flat, automatisk og uavhengig av om du faktisk har tapt penger.",
        "<strong>Bygging på egen tomt:</strong> Hvis du allerede eier tomten, og betaler et firma for å bygge huset, har du krav på 1 promille (0,1 %) av den totale kontraktssummen for hver kalenderdag de er for sene.",
        "<strong>Prosjektbolig (tomt og hus sammen):</strong> Hvis du kjøper bolig og tomt som én pakke fra en utbygger, er tomteprisen bakt inn. Da er satsen litt lavere: 0,75 promille (0,075 %) per dag.",
        "Loven setter også et tak. Dagmulkten stopper når forsinkelsen når 100 dager. Etter det vokser ikke straffebeløpet lenger. Dessuten har loven en minimumsgrense (en halv prosent av G) for at straffen ikke skal bli latterlig lav på veldig billige byggeprosjekter, for eksempel bygging av en liten garasje.",
        "<strong>Regneksempel:</strong> Du har kjøpt en prosjektbolig der tomt og hus koster totalt 5 000 000 kr. Sats: 0,75 promille. 5 000 000 × 0,00075 = 3 750 kr per dag. Forsinket i 14 dager = 52 500 kr i dagmulkt.",
    ),
    "eksempler": [{"navn": "Sara", "tekst": "Sara har en avtale om oppføring av hytte på familiens gamle tomt. Kontraktsummen for hytta er 3 000 000 kr. Snekkeren skulle vært ferdig 1. juni, men hytta ble ikke overlevert før 21. juni (20 dagers forsinkelse). Siden hun bygger på egen tomt, er satsen 1 promille. Sara regner ut: 3 000 000 × 0,001 = 3 000 kr per dag. Ganget med 20 dager blir det 60 000 kroner. Hun trekker disse 60 000 kronene lovlig fra den siste fakturaen hun betaler til snekkeren."}],
    "vanlige_feil": [
        "Å la entreprenøren overtale deg til å ta imot gratis tilvalg (finere parkett) i stedet for dagmulkten — dagmulkten er som regel verdt mye mer i rene penger",
        "Glemme at helger og helligdager også teller med i dagsberegningen",
        "Tro at merverdiavgift (moms) ikke skal være med — dagmulkten regnes av hele kjøpesummen <em>inkludert</em> moms",
    ],
    "hva_bor_du_html": _p(
        "Når forsinkelsen oppstår, regn ut beløpet umiddelbart, slik at du vet hva dagsatsen din er. Gi entreprenøren skriftlig beskjed om at du krever dagmulkt.",
        "Når huset endelig er ferdig, trekker du det totale dagmulkt-beløpet direkte fra sluttoppgjøret. Ikke betal ut pengene for å «kreve dem tilbake» senere. Pengene skal holdes igjen.",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg dagmulkt for lørdag og søndag?", "a": "Ja. Loven sier «for kvar dag». Det betyr alle kalenderdager, inkludert helger, påske, jul og fellesferie."},
        {"q": "Hva skjer når det har gått 100 dager?", "a": "Dagmulkten slutter å løpe. Utbyggeren får ikke mer automatisk straff. Men på det tidspunktet er forsinkelsen så alvorlig at du ofte har rett til å heve avtalen helt, eller kreve erstatning for det <em>faktiske</em> tapet du har fra dag 101 og utover."},
        {"q": "Gjelder prisen med eller uten alle tilvalgene jeg gjorde underveis?", "a": "Dette regnes fra det samlede vederlaget entreprenøren skal ha. Hvis du la til ekstra fliser og et dyrt kjøkken, slik at totalsummen økte, regnes dagmulkten fra den nye, høyere totalsummen."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "17", "tittel": "Vilkårene for når det er en forsinkelse", "available": True},
        {"lov": LOV, "paragraf": "19", "tittel": "Erstatning for dokumentert tap", "available": True},
        {"lov": LOV, "paragraf": "24", "tittel": "Retten din til å holde pengene tilbake", "available": True},
    ],
},
{
    "number": "19",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Når dagmulkten ikke er nok: Erstatning",
    "description": "Har forsinkelsen kostet deg hundretusener i ekstra leie og lagerleie? Du kan kreve erstatning utover dagmulkten, men bare i spesielle tilfeller.",
    "kort_svar": "Dagmulkten er vanligvis det eneste du får ved forsinkelse, selv om det faktiske tapet ditt er større. Unntaket er hvis entreprenøren har vært grovt uaktsom eller uærlig. Da kan du kreve erstatning for hver eneste krone du har tapt, som dyre hotellregninger eller dobbelt boliglån.",
    "paragraftekst": "Forbrukaren kan berre krevje skadebot for tap som overstig dagmulkta, dersom tapet kjem av at entreprenøren eller nokon som entreprenøren svarer for, har fare fram grovt aktlaust eller i strid med heider og god tru elles. I tidsrom når det ikkje vert rekna dagmulkt, kan forbrukaren krevje skadebot a) for tap som følgjer av at arbeidet eller delar av arbeidet ikkje er fullført til den tida forbrukaren kan krevje, b) for tap som følgjer av at heimelsoverføring ikkje skjer til den tida forbrukaren kan krevje. Skadebota skal dekkje økonomisk tap så langt entreprenøren rimeleg kunne rekne med tapet som ei følgje av forseinkinga. Forsømer forbrukaren å avgrense tapet gjennom rimelege tiltak, blir skadebota sett ned tilsvarande. For skadebot i hevingstilfella gjeld § 22.",
    "hva_betyr_html": _p(
        "Dagmulktordningen (§ 18) er laget for å gjøre ting enkelt. Det er en flat sats, slik at verken du eller utbygger trenger å krangle om kvitteringer. Ulempen er at hvis forsinkelsen påfører deg enorme kostnader som er større enn dagmulkten dekker, må du vanligvis bære det tapet selv.",
        "Paragraf 19 gir deg imidlertid en sikkerhetsventil. Hvis entreprenøren har opptrådt «grovt aktlaust» (grovt skjødesløst) eller direkte uærlig, kan du kreve erstatning (skadebot) for hele det overskytende tapet ditt. Grovt uaktsomt betyr at de har gitt fullstendig blaffen. Et eksempel kan være at de lyver om at huset er ferdig slik at du selger den gamle boligen din, for så å innrømme at de mangler taket.",
        "Loven stiller også et strengt krav til deg: Du har plikt til å begrense tapet ditt. Må du leie et sted å bo på grunn av forsinkelsen, kan du leie en normal, nøktern leilighet. Tar du inn på luksushotell til 5 000 kroner natten, vil entreprenøren nekte å betale for hele beløpet fordi du ikke prøvde å redusere kostnaden.",
        "<strong>Etter dag 100:</strong> Dagmulkten stopper automatisk etter 100 dager. Andre avsnitt sier at i tidsrom hvor dagmulkten ikke løper (fra dag 101 og fremover), kan du kreve full erstatning for det faktiske, økonomiske tapet ditt uansett om entreprenøren var grovt uaktsom eller bare uheldig. Da må du fremlegge kvitteringer.",
    ),
    "eksempler": [{"navn": "Tom", "tekst": "Tom bygger hus og opplever at entreprenøren, uten å gi beskjed, tar med seg alle snekkerne over til et annet mer innbringende prosjekt i to måneder. Huset blir forsinket. Toms dagmulkt utgjør 30 000 kroner, men han måtte leie bolig og lager til 70 000 kroner i samme periode. Å forlate en byggeplass bevisst for å tjene penger et annet sted, er grovt uaktsomt. Tom kan derfor bruke § 19 til å kreve de resterende 40 000 kronene dekket som erstatning utover dagmulkten."}],
    "vanlige_feil": [
        "Å kreve erstatning for ekstra bokostnader på toppen av dagmulkten ved <em>vanlige</em> forsinkelser — du får kun dagmulkten med mindre det er grov uaktsomhet",
        "Å ikke ta vare på kvitteringer for lagerleie og ekstra husleie",
        "Leie dyre boliger uten å vurdere rimeligere alternativer for å begrense tapet",
    ],
    "hva_bor_du_html": _p(
        "Hvis forsinkelsen skyldes at entreprenøren har gjort grove feil eller løyet, begynn umiddelbart å samle bevis. Ta vare på alle kvitteringer for ekstra bo-utgifter, transport, mellomfinansiering i banken og lagerleie.",
        "Send et skriftlig varsel der du sier at du vil kreve tapet erstattet fordi du mener de har opptrådt grovt uaktsomt etter § 19. Siden «grov uaktsomhet» er en streng juridisk terskel, lønner det seg ofte å bruke en advokat for å formulere dette kravet riktig.",
    ),
    "dumme_sporsmal": [
        {"q": "Hva om snekkeren gjorde en ærlig feilmåling som forsinket hele bygget?", "a": "En ærlig tabbe regnes sjelden som <em>grovt</em> uaktsomt. Da er det bare vanlig uaktsomhet. I slike tilfeller er det kun den flate dagmulkten som gjelder, selv om regningen din for mellomfinansiering overstiger dagmulkten."},
        {"q": "Hva menes med å «avgrense tapet»?", "a": "Det betyr at du må opptre fornuftig for å spare penger der du kan. Hvis du må leie bod til møblene dine, skal du velge et minilager til normal pris, og ikke det dyreste og mest eksklusive lageret i byen."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "18", "tittel": "Den faste dagmulkten som normalt dekker alt", "available": True},
        {"lov": LOV, "paragraf": "22", "tittel": "Erstatning hvis du må heve (kansellere) hele avtalen", "available": True},
        {"lov": LOV, "paragraf": "17", "tittel": "Vilkårene for forsinkelse", "available": True},
    ],
},
{
    "number": "20",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Slik kansellerer du byggekontrakten",
    "description": "Er forsinkelsen blitt helt ekstrem, og fremdriften har stoppet opp? Loven gir deg en nødutgang: Du kan heve (kansellere) hele avtalen.",
    "kort_svar": "Hvis forsinkelsen er et vesentlig avtalebrudd — altså at prosjektet er alvorlig på etterskudd, eller snekkeren har forlatt plassen helt — kan du heve avtalen. Det betyr at du bryter kontrakten, sparker utbyggeren, og står fritt til å leie inn noen andre. Du må gi beskjed om dette før du tar over huset.",
    "paragraftekst": "Forbrukaren kan heve avtalen dersom forseinkinga inneber eit vesentleg avtalebrot. Forbrukaren kan òg heve avtalen dersom det er klårt at det kjem til å oppstå forseinking som nemnd i første punktum. Forbrukaren kan berre heve avtalen dersom det er gjeve melding til entreprenøren om hevingskravet før overtaking. Vert avtalen med entreprenøren heva fordi entreprenørens yting er forseinka, kan forbrukaren òg heve avtale om rett til grunnen som er gjort med nokon annan enn entreprenøren dersom a) planlegging og oppføring av bustaden er eit vilkår for avtalen om rett til grunnen, og b) avtalen med entreprenøren omfattar det hovudsaklege av både planlegging og oppføring av bustaden. I slike tilfelle kan forbrukaren jamvel heve avtalen med entreprenøren dersom avtalen om rett til grunnen blir heva på grunn av forseinking. Blir begge avtalane heva, skal hevingsoppgjeret skje etter § 21 tredje ledd.",
    "hva_betyr_html": _p(
        "Å heve en kontrakt er den kraftigste reaksjonen du har i norsk rett. Det er en juridisk atomknapp. Du river i praksis i stykker avtalen fordi den andre parten har sviktet fundamentalt.",
        "For at du skal kunne trykke på denne knappen, krever loven at forsinkelsen er et «vesentleg avtalebrot». Det holder ikke at huset er en måned forsinket fordi vinduene kom sent. Forsinkelsen må være ekstrem, slik at selve meningen med kontrakten faller bort for deg — for eksempel at entreprenøren stopper arbeidet og forsvinner, eller at forsinkelsen har passert de 100 dagene med dagmulkt og det fremdeles ikke er tegn til ferdigstillelse.",
        "Loven lar deg også «se inn i fremtiden» (kalt antesipert mislighold). Hvis du ser i juli at entreprenøren ikke en gang har støpt grunnmuren, og overlevering er i august, er det åpenbart at de ikke vil klare fristen. Da kan du heve avtalen allerede i juli.",
        "Du har også en absolutt frist: Du kan ikke flytte inn, akseptere boligen på overtakelse, og <em>deretter</em> kreve heving fordi den var forsinket. Hevingskravet må skrives og sendes før overtakelsen.",
    ),
    "eksempler": [{"navn": "Ingrid", "tekst": "Ingrid inngikk kontrakt med et tømrerfirma i mars. Fristen for ferdig hus var desember. I september har firmaet kun satt opp reisverket, og de har ikke vært på byggeplassen på to måneder fordi de tok et annet oppdrag. Ingrid sender dem først et varsel med en kort frist for å gjenoppta arbeidet. Når ingenting skjer, og forsinkelsen anslås til å bli mange måneder, sender Ingrid en formell hevingserklæring. Avtalen avsluttes, og Ingrid leier inn et nytt firma til å bygge videre på reisverket."}],
    "vanlige_feil": [
        "Å heve avtalen i sinne over en normal, ukerslang forsinkelse — gjør du dette uten at lovens strenge vilkår er oppfylt, blir det ansett som om <em>du</em> bryter kontrakten, og utbygger kan saksøke deg for tapt fortjeneste",
        "Å ikke gi utbygger en siste, skriftlig sjanse (tilleggsfrist) før man hever",
        "Å glemme å sende hevingskravet skriftlig",
    ],
    "hva_bor_du_html": _p(
        "Ikke hev en byggekontrakt alene. Terskelen for «vesentlig avtalebrudd» er skjønnsmessig og komplisert. Kontakt en advokat.",
        "Det advokaten normalt vil gjøre, er å skrive et varsel til entreprenøren der det står: «Dersom normal framdrift ikke er gjenopptatt innen 14 dager, vil avtalen heves etter § 20.» Dette gir snekkeren en siste sjanse, og gjør din egen sak bunnsolid i retten hvis de ikke dukker opp.",
        "<strong>Hvis du hever uberettiget</strong> kalles det «erstatningsbetingende mislighold». Da kan entreprenøren snu situasjonen mot deg, og kreve at du betaler ut millionene de skulle tjent på å bygge huset ditt. Derfor må du være sikker i din sak.",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg tilbake alle pengene jeg har betalt når jeg hever?", "a": "Dette styres av § 21. Bygger de på din tomt, beholder du det de har bygget, og betaler dem for verdien av dette. Har du kjøpt tomt og hus sammen (prosjekt), får du som regel alle pengene tilbake mot at de beholder tomta og huset."},
        {"q": "Kan jeg heve kontrakten fordi de har brukt feil farge på kledningen?", "a": "Ikke etter denne paragrafen. § 20 gjelder heving på grunn av <em>forsinkelse</em>. Hvis problemet er at arbeidet er dårlig utført eller har feil (mangel), er det § 34 du må bruke. Vilkåret om vesentlig avtalebrudd gjelder der også."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "21", "tittel": "Det økonomiske oppgjøret etter at du har hevet", "available": True},
        {"lov": LOV, "paragraf": "22", "tittel": "Erstatning fordi du måtte heve", "available": True},
        {"lov": LOV, "paragraf": "34", "tittel": "Heving på grunn av store feil (mangler)", "available": True},
    ],
},
{
    "number": "21",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Hvem får hva når du har hevet kontrakten?",
    "description": "Du har sparket utbyggeren for løftebrudd. Hvordan gjør dere opp regningen? Lær hvem som eier huset og materialene som ligger igjen på tomta.",
    "kort_svar": "Når avtalen kanselleres (heves) midt i byggingen, skal entreprenøren ha betalt for den delen av huset som er riktig bygget så langt. Du har rett til å ta over materialene som ligger på byggeplassen for å fullføre arbeidet. Er det en prosjektbolig (tomt+hus), kan oppgjøret gjøres ved at de får tilbake boligen og du får tilbake alle pengene dine.",
    "paragraftekst": "Vert avtalen heva, har entreprenøren krav på vederlag for det som er utført i samsvar med avtalen. Vederlaget skal fastsetjast på grunnlag av dei prisane som er avtalt, eller dersom dette ikkje let seg gjere, etter føresegnene i § 41 andre ledd. Etter heving skal entreprenøren i rimeleg omfang sikre utført arbeid og materialar og utstyr som finst på byggjeplassen. Forbrukaren har rett til å gjere seg nytte av utstyr og materialar som finst på byggjeplassen, og som trengst til fullføringa av arbeidet. For den bruken skal det betalast eit rimeleg vederlag. Ved avtalar om rett til fast eigedom med ny eigarbustad, kan forbrukaren krevje at hevingsoppgjeret, i staden for etter første og andre ledd, skal skje ved at kvar parts plikt til å oppfylle fell bort. Er avtalen heilt eller delvis oppfylt, har kvar part krav på å få att det som er ytt. Entreprenøren kan krevje vederlag for verdireduksjon som forbrukaren svarer for. Ein part kan likevel halde attende det som er motteke, til den andre parten gjev frå seg det mottekne.",
    "hva_betyr_html": _p(
        "Et brudd i en byggekontrakt er et rotete «skilsmisseoppgjør». Huset står der halvferdig, og hagen er full av isolasjon. § 21 bestemmer hvordan delingen foregår.",
        "<strong>For deg som bygger på egen tomt:</strong> Utbyggeren får sparken. Men de har tross alt støpt en fin grunnmur og satt opp reisverket riktig før de rotet det til. Loven sier at du skal betale dem for verdien av det de faktisk har bygget <em>riktig</em>. Samtidig sier andre ledd at utbygger ikke kan ta med seg vinduene og isolasjonen som ligger klart på tomta for å hevne seg. Du har lovfestet rett til å bruke disse materialene (og stillaset) for å bygge ferdig med nye håndverkere — du betaler selvsagt en rettferdig pris for materialene til den sparkede entreprenøren.",
        "<strong>For deg som kjøper prosjekt (tomt og hus sammen):</strong> Tredje ledd er for deg. Hvis du hever en slik kontrakt, betyr det vanligvis «alt leveres tilbake». Entreprenøren beholder tomten og halvbygget, og de må tilbakebetale alle hundretusener du har innbetalt i forskudd, med renter.",
        "<strong>Sikring av byggeplassen:</strong> Når du sier «du er sparket», kan ikke håndverkerne bare slippe hammeren og reise hjem. Loven krever at de sikrer byggeplassen. De må slenge en presenning over taket slik at det ikke regner inn i reisverket før du får en ny snekker på plass.",
    ),
    "eksempler": [{"navn": "Lars", "tekst": "Lars bygger hytte på fjellet. Entreprenøren stopper arbeidet på grunn av pengemangel. Lars hever avtalen rettmessig. Fundamentet og veggene er satt opp og verdsettes til 400 000 kr. På plassen ligger det vinduer verdt 50 000 kr som entreprenøren har kjøpt inn. Lars holder tilbake vinduene og bruker dem når det nye firmaet tar over. Lars skylder den første entreprenøren 450 000 kr totalt, men siden Lars har lidt store ekstra utgifter på grunn av bruddet, trekker han fra sitt erstatningskrav (etter § 22) før han betaler den første entreprenøren."}],
    "vanlige_feil": [
        "Å betale full pris for det halvferdige bygget, uten å trekke fra de ekstra kostnadene det innebærer å få et nytt firma til å overta",
        "La den oppsagte entreprenøren hente tilbake paller med materialer som du strengt tatt trengte for å bygge ferdig",
    ],
    "hva_bor_du_html": _p(
        "I det sekundet kontrakten er hevet, må du sikre bevis. Lei umiddelbart inn en uavhengig takstmann som går gjennom byggeplassen med et kamera. De skal lage en nøyaktig verditakst av nøyaktig hva som er bygget, hva det er verdt, og hvor mye materialer som ligger på tomta.",
        "Denne rapporten blir fasiten i det økonomiske oppgjøret. Ikke la den nye entreprenøren slå inn en eneste spiker før denne dokumentasjonen er sikret.",
    ),
    "dumme_sporsmal": [
        {"q": "Hva om fundamentet de la er ubrukelig og skjevt? Må jeg betale for det?", "a": "Nei. Paragrafen sier de har krav på vederlag for det som er «utført i samsvar med avtalen». Er det bygget feil og må rives, har det negativ verdi. Da skal du ikke betale, og du kan kreve rivningskostnadene dekket."},
        {"q": "Har entreprenøren krav på å ta med verktøyet sitt?", "a": "Ja, maskiner og verktøy tilhører dem, med mindre det ligger der som «utstyr» du trenger i en kortere periode (f.eks. et montert stillas som ikke bare kan demonteres uten at huset skades)."},
        {"q": "Kan utbygger kreve penger for at boligen har falt i verdi mens vi kranglet?", "a": "Hvis du har bodd i boligen og den leveres tilbake, kan de kreve penger for «verdireduksjon som forbrukeren svarer for» (slitasje eller skade du har påført). Prisfall i markedet generelt må utbyggeren bære selv."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "22", "tittel": "Hvordan du krever dekket dine merkostnader", "available": True},
        {"lov": LOV, "paragraf": "20", "tittel": "Vilkårene for at du kan heve avtalen", "available": True},
        {"lov": LOV, "paragraf": "41", "tittel": "Hvordan prisen fastsettes", "available": True},
    ],
},
{
    "number": "22",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Få dekket tapet ditt når kontrakten heves",
    "description": "Å måtte bytte snekker midt i byggingen koster dyrt. Loven lar deg kreve disse ekstra kostnadene dekket av den som fikk sparken.",
    "kort_svar": "Når du har hevet avtalen på grunn av utbyggers forsinkelser, blir det ofte dyrere å få et nytt firma til å bygge ferdig huset. Disse ekstra kostnadene kan du kreve dekket (erstatning) fra den første entreprenøren.",
    "paragraftekst": "Ved heving kan forbrukaren krevje dekt nødvendige meirkostnader som følgjer av at andre må fullføre arbeidet. I tillegg kan forbrukaren krevje bøtt anna økonomisk tap som forseinkinga fører til, så langt entreprenøren rimeleg kunne rekne med tapet som ei følgje av forseinkinga. Forsømer forbrukaren å avgrense tapet gjennom rimelege tiltak, blir skadebota sett ned tilsvarande. Forbrukaren kan ikkje krevje dagmulkt for tida etter hevinga, og pådregen dagmulkt går til frådrag i skadebot etter første ledd andre punktum.",
    "hva_betyr_html": _p(
        "Når et byggeprosjekt krasjer, er du som forbruker beskyttet økonomisk. Den opprinnelige utbyggeren kan ikke bare forsvinne og la deg sitte igjen med ekstraregningen.",
        "Dette kalles «dekningskjøp». La oss si at det gjensto arbeid på huset for 1 million kroner i den gamle kontrakten. Du ansetter en ny snekker til å bygge huset ferdig, men de må ha 1,3 millioner kroner fordi de må sette seg inn i andres rot og gi garanti på jobben. Forskjellen på 300 000 kroner er en «nødvendig meirkostnad». Denne regningen kan du sende direkte til den første entreprenøren.",
        "I tillegg kan du kreve erstatning for leieutgifter til midlertidig bolig eller lagringsplass i den perioden huset er forsinket. Loven slår fast at hvis du hever kontrakten, stopper imidlertid de faste dagbøtene. Erstatningen din erstatter da dagmulkten. Hvis du allerede hadde tjent opp 50 000 i dagmulkt da du hevet, skal dette beløpet trekkes fra i regnestykket over det ekstra tapet ditt, slik at du ikke får betalt dobbelt opp for samme ulempe.",
        "<strong>Plikt til å begrense tapet:</strong> Du må avgrense tapet. Du kan ikke bare huke tak i byens dyreste arkitekt og tømrerfirma for å rette opp feilene, for så å sende regningen. Du har plikt til å innhente et par tilbud og velge en fornuftig og rimelig løsning for å få huset ferdigstilt.",
    ),
    "eksempler": [{"navn": "Håkon", "tekst": "Håkon hever byggekontrakten på 4 millioner kroner rettmessig etter to måneders stillstand (og 30 000 i opptjent dagmulkt). Han hadde betalt 2 millioner så langt. Han får inn tre tilbud fra nye håndverkere for å ferdigstille huset. Det billigste, seriøse tilbudet er på 2,5 millioner. Huset vil da koste Håkon totalt 4,5 millioner. Siden den opprinnelige prisen var 4 millioner, er merkostnaden 500 000 kroner. Håkon krever dette beløpet som erstatning fra første utbygger."}],
    "vanlige_feil": [
        "Å bare innhente ett (og veldig dyrt) tilbud fra en bekjent for å fullføre arbeidet — det vil fort bli avvist i retten fordi du ikke har «avgrenset tapet»",
        "Å tro at man kan få både full dagmulkt <em>og</em> full erstatning for tapt husleie på toppen av hverandre for samme tidsrom",
    ],
    "hva_bor_du_html": _p(
        "Når du skal ha inn nye folk til å fullføre huset ditt, må du være ryddig. Be om skriftlige tilbud fra minst to, helst tre, uavhengige og seriøse firmaer. Gi dem den opprinnelige leveransebeskrivelsen, slik at de gir pris på akkurat det samme som den sparkede entreprenøren skulle levert.",
        "Når du velger det rimeligste av disse, har du et bunnsolid bevis på at merkostnaden er nødvendig, og kravet ditt mot den første utbyggeren vil som regel stå seg i retten.",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg erstatning for at dette har vært en psykisk påkjenning for meg?", "a": "Nei. Norsk erstatningsrett i bygge- og kontraktssaker dekker utelukkende dokumentert <em>økonomisk</em> tap. Søvnløshet, stress og frustrasjon gir ikke rett på penger (tort og svie) etter bustadoppføringslova."},
        {"q": "Entreprenøren gikk konkurs, så jeg får vel aldri de pengene uansett?", "a": "Her kommer den lovpålagte garantien (§ 12) inn som en reddende engel. Ekstrakostnadene for å få huset ferdig er nøyaktig det denne bankgarantien er til for å dekke. Du retter da erstatningskravet ditt mot banken som har utstedt garantien, ikke det konkursrammede firmaet."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "19", "tittel": "Vanlige erstatningskrav (når du ikke hever)", "available": True},
        {"lov": LOV, "paragraf": "12", "tittel": "Bankgarantien som gjør at du faktisk får pengene", "available": True},
        {"lov": LOV, "paragraf": "21", "tittel": "Det økonomiske oppgjøret etter heving", "available": True},
    ],
},
{
    "number": "23",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Når utbyggers regning blir urettferdig stor",
    "description": "Entreprenører kan be om nåde (lemping) hvis dagmulkten og erstatningskravet ditt blir helt uforsvarlig stort og slår dem konkurs.",
    "kort_svar": "Hvis dagmulkten og erstatningskravene dine blir så høye at det virker fullstendig urimelig og ødeleggende for entreprenøren i forhold til feilen som ble gjort, har domstolene lov til å sette ned (lempe) beløpet du får utbetalt.",
    "paragraftekst": "Dagmulkt eller skadebot kan setjast ned dersom det vil verke urimeleg for entreprenøren ut frå omfanget av arbeidet, storleiken av tapet og tilhøva elles.",
    "hva_betyr_html": _p(
        "Dette er en sjelden, men viktig unntaksregel. Loven er designet for å være tøff mot entreprenørene for å beskytte deg som forbruker. Men den skal ikke være blind.",
        "Lemping er en «sikkerhetsventil» for utbyggerne. Hvis forsinkelsen er langvarig, og du bygger et gigantisk, svindyrt hus, kan 100 dager med dagmulkt og et gigantisk erstatningskrav kanskje beløpe seg til flere millioner kroner. Kanskje problemet bare var at en spesiell dør var forsinket fra fabrikken. Å kreve 2 millioner av tømrerfirmaet fordi døren mangler, vil kunne velte hele bedriften.",
        "Da kan entreprenøren kreve lemping. En dommer vurderer da om kravet ditt står i forhold til selve byggeoppdraget. Var det en liten jobb, men erstatningen ble gigantisk? Da kan dommeren bestemme at «ja, du har rett på erstatning, men vi reduserer beløpet til en halv million».",
        "<strong>Bør du være redd for å miste kravet ditt?</strong> Nei. Terskelen for å bruke § 23 er svært høy i Norge. Det skal veldig mye til for at en forbruker mister den dagmulkten som er utregnet etter loven.",
    ),
    "eksempler": [{"navn": "Kari og rørleggeren", "tekst": "Kari inngår en mindre kontrakt på 150 000 kr med et lite rørleggerfirma for montering av noen rør i huset. Rørleggeren gjør en uaktsom feil, det oppstår en flom, og halve underetasjen hennes blir ødelagt. Erstatningskravet Kari og forsikringsselskapet krever fra rørleggeren er på 3,5 millioner kroner. Det lille rørleggerfirmaet har av en eller annen grunn ikke dekning for akkurat denne skaden. Retten vurderer saken og mener at 3,5 millioner er urimelig ruinerende i forhold til oppdragets lille størrelse på 150 000 kr, og setter skadeboten noe ned etter lempingsregelen i § 23."}],
    "vanlige_feil": [
        "At entreprenører truer med «lemping» på småbeløp (f.eks. en dagmulkt på 60 000 kr) — det kommer de aldri noen vei med",
        "Å tro at lemping gjelder uavhengig av om entreprenøren har tabbet seg ut — hvis de har vært grovt uaktsomme (løyet eller oversett grove feil), skal det nesten et mirakel til for at de får medhold",
    ],
    "hva_bor_du_html": _p(
        "Stå på kravene dine. Du skal alltid kreve det maksimale beløpet loven gir deg rett på etter §§ 18, 19 og 22.",
        "Ikke gi rabatt til utbygger bare fordi de sier «det blir for dyrt for oss». Hvis beløpet faktisk er urimelig, må det avgjøres av domstolene (eller Forbrukertilsynet), ikke av en gråtende snekker på telefonen.",
    ),
    "dumme_sporsmal": [
        {"q": "Kan jeg kreve lemping av regningen jeg skal betale til dem?", "a": "Nei. § 23 beskytter utelukkende entreprenøren mot gigantiske <em>straffekrav</em> (dagmulkt og erstatning). For prisen på selve huset er du beskyttet av reglene om prisoverslag og justering i kapittel V."},
        {"q": "Kan de kreve lemping hvis de har god ansvarsforsikring?", "a": "Nei. Hvis entreprenørens forsikringsselskap betaler regningen, rammer ikke erstatningen entreprenørens økonomi på en urimelig måte. Da skal full erstatning utbetales til deg."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "18", "tittel": "Lovens strenge formel for dagmulkt", "available": True},
        {"lov": LOV, "paragraf": "19", "tittel": "Erstatning for forsinkelser", "available": True},
        {"lov": LOV, "paragraf": "22", "tittel": "Erstatning ved heving", "available": True},
    ],
},
{
    "number": "24",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Hold tilbake penger hvis huset er forsinket",
    "description": "Du er din egen bank. Hvis entreprenøren er forsinket, har du lovfestet rett til å nekte å betale sluttoppgjøret inntil kravet ditt er dekket.",
    "kort_svar": "Hvis bygget blir forsinket slik at du tjener opp dagmulkt eller andre krav mot utbygger, kan du fryse innbetalingen av sluttoppgjøret. Du kan holde tilbake nøyaktig like mye penger som du mener de skylder deg.",
    "paragraftekst": "Har forbrukaren krav som følgje av forseinkinga, kan forbrukaren halde tilbake så mykje av vederlaget som er nødvendig for å sikre at kravet vert dekt.",
    "hva_betyr_html": _p(
        "Dette er ditt desidert mest effektive maktmiddel. Penger er det eneste språket alle entreprenører forstår.",
        "Hvis snekkeren har vært forsinket i 20 dager, og du vet at dette utgjør 60 000 kroner i dagmulkt (etter § 18), skal du ikke betale fakturaene deres som normalt. Siste faktura (sluttoppgjøret) før du får nøkkelen, vil vanligvis være på et høyt beløp. Loven sier at du da har rett til å si: «Jeg betaler ikke de siste 60 000 kronene, fordi det tilsvarer det dere nå skylder meg for forsinkelsen.»",
        "Dette kalles tilbakeholdsrett. Poenget er at du sikrer pengene dine. Hvis du betaler fullt ut, og heller stoler på at utbyggeren betaler deg dagmulkten tilbake neste måned, har du gjort deg selv om til bank. Hvis firmaet da går konkurs uken etter, har du tapt de 60 000 kronene.",
        "Paragrafen setter imidlertid én begrensning: «Så mye som er nødvendig». Er kravet ditt på 60 000 kr, kan du ikke nekte å betale en regning på én million. Du betaler 940 000, og fryser 60 000 kr.",
    ),
    "eksempler": [{"navn": "Jonas", "tekst": "Jonas bygger hytte. Hytta overleveres 14 dager for sent, noe som gir ham et lovfestet krav på 28 000 kr i dagmulkt. Utbyggeren sender en sluttfaktura på 200 000 kroner før overtakelsen, og krever at pengene er på konto for at Jonas skal få nøkkelen. Jonas svarer skriftlig: «Jeg betaler 172 000 kroner. De resterende 28 000 kronene holdes tilbake etter bustadoppføringslova § 24 som dekning for opptjent dagmulkt.» Utbyggeren må godta dette og gi Jonas nøkkelen."}],
    "vanlige_feil": [
        "Å føle seg presset til å betale alt fordi utbygger sier «vi gir deg ikke nøkkelen før 100 % av fakturaen er innbetalt» (dette er ulovlig utpressing)",
        "Holde tilbake altfor mye penger «bare for å være sikker» — er du urimelig i anslaget ditt, er det <em>du</em> som bryter betalingsfristen",
        "Holde tilbake pengene uten å si ifra hvorfor — da ser det bare ut som en ubetalt regning",
    ],
    "hva_bor_du_html": _p(
        "Regn ut kravet ditt på krona (bruk formelen i § 18). Så legger du kanskje på et lite påslag for eventuelt dokumentert tap på toppen. Trekk denne eksakte summen fra regningen.",
        "Du MÅ skrive en e-post der du informerer om trekket og lovhjemmelen. Penger du «ikke betaler» uten forklaring, er bare en ubetalt regning som går til inkasso. Penger du «holder tilbake skriftlig etter loven», blokkerer inkasso og tvinger utbyggeren til å håndtere saken din.",
    ),
    "dumme_sporsmal": [
        {"q": "Utbygger sier jeg må sette de tilbakeholdte pengene inn på en spesiell konto de disponerer. Stemmer det?", "a": "Nei, men etter § 49 kan det avtales «deponering» av omstridte penger. Det krever at pengene står på en sperret bankkonto som verken du eller entreprenøren kan ta ut av alene. De skal ikke overføres til deres private firma-konto."},
        {"q": "Entreprenøren nekter overtakelse fordi jeg holder tilbake dagmulkten. Er det lov?", "a": "Nei. Hvis du holder tilbake penger helt i tråd med loven for et rettmessig krav, og boligen ellers er ferdig, har entreprenøren ikke rett til å nekte overtakelse. Gjør de det, løper dagmulkten bare videre, for da er jo huset <em>fremdeles</em> ikke overlevert."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "31", "tittel": "Tilbakeholdsrett ved fysiske feil (mangler)", "available": True},
        {"lov": LOV, "paragraf": "49", "tittel": "Hvordan deponere omstridte penger i bank", "available": True},
        {"lov": LOV, "paragraf": "18", "tittel": "Slik regner du ut hvor mye du kan holde igjen", "available": True},
    ],
},
{
    "number": "25",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Hva er egentlig en byggefeil (mangel)?",
    "description": "Har du funnet noe feil med huset? Denne paragrafen slår fast hva som juridisk regnes som en «mangel» du kan klage på.",
    "kort_svar": "Det er en feil (mangel) hvis boligen ikke ser ut eller fungerer slik det står i kontrakten, eller hvis snekkeren har brutt regelen om godt og fagmessig håndverk. Det er også en mangel hvis huset bryter offentlige lover og byggeforskrifter (TEK).",
    "paragraftekst": "Det ligg føre mangel dersom resultatet ikkje er i samsvar med dei krava som følgjer av avtalen eller av føresegnene i §§ 7, 9 og 13. Mangel ligg likevel ikkje føre dersom avviket kjem av forhold på forbrukarens side. Mangel ligg òg føre dersom resultatet ikkje er i samsvar med offentlegrettslege krav som er stilt i lov eller i medhald av lov. Dette gjeld likevel ikkje dersom tilhøva viser at forbrukaren for så vidt ikkje bygde på entreprenørens sakkunnskap og vurdering, eller ikkje hadde rimeleg grunn til å gjere det.",
    "hva_betyr_html": _p(
        "Dette er inngangsbilletten din til å kreve retting og erstatning etter at huset er bygget. Loven definerer feil (mangler) ut fra to spor:",
        "<strong>1. Brudd på kontrakten:</strong> Har du bestilt hvite kjøkkenskap, og de har montert sorte? Det er en mangel, uansett hvor fine de sorte er. Har du krevd eikeparkett, og de la laminat? Mangel. I tillegg peker loven tilbake til § 7: Hvis arbeidet ser elendig ut og ikke følger standarden for «godt håndverk» (f.eks. knusktørr, knirkende parkett og ujevn maling), er det en mangel selv om fargen er riktig.",
        "<strong>2. Brudd på byggereglene (TEK):</strong> Selv om det i kontrakten bare står «bygg et bad», finnes det strenge offentlige regler for hvordan et bad skal bygges (ofte kalt TEK17). Mangler det smøremembran under flisene, er badet ulovlig bygget. Det er da en soleklar mangel etter § 25, og utbyggeren må betale for å rive alt og gjøre det lovlig — selv om kontrakten dere imellom var vag.",
        "<strong>Unntaket:</strong> Hvis feilen er din egen skyld. Bestilte du feil vinduer på egen hånd, eller rotet bort leveransen din av lister, kan du ikke kalle det en «mangel» fra utbyggers side.",
    ),
    "eksempler": [{"navn": "Sofie", "tekst": "Sofie har overtatt sin nye bolig. Hun leier inn et uavhengig takstfirma for å sjekke arbeidet. Takstmannen finner at avtrekksviften på badet ikke trekker ut nok liter luft per sekund etter kravene i teknisk forskrift (TEK17). Dessuten oppdager han at flisene i stua ikke er «store grå italienske» slik det stod i kontrakten, men en billigere, lys versjon. Begge deler er mangler etter § 25. Den ene fordi kontrakten er brutt (feil farge), og den andre fordi den bryter Norges lover (offentlig krav til ventilasjon). Utbygger må rette begge deler."}],
    "vanlige_feil": [
        "Å tro at man ikke kan klage på manglende membran fordi man ikke spesifiserte membran i avtalen — offentlige lover dekker deg her",
        "At utbyggere påstår feilen «ikke er så farlig» siden bygget fungerer — et kontraktsbrudd er en mangel selv om det fungerer",
        "Tro at vanlig slitasje og skitt etter to års bruk er en «mangel» — mangler er feil som oppstod under bygging",
    ],
    "hva_bor_du_html": _p(
        "Når du mistenker en feil, slå opp i Norsk Standard eller byggforsk-bladene, eller engasjer en bygningssakkyndig (takstmann).",
        "Hvis de skriver i sin rapport at «utførelsen ikke er i samsvar med TEK17», har du en klinkende klar mangel å slå i bordet med. Da er loven i stor grad på din side.",
    ),
    "dumme_sporsmal": [
        {"q": "Hva om jeg ba utbyggeren uttrykkelig om å droppe membran for å spare penger?", "a": "Her fanger lovens siste setning deg. Loven sier at offentlighetsbrudd ikke er utbyggers ansvar «dersom tilhøva viser at forbrukaren ikkje bygde på entreprenørens sakkunnskap». Har du presset frem en løsning som bryter loven, og utbyggeren (etter rådgivningsplikten sin) sa nei, men du insisterte, er ulovligheten ditt problem, ikke deres."},
        {"q": "Det trekker kaldt fra vinduene. Er det en mangel?", "a": "Hvis trekk og isolasjonsevne er dårligere enn det byggekravene på byggetidspunktet tillater, er det en mangel. Hvis alt er bygget riktig etter teknisk standard, men det likevel er litt gulvkaldt, er det <em>ikke</em> en mangel. Alt handler om hva som var lovpålagt standard da byggetillatelsen ble gitt."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "26", "tittel": "Manglende eller feil opplysninger er også en mangel", "available": True},
        {"lov": LOV, "paragraf": "29", "tittel": "Hvilke krav du kan fremme når huset har en mangel", "available": True},
        {"lov": LOV, "paragraf": "32", "tittel": "Din rett til å kreve retting", "available": True},
    ],
},
{
    "number": "26",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Entreprenøren holdt tilbake viktig informasjon",
    "description": "Visste utbyggeren noe negativt om tomten eller materialene, men lot være å fortelle deg det? Loven kaller dette en mangel.",
    "kort_svar": "Det regnes som en byggefeil (mangel) hvis entreprenøren holdt skjult viktig informasjon som de visste om, og som du hadde grunn til å forvente å få. Dette gjelder hvis informasjonen ville gjort at du ikke signerte kontrakten, eller krevde en lavere pris.",
    "paragraftekst": "Mangel ligg òg føre dersom forbrukaren før avtalen vart gjord ikkje har fått opplysningar om arbeidet, materialane eller eigedomen som entreprenøren kjende eller måtte kjenne til, og som forbrukaren hadde grunn til å rekne med å få. Dette gjeld likevel berre dersom ein kan gå ut i frå at det har verka inn på avtalen at opplysningane ikkje vart gjevne.",
    "hva_betyr_html": _p(
        "Når du kjøper en ny bolig eller bygger et hus, stoler du på at fagfolkene er ærlige med deg. § 26 beskytter deg mot utbyggere som tier om negative ting for å få i havn et salg.",
        "Loven sier at hvis entreprenøren visste om noe vesentlig, og holdt kjeft, er selve huset mangelfullt. Et klassisk eksempel er at de vet at tomten tidligere har vært en søppelfylling som kan sige, eller at de vet at naboen nettopp har fått godkjent bygging av en blokk som vil ta all solen din.",
        "For at du skal vinne frem med dette, krever loven to ting. For det første må det være noe de «måtte kjenne til». De kan ikke straffes for ting de umulig kunne vite om. Men de kan heller ikke lukke øynene — som proffe aktører plikter de å sjekke reguleringsplaner for området. For det andre må det ha «verka inn på avtalen». Det betyr at hvis du hadde fått vite om blokken naboen skal bygge, hadde du enten nektet å kjøpe huset, eller du hadde krevd å få det 500 000 kroner billigere.",
        "<strong>Må de fortelle om absolutt alt?</strong> Nei. De trenger ikke fortelle deg at det blåser litt om høsten, eller at det er langt til butikken. De har opplysningsplikt om usynlige, tekniske eller juridiske ting som spesifikt påvirker akkurat dette byggeprosjektet eller denne tomten, og som en vanlig person ikke så lett oppdager.",
    ),
    "eksempler": [{"navn": "Lars", "tekst": "Lars kjøper en nøkkelferdig hytte av en utbygger. Etter overtakelsen finner Lars ut at hytta er koblet til en gammel brønn som tørker ut hver sommer. Utbyggeren visste om problemet med brønnen, fordi naboene hadde klaget på det under byggingen, men utbygger nevnte det ikke for Lars. Hadde Lars visst at hytta manglet vann på sommeren, ville han ikke betalt full pris. At utbygger tidde om dette, utgjør en mangel etter § 26. Lars kan kreve at utbyggeren borer en ny, dypere brønn på sin egen regning."}],
    "vanlige_feil": [
        "Å tro at man ikke kan klage på ting som ikke står i kontrakten — loven beskytter nettopp det som <em>manglet</em> av info før du signerte",
        "Kjøpere som glemmer å sjekke åpenbare ting selv, og etterpå klager på at utbygger ikke fortalte det (f.eks. at det ligger en bråkete skole to gater unna)",
    ],
    "hva_bor_du_html": _p(
        "Oppdager du noe alvorlig som utbyggeren må ha visst om, sikre bevis. Få gjerne innsyn i kommunens saksdokumenter (postlister) knyttet til prosjektet.",
        "Hvis det ligger et brev der fra utbygger datert to måneder før du kjøpte, hvor de diskuterer forurenset grunn på tomten din, har du et vanntett bevis. Send da et formelt krav til utbygger og vis til «brudd på opplysningsplikten i bustadoppføringslova § 26».",
    ),
    "dumme_sporsmal": [
        {"q": "Hva om snekkeren trodde han hadde fortalt det til meg?", "a": "Det er entreprenørens ansvar å bevise at informasjonen faktisk ble gitt på en tydelig måte, helst skriftlig. Vage, muntlige bisetninger på en bråkete byggeplass regnes ikke som god nok informasjon."},
        {"q": "De solgte meg et hus med fuktig kjeller, men de visste det faktisk ikke selv. Hva da?", "a": "Hvis de genuint ikke visste, og ikke hadde noen «profesjonell grunn» til å vite, gjelder ikke § 26. Da må du klage etter § 25 i stedet, altså at kjelleren teknisk sett er feilbygget (ikke i samsvar med kravene for godt håndverk)."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "25", "tittel": "Generell definisjon av mangel", "available": True},
        {"lov": LOV, "paragraf": "27", "tittel": "Når de gir uriktig info i stedet for å tie", "available": True},
        {"lov": LOV, "paragraf": "29", "tittel": "Hvilke krav du kan fremme", "available": True},
    ],
},
{
    "number": "27",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Løy utbygger i salgsprospektet?",
    "description": "Lovet reklamen at du skulle få «en solrik, lydisolert leilighet», mens realiteten er stikk motsatt? Urette opplysninger er en mangel.",
    "kort_svar": "Hvis utbyggeren skryter på seg kvaliteter i en annonse, på visning eller i prospektet, og huset ikke leverer dette, regnes det som en mangel (feil). Dette gjelder selv om selve kontrakten er vagere formulert enn markedsføringen.",
    "paragraftekst": "Mangel ligg òg føre dersom resultatet ikkje svarer til opplysningar om eigenskapar eller bruk som er gjevne i samband med avtaleinngåinga eller ved marknadsføring a) av entreprenøren eller på entreprenørens vegner, eller b) av nokon annan i eigenskap av eller på vegner av materialleverandør eller tidlegare salsledd. Første ledd gjeld likevel berre dersom ein kan gå ut i frå at opplysningane har verka inn på avtalen, og opplysningane ikkje er retta i tide på ein tydeleg måte.",
    "hva_betyr_html": _p(
        "Utbyggere elsker å bruke store, flotte ord i markedsføringen av nye byggeprosjekter. «Vedlikeholdsfritt», «lydtett», «eksklusivt design» og «solrik terrasse».",
        "§ 27 setter en stopper for falsk markedsføring. Loven likestiller løfter gitt i reklamen, på en plakat, eller muntlig av en megler, med det som står med liten skrift i selve avtalen. Hvis brosjyren viser et vindu i trappeoppgangen, og du får en mørk vegg, er det en byggefeil (mangel).",
        "Regelen rammer også leverandører lenger bak i kjeden. Hvis utbyggeren har brukt et spesielt takbelegg fordi produsenten av belegget lovet i sin reklame at «Dette tåler å stå under vann», og taket likevel lekker, er det entreprenøren du skal klage til. De står ansvarlig for lovnadene til sine leverandører.",
        "Det finnes et lite sikkerhetsnett for utbyggeren: Hvis de skrev feil i annonsen, men oppdaget det og sa tydelig ifra til deg før du skrev under («Hei, vi har feiltrykk i brosjyren, det blir ikke fliser på vaskerommet, bare betong»), gjelder ikke brosjyren.",
        "<strong>Er all reklame bindende?</strong> Nei. Står det «Byens koseligste bad», er det en smakssak og vanskelig å saksøke på. Står det «Lyddemping mot nabo av ypperste klasse», har de satt en forventning om at veggen demper mer lyd enn minimumskravet. Får du bare minimumsstandard, er annonsen løgn, og det utgjør en mangel.",
    ),
    "eksempler": [{"navn": "Anne", "tekst": "Anne kjøper leilighet i et nytt prosjekt. I salgsprospektet står det: «Alle leiligheter leveres med smart-styring av lys og varme fra telefonen». Da Anne tar over boligen, er det bare vanlige, manuelle dimmere på veggen. Entreprenøren sier at smart-styring ikke stod nevnt i den formelle byggebeskrivelsen bak i kontrakten. Etter § 27 vinner Anne. Opplysningen i prospektet var helt konkret og motiverte henne til å kjøpe. Entreprenøren må installere smarthus-løsningen gratis."}],
    "vanlige_feil": [
        "Å kaste salgsprospektet og reklamen i søpla etter at man har flyttet inn — det er ofte her de beste bevisene dine ligger",
        "Å tro at entreprenøren har ryggen fri bare fordi megleren «tok feil» på visning — entreprenøren har ansvar for det som blir sagt på deres vegne",
    ],
    "hva_bor_du_html": _p(
        "Når du kjøper en prosjektbolig fra tegning: Lagre PDF-en av salgsprospektet. Ta skjermbilde av finn-annonsen. Hvis selgeren gir deg spesifikke lovnader på e-post eller telefon før kontraktsmøtet, lagre dem i en mappe.",
        "Oppdager du feil, skriv til utbygger: «Jeg krever at utbedring gjøres, da nåværende løsning er en mangel etter § 27, i strid med markedsføringsmateriellet fra april i fjor.»",
    ),
    "dumme_sporsmal": [
        {"q": "Selgeren sa på visning at jeg fikk med dobbel garasje, men det ble enkel. Har jeg en sak?", "a": "Ja, muntlige lovnader før kjøp er absolutt bindende etter denne paragrafen. Utfordringen din er bevis. Hvis selgeren nekter for at han sa det, og ingen andre hørte det, taper du mest sannsynlig saken. Krev alltid alt skriftlig."},
        {"q": "Hva om utbygger rettet opp feilen i et vedlegg bak i kontrakten med bittesmå bokstaver?", "a": "Loven krever at feil i reklamen må rettes «på ein tydeleg måte» før avtalen signeres. Å gjemme rettelsen på side 45 i et teknisk vedlegg uten å nevne det høyt, er ofte ikke ansett som tydelig. Retten er på din side her."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "26", "tittel": "Når de skjuler negativ informasjon", "available": True},
        {"lov": LOV, "paragraf": "25", "tittel": "Generell definisjon av mangel", "available": True},
        {"lov": LOV, "paragraf": "33", "tittel": "Prisavslag hvis de ikke kan levere det annonsen lovet", "available": True},
    ],
},
{
    "number": "28",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Har du oppdaget skjulte feil lenge etter innflytting?",
    "description": "Et tak som lekker etter tre år, regnes som en byggefeil hvis årsaken lå der den dagen du fikk nøkkelen. Slik fungerer skjulte feil.",
    "kort_svar": "For at du skal kunne kreve utbedring av en feil, må årsaken til feilen ha vært der den dagen du tok over boligen (overtakelsestidspunktet). Selv om fukten eller råten først viser seg flere år senere, er utbyggeren ansvarlig.",
    "paragraftekst": "Om ytinga frå entreprenøren har mangel eller ikkje, skal avgjerast ut frå tilhøva på overtakingstidspunktet sjølv om mangelen viser seg først seinare. Entreprenøren svarer òg for feil som oppstår seinare, dersom årsaka til feilen er eit avtalebrot frå entreprenøren. Det same gjeld dersom entreprenøren ved garanti eller på annan måte har teke på seg ansvar for eigenskapar eller anna ved ytinga fram til eit seinare tidspunkt.",
    "hva_betyr_html": _p(
        "Hvem har skylden? Det er spørsmålet § 28 skal svare på. Den setter en hard knagg på selve overtakelsesdagen.",
        "Alt som bygges feil før du får nøkkelen, er utbyggers ansvar. Alt som skjer etter du har fått nøkkelen fordi du har brukt boligen feil, er ditt problem.",
        "Men byggfeil er lumske. Det er det som står i andre leddet som redder deg: «Skjulte mangler». La oss si snekkeren glemte å teipe vindsperren ordentlig bak veggpanelet. Veggen så perfekt ut på overtakelsesdagen. Tre år senere er veggen full av mugg fordi vann har sivet inn. Siden selve <em>årsaken</em> til feilen (den manglende teipen) skjedde før overtakelsen, er det et kontraktsbrudd fra entreprenøren. De må rive veggen og fjerne muggen.",
        "Andre ledd nevner også garanti. Hvis entreprenøren har gitt deg et papir hvor det står «Vi garanterer at varmepumpen virker i 10 år», er de bundet av det papiret uansett hva loven ellers sier.",
    ),
    "eksempler": [{"navn": "Håkon", "tekst": "Håkon flytter inn i sin nye tomannsbolig. To år senere begynner vinduene i stua å flasse stygt i malingen, og treverket sveller opp. Entreprenøren avviser saken og sier at «dette skjedde etter overtakelsen, du må ha vasket dem for hardt». Håkon får inn en takstmann som slår fast at vinduene ble lakkert uten riktig grunning på fabrikken. Dette beviser at <em>årsaken</em> lå der allerede før huset ble overlevert, selv om det tok to år før flassingen ble synlig. Etter § 28 er entreprenøren ansvarlig."}],
    "vanlige_feil": [
        "Entreprenører som avviser feil bare fordi det «har gått så lang tid siden du flyttet inn»",
        "Forbrukere som krever at utbygger bytter ut tette rør, når årsaken er at kunden selv har kastet matrester i vasken i to år — årsaken oppsto etter overtakelse og er din feil",
        "Å glemme å finne ut <em>hvorfor</em> skaden skjedde før man klager",
    ],
    "hva_bor_du_html": _p(
        "Når du oppdager en skade etter at du har bodd der en stund, prøv å finne årsaken. Vann og fukt er typiske eksempler på ting som bruker lang tid på å bryte ned materialer.",
        "Få inn en fagperson som kan skrive en rapport hvor de konkluderer med at «dette skyldes mangelfull utførelse på byggetidspunktet». Legg ved denne rapporten når du sender klagen til utbyggeren. Da knuser du argumentet deres om at feilen oppsto etter innflytting.",
    ),
    "dumme_sporsmal": [
        {"q": "Det har kommet et stygt hakk i parketten tre måneder etter innflytting. Kan jeg klage?", "a": "Trolig ikke. Hakk og riper er overflateskader du vil slite tungt med å bevise at var der ved overtakelsen. Utbygger vil påstå at du mistet noe i gulvet etter at du flyttet inn. Dette er grunnen til at overflateskader alltid må klages på senest ved den formelle overtakelsesbefaringen."},
        {"q": "Kjøkkenvifta kortsluttet etter tre og et halvt år. Snekkerne gjorde ikke noe galt med monteringen, motoren bare døde. Hvem sitt ansvar er det?", "a": "Entreprenøren. Selve vifta er en del av det de leverte, og tekniske apparater ment å vare lenge har fem års reklamasjonsrett. Feilen i den interne motoren er en produksjonsfeil som utbygger må ta ansvaret for å få byttet på garanti."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "14", "tittel": "Selve overtakelsesforretningen", "available": True},
        {"lov": LOV, "paragraf": "25", "tittel": "Generell definisjon av mangel", "available": True},
        {"lov": LOV, "paragraf": "30", "tittel": "Den absolutte fristen på 5 år", "available": True},
    ],
},
{
    "number": "29",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Ditt arsenal av rettigheter ved feil",
    "description": "Dette er innholdsfortegnelsen for hva du kan kreve når det er byggefeil (mangler) i huset ditt. Lær verktøykassen din.",
    "kort_svar": "Når du har oppdaget en feil (mangel) i den nye boligen din, gir loven deg en meny av sanksjoner: Du kan holde tilbake penger, kreve at de fikser det gratis, kreve avslag i prisen, heve (kansellere) kontrakten, eller kreve økonomisk erstatning.",
    "paragraftekst": "Ligg det føre mangel, kan forbrukaren a) halde attende vederlag etter § 31, b) krevje mangelen retta etter § 32, krevje prisavslag etter § 33 eller heve etter § 34, c) krevje skadebot etter § 35. For andre feil ved entreprenørens oppfylling gjeld føresegnene om manglar så langt dei høver.",
    "hva_betyr_html": _p(
        "§ 29 forklarer ingenting i detalj, men den er ekstremt viktig fordi den fungerer som et kart over maktmidlene dine. Har entreprenøren bygget noe feil, har du flere knapper å trykke på:",
        "<strong>Hold pengene (a):</strong> Første bud hvis du ikke har betalt sluttfakturaen ennå. Du nekter å betale tilsvarende det det vil koste å fikse feilen. Dette setter press på dem.",
        "<strong>Fiks det (b):</strong> Dette er den vanligste løsningen. Du krever «retting». Entreprenøren må da sende folk for å reparere feilen på sin egen regning.",
        "<strong>Gi meg rabatt (b):</strong> Hvis feilen ikke kan fikses, eller utbyggeren nekter, kan du kreve «prisavslag». Det betyr at du skal ha tilbake penger tilsvarende verditapet feilen utgjør.",
        "<strong>Jeg avlyser kjøpet (b):</strong> Heving. Hvis huset er så fullt av sopp, feil og mangler at det knapt er beboelig, kan du i ekstreme tilfeller si «ta huset, gi meg pengene tilbake».",
        "<strong>Betal meg erstatning (c):</strong> Hvis feilen har gjort at du har lidd et økonomisk tap i tillegg (for eksempel at fukten i kjelleren ødela de dyre møblene dine), kan du kreve dette beløpet som «skadebot».",
        "I praksis bruker du ofte flere av dem samtidig. Når du klager, skriver du: «Jeg krever mangelen rettet (§ 32), og jeg holder inntil videre tilbake 50 000 kroner fra sluttoppgjøret for å sikre at det blir gjort (§ 31).»",
    ),
    "eksempler": [{"navn": "Kari", "tekst": "Kari kjøper et nytt rekkehus. Det viser seg at de har lagt feil farge på taksteinen. Å bytte hele taket vil bli kjempedyrt, og utbyggeren nekter. Kari bruker lovens meny i § 29. Siden de nekter å bytte taksteinen (retting), går hun videre i menyen til «prisavslag» (§ 33). Huset er kanskje ikke verdt noe mindre på markedet på grunn av fargen, men Kari krevde rød stein og fikk svart. Hun fremmer da krav om prisavslag for at entreprenøren leverte et billigere utseende, og får tilbake 40 000 kroner."}],
    "vanlige_feil": [
        "Å kreve penger utbetalt umiddelbart for en liten feil — hovedregelen i norsk rett er at entreprenøren først og fremst har rett til å prøve å <em>reparere</em> feilen selv",
        "Å tro at du kan heve hele boligkjøpet på grunn av en riper i gulvet — heving gjelder kun ekstreme, vesentlige feil",
    ],
    "hva_bor_du_html": _p(
        "Gjør deg kjent med disse fem rettighetene. Ikke la utbyggeren diktere hva løsningen på feilen skal være.",
        "Mange forsøker seg med små, provisoriske reparasjoner som ser stygge ut, og sier «da er det fiksa». Hvis reparasjonen etterlater huset med redusert standard, har du krav på å kombinere «retting» med «prisavslag».",
    ),
    "dumme_sporsmal": [
        {"q": "Må jeg velge bare én av disse sanksjonene?", "a": "Nei. De kombineres ofte. Du kan holde tilbake penger mens de retter. Retter de, og det ble skader på tingene dine underveis, kan du også kreve erstatning for tapet. Det eneste du ikke kan kombinere fullt ut, er å kreve fullt prisavslag for en vegg <em>og</em> kreve at de reparerer samme veggen."},
        {"q": "Kan jeg fikse feilen selv og sende regningen til snekkeren?", "a": "Forsiktig her. Før du leier inn andre folk, må du gi den opprinnelige snekkeren en sjanse til å rette feilen sin (§ 32). Nekter de, ELLER de ikke gjør det raskt nok, kan du hente inn noen andre og kreve kostnaden dekket som prisavslag."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "31", "tittel": "Detaljene for å holde tilbake penger", "available": True},
        {"lov": LOV, "paragraf": "32", "tittel": "Reglene for selve utbedringen", "available": True},
        {"lov": LOV, "paragraf": "33", "tittel": "Krav om prisavslag", "available": True},
    ],
},
{
    "number": "30",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Den viktigste fristen for å klage",
    "description": "Ikke vent med å melde fra om byggefeil. Sender du e-posten for sent, mister du femårsgarantien din for alltid.",
    "kort_svar": "Du har en absolutt grense på fem år fra overtakelsen for å klage på feil (reklamere). I tillegg har du en relativ, streng frist: Du må melde ifra «innen rimelig tid» (ca. to måneder) etter at du faktisk oppdaget, eller burde oppdaget, feilen. Vent aldri.",
    "paragraftekst": "Forbrukaren mistar retten til å gjere ein mangel gjeldande dersom det ikkje er gjeve melding til entreprenøren om at mangelen blir gjord gjeldande innan rimeleg tid etter at forbrukaren oppdaga eller burde ha oppdaga mangelen. Ein mangel kan ikkje gjerast gjeldande seinare enn fem år etter overtakinga. Entreprenøren kan likevel ha teke på seg å svare for manglar i lengre tid. Vil forbrukaren gjere gjeldande manglar som var eller burde ha vore oppdaga ved overtakinga, må dette gjerast så snart råd er dersom overtakinga skjer ved overtakingsforretning. Når det blir halde seinare synfaring etter § 16, må forbrukaren gjere gjeldande manglar som var eller burde ha vore oppdaga, så snart råd er. Entreprenøren kan ikkje gjere gjeldande at det er reklamert for seint etter denne paragrafen, om mangelen kjem av at entreprenøren eller nokon entreprenøren svarer for, har fare fram grovt aktlaust eller i strid med heider og god tru elles. Retten til å gjere ein mangel gjeldande kan òg bli mista etter reglane om forelding i foreldingslova.",
    "hva_betyr_html": _p(
        "§ 30 er lovens dødsfelle. Bommer du på reglene her, mister du alle rettighetene dine, og entreprenøren slipper å reparere uansett hvor håpløst de har bygget huset.",
        "<strong>1. Den absolutte fristen (5 år):</strong> Fra den dagen du signerer papirene på at du overtar huset, begynner en klokke å tikke ned. Etter nøyaktig fem år stenges døren (med mindre de skriftlig ga deg f.eks. 10 års garanti). Oppdager du at bjelkelaget i gulvet råtner etter 5 år og én måned, er det ditt problem.",
        "<strong>2. Den relative fristen («innen rimelig tid»):</strong> Denne er enda farligere. Oppdager du en feil på badet i år 3, kan du ikke vente i et halvt år med å sende klagen. Du må si ifra innen to, maks tre måneder. Domstolene i Norge aksepterer vanligvis 2 måneder som «rimelig tid». Sitter du og venter, mister du kravet, selv om det ikke har gått fem år enda.",
        "Paragrafen setter også ekstra press på deg på to dager i byggeprosessen: under overtakelsen, og under ettårsbefaringen. Da må du klage «så snart som råd er» (ofte tolket til noen dager) på ting du ser der.",
        "<strong>Unntaket:</strong> Har entreprenøren direkte svindlet deg, løyet, eller vist en horribel, grov uaktsomhet for å bygge billigst mulig, beskyttes de ikke av disse fristene.",
    ),
    "eksempler": [{"navn": "Per", "tekst": "Per oppdager at det lekker vann ned fra taket på vaskerommet. Dette skjer tre år etter innflytting. Han er midt i en travel periode på jobb og legger håndklær på gulvet i fire måneder før han til slutt sender en e-post til utbyggeren for å klage. Entreprenøren svarer: «Du reklamerte for sent etter § 30, vi avviser kravet.» Per taper saken i retten. Han varslet ikke «innen rimelig tid» etter at han faktisk oppdaget at taket lakk."}],
    "vanlige_feil": [
        "Å sende vage meldinger til snekkeren («Taket er litt rart, vi må snakkes til uka») — en gyldig klage må tydelig angi at du gjør en feil gjeldende",
        "Vente til «ting har roet seg på jobb» før du klager",
        "Sende klager på SMS som man senere mister telefonen til, slik at man mangler bevis på datoen man sendte klagen",
    ],
    "hva_bor_du_html": _p(
        "Når du ser en feil, send e-post med en gang. Du trenger ikke ha takstmannsrapporten eller alle svarene klare for å holde fristen. Send en såkalt «nøytral reklamasjon»:",
        "<em>«Hei. Jeg oppdaget i dag at flisene på badet har begynt å løsne fra veggen. Jeg gjør med dette gjeldende at dette utgjør en mangel, og vil komme tilbake med mer teknisk informasjon når jeg har undersøkt saken nærmere.»</em>",
        "Da har du fryst klokka, holdt lovens frist, og du kan bruke all den tiden du trenger på å hente inn en ekspert for å finne ut hvor mye det vil koste å utbedre det.",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg nye fem år på feilen etter at de har fikset den?", "a": "Hovedregelen etter nyere dommer er at hvis de skifter ut en stor, selvgående del (f.eks. hele varmepumpen), kan det løpe en ny klagefrist på den delen. Hvis de bare sprøyter inn litt fugemasse, løper det ikke fem nye år. Men etter foreldelsesloven forlenges kravet vanligvis i ett ekstra år for å se om reparasjonen holdt."},
        {"q": "Kan entreprenøren kreve at jeg beviser <em>når</em> jeg oppdaget det?", "a": "Bevisbyrden snus ofte her, men hvis lekkasjen åpenbart har pågått i lange tider med store, råtne skjolder på hele veggen din, vil retten legge til grunn at du «burde ha oppdaget» det for lengst."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "14", "tittel": "Fristen starter på overtakelsesdatoen", "available": True},
        {"lov": LOV, "paragraf": "15", "tittel": "Overtakelsesforretningen", "available": True},
        {"lov": LOV, "paragraf": "16", "tittel": "Ettårsbefaringen", "available": True},
    ],
},
{
    "number": "31",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Slik presser du utbygger til å fikse feilen",
    "description": "Du har lovfestet rett til å holde tilbake betaling hvis utbyggeren har levert en bolig med byggefeil. Penger er makt.",
    "kort_svar": "Finner du en byggefeil før du har betalt den siste regningen for huset, kan du nekte å betale det beløpet det koster å fikse feilen. Dette sikrer at utbyggeren faktisk kommer tilbake for å utbedre, siden de vil ha restpengene sine.",
    "paragraftekst": "Har forbrukaren krav som følgje av mangelen, kan forbrukaren halde tilbake så mykje av vederlaget som er nødvendig for å sikre at kravet vert dekt.",
    "hva_betyr_html": _p(
        "Loven gir deg et utrolig sterkt kort på hånden, og det heter tilbakeholdsrett. Mens § 24 gjelder tilbakehold ved forsinkelser, gjelder § 31 ved fysiske feil (mangler) på bygget.",
        "Hvis du oppdager på overtakelsesdagen at malingen på utsiden mangler to strøk, og kjøkkenviften ikke er koblet til, skriver du det i protokollen. Hvis utbyggeren deretter sender en sluttfaktura på hele kjøpesummen, sier loven at du har full rett til å fryse den delen av summen som «sikrer kravet».",
        "Det betyr at du skal beregne hva det vil koste å leie inn noen andre til å male huset og fikse viften. Kanskje det vil koste 60 000 kroner totalt i et verste-falls-scenario. Da betaler du den store fakturaen, men minus 60 000 kroner, og gir skriftlig beskjed om at disse holdes tilbake etter § 31 inntil de har utbedret mangelen.",
        "Dette fungerer som et fantastisk ris bak speilet. Hvis du betaler alt med én gang og stoler på at de «fikser det neste uke», havner saken din fort nederst i en skuff. Snekkeren som alt har fått betalt, har ikke travelt. Ligger det derimot 60 000 kroner og venter hos deg, stiller de opp på mandag morgen.",
        "<strong>Begrensning:</strong> Paragrafen krever at det må være proporsjonalt. Holder du tilbake 500 000 kroner for en ødelagt dørvrider til 500 kr, bryter du betalingsplikten din, og da er det <em>du</em> som er avtale-bryter.",
    ),
    "eksempler": [{"navn": "Sara", "tekst": "Sara sjekker den nye boligen sin med en uavhengig takstmann før overtakelse. Takstmannen finner skjeve gulvfliser på badet. En ny flislegger vil ta 80 000 kroner for å rette opp i dette fordi membranen kanskje må skiftes ut. Entreprenøren nekter å fikse det og mener det «er innafor toleransegrensene». Sara får sluttoppgjøret på 400 000 kr. Hun betaler 320 000 kr, og sender en e-post hvor hun viser til rapporten fra takstmannen, og at de resterende 80 000 kr holdes tilbake etter § 31 for utbedring av badet."}],
    "vanlige_feil": [
        "Betale 100 % av summen ved overtakelse av «godvilje», og tro at håndverkerne dukker opp etterpå",
        "Holde igjen penger, men ikke gi skriftlig beskjed om <em>hvorfor</em> man ikke betalte hele regningen",
        "Å tro at utbygger kan sette en egen klausul i kontrakten som fjerner denne retten (loven trumfer alle kontrakter)",
    ],
    "hva_bor_du_html": _p(
        "Vær systematisk. Hvis noe er feil ved innflytting, innhent prisoverslag fra to andre lokale håndverkere på hva det koster å utbedre akkurat det punktet. Trekk det høyeste av de to estimatene fra sluttoppgjøret.",
        "Husk at du ikke bare holder tilbake summen — du sender en skriftlig reklamasjon der du ber den opprinnelige entreprenøren komme for å rette feilen. Fikser de feilen gratis for deg uken etter, betaler du ut restbeløpet.",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg lov å holde igjen pengene hvis feilen var at tomten var skitten?", "a": "Ja, mangler er alt som ikke er levert i henhold til kontrakten. Om opprydningen er en del av avtalen, og det koster 20 000 å få et ryddefirma til å kjøre det vekk, kan du holde tilbake 20 000 kr inntil entreprenøren rydder opp."},
        {"q": "Hva om jeg ikke har flere regninger igjen å betale, og oppdager feilen om tre år?", "a": "Da hjelper dessverre ikke denne paragrafen deg. Tilbakeholdsretten krever at du faktisk har penger du fortsatt skylder utbyggeren. Hvis regningen er betalt for to år siden, har du ingenting å holde tilbake. Da må du kreve at de kommer og retter (§ 32) eller betaler deg penger for mangelen (§ 33), og i verste fall tvinge det gjennom bankgarantien etter § 12."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "24", "tittel": "Tilbakehold ved forsinkelse", "available": True},
        {"lov": LOV, "paragraf": "32", "tittel": "Entreprenørens plikt og rett til å rette opp", "available": True},
        {"lov": LOV, "paragraf": "29", "tittel": "Oversikt over alle dine krav", "available": True},
    ],
},
{
    "number": "32",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Reparasjon (retting) av byggefeil",
    "description": "Du har krav på at feil blir fikset gratis. Men visste du at snekkeren har en lovfestet rett til å gjøre jobben selv for å spare penger?",
    "kort_svar": "Oppdages en feil i bygget, kan du kreve at entreprenøren kommer og fikser den på sin regning innen rimelig tid. På samme måte har entreprenøren rett til å kreve å få fikse det selv, i stedet for at du leier inn en annen, dyrere håndverker og sender dem regningen.",
    "paragraftekst": "Forbrukaren kan krevje at entreprenøren rettar ein mangel om ikkje rettinga vil føre til kostnader eller ulemper som ikkje står i rimeleg høve til det forbrukaren oppnår. Skade som mangelen har ført til på arbeid eller eigedom som er omfatta av avtalen mellom forbrukaren og entreprenøren, skal òg rettast dersom skaden er ei nærliggjande og pårekneleg følgje av mangelen. Vil forbrukaren gjere gjeldande ein mangel, har entreprenøren krav på å få rette mangelen dersom rettinga kan skje utan vesentleg ulempe for forbrukaren, og forbrukaren heller ikkje elles har særleg grunn til å setje seg imot retting. Retting skal skje innan rimeleg tid etter at forbrukaren har gjort mangelen gjeldande og har gjort det mogleg for entreprenøren å rette. Retting skjer for entreprenørens rekning. Entreprenøren skal bere tilkomstutgifter, utgifter til konstatering av mangelen og andre utgifter som er ei direkte og nødvendig følgje av rettinga.",
    "hva_betyr_html": _p(
        "Retting er den absolutte hovedregelen i norsk kontraktsrett. Har du bygget feil, skal du få lov til — og du har plikt til — å fikse det.",
        "<strong>Første ledd gir <em>deg</em> makten:</strong> Du kan beordre utbyggeren til å reparere feilen, helt gratis for deg. De må da kjøre ut, demontere det ødelagte, montere nytt, og dekke alle regninger knyttet til feilsøking. Du skal ikke betale et rødt øre i transportgebyr eller materialer som knakk. Unntaket er bare hvis utbedringen er totalt vanvittig dyr i forhold til nytten.",
        "<strong>Andre ledd gir <em>entreprenøren</em> makten:</strong> Hvis rørleggeren har montert blandebatteriet feil, har rørleggeren rett til å komme for å prøve å skru det til selv. Du kan ikke bare hyle «jeg stoler ikke på dere lenger», ringe konkurrenten deres, og sende dem fakturaen på 25 000 kroner. Du MÅ la dem prøve å rette sine egne feil. Gjør du ikke det, må du betale konkurrenten av din egen lomme.",
        "<strong>Når skal det fikses?</strong> Innen «rimelig tid». Det betyr at de ikke kan vente i et år. Unntaket er kosmetiske småting; her tillater loven at de venter til ettårsbefaringen hvis det ikke forstyrrer hverdagen din i mellomtiden.",
    ),
    "eksempler": [{"navn": "Marius", "tekst": "Marius merker at vannet på badet ikke renner ned i sluket, men samler seg i hjørnet. Han sender en klage (§ 30). Entreprenøren mottar klagen og sier de vil komme neste uke for å legge flisene på badet på nytt (entreprenørens rett til retting, § 32). Marius er sur på firmaet og vil egentlig leie inn naboen sin som er flislegger, for så å kreve prisavslag for regningen. Heldigvis advarer naboen ham om loven. Marius må pent låse opp døren, la den opprinnelige entreprenøren rive gulvet, betale for nye fliser, og legge dem i riktig fall mot sluket, uten at det koster Marius noe som helst."}],
    "vanlige_feil": [
        "Forbrukere som bytter ut ødelagte vinduer med andre folk, uten å reklamere og gi utbyggeren tilbud om å fikse det først — dette ødelegger saken deres totalt",
        "Utbyggere som krever at kunden betaler reisevei, parkeringsgebyr eller bompenger for at de må «komme tilbake» (alt dette er entreprenørens regning)",
        "Entreprenører som sier «vi venter til ettårsbefaringen» med feil som gjør at rom ikke kan brukes",
    ],
    "hva_bor_du_html": _p(
        "Når du klager (reklamerer), bruk standardsetningen: «Jeg krever mangelen utbedret etter bustadoppføringslova § 32, og ber dere ta kontakt innen 14 dager for å avtale tidspunkt for gratis retting.»",
        "Hvis de kommer for å rette, rydd unna tingene dine. Loven sier du har plikt til å gjøre det «mogleg» for dem. Lås opp, flytt bilen fra oppkjørselen og la dem gjøre jobben sin.",
    ),
    "dumme_sporsmal": [
        {"q": "Hvor mange ganger kan de «prøve å rette» den samme feilen?", "a": "Loven setter ikke et absolutt tall, men rettspraksis tilsier at to forsøk er det maksimale for samme feil. Klarer de ikke å tette taket på andre forsøk, kan du si at det «medfører en vesentlig ulempe» for deg, nekte dem flere forsøk, og heller gå over til krav om prisavslag (§ 33)."},
        {"q": "Målene på hytta ble to kvadratmeter for små. Kan jeg kreve retting?", "a": "Her kommer kravet om «kostnader i rimelig forhold til det forbrukeren oppnår» inn. Å rive hytta for å gjøre den to kvadratmeter større koster millioner og er absurd uforholdsmessig. I slike tilfeller er «retting» umulig etter loven. Da er kravet ditt automatisk rettet mot økonomisk prisavslag i stedet for fysisk fiks."},
        {"q": "De ødela den dyre tapeten min da de fikset feilen inne i veggen. Skal de fikse den også?", "a": "Ja. Første ledd slår fast at skade mangelen har ført til på annen eiendom omfattet av avtalen, også skal rettes. Røret som var feilmontert koster dem kanskje ingenting å skru til, men å rive den nye tapeten, sette opp ny gips og tapetsere rommet på nytt, inngår i kostnaden for rettingen som de fullt ut må betale for."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "33", "tittel": "Når retting ikke er mulig — prisavslag", "available": True},
        {"lov": LOV, "paragraf": "30", "tittel": "Fristene du må overholde", "available": True},
        {"lov": LOV, "paragraf": "16", "tittel": "Ettårsbefaringen", "available": True},
    ],
},
]
