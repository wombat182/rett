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
{
    "number": "33",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Kreve penger i stedet for reparasjon (prisavslag)",
    "description": "Nekter entreprenøren å reparere byggefeilen, eller er det umulig å fikse den? Da kan du kreve å få pengene tilbakebetalt i form av prisavslag.",
    "kort_svar": "Prisavslag er plan B. Hvis entreprenøren ikke retter byggefeilen innen rimelig tid, eller hvis feilen fysisk sett ikke kan rettes, kan du kreve penger tilbake for verditapet feilen utgjør.",
    "paragraftekst": "Dersom ein mangel ikkje blir retta i samsvar med § 32, kan forbrukaren krevje prisavslag. Dette gjeld likevel ikkje dersom forbrukaren avslår retting som entreprenøren har rett til å utføre etter § 32 andre ledd. Prisavslaget skal vere lik kostnadene for forbrukaren med å få mangelen retta, bortsett frå slike kostnader som er nemnde i § 32 fjerde ledd tredje punktum. Blir kostnadene urimeleg høge i høve til det mangelen har å seie for forbrukaren, skal prisavslaget vere lik den verdireduksjonen som mangelen medfører. Prisavslaget skal likevel minst tilsvare det entreprenøren har spart ved ikkje å levere mangelfri yting.",
    "hva_betyr_html": _p(
        "Paragrafen setter prisavslag i en klar rekkefølge: Først skal utbyggeren få lov til å prøve å rette feilen fysisk (§ 32). Prisavslag er en erstatningsløsning som aktiveres bare når rettingen feiler, de nekter å komme, eller hvis retting er bygningsteknisk meningsløst (f.eks. at takhøyden er fem centimeter for lav).",
        "Neste spørsmål er: Hvor mye penger utgjør et prisavslag? Loven har en tre-trinns rakett for beregningen:",
        "Trinn 1 (Hovedregelen): Prisavslaget skal tilsvare det det koster deg å leie inn noen andre til å fikse feilen. Koster det 40 000 kroner å få en annen rørlegger til å bytte den ødelagte vasken den første nektet å ta ansvar for? Da er prisavslaget ditt 40 000 kroner.",
        "Trinn 2 (Når utbedring er for dyrt): Hvis det koster 2 millioner å rive taket for å endre fargen på en takbjelke, er det en urimelig høy kostnad i forhold til nytten. Da beregnes prisavslaget ut fra \"verdireduksjon\". Har feil farge gjort huset mindre verdt ved videresalg? Kanskje verdien sank med 50 000 kr. Da er det prisavslaget.",
        "Trinn 3 (Straffebestemmelsen): Prisavslaget kan aldri være lavere enn det entreprenøren sparte på å jukse. Hvis de brukte en billig isolasjon i veggen som de tjente 20 000 kroner på, og dette ikke påvirker markedsverdien på huset (verdireduksjon = 0), slår trinn 3 inn. De skal aldri få tjene penger på å levere feil. Prisavslaget blir da på de 20 000 kronene de prøvde å spare.",
    ),
    "eksempler": [
        {"navn": "Eva", "tekst": "Eva bygger hytte. Kontrakten spesifiserte at terrassen skulle være 40 kvadratmeter. Da hytta var ferdig, viste det seg at utbyggeren leste tegningen feil og bare bygget 35 kvadratmeter. Å rive terrassen og bygge ny (retting) ville vært kjempedyrt, og utbygger nekter. Eva krever da prisavslag etter § 33. Hun innhenter pris på hva det vil koste en annen lokal snekker å bygge et tilbygg til terrassen på 5 kvadratmeter. Den prisen er 30 000 kr. Eva krever dette beløpet i prisavslag og holder det tilbake i sluttoppgjøret."},
    ],
    "vanlige_feil": [
        "Å kreve prisavslag umiddelbart uten å ha sendt en reklamasjon der man gir utbyggeren frist til å rette feilen først. (Unntaket er der retting er fysisk umulig).",
        "Å gjette på en sum (for eksempel: \"Jeg synes jeg bør få 100 000 kroner i rabatt for dette\"). Domstolen hater gjetting. Prisavslag skal alltid dokumenteres teknisk.",
    ],
    "hva_bor_du_html": _p(
        "For å få penger (prisavslag) ut av en motvillig utbygger, må du levere bevis. Ring to uavhengige håndverkerfirmaer og be dem gi et skriftlig tilbud på å utbedre feilen. Da har du et konkret tall. Send dette til utbygger: \"Siden dere har avvist retting, kreves herved prisavslag etter bustadoppføringslova § 33. I henhold til vedlagte tilbud utgjør dette 45 000 kr, som vil bli trukket fra restbetalingen.\"",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg prisavslag for de timene jeg selv brukte på å rydde opp vannlekkasjen?", "a": "Nei, prisavslag dekker verditapet på selve huset eller regningen fra andre håndverkere. Din egen innsats eller ødelagte møbler regnes som et økonomisk tap, og skal kreves gjennom erstatning (skadebot) i § 35."},
        {"q": "Huset står en halvmeter feil på tomta, men det koster ingenting for husets markedsverdi og det sparer ikke utbygger noe for. Får jeg ikke noe da?", "a": "Slike saker (ofte kalt \"estetiske mangler\") er veldig vanskelige, og retten dømmer ofte at prisavslaget blir kroner 0,- fordi vilkårene i beregningen ikke slår ut. Du må i så fall kunne bevise at huset vil oppfattes som mindre attraktivt i markedet (verdireduksjon)."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "32", "tittel": "§ 32", "available": True},
        {"lov": LOV, "paragraf": "29", "tittel": "§ 29", "available": True},
        {"lov": LOV, "paragraf": "49", "tittel": "§ 49", "available": True},
    ],
},
{
    "number": "34",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Siste utvei: Du kansellerer huset (Heving)",
    "description": "Har du tatt over et hus som viser seg å være bygget så feil at det er helsefarlig? Da kan du i ekstreme tilfeller heve kontrakten.",
    "kort_svar": "Hvis feilen i boligen er massiv og innebærer et \"vesentlig avtalebrudd\", kan du heve avtalen. Dette betyr at du gir huset tilbake til entreprenøren og får alle pengene dine tilbakebetalt. Det skal svært mye til for at domstolene tillater heving fremfor å kreve feilen utbedret eller dekket med penger.",
    "paragraftekst": "Forbrukaren kan heve avtalen dersom mangelen inneber eit vesentleg avtalebrot. Forbrukaren kan òg heve avtalen før overtakingstidspunktet dersom det er klårt at ytinga kjem til å få ein slik mangel som nemnd i første punktum.",
    "hva_betyr_html": _p(
        "Paragraf 34 er tvillingen til paragraf 20. Mens § 20 gjelder for heving på grunn av forsinkelse, gjelder § 34 heving på grunn av feil og mangler i selve bygget. Dette er den absolutte nødløsningen.",
        "Du kan ikke heve en boligkontrakt fordi parketten knirker, selv om du hater knirk. For å heve, må domstolen konkludere med at bygget har et \"vesentlig avtalebrudd\". Da ser de på totalbildet: Er huset helsefarlig? Må store deler av det rives for å kunne rettes? Nekter utbygger å ordne opp?",
        "Hvis en familie flytter inn, og to uker senere oppdager de at det er brukt giftige plater, ingen fuktsikring og taket er iferd med å klappe sammen, kan de heve. Konsekvensen står i § 21: Penger bytter hender slik at du settes i samme økonomiske situasjon som før du tegnet kontrakten. Du gir huset tilbake og får millionene dine utbetalt fra entreprenøren (eller bankgarantien).",
    ),
    "eksempler": [
        {"navn": "Kari", "tekst": "Kari har kjøpt og flyttet inn i et ferdighus. Etter to måneder begynner veggene å bule innover. Takstmannen oppdager at utbyggeren har murt inn våt, råtten plank i hele reisverket, og huset er fullt av giftig muggsopp. Det vil koste mer å rive huset og bygge det opp igjen enn det kostet å kjøpe det i utgangspunktet. I tillegg nekter utbygger skyld og skylder på \"condens fra Karis tørketrommel\". Dette er et grovt og vesentlig avtalebrudd. Kari engasjerer advokat, hever kjøpet, og retten dømmer utbygger (og garantibanken deres) til å betale tilbake alt Kari har innbetalt pluss erstatning for opphold på hotell."},
    ],
    "vanlige_feil": [
        "Å prøve å heve avtalen som et \"forhandlingskort\" i en konflikt om små mangler. Gjør du dette uberettiget, blir du saksøkt for kontraktsbrudd.",
        "Å heve avtalen muntlig over telefon. Heving må fremmes formelt, skriftlig, og helst av en advokat.",
        "Flytte ut av huset uten en skriftlig plan for hevingsprosessen.",
    ],
    "hva_bor_du_html": _p(
        "Bruk aldri ordet \"heving\" til utbyggeren din i en e-post uten at du har snakket med en ekspert i bygningsrett eller takstbransjen først. Terskelen er skyhøy i norsk rett. Det normale er prisavslag og erstatning (§ 33 og § 35), hvor du i stedet bruker pengene til å betale et proft firma for å renovere huset mens du bor der. Heving velges kun når huset er tilnærmet usalgbart.",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg beholde huset hvis jeg hever?", "a": "Nei, poenget med heving for bolig+tomt er at prestasjonene går tilbake. De får boligen og risikoen, du får tilbake pengene (pluss eventuelt forsinkelsesrenter og erstatning for ulempen)."},
        {"q": "Hva om jeg bygget på egen tomt og hever fordi huset ble bygget feil?", "a": "Da gjelder § 21 andre ledd. Entreprenøren forsvinner fra tomten din, du betaler dem kun for verdien av det de faktisk har bygget riktig oppå din jord, og så overtar et nytt firma."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "33", "tittel": "§ 33", "available": True},
        {"lov": LOV, "paragraf": "20", "tittel": "§ 20", "available": True},
        {"lov": LOV, "paragraf": "21", "tittel": "§ 21", "available": True},
    ],
},
{
    "number": "35",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Penger for økonomisk tap (Erstatning) ved byggefeil",
    "description": "Lakk røret slik at TV-en din ble ødelagt? Eller måtte du bo på hotell? Du har krav på erstatning for økonomiske tap som feilen forårsaket.",
    "kort_svar": "I tillegg til at utbyggeren må fikse selve huset, kan du kreve at de erstatter andre økonomiske tap som feilen deres var skyld i. Du har rett på erstatning selv om utbyggeren ikke gjorde feilen med vilje.",
    "paragraftekst": "Økonomisk tap som kjem av ein mangel, og som ikkje er dekt ved prisavslag etter § 33, kan forbrukaren krevje bøtt utan at det ligg føre skyld på entreprenørens side. Dette gjeld likevel ikkje så langt entreprenøren godtgjer at mangelen oppstod på grunn av ei hindring utanfor entreprenørens kontroll, og det ikkje er rimeleg å vente at entreprenøren kunne ha rekna med hindringa på avtaletida, eller at entreprenøren kunne ha overvunne eller unngått følgjene av hindringa.",
    "hva_betyr_html": _p(
        "Mens prisavslag og retting gjelder feil på selve huset, handler paragraf 35 om \"følgeskader\" (også kalt skadebot eller erstatning).",
        "Kravet i loven er et såkalt objektivt ansvar (kontrollansvar). Det betyr at du ikke trenger å bevise at snekkeren eller rørleggeren var fyllesyk, uaktsom eller elendig i jobben sin. Så lenge huset har en byggefeil (for eksempel et rør som hopper av under vasken), og dette påfører deg et ekstra økonomisk tap (kjøkkenskapet ditt og en dyr blender blir ødelagt), er utbyggeren ansvarlig for tapet. De er ansvarlige uansett om det er deres egne ansatte, eller rørleggeren de leide inn, som forårsaket det.",
        "Den eneste måten entreprenøren slipper å betale deg på, er hvis de kan bevise force majeure. Det betyr at feilen skyldtes noe helt ekstremt utenfor deres kontroll (som et jordskjelv). I Norge skjer nesten alt under utbyggers \"kontrollsfære\", fra kvaliteten på limet til arbeidet som utføres, så regelen er veldig sterk for deg.",
    ),
    "eksempler": [
        {"navn": "Jonas", "tekst": "Et år etter at Jonas flyttet inn, svikter membranen i dusjen fordi mureren til utbyggeren la den feil. Vannet renner ned i etasjen under, og taket raser ned over stua. Den dyre stressless-stolen til Jonas blir fullstendig ødelagt av vann, og Jonas og familien må leie en Airbnb i to uker mens gulvet rives og tørkes. Etter § 32 må entreprenøren rive badet og bygge det på nytt (retting av feilen). Etter § 35 kan Jonas sende krav til entreprenøren for de andre tapene: Regningen for Airbnb-oppholdet, og en sum som tilsvarer verdien av den ødelagte stolen."},
    ],
    "vanlige_feil": [
        "Å blande det med hjemmeforsikringen. Det er som regel billigere å bruke egen innboforsikring på ødelagt løsøre fordi du får det raskt, men du kan kreve at entreprenøren betaler egenandelen og tapet av bonus.",
        "Å kreve erstatning for \"frustrasjon\" og \"tort og svie\". Paragrafen krever et konkret, dokumenterbart økonomisk tap. Du må ha kvitteringer.",
        "Å akseptere at hovedentreprenøren avviser deg og ber deg ringe underleverandøren (elektrikeren) direkte. Loven slår fast at hovedentreprenøren har ansvaret overfor deg.",
    ],
    "hva_bor_du_html": _p(
        "Når en byggefeil oppstår, lag en egen mappe som heter \"Erstatning\". Legg inn alle kvitteringer du påføres fordi feilen eksisterer: parkeringskvitteringer når du måtte dra på visning for en Airbnb, lunsjkvitteringer hvis kjøkkenet måtte stenges ned i en uke, og kvitteringer for tapte leieinntekter hvis du hadde en leieboer i kjelleren. Dokumenter alt med bilder og send det som ett samlet erstatningskrav sammen med mangelsklagen.",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg dekket at jeg måtte ta en fridag fra jobben for å være hjemme da de reparerte feilen?", "a": "Ja. Tapt arbeidsfortjeneste fordi du måtte tilrettelegge for håndverkere som skal reparere en klage-sak, regnes som et økonomisk tap etter § 35, hvis det var absolutt nødvendig at du var hjemme."},
        {"q": "Kan de tvinge meg til å bruke deres forsikringsselskap for den ødelagte sofaen?", "a": "Du har et krav mot entreprenøren. Om entreprenøren betaler deg kontant, eller sender kravet videre til sitt eget forsikringsselskap (ansvarsforsikring), er deres interne sak."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "36", "tittel": "§ 36", "available": True},
        {"lov": LOV, "paragraf": "33", "tittel": "§ 33", "available": True},
        {"lov": LOV, "paragraf": "6", "tittel": "§ 6", "available": True},
    ],
},
{
    "number": "36",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Hvilke økonomiske tap får du erstattet?",
    "description": "Du har rett på erstatning for byggefeil. Men loven krever at du gjør det du kan for å holde regningen lavest mulig for utbyggeren.",
    "kort_svar": "Får du erstatning for en byggefeil, skal beløpet dekke det faktiske økonomiske tapet ditt (f.eks. utgifter, prisforskjeller og tapt lønn). Men du får ikke ubegrenset med penger. Loven krever at tapet måtte være forventet for entreprenøren, og at du aktivt prøver å begrense utgiftene dine.",
    "paragraftekst": "Skadebota skal svare til det økonomiske tapet forbrukaren har hatt (utlegg, prisskilnad, tapt arbeidsforteneste, tingskade m.m.). Dette gjeld likevel berre tap som ein rimeleg kunne ha rekna med som ei mogleg følgje av mangelen. Forsømer forbrukaren å avgrense tapet gjennom rimelege tiltak, må forbrukaren sjølv bere den tilsvarande delen av tapet.",
    "hva_betyr_html": _p(
        "Paragrafen forteller deg akkurat hva erstatningen din (skadeboten) skal inneholde. Du har krav på å bli stilt som om feilen aldri skjedde.",
        "Loven lister opp typiske tap: utlegg, prisforskjeller, tapt arbeidsfortjeneste og tingskader.",
        "Men det er to store begrensninger. For det første må tapet være \"påregnelig\". Hvis strømmen går på grunn av en feilmontert stikkontakt, er det forventet at maten i fryseren blir ødelagt. Men hvis du hadde lagret en lottokupong på PC-en som du ikke fikk levert fordi strømmen gikk, kunne ikke snekkeren forvente det. Da får du ikke erstatning for tapte lottomillioner.",
        "For det andre har du \"tapsbegrensningsplikt\". Det betyr at du ikke kan lene deg tilbake og la takstameteret løpe. Du må handle fornuftig for å holde prisen nede. Går et rør lekk, må du skru av hovedkranen. Lar du vannet renne i en uke fordi \"det er rørleggerens skyld\", får du ikke erstatning for den skaden du kunne forhindret.",
    ),
    "eksempler": [
        {"navn": "Anne", "tekst": "En vannlekkasje på det nye badet ødelegger gulvet i etasjen under, som Anne pleier å leie ut. Hun må kaste ut leieboeren i fire måneder mens entreprenøren tørker og bygger opp badet. Anne krever erstatning. Hun legger frem dokumentasjon for tapt leieinntekt på 12 000 kr i måneden, pluss egenandelen hun betalte for å få byttet ut en ødelagt sofa. Entreprenøren må erstatte alt sammen, siden tapte leieinntekter og ødelagte møbler er tap en utbygger med rimelighet kan forvente ved en lekkasje."},
    ],
    "vanlige_feil": [
        "Å kreve erstatning for sinne, stress og tårer. Det finnes ikke noe som heter \"tort og svie\" for boligfeil.",
        "Å ikke ta umiddelbare grep for å stoppe en skade, slik at man mister retten på penger.",
        "Leie en luksusbil fordi den vanlige bilen stod innesperret i den ødelagte garasjen.",
    ],
    "hva_bor_du_html": _p(
        "Dokumenter alt. Før en logg. Må du ta deg fri fra jobben? Be sjefen din om en skriftlig bekreftelse på at du har tapt for eksempel 2 500 kr i lønn den dagen. Må du leie hotell? Sjekk prisene på to ulike hoteller, velg det rimeligste, og lagre kvitteringen. Når du sender kravet til utbygger, legger du frem en ryddig Excel-liste med bilag på alt. Da er det veldig vanskelig for dem å argumentere mot kravet.",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg betalt for tiden jeg brukte på å klage og skrive e-poster?", "a": "Normalt sett, nei. Din egen tid (fritid) til å rydde opp i rotet eller klage, regnes ikke som et økonomisk tap. Unntaket er hvis du faktisk har tapt inntekt fordi du måtte ta fri fra jobben for å gjøre det."},
        {"q": "Hva om de sier det blir altfor dyrt for dem å betale alt?", "a": "Siste ledd gir en bitte liten sikkerhetsventil for utbygger (lemping). Hvis erstatningen er helt ruinerende urimelig for dem, kan dommeren redusere beløpet. Men dette skjer nesten aldri."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "35", "tittel": "§ 35", "available": True},
        {"lov": LOV, "paragraf": "22", "tittel": "§ 22", "available": True},
        {"lov": LOV, "paragraf": "19", "tittel": "§ 19", "available": True},
    ],
},
{
    "number": "37",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Kan du klage direkte til underleverandøren?",
    "description": "Gikk snekkeren konkurs, eller er de vanskelige? Du har rett til å hoppe over dem og sende klagen rett til produsenten av varen.",
    "kort_svar": "Ja. Du trenger ikke alltid gå gjennom firmaet du skrev kontrakt med. Loven gir deg rett til å rette klagen (direktekrav) mot rørleggeren de leide inn, fabrikken som laget vinduet, eller importøren av gulvet, hvis de har gjort en feil.",
    "paragraftekst": "Forbrukaren kan gjere sitt krav som følgje av mangel gjeldande mot ein tidlegare avtalepart som har gjort avtalen som ledd i næringsverksemd, i same mon som mangelen kan gjerast gjeldande av entreprenøren eller annan avtalepart. Avtale som innskrenkar det kravet entreprenøren eller ein annan avtalepart har, kan ikkje gjerast gjeldande mot forbrukaren i større mon enn det som kunne ha vore avtalt mellom forbrukaren og entreprenøren.",
    "hva_betyr_html": _p(
        "I byggebransjen finnes det ofte en lang kjede av firmaer. Du hyrer en hovedentreprenør. De kjøper fliser fra en flisbutikk. Butikken kjøpte dem fra en norsk importør. Importøren kjøpte dem fra Italia.",
        "Hvis flisene sprekker på grunn av en fabrikasjonsfeil, skal du normalt klage til hovedentreprenøren din. Men hva om de har gått konkurs, eller bare nekter å svare på telefonen?",
        "Paragraf 37 er din snarvei. Den gir deg \"direktekravsrett\". Du kan hoppe over din egen entreprenør og gå direkte på flisbutikken eller importøren (det \"bakre leddet\") for å kreve retting eller penger. De har ikke lov til å avvise deg med å si \"du er ikke kunden vår\". Så lenge de har solgt varen som et ledd i sin egen næringsvirksomhet, må de rydde opp.",
        "Loven sier at de heller ikke kan bruke dårlige proff-kontrakter mot deg. Hvis importøren har skrevet i kontrakten med butikken at \"vi gir kun 1 års garanti på disse flisene\", gjelder ikke dette mot deg. Du har dine 5 år etter bustadoppføringslova i behold.",
    ),
    "eksempler": [
        {"navn": "Tom", "tekst": "Tom flytter inn i et nytt hus. Tre år senere begynner vann å lekke inn gjennom et takvindu av merket Velux, på grunn av en feil med selve glassruten. Utbyggerselskapet som bygget huset gikk konkurs i fjor. Tom kontakter Velux Norge direkte og reklamerer på feilen etter § 37. Velux kan ikke be ham om å ta det med konkursboet. De er det \"tidligere avtalepart\" og må ta saken, og de dekker et nytt vindu."},
    ],
    "vanlige_feil": [
        "Å gi opp saken når utbyggeren går konkurs, fordi man glemmer at man kan gå etter fabrikken, grossisten eller underleverandøren i stedet.",
        "Å tro at produsenten har ansvaret for feilmontering. Rørlegger-firmaet har ansvaret hvis de skrudde røret skjevt på.",
        "Vente for lenge med å sende klagen til det bakre leddet.",
    ],
    "hva_bor_du_html": _p(
        "Det er alltid ryddigst å klage til den utbyggeren du har skrevet kontrakt med. La dem ordne opp med sine egne leverandører. Men hvis saken stopper opp der, be dem om en liste over hvem som leverte hva. Hvis problemet er vinduene, badet eller ventilasjonen, finn ut hvem som er den norske produsenten eller importøren. Send en formell klage til dem og vis til \"direktekrav etter bustadoppføringslova § 37\".",
    ),
    "dumme_sporsmal": [
        {"q": "Hva om produsenten holder til i Tyskland?", "a": "I teorien gjelder regelen uansett, men i praksis er det svært vanskelig å føre en rettssak mot et tysk selskap i Tyskland som privatperson. Gå derfor alltid etter den norske importøren eller grossisten som solgte varen til din utbygger."},
        {"q": "Snekkeren min kjøpte trappa brukt av en annen privatperson. Kan jeg klage til ham?", "a": "Nei. Paragrafen krever uttrykkelig at den tidligere parten må ha handlet som \"ledd i næringsverksemd\". Privatpersoner har du ingen direktekrav mot."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "38", "tittel": "§ 38", "available": True},
        {"lov": LOV, "paragraf": "25", "tittel": "§ 25", "available": True},
        {"lov": LOV, "paragraf": "30", "tittel": "§ 30", "available": True},
    ],
},
{
    "number": "38",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Når tredjepersonen skrøt på seg noe",
    "description": "Du kan også kreve erstatning fra produsenten hvis reklamen deres viste seg å være usann.",
    "kort_svar": "Hvis produsenten av vinduet eller parketten ga falske opplysninger i sin egen reklame, kan du kreve erstatning (skadebot) direkte fra produsenten. De står ansvarlig for lovnadene de sprer.",
    "paragraftekst": "Ein person som ikkje har mangelsansvar etter § 37, svarer andsynes forbrukaren etter reglane i § 35 dersom vedkomande har gjeve slike opplysningar om ytinga som § 27 nemner, på vegner av entreprenøren eller i eigenskap av eller på vegner av tidlegare leverandørledd.",
    "hva_betyr_html": _p(
        "Paragraf 38 henger tett sammen med paragraf 37 (direktekrav) og 27 (uriktige opplysninger i markedsføring).",
        "Se for deg at du kjøper et hus. Snekkeren monterer en ekstremt dyr terrassebord-type fra en produsent. Produsenten har en plakat der det står: \"Denne typen treverk vil aldri råtne\". Fire år senere er treverket pillråttent.",
        "Selv om produsenten ligger langt bak i kjeden, og selv om du aldri tegnet kontrakt direkte med dem, kan du saksøke dem for at de løy. De \"svarer andsynes forbrukaren\". Fordi produsenten aktivt har gitt falske eller villedende opplysninger i sin markedsføring (se § 27), fanger loven dem direkte.",
    ),
    "eksempler": [
        {"navn": "Kari", "tekst": "Kari bygger nytt. I en katalog fra vindusprodusenten \"Glassfabrikken AS\" står det tydelig: \"Alle våre vinduer garanteres 100 % lyddempende for trafikkstøy over 60 dB\". Huset bygges, og Kari hører bilene tydelig gjennom lukket vindu. Hun oppdager at glassene ikke isolerer på langt nær det reklamen lovet. Hovedentreprenøren nekter å ta ansvar fordi \"det var bare de vinduene Glassfabrikken sendte oss\". Kari bruker § 38 og retter kravet for feil markedsføring direkte mot Glassfabrikken AS, og krever utgiftene til nye vinduer dekket av dem."},
    ],
    "vanlige_feil": [
        "Å la en produsent slippe unna løgnaktig reklame med argumentet \"du kjøpte ikke av oss direkte\".",
        "Glemme å klage raskt nok til selve produsenten.",
    ],
    "hva_bor_du_html": _p(
        "Ta vare på produktark, brosjyrer og FDV-dokumentasjon (Forvaltning, Drift, Vedlikehold) for alt det dyre utstyret i huset: varmepumper, sentralstøvsuger, vinduer, smarthus-systemer og taktekking. Det er disse dokumentene som beviser at produsenten lovet en funksjon.",
    ),
    "dumme_sporsmal": [
        {"q": "Hvorfor gå på produsenten og ikke bare snekkeren?", "a": "Vanligvis går du på snekkeren (hovedentreprenøren). De har totalansvaret. Men av og til er snekkeren gått konkurs, eller de krangler så voldsomt at det faktisk er lettere å gå rett på et stort, seriøst produsentfirma som bare vil rydde opp for merkevarens skyld."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "37", "tittel": "§ 37", "available": True},
        {"lov": LOV, "paragraf": "27", "tittel": "§ 27", "available": True},
        {"lov": LOV, "paragraf": "35", "tittel": "§ 35", "available": True},
    ],
},
{
    "number": "39",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Noen andre eier noe i huset ditt (Rettsmangel)",
    "description": "Du tok over et nytt hus, men så får du beskjed om at naboen har tinglyst rett til å bruke veien din, eller at banken har pant i tomten. Slik løser loven det.",
    "kort_svar": "Hvis det viser seg at en tredjeperson har rettigheter i eiendommen din (for eksempel et panteselskap, eller naboen), kalles det en rettsmangel. Loven gir deg rett til å kreve prisavslag, erstatning, eller i verste fall at du leverer huset tilbake, på samme måte som ved fysiske feil.",
    "paragraftekst": "Har ein tredjeperson eigedomsrett, panterett eller annan rett i det entreprenøren skal yte, gjeld føresegnene om manglar tilsvarande, om ikkje forbrukaren etter avtalen skal overta heftet. Forbrukaren kan likevel ikkje krevje retting etter § 32.",
    "hva_betyr_html": _p(
        "Feil i et hus handler ikke bare om vannlekkasjer. Det kan også være juridiske feil. Du kjøper kanskje en prosjektbolig og forventer at hele hagen er din egen. Men etter at du har betalt, finner du ut at naboen har tinglyst en evig bruksrett til å kjøre traktor over hagen din. Eller du oppdager at utbyggerens bank fortsatt har et pantedokument på 5 millioner liggende på din tomt.",
        "Dette er \"rettsmangler\". Du eier rett og slett ikke 100 % av det du trodde du kjøpte.",
        "Paragraf 39 sier at dette skal behandles nesten likt som fysiske mangler. Du kan kreve penger tilbake (prisavslag). Men, ganske logisk, du kan ikke kreve \"retting\" av entreprenøren (at snekkeren skal reise ned med hammer for å fjerne naboens juridiske rettighet).",
    ),
    "eksempler": [
        {"navn": "Lars", "tekst": "Lars kjøper og overtar en nybygget hytte inkludert tomt av Utbygger AS. Et år senere får Lars et inkassovarsel i posten. Utbygger AS glemte å slette et pantlån (heftelse) de hadde på tomten fra sin egen bank før de overførte den til Lars. Nå krever banken tomta tvangssolgt fordi Utbygger AS ikke har betalt regningene sine. Dette er en rettsmangel. Lars krever erstatning av Utbygger AS, som må punge ut for å betale slette-gebyret til banken slik at Lars får tomten gjeldfri."},
    ],
    "vanlige_feil": [
        "Å ikke lese grunnboken (tinglyste heftelser) før man signerer på en eiendom.",
        "Å tro at utbygger ikke har ansvar for at tomten selges med andres pantelån liggende der.",
    ],
    "hva_bor_du_html": _p(
        "Sjekk alltid grunnboken hos Kartverket (dette er gratis) før du kjøper et boligprosjekt. Det skal stå \"Ingen heftelser\" eller bare heftelser som du aksepterer (som for eksempel borettslagets fellesgjeld). Hvis det plutselig ligger en uavklart rettighet der etter overtakelsen, send et umiddelbart erstatningskrav til utbyggeren for å få det slettet.",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg erstatning hvis noen har tinglyst rett til å ha vannrør under min hage?", "a": "Trolig ja, hvis det begrenser din bruk av hagen og du ikke fikk vite det på forhånd. Det er en rettsmangel. Koster det deg penger eller verdi, kan du kreve prisavslag."},
        {"q": "Hva skjer hvis naboen bare har en muntlig avtale med den tidligere tomteeieren?", "a": "Da er det vanligvis naboens problem, siden usignerte og utinglyste avtaler sjelden er gyldige mot en ny kjøper i god tro. Entreprenøren må uansett rydde opp i det."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "40", "tittel": "§ 40", "available": True},
        {"lov": LOV, "paragraf": "29", "tittel": "§ 29", "available": True},
        {"lov": LOV, "paragraf": "25", "tittel": "§ 25", "available": True},
    ],
},
{
    "number": "40",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Kommunen sier nei til å bruke tomten",
    "description": "Du kjøper et hus, men kommunen har lagt ned et lokalt byggeforbud, og du kan ikke bruke garasjen. Dette gir deg de samme rettighetene som ved byggefeil.",
    "kort_svar": "Hvis eiendommen du overtar har \"offentligrettslige rådighetsbegrensninger\" – som betyr at kommunen eller staten har bestemt noe som begrenser din bruk av eiendommen – regnes dette som en mangel (feil) som du kan klage på.",
    "paragraftekst": "For avtalar som omfattar rett til grunn (§ 1 første ledd bokstav b), gjeld føresegnene om manglar tilsvarande i høve til offentlegrettslege rådvaldsband eller offentlegrettslege tyngsler på eigedomen.",
    "hva_betyr_html": _p(
        "Paragraf 40 er en fortsettelse av paragraf 39. Men mens § 39 handler om at naboen eller banken har private rettigheter på tomta di, handler § 40 om at det offentlige stikker kjepper i hjulene.",
        "Når du kjøper en ny bolig inkludert tomt (prosjekt), forventer du at boligen er fullt lovlig å bo i. \"Offentlegrettslege rådvaldsband\" betyr vedtak fra stat, kommune eller fylke.",
        "Eksempler: Du får ikke brukstillatelse på boligen fordi den er bygget over en kommunal vannledning i strid med reguleringsplanen. Boligen mangler brannseksjonering og kommunen nedlegger bruksforbud på kjelleren. Kommunen har vedtatt ekspropriasjon og utbygger skjulte dette.",
        "Slike restriksjoner fra det offentlige er utbyggerens ansvar. De solgte deg en tomt som ikke har de kvalitetene en vanlig bolig skal ha. Siden feilen regnes som en mangel, kan du kreve prisavslag, erstatning eller i ytterste konsekvens heve hele kjøpet.",
    ),
    "eksempler": [
        {"navn": "Sofie", "tekst": "Sofie har nettopp overtatt en nøkkelferdig hytte av Utbygger AS. Tre uker senere kommer det et brev fra fylkesmannen. Brygga som hørte til hytta, er bygget i et vernet naturreservat uten gyldig dispensasjon, og staten krever at Sofie river den. Sofie sjekker § 40. Hytta er solgt med en offentlig tyngsle/restriksjon hun ikke ble opplyst om. Sofie kan henvise utbyggeren til denne loven og kreve flere hundre tusen kroner i prisavslag, fordi en hytte uten brygge har mye lavere verdi."},
    ],
    "vanlige_feil": [
        "Å tro at man er overlatt til seg selv i kampen mot kommunen for en ulovlig bygget garasje man nettopp har kjøpt ny. Du skal rette kravet direkte mot utbygger.",
        "Å ikke be utbygger fremlegge midlertidig brukstillatelse eller ferdigattest før overtakelse.",
    ],
    "hva_bor_du_html": _p(
        "Dersom kommunen sender et brev om \"ulovlig bruk\" av det nye bygget, ring dem først for å forstå hva vedtaket gjelder. Send deretter umiddelbart e-post til utbygger: \"Viser til vedtak fra kommunen datert dd.mm.åå. Da eiendommen lider av offentligrettslige rådighetsbegrensninger jeg ikke ble varslet om, utgjør dette en mangel etter bustadoppføringslova § 40.\"",
    ),
    "dumme_sporsmal": [
        {"q": "Hva om reguleringsplanen bare sier \"potensielt støyområde\"?", "a": "Det må foreligge en faktisk begrensning eller forbud. Et generelt varsel i reguleringsplanen om støy kan utgjøre en mangel etter \"manglende opplysninger\" (§ 26), men er vanligvis ikke et \"rådvaldsband\" etter denne paragrafen."},
        {"q": "Gjelder dette hvis jeg eide tomten selv fra før?", "a": "Paragrafen gjelder uttrykkelig bare når avtalen omfatter rett til grunn (prosjektbolig). Har du eid tomten din i ti år og ber noen bygge et hus der, er det du som sitter med ansvaret."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "39", "tittel": "§ 39", "available": True},
        {"lov": LOV, "paragraf": "29", "tittel": "§ 29", "available": True},
    ],
},
{
    "number": "41",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Hva er prisen hvis dere ikke avtalte noe?",
    "description": "Du bestilte en snekker, men glemte å spørre hva det kostet. Nå har du fått en regning du mener er galskap. Hvor mye har de egentlig lov å kreve?",
    "kort_svar": "Du skal betale den prisen dere har avtalt. Er ingen pris avtalt, skal du kun betale det som regnes som en \"rimelig pris\" i markedet. Har de gitt deg et prisoverslag, kan sluttregningen maks bli 15 prosent dyrere. Merverdiavgift (moms) skal alltid være inkludert.",
    "paragraftekst": "Forbrukaren skal betale det vederlaget som er avtalt. I den mon det ikkje er avtalt kva vederlag entreprenøren har krav på, skal forbrukaren betale eit vederlag som dekkjer nødvendige kostnader og eit rimeleg påslag. Dersom entreprenøren har gjeve eit prisoverslag, skal vederlaget ikkje overstige den oppgjevne summen vesentleg, og høgst med 15 prosent.",
    "hva_betyr_html": _p(
        "Paragraf 41 rydder opp i de vanligste pengekranglene i byggebransjen.",
        "Regning uten avtalt pris: Sier du bare \"kan du bygge denne verandaen?\", og ikke ber om pris, går avtalen på regning. Da sier loven at du skal betale for \"nødvendige kostnader\" pluss et \"rimelig påslag\". Dette er løpende timer og materialer til normal markedspris.",
        "Prisoverslaget (15%-regelen): Hvis entreprenøren sier \"Det vil koste cirka 500 000 kroner\", er dette et prisoverslag. Loven setter et tak: De kan aldri kreve mer enn 15 % på toppen av dette. Sluttregningen kan altså ikke bli mer enn 575 000 kr.",
        "Moms: Noen useriøse aktører legger på \"25 % MVA\" med små bokstaver på den aller siste fakturaen. Det er ulovlig overfor privatpersoner. Alle priser en håndverker gir deg skal alltid inneholde moms.",
        "Prisstigning: Utbyggeren kan ikke sende deg et gebyr for \"økning i trelastprisene\", med mindre det står skriftlig nedfelt i avtalen at de har lov til å prisregulere kontrakten.",
    ),
    "eksempler": [
        {"navn": "Ola", "tekst": "Ola skal grave opp hagen og asfaltere. Han spør en entreprenør hva det vil koste. Entreprenøren sender en SMS: \"Estimert pris på gravejobben ca. 100 000 kr\". Ola svarer ja. Tre uker senere dumper det ned en faktura i innboksen på 150 000 kroner + MVA, totalt 187 500 kr. Ola sjekker § 41. Han avviser regningen. SMS-en er et prisoverslag. Taket på 15 % betyr maksimalt 115 000 kr. Og siden MVA alltid skal være inkludert overfor forbrukere, var estimatet deres på 100 000 allerede inkludert MVA. Ola betaler lovlig 115 000 kr for hele jobben."},
    ],
    "vanlige_feil": [
        "Å godta en dyr regning basert på at de brukte \"mange fler timer enn forventet\" når de allerede hadde gitt et prisoverslag.",
        "Å ikke be om priser skriftlig.",
        "Utbyggere som nekter å bære smellen for egne grove bom-kalkyler i et anbud.",
    ],
    "hva_bor_du_html": _p(
        "Be alltid om fastpris. Unngå ord som \"anslag\", \"estimat\" eller \"timepris\" i kontrakten. Har du først fått et prisoverslag, og ser at byggeprosessen ser ut til å dra ut, minn håndverkeren vennlig om 15%-regelen.",
    ),
    "dumme_sporsmal": [
        {"q": "Fungerer 15%-regelen hvis jeg har bedt dem om å bygge en carport etter at estimatet ble gitt?", "a": "Nei. Regelen gjelder det opprinnelige prisoverslaget. Bestiller du endringer og ber om et tilbygg som gjør prosjektet dyrere, faktureres dette i tillegg til de opprinnelige 15 prosentene."},
        {"q": "Kan utbygger kreve 15 % mer uten grunn, selv om estimatet deres var perfekt?", "a": "Nei. De skal kun fakturere for de faktiske timene og materialene de brukte. 15 % er bare et absolutt pristak."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "42", "tittel": "§ 42", "available": True},
        {"lov": LOV, "paragraf": "3", "tittel": "§ 3", "available": True},
        {"lov": LOV, "paragraf": "9", "tittel": "§ 9", "available": True},
    ],
},
{
    "number": "42",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Hva koster det å endre planene?",
    "description": "Har du bestemt deg for å få eikeparkett i stedet for furu? Denne regelen styrer hvordan snekkeren skal regne ut den nye prisen for deg.",
    "kort_svar": "Når du gjør endringer underveis i byggingen, skal prisen forhøyes eller senkes ut fra hva endringen faktisk koster snekkeren i materialer og tid, pluss et normalt fortjenestepåslag.",
    "paragraftekst": "Partane kan krevje justering av vederlaget som følgje av endringar og tilleggsarbeid i den mon det følgjer av den opprinnelege avtalen eller er fastsett i særskilt skriftleg avtale om endringane eller tilleggsarbeidet.",
    "hva_betyr_html": _p(
        "Gjennom byggeprosjektet (ifølge § 9) har du rett til å bestille endringer (tilvalg) og fjerne ting (fradrag). Paragraf 42 forteller hvordan regningen påvirkes.",
        "Første ledd er drømmescenariet: Dere avtaler prisen skriftlig før jobben gjøres. \"Ny eikeparkett i stedet for standard vil koste 25 000 kroner ekstra.\" Ferdig snakka.",
        "Andre ledd dekker det som skjer i den virkelige verden: Snekkeren står i stua di, du ber om at en vegg flyttes, han sier \"ok\", og ingen snakker om penger. Snekkeren kan etter loven bare kreve ekstra penger for dette dersom han varslet deg om at det ville koste ekstra akkurat da du ba om det, eller hvis du, som en normalt oppegående person, måtte skjønne at det selvsagt koster ekstra å flytte en helt ny vegg.",
        "Tredje ledd er prisformelen. Hvis du la til veggen, skal du betale for de faktiske, dokumenterte utgiftene snekkeren hadde til materialer og ekstra timer, pluss det vanlige påslaget de tjener penger på.",
    ),
    "eksempler": [
        {"navn": "Kari", "tekst": "Kari bygger nøkkelferdig hus. Etter at grunnmuren er støpt, ringer hun entreprenøren og sier: \"Jeg vil ha varmekabler i garasjegulvet også.\" Entreprenøren svarer \"Vi fikser det!\", men nevner ikke pris. Ved sluttoppgjøret krever entreprenøren 50 000 kr ekstra for kablene. Kari nekter å betale fordi de ikke krevde tillegg der og da. Men Kari taper saken. Bokstav b sier at hun, som huseier, måtte skjøne at det å kjøpe inn og montere varmekabler i et nytt gulv koster ekstra penger."},
    ],
    "vanlige_feil": [
        "Muntlige tilvalg uten å spørre om \"Hva blir ekstrakostnaden for dette, helt konkret?\".",
        "Entreprenører som prøver å kreve urealistisk høye timesatser for endringer fordi du nå er \"låst\" til dem som leverandør.",
        "Forbrukere som forventer at de kan trekke ut dyre kjøkken fra entreprenøren for å kjøpe det på IKEA, og tror de får refundert 100 % av katalogprisen.",
    ],
    "hva_bor_du_html": _p(
        "Ikke godta \"vi tar det på regning\" når du gjør endringer i en fastpriskontrakt. Skriv alltid en e-post der du bestiller endringen, og be om at de skriftlig bekrefter summen, og om det vil påvirke overleveringsdatoen.",
    ),
    "dumme_sporsmal": [
        {"q": "Fakturagrunnlaget viser at snekkeren tok 20 prosent påslag på materialene han la til for meg. Er det lov?", "a": "Ja. Det kalles \"entreprenørens påslag\". Et påslag på rundt 10 til 20 prosent oppå innkjøpsprisen regnes normalt som \"rimelig\" i norsk byggebransje."},
        {"q": "Snekkeren foreslo selv å bytte ut treverket på terrassen fordi de var utsolgt, men sendte faktura på 10 000 kr ekstra. Må jeg betale?", "a": "Nei, ikke hvis det var deres problem som løste seg ved byttet, og du ikke krevde oppgraderingen."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "9", "tittel": "§ 9", "available": True},
        {"lov": LOV, "paragraf": "41", "tittel": "§ 41", "available": True},
        {"lov": LOV, "paragraf": "43", "tittel": "§ 43", "available": True},
    ],
},
{
    "number": "43",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Ekstrautgifter fordi du rotet det til",
    "description": "Hvis du somlet med betalingen eller glemte å rydde tomta, slik at entreprenøren måtte bruke ekstra tid, kan de kreve kompensasjon for dette.",
    "kort_svar": "Entreprenøren kan kreve mer penger av deg (tilleggsvederlag) hvis du som kunde er skyld i at de har fått unødvendige kostnader, for eksempel fordi du ikke dukket opp for å slippe dem inn, eller fordi du manglet byggetillatelse.",
    "paragraftekst": "Entreprenøren kan krevje tilleggsvederlag for nødvendige kostnader som kjem av forhold på forbrukarens side, med tilsvarande endring av entreprenørens påslag. Entreprenøren kan likevel ikkje krevje tilleggsvederlag på grunn av manglande medverknad dersom forbrukaren har krav på tilleggsfrist etter § 51.",
    "hva_betyr_html": _p(
        "Akkurat som entreprenøren må betale dagmulkt når de roter med tiden, må du betale hvis du kaster bort entreprenørens tid og penger.",
        "\"Forhold på forbrukerens side\" dekker alt du hadde ansvaret for. For eksempel: Det er avtalt at du selv skal fjerne alle paller og rydde tomten hver fredag. Du glemmer det, og graveren kan ikke komme frem mandag morgen. Graveren må bruke to timer på å flytte paller før han kan starte gravingen. Entreprenøren kan da kreve at du betaler for de to timene gravemaskinen og arbeideren gikk tomgang.",
        "Unntaket i siste setning er din \"force majeure\". Hvis du ikke kunne rydde tomten fordi lynet slo ned og brente opp bilen din, og du varsler om dette, har du rett på en fristutsettelse. Da kan ikke entreprenøren gi deg noen strafferegning.",
    ),
    "eksempler": [
        {"navn": "Per", "tekst": "Per pusser opp huset. Kontrakten sier at Per skal kjøpe inn og levere alt av fliser og baderomsinnredning, mens entreprenøren skal montere. Den dagen rørleggeren og flisleggeren kommer til huset, er ikke varene ankommet. Arbeiderne må snu, reise tilbake til brakka, og bedriften taper arbeidsdagen. Entreprenøren sender Per en faktura på 8 000 kroner for \"bomtur og tapt arbeidstid\". Per må betale denne."},
    ],
    "vanlige_feil": [
        "Forbrukere som avtaler å gjøre stor egeninnsats (male, legge gulv), uten å innse at forsinkelser i eget arbeid vil koste dyrt.",
        "Å ikke slippe håndverkerne inn på avtalt tid, for deretter å nekte å betale bomtur-fakturaen.",
    ],
    "hva_bor_du_html": _p(
        "Pass på avtalen. Hvis kontrakten sier at du skal skaffe godkjenninger fra kommunen, sikre at tomten er ryddet, eller levere materialer innen 1. september – overhold den fristen. Ligger du an til å bomme på din egen frist, må du informere entreprenøren skriftlig uker i forveien.",
    ),
    "dumme_sporsmal": [
        {"q": "Kommunen somlet med byggetillatelsen. Er det \"min skyld\"?", "a": "Ja, overfor entreprenøren er dette ditt ansvar. Entreprenøren bryr seg ikke om at byråkratiet går sakte; for dem er tomten ulovlig å gå inn på, og de mister tid."},
        {"q": "Må jeg betale entreprenørens \"påslag\" på den tiden de satt og ventet på meg?", "a": "Ja, loven sier \"med tilsvarande endring av entreprenørens påslag\". De skal ikke bare ha dekket selve lønnen til snekkeren; de har lov til å kreve det de normalt ville tjent som bedrift de timene."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "42", "tittel": "§ 42", "available": True},
        {"lov": LOV, "paragraf": "51", "tittel": "§ 51", "available": True},
        {"lov": LOV, "paragraf": "50", "tittel": "§ 50", "available": True},
    ],
},
{
    "number": "44",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Skal arkitekten ha betalt før kontrakten er signert?",
    "description": "Du tok et innledende møte med en snekker og fikk noen fine tegninger. Kan de plutselig sende regning for dette? Ikke uten at de advarte deg først.",
    "kort_svar": "Entreprenøren eller arkitekten har ikke lov til å sende deg en faktura for utredninger, tegnearbeid eller prisoverslag de har gjort før dere inngikk den endelige byggekontrakten, med mindre de ga deg krystallklar beskjed på forhånd om at dette arbeidet koster penger.",
    "paragraftekst": "For utgreiingar, teikningar, utarbeiding av pristilbod og for liknande førebuing før ytinga er bestilt, skal forbrukaren berre betale vederlag dersom det er opplyst eller teke atterhald om det på førehand.",
    "hva_betyr_html": _p(
        "Paragrafen beskytter deg mot overraskelsesregninger i den fasen hvor du bare \"shopper rundt\" for å finne riktig byggefirma.",
        "Mange husfirmaer tilbyr seg å tegne skisser, regne på tilbud og foreslå smarte løsninger på tomta di. For bedriften koster dette mye tid. Av og til blir det ikke noe av byggingen. En irritert utbygger prøver da ofte å sende en regning på 15 000 kroner for \"Konsulenttjenester\".",
        "Loven gir dem null og niks. Hovedregelen er at innsalg, tilbud og befaring er gratis markedsføring. Eneste unntak: Firmaet sier allerede på første møte (og kan bevise det): \"Vi kommer gjerne på tomta og tegner et forslag til deg. Dette er en tjeneste vi tar 5 000 kroner for, uansett om du velger oss eller ikke.\" Hvis du da sier \"ja, gjør det\", må du selvsagt betale.",
    ),
    "eksempler": [
        {"navn": "Sofie", "tekst": "Sofie har arvet en eiendom. Hun kontakter \"Lokal Byggmester AS\" og spør hva de vil ta for å bygge en hytte. Byggmesteren kommer på befaring, sender skisser og tegninger, og gir henne et tilbud på 3 millioner kroner. Sofie synes det er for dyrt og velger å ikke bygge i det hele tatt. To uker senere dumper det en regning fra Byggmester AS ned i postkassen på 8 500 kroner for \"Møtevirksomhet og utarbeidelse av prisoverslag\". Sofie avviser fakturaen med henvisning til § 44. Firmaet varslet aldri at de tok betalt for utarbeidelsen av tilbudet."},
    ],
    "vanlige_feil": [
        "Entreprenører som forsøker å \"straffe\" en kunde som valgte konkurrenten, ved å ettersende et krav for tiden de brukte på salget.",
        "Kunder som føler seg skyldige og betaler for arkitekttimer de ikke hadde avtalt.",
        "Entreprenører som skriver med bittesmå bokstaver i bunnen av e-postsignaturen at \"møter faktureres med 1500,-\".",
    ],
    "hva_bor_du_html": _p(
        "Når du kontakter et firma for å få priser og ideer, skriv gjerne i den første e-posten: \"Vi innhenter tilbud fra flere. Kan dere komme med et uforpliktende og kostnadsfritt prisoverslag?\". Får du likevel en regning i etterkant, bestrider du den skriftlig: \"Bestrider faktura. Det var ikke inngått avtale om betaling for forarbeid, jf. bustadoppføringslova § 44.\"",
    ),
    "dumme_sporsmal": [
        {"q": "Hva om jeg ber dem bruke arkitekten sin til å lage godkjente byggetegninger for kommunen, men ikke skriver kontrakt på selve huset?", "a": "Det å tegne et komplett arkitekt-sett som kan sendes inn til en bygge-søknad, er et omfattende oppdrag som i seg selv er \"bestilt\". I slike tilfeller er det stor sjanse for at domstolen anser arbeidet for å gå langt utover et vanlig \"pristilbud og forberedelse\"."},
        {"q": "Entreprenøren ringte og sa muntlig at de tok betalt for befaringen. Gjelder det?", "a": "Ja, det er \"opplyst på førehand\". Hvis de tar det til forliksrådet, vil utfordringen deres være å bevise at telefonsamtalen fant sted."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "41", "tittel": "§ 41", "available": True},
        {"lov": LOV, "paragraf": "61", "tittel": "§ 61", "available": True},
    ],
},
{
    "number": "45",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Hvem betaler hvis huset skades underveis?",
    "description": "Du skal ikke betale for materialer som blir stjålet fra byggeplassen, eller for vegger som blåser over ende før du har flyttet inn. Dette er utbyggers risiko.",
    "kort_svar": "Risikoen for at noe blir ødelagt, stjålet eller brenner ned før den formelle overtakelsesdatoen, ligger 100 prosent på utbyggeren. Entreprenøren må selv betale for å kjøpe nye materialer og bygge opp huset igjen.",
    "paragraftekst": "Forbrukaren skal ikkje betale for arbeid eller materialar som blir skadde eller går tapt ved ei hending før overtakinga som ikkje kjem av forhold på forbrukarens side. Entreprenøren har òg vågnaden for materialar som forbrukaren har skaffa, dersom dei er overlatne til entreprenøren.",
    "hva_betyr_html": _p(
        "\"Vågnad\" er et gammelt ord for risiko. Hvem har ansvaret og regningen hvis katastrofen inntreffer?",
        "Loven gir deg en enorm trygghet under byggetiden. Frem til overtakelsesprotokollen er signert og du får nøkkelen, eier utbyggeren risikoen.",
        "Hvis noen stjeler verktøy og treverk fra tomta i helgen, eller et uvær blåser taket av nybygget, er det et rent tap for snekkerfirmaet. Loven slår fast at de må kjøpe nytt treverk, bestille nytt tak, og bygge det opp igjen – og du skal kun betale det beløpet dere opprinnelig ble enige om i kontrakten.",
        "Loven går faktisk enda lenger i andre setning. La oss si at du kjørte til Maxbo og brukte dine egne sparepenger på 40 000 kr til italienske fliser. Du kjører dem til byggeplassen og sier til snekkeren: \"Vær så god, disse skal brukes på badet.\" I det du overleverer dem til entreprenøren, går risikoen for de knuselige flisene over på entreprenøren.",
        "Unntaket? \"Hending som kjem av forhold på forbrukarens side.\" Besøker du byggeplassen i helgen og velter et malingspann over det nye parkettgulvet, er skaden selvfølgelig din skyld.",
    ),
    "eksempler": [
        {"navn": "Håkon", "tekst": "Håkon og familien gleder seg til å overta det nye ferdighuset om en uke. Lørdag natt brenner huset ned til grunnen. Brannvesenet finner ingen mistenkelig årsak. Entreprenøren må, etter § 45, rydde tomten og bygge opp nøyaktig det samme huset for Håkon på nytt. Håkon skal kun betale den avtalte kontraktssummen når hus nummer to står ferdig."},
    ],
    "vanlige_feil": [
        "At utbygger sender regning til huseier for opprydding etter vandalisme på byggeplassen.",
        "Forbrukere som sier seg villige til å bruke egen innboforsikring på løsøre de har levert på byggeplassen.",
        "Tror at risikoen følger med når man betaler avdragene underveis.",
    ],
    "hva_bor_du_html": _p(
        "Pass på hvem som har tilgang til plassen og materialene. Hvis du har kjøpt egne vinduer som står under en presenning i oppkjørselen, bør du skrive en e-post til utbygger: \"De nye vinduene står nå på tunet og overleveres herved til dere for montering.\" Da har du skriftlig bekreftelse på at risikoen har hoppet over til entreprenøren.",
    ),
    "dumme_sporsmal": [
        {"q": "Får utbyggeren forlenget frist til å bli ferdig hvis bygget brenner?", "a": "Brann eller tyveri er i noen tilfeller force majeure, men ikke alltid. Hvis det brenner på grunn av en ulmende feil i en skjøteledning de selv brukte, er det innenfor deres kontroll."},
        {"q": "Naboen min rygget på en vegg de hadde satt opp. Er det \"min skyld\"?", "a": "Nei, naboen din er ikke en \"person forbrukeren svarer for\". Da må utbyggers forsikringsselskap dekke skaden, og de må ta erstatningskravet videre med naboen."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "14", "tittel": "§ 14", "available": True},
        {"lov": LOV, "paragraf": "13", "tittel": "§ 13", "available": True},
        {"lov": LOV, "paragraf": "55", "tittel": "§ 55", "available": True},
    ],
},
{
    "number": "46",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Når skal du betale for bygget?",
    "description": "Du skal ikke betale noe før du har fått huset, med mindre noe annet er strengt avtalt. Her er hovedreglene for når regningen forfaller.",
    "kort_svar": "Hovedregelen er at du betaler når huset er ferdig og du har fått nøkkelen. Kjøper du tomt og bolig som en pakke (prosjektbolig), skal du betale når skjøtet på eiendommen overføres til deg i grunnboken.",
    "paragraftekst": "Er ikkje betalingstida avtalt, skal forbrukaren betale når entreprenøren krev det etter overtaking. Ved avtalar som omfattar rett til grunn (§ 1 første ledd bokstav b), kan entreprenøren berre krevje betaling mot heimelsoverføring.",
    "hva_betyr_html": _p(
        "I byggebransjen gjelder regelen \"ytelse mot ytelse\". Dette er ryggraden i en rettferdig avtale. Entreprenøren gir deg et hus, og i det samme øyeblikket gir du dem pengene.",
        "Så lenge dere ikke har avtalt noe annet, kan snekkeren sende deg fakturaen den dagen dere skriver under overtakelsesprotokollen. De har ingen rett til å be om \"20 prosent ved byggestart\" med mindre det er uttrykkelig inngått en lovlig avtale om forskuddsbetaling.",
        "Den andre setningen handler om prosjektboliger. Her blir loven enda strengere. Du trenger ikke overføre sluttoppgjøret før entreprenøren fysisk har gitt papirene (skjøtet) til Kartverket slik at du offisielt står som eier.",
        "Loven beskytter selvsagt også entreprenøren: Bygger du et hus, er det en stor risiko for at du ikke har penger når regningen kommer. Derfor sier § 46 at de kan kreve at du beviser betalingsevnen din – som regel i form av et finansieringsbevis fra banken din.",
    ),
    "eksempler": [
        {"navn": "Kari", "tekst": "Kari engasjerer et firma for å bygge et tilbygg på 600 000 kr. De inngår standardkontrakt uten å fylle inn egne betalingsplaner. Etter første dag med graving sender entreprenøren en e-post: \"Vi trenger 200 000 kr overført nå, for å betale sement-leverandøren.\" Kari sjekker § 46 og ser at det ikke er avtalt forskuddsbetaling. Hovedregelen er \"betaling etter overtaking\". Hun nekter pent å betale regningen før tilbygget er 100 prosent ferdig."},
    ],
    "vanlige_feil": [
        "Å føle seg forpliktet til å overføre halve regningen \"slik at snekkeren kan kjøpe materialer\".",
        "Å nekte å levere finansieringsbevis til entreprenøren i starten fordi man synes det er \"privat\".",
    ],
    "hva_bor_du_html": _p(
        "Sjekk kontrakten. Mange standardkontrakter har en ferdig utfylt betalingsplan for \"avdrag\". Signerer du denne, gjelder § 47 i stedet for § 46. Ønsker du maksimal trygghet, streker du over betalingsplanen før du signerer, og krever at dere følger § 46: Alt betales til slutt.",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg sjekke huset etter overtakelse før jeg betaler?", "a": "Loven sier \"etter overtaking\". Det betyr at pengene som hovedregel forfaller i løpet av en vanlig fakturafrist etter at møtet er ferdig og du har fått nøkkelen. Men oppdager du feil på overtakelsen, fryser du en del av oppgjøret (tilbakeholdsrett, § 31)."},
        {"q": "Hva om utbygger krever å ha pengene mine låst (deponert) på meglers konto en måned før overtakelse?", "a": "Dette er veldig vanlig. Du overfører da pengene til meglerens sperrede klientkonto før du får nøkkelen. Megleren utbetaler ikke pengene til entreprenøren før skjøtet er tinglyst på deg."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "47", "tittel": "§ 47", "available": True},
        {"lov": LOV, "paragraf": "14", "tittel": "§ 14", "available": True},
        {"lov": LOV, "paragraf": "48", "tittel": "§ 48", "available": True},
    ],
},
{
    "number": "47",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Strenge regler for forskudd og avdrag",
    "description": "Skal du betale regninger mens huset bygges? Loven stiller knallharde vilkår for at entreprenøren skal få lov til å kreve penger før de er ferdige.",
    "kort_svar": "Entreprenøren kan ikke kreve at du betaler penger raskere enn bygget reiser seg. Betaler du avdrag underveis, krever loven at verdien av materialene og arbeidet på tomta minst tilsvarer det du har betalt. Du skal alltid holde tilbake minst 10 % av totalsummen helt til bygget er overlevert til deg.",
    "paragraftekst": "Avtale om at forbrukaren skal betale avdrag eller forskot på entreprenørens vederlag, gjeld berre så langt verdien av arbeid som er utført på eigedomen, saman med materialar som er tilførte eigedomen, minst svarer til det som til kvar tid er betalt, det ikkje kviler salspant eller andre hefte på materialar som er innbygde eller tilførte eigedomen, og minst ein tiandedel av vederlaget ikkje skal betalast før overtakinga.",
    "hva_betyr_html": _p(
        "Mange byggeprosjekter skjer ved at man betaler tre eller fire store fakturaer i løpet av året bygget tar. Paragraf 47 er skrevet for å unngå at utbyggeren får inn store forskudd og stikker av med dem.",
        "Loven lister opp tre jernharde krav: Ikke forskudd: Du skal aldri betale før jobben er gjort. Hvis snekkeren har støpt grunnmur og satt opp trevegger til en anslått verdi av 400 000 kr, kan de maksimalt be deg om en faktura på 400 000 kr. Ingen gjeld på plankene: Materialene de bruker, skal være betalt for av entreprenøren. Hvis snekkeren slår seg konkurs, skal ikke Montér komme hjem til deg og kreve parketten tilbakebetalt. Ti-prosent-regelen: Utbygger kan aldri kreve 100 % innbetalt før nøkkelen overleveres. 10 % av hele kjøpesummen skal stå på din konto som en \"gissel-sum\" frem til overtakelsen.",
        "For deg som kjøper \"prosjektbolig\", er det en fjerde livsviktig regel: Du skal aldri betale så mye som en krone underveis, uten at du allerede har fått tinglyst hele eiendommen på ditt eget navn. Den eneste måten de kan omgå dette på, er å gi deg en formell bankgaranti for alle forskuddspengene dine.",
    ),
    "eksempler": [
        {"navn": "Jonas", "tekst": "Jonas bygger på egen tomt og har signert en fremdriftsplan. Huset koster 2 000 000 kr. Byggefirmaet graver bare ut et lite hull i hagen (anslått verdi: 50 000 kr), før de sender en \"første avdragsregning\" på 400 000 kroner for å \"komme i gang\". Jonas sjekker § 47. Loven sier verdien av utført arbeid må tilsvare betalingen. Å betale 400 000 kr for et hull i bakken er et usikret forskudd og ulovlig. Jonas bestrider fakturaen."},
    ],
    "vanlige_feil": [
        "Betale hundretusener for \"materialer de sier at de har på lager hos seg\". Materialene må befinne seg på din tomt før de kan regnes med.",
        "Å ikke sjekke om tinglysningen av skjøtet er i orden før man betaler den første millionen i et ferdighus-prosjekt.",
        "Overføre de siste ti prosentene dagen før befaringen for å \"være hyggelig\".",
    ],
    "hva_bor_du_html": _p(
        "Når du får en faktura på et avdrag, ta deg en tur ut på tomta. Vurder om arbeidet som er gjort, rent fysisk er verdt den summen du skal betale nå. Ser du at betalingene ligger milevis foran fremdriften, må du slå bremser på.",
    ),
    "dumme_sporsmal": [
        {"q": "Firmaet sier de ikke har råd til å bestille inn det svindyre kjøkkenet jeg valgte uten at jeg overfører penger til det først. Hva da?", "a": "Loven gir dem et smutthull: De kan be deg betale i forskudd for å kjøpe inn materialene, MEN kun hvis de stiller en egen forskuddsgaranti fra en norsk bank. Uten denne garantien: Nei, ikke betal."},
        {"q": "Kan vi ikke bare bli enige i kontrakten om at de får forskudd, siden vi er venner?", "a": "Nei, Bustadoppføringslova er ufravikelig (§ 3)."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "46", "tittel": "§ 46", "available": True},
        {"lov": LOV, "paragraf": "12", "tittel": "§ 12", "available": True},
        {"lov": LOV, "paragraf": "14", "tittel": "§ 14", "available": True},
    ],
},
{
    "number": "48",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Ryddig sluttoppgjør før betaling",
    "description": "Du har rett til en komplett og forståelig sluttregning. Entreprenøren kan verken ta urimelige administrasjonsgebyrer eller skjule pristillegg.",
    "kort_svar": "Før du betaler den siste regningen, kan du kreve at entreprenøren leverer et tydelig regnskap som kan kontrolleres. Hvis regningen stemmer, har du én måned på deg til å klage før du låses til prisen. Entreprenøren har heller ikke lov til å skrive på bestillings- eller skrivegebyrer.",
    "paragraftekst": "Forbrukaren kan setje som vilkår for betaling av avdrag og sluttoppgjer at entreprenøren legg fram rekning som kan kontrollerast. Tillegg for prisstiging, justering av vederlaget etter § 42 og tillegg etter § 43 skal gå fram særskilt. Rekning for sluttoppgjer utan atterhald er bindande for forbrukaren dersom innvending ikkje er reist seinast ein månad etter at rekninga er motteken. Entreprenøren kan ikkje krevje bestillingsgebyr, ordregebyr, ekspedisjonsgebyr, gebyr for skriving av rekning e.l. i tillegg til vederlaget.",
    "hva_betyr_html": _p(
        "Paragraf 48 sørger for at du og entreprenøren blir ferdige med hverandre økonomisk, på en ryddig måte.",
        "Du har rett til en regning du faktisk forstår. Får du et ark hvor det bare står \"Bygging av hus – 5,6 millioner kr\" og et kontonummer, kan du lovlig stoppe betalingen. Loven krever at regningen skal kunne kontrolleres.",
        "Sendt regning er bindende for entreprenøren. Når de har sendt sluttoppgjøret, kan de ikke våkne tre uker senere og si \"Ops, vi glemte å kreve 40 000 for malingen.\"",
        "Hvis regningen ser grei ut, men du egentlig mener at 10 000 for ekstra stikkontakter er feil – har du nøyaktig én måned på deg til å si ifra. Venter du lengre enn det, låses regningen også for deg, og du må betale.",
        "Til slutt: Ikke aksepter \"fakturagebyr på 49,-\" eller \"administrasjonspåslag 1000,-\". Lovens fjerde ledd forbyr entreprenøren fra å dytte irriterende smågebyrer for eget kontorarbeid over på kunden.",
    ),
    "eksempler": [
        {"navn": "Eva", "tekst": "Eva bygger hytte og har valgt å gjøre en del endringer underveis. Når hytta er ferdig, sender entreprenøren en sluttfaktura på 450 000 kroner med tekst: \"Restbeløp inkludert alle tidligere og nye tillegg og fradrag\". Eva sender regningen tilbake og viser til § 48. Hun krever en ny versjon der de spesifiserer prisen for det opprinnelige restbeløpet, og eksakt pris pr ekstra vindu hun bestilte, pluss fradraget hun skal ha for at hun valgte bort peisen."},
    ],
    "vanlige_feil": [
        "Å betale gebyrer (\"ordregebyr\") blindt fordi \"det stod på regningen\".",
        "At entreprenører fakturerer et klumpbeløp uten spesifikasjon og truer kunden med inkasso.",
        "Å irritere seg over en regning, men glemme å sende et skriftlig avslag innen den absolutte fristen på én måned.",
    ],
    "hva_bor_du_html": _p(
        "Gå alltid gjennom sluttfakturaen med falkeblikk. Finn frem kontrakten og de godkjente tilbudene for endringer du har gjort. Sammenlign prisene. Finner du en utregning som skurrer, send e-posten i kveld: \"Jeg bestrider faktura X på det grunnlaget at punkt 4 om flislegging ikke samsvarer med opprinnelig kontrakt.\"",
    ),
    "dumme_sporsmal": [
        {"q": "Hva om fakturaen er urimelig dyr, og det gikk mer enn en måned?", "a": "Da er det et bittelite håp. Paragrafen har et unntak: Fristen din gjelder ikke hvis regningen er i strid med \"avtalen\" eller den er helt åpenbart \"urimeleg\"."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "41", "tittel": "§ 41", "available": True},
        {"lov": LOV, "paragraf": "42", "tittel": "§ 42", "available": True},
        {"lov": LOV, "paragraf": "46", "tittel": "§ 46", "available": True},
    ],
},
{
    "number": "49",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Slik setter du penger på sperret konto (Deponering)",
    "description": "Utbygger nekter å gi deg nøkkelen fordi du nekter å betale for en byggefeil. Løsningen er å deponere pengene i banken inntil dere er enige.",
    "kort_svar": "Hvis du og entreprenøren krangler om en regning helt på slutten av byggingen, kan dere løse floken ved å låse pengene inne på en sperret konto i en norsk bank. Rettslig sett regnes pengene da som \"betalt\", og utbyggeren må gi deg huset.",
    "paragraftekst": "Er det avtalt at sluttoppgjeret skal vere betalt før overtaking eller før heimelsoverføring, og noko av vederlaget er omtvista, skal betalinga likevel reknast for å vere skjedd dersom den omtvista delen er deponert etter føresegnene i andre og tredje ledd og resten er betalt.",
    "hva_betyr_html": _p(
        "Paragraf 49 er tvisteløseren. Ofte står partene steilt mot hverandre på overtakelsesdagen: Huseieren sier \"Taket lekker, jeg holder igjen 200 000 kroner\". Entreprenøren sier: \"Taket er helt fint, og kontrakten sier at du ikke får nøkkelen før 100 % av pengene er på min konto.\"",
        "Dette skaper en fastlåst situasjon. Men loven gir deg en løsning: Deponering.",
        "Du tar de omstridte 200 000 kronene og ber din egen bank opprette en \"sperret depositumskonto i forbindelse med tvist\". (Resten av kjøpesummen betaler du til entreprenøren). I det øyeblikket banken bekrefter at de 200 000 kronene står trygt på den sperrede kontoen, sier loven at du formelt sett har \"betalt\". Entreprenøren har da mistet retten til å nekte deg huset.",
        "Pengene står der trygt og samler renter. Banken gir dem ikke til snekkeren, og du kan ikke ta dem ut for å kjøpe ny bil. De låses opp først når du og entreprenøren signerer et papir der dere er enige om et forlik, eller hvis dere går i retten.",
    ),
    "eksempler": [
        {"navn": "Håkon", "tekst": "Håkon er i en heftig diskusjon med utbygger om en forsinkelse som ga ham 50 000 kr i dagmulkt. Utbyggeren nekter å anerkjenne forsinkelsen, krever betaling og nekter å tinglyse huset før alt er innbetalt. Håkon går til banken sin, oppretter en deponeringskonto etter § 49, og setter inn de omstridte 50 000 kronene der. Banken sender en bekreftelse. Håkon oversender dette til utbygger og krever nøklene. Utbygger er lovpålagt å utlevere nøklene."},
    ],
    "vanlige_feil": [
        "Å godta meglerens beskjed om at \"vi kan holde dem på vår meglerkonto inntil videre\". Bruk din egen bank.",
        "Utbyggere som nekter overlevering av huset fordi de \"ikke anerkjenner deponering\". Deponering er en ufravikelig rett du har.",
    ],
    "hva_bor_du_html": _p(
        "Snakk med banken din før selve overtakelsesforretningen hvis du vet at det blir bråk. Spør dem: \"Hvordan oppretter vi en deponeringskonto etter bustadoppføringsloven § 49 hvis det trengs raskt?\".",
    ),
    "dumme_sporsmal": [
        {"q": "Får utbyggeren rentene som bygger seg opp på kontoen mens vi venter i årevis på rettssak?", "a": "Den som vinner pengene, får også de tilhørende rentene. Hvis retten sier at du hadde rett til prisavslaget, får du ut pengene pluss den renten banken har lagt til mens den var låst."},
        {"q": "Koster det penger å ha en slik sperret konto?", "a": "Vanligvis vil banken ta et lite etableringsgebyr, men dette dekkes normalt av selve renten kontoen skaper."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "31", "tittel": "§ 31", "available": True},
        {"lov": LOV, "paragraf": "24", "tittel": "§ 24", "available": True},
        {"lov": LOV, "paragraf": "14", "tittel": "§ 14", "available": True},
    ],
},
{
    "number": "50",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Du må faktisk gjøre din del av jobben",
    "description": "Du kan ikke bare lene deg tilbake og klage på at huset ikke blir ferdig hvis du selv aldri leverer fargen du skulle male med, eller holder tomten låst.",
    "kort_svar": "Byggeprosjektet er et samarbeid. Loven krever at du møter opp til avtalt tid for avgjørelser, leverer papirer du har lovet å skaffe, og ikke stenger entreprenøren ute fra byggeplassen.",
    "paragraftekst": "Skal forbrukaren eller nokon forbrukaren svarer for, levere teikningar, skaffe materialar eller medverke på anna vis, skal medverknaden ytast til den tida som er avtalt, og elles til slik tid at det blir teke rimeleg omsyn til utføringa av entreprenørens arbeid.",
    "hva_betyr_html": _p(
        "Selv om det er entreprenøren som bygger huset, har du som huseier også en juridisk plikt i kontrakten. Dette kalles \"medvirkningsplikt\".",
        "Hvis du har inngått en avtale hvor snekkerne trenger ditt samtykke før de kjøper flisene, kan du ikke vente i tre uker med å bestemme deg. Du må yte din innsats i tide.",
        "Andre eksempler på medvirkning er at du faktisk er tilstede og låser opp hytta den dagen de skal begynne, at arkitekten du leide inn leverer tegningene til snekkeren i tide, og at du holder avtaler for å la dem montere byggestrøm.",
        "Bommer du på dette, kan det få store konsekvenser. Du mister da retten til å kreve dagmulkt hvis huset blir forsinket på grunn av deg, og du kan selv bli krevd for ekstra penger.",
    ),
    "eksempler": [
        {"navn": "Sofie", "tekst": "Sofie har avtalt med kjøkkenmontøren at de skal komme mandag morgen klokken 07:00 for å sette opp det nye kjøkkenet. Hun har avtalt at hun selv skal hente og bære inn alle flatpakkene fra Ikea i løpet av helgen. Lørdagen regner bort, og Sofie gidder ikke hente pakkene. Mandag klokken 07:00 står montørene klare, men stua er tom. Sofie har brutt medvirkningsplikten sin etter § 50. Montørene kan lovlig forlate plassen og fakturere Sofie for tapt arbeidstid."},
    ],
    "vanlige_feil": [
        "Å være utilgjengelig på telefon når håndverkerne ringer for å få en \"kjapp avklaring\".",
        "Å overlate \"litt maling\" til en vennegjeng midt i byggetiden, som aldri dukker opp.",
    ],
    "hva_bor_du_html": _p(
        "Be entreprenøren om en tidsplan over \"milepæler for beslutninger\". Dette er utrolig nyttig. Hvis de gir deg et ark hvor det står: \"Farge i stue må velges innen 14. april\", \"Parkett leveres av deg senest 1. mai\", har du klare rammer å forholde deg til.",
    ),
    "dumme_sporsmal": [
        {"q": "Må jeg låse dem inn klokken 06:00 om morgenen hvis de krever det?", "a": "Nei, loven krever at din medvirkning skal skje \"til slik tid at det blir teke rimeleg omsyn\". Avtaler om tilgang gjøres med rimelighet."},
        {"q": "De sier jeg forsinket dem fordi jeg ikke bestilte rørlegger i tide, men jeg visste ikke at jeg skulle gjøre det?", "a": "Du må bare medvirke med det som er avtalt, eller det som åpenbart forutsettes at er ditt ansvar."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "43", "tittel": "§ 43", "available": True},
        {"lov": LOV, "paragraf": "51", "tittel": "§ 51", "available": True},
        {"lov": LOV, "paragraf": "55", "tittel": "§ 55", "available": True},
    ],
},
{
    "number": "51",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Du forsinker arbeidet, men har en god unnskyldning",
    "description": "Klarer du ikke å betale eller gjøre jobben din i tide, kan du få ekstra frist hvis det var banken som sviktet eller stormen som hindret deg.",
    "kort_svar": "Du har krav på mer tid (tilleggsfrist) til å betale regningen eller levere materialer, hvis forsinkelsen skyldes at snekkeren har tabbet seg ut, eller fordi noe helt ekstremt utenfor din kontroll har skjedd.",
    "paragraftekst": "Forbrukaren kan krevje lenging av fristar for betaling og medverknad dersom betalinga eller medverknaden blir seinka på grunn av entreprenørens forhold, eller betalinga eller medverknaden blir seinka på grunn av ei hindring utanfor forbrukarens kontroll, og det ikkje er rimeleg å vente at forbrukaren kunne ha rekna med hindringa på avtaletida.",
    "hva_betyr_html": _p(
        "Denne paragrafen er ditt speilbilde av paragraf 11. Hvis kontrakten din sier at du må betale innen 1. september, eller rydde hagen innen fredag, er det to grunner som fritar deg for den avtalen:",
        "Snekkerens feil: Du skal betale faktura nr. 3 når taket er lukket. Men snekkeren har brukt tre uker lenger enn avtalt på å lukke taket. Da forlenges selvsagt også din frist for å betale fakturaen helt automatisk.",
        "Ekstreme hindringer: Dette er forbrukerens egen \"force majeure\". Skulle du overføre tre millioner kroner 1. desember, men bankenes datasystemer krasjet over hele Europa slik at overføringen kom frem tre dager for sent? Siden du verken kunne forutse det da du kjøpte huset, eller gjøre noe som helst for å fikse bankens IT-system, er det en hindring utenfor din kontroll.",
    ),
    "eksempler": [
        {"navn": "Kari", "tekst": "Kari skal ifølge kontrakten hente nøkkelen og betale sluttoppgjøret for hytta si. Kvelden før går det et gigantisk steinras som kutter all vei til fjellandsbyen, og veivesenet stenger veien i en uke. Kari kan verken sjekke hytta, og nettet i landsbyen er brutt slik at banken ikke kan frigjøre midlene. Utbygger truer med å heve avtalen. Kari har full ryggdekning i § 51. Steinraset var helt utenfor hennes kontroll, og hun får en lovlig utvidet frist for betalingen og overtakelsen."},
    ],
    "vanlige_feil": [
        "Å tro at man får lovlig tilleggsfrist fordi man \"hadde det for travelt på jobben\", \"ble litt syk\" eller \"glemte det\".",
        "Å tro at det faktum at man ikke fikk lån i banken likevel, er en force majeure. Det å ikke ha penger er nesten aldri utenfor din kontroll.",
    ],
    "hva_bor_du_html": _p(
        "Hvis banken roter det til slik at oppgjøret ditt sendes for sent: Send en e-post til entreprenøren umiddelbart. Skriv: \"Pga et sammenbrudd hos DNB er oppgjøret forsinket. Dette er et forhold utenfor min kontroll, og jeg krever derfor tilleggsfrist for oppgjøret etter bustadoppføringslova § 51.\"",
    ),
    "dumme_sporsmal": [
        {"q": "Entreprenøren fakturerte feil beløp og sendte en ny i går, men fristen var i dag. Må jeg betale i dag?", "a": "Nei, du får tilleggsfrist (\"på grunn av entreprenørens forhold\"). De må gi deg den vanlige betalingstiden regnet fra det tidspunktet de endelig sendte deg en riktig faktura."},
        {"q": "Gjelder force majeure hvis jeg mister jobben og går personlig konkurs?", "a": "Nei, som hovedregel dekker sjelden \"penge- og inntektssvikt\" kravene for hindring utenfor kontroll."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "50", "tittel": "§ 50", "available": True},
        {"lov": LOV, "paragraf": "11", "tittel": "§ 11", "available": True},
        {"lov": LOV, "paragraf": "60", "tittel": "§ 60", "available": True},
    ],
},
{
    "number": "52",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Du har rett til å avlyse hele byggeprosjektet",
    "description": "Har livssituasjonen endret seg, og du vil trekke deg fra huskjøpet? Du kan avbestille når som helst, men det kan bli dyrt.",
    "kort_svar": "Du har en ubetinget rett til å avbestille boligen eller deler av den, helt frem til den dagen du overtar nøkkelen. Men du må betale for alt arbeidet snekkeren allerede har utført, pluss erstatning for den fortjenesten snekkerfirmaet taper på at de ikke får bygge huset ferdig.",
    "paragraftekst": "Forbrukaren kan avbestille ytinga eller delar av den før overtaking. For arbeid som er utført før avbestillinga, kan entreprenøren krevje vederlag. Entreprenøren kan vidare krevje skadebot for økonomisk tap så langt forbrukaren rimeleg kunne rekne med tapet som ei følgje av avbestillinga.",
    "hva_betyr_html": _p(
        "Noen ganger skjer livet. Du signerer en byggekontrakt, men to måneder senere mister du jobben, eller du og partneren skiller lag.",
        "Første ledd er krystallklart: Entreprenøren kan ikke tvinge deg til å bygge huset. Du kan ringe dem og si \"stopp, vi avbestiller\".",
        "Men utbyggeren skal ikke tape penger på at du trekker deg. Regningen din deles i to: Du må betale for det som allerede er bygget, og du må betale erstatning for tapt fortjeneste (skadebot). De hadde satt av de neste seks månedene til å bygge for deg, og de forventet å tjene kanskje 400 000 kroner i overskudd. Når du avlyser, mister de denne inntekten.",
        "Loven stiller likevel et krav til utbygger: De må prøve å skaffe seg en ny jobb. Får de et annet byggeoppdrag umiddelbart, taper de ikke fortjenesten sin.",
        "Det finnes et unntak: Din force majeure. Blir du rammet av en ekstrem og uforutsett hindring, slipper du å betale erstatning for tapt fortjeneste.",
    ),
    "eksempler": [
        {"navn": "Jonas og Mette", "tekst": "Jonas og Mette har signert en kontrakt på 3 millioner kroner for bygging av en hytte. Snekkerfirmaet har ikke begynt å bygge ennå, men de har brukt to uker på planlegging og innkjøp. Paret går fra hverandre og må avbestille. Snekkeren sender et krav: 50 000 kr for utført planlegging og materialer, pluss 200 000 kr i tapt fortjeneste fordi de nå har en tom kalender de neste månedene. Jonas og Mette er lovpålagt å betale de 250 000 kronene."},
    ],
    "vanlige_feil": [
        "Å tro at man har en gratis \"angrefrist\" på flere uker når man skriver under en byggekontrakt.",
        "Å ikke be utbyggeren dokumentere at de faktisk tapte penger.",
        "Å nekte å betale fordi man synes det er urettferdig.",
    ],
    "hva_bor_du_html": _p(
        "Må du avbestille, gjør det så tidlig som overhodet mulig. Jo før du sier ifra, jo større sjanse er det for at utbyggeren klarer å fylle kalenderen sin med andre kunder.",
    ),
    "dumme_sporsmal": [
        {"q": "Gjelder dette også hvis jeg bare vil ta ut malerjobben fra kontrakten?", "a": "Ja. Å fjerne deler av prosjektet kalles en del-avbestilling. Men entreprenøren har rett til å kreve utbetalt den fortjenesten de hadde budsjettert med."},
        {"q": "Jeg mistet jobben og fikk ikke lån i banken. Slipper jeg erstatning?", "a": "Nei. Det å ikke få lån i banken regnes som en risiko du bærer selv. Det er ikke en \"hindring utenfor kontroll\" i lovens forstand."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "53", "tittel": "§ 53", "available": True},
        {"lov": LOV, "paragraf": "54", "tittel": "§ 54", "available": True},
        {"lov": LOV, "paragraf": "41", "tittel": "§ 41", "available": True},
    ],
},
{
    "number": "53",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Avbestilling når du kjøper tomt og hus sammen",
    "description": "Kjøpte du hus på utbyggerens tomt? Da er det litt mer komplisert å avbestille. Ofte må utbyggeren ta boligen tilbake og selge den til noen andre.",
    "kort_svar": "Hvis du kjøper en bolig som inkluderer både tomt og hus fra en utbygger, kan du avbestille. Men siden tomten var en del av pakken, kan entreprenøren bestemme at hele avtalen går i vasken. Du må betale utbyggeren erstatning for eventuelle tap de lider når de må selge boligen til noen andre.",
    "paragraftekst": "§ 52 andre til fjerde ledd gjeld ikkje når avbestillinga omfattar rett til grunn. I slike tilfelle kan entreprenøren krevje skadebot for økonomisk tap så langt forbrukaren rimeleg kunne rekne med tapet som ei følgje av avbestillinga.",
    "hva_betyr_html": _p(
        "Paragraf 53 er en tilpasning av avbestillingsreglene, spesielt laget for \"prosjektboliger\" og ferdighus der tomta følger med i prisen.",
        "Hvis du avbestiller et slikt prosjekt, kan du ikke bare betale for den halvferdige grunnmuren og kreve at tomta står der. Utbyggeren eier normalt prosjektet frem til det er ferdig. Utbygger kan sette som vilkår at hele kjøpet annulleres, altså at de beholder tomten og selger det halvferdige huset til en annen familie.",
        "Erstatningen du skal betale fungerer annerledes her enn i paragraf 52. Fordi utbyggeren kan selge boligen (kalt et \"dekningssalg\"), skal du bare betale det de taper på at du trakk deg.",
        "Kjøpte du huset for 4 millioner, men utbygger nå bare klarer å selge det videre til en annen for 3,8 millioner, taper de 200 000 kroner. I tillegg må de kanskje betale megleren 50 000 kroner. Da sender de en erstatningsregning til deg på 250 000 kroner.",
    ),
    "eksempler": [
        {"navn": "Kari", "tekst": "Kari signerer en kontrakt på en nøkkelferdig leilighet i et nytt blokkprosjekt til 5 millioner kroner. Tre måneder senere mister Kari jobben og avbestiller. Utbyggeren legger leiligheten ut på det åpne markedet igjen. Fordi boligmarkedet har steget, får utbyggeren solgt den til en ny kjøper for 5,2 millioner. Siden utbyggeren faktisk tjente mer penger enn de ville gjort med Kari, har de ikke hatt et \"økonomisk tap\". Kari slipper dermed å betale erstatning."},
    ],
    "vanlige_feil": [
        "Å tro at utbyggeren kan beholde hele innskuddet/forskuddet ditt som straff.",
        "Å ikke følge med på hva utbyggeren selger boligen din for.",
    ],
    "hva_bor_du_html": _p(
        "Hvis du må avbestille en prosjektbolig, kan det i noen tilfeller lønne seg å ikke avbestille, men heller vente til boligen er ferdig, overta den, og deretter selge den selv. Da har du full kontroll på salgsprosessen.",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg tilbakebetalt penger hvis utbygger selger boligen dyrere enn jeg kjøpte for?", "a": "Nei. Hvis utbyggeren selger leiligheten din for 500 000 mer enn du hadde avtalt å betale, putter de den gevinsten i sin egen lomme. Du har ingen rett til fremtidig verdistigning."},
        {"q": "Entreprenøren forlanger 10 % av kjøpesummen fordi det er \"standard\". Må jeg betale?", "a": "Hvis de henviser til et fast avbestillingsgebyr, gjelder reglene i paragraf 54. Har dere ikke avtalt et slikt gebyr skriftlig, må de bevise tapet sitt krone for krone."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "52", "tittel": "§ 52", "available": True},
        {"lov": LOV, "paragraf": "54", "tittel": "§ 54", "available": True},
    ],
},
{
    "number": "54",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Faste gebyrer ved avbestilling",
    "description": "For å slippe en lang krangel om hvor mye penger utbygger tapte på at du avlyste, kan dere avtale et fast avbestillingsgebyr i kontrakten.",
    "kort_svar": "I stedet for å finregne på akkurat hvor mye utbyggeren tapte, tillater loven at dere på forhånd avtaler et fast avbestillingsgebyr (normalskadebot). Dette gir forutsigbarhet for begge parter.",
    "paragraftekst": "I staden for skadebotansvar etter § 52 eller § 53 kan avtalen fastsetje ei normalskadebot (avbestillingsgebyr) ved avbestilling. Normalskadebota lyt verke rimeleg i lys av føresegnene i § 52 og § 53.",
    "hva_betyr_html": _p(
        "Det er slitsomt, tidkrevende og dyrt å regne ut nøyaktig hva et byggefirma taper i fremtidig fortjeneste.",
        "Denne lille paragrafen lar utbyggerne putte en \"angre-pris\" inn i kontrakten. Det står typisk: \"Ved avbestilling før igangsettingstillatelse foreligger, belastes et gebyr på 5 % av kjøpesummen. Ved avbestilling etter dette, belastes 10 % av kjøpesummen.\"",
        "Poenget er at verken du eller entreprenøren trenger å dokumentere ett eneste tap. Hever du kontrakten, utløses gebyret automatisk. Avbestiller du en leilighet til 5 millioner der gebyret er 5 %, får du en regning på 250 000 kroner.",
        "Loven stiller bare ett krav: Gebyret må være \"rimelig\". De kan ikke ha en kontrakt som sier \"Ved avbestilling beholder vi 50 % av kjøpesummen\". Da vil domstolene anse avtalen som ugyldig.",
    ),
    "eksempler": [
        {"navn": "Tom", "tekst": "Tom signerer kontrakt for oppføring av en hytte. I kontrakten står det: \"Avbestillingsgebyr utgjør 8 % av kontraktsummen\". Etter seks måneder blir Tom syk, og han mister muligheten til å få lån. Han må avbestille hytta som skulle koste 3 millioner kroner. Snekkeren trenger ikke bevise at de har tapt penger. De sender Tom en regning på 240 000 kroner (8 %)."},
    ],
    "vanlige_feil": [
        "Å signere kontrakter med urimelig høye gebyrer uten å protestere.",
        "Å tro at utbygger kan kreve både det faste avbestillingsgebyret og dokumentert erstatning i tillegg.",
    ],
    "hva_bor_du_html": _p(
        "Sjekk alltid kontrakten for \"Avbestillingsgebyr\" eller \"Normalskadebot\" før du signerer. Er prosentsatsen veldig høy, kan du forsøke å forhandle den ned, eller be om at gebyret trappes.",
    ),
    "dumme_sporsmal": [
        {"q": "Utbyggeren har solgt boligen min videre med stor fortjeneste. Slipper jeg gebyret da?", "a": "Nei, og det er den store risikoen med fast gebyr. Selv om utbyggeren ikke har hatt et eneste reelt økonomisk tap, har de likevel krav på å få betalt det faste avbestillingsgebyret."},
        {"q": "Gebyret står på fakturaen, men ikke i kontrakten. Må jeg betale?", "a": "Nei. Normalskadebot må være \"fastsatt i avtalen\" på forhånd."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "52", "tittel": "§ 52", "available": True},
        {"lov": LOV, "paragraf": "53", "tittel": "§ 53", "available": True},
    ],
},
{
    "number": "55",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Utbyggers rettigheter når DU er forsinket",
    "description": "Betaler du ikke avdragene dine i tide? Loven gir entreprenøren rett til å stanse arbeidet, kreve forsinkelsesrenter, eller kansellere hele byggekontrakten.",
    "kort_svar": "Entreprenøren har en egen verktøykasse med maktmidler mot deg. Hvis du er forsinket med å betale fakturaer, eller hvis du hindrer snekkerne i å jobbe, har entreprenøren rett til å stoppe byggingen, heve kontrakten, og kreve forsinkelsesrenter pluss erstatning fra deg.",
    "paragraftekst": "Dersom betaling eller medverknad frå forbrukarens side ikkje blir ytt til dei tider entreprenøren kan krevje, kan entreprenøren stanse arbeidet og krevje tilleggsvederlag, heve avtalen og krevje skadebot, eller krevje rente og skadebot for rentetap.",
    "hva_betyr_html": _p(
        "Paragraf 55 er speilbildet av paragraf 17. Mens § 17 lister opp hva du kan gjøre mot snekkeren, lister § 55 opp hva snekkeren kan gjøre mot deg.",
        "Utbyggers verktøykasse ser slik ut: Stoppe arbeidet: De kan legge ned hammeren, sette seg i brakka, og sende deg regning for tapt arbeidstid frem til du betaler regningen de venter på. Heve avtalen: Hvis forsinkelsen din er alvorlig (f.eks. banken nekter deg lån og du kan ikke betale i det hele tatt), kan snekkeren avlyse kontrakten. Renter: For hver dag du betaler fakturaen for sent, har de krav på ganske høye forsinkelsesrenter.",
        "Det siste leddet er kanskje det mest brukte i praksis: Entreprenøren har full rett til å skifte lås på huset og nekte å gi deg nøkkelen, helt frem til alle fakturaer er betalt.",
    ),
    "eksempler": [
        {"navn": "Marius", "tekst": "Marius bygger en tomannsbolig og har avtalt å fjerne alt søppel hver søndag. Han glemmer det to uker på rad, og stillaset sperres av søppel slik at snekkerne ikke får bygd taket. Etter § 55 har Marius \"ikke ytt medvirkning\" til tiden. Entreprenøren pakker sakene, stanser arbeidet, og sender Marius et krav om betaling for tapt arbeidstid for de fem snekkerne. Arbeidet starter ikke opp igjen før Marius har ryddet plassen."},
    ],
    "vanlige_feil": [
        "Å holde tilbake betaling i sinne, uten å vise til en lovfestet grunn.",
        "At man ikke har avklart finansiering i banken, og avdragene blir to uker forsinket.",
    ],
    "hva_bor_du_html": _p(
        "Hold fristene dine! Skal du betale 500 000 kroner om fem dager, sjekk i dag at beløpsgrensen i nettbanken din er høy nok. Hvis du lovlig holder igjen penger fordi huset har feil, må du alltid skrive en e-post der du sier: \"Jeg betaler ikke fakturaen fordi jeg utøver tilbakeholdsrett etter § 31\".",
    ),
    "dumme_sporsmal": [
        {"q": "Får utbygger kreve et gebyr (dagmulkt) av meg hver dag jeg er forsinket?", "a": "Nei. Det finnes ingen \"omvendt dagmulkt\" for forbrukere. Utbygger får kun forsinkelsesrenter pluss eventuell kompensasjon for direkte tap."},
        {"q": "Kan snekkerne holde igjen verktøyet mitt som straff?", "a": "Loven gir dem rett til å stanse byggearbeidet og holde huset igjen før overtakelse. Men de har ikke lov til å stjele private gjenstander."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "56", "tittel": "§ 56", "available": True},
        {"lov": LOV, "paragraf": "57", "tittel": "§ 57", "available": True},
        {"lov": LOV, "paragraf": "17", "tittel": "§ 17", "available": True},
    ],
},
{
    "number": "56",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Utbyggeren legger ned arbeidet (Stansing)",
    "description": "Hvis du slutter å betale regningene dine, vil håndverkerne pakke sammen og stanse byggeplassen. De kan også sende deg faktura for tapt arbeidstid.",
    "kort_svar": "Entreprenøren kan stoppe arbeidet midlertidig hvis du ikke betaler avtalt forskudd eller avdrag. De må gi deg beskjed først. Stanses arbeidet, har de krav på ekstra betaling for alle forsinkelser og tap stansen medfører. De plikter imidlertid å sikre byggeplassen før de drar.",
    "paragraftekst": "Betaler forbrukaren ikkje avtalt avdrag eller forskot på entreprenørens vederlag til rett tid, kan entreprenøren gje forbrukaren varsel om stansing. Betaler ikkje forbrukaren snarast råd etter at han har motteke eit slikt varsel, kan entreprenøren stanse arbeidet. Entreprenøren skal likevel i rimeleg omfang sikre utført arbeid og materialar og utstyr som finst på byggjeplassen.",
    "hva_betyr_html": _p(
        "Utbyggere trenger kontantstrøm. Hvis kontrakten sier at du skal betale 1 million kroner når taket er tett, og pengene ikke dukker opp på kontoen deres, er dette et alvorlig kontraktsbrudd.",
        "Paragraf 56 gir dem rett til å stenge byggeplassen. Slik er reglene: Først må de gi deg et varsel. De kan ikke bare stoppe fordi betalingen er tre timer forsinket. Varselet betyr: \"Får vi ikke penger umiddelbart, stopper vi.\"",
        "Hvis du fortsatt ikke betaler, går snekkerne hjem. Men de må opptre proft. De skal dekke til materialer med presenning, stenge for vind og vær, og låse porten (sikring).",
        "I tillegg åpner andre ledd opp for at det blir dyrt for deg. Når byggeplassen stanses, koster det penger å sende arbeiderne hjem eller flytte gravemaskiner. Alt dette kan utbygger legge på den neste fakturaen din.",
    ),
    "eksempler": [
        {"navn": "Ola", "tekst": "Ola har bestilt nytt hus og skal betale det andre avdraget på 600 000 kr. Pengene forfaller 1. april. Ola betaler ikke. Den 4. april sender entreprenøren en e-post om at betalingen uteblir, og at arbeidet vil stanses i morgen hvis ikke pengene mottas. Ola svarer ikke. 5. april dekker snekkerne til veggene og forlater plassen. To uker senere skaffer Ola pengene. Snekkerne kommer tilbake, men Ola får nå et \"tilleggsvederlag\" på 40 000 kr for administrasjon og tapte timer for de to ukene."},
    ],
    "vanlige_feil": [
        "Å overse varselet fra entreprenøren og tro de bare \"truer\".",
        "Å holde tilbake et gigantisk avdrag på 800 000 kr fordi vinduet til 5 000 kr har feil farge.",
    ],
    "hva_bor_du_html": _p(
        "Hvis du vet at banken din er forsinket med overføringen, ikke vent i stillhet. Ring entreprenøren, forklar situasjonen, og send gjerne over en bekreftelse fra saksbehandleren i banken.",
    ),
    "dumme_sporsmal": [
        {"q": "Får de lov til å stanse bygget selv om jeg ikke mottok fakturaen i posten?", "a": "Hvis de har sendt den til adressen/e-posten du har oppgitt, ligger risikoen hos deg. Men de har en varslingsplikt før de stanser arbeidet."},
        {"q": "Må jeg betale regningen hvis stormen blåste ned det usikrede taket etter at de stanset arbeidet?", "a": "Nei, entreprenøren har en streng plikt til å sikre \"i rimelig omfang\". Hvis de slurvet med sikringen, er de erstatningsansvarlige."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "55", "tittel": "§ 55", "available": True},
        {"lov": LOV, "paragraf": "50", "tittel": "§ 50", "available": True},
        {"lov": LOV, "paragraf": "43", "tittel": "§ 43", "available": True},
    ],
},
{
    "number": "57",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Entreprenøren kansellerer kontrakten (Heving)",
    "description": "Du er helt tom for penger og kan ikke betale for bygget. Da har utbyggeren rett til å rive i stykker kontrakten, sparke deg som kunde og saksøke deg.",
    "kort_svar": "Entreprenøren kan avbryte (heve) byggekontrakten hvis du gjør deg skyldig i et vesentlig avtalebrudd, vanligvis at du totalt slutter å betale regningene. Når du har fått skjøtet på huset (tinglyst), mister entreprenøren retten til å heve.",
    "paragraftekst": "Entreprenøren kan heve avtalen dersom forseinking med forbrukarens betaling eller medverknad inneber vesentleg avtalebrot. Entreprenøren kan ikkje heve avtalen etter overtaking eller etter at skøyte eller festedokument er tinglyst eller gjeve forbrukaren.",
    "hva_betyr_html": _p(
        "Paragraf 57 gir utbyggeren den samme \"atomknappen\" som du har: Retten til å heve avtalen. Heving betyr å avbryte hele kjøpet og kreve økonomisk oppgjør.",
        "For at en snekker skal kunne sparke deg som kunde, må ditt brudd være \"vesentleg\". De kan ikke heve en avtale på fire millioner fordi du er to dager forsinket med en regning på fem tusen kroner. \"Vesentlig avtalebrudd\" betyr at du har misligholdt avdrag for flere hundre tusen kroner over lang tid, at banken din har trukket lånetilsagnet ditt, eller at du nekter dem tilgang til tomten over lengre tid.",
        "Men entreprenøren har en \"deadline\". Når du har overtatt huset og skjøtet er tinglyst på deg, er toget gått. Loven sier at da eier du huset. Mangler det da betaling, kan de ikke lenger \"ta huset tilbake\" ved å heve; da må de sende regningen din til inkasso.",
    ),
    "eksempler": [
        {"navn": "Håkon", "tekst": "Håkon er i store økonomiske problemer og klarer ikke å betale det tredje avdraget på 1 million kroner til ferdighus-firmaet. Han svarer ikke på varsler om stans, og det går en måned uten penger. Å utebli med en fjerdedel av kjøpesummen i lang tid, regnes som et vesentlig avtalebrudd. Utbyggeren sender Håkon et brev om at kontrakten er hevet. Firmaet plikter da ikke å bygge huset ferdig, og de kan nå kreve erstatning fra Håkon."},
    ],
    "vanlige_feil": [
        "Å begrave hodet i sanden når man mister finansieringen.",
        "Forbrukere som tror at de kan bare trekke seg gratis ved å \"slutte å betale\" og håpe entreprenøren hever.",
    ],
    "hva_bor_du_html": _p(
        "Mister du betalingsevnen, ta kontakt med utbygger umiddelbart. I stedet for å la dem heve kontrakten og saksøke deg for tap, kan du undersøke om det er bedre å avbestille etter § 52 og forsøke å forhandle frem et akseptabelt erstatningsbeløp.",
    ),
    "dumme_sporsmal": [
        {"q": "Får snekkeren ta med seg vinduene han satte inn sist uke, hvis han hever avtalen?", "a": "Nei, ikke uten videre. Hvis de har satt opp deler av huset på din egen tomt, inngår materialene normalt i det som blir igjen på tomten din."},
        {"q": "Hva menes med at \"skjøtet er tinglyst\"?", "a": "Tinglysing hos Kartverket betyr at samfunnet offisielt anerkjenner at du eier eiendommen."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "58", "tittel": "§ 58", "available": True},
        {"lov": LOV, "paragraf": "56", "tittel": "§ 56", "available": True},
        {"lov": LOV, "paragraf": "20", "tittel": "§ 20", "available": True},
    ],
},
{
    "number": "58",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Oppgjøret når utbygger hever kontrakten",
    "description": "Du mistet lånet og snekkeren kansellerte hele husbyggingen. Her er reglene for hvem som rydder opp og hvordan sluttregningen din blir.",
    "kort_svar": "Når entreprenøren avbryter (hever) avtalen fordi du ikke har betalt, regnes det økonomisk sett som om du har avbestilt frivillig. De skal ha betalt for arbeidet de har gjort pluss tapt fortjeneste, og de må sikre byggeplassen før de forlater den.",
    "paragraftekst": "Blir avtalen heva, har entreprenøren krav på oppgjer som om forbrukaren hadde avbestilt på hevingstidspunktet (§ 52 eller § 53). Etter heving skal entreprenøren i rimeleg omfang sikre utført arbeid og materialar og utstyr som finst på byggjeplassen.",
    "hva_betyr_html": _p(
        "Paragraf 58 forteller hva som skjer i ruinene av en kollapset byggekontrakt når det er du som forbruker som har skylden.",
        "Første ledd gjør oppgjøret ganske enkelt: Det håndteres nøyaktig som om du hadde ringt dem og sagt \"jeg avbestiller\". Det betyr at reglene i § 52 eller § 53 gjelder. Utbyggeren sender deg en faktura som inneholder verdien av alt de har bygget til nå, og i tillegg et krav om erstatning for overskuddet de gikk glipp av.",
        "Andre ledd krever at snekkerne opptrer voksent. Selv om de er sinte fordi du ikke betaler, kan de ikke bare slenge fra seg verktøyet og la det nye taket ditt regne i stykker.",
        "Tredje ledd er viktig hvis du bygger på din egen tomt: Har de skrudd opp gipsplater eller montert et kjøkken i huset ditt, har de som hovedregel ikke lov til å komme med brekkjern og skru det ned igjen.",
    ),
    "eksempler": [
        {"navn": "Tom", "tekst": "Tom bygger tilbygg. Han mister jobben og slutter å betale regningene til tømrerfirmaet. Tømrerfirmaet stanser arbeidet, hever avtalen, og reiser derfra. Før de drar, legger de en vanntett presenning over det åpne taket. De krever deretter at Tom betaler 200 000 kr for reisverket som står der, og 50 000 kr for tapt fortjeneste. Reisverket og vinduene som er montert forblir Toms eiendom på hans tomt, men Tom er skyldig firmaet de 250 000 kronene."},
    ],
    "vanlige_feil": [
        "Entreprenører som i sinne begynner å demontere vinduer og dører fra kundens hus.",
        "Å la være å sjekke om utbyggeren faktisk tjente inn igjen det tapte overskuddet sitt.",
    ],
    "hva_bor_du_html": _p(
        "Når du får sluttregningen etter at entreprenøren har hevet, må du kreve fullt innsyn i utregningene deres. De må dokumentere utgiftene sine og det forventede overskuddet sitt.",
    ),
    "dumme_sporsmal": [
        {"q": "Får de erstatning hvis avbestillingsgebyr var avtalt i kontrakten?", "a": "Hvis dere hadde fylt inn et fast avbestillingsgebyr i kontrakten etter § 54, er det dette beløpet som gjelder."},
        {"q": "De ødela hagen min da de kjørte vekk gravemaskinen. Hvem betaler?", "a": "Sikringsplikten gjelder utført arbeid, men den dekker også at de ikke skal påføre unødig skade på eiendommen din. Har de utført tingskade på tomten din i hevn eller uforsiktighet, kan du rette et motkrav."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "57", "tittel": "§ 57", "available": True},
        {"lov": LOV, "paragraf": "52", "tittel": "§ 52", "available": True},
        {"lov": LOV, "paragraf": "21", "tittel": "§ 21", "available": True},
    ],
},
{
    "number": "59",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": "gjeld",
    "title": "Forsinkelsesrenter når regningen ikke betales",
    "description": "Betaler du sluttoppgjøret to uker for sent, kan utbyggeren legge på strenge forsinkelsesrenter (morarenter) på toppen av regningen.",
    "kort_svar": "Betaler du ikke fakturaen fra utbyggeren innen forfallsdatoen, kan de kreve forsinkelsesrenter for hver dag som går frem til du betaler. Hvis du har en ekstremt god grunn (force majeure) til at du ikke kunne betale, fryses imidlertid renten.",
    "paragraftekst": "Ved forseinka betaling kan entreprenøren krevje rente og skadebot for rentetap etter lov 17. desember 1976 nr. 100 om renter ved forsinket betaling m.m.",
    "hva_betyr_html": _p(
        "Penger har en pris. Når utbyggeren bygger for deg, regner de med å få pengene inn på konto til avtalt tid slik at de kan betale sine egne regninger og ansatte. Når du betaler for sent, tvinger du entreprenøren til å ta opp kreditt.",
        "Paragraf 59 viser ganske enkelt til \"forsinkelsesrenteloven\". Denne loven har en standardrentesats som fastsettes av staten to ganger i året. Den er veldig høy, ofte mellom 8 og 13 prosent i året. Skylder du entreprenøren 2 millioner kroner, og er en måned forsinket med betalingen, kan forsinkelsesrenten fort beløpe seg til nærmere 20 000 kroner bare i renter.",
    ),
    "eksempler": [
        {"navn": "Eva", "tekst": "Eva og banken hennes roter med papirene. Sluttoppgjøret for leiligheten på 4 000 000 kroner forfaller 1. juni. Banken får ikke overført pengene før 15. juni. Entreprenøren mottar pengene to uker for sent. I slutten av måneden får Eva en ny, liten faktura fra entreprenøren på 15 000 kroner. Dette er lovpålagte forsinkelsesrenter for de 14 dagene pengene uteble."},
    ],
    "vanlige_feil": [
        "Å tro at utbyggeren må gi deg et \"nåderom\" før de kan legge på forsinkelsesrenter.",
        "Holde tilbake penger for en byggefeil, og glemme å sende et skriftlig varsel om at man utøver tilbakeholdsrett.",
    ],
    "hva_bor_du_html": _p(
        "Dersom du må utsette en regning fordi du mangler finansiering, si fra til entreprenøren før fakturaen forfaller. Hvis du holder tilbake 50 000 kroner fra sluttoppgjøret fordi vasken lekker, må du umiddelbart sende e-post og presisere: \"Dette beløpet holdes lovlig tilbake, og forsinkelsesrenter skal ikke beregnes av beløpet.\"",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg forsinkelsesrenter hvis utbyggeren er forsinket med å betale tilbake penger de skylder meg?", "a": "Ja. Forsinkelsesrenteloven gjelder begge veier."},
        {"q": "Hva om nettbanken var nede for hele landet, og det ikke var min feil?", "a": "Hvis det var force majeure, har du lovfestet rett på fristforlengelse. Da stopper forsinkelsesrenten å løpe i de dagene nettet var nede."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "55", "tittel": "§ 55", "available": True},
        {"lov": LOV, "paragraf": "46", "tittel": "§ 46", "available": True},
    ],
},
{
    "number": "60",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Langvarig avbrudd",
    "description": "Et jordskred raserer tomten og arbeidet må stanses i et halvt år. Slik kan du komme deg ut av kontrakten uten å betale erstatning.",
    "kort_svar": "Hvis en ekstrem og uforutsett hendelse (force majeure) gjør at byggearbeidet må avbrytes over svært lang tid, slik at forutsetningene for hele avtalen endres, kan både du og entreprenøren bryte kontrakten (seie seg løyst) uten å betale erstatning til den andre.",
    "paragraftekst": "Kvar av partane kan seie seg løyst frå avtalen dersom arbeidet må avbrytast eller ikkje kan kome i gang på grunn av omstende som nemnde i § 11 første ledd bokstav c eller § 51 første ledd bokstav b, i så lang tid at føresetnadene for avtalen blir vesentleg endra.",
    "hva_betyr_html": _p(
        "Noen ganger rammer ulykken hardt. Vi snakker ikke om noen dager med dårlig vær. Vi snakker om ras, krig, globale pandemier som stenger alle grenser i månedsvis, eller et langvarig statlig inngrep.",
        "Paragraf 11 og 51 beskytter dere mot forsinkelser fra \"force majeure\". Men hva skjer hvis kommunen finner en fredet fugl på tomten din, og nedlegger byggeforbud i ett helt år? Det er urimelig at snekkeren skal holde avtalen varm og maskinene klare i et år. Det er også urimelig at du skal være låst til akkurat dette firmaet.",
        "Paragraf 60 sier at når avbruddet varer \"så lenge at forutsetningene for avtalen er vesentlig endret\", kan begge parter si opp avtalen.",
        "Konsekvensen? \"Partane har ikkje krav på skadebot.\" Dere skiller lag, ingen er sure, du betaler for det som faktisk er bygget til nå, og ingen betaler erstatning til den andre for tapt fortjeneste.",
    ),
    "eksempler": [
        {"navn": "Sara", "tekst": "Sara bygger et hus ved en bratt skråning. Halvveis i grunnarbeidet går det et kvikkleireskred på nabotomten. Kommunen evakuerer området, og legger ned et forbud mot all byggevirksomhet i ni måneder. Entreprenøren kan ikke binde opp gravemaskinene og folkene sine så lenge. Entreprenøren sier seg \"løyst frå avtalen\" etter § 60. Sara aksepterer at forutsetningene er borte. Entreprenøren får betalt 150 000 for det de allerede har gravd, avtalen oppløses, og ingen må betale erstatning."},
    ],
    "vanlige_feil": [
        "Å forsøke å bruke § 60 ved vanlige trege perioder.",
        "At entreprenøren krever tapt fortjeneste i det endelige sluttoppgjøret ved bruk av § 60.",
    ],
    "hva_bor_du_html": _p(
        "Dersom prosjektet ditt blir stoppet på ubestemt tid av kommunen, politiet, eller ekstrem natur, bør dere ta et formelt møte. Bli enige om en status, og dersom dere beslutter å kansellere, skriv en protokoll som sier: \"Partene sier seg løst fra avtalen i henhold til bustadoppføringslova § 60 grunnet force majeure.\"",
    ),
    "dumme_sporsmal": [
        {"q": "Hvor lenge må det vare for å være \"langvarig avbrot\"?", "a": "Loven har ingen fast grense i antall dager. Det vurderes i hvert enkelt prosjekt. En uke er for lite. Et halvt år er som oftest mer enn nok."},
        {"q": "Gjelder det hvis underleverandøren gikk konkurs?", "a": "Nei, at en bedrift går konkurs, anses å ligge innenfor entreprenørens kontrollsfære. De må bare skaffe en ny underleverandør."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "11", "tittel": "§ 11", "available": True},
        {"lov": LOV, "paragraf": "51", "tittel": "§ 51", "available": True},
        {"lov": LOV, "paragraf": "52", "tittel": "§ 52", "available": True},
    ],
},
{
    "number": "61",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Loven gjelder også for arkitekter og konsulenter",
    "description": "Du har leid inn en ingeniør eller arkitekt til å tegne huset ditt. Loven beskytter deg også når planleggerne gjør grove feil.",
    "kort_svar": "Kapittel 9 i bustadoppføringsloven gjelder når du leier inn en uavhengig profesjonell konsulent (for eksempel en arkitekt eller ingeniør) til å tegne eller planlegge huset før snekkerne begynner å bygge.",
    "paragraftekst": "Føresegnene i dette kapitlet gjeld konsulentavtalar med forbrukar. Med konsulentavtale er det meint ein avtale mellom ein sjølvstendig oppdragstakar (konsulenten) og ein oppdragsgjevar (forbrukaren) om planlegging av oppføring av bygning til bustadføremål.",
    "hva_betyr_html": _p(
        "Hittil har vi snakket mye om entreprenøren (snekkerne, graverne). Men veldig ofte hyrer du en arkitekt for å tegne huset først. Arkitekten slår ikke inn en eneste spiker, men de leverer tegningene og beregningene som huset hviler på.",
        "Paragraf 61 drar disse planleggerne, konsulentene og arkitektene inn under lovens beskyttende paraply.",
        "Vilkårene er de samme som for selve byggingen: Det må gjelde planlegging av en bolig eller hytte, du må være privatperson (forbruker), og arkitekten må drive med dette som en profesjonell næring.",
        "At loven gjelder, betyr at du som forbruker har strenge, ufravikelige rettigheter hvis arkitekten tegner trappa i feil etasje, eller glemmer å tegne inn bæreveggen slik at taket klapper sammen.",
    ),
    "eksempler": [
        {"navn": "Marius", "tekst": "Marius vil bygge drømmehuset sitt på en skrå tomt. Han leier inn det uavhengige firmaet \"Topp Arkitekter AS\" for å tegne huset og beregne hvor tykk grunnmuren må være. Firmaet fakturerer ham for 150 000 kroner. Da snekkeren (som Marius har hyret separat) begynner å bygge ut fra tegningene, viser det seg at takvinkelen er regnet feil. Tegne-avtalen med \"Topp Arkitekter AS\" styres av reglene i lovens kapittel 9."},
    ],
    "vanlige_feil": [
        "Å tro at arkitekter ikke kan holdes ansvarlige for feil fordi de \"bare lager papirer\".",
        "Å la naboen (som tegner litt på si som hobby) lage de tekniske tegningene.",
    ],
    "hva_bor_du_html": _p(
        "Be om kontrakt med arkitekten før de starter tegnearbeidet. Sjekk at de har en ansvarsforsikring. Prosjekteringsfeil er noe av det aller dyreste å rette opp i når huset først står der.",
    ),
    "dumme_sporsmal": [
        {"q": "Jeg leide inn et firma som hjalp meg med å fylle ut selve bygge-søknad-skjemaet til kommunen. Gjelder loven?", "a": "Ja. Utfylling av byggesøknad for bygning til boligformål inngår i begrepet \"planlegging\". Gjør de en tabbe slik at du får millionbøter fra kommunen, fanger paragraf 61 dem i garnet."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "62", "tittel": "§ 62", "available": True},
        {"lov": LOV, "paragraf": "63", "tittel": "§ 63", "available": True},
        {"lov": LOV, "paragraf": "1", "tittel": "§ 1", "available": True},
    ],
},
{
    "number": "62",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Arkitekten kan ikke nekte ansvar",
    "description": "Står det med liten skrift i kontrakten at arkitekten ikke betaler erstatning hvis de regner feil? Glem det. Denne regelen er ugyldig.",
    "kort_svar": "En konsulent, ingeniør eller arkitekt har forbud mot å putte vilkår inn i kontrakten som fjerner deres ansvar for feil og tabber de gjør i planleggingen av huset ditt.",
    "paragraftekst": "Konsulenten kan ikkje fråskrive seg skadebotansvar som han eller ho har etter allmenne reglar på grunn av feil.",
    "hva_betyr_html": _p(
        "Feil i byggetegninger koster ofte ufattelig mye penger å reparere i virkeligheten. En arkitekt som glemmer å tegne inn et rør-sjakt gjennom to etasjer, kan tvinge snekkeren til å rive hele badet og bygge det på nytt når rørene endelig skal på plass.",
        "Mange arkitekt- og konsulentfirmaer har i sine standardkontrakter klausuler som: \"Vårt maksimale erstatningsansvar er begrenset til honoraret for oppdraget\". Det ville betydd at hvis du betalte dem 50 000 kr, ville de aldri måtte betale mer enn 50 000 kr, selv om feilen deres kostet deg 500 000 kr.",
        "Paragraf 62 gjør dette klinkende klart: Ulovlig. Konsulenten har absolutt forbud mot å fraskrive seg, eller redusere, det erstatningsansvaret de har etter \"alminnelige regler\".",
    ),
    "eksempler": [
        {"navn": "Eva", "tekst": "Eva leier inn \"Sol-Arkitekter AS\" for å tegne påbygget til huset sitt. I kontrakten står det: \"Selskapet fraskriver seg ethvert erstatningsansvar for prosjekteringsfeil oppdaget etter byggeperiodens slutt\". Snekkeren bygger etter tegningen. Et år etter innflytting knekker bærekonstruksjonen i taket, fordi snølasten var beregnet feil av arkitekten. Eva krever 400 000 kr i erstatning. Sol-Arkitekter viser til kontrakten. Takket være § 62 kan Eva se bort ifra denne kontraktslinjen."},
    ],
    "vanlige_feil": [
        "Å ikke ta en konflikt med arkitekten fordi de viser til en klausul om \"ansvarsbegrensning\" i kontrakten.",
        "At entreprenøren du engasjerer sier: \"Det var arkitekten din som tegnet feil, du må betale oss for å rive veggen.\"",
    ],
    "hva_bor_du_html": _p(
        "Dersom entreprenøren oppdager en grov feil i tegningene på byggeplassen, krev at det sendes et såkalt \"avviksvarsel\" umiddelbart. Kontakt arkitekten og si at de må komme opp med en ny løsning straks.",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg erstatning hvis tegningen bare ble stygg, og ikke slik jeg egentlig ville ha den?", "a": "Estetikk er en vanskelig sak. Du får sjelden erstatning bare fordi huset føles upraktisk hvis de har holdt seg til teknisk standard."},
        {"q": "Hva om arkitekten skylder på konsulenten han hyret inn til å regne på rørene?", "a": "Du har kontrakt med hovedarkitekten. Du sender hele kravet til arkitekten."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "61", "tittel": "§ 61", "available": True},
        {"lov": LOV, "paragraf": "63", "tittel": "§ 63", "available": True},
        {"lov": LOV, "paragraf": "3", "tittel": "§ 3", "available": True},
    ],
},
{
    "number": "63",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Tidsfrist for å klage på arkitekt",
    "description": "Du har også en femårsfrist på deg for å avsløre feil i arkitekttegningene. Sender du klagen for sent, slipper de unna.",
    "kort_svar": "Du har en absolutt grense på fem år fra bygget er ferdig til å klage på tabber gjort av arkitekten eller bygningsingeniøren. Du må også klage innen rimelig tid (ca. to måneder) etter at du oppdaget feilen.",
    "paragraftekst": "Forbrukaren mistar retten til å krevje skadebot på grunn av feil dersom det ikkje er gjeve melding til konsulenten om kravet innan rimeleg tid etter at forbrukaren oppdaga eller burde ha oppdaga feilen. Kravet kan ikkje meldast seinare enn fem år etter overtakinga av den ytinga som oppdraget knyter seg til.",
    "hva_betyr_html": _p(
        "Paragraf 63 gjør nøyaktig det samme for arkitekter (konsulenter) som paragraf 30 gjør for snekkere (entreprenører). Den setter strenge frister.",
        "For at arkitekter ikke skal bli saksøkt i evig tid for hus de tegnet på 80-tallet, stenges døren fem år etter at du har overtatt huset. Går det 5 år og én dag før du merker at vinduene de tegnet inn var for store for bæringen, mister du alle rettigheter til å få penger fra dem.",
        "Du har også en kortere frist. Så snart du, eller snekkeren din, oppdager en feil i tegningen, må du gi arkitekten beskjed \"innen rimelig tid\". Domstolene i Norge pleier å sette denne grensen ved omtrent to måneder.",
        "Siste ledd er den klassiske nødventilen: Har konsulenten forfalsket beregningene sine med viten og vilje, eller vært grovt uaktsom, kan de ikke gjemme seg bak femårsfristen.",
    ),
    "eksempler": [
        {"navn": "Kari", "tekst": "Kari engasjerte \"Rask Strek AS\" som ansvarlig søker og arkitekt for eneboligen sin. Tegningene ble levert i 2023. Huset sto ferdig og Kari fikk nøkkelen 1. oktober 2024. Høsten fire år senere oppdager hun fuktskader fordi arkitekten glemte å tegne inn nødvendig fuktsikring for kjelleren. Siden det bare har gått fire år siden 1. oktober 2024, er hun godt innenfor den absolutte 5-årsfristen."},
    ],
    "vanlige_feil": [
        "Å sende klagen til snekkerfirmaet, og tro at de fikser problemet med din uavhengige arkitekt for deg.",
        "Å glemme å ta tak i saken fordi huset ennå ikke er ferdigbygget, selv om snekkeren avdekket arkitektfeilen i fjor.",
    ],
    "hva_bor_du_html": _p(
        "Dersom håndverkeren stanser opp og sier \"Det er en krasj i tegningene her, rørene kan ikke gå der arkitekten har tegnet dem\", send en e-post med én gang: \"Til arkitekt. Tømreren har påpekt en prosjekteringsfeil. Jeg gir herved formell melding om at dette utgjør en feil (reklamasjon etter § 63).\"",
    ),
    "dumme_sporsmal": [
        {"q": "Får jeg snekker-regningen for feilen dekket automatisk?", "a": "Du må kreve det skriftlig som skadebot (erstatning). Det er dette § 63 gjelder – selve varselet om at du kommer til å kreve utlegget."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "61", "tittel": "§ 61", "available": True},
        {"lov": LOV, "paragraf": "62", "tittel": "§ 62", "available": True},
        {"lov": LOV, "paragraf": "30", "tittel": "§ 30", "available": True},
    ],
},
{
    "number": "64",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Gratis og rask hjelp mot utbygger",
    "description": "Du trenger ikke hyre en dyr advokat og gå i tingretten for å krangle om vinduet. Loven har etablert en egen gratisløsning for slike konflikter.",
    "kort_svar": "Hvis du og entreprenøren blir uenige om penger, feil eller forsinkelser, kan saken meldes inn til en offisiell nemnd for boligtvister (som Boligtvistnemnda). Mens saken ligger til behandling der, har entreprenøren forbud mot å trekke deg for domstolen.",
    "paragraftekst": "Dersom det på grunnlag av avtale mellom entreprenørane eller konsulentane sine organisasjonar og Forbrukarrådet er skipa ei nemnd for tvistar om avtalar som går inn under lova her, og som er godkjend etter godkjenningslova, kan kvar av partane leggje fram for nemnda ein tvist der nemnda er kompetent. Så lenge tvisten er til førehaving i nemnda, kan ikkje entreprenøren reise søksmål om same tvisteemnet.",
    "hva_betyr_html": _p(
        "En konflikt med en entreprenør om et skjevt tak kan fort koste hundretusener av kroner i advokatutgifter hvis saken går til tingretten. Loven har derfor godkjent en enklere, raskere og nesten gratis utvei.",
        "\"Nemnd for tvistar\" refererer i dag vanligvis til Boligtvistnemnda. Dette er uavhengige organer hvor eksperter sitter rundt et bord og avgjør hvem av dere som har rett, basert på papirer, e-poster og takstrapporter.",
        "Det viktigste her er siste setning. Entreprenører liker ofte å skremme forbrukere ved å si: \"Betaler du ikke de siste 100 000 kronene, sender jeg advokaten min på deg.\" Paragraf 64 er ditt skjold. Hvis du sender saken inn til Boligtvistnemnda, fryses prosessen. Entreprenøren har bokstavelig talt forbud mot å dra deg i tingretten så lenge saken behandles av nemnda.",
    ),
    "eksempler": [
        {"navn": "Jonas", "tekst": "Jonas og snekkeren krangler om en regning. Jonas holder tilbake 50 000 kroner for en feilmontert trapp. Snekkeren sender et brev fra et dyrt advokatfirma med trussel om stevning til forliksrådet og tingretten hvis Jonas ikke betaler i morgen. Jonas går inn på nettsidene til Boligtvistnemnda og registrerer klagen sin der. Han sender kvitteringen for saken til snekkerens advokat. Advokaten må da pent lukke saken sin midlertidig."},
    ],
    "vanlige_feil": [
        "Å bli skremt av advokatbrev til å betale for en byggefeil man åpenbart ikke burde betale for.",
        "Å tro at nemndas avgjørelse ikke gjelder for noe.",
        "Mangle dokumentasjon. Nemnda kommer ikke hjem til deg for å se på trappen.",
    ],
    "hva_bor_du_html": _p(
        "Står saken bom fast, og entreprenøren nekter å gi deg prisavslag eller rette mangelen: Sjekk om entreprenøren din er medlem av Boligprodusentenes Forening eller lignende. Melder du saken inn til Boligtvistnemnda, skjer hele saksbehandlingen skriftlig.",
    ),
    "dumme_sporsmal": [
        {"q": "Hva koster det å bruke en slik nemnd?", "a": "Det er normalt helt gratis eller innebærer bare et veldig lite saksgebyr for privatpersoner."},
        {"q": "Kan jeg reise søksmål mot snekkeren mens nemnda ser på saken?", "a": "Ja. Loven sier \"kan ikkje entreprenøren reise søksmål\". Forbrukeren har teknisk sett lov, men det gir sjelden mening."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "31", "tittel": "§ 31", "available": True},
        {"lov": LOV, "paragraf": "29", "tittel": "§ 29", "available": True},
    ],
},
{
    "number": "65",
    "lov": LOV, "lov_display": LOV_DISPLAY, "kategori": KAT,
    "title": "Når loven gjelder fra",
    "description": "Kjøpte du hus på 90-tallet? Bustadoppføringsloven beskytter alle byggekontrakter som ble inngått etter sommeren 1998.",
    "kort_svar": "Bustadoppføringslova er gjeldende lov for avtaler om å bygge bolig. Den ble satt i kraft 1. juli 1998 og har tilbakevirkende kraft kun for tekniske foreldelsesregler.",
    "paragraftekst": "§ 65: Endringar i andre lover. § 66: Lova gjeld frå den tid Kongen fastset. Lova får berre verknad for avtalar som blir gjorde etter at ho tek til å gjelde. Frå 1. juli 1998 iflg. res. 3 okt 1997 nr. 1072.",
    "hva_betyr_html": _p(
        "De to siste paragrafene er rene administrative formaliteter. Paragraf 65 inneholdt tekniske oppdateringer i andre lovbøker. Paragraf 66 bestemte når loven trådte i kraft. Knappen ble trykket på 1. juli 1998.",
        "Loven gjelder alle byggekontrakter du inngår i dag. Eneste viktig: Den gjelder ikke bakover i tid for selve byggingen. Men dette har liten betydning – alle 5-årsfrister på hus fra 90-tallet er uansett utløpt.",
    ),
    "eksempler": [
        {"navn": "Kari", "tekst": "Kari skal kjøpe rehabilitert hus. Byggebedriften sier de bygger etter \"gamle regler fra før loven kom\". Kari ser i § 66 at loven gjelder alle avtaler etter 1998. Hun krever kontrakt som refererer til dagens bustadoppføringslov."},
    ],
    "vanlige_feil": [
        "Ingen vanlige forbrukerfeil. Loven er inngrodd i bransjen. Alt som bygges nytt i dag, omfattes.",
    ],
    "dumme_sporsmal": [
        {"q": "Endrer loven seg aldri?", "a": "Jo. Stortinget har lagt inn mange nye paragrafer senere (som § 1a, § 1b, § 6a). Avtalen du signerer i dag styres av sist oppdaterte regler."},
    ],
    "related": [
        {"lov": LOV, "paragraf": "1", "tittel": "§ 1", "available": True},
        {"lov": LOV, "paragraf": "4", "tittel": "§ 4", "available": True},
    ],
},

]
