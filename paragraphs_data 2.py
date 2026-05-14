"""Rettsregel paragraf-innhold. Importeres av build.py."""

PARAGRAPHS = [{'number': '1',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Hvilke kjøp loven gjelder for',
  'description': 'Hvilke kjøp dekkes av angrerettloven? Loven gjelder netthandel og kjøp utenom butikk – her er '
                 'reglene for når du har angrerett som forbruker.',
  'kort_svar': 'Angrerettloven gjelder når du som vanlig forbruker kjøper noe av en bedrift, og du enten kjøpte det på '
               'nett, over telefon, eller utenfor butikken deres — for eksempel hjemme hos deg selv eller på et stand. '
               'Da har du som hovedregel rett til å angre kjøpet.',
  'paragraftekst': 'Loven gjelder ved salg av varer og tjenester til forbruker når den næringsdrivende opptrer i '
                   'næringsvirksomhet, forbrukeren betaler eller påtar seg å betale en pris, og avtalen inngås ved '
                   'fjernsalg eller salg utenom faste forretningslokaler. Loven gjelder også der forbrukeren gir fra '
                   'seg eller påtar å gi fra seg personopplysninger til den næringsdrivende. Annet punktum gjelder '
                   'likevel ikke dersom personopplysningene utelukkende behandles av den næringsdrivende for å levere '
                   'varen, det digitale innholdet som ikke leveres på et fysisk medium eller den digitale tjenesten '
                   'eller for å overholde lovpålagte plikter, og den næringsdrivende ikke behandler disse '
                   'opplysningene til noe annet formål.\n'
                   '\n'
                   'Lovens kapittel 2 til 5 og §§ 28 og 29 gjelder også den som i næringsvirksomhet opptrer på vegne '
                   'av en ikke-næringsdrivende selger eller tjenesteyter i situasjoner som nevnt i første ledd.\n'
                   '\n'
                   'Loven gjelder for Svalbard og Jan Mayen. Departementet kan likevel i forskrift bestemme at hele '
                   'eller deler av loven ikke skal gjelde, og gi særlige regler av hensyn til de stedlige forhold.',
  'hva_betyr_html': '<p>§ 1 sier hvilke kjøp loven gjelder for. Fire vilkår må være på plass:</p>\n'
                    '<ol>\n'
                    '<li><strong>Du må være forbruker.</strong> Du kjøper noe som privatperson, ikke for firmaet '
                    'ditt.</li>\n'
                    '<li><strong>Selgeren må være næringsdrivende.</strong> Det er en bedrift, ikke en privatperson '
                    'som selger en gammel sofa på Finn.</li>\n'
                    '<li><strong>Du må betale noe.</strong> Enten penger, eller personopplysninger som selgeren bruker '
                    'til markedsføring eller annet. Hvis selgeren bare bruker opplysningene dine til å levere selve '
                    'varen, regnes det ikke som "betaling".</li>\n'
                    '<li><strong>Kjøpet må skje på avstand eller utenfor butikken.</strong> Det betyr på nett, over '
                    'telefon, på e-post, hjemme hos deg, på et stand på kjøpesenteret, eller lignende. Når du går inn '
                    'i en vanlig butikk og kjøper noe over disk, gjelder ikke angrerettloven.</li>\n'
                    '</ol>\n'
                    '<p>Tredje ledd sier at loven også gjelder på Svalbard og Jan Mayen.</p>',
  'eksempler': [{'navn': 'Anne',
                 'tekst': 'Anne kjøper et par sko på Zalando for 1 200 kr. Hun betaler med Vipps. Dette er klassisk '
                          'fjernsalg — hun har ikke møtt selgeren fysisk. Alle fire vilkår er oppfylt: hun er '
                          'forbruker, Zalando er en bedrift, hun betaler 1 200 kr, og hun handlet på nett. '
                          'Angrerettloven gjelder, og hun kan angre i 14 dager etter at hun mottar skoene.'},
                {'navn': 'Lars',
                 'tekst': 'Lars sitter hjemme da en selger fra et solenergifirma ringer på døra. Selgeren overtaler '
                          'ham til å bestille solcellepaneler for 80 000 kr. Lars signerer på et nettbrett ved '
                          'kjøkkenbordet. Dette er salg utenom faste forretningslokaler — selgeren kom hjem til ham. '
                          'Lars har 14 dagers angrerett. Hadde han derimot gått inn i firmaets butikk og signert der, '
                          'ville loven ikke gjeldt.'}],
  'vanlige_feil': ['Du tror angrerett gjelder kjøp i fysisk butikk. Det gjør den ikke. Går du inn i en H&M og kjøper '
                   'en genser, finnes det ingen lovbestemt angrerett. Eventuelle byttemuligheter er bare butikkens '
                   'eget tilbud.',
                   'Du tror angrerett gjelder kjøp fra privatpersoner. Kjøper du noe på Finn fra en privatperson, '
                   'gjelder ikke angrerettloven. Kjøper du fra en næringsdrivende på Finn, gjelder den.',
                   'Du tror at "gratis" prøveperioder med dine personopplysninger er gratis. Hvis selgeren bruker '
                   'opplysningene dine til markedsføring eller salg, regnes det som betaling — og loven gjelder fullt '
                   'ut.'],
  'hva_bor_du_html': '<p>Når du handler, spør deg selv: kjøpte jeg dette på nett, over telefon, eller utenfor '
                     'butikkens lokaler? Og kjøpte jeg det av en bedrift? Hvis svaret er ja på begge, har du '
                     'sannsynligvis angrerett. Sjekk de neste paragrafene for hvor lang fristen er og hvordan du går '
                     'frem.</p>',
  'dumme_sporsmal': [{'q': 'Gjelder angrerettloven hvis jeg kjøper noe på Vinmonopolets nettside?',
                      'a': 'Ja. Vinmonopolet er en bedrift, og du handler på nett. Angrerett gjelder.'},
                     {'q': 'Hva med kjøp på Facebook Marketplace?',
                      'a': 'Det kommer an på hvem selgeren er. Er det en privatperson som selger en brukt sykkel, '
                           'gjelder ikke loven. Er det et firma som selger nye varer, gjelder den.'}],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '2',
               'tittel': 'Hvilke kjøp som likevel faller utenfor',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '5',
               'tittel': 'Definisjoner av "forbruker", "fjernsalg" og lignende',
               'available': True},
              {'lov': 'angrerettloven', 'paragraf': '20', 'tittel': 'Slik bruker du angreretten', 'available': True},
              {'lov': 'angrerettloven', 'paragraf': '21', 'tittel': 'Angrefristen på 14 dager', 'available': True}]},
 {'number': '2',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Når loven likevel ikke gjelder',
  'description': 'Når gjelder ikke angrerettloven? Listen over kjøp som faller utenfor – bolig, pakkereiser, små beløp '
                 'og andre viktige unntak forklart enkelt.',
  'kort_svar': 'Selv om du har handlet på nett eller utenfor butikk, har du ikke alltid angrerett. Loven har ti unntak '
               '— blant annet kjøp av bolig, pakkereiser, togbilletter, forsikring, kjøp under 300 kr på stand, og '
               'pengespill.',
  'paragraftekst': 'Loven gjelder ikke for:\n'
                   'a. avtaler om salg av varer og tjenester fra salgsautomater og automatiserte forretningslokaler,\n'
                   'b. avtaler om salg eller oppføring av fast eiendom og avtaler som gjelder rettigheter i fast '
                   'eiendom, med unntak av utleie. Som salg av fast eiendom regnes også salg av adkomstdokumenter med '
                   'tilknyttet leierett eller borett i bolig,\n'
                   'c. avtaler som omfattes av lov om avtaler om deltidsbruksrett og langtidsferieprodukter mv. '
                   '(tidspartloven),\n'
                   'd. avtaler om pakkereiser, jf. pakkereiseloven § 6,\n'
                   'e. avtaler om persontransporttjenester. Kravene i § 16 får likevel anvendelse,\n'
                   'f. avtaler som omfattes av finansavtaleloven og forsikringsavtaleloven,\n'
                   'g. avtaler om salg av varer og tjenester utenom faste forretningslokaler når den samlede '
                   'kontraktssummen, inkludert frakt- og tilleggskostnader som forbrukeren skal betale, er 300 kr '
                   'eller mindre,\n'
                   'h. avtaler som er inngått med ekomtilbyder gjennom offentlig tilgjengelige betalingstelefoner for '
                   'bruk av disse, eller som er inngått for bruk av én enkelt telefon-, Internett- eller '
                   'telefaksforbindelse opprettet av en forbruker,\n'
                   'i. avtaler om pengespill,\n'
                   'j. avtaler om salg av varer som selges på tvangsauksjon eller på annen måte tvangsmessig i henhold '
                   'til lov.',
  'hva_betyr_html': '<p>§ 2 lister opp ti typer kjøp som er unntatt fra angrerettloven. Du har altså ingen lovbestemt '
                    'angrerett — selv om kjøpet skjedde på nett eller utenfor butikk. La oss gå gjennom dem:</p>\n'
                    '<p><strong>a) Salgsautomater og automatiserte butikker.</strong> Kjøper du en Coca-Cola fra en '
                    'automat, eller handler i en ubemannet 24/7-butikk, gjelder ikke loven.</p>\n'
                    '<p><strong>b) Fast eiendom.</strong> Kjøp av hus, hytte og leilighet er unntatt. Det gjelder også '
                    'borett og leierett i borettslag (de såkalte "adkomstdokumentene"). Vanlig utleie er likevel ikke '
                    'unntatt.</p>\n'
                    '<p><strong>c) Tidsparter og langtidsferieprodukter.</strong> Dette er den litt foreldede ideen om '
                    '"tidspart" i en feriebolig. Disse dekkes av tidspartloven, som har sine egne regler.</p>\n'
                    '<p><strong>d) Pakkereiser.</strong> Reiser som omfatter for eksempel både fly og hotell, og som '
                    'er solgt samlet som en pakke, har egne regler i pakkereiseloven.</p>\n'
                    '<p><strong>e) Persontransport.</strong> Tog-, fly-, buss- og fergebilletter er unntatt. Men noen '
                    'opplysningsplikter (etter § 16) gjelder fortsatt.</p>\n'
                    '<p><strong>f) Finansielle tjenester.</strong> Lån, banktjenester, kreditt, forsikring og '
                    'betalingstjenester følger finansavtaleloven eller forsikringsavtaleloven i stedet. De har egne, '
                    'og ofte bedre, angrerettregler.</p>\n'
                    '<p><strong>g) Småkjøp under 300 kr utenfor butikk.</strong> Hvis en selger kommer hjem til deg '
                    'eller på et stand, og hele kjøpet (inkludert frakt) er på 300 kr eller mindre, gjelder ikke '
                    'loven.</p>\n'
                    '<p><strong>h) Bruk av betalingstelefon og enkeltforbindelser.</strong> Veldig sjelden i praksis. '
                    'Gjelder for eksempel hvis du ringer fra en offentlig betalingstelefon og betaler for '
                    'samtalen.</p>\n'
                    '<p><strong>i) Pengespill.</strong> Tipping, Lotto, Eurojackpot og lignende.</p>\n'
                    '<p><strong>j) Tvangsauksjoner.</strong> Varer solgt på tvangsauksjon, for eksempel når noen '
                    'mister tingene sine til namsmannen.</p>',
  'eksempler': [{'navn': 'Petter',
                 'tekst': 'Petter forelsker seg i en hytte han ser på Finn. Megleren sender ham budskjema, og han byr '
                          '3,2 millioner kroner over e-post. Han får tilslaget. Etter to dager angrer han og lurer på '
                          'om han kan trekke seg. Det kan han ikke. Kjøp av fast eiendom er unntatt etter § 2 bokstav '
                          'b. Selv om hele prosessen foregikk digitalt, gjelder ikke angrerettloven. Petter må holde '
                          'det han har lovet — eller forhandle med selgeren.'},
                {'navn': 'Sara',
                 'tekst': 'Sara bestiller en charterreise til Hellas på nett — fly og hotell i én pakke for 18 000 kr. '
                          'Hun angrer dagen etter. Hun har ikke angrerett etter angrerettloven, fordi pakkereiser er '
                          'unntatt etter bokstav d. Hun må sjekke pakkereiseloven og vilkårene til reisearrangøren.'}],
  'vanlige_feil': ['Du tror "alle kjøp på nett" har angrerett. Det stemmer ikke. Pakkereiser, togbilletter, forsikring '
                   'og hyttekjøp har det ikke — selv om kjøpet skjedde på nett.',
                   'Du tror "300 kr-regelen" gjelder ved netthandel. Det gjør den ikke. Unntaket gjelder bare for kjøp '
                   'utenfor faste forretningslokaler — altså hjemmebesøk og stand. På nett har du angrerett uansett '
                   'pris.',
                   'Du forveksler unntak fra angrerettloven med "ingen rettigheter". Selv om angrerettloven ikke '
                   'gjelder, har du fortsatt rettigheter etter andre lover — for eksempel finansavtaleloven (lån) '
                   'eller forsikringsavtaleloven (forsikring), som ofte gir egne angrefrister.'],
  'hva_bor_du_html': '<p>Før du kjøper noe på nett eller utenfor butikk: sjekk om varen din står på unntakslisten. '
                     'Hvis den gjør det, må du finne hvilken annen lov som gjelder. For reiser: pakkereiseloven. For '
                     'forsikring og lån: finansavtaleloven eller forsikringsavtaleloven. For pengespill: ingen '
                     'angrerett i det hele tatt.</p>',
  'dumme_sporsmal': [{'q': 'Har jeg angrerett på en flybillett jeg bestilte på nett?',
                      'a': 'Nei. Persontransport er unntatt etter § 2 bokstav e. Du må sjekke flyselskapets egne '
                           'regler — noen tilbyr 24 timers angrefrist frivillig.'},
                     {'q': 'Har jeg angrerett på en forsikring jeg tegnet på nett?',
                      'a': 'Ikke etter angrerettloven, men ofte etter forsikringsavtaleloven, som gir 14 dagers '
                           'angrefrist for de fleste forbrukerforsikringer.'}],
  'related': [{'lov': 'angrerettloven', 'paragraf': '1', 'tittel': 'Hvilke kjøp loven gjelder for', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '22',
               'tittel': 'Unntak fra angreretten ved bestemte varer',
               'available': True},
              {'lov': 'pakkereiseloven', 'paragraf': '6', 'tittel': 'Regler for pakkereiser', 'available': False},
              {'lov': 'finansavtaleloven',
               'paragraf': '1',
               'tittel': 'Lån, kreditt og betalingstjenester',
               'available': False}]},
 {'number': '3',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Selgeren kan ikke ta fra deg rettighetene dine',
  'description': 'Selgeren kan ikke ta fra deg angreretten ved å skrive det i vilkårene. § 3 sikrer rettighetene dine '
                 'uansett hva som står i avtalen du signerte.',
  'kort_svar': 'Selv om selgeren har skrevet "ingen angrerett" i vilkårene eller fått deg til å huke av en boks, har '
               'du fortsatt alle rettighetene loven gir deg. Angrerettloven kan ikke fravikes til ulempe for deg som '
               'forbruker.',
  'paragraftekst': 'Loven kan ikke fravikes ved avtale til ulempe for en forbruker.',
  'hva_betyr_html': '<p>Dette er et viktig prinsipp som juristene kaller "preseptorisk". På norsk betyr det at loven '
                    'står sterkere enn avtalen. Selgeren kan ikke fjerne rettighetene dine ved å skrive noe annet i '
                    'vilkårene.</p>\n'
                    '<p>Med andre ord: selv om du har klikket på "Jeg godtar vilkårene", og selgerens vilkår sier "Det '
                    'gis ikke angrerett på dette produktet", har du angrerett likevel — så lenge angrerettloven '
                    'gjelder for kjøpet ditt.</p>\n'
                    '<p>Men loven kan brukes til din fordel. Hvis selgeren gir deg bedre vilkår enn loven krever — for '
                    'eksempel 30 dagers angrerett istedenfor 14 — er det selvsagt helt greit. Det er bare regler til '
                    'ulempe for deg som er ugyldige.</p>',
  'eksempler': [{'navn': 'Eva',
                 'tekst': 'Eva kjøper en kaffemaskin fra en nettbutikk for 4 500 kr. I selgerens vilkår står det: "Ved '
                          'kjøp av elektronikk gis det ingen angrerett." Det stemmer ikke. Vilkåret er ugyldig etter § '
                          '3. Eva har fortsatt sin lovbestemte angrerett på 14 dager. Hun sender en angremelding, '
                          'returnerer maskinen, og får tilbake pengene sine. Selgerens vilkår spiller ingen rolle.'}],
  'vanlige_feil': ['Du tror "vilkår er vilkår". Det er de ikke når de strider mot forbrukerlovgivningen. Loven slår '
                   'alltid avtalen — så lenge avtalen er til ulempe for deg.',
                   'Du tror at fordi du huket av "jeg godtar", er du bundet. Du er bundet av det som er gyldig. '
                   'Ugyldige vilkår er ikke bindende, uansett hvor mange ganger du klikket "ja".',
                   'Du forveksler dette med at all angrerett er ufravikelig. Lovens egne unntak gjelder fortsatt — for '
                   'eksempel for spesiallagde varer (§ 22). Det selgeren ikke kan gjøre, er å innskrenke rettighetene '
                   'loven gir deg.'],
  'hva_bor_du_html': '<p>Hvis en selger nekter å godta angreretten din med henvisning til sine egne vilkår, vis dem '
                     'til § 3. Hvis de ikke gir seg, kan du klage til Forbrukerrådet og eventuelt Forbrukertilsynet. '
                     'Du står på trygg grunn — loven er på din side.</p>',
  'dumme_sporsmal': [{'q': 'Hva om jeg har signert på et papir der det står at jeg ikke har angrerett?',
                      'a': 'Da har du fortsatt angrerett. § 3 sier at slike vilkår er ugyldige, uansett om de står på '
                           'papir eller på nett, og uansett om du har signert eller huket av.'},
                     {'q': 'Kan selgeren ta betalt et "gebyr" for å bruke angreretten?',
                      'a': 'Nei, ikke for selve det å angre. Selgeren kan kreve at du betaler returkostnadene (frakt '
                           'tilbake), men bare hvis det er opplyst om dette på forhånd. Et eget "angregebyr" på toppen '
                           'er ugyldig.'}],
  'related': [{'lov': 'angrerettloven', 'paragraf': '1', 'tittel': 'Hvilke kjøp loven gjelder for', 'available': True},
              {'lov': 'angrerettloven', 'paragraf': '20', 'tittel': 'Slik bruker du angreretten', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '22',
               'tittel': 'De spesifikke unntakene som er lovlige',
               'available': True}]},
 {'number': '4',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Andre rettigheter gjelder ved siden av',
  'description': 'Angrerettloven utelukker ikke andre rettigheter du har. Forbrukerkjøpsloven, garantier og '
                 'reklamasjonsregler gjelder ved siden av angreretten.',
  'kort_svar': 'Angrerettloven kommer i tillegg til andre rettigheter du har. Den fjerner ikke garantien, '
               'reklamasjonsretten eller reglene i forbrukerkjøpsloven. Du kan bruke alle rettighetene du har, etter '
               'behov.',
  'paragraftekst': 'Loven medfører ingen begrensninger i opplysningsplikt eller krav til avtalen som følger av andre '
                   'regler.',
  'hva_betyr_html': '<p>§ 4 sier at angrerettloven ikke står alene. Hvis en annen lov gir deg flere opplysninger eller '
                    'bedre rettigheter, gjelder de fortsatt.</p>\n'
                    '<p>De viktigste tilleggsreglene du bør kjenne til:</p>\n'
                    '<p><strong>Forbrukerkjøpsloven</strong> gir deg rett til å reklamere på feil og mangler i varen. '
                    'Du har normalt to års reklamasjonsfrist, eller fem år på varer som er ment å vare lenge (som '
                    'hvitevarer og møbler). Dette gjelder helt uavhengig av om du har angrerett.</p>\n'
                    '<p><strong>Markedsføringsloven</strong> har regler om villedende reklame, urimelig '
                    'forretningspraksis og uoppfordret telefonsalg.</p>\n'
                    '<p><strong>Garantier fra selgeren</strong> kommer i tillegg til loven. Selgeren kan aldri gi deg '
                    'dårligere vilkår enn loven krever, men kan gi deg bedre.</p>\n'
                    '<p>Praktisk betyr dette: du må ikke velge mellom angrerett og reklamasjonsrett. Du har begge '
                    'deler.</p>',
  'eksempler': [{'navn': 'Tom',
                 'tekst': 'Tom kjøper en designerlampe på nett for 3 200 kr. Når han pakker opp pakken, ser han at '
                          'lampen har en ripe. Han har to muligheter: (1) Bruke angreretten innen 14 dager og sende '
                          'lampen tilbake fordi han ikke vil ha den. (2) Reklamere på mangelen etter '
                          'forbrukerkjøpsloven og kreve at selgeren retter feilen, eller gir ham en ny. § 4 sier at '
                          'begge mulighetene er åpne. Han velger det som passer ham best.'}],
  'vanlige_feil': ['Du tror angrefristen er den eneste tidsfristen. Det er den ikke. Selv etter at angrefristen er '
                   'ute, har du fortsatt reklamasjonsrett i to eller fem år hvis varen har en mangel.',
                   'Du tror du må velge en lov og holde deg til den. Du må ikke det. Du kan kombinere rettighetene — '
                   'for eksempel reklamere på en mangel selv om angrefristen har gått ut.',
                   'Du tror en "garanti" fra selgeren er en gave. Den er den ofte ikke. Garantien må gi deg noe mer '
                   'enn det loven allerede gir. Hvis ikke, har den ingen reell verdi.'],
  'hva_bor_du_html': '<p>Når noe går galt med et kjøp, ikke begrens deg til angreretten. Sjekk om du har en mangelsak '
                     '(forbrukerkjøpsloven), om markedsføringen var villedende (markedsføringsloven), eller om '
                     'selgeren har gitt en garanti utover loven. Du står ofte bedre rustet enn du tror.</p>',
  'dumme_sporsmal': [{'q': 'Hva er forskjellen på angrerett og reklamasjon?',
                      'a': 'Angrerett betyr at du kan ombestemme deg uten å forklare hvorfor, innen 14 dager. '
                           'Reklamasjon betyr at du klager på en feil eller mangel ved varen — og du har normalt to '
                           'eller fem år på deg.'},
                     {'q': 'Trenger jeg å si "jeg reklamerer" eller "jeg angrer"?',
                      'a': 'Bruk det ordet som passer. Angrer du fordi du ikke ville hatt varen, si "angrer". Klager '
                           'du fordi varen har en feil, si "reklamerer". Det viktigste er at det kommer tydelig frem '
                           'hva du vil.'}],
  'related': [{'lov': 'angrerettloven', 'paragraf': '1', 'tittel': 'Hvilke kjøp loven gjelder for', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '3',
               'tittel': 'Selgeren kan ikke ta fra deg rettighetene dine',
               'available': True},
              {'lov': 'forbrukerkjopsloven',
               'paragraf': '1',
               'tittel': 'Lovens virkeområde og reklamasjonsregler',
               'available': False}]},
 {'number': '5',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Definisjoner av begrepene i loven',
  'description': "Hva betyr 'fjernsalg', 'forbruker' og 'varig medium'? Definisjonene i angrerettloven § 5 forklart på "
                 'vanlig norsk med eksempler du kjenner igjen.',
  'kort_svar': '§ 5 forklarer hva ordene i loven egentlig betyr. Du er "forbruker" når du handler privat. "Fjernsalg" '
               'er nettkjøp, telefonsalg og post-/e-postkjøp. "Faste forretningslokaler" er den vanlige butikken — alt '
               'utenfor regnes som "utenfor faste forretningslokaler".',
  'paragraftekst': 'I loven menes med:\n'
                   'a. forbruker: fysisk person som ikke hovedsakelig handler som ledd i næringsvirksomhet,\n'
                   'b. fjernsalg: avtale inngått ved organisert ordning for salg eller tjenesteyting uten at den '
                   'næringsdrivende og forbrukeren er fysisk til stede samtidig, og der inngåelse av avtale skjer '
                   'utelukkende ved bruk av fjernkommunikasjonsmidler,\n'
                   'c. faste forretningslokaler: sted for detaljsalg der den næringsdrivende utøver sin faste '
                   'virksomhet, eller flyttbare forretningslokaler for detaljsalg der den næringsdrivende vanligvis '
                   'utøver sin virksomhet,\n'
                   'd. avtale inngått utenom faste forretningslokaler: avtale der forbrukeren inngår avtale eller '
                   'fremsetter tilbud i nærvær av den næringsdrivende på annet sted enn dennes faste '
                   'forretningslokaler [...]\n'
                   'e. finansiell tjeneste: banktjeneste, kredittjeneste, forsikringstjeneste, individuell '
                   'pensjonstjeneste, investeringstjeneste, eller betalingstjeneste,\n'
                   'f. varig medium: enhver innretning som gjør forbrukeren eller den næringsdrivende i stand til å '
                   'lagre opplysninger på en slik måte at opplysningene i fremtiden er tilgjengelige i uendret form,\n'
                   'g. tilknyttet avtale: avtale der forbrukeren mottar varer eller tjenester i forbindelse med en '
                   'fjernsalgsavtale eller en avtale inngått utenom faste forretningslokaler [...]\n'
                   'h. offentlig auksjon: salgsmetode der varer eller tjenester tilbys av den næringsdrivende til '
                   'forbrukere, der forbrukeren er personlig til stede [...]\n'
                   'i. digitalt innhold: data som fremstilles og leveres i digital form [...]\n'
                   'j. digital tjeneste: tjeneste som gjør det mulig for brukeren å frembringe, behandle, lagre eller '
                   'få tilgang til data i digital form [...]\n'
                   'k. nettbasert markedsplass: enhver tjeneste som bruker programvare, herunder et nettsted eller en '
                   'applikasjon, som drives av eller på vegne av en næringsdrivende [...]\n'
                   '\n'
                   '(Loven har i tillegg bokstavene l til o, om tilbyder av markedsplass, kompatibilitet, '
                   'funksjonalitet og samvirkingsevne.)',
  'hva_betyr_html': '<p>Her er de viktigste begrepene i hverdagsspråk:</p>\n'
                    '<h3>Forbruker (a)</h3>\n'
                    '<p>Det er deg som privatperson. Du handler ikke for firmaet ditt. Hvis du driver '
                    'enkeltpersonforetak og kjøper en laptop som hovedsakelig skal brukes i jobben, er du ikke '
                    'forbruker.</p>\n'
                    '<h3>Fjernsalg (b)</h3>\n'
                    '<p>Det er kjøp der du og selgeren aldri står foran hverandre. Typisk: nettbutikk, telefonsalg, '
                    'kjøp via e-post eller chat, postordresalg, og kjøp via en app. Selgeren må ha et "organisert '
                    'opplegg" for slikt salg — at en bedrift én gang per år tar imot en bestilling via e-post er ikke '
                    'nok.</p>\n'
                    '<h3>Faste forretningslokaler (c)</h3>\n'
                    '<p>Det er den vanlige butikken — der bedriften driver fra dag til dag. Det kan også være en bod '
                    'på et marked, så lenge selgeren vanligvis selger derfra. Men selgerstanden som dukker opp på Karl '
                    'Johan én lørdag i året, er ikke "faste forretningslokaler".</p>\n'
                    '<h3>Avtale inngått utenom faste forretningslokaler (d)</h3>\n'
                    '<p>Dekker tre situasjoner: salg hjemme hos deg, salg på arbeidsplassen, salg på et stand. Det '
                    'dekker også de tilfellene der selgeren tar kontakt med deg på gaten og umiddelbart får deg inn i '
                    'sin egen butikk for å signere.</p>\n'
                    '<h3>Finansiell tjeneste (e)</h3>\n'
                    '<p>Bank, lån, forsikring, pensjon, investering og betaling. Disse er unntatt fra angrerettloven '
                    '(§ 2 bokstav f).</p>\n'
                    '<h3>Varig medium (f)</h3>\n'
                    '<p>Noe der opplysninger kan lagres uten å bli endret. Eksempler: e-post, PDF, SMS, papirbrev, '
                    'USB-pinne. En vanlig nettside som kan endres av selgeren, er ikke "varig medium". Når loven '
                    'krever at selgeren skal gi deg opplysninger på "varig medium", må du altså få dem på en form du '
                    'selv kan lagre.</p>\n'
                    '<h3>Tilknyttet avtale (g)</h3>\n'
                    '<p>En avtale knyttet til hovedkjøpet. For eksempel: du kjøper en mobiltelefon på nett, og '
                    'samtidig blir du tilbudt en mobilforsikring fra et annet selskap. Forsikringen er en tilknyttet '
                    'avtale.</p>\n'
                    '<h3>Offentlig auksjon (h)</h3>\n'
                    '<p>En fysisk auksjon med en auksjonarius — som hos Blomqvist eller en kunstauksjon. Nettauksjoner '
                    'regnes ikke som "offentlig auksjon" i lovens forstand, selv om de heter auksjon.</p>\n'
                    '<h3>Digitalt innhold og digital tjeneste (i, j)</h3>\n'
                    '<p>Digitalt innhold er noe du laster ned eller kjøper én gang — en film, en e-bok, et spill. '
                    'Digital tjeneste er noe du bruker over tid — Netflix, Spotify, Microsoft 365.</p>\n'
                    '<h3>Nettbasert markedsplass (k og l)</h3>\n'
                    '<p>For eksempel Finn, Amazon, eBay og Etsy — plattformer der mange selgere selger til mange '
                    'kjøpere. "Tilbyderen" er selve plattformen.</p>',
  'eksempler': [{'navn': 'Ingrid',
                 'tekst': 'Ingrid driver et enkeltpersonforetak som frisør. Hun kjøper en sofa på Komplett.no for 12 '
                          '000 kr. Sofaen skal stå hjemme hos henne, ikke i salongen. Er hun forbruker? Ja. '
                          'Definisjonen i bokstav a sier at man er forbruker når man "ikke hovedsakelig handler som '
                          'ledd i næringsvirksomhet". Hovedformålet med sofaen er privat bruk, så hun er beskyttet av '
                          'loven. Hadde hun kjøpt en frisørstol til salongen, ville hun ikke vært forbruker — og '
                          'angrerettloven ville ikke gjeldt.'},
                {'navn': 'Marius',
                 'tekst': 'Marius går på Karl Johans gate i Oslo en sommerdag. En selger stopper ham og snakker om et '
                          'magasinabonnement. Selgeren får ham med opp på et hotell i nærheten, der han signerer en '
                          'kontrakt for 12 måneders abonnement. Er dette "utenom faste forretningslokaler"? Ja. '
                          'Selgeren tok kontakt med ham på gaten — utenfor sine faste lokaler — og tok ham deretter '
                          'med til et annet sted. Selv om kontrakten ble signert inne på et hotell, regnes hele '
                          'situasjonen som "utenfor faste forretningslokaler" etter bokstav d. Marius har 14 dagers '
                          'angrerett.'}],
  'vanlige_feil': ['Du tror "nettbutikk" og "nettbasert markedsplass" er det samme. Det er det ikke. En nettbutikk '
                   'eier varene den selger. En markedsplass kobler bare kjøpere og selgere sammen. Forskjellen '
                   'påvirker hvem som har ansvaret hvis noe går galt.',
                   'Du tror at fordi en avtale ble signert i butikken, er det ikke "utenom faste forretningslokaler". '
                   'Det stemmer ikke alltid. Hvis selgeren først tok kontakt med deg ute på gaten og tok deg med inn, '
                   'regnes det fortsatt som "utenfor".',
                   'Du tror "varig medium" betyr noe permanent som papir. Varig medium kan også være digitalt — så '
                   'lenge du kan lagre det selv. E-post er varig medium. En nettside som selgeren kan endre, er det '
                   'ikke.'],
  'hva_bor_du_html': '<p>Når du leser om angrerett, vær oppmerksom på de presise ordene. "Fjernsalg" er ikke det samme '
                     'som "salg utenom faste forretningslokaler" — selv om begge gir deg angrerett. "Digitalt innhold" '
                     'og "digital tjeneste" har litt forskjellige regler. Ved tvil: les definisjonen i § 5, og se '
                     'hvilken bokstav som passer for ditt tilfelle.</p>',
  'dumme_sporsmal': [{'q': 'Er jeg "forbruker" hvis jeg kjøper noe til hobbyen min?',
                      'a': 'Ja, så lenge hobbyen ikke er næring. Hvis du strikker og selger noen luer av og til uten å '
                           'drive virksomhet, er du fortsatt forbruker. Hvis du har enkeltpersonforetak og selger '
                           'strikketøy regelmessig, er du næringsdrivende.'},
                     {'q': 'Hva er forskjellen på "digitalt innhold" og "digital tjeneste"?',
                      'a': 'Digitalt innhold er noe du laster ned eller kjøper én gang — en film, en e-bok, et spill. '
                           'Digital tjeneste er noe du bruker over tid — Netflix, Spotify, Microsoft 365. Forskjellen '
                           'påvirker blant annet hvor lenge du har angrerett, og hva som skjer hvis du har begynt å '
                           'bruke det.'}],
  'related': [{'lov': 'angrerettloven', 'paragraf': '1', 'tittel': 'Hvilke kjøp loven gjelder for', 'available': True},
              {'lov': 'angrerettloven', 'paragraf': '2', 'tittel': 'Når loven likevel ikke gjelder', 'available': True},
              {'lov': 'angrerettloven', 'paragraf': '8', 'tittel': 'Selgerens opplysningsplikt', 'available': True},
              {'lov': 'angrerettloven', 'paragraf': '20', 'tittel': 'Slik bruker du angreretten', 'available': True}]},
 {'number': '6',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Slik regnes angrefristen',
  'description': 'Når starter angrefristen og hvordan teller du dagene? Reglene for hvordan fristen beregnes – '
                 'inkludert hva som skjer i helgene.',
  'kort_svar': 'Dagen du mottar varen eller inngår avtalen, teller ikke med. Fristen starter dagen etter. Alle '
               'kalenderdager regnes med — også helger. Men hvis siste dag faller på en lørdag, søndag eller '
               'helligdag, forlenges fristen til nærmeste virkedag.',
  'paragraftekst': 'Når en frist uttrykt i dager skal beregnes fra det tidspunkt en hendelse inntreffer eller en '
                   'handling finner sted, skal den dag hendelsen inntreffer eller handlingen finner sted, ikke anses '
                   'som en del av fristen.\n'
                   '\n'
                   'Alle kalenderdager medregnes i en frist. Ender en frist på en lørdag, helligdag eller høytidsdag '
                   'forlenges den til nærmeste virkedag.',
  'hva_betyr_html': '<p>§ 6 forklarer hvordan du teller dager når du skal regne ut en frist.</p>\n'
                    '<p><strong>Regel 1: Dag null teller ikke.</strong> Hvis varen ankommer mandag, starter '
                    'angrefristen tirsdag. Hvis du signerer en avtale på en torsdag, starter fristen fredag. Selve '
                    '"dagen for hendelsen" skal aldri regnes som dag 1.</p>\n'
                    '<p><strong>Regel 2: Alle dager teller.</strong> Det betyr at lørdager, søndager og helligdager '
                    'teller helt likt som vanlige hverdager. Du kan ikke "trekke fra" helga.</p>\n'
                    '<p><strong>Regel 3: Helgen redder deg på slutten.</strong> Hvis den siste dagen — dag 14 — '
                    'tilfeldigvis faller på en lørdag, søndag eller helligdag, får du fristen forlenget til neste '
                    'virkedag. Det betyr som regel mandagen etter.</p>\n'
                    '<p>For angrerett er den vanlige fristen 14 dager (etter § 21). Disse 14 dagene starter altså '
                    'dagen etter du mottok varen eller inngikk avtalen.</p>',
  'eksempler': [{'navn': 'Anne',
                 'tekst': 'Anne mottar et par sko fra Zalando på en mandag. Mandagen selv teller ikke med. Dag 1 er '
                          'tirsdag. Hun teller fjorten dager fremover — og lander på mandagen to uker senere. Hun har '
                          'angrerett til og med den dagen. Sender hun angremeldingen samme mandag, er hun innenfor '
                          'fristen.'},
                {'navn': 'Eva',
                 'tekst': 'Eva mottar en pakke fra Komplett.no på en lørdag. Dag 1 er søndagen etter. Hun teller '
                          'fjorten dager fremover, og lander på lørdagen to uker senere. Siden lørdag er helgen, '
                          'forlenges fristen til mandag. Hun har altså noen ekstra dager — men bare fordi siste dag '
                          'tilfeldigvis havnet på en helg.'}],
  'vanlige_feil': ['Du tror dagen du mottar varen er dag 1. Det er den ikke. Mottaksdagen teller aldri med. Fristen '
                   'starter dagen etter.',
                   'Du tror helga ikke teller. Det gjør den. Alle dager teller — lørdager, søndager og helligdager. '
                   'Bare hvis siste dag faller på helg, får du forlenget frist.',
                   'Du venter til siste sekund. Hvis du sender angremelding kl. 23.59 på dag 14, er du innenfor — men '
                   'sjansen for å regne feil er mye større. Send det heller noen dager før.'],
  'hva_bor_du_html': '<p>Når varen kommer, sjekk datoen umiddelbart. Sett et minne i kalenderen for dag 10 eller 11 — '
                     'da har du fortsatt god tid hvis du ombestemmer deg. Hvis du er usikker på siste dag, regn heller '
                     'bakover fra det du tror er fristen og legg på et par dager for sikkerhets skyld.</p>',
  'dumme_sporsmal': [{'q': 'Teller dagen jeg signerte avtalen?',
                      'a': 'Nei. Selve signeringsdagen er "dag null" og teller ikke. Fristen starter dagen etter.'},
                     {'q': 'Hva regnes som helligdag i Norge?',
                      'a': 'Nyttårsdag, skjærtorsdag, langfredag, første og andre påskedag, Kristi himmelfartsdag, '
                           'første og andre pinsedag, første og andre juledag, samt 1. og 17. mai. Søndager regnes '
                           'også som helligdag.'},
                     {'q': 'Hva om jeg sender angremelding på et tidspunkt der posten er stengt?',
                      'a': 'Det spiller ingen rolle. Det avgjørende er når du sender meldingen, ikke når selger mottar '
                           'den. En e-post sendt kl. 23.45 på dag 14 er innenfor fristen.'}],
  'related': [{'lov': 'angrerettloven', 'paragraf': '21', 'tittel': 'Angrefristen på 14 dager', 'available': True},
              {'lov': 'angrerettloven', 'paragraf': '20', 'tittel': 'Slik bruker du angreretten', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '1',
               'tittel': 'Hvilke kjøp loven gjelder for',
               'available': True}]},
 {'number': '7',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Det er selgeren som må bevise',
  'description': 'Det er selgeren som må bevise at de informerte deg riktig. Selgerens bevisbyrde for '
                 'opplysningsplikten – og hva det betyr for deg som forbruker.',
  'kort_svar': 'Det er selgeren — ikke du — som må bevise at de har gitt deg riktig informasjon før kjøpet. Hvis '
               'selgeren ikke kan dokumentere at du fikk opplysninger om angrerett, pris, returkostnader og lignende, '
               'har de ikke oppfylt loven. Dette gir deg flere rettigheter.',
  'paragraftekst': 'Den næringsdrivende har bevisbyrden for at opplysningsplikten i §§ 8 til 16 og § 18 er oppfylt.',
  'hva_betyr_html': '<p>"Bevisbyrde" betyr at det er én av partene som må bevise noe i en tvist. § 7 sier at det er '
                    'selgeren som har den byrden — ikke du.</p>\n'
                    '<p><strong>Praktisk:</strong> Hvis dere blir uenige om hvorvidt selgeren har gitt deg informasjon '
                    'om for eksempel angrerett, returkostnader eller pris, må selgeren kunne fremlegge dokumentasjon. '
                    'Et "vi pleier å gjøre det" er ikke nok. De må kunne vise konkret at akkurat du fikk akkurat den '
                    'informasjonen.</p>\n'
                    '<p>Hvis selgeren ikke kan dokumentere det, går loven ut fra at de ikke har informert deg. Da kan '
                    'du for eksempel slippe å betale tilleggskostnader (§ 9), eller få utvidet angrefristen til 12 '
                    'måneder (§ 21 tredje ledd).</p>\n'
                    '<p>Dette er en stor fordel for deg. Mange forbrukere tror feilaktig at de selv må bevise hva som '
                    'ble sagt eller skrevet. Det stemmer ikke. Bevisbyrden ligger hos den profesjonelle parten — '
                    'bedriften.</p>',
  'eksempler': [{'navn': 'Tom',
                 'tekst': 'Tom kjøper en bordlampe på nett for 1 800 kr. Når han pakker opp pakken, finner han ingen '
                          'informasjon om angrerett — verken på papir eller i bekreftelses-e-posten. Han bestemmer seg '
                          'for å returnere lampen og krever full refusjon. Selgeren protesterer og sier at "alle våre '
                          'kunder får angrerett-info". Men de kan ikke vise hvilken e-post de sendte til Tom, eller '
                          'hvor på nettsiden informasjonen sto. Etter § 7 må selgeren bevise — det er ikke Tom som må '
                          'bevise det motsatte. Resultatet: selgeren har ikke oppfylt sin opplysningsplikt, og Toms '
                          'angrefrist forlenges automatisk.'}],
  'vanlige_feil': ['Du tror du må bevise hva selgeren sa. Du må det ikke. Det er selgeren som må bevise hva de '
                   'informerte deg om.',
                   'Du tror at "det står i vilkårene mine et sted" er nok bevis fra selgerens side. Det er det ofte '
                   'ikke. Selgeren må kunne vise at akkurat du fikk informasjonen på en klar og forståelig måte.',
                   'Du sletter all kommunikasjon med selgeren etter kjøpet. Selv om bevisbyrden ligger på selgeren, er '
                   'det smart å beholde bekreftelses-e-poster, kvitteringer og skjermbilder. Hvis det blir tvist, '
                   'hjelper dette.'],
  'hva_bor_du_html': '<p>Selv om loven står på din side: ta vare på dokumentasjonen. Lagre bekreftelses-e-post, ta '
                     'skjermbilder av handlekurv og bestillingsside, og oppbevar fysiske kvitteringer. Hvis du klager '
                     'til selger og opplever motstand, vis dem til § 7 og krev at de fremlegger dokumentasjon på at de '
                     'oppfylte opplysningsplikten.</p>\n'
                     '<p>Hvis selgeren ikke samarbeider, kan du klage til Forbrukerrådet. De vurderer ofte bevisene '
                     'strengt — i din favør hvis selgeren ikke kan dokumentere.</p>',
  'dumme_sporsmal': [{'q': 'Hva hvis selger sier de ikke har fått min angremelding?',
                      'a': 'Selve angremeldingen er din sak å dokumentere — § 7 gjelder selgerens opplysningsplikt før '
                           'avtalen, ikke meldinger du sender. Send angremeldingen på e-post (eller bruk angreskjema) '
                           'så har du en kopi.'},
                     {'q': 'Må selgeren bevise at jeg leste opplysningene?',
                      'a': 'Nei. De må bevise at de ga deg opplysningene på en klar og forståelig måte. Om du faktisk '
                           'leste dem, er din sak.'}],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '8',
               'tittel': 'Selgerens opplysningsplikt før kjøpet',
               'available': True},
              {'lov': 'angrerettloven', 'paragraf': '20', 'tittel': 'Slik bruker du angreretten', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '21',
               'tittel': 'Angrefristen og når den forlenges',
               'available': True}]},
 {'number': '8',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Hva selgeren må fortelle deg før du kjøper',
  'description': 'Hva må selgeren opplyse om før du kjøper? Den fullstendige listen over informasjon du har krav på – '
                 'pris, angrerett, returkostnader og mye mer.',
  'kort_svar': 'Før du kjøper noe på nett eller utenfor butikk, må selgeren gi deg en lang liste med opplysninger — '
               'blant annet pris, leveringsmåte, angrerett, returkostnader, garantier og hvem selgeren faktisk er. '
               'Hvis selgeren ikke gjør det, kan du få utvidet angrefrist og slippe å betale tilleggskostnader.',
  'paragraftekst': 'Før det blir inngått en avtale om fjernsalg eller avtale utenom faste forretningslokaler, skal den '
                   'næringsdrivende på en klar og forståelig måte gi forbrukeren opplysninger om:\n'
                   '\n'
                   'a. varenes eller tjenestenes viktigste egenskaper [...]\n'
                   'd. den næringsdrivendes identitet, slik som foretaksnavn, geografisk adresse og telefonnummer, '
                   'e-postadresse [...]\n'
                   'e. den samlede prisen for varen eller tjenesten medregnet avgifter [...]\n'
                   'h. at det foreligger angrerett samt vilkårene, tidsfristene og fremgangsmåtene for å bruke '
                   'angreretten [...]\n'
                   'i. at forbrukeren må bære kostnadene ved å returnere varene dersom angreretten brukes [...]\n'
                   'n. avtalens varighet og eventuell minste bindingstid [...]\n'
                   'r. eventuell ettersalgsservice og eventuelle kommersielle garantier [...]\n'
                   '\n'
                   '(Hele paragrafen har bokstavene a til r, totalt 18 opplysningskrav. Se Lovdata for fullstendig '
                   'liste.)\n'
                   '\n'
                   'Når næringsdrivende retter sin markedsføring mot norske forbrukere, skal opplysningene etter '
                   'første ledd gis på norsk.',
  'hva_betyr_html': '<p>§ 8 er én av de viktigste paragrafene i loven. Den lister opp atten ting selgeren må fortelle '
                    'deg før du forplikter deg til å kjøpe. Listen virker overveldende, men kan grupperes slik:</p>\n'
                    '<h3>Hvem du handler med (d)</h3>\n'
                    '<p>Selgerens fulle navn, adresse, telefon og e-post. Hvis selgeren opptrer på vegne av noen '
                    'andre, må også den andre parten oppgis.</p>\n'
                    '<h3>Hva du kjøper (a, b, c)</h3>\n'
                    '<p>Varens eller tjenestens viktigste egenskaper. For digitale produkter må selgeren også opplyse '
                    'om funksjonalitet, kompatibilitet og om det fungerer med andre systemer.</p>\n'
                    '<h3>Hva det koster (e, f, q)</h3>\n'
                    '<p>Total pris inkludert moms og avgifter. Frakt og andre tilleggskostnader skal være med, eller '
                    'iallfall opplyses om at de kan komme. Ved abonnement må de oppgi pris per måned eller annen '
                    'periode. Hvis prisen er personlig tilpasset basert på algoritmer, må selgeren si fra om det.</p>\n'
                    '<h3>Hvordan kjøpet gjennomføres (g, l, n, o)</h3>\n'
                    '<p>Hvordan du betaler, når du får varen, hvor lang leveringstid, hvordan reklamasjoner håndteres. '
                    'For abonnementer: bindingstid og oppsigelsesvilkår. Eventuelt depositum.</p>\n'
                    '<h3>Angrerett — den viktigste delen (h, i, j, k)</h3>\n'
                    '<p>At du har angrerett. Hvor lang fristen er. Hvordan du går frem for å angre. Et standardisert '
                    'angreskjema. Hvem som betaler returkostnadene. Hva som skjer hvis du har bedt om at en tjeneste '
                    'skulle starte før angrefristen var ute. Og hvis det finnes unntak fra angreretten (etter § 22), '
                    'må selgeren si fra om det.</p>\n'
                    '<h3>Garantier og klageordninger (m, p, r)</h3>\n'
                    '<p>Eventuelle bransjeregler selgeren følger, eventuell tilknytning til en klagenemnd som '
                    'Forbrukerrådet, og eventuell ettersalgsservice eller produktgaranti.</p>\n'
                    '<h3>To viktige tilleggsregler</h3>\n'
                    '<p><strong>Norsk språk.</strong> Hvis selgeren retter markedsføringen mot norske forbrukere, skal '
                    'opplysningene gis på norsk. En nettbutikk med norsk språkversjon eller norsk markedsføring kan '
                    'ikke gjemme angrerett-info i engelsk småtekst.</p>\n'
                    '<p><strong>Standardskjema.</strong> Selgeren kan oppfylle deler av plikten (h, i, j) ved å gi deg '
                    'et offentlig standardskjema med opplysninger om angreretten. Du kjenner det igjen som '
                    '"Opplysninger om angrerett" — et A4-skjema som mange nettbutikker sender med '
                    'bekreftelses-e-posten.</p>',
  'eksempler': [{'navn': 'Sara',
                 'tekst': 'Sara kjøper en jakke på et utenlandsk nettsted som markedsfører seg mot norske kunder. '
                          'Bekreftelses-e-posten kommer på engelsk, og det er ingen info om angrerett. Hun vet ikke om '
                          'hun har rett til å returnere. Selgeren har brutt § 8. Norsk markedsføring krever norsk '
                          'språk. Manglende angrerett-info gir Sara en utvidet angrefrist på opptil 12 måneder etter § '
                          '21 tredje ledd. Hun har altså god tid til å bestemme seg.'},
                {'navn': 'Lars',
                 'tekst': 'Lars får hjemmebesøk fra et solenergifirma. Selgeren snakker engasjert om panelene, men gir '
                          'Lars ingen skriftlig informasjon. Han signerer en kontrakt på selgerens nettbrett for 80 '
                          '000 kr. Selgeren har brutt § 8 på flere punkter — manglende skriftlig prisinfo, ingen '
                          'angreskjema, ingen klar info om returkostnader. Lars kan kreve at hele eller deler av '
                          'kostnadene faller bort (§ 9), og hans angrefrist forlenges. Han står i en mye sterkere '
                          'posisjon enn han kanskje selv tror.'}],
  'vanlige_feil': ['Du tror "small print" er nok. Det er det ikke. Informasjonen skal gis "på en klar og forståelig '
                   'måte". Skjult tekst i lange vilkår oppfyller ikke kravet.',
                   'Du tror at hvis du ikke leste opplysningene, er det din feil. Det er det ikke. Selgeren har '
                   'plikten til å gi dem på en tydelig måte. § 7 sier også at det er selgeren som må bevise at de ble '
                   'gitt.',
                   'Du tror at total pris kan komme som en overraskelse i kassen. Det kan den ikke. Alle obligatoriske '
                   'avgifter og kostnader skal være med i prisen som vises. Tilleggskostnader som frakt skal opplyses '
                   'tydelig før du fullfører kjøpet.'],
  'hva_bor_du_html': '<p>Når du handler på nett eller utenfor butikk, sjekk at du fikk:</p>\n'
                     '<ul>\n'
                     '<li>Tydelig pris inkludert frakt og avgifter</li>\n'
                     '<li>Selgerens fulle navn og kontaktinformasjon</li>\n'
                     '<li>Et angreskjema eller annen tydelig informasjon om hvordan du angrer</li>\n'
                     '<li>Info om returkostnader (hvis du må betale frakt tilbake)</li>\n'
                     '</ul>\n'
                     '<p>Hvis noe mangler, ta vare på bekreftelses-e-posten din og vis til § 8 hvis det oppstår en '
                     'tvist senere.</p>',
  'dumme_sporsmal': [{'q': 'Hva er et "angreskjema"?',
                      'a': 'Det er et standardisert skjema som selgeren skal gi deg sammen med kjøpet. Skjemaet '
                           'inneholder forklaring av angreretten din og et felt du kan fylle ut for å angre. Du finner '
                           'den offisielle versjonen på Forbrukertilsynets nettsider.'},
                     {'q': 'Må selgeren si fra om garantien er bedre enn loven?',
                      'a': 'Selgeren må opplyse om garantien finnes og hva den dekker. Garantien må gi deg noe utover '
                           'lovens minimumsrettigheter for å være verdt noe — hvis ikke, er den i praksis tom.'}],
  'related': [{'lov': 'angrerettloven', 'paragraf': '7', 'tittel': 'Selgeren har bevisbyrden', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '9',
               'tittel': 'Hva skjer hvis selger ikke informerte om kostnader',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '9a',
               'tittel': 'Ekstra regler for nettbaserte markedsplasser',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '21',
               'tittel': 'Angrefristen forlenges hvis selgeren ikke informerer',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '22',
               'tittel': 'Når angreretten ikke gjelder',
               'available': True}]},
 {'number': '9',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Skjulte kostnader trenger du ikke å betale',
  'description': 'Glemte selgeren å nevne frakt eller andre kostnader? Da kan du la være å betale dem. Slik fungerer '
                 'regelen om tilleggskostnader i § 9.',
  'kort_svar': 'Hvis selgeren ikke har opplyst deg om tilleggskostnader som frakt eller andre kostnader før du kjøpte, '
               'trenger du ikke å betale dem. Dette gjelder også returkostnader. Selgeren mister retten til disse '
               'pengene fordi de brøt opplysningsplikten.',
  'paragraftekst': 'Har den næringsdrivende ikke opplyst om tilleggskostnader eller andre kostnader som omhandlet i § '
                   '8 første ledd bokstav e og i, skal forbrukeren ikke bære disse kostnadene.',
  'hva_betyr_html': '<p>§ 9 er en streng konsekvens av brudd på § 8. Hvis selgeren skulle ha fortalt deg om en kostnad '
                    '— men ikke gjorde det — så slipper du å betale den.</p>\n'
                    '<p>Det er to typer kostnader regelen gjelder for:</p>\n'
                    '<p><strong>1. Tilleggskostnader til prisen (§ 8 bokstav e).</strong> Dette er typisk frakt, '
                    'ekspedisjon, betalingsgebyr, miljøgebyr og lignende. Hvis selgeren ikke har opplyst om disse før '
                    'kjøpet, faller de bort.</p>\n'
                    '<p><strong>2. Returkostnader (§ 8 bokstav i).</strong> Hvis du angrer og må sende varen tilbake, '
                    'er hovedregelen at du betaler frakten. Men hvis selgeren ikke har sagt det på forhånd, må '
                    'selgeren dekke det.</p>\n'
                    '<p>Dette er en av flere "sanksjoner" loven har for å sørge for at selgerne faktisk gir deg riktig '
                    'informasjon. Det er ikke nok å gjemme kostnadene i vilkårene — de må kommuniseres klart før '
                    'kjøpet.</p>',
  'eksempler': [{'navn': 'Anne',
                 'tekst': 'Anne kjøper en stol på nett for 2 400 kr. På siden står prisen tydelig. Hun går til kassen, '
                          'fyller ut adressen, klikker "fullfør kjøp". Først i bekreftelses-e-posten ser hun at det er '
                          'lagt på 250 kr i frakt. Selgeren skulle ha opplyst om dette før kjøpet, ikke etter. Etter § '
                          '9 trenger Anne ikke å betale fraktkostnaden. Hun krever at de 250 kronene tilbakebetales — '
                          'og står på trygg grunn.'},
                {'navn': 'Tom',
                 'tekst': 'Tom kjøper en kaffemaskin på nett for 4 500 kr og bestemmer seg etter to dager for å angre. '
                          'Han ser i bekreftelses-e-posten at selgeren aldri nevnte at han måtte betale returfrakt '
                          'selv. Etter § 8 bokstav i skal selgeren opplyse om dette på forhånd. Når de ikke gjorde '
                          'det, faller returkostnaden bort. Tom kan returnere maskinen for selgerens regning, eller få '
                          'fraktkostnadene refundert.'}],
  'vanlige_feil': ['Du tror "det stod i vilkårene" er nok. Det er det sjelden. Kostnader skal opplyses klart og før '
                   'kjøpet — ikke gjemmes i flere ledd ned i en lang vilkårstekst.',
                   'Du betaler kostnaden uten å spørre. Mange forbrukere betaler skjulte kostnader bare for å unngå '
                   'konflikt. Hvis selgeren brøt § 8, har du krav på pengene tilbake.',
                   'Du tror dette gjelder alle uventede kostnader. Det gjelder spesifikt tilleggskostnader (bokstav e) '
                   'og returkostnader (bokstav i). Andre brudd på opplysningsplikten har egne konsekvenser — for '
                   'eksempel utvidet angrefrist etter § 21.'],
  'hva_bor_du_html': '<p>Når du oppdager en kostnad som ikke var nevnt, samle dokumentasjon: bekreftelses-e-post, '
                     'skjermbilder av handlekurven, faktura. Send en e-post til selgeren der du viser til § 8 og § 9, '
                     'og krev refusjon. Hvis selgeren ikke samarbeider, klag til Forbrukerrådet.</p>',
  'dumme_sporsmal': [{'q': 'Hva hvis selgeren sier at "frakt er normalt"?',
                      'a': 'Det spiller ingen rolle. Det avgjørende er om akkurat den kostnaden ble opplyst om før '
                           'kjøpet — ikke om kunden burde forventet det.'},
                     {'q': 'Gjelder dette også betalingsgebyr eller "service avgift"?',
                      'a': 'Ja. Alle obligatoriske tilleggskostnader er omfattet. Hvis en selger legger på 39 kr '
                           '"ekspedisjonsgebyr" som ikke var opplyst om, kan du kreve det tilbake.'}],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '8',
               'tittel': 'Selgerens opplysningsplikt før kjøpet',
               'available': True},
              {'lov': 'angrerettloven', 'paragraf': '7', 'tittel': 'Selgeren har bevisbyrden', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '25',
               'tittel': 'Forbrukerens forpliktelser ved retur',
               'available': True}]},
 {'number': '9a',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Hva en markedsplass som Finn eller Amazon må fortelle deg',
  'description': 'Hva må Finn, Amazon og andre markedsplasser opplyse om? Reglene for rangering, privat vs '
                 'næringsdrivende selger og fordeling av ansvar.',
  'kort_svar': 'Når du handler på en nettbasert markedsplass som Finn, Amazon eller eBay, må plattformen fortelle deg '
               'fire ting: hvordan søkeresultatene rangeres, om selgeren er en bedrift eller en privatperson, at '
               'forbrukerrettigheter ikke gjelder hvis selgeren er privat, og hvem som har ansvar for hva mellom '
               'selger og plattform.',
  'paragraftekst': 'Før det blir inngått en avtale om fjernsalg på nettbaserte markedsplasser, skal tilbyderen av den '
                   'nettbaserte markedsplassen gi forbrukeren følgende opplysninger på en måte som er klar, forståelig '
                   'og egnet for fjernkommunikasjonsmiddel:\n'
                   '\n'
                   'a. generelle opplysninger om hovedparametrene som avgjør rangeringen av tilbud som presenteres for '
                   'forbrukeren i søkeresultatet, og den relative betydningen av disse parametrene i forhold til andre '
                   'parametrer\n'
                   '\n'
                   'b. om selgeren er næringsdrivende eller ikke, på grunnlag av selgerens erklæring til tilbyderen av '
                   'den nettbaserte markedsplassen\n'
                   '\n'
                   'c. at forbrukerrettigheter ikke kommer til anvendelse på avtalen dersom selgeren ikke er '
                   'næringsdrivende\n'
                   '\n'
                   'd. der det er relevant, fordelingen av plikter knyttet til avtalene mellom selgeren og tilbyderen '
                   'av den nettbaserte markedsplassen.\n'
                   '\n'
                   'Opplysningene etter første ledd bokstav a må gis i en særskilt del av det nettbaserte '
                   'grensesnittet som er direkte og enkelt tilgjengelig fra siden der tilbudene presenteres.',
  'hva_betyr_html': '<p>§ 9 a er nyere enn resten av loven (lagt til i 2023) og handler om nettbaserte markedsplasser. '
                    'Det er plattformer som Finn, Amazon, eBay, Etsy og Tise — steder der mange selgere selger til '
                    'mange kjøpere gjennom én felles plattform.</p>\n'
                    '<p>Plattformen har et eget ansvar for å gi deg fire typer informasjon, i tillegg til det selgeren '
                    'selv skal opplyse om (etter § 8):</p>\n'
                    '<p><strong>a) Hvordan rangeres søkeresultatene?</strong> Når du søker, må plattformen forklare '
                    'hvilke kriterier som avgjør rekkefølgen. Er det pris? Popularitet? Annonsering? Algoritmer basert '
                    'på din historikk? Du har krav på å vite hovedreglene. Disse opplysningene skal være enkelt '
                    'tilgjengelige fra søkesiden — typisk via en lenke.</p>\n'
                    '<p><strong>b) Er selgeren bedrift eller privatperson?</strong> Plattformen må vise tydelig om '
                    'selgeren er næringsdrivende eller privat. Forskjellen er stor: ved kjøp fra en bedrift har du '
                    'angrerett, reklamasjonsrett og andre forbrukerrettigheter. Ved kjøp fra en privatperson har du '
                    'langt færre rettigheter.</p>\n'
                    '<p><strong>c) Konsekvensen av å kjøpe fra en privatperson.</strong> Plattformen må fortelle deg '
                    'at forbrukerrettighetene IKKE gjelder hvis selgeren er privat. Dette er en advarsel — for du kan '
                    'lett tro at "jeg handlet på Finn, så jeg er beskyttet". Det er du ikke nødvendigvis.</p>\n'
                    '<p><strong>d) Hvem har ansvar for hva?</strong> Hvis plattformen har ansvar for visse deler av '
                    'avtalen (for eksempel betaling, levering, eller kundeservice), skal det opplyses tydelig. Dette '
                    'er viktig hvis noe går galt.</p>\n'
                    '<p>Merk at plattformen baserer informasjonen om "næringsdrivende eller ikke" på selgerens egen '
                    'erklæring. Hvis en privatperson lyver og sier de er privatperson når de faktisk driver næring, er '
                    'det ikke plattformens feil — men du kan ha rettigheter mot selgeren selv.</p>',
  'eksempler': [{'navn': 'Petter',
                 'tekst': 'Petter søker etter en brukt jakke på Finn. Han finner en jakke for 800 kr, klikker seg inn, '
                          'og ser tydelig på toppen av annonsen: "Privat selger". Under annonsen står det en kort '
                          'tekst: "Ved kjøp fra privatperson gjelder ikke forbrukerkjøpsloven eller angrerettloven." '
                          'Det er § 9 a bokstav b og c i praksis. Petter er nå informert: hvis jakken har en feil, har '
                          'han ikke samme reklamasjonsrett som ved kjøp fra en bedrift. Han kjøper likevel — men nå '
                          'med åpne øyne.'},
                {'navn': 'Marius',
                 'tekst': 'Marius kjøper en sportsklokke på en nettbasert markedsplass. Klokken er defekt. Han '
                          'kontakter plattformen, som sier "selgeren er ansvarlig, ikke vi". Marius lurer på hva som '
                          'faktisk gjelder. Han sjekker plattformens hjelpesider og finner informasjonen om "fordeling '
                          'av plikter" etter § 9 a bokstav d. Det viser seg at plattformen har en kjøperbeskyttelse '
                          'hvis varen aldri leveres, men ikke ansvar for feil og mangler — det ligger på selger. Nå '
                          'vet han hva han kan kreve og fra hvem.'}],
  'vanlige_feil': ['Du tror "kjøp på Finn = forbrukerrettigheter". Det stemmer bare hvis selgeren er en bedrift. Mange '
                   'selgere på Finn er privatpersoner — og da gjelder ikke angrerett, og reklamasjonsretten er mye '
                   'svakere.',
                   'Du tror plattformen alltid er ansvarlig hvis noe går galt. Plattformen er som regel bare '
                   'mellommann. Det er selgeren som er din avtalemotpart — med mindre plattformen har påtatt seg '
                   'spesifikke plikter.',
                   'Du tror søkeresultatene viser "objektivt det beste". De gjør sjelden det. Mange plattformer '
                   'rangerer etter annonsekjøp, kommisjon eller andre kommersielle hensyn. Du har rett til å få vite '
                   'hovedkriteriene.'],
  'hva_bor_du_html': '<p>Før du kjøper på en markedsplass: sjekk om selgeren er merket som bedrift eller privatperson. '
                     'Det er som regel tydelig vist nær prisen eller selgerinformasjonen. Hvis det er en privatperson, '
                     'vær klar over at du tar større risiko. Hvis det er en bedrift, har du fulle '
                     'forbrukerrettigheter.</p>\n'
                     '<p>Hvis du er nysgjerrig på rangeringskriteriene, se etter en lenke som "Hvordan vi rangerer '
                     'tilbud" — den skal være tilgjengelig fra søkesiden.</p>',
  'dumme_sporsmal': [{'q': 'Hva er forskjellen på å kjøpe fra en bedrift vs. privatperson på Finn?',
                      'a': 'Stor forskjell. Fra bedrift har du angrerett (14 dager), reklamasjonsrett (2-5 år) og rett '
                           'til feilfri vare. Fra privatperson har du langt færre rettigheter — i hovedsak kjøpsloven, '
                           'som er svakere enn forbrukerkjøpsloven. Privatpersoner har heller ikke angrerett-plikt.'},
                     {'q': 'Hvorfor må plattformen forklare rangering?',
                      'a': 'Fordi mange tror at det "beste" tilbudet kommer øverst. I virkeligheten kan rangering være '
                           'påvirket av annonsekjøp, kommisjon og algoritmer som ikke nødvendigvis tjener deg. Reglene '
                           'skal gjøre dette synlig.'}],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '8',
               'tittel': 'Selgerens opplysningsplikt før kjøpet',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '5',
               'tittel': 'Definisjoner (inkl. nettbasert markedsplass)',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '1',
               'tittel': 'Hvilke kjøp loven gjelder for',
               'available': True}]},
 {'number': '10',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Du er ikke bundet av telefonsalg før du har akseptert skriftlig',
  'description': 'Du sa "ja" til en selger på telefonen — er du bundet? Nei, ikke før du har akseptert skriftlig. Slik '
                 'fungerer regelen for uanmodet telefonsalg.',
  'kort_svar': 'Hvis en selger ringer deg uten at du har bedt om det, og du sier "ja" på telefonen, er du ikke bundet '
               'av avtalen. Selgeren må sende deg en skriftlig bekreftelse, og du må akseptere skriftlig før avtalen '
               'gjelder. Hvis du ikke svarer, har du ingen avtale. Unntakene er avisabonnement og salg fra frivillige '
               'organisasjoner.',
  'paragraftekst': 'Før det blir inngått en avtale som følge av at den næringsdrivende uanmodet har fremsatt et tilbud '
                   'på telefon, skal den næringsdrivende bekrefte tilbudet skriftlig på et varig medium etter at '
                   'telefonsamtalen er avsluttet. Forbrukeren blir ikke bundet før tilbudet er akseptert skriftlig, '
                   'noe den næringsdrivende skal opplyse om i bekreftelsen nevnt i første punktum. Den næringsdrivende '
                   'skal kunne dokumentere forbrukerens aksept.\n'
                   '\n'
                   'Første ledd gjelder ikke ved salg av avisabonnement eller salg fra frivillige organisasjoner. '
                   'Departementet kan i forskrift stille krav om registrering i frivillighetsregisteret etter '
                   'frivillighetsregisterloven for å bli regnet som frivillig organisasjon.',
  'hva_betyr_html': '<p>§ 10 beskytter deg mot et veldig vanlig press-scenario: en selger ringer uten forvarsel, '
                    'snakker entusiastisk, og før du vet ordet av det har du "sagt ja" til noe. Loven sier at dette '
                    'muntlige ja-et ikke binder deg.</p>\n'
                    '<p>Slik fungerer regelen:</p>\n'
                    '<ol>\n'
                    '<li><strong>Selgeren må ringe uoppfordret.</strong> Det betyr at det er selgeren som tok kontakt '
                    'med deg — du ringte ikke dem. Hvis du selv ringte for å bestille noe, gjelder ikke regelen.</li>\n'
                    '<li><strong>Etter samtalen skal selgeren sende skriftlig bekreftelse.</strong> Dette skal være på '
                    'et "varig medium" — typisk e-post, SMS eller papirpost. I bekreftelsen skal det stå klart at du '
                    'ikke er bundet før du har akseptert skriftlig.</li>\n'
                    '<li><strong>Du må aktivt akseptere skriftlig.</strong> Hvis du ikke svarer på bekreftelsen, har '
                    'du ingen avtale. Stillhet er ikke aksept. Du trenger ikke engang å si "nei" — du kan bare la være '
                    'å svare.</li>\n'
                    '<li><strong>Selgeren må kunne dokumentere din aksept.</strong> Hvis dere senere blir uenige, må '
                    'selgeren bevise at du faktisk aksepterte skriftlig. Et muntlig "ja" på telefonen teller '
                    'ikke.</li>\n'
                    '</ol>\n'
                    '<p>Unntakene er avisabonnement og salg fra frivillige organisasjoner. Disse kan inngå avtale '
                    'muntlig. Bakgrunnen er at disse aktørene tradisjonelt har drevet med ringekampanjer, og lovgiver '
                    'har valgt å gjøre unntak for dem.</p>',
  'eksempler': [{'navn': 'Anne',
                 'tekst': 'Anne sitter hjemme en kveld da en strømleverandør ringer. Selgeren snakker engasjert om '
                          'hvor mye hun kan spare, og spør om hun vil bytte. Anne sier "ja, det høres bra ut". '
                          'Selgeren sier "supert, du vil få en bekreftelse på e-post". Bekreftelsen kommer dagen '
                          'etter. Anne har ombestemt seg og lar e-posten ligge ulest i tre uker. Strømleverandøren '
                          'purrer flere ganger. Anne svarer aldri. Hun har ingen avtale. Strømleverandøren kan ikke '
                          'kreve at hun betaler bruddgebyr eller at hun bytter — fordi hun aldri aksepterte '
                          'skriftlig.'},
                {'navn': 'Kari',
                 'tekst': 'Kari får telefon fra Røde Kors (en frivillig organisasjon). De spør om hun vil bli fast '
                          'giver med 200 kr i måneden. Hun sier ja, og oppgir kontonummer på telefonen. Her gjelder '
                          'ikke § 10, fordi salg fra frivillige organisasjoner er unntatt etter andre ledd. Karis '
                          'muntlige aksept er bindende. Hun kan likevel si opp avtalen senere etter alminnelige regler '
                          '— frivillige donasjoner har normalt ingen bindingstid.'}],
  'vanlige_feil': ['Du tror du er bundet fordi du "sa ja" på telefonen. Du er ikke det ved uanmodet telefonsalg. Et '
                   'muntlig ja har ingen rettslig virkning. Du må akseptere skriftlig.',
                   'Du svarer på bekreftelsen "for å være høflig". Hvis du svarer "ja takk" eller "ok" på e-post eller '
                   'SMS, er du bundet. Pass på hva du skriver tilbake. Vil du ikke ha avtalen, ikke svar.',
                   'Du tror at "stillhet er aksept" hvis du ikke svarer innen en frist. Det stemmer ikke. Selgeren kan '
                   'ikke skrive "vi anser deg som bundet hvis du ikke svarer innen 14 dager". Du må aktivt si ja '
                   'skriftlig.'],
  'hva_bor_du_html': '<p>Når en selger ringer:</p>\n'
                     '<ul>\n'
                     '<li>Ikke føl deg presset til å si ja på telefonen</li>\n'
                     '<li>Be om at de sender informasjon på e-post i stedet, så du får tenke deg om</li>\n'
                     '<li>Hvis du får en bekreftelse du ikke vil ha, ignorer den — du trenger ikke svare</li>\n'
                     '<li>Hvis du allerede har akseptert skriftlig, husk at du har 14 dagers angrerett</li>\n'
                     '</ul>',
  'dumme_sporsmal': [{'q': 'Hva hvis selgeren ringer tilbake og presser meg?',
                      'a': 'Du trenger ikke svare på spørsmål eller forklare deg. Du kan bare si "jeg har ombestemt '
                           'meg" og legge på. Selgeren har ingen avtale å bygge på.'},
                     {'q': 'Gjelder dette også hvis selger sender meg en SMS jeg svarer "ja" på?',
                      'a': 'Ja, da har du akseptert skriftlig. SMS regnes som varig medium. Vær bevisst på hva du '
                           'svarer.'},
                     {'q': 'Hva med "Reservasjon mot telefonsalg"?',
                      'a': 'Du kan registrere deg i Reservasjonsregisteret hos Brønnøysundregistrene. Da har de fleste '
                           'selgere ikke lov til å ringe deg i det hele tatt. Dette er en egen regel under '
                           'markedsføringsloven, ikke angrerettloven.'}],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '11',
               'tittel': 'Krav til avtaler utenom faste forretningslokaler',
               'available': True},
              {'lov': 'angrerettloven', 'paragraf': '20', 'tittel': 'Slik bruker du angreretten', 'available': True},
              {'lov': 'angrerettloven', 'paragraf': '21', 'tittel': 'Angrefristen på 14 dager', 'available': True},
              {'lov': 'markedsforingsloven',
               'paragraf': '12',
               'tittel': 'Reservasjon mot telefonsalg',
               'available': False}]},
 {'number': '11',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Hva avtalen må inneholde ved hjemmesalg',
  'description': 'Hva må avtalen inneholde når selger kommer hjem til deg eller på et stand? Reglene for skriftlig '
                 'avtale, språk og hva du har krav på å få med deg.',
  'kort_svar': 'Når selger har kommet hjem til deg, på arbeidsplassen eller på et stand, må du få avtalen skriftlig. '
               'Den skal inneholde all informasjonen i § 8 — pris, angrerett, selgerens kontaktopplysninger og mer — '
               'på et enkelt og forståelig norsk. Du skal ha et fysisk eksemplar eller en bekreftelse på e-post.',
  'paragraftekst': 'Avtaler inngått utenom faste forretningslokaler skal inneholde opplysningene fastsatt i § 8 første '
                   'ledd. Opplysningene skal regnes som en del av avtalen og skal ikke endres, med mindre partene '
                   'uttrykkelig avtaler noe annet. Opplysningene skal være lett leselige og på et enkelt og forståelig '
                   'språk. Er opplysningene gitt på norsk, skal avtalen utformes på norsk.\n'
                   '\n'
                   'Den næringsdrivende skal gi forbrukeren et eksemplar av undertegnet avtale eller bekreftelse av '
                   'avtalen på papir eller, dersom forbrukeren samtykker, på annet varig medium. Har forbrukeren '
                   'samtykket i nedlastning av digitalt innhold og erkjent at angrerett dermed bortfaller, jf. § 22 '
                   'bokstav n, skal dette også fremgå av avtalen eller bekreftelsen.',
  'hva_betyr_html': '<p>§ 11 gjelder for kjøp utenfor selgerens faste butikk — typisk hjemmesalg, stand-salg eller '
                    'salg på arbeidsplassen.</p>\n'
                    '<p><strong>Avtalen må inneholde alt fra § 8.</strong> Pris, angrerett, kontaktopplysninger, '
                    'returkostnader, garantier og så videre. Selgeren kan ikke kalle det "tilleggsbetingelser" og '
                    'gjemme det bort. Informasjonen er en del av avtalen.</p>\n'
                    '<p><strong>Klart språk.</strong> Vilkårene skal være "lett leselige" og på "enkelt og forståelig '
                    'språk". Småskrift og juridisk sjargong oppfyller ikke kravet.</p>\n'
                    '<p><strong>Norsk språk.</strong> Hvis informasjonen er gitt på norsk, skal hele avtalen være på '
                    'norsk. En selger kan ikke gi muntlig info på norsk og deretter levere kontrakt på engelsk.</p>\n'
                    '<p><strong>Du skal ha en kopi.</strong> Hovedregelen er papir. Hvis du samtykker, kan selger '
                    'sende på e-post eller annet varig medium. Du har krav på enten et signert eksemplar eller en '
                    'formell bekreftelse av avtalen.</p>\n'
                    '<p><strong>Spesielt for digitalt innhold.</strong> Hvis du har samtykket til å laste ned digitalt '
                    'innhold (for eksempel en e-bok eller film), og dermed mistet angreretten etter § 22 bokstav n, må '
                    'det fremgå tydelig av avtalen.</p>',
  'eksempler': [{'navn': 'Lars',
                 'tekst': 'Lars får hjemmebesøk fra et alarmselskap. Selgeren forklarer abonnementet muntlig, og Lars '
                          'signerer på et nettbrett. Selgeren sier: "Avtalen ligger inne i systemet vårt, du kan logge '
                          'inn senere og se den." Det er ikke nok. Etter § 11 har Lars krav på enten et fysisk papir '
                          'eller en e-post med hele avtalen og alle vilkår. Selgeren har brutt loven. Lars kan kreve '
                          'at avtalen sendes på varig medium — og hvis det aldri kommer, kan han hevde at avtalen ikke '
                          'er gyldig inngått eller bruke utvidet angrefrist etter § 21.'},
                {'navn': 'Sara',
                 'tekst': 'Sara står på et kjøpesenter da en selger viser henne en støvsuger til 6 500 kr. Hun '
                          'bestemmer seg for å kjøpe. Selgeren gir henne en kontrakt på engelsk og forklarer ting '
                          'muntlig på norsk. Etter § 11 er dette i strid med kravet om at avtalen skal være på norsk '
                          'når informasjonen er gitt på norsk. Sara kan be om norsk versjon. Hvis selgeren ikke '
                          'leverer, kan hun klage til Forbrukertilsynet og eventuelt bruke utvidet angrefrist.'}],
  'vanlige_feil': ['Du signerer uten å få noe i hånda. Mange selgere bruker nettbrett uten å sende noe i etterkant. Be '
                   'alltid om at avtalen sendes til deg på e-post eller papir før du går derfra.',
                   'Du tar imot avtalen på engelsk og signerer. Hvis selgeren har henvendt seg til deg på norsk, har '
                   'du krav på norsk kontrakt. Aksepter ikke noe annet.',
                   'Du tror du må logge inn på "min side" for å se avtalen. Avtalen skal leveres på et varig medium — '
                   'typisk e-post eller papir. En innlogget side som kan endres av selgeren, oppfyller ikke kravet.'],
  'hva_bor_du_html': '<p>Når selgeren kommer hjem eller står på et stand:</p>\n'
                     '<ul>\n'
                     '<li>Be om å lese gjennom avtalen før du signerer</li>\n'
                     '<li>Krev at du får et papireksemplar eller en kopi på e-post umiddelbart</li>\n'
                     '<li>Sjekk at angrerett-info og angreskjema er med</li>\n'
                     '<li>Hvis selgeren ikke har dette tilgjengelig, ikke signer — det er et tegn på at firmaet ikke '
                     'følger reglene</li>\n'
                     '</ul>',
  'dumme_sporsmal': [],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '8',
               'tittel': 'Hva selgeren må fortelle deg før kjøpet',
               'available': True},
              {'lov': 'angrerettloven', 'paragraf': '10', 'tittel': 'Uanmodet telefonsalg', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '12',
               'tittel': 'Hvis du vil at tjenesten starter før angrefristen',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '22',
               'tittel': 'Når angreretten ikke gjelder',
               'available': True}]},
 {'number': '12',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Hvis du vil at tjenesten starter før angrefristen er ute',
  'description': 'Vil du at en tjeneste starter med en gang, før angrefristen er ute? Da må selgeren ha din '
                 'uttrykkelige aksept – og du må forstå at angreretten kan gå tapt.',
  'kort_svar': 'Hvis du har inngått en avtale om en tjeneste utenfor butikk (for eksempel rørlegger hjem til deg), og '
               'du ønsker at tjenesten skal starte før de 14 dagene av angrefristen er ute, må selgeren ha din '
               'uttrykkelige aksept på et varig medium. Du må også bekrefte at du forstår at angreretten faller bort '
               'når jobben er ferdig.',
  'paragraftekst': 'Ønsker forbrukeren at levering av tjenester starter før utløpet av angrefristen, jf. § 21, og '
                   'avtalen innebærer en betalingsforpliktelse for forbrukeren, skal den næringsdrivende kreve at '
                   'forbrukeren uttrykkelig ber om dette på et varig medium. Den næringsdrivende skal også be '
                   'forbrukeren om å erkjenne at angreretten vil gå tapt når avtalen er oppfylt fullt ut av den '
                   'næringsdrivende.',
  'hva_betyr_html': '<p>§ 12 handler om tjenester som starter raskt. Normalt har du 14 dagers angrerett. Men hvis du '
                    'vil at tjenesten skal starte med en gang, må selger og du følge en bestemt prosedyre.</p>\n'
                    '<p><strong>Du må be om det uttrykkelig.</strong> Det holder ikke at selgeren spør "kan vi begynne '
                    'i morgen?" og du svarer ja muntlig. Du må bekrefte på et varig medium — typisk e-post, SMS, eller '
                    'signere på et fysisk skjema.</p>\n'
                    '<p><strong>Selgeren må også få deg til å bekrefte at angreretten kan gå tapt.</strong> Når jobben '
                    'er ferdig, har du ikke lenger angrerett. Du skal forstå dette på forhånd. Det er en bevisst '
                    'beslutning du tar.</p>\n'
                    '<p><strong>Hva skjer hvis du angrer underveis?</strong> Hvis tjenesten har startet, men ikke er '
                    'ferdig, har du fortsatt angrerett. Men du må betale for det som allerede er gjort (se § 26). Hvis '
                    'hele jobben er ferdig, er angreretten borte.</p>\n'
                    '<p>Hvis selger ikke følger reglene — for eksempel ikke får din uttrykkelige aksept på varig '
                    'medium — slipper du å betale for det som er levert (§ 26 andre ledd). Det er et sterkt insentiv '
                    'for selger til å gjøre dette riktig.</p>',
  'eksempler': [{'navn': 'Eva',
                 'tekst': 'Eva har vannlekkasje i kjelleren. Hun ringer en rørlegger, som kommer hjem til henne samme '
                          'dag. De avtaler reparasjon for 8 000 kr. Reparasjonen tar 6 timer. Dette er et hjemmesalg '
                          '(utenom faste forretningslokaler), så hovedregelen er 14 dagers angrerett. Eva vil åpenbart '
                          'ikke vente 14 dager med vannlekkasjen. Rørleggeren ber henne signere et skjema der hun '
                          'bekrefter (1) at hun ønsker at arbeidet skal starte umiddelbart og (2) at hun forstår at '
                          'angreretten faller bort når jobben er ferdig. Hun signerer. Rørleggeren reparerer '
                          'lekkasjen. Eva kan ikke angre i etterkant fordi jobben er fullført.'},
                {'navn': 'Ola',
                 'tekst': 'Ola får hjemmebesøk fra et solenergifirma. Han bestiller installasjon av solcellepaneler. '
                          'Firmaet ringer dagen etter og sier "vi kommer i morgen og installerer". Ola samtykker '
                          'muntlig. Etter installasjonen ombestemmer Ola seg. Selgeren sier "for sent, du sa jo ja". '
                          'Men selgeren glemte å få Olas uttrykkelige aksept på varig medium etter § 12. Etter § 26 '
                          'andre ledd slipper Ola å betale for arbeidet som er gjort. Han har fortsatt 14 dagers '
                          'angrerett — og kan trekke seg fra hele avtalen uten økonomisk tap.'}],
  'vanlige_feil': ['Selger gjør jobben uten å få skriftlig aksept. Da er ikke kravene oppfylt, og kunden kan slippe å '
                   'betale. Selgeren taper.',
                   'Du signerer uten å lese om angreretten. Hvis selgeren får deg til å signere en setning du ikke '
                   'leste, kan det fortsatt være gyldig — men sjekk alltid at du forstår hva du bekrefter.',
                   'Du tror at "jeg sa det jo til selgeren" er nok. Det er det ikke. Muntlig aksept oppfyller ikke '
                   'kravet om varig medium. Sørg for at det står skriftlig.'],
  'hva_bor_du_html': '<p>Hvis du trenger en tjeneste raskt:</p>\n'
                     '<ul>\n'
                     '<li>Forstå at du kanskje må gi opp angreretten — det er ofte verdt det for hastetjenester</li>\n'
                     '<li>Krev at selgeren forklarer angreretten før du signerer</li>\n'
                     '<li>Behold ditt eksemplar av skjemaet eller e-posten du signerte</li>\n'
                     '</ul>\n'
                     '<p>Hvis selgeren ikke følger reglene og krever betaling: vis til § 26 andre ledd. Du har rett '
                     'til å nekte betaling for det som er levert, hvis ikke uttrykkelig aksept er gitt på varig '
                     'medium.</p>',
  'dumme_sporsmal': [],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '11',
               'tittel': 'Hva avtalen må inneholde ved hjemmesalg',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '19',
               'tittel': 'Tilsvarende regel ved fjernsalg',
               'available': True},
              {'lov': 'angrerettloven', 'paragraf': '21', 'tittel': 'Angrefristen på 14 dager', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '26',
               'tittel': 'Hva du betaler hvis du angrer underveis',
               'available': True}]},
 {'number': '13',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Forenklede regler for små reparasjoner under 1500 kr',
  'description': 'Reparasjon eller vedlikehold under 1500 kr hjemme hos deg? Da gjelder forenklede regler – men du '
                 'skal fortsatt få en bekreftelse i etterkant.',
  'kort_svar': 'Når du ringer en håndverker hjem for å fikse noe, og hele jobben koster 1500 kr eller mindre, gjelder '
               'forenklede regler. Selger trenger ikke å gi all informasjon skriftlig på forhånd — det holder med '
               'navn, kontaktinfo og prisestimat. Men du skal fortsatt få en skriftlig bekreftelse av hele avtalen '
               'etterpå.',
  'paragraftekst': 'Dersom forbrukeren uttrykkelig ber om å få utført reparasjoner eller vedlikehold, partene '
                   'umiddelbart utfører sine forpliktelser etter avtalen og kontraktssummen ikke overstiger 1500 kr, '
                   'er det tilstrekkelig at den næringsdrivende gir forbrukeren opplysningene i § 8 første ledd '
                   'bokstav d, jf. § 11 annet ledd, og opplysninger om prisen eller hvordan prisen skal beregnes, samt '
                   'et anslag over den samlede prisen. Opplysningene omhandlet i § 8 første ledd bokstav a, h og k kan '
                   'gis muntlig, dersom forbrukeren uttrykkelig samtykker i dette.\n'
                   '\n'
                   'Bekreftelsen av avtalen, jf. § 11 annet ledd, skal inneholde opplysningene fastsatt i § 8 første '
                   'ledd.',
  'hva_betyr_html': '<p>§ 13 erkjenner at vanlige småjobber ikke trenger samme byråkrati som store kontrakter. Når du '
                    'ringer en håndverker for å fikse en vannkran eller skifte en pakning, er det upraktisk å kreve '
                    'fullstendig forhåndsinformasjon på papir.</p>\n'
                    '<p>Tre vilkår må være oppfylt for at den forenklede regelen skal gjelde:</p>\n'
                    '<ol>\n'
                    '<li><strong>Du må uttrykkelig be om reparasjon eller vedlikehold.</strong> Ikke nye kjøp, ikke '
                    'installasjoner, ikke design eller rådgivning. Bare reparasjon og vedlikehold.</li>\n'
                    '<li><strong>Begge parter utfører sine plikter umiddelbart.</strong> Håndverkeren gjør jobben med '
                    'en gang, du betaler med en gang.</li>\n'
                    '<li><strong>Totalbeløpet er 1500 kr eller mindre.</strong> Inkludert alt — arbeid, materialer, '
                    'kjørekostnader, moms. Hvis jobben skulle koste mer, slår de vanlige reglene i § 8 og § 11 '
                    'inn.</li>\n'
                    '</ol>\n'
                    '<p>Hvis alle tre vilkår er oppfylt, må selgeren bare gi tre ting før jobben: sitt fulle navn og '
                    'kontaktinformasjon, prisen eller hvordan den beregnes, og et estimat på totalprisen.</p>\n'
                    '<p>Resten av opplysningene fra § 8 — om angrerett, returkostnader, garantier osv. — kan gis '
                    'muntlig hvis du uttrykkelig samtykker.</p>\n'
                    '<p><strong>Men:</strong> etter jobben skal du fortsatt få en skriftlig bekreftelse som inneholder '
                    'all informasjonen i § 8. Det er bare den forhåndsinformasjonen som er forenklet.</p>',
  'eksempler': [{'navn': 'Petter',
                 'tekst': 'Petter har en tett sluk på badet. Han ringer en rørlegger som sier "jeg kan komme om en '
                          'time, og det koster rundt 1 200 kr". Petter sier "perfekt, kom". Rørleggeren kommer, fikser '
                          'sluket på 30 minutter, og Petter betaler 1 200 kr. Dette er klassisk § 13. Rørleggeren '
                          'trengte bare å oppgi navn, kontaktinfo og prisestimat på forhånd. Etter jobben sender han '
                          'Petter en faktura/kvittering med all opplysningsplikt-info etter § 8. Det er nok.'},
                {'navn': 'Anne',
                 'tekst': 'Anne har en frosen vannrør. Hun ringer en rørlegger som anslår 1 300 kr. Når jobben '
                          'starter, viser det seg at det er mer omfattende. Rørleggeren sier "dette blir nok 4 000 '
                          'kr". Nå overstiger jobben 1500 kr. Den forenklede regelen i § 13 gjelder ikke lenger. '
                          'Rørleggeren må følge de vanlige reglene i § 8 og § 11 — gi henne skriftlig informasjon om '
                          'alle vilkår, inkludert angrerett, før arbeidet fortsetter.'}],
  'vanlige_feil': ['Du tror "småjobb" alltid betyr forenklet. Det gjør det bare hvis hele beløpet er under 1500 kr. '
                   'Krysser dere grensen, gjelder de vanlige reglene.',
                   'Du glemmer å kreve kvittering. Selv ved forenklet prosedyre har du krav på skriftlig bekreftelse '
                   'etterpå. Be om kvittering eller faktura på e-post.',
                   'Du tror "reparasjon" inkluderer alt mulig. Det gjør det ikke. Installasjon av nye produkter, '
                   'design eller konsulentarbeid er ikke "reparasjon eller vedlikehold". Da gjelder normalreglene.'],
  'hva_bor_du_html': '<p>Ved små reparasjoner hjemme:</p>\n'
                     '<ul>\n'
                     '<li>Be om et prisestimat før jobben starter</li>\n'
                     '<li>Hvis estimatet er nær 1500 kr, vurder å be om skriftlig avtale uansett</li>\n'
                     '<li>Ta vare på kvitteringen — den skal inneholde all § 8-informasjonen</li>\n'
                     '<li>Hvis jobben blir dyrere underveis enn estimert, sørg for skriftlig bekreftelse på den nye '
                     'prisen</li>\n'
                     '</ul>',
  'dumme_sporsmal': [],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '11',
               'tittel': 'Hva avtalen må inneholde ved hjemmesalg',
               'available': True},
              {'lov': 'angrerettloven', 'paragraf': '8', 'tittel': 'Selgerens opplysningsplikt', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '12',
               'tittel': 'Hvis du vil at tjenesten skal starte umiddelbart',
               'available': True}]},
 {'number': '14',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Krav til avtaler ved netthandel',
  'description': 'Hva må stå i en netthandelsavtale? Selgerens opplysninger skal være tilgjengelige, klare og '
                 'forståelige – og er en del av avtalen.',
  'kort_svar': 'Ved kjøp på nett, telefon eller andre kanaler der dere ikke møtes fysisk, skal informasjonen fra § 8 '
               'være en del av selve avtalen. Den skal være tilgjengelig på et enkelt og forståelig språk, tilpasset '
               'kanalen, og lett leselig.',
  'paragraftekst': 'Avtaler inngått ved fjernsalg skal inneholde opplysningene fastsatt i § 8 første ledd eller så '
                   'skal opplysningen gjøres tilgjengelig for forbrukeren på et enkelt og forståelig språk på en måte '
                   'som er tilpasset fjernkommunikasjonsmiddelet. Opplysningene skal regnes som en del av avtalen og '
                   'skal ikke endres, med mindre partene uttrykkelig avtaler noe annet. Dersom opplysningene gis på et '
                   'varig medium, skal de være lett leselige.',
  'hva_betyr_html': '<p>§ 14 gjør for nettsalg det § 11 gjør for hjemmesalg: den krever at all informasjonen fra § 8 — '
                    'pris, angrerett, returkostnader, kontaktinfo og resten — skal være en del av avtalen.</p>\n'
                    '<p>Tre praktiske krav:</p>\n'
                    '<p><strong>1. Opplysningene er del av avtalen.</strong> Det betyr at de er bindende. Selgeren kan '
                    'ikke vise én pris i bestillingen og kreve en annen i fakturaen. De kan ikke endre vilkårene etter '
                    'at avtalen er inngått, med mindre dere uttrykkelig blir enige om noe annet.</p>\n'
                    '<p><strong>2. Tilpasset kommunikasjonskanalen.</strong> Reglene er litt mer fleksible enn ved '
                    'hjemmesalg. Selgeren trenger ikke nødvendigvis å sende deg en stor kontrakt — informasjonen kan '
                    'være tilgjengelig på nettsiden, så lenge den er klar og enkel å finne. En lenke til "vilkår" må '
                    'ikke gjemmes nederst på siden.</p>\n'
                    '<p><strong>3. Klart språk.</strong> Informasjonen skal være på "enkelt og forståelig språk". Hvis '
                    'du må ha jusutdannelse for å forstå vilkårene, oppfyller selgeren ikke kravet.</p>\n'
                    '<p>Og hvis opplysningene gis på et varig medium (typisk e-post med bekreftelse), skal de være '
                    '"lett leselige". Det betyr ingen mikroskopisk tekst eller gjemte avsnitt.</p>\n'
                    '<p>Forskjellen fra § 11 er at her godtas litt enklere former — du må ikke nødvendigvis få en '
                    'signert kontrakt. Men selgeren har likevel plikt etter § 18 til å sende en skriftlig bekreftelse '
                    'i etterkant.</p>',
  'eksempler': [{'navn': 'Sara',
                 'tekst': 'Sara kjøper en stol på en norsk nettbutikk for 3 200 kr. På bestillingssiden ser hun en '
                          'lenke som heter "Vilkår og angrerett". Hun klikker, og finner en oversiktlig side med all '
                          'informasjonen om pris, frakt, angrerett, returkostnader og kontaktinfo. Dette oppfyller § '
                          '14. Informasjonen er klar, tilgjengelig og tilpasset nettkommunikasjon. Når Sara fullfører '
                          'bestillingen, blir vilkårene en del av avtalen — selgeren kan ikke endre dem unilateralt.'},
                {'navn': 'Tom',
                 'tekst': 'Tom kjøper et abonnement på en streamingtjeneste. Vilkårene viser 99 kr per måned. Tre '
                          'måneder senere får han faktura på 149 kr. Selgeren forklarer at "prisen ble justert". Etter '
                          '§ 14 er den opprinnelige prisen en del av avtalen. Selgeren kan ikke endre den uten at Tom '
                          'uttrykkelig samtykker. Tom kan kreve at den opprinnelige prisen gjelder, eller si opp '
                          'abonnementet uten kostnad.'}],
  'vanlige_feil': ['Du tror "vilkår er vilkår" — at selger kan endre dem som de vil. Det kan de ikke. Vilkårene er en '
                   'del av den bindende avtalen.',
                   'Du tror nettsiden alltid er nok. Den er nok ved bestilling — men i etterkant skal du ha en '
                   'skriftlig bekreftelse på varig medium (§ 18). Bare nettsiden er ikke tilstrekkelig hvis selgeren '
                   'senere endrer den.',
                   'Du tror "tilpasset" betyr "kortere". Det er en misforståelse. Tilpasset kommunikasjon betyr at '
                   'informasjonen skal være lett tilgjengelig og forståelig — ikke at deler kan kuttes ut.'],
  'hva_bor_du_html': '<p>Ved netthandel:</p>\n'
                     '<ul>\n'
                     '<li>Sjekk at vilkårene er enkle å finne før du fullfører kjøpet</li>\n'
                     '<li>Lagre eller skjermbildelagre vilkårene som gjelder på kjøpstidspunktet</li>\n'
                     '<li>Når bekreftelses-e-posten kommer, sjekk at vilkårene fra bestillingen er med</li>\n'
                     '<li>Hvis selgeren senere endrer pris eller vilkår, vis til § 14 og krev at de opprinnelige '
                     'vilkårene gjelder</li>\n'
                     '</ul>',
  'dumme_sporsmal': [],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '8',
               'tittel': 'Hva selgeren må fortelle deg før kjøpet',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '11',
               'tittel': 'Tilsvarende regel ved hjemmesalg',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '15',
               'tittel': 'Forenklet regel ved begrenset plass',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '18',
               'tittel': 'Bekreftelse på inngått avtale',
               'available': True}]},
 {'number': '15',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Når kommunikasjonskanalen har begrenset plass',
  'description': 'Hva må selgeren opplyse om når kjøpet skjer på en kanal med lite plass – som SMS eller en liten '
                 'skjerm? Reglene for minimumsinformasjon.',
  'kort_svar': 'Hvis kjøpet skjer via en kanal med begrenset plass — for eksempel SMS eller en liten enhet — må '
               'selgeren minst opplyse om varens viktigste egenskaper, selgerens identitet, totalprisen, at det finnes '
               'angrerett, og avtalens varighet. Resten av informasjonen må gis på en tilpasset måte i etterkant.',
  'paragraftekst': 'Når avtale inngås gjennom et fjernkommunikasjonsmiddel som har begrenset plass eller tid til å '
                   'vise opplysninger, skal den næringsdrivende gi opplysninger etter § 8 første ledd bokstav a, d, e, '
                   'h første punktum og n før avtale inngås.\n'
                   '\n'
                   'Øvrige opplysninger i § 8 første ledd gis på en måte som er tilpasset fjernkommunikasjonsmiddelet, '
                   'jf. § 14.',
  'hva_betyr_html': '<p>§ 15 er en praktisk regel for kjøp gjennom kanaler der det rett og slett ikke er plass til all '
                    'informasjonen fra § 8. Eksempler er kjøp via SMS, kjøp gjennom et grensesnitt med få tegn, eller '
                    'via stemmeassistenter.</p>\n'
                    '<p>I disse tilfellene må selgeren minst opplyse om fem ting før avtalen inngås:</p>\n'
                    '<ul>\n'
                    '<li><strong>a) Varens viktigste egenskaper.</strong> Hva er det egentlig du kjøper?</li>\n'
                    '<li><strong>d) Selgerens identitet.</strong> Navn og kontaktinformasjon.</li>\n'
                    '<li><strong>e) Totalprisen.</strong> Inkludert eventuelle obligatoriske avgifter.</li>\n'
                    '<li><strong>h første punktum) At det finnes angrerett.</strong> Selve eksistensen av angreretten '
                    '— du trenger ikke alle detaljer på selve kanalen, men du skal vite at den finnes.</li>\n'
                    '<li><strong>n) Avtalens varighet og bindingstid.</strong> Spesielt viktig ved abonnementer.</li>\n'
                    '</ul>\n'
                    '<p>Resten av informasjonen — fullstendige angrerett-vilkår, returkostnader, klageordninger og så '
                    'videre — må gis "på en måte som er tilpasset" kanalen, etter de vanlige reglene i § 14. Det vil i '
                    'praksis si: enten med en lenke til mer info, eller i en bekreftelses-e-post etterpå (etter § '
                    '18).</p>\n'
                    '<p>§ 15 er altså ikke en gratisbillett for selgere. De må fortsatt oppfylle hele '
                    'opplysningsplikten i § 8, men de får lov til å fordele den.</p>',
  'eksempler': [{'navn': 'Marius',
                 'tekst': 'Marius kjøper en parkeringstjeneste ved å sende en SMS med kode og bilnummer. Tjenesten '
                          'bekrefter parkeringen med en SMS tilbake. Selgeren har ikke plass til all informasjonen i § '
                          '8 i en SMS. Etter § 15 må de minst opplyse om hva tjenesten er (parkering), selgerens navn, '
                          'prisen, eksistensen av angrerett, og varigheten. Resten gjøres tilgjengelig på selskapets '
                          'nettside og i bekreftelses-e-post.'},
                {'navn': 'Ingrid',
                 'tekst': 'Ingrid kjøper en app gjennom App Store via Apple Watch. Det vises lite informasjon på selve '
                          'skjermen — bare appens navn, pris og en "Kjøp"-knapp. Apple Watch er et klassisk eksempel '
                          'på begrenset visningsplass. Etter § 15 holder det med minimumsopplysningene før kjøpet, men '
                          'full informasjon må være tilgjengelig på iPhone eller via e-post i etterkant.'}],
  'vanlige_feil': ['Selgere bruker "begrenset plass" som unnskyldning på en vanlig nettside. En full nettside har ikke '
                   '"begrenset plass". Regelen gjelder reelle plassbegrensninger, ikke valget om å lage en kort '
                   'bestillingsside.',
                   'Du tror at fordi informasjonen ikke sto i SMS-en, er selgeren fri for ansvar. Det er de ikke. '
                   'Resten av opplysningene må gis på annet vis — typisk i bekreftelse på e-post.'],
  'hva_bor_du_html': '<p>Ved kjøp via SMS, klokke eller andre små kanaler:</p>\n'
                     '<ul>\n'
                     '<li>Sjekk at minimumsinformasjonen er der: hva, hvem, pris, angrerett, varighet</li>\n'
                     '<li>Forvent en utfyllende bekreftelse på e-post i etterkant</li>\n'
                     '<li>Hvis du ikke får den, klag — det er brudd på opplysningsplikten</li>\n'
                     '</ul>',
  'dumme_sporsmal': [],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '14',
               'tittel': 'Krav til avtaler ved netthandel',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '8',
               'tittel': 'Selgerens fulle opplysningsplikt',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '16',
               'tittel': 'Krav ved elektronisk kjøp generelt',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '18',
               'tittel': 'Bekreftelse på inngått avtale',
               'available': True}]},
 {'number': '16',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': '"Bestilling med forpliktelse til å betale" — den viktigste knappen på nett',
  'description': 'Bestillingsknappen på en nettbutikk skal være tydelig merket. Hvis ikke er du faktisk ikke bundet av '
                 'kjøpet. Slik fungerer § 16.',
  'kort_svar': 'Når du kjøper noe elektronisk, må knappen du klikker for å fullføre kjøpet være tydelig merket med '
               '"bestilling med forpliktelse til å betale" eller noe tilsvarende. Hvis selgeren ikke har gjort dette, '
               'er du ikke bundet av kjøpet — selv om du klikket. Den må også vise pris og varighet tydelig like over '
               'knappen.',
  'paragraftekst': 'Når en avtale som skal inngås elektronisk forplikter forbrukeren til å betale, skal den '
                   'næringsdrivende tydelig og i fremhevet form gjøre forbrukeren oppmerksom på opplysningene fastsatt '
                   'i § 8 første ledd bokstav a, e, og n umiddelbart før forbrukeren foretar bestillingen.\n'
                   '\n'
                   'Den næringsdrivende skal påse at forbrukeren uttrykkelig erkjenner at bestillingen medfører en '
                   'forpliktelse til å betale. Utføres bestillingen ved å aktivere en knapp eller annen funksjon, skal '
                   'knappen eller funksjonen være merket på en lett leselig måte med «bestilling med forpliktelse til '
                   'å betale» eller tilsvarende.\n'
                   '\n'
                   'Overholder ikke den næringsdrivende bestemmelsen i annet ledd, blir forbrukeren ikke bundet av '
                   'avtalen eller bestillingen.',
  'hva_betyr_html': '<p>§ 16 er en av de mektigste forbrukerbeskyttelsene i hele loven. Den krever to ting av enhver '
                    'nettbutikk eller app som tar betalt:</p>\n'
                    '<p><strong>1. Tydelig informasjon rett før kjøpet.</strong> Like før du klikker "Bestill", skal '
                    'du se tre ting på en fremhevet måte:</p>\n'
                    '<ul>\n'
                    '<li>Hva du kjøper (varens viktigste egenskaper, § 8 bokstav a)</li>\n'
                    '<li>Totalprisen inkludert avgifter og frakt (bokstav e)</li>\n'
                    '<li>Avtalens varighet og bindingstid, hvis det er et abonnement (bokstav n)</li>\n'
                    '</ul>\n'
                    '<p>Dette kan ikke gjemmes nederst på siden eller bak en lenke. Det skal stå tydelig like over '
                    'bestillingsknappen.</p>\n'
                    '<p><strong>2. Bestillingsknappen må være tydelig merket.</strong> Knappen skal si "bestilling med '
                    'forpliktelse til å betale" eller noe tilsvarende. Eksempler som godtas: "Betal nå", "Kjøp nå", '
                    '"Bestill og betal". Eksempler som IKKE godtas: "Bestill", "Send", "Fortsett", "Bekreft", '
                    '"Registrer deg".</p>\n'
                    '<p><strong>Konsekvensen av brudd er drastisk.</strong> Hvis selgeren ikke har en korrekt merket '
                    'betalingsknapp, er du ikke bundet av kjøpet. Du har ingen avtale. Du skylder ingen penger. Du har '
                    'ikke trengt å si "jeg angrer" eller bruke 14-dagers fristen — kjøpet er rett og slett ikke gyldig '
                    'fra starten.</p>\n'
                    '<p>Dette er ikke en formalitet juristene har funnet på. Det er ment å forhindre lureri der '
                    'nettbutikker bruker formuleringer som "Gå videre" eller "Registrer abonnement" for å skjule at du '
                    'faktisk forplikter deg økonomisk.</p>',
  'eksempler': [{'navn': 'Anne',
                 'tekst': 'Anne registrerer seg på et nettsted for å "prøve gratis i 7 dager". Hun fyller ut '
                          'kortinformasjon og klikker på en knapp som heter "Start prøveperioden". To uker senere ser '
                          'hun en trekk på 499 kr på kontoen. Hun sjekker bestillingsprosessen. Knappen sa "Start '
                          'prøveperioden" — ikke "bestilling med forpliktelse til å betale" eller tilsvarende. Etter § '
                          '16 tredje ledd er Anne ikke bundet av avtalen. Hun kan kreve pengene tilbake fra selgeren, '
                          'og hvis selger nekter, kan hun gjøre en tilbakeføring (chargeback) via banken sin med '
                          'henvisning til § 16.'},
                {'navn': 'Sara',
                 'tekst': 'Sara handler på en stor nettbutikk. Hun fyller handlekurven, går til kassen. Like over '
                          '"Bestill og betal"-knappen ser hun: produktbildet, prisen 1 749 kr inkludert frakt, og en '
                          'linje som sier "Engangskjøp, ingen binding". Dette oppfyller § 16. Sara har all '
                          'kjerneinformasjon rett over knappen, og knappen er tydelig merket med '
                          'betalingsforpliktelse. Hun klikker bevisst, og er bundet av avtalen.'}],
  'vanlige_feil': ['Du tror du er bundet fordi du klikket. Du er ikke bundet hvis knappen ikke var merket riktig. '
                   'Klikket alene har ikke rettslig virkning hvis selgeren brøt § 16.',
                   'Du tror "Bekreft bestilling" er nok. Det er det ikke. Ordet "bestilling" alene formidler ikke '
                   'betalingsforpliktelsen. Loven krever at det skal være klart at du forplikter deg til å betale.',
                   'Du tror dette bare gjelder for nye kunder. Nei, det gjelder hver gang du gjør en ny bestilling — '
                   'også som etablert kunde. Hvert nytt kjøp utløser kravet om en korrekt merket knapp.'],
  'hva_bor_du_html': '<p>Hvis du har "klikket ja" på noe som ikke var korrekt merket, og selgeren krever betaling: vis '
                     'til § 16 tredje ledd. Du er ikke bundet. Selgeren har ingen rettslig grunnlag for å kreve penger '
                     'fra deg.</p>\n'
                     '<p>Hvis pengene allerede er trukket fra kortet, kontakt banken din og be om tilbakeføring '
                     '(chargeback). Beskriv at selgeren brøt § 16. Bankene er som regel oppmerksomme på denne '
                     'regelen.</p>\n'
                     '<p>Når du handler på nett:</p>\n'
                     '<ul>\n'
                     '<li>Se etter en tydelig betalingsknapp — "Bestill og betal", "Kjøp nå", eller lignende</li>\n'
                     '<li>Sjekk at pris og varighet vises like over knappen</li>\n'
                     '<li>Hvis du oppdager en betalingsknapp som bare sier "Bestill" eller "Send", vær ekstra '
                     'forsiktig — det kan være et signal om at selgeren ikke følger reglene</li>\n'
                     '</ul>',
  'dumme_sporsmal': [{'q': 'Hva med abonnementer som fornyes automatisk?',
                      'a': 'Hver fornyelse skal også oppfylle § 16 ved tilstrekkelig forhåndsvarsel, men det er noe '
                           'omdiskutert. Det avgjørende er at du var korrekt informert ved den opprinnelige '
                           'bestillingen — at det var et abonnement, varigheten, prisen, og at knappen forpliktet '
                           'deg.'},
                     {'q': 'Gjelder dette også apper i App Store?',
                      'a': 'Ja. Hvert "Kjøp" i App Store skal være en bestilling med forpliktelse til å betale. Apple '
                           'bruker normalt knappen "Kjøp" eller "Få" — med Touch ID/Face ID-bekreftelse — som regel '
                           'ansett som tilstrekkelig.'},
                     {'q': 'Hva med kjøp av billett til konsert eller arrangement?',
                      'a': 'Det er fortsatt elektronisk handel der § 16 gjelder. Knappen skal være tydelig merket og '
                           'pris/varighet skal vises like over.'}],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '8',
               'tittel': 'Selgerens opplysningsplikt før kjøpet',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '14',
               'tittel': 'Krav til avtaler ved netthandel',
               'available': True},
              {'lov': 'angrerettloven', 'paragraf': '18', 'tittel': 'Bekreftelse på inngått avtale', 'available': True},
              {'lov': 'angrerettloven', 'paragraf': '20', 'tittel': 'Slik bruker du angreretten', 'available': True}]},
 {'number': '17',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Nettbutikken skal vise hvor de leverer og hvilke betalingsmidler de godtar',
  'description': 'En nettbutikk må tidlig opplyse om de leverer til ditt område og hvilke betalingsmidler de godtar – '
                 'ikke gjemme det til siste øyeblikk.',
  'kort_svar': 'Når du handler på nett, må selgeren tydelig og senest når du starter bestillingen opplyse om '
               'eventuelle leveringsbegrensninger og hvilke betalingsmåter de godtar. Det skal ikke komme som en '
               'overraskelse i kassen at de ikke leverer til Norge, eller at de bare tar Visa.',
  'paragraftekst': 'Nettsteder for elektronisk handel skal klart og tydelig og senest på det tidspunktet '
                   'bestillingsprosessen begynner, opplyse om eventuelle leveringsbegrensninger. Det skal også '
                   'opplyses om hvilke betalingsmidler som aksepteres.',
  'hva_betyr_html': '<p>§ 17 handler om to ting som ofte irriterer kunder: at man bruker tid på å handle, og så viser '
                    'det seg at selgeren ikke leverer til ens område, eller ikke tar imot ens betalingsmåte.</p>\n'
                    '<p><strong>Leveringsbegrensninger.</strong> Hvis nettbutikken ikke leverer til hele Norge, til '
                    'Svalbard, eller til utlandet, skal det stå klart. Eksempler: "Vi leverer kun til Sør-Norge", '
                    '"Ekstra frakt til Nord-Norge", "Leverer ikke til Svalbard".</p>\n'
                    '<p><strong>Betalingsmidler.</strong> Hvilke betalingsmåter godtar de? Vipps? Klarna? Visa? '
                    'Faktura? Kontoinnskudd? Dette skal være tydelig fra start.</p>\n'
                    '<p><strong>Tidspunkt:</strong> Opplysningene skal være tilgjengelige senest når '
                    'bestillingsprosessen starter. Det betyr typisk når du har lagt noe i handlekurven og begynner å '
                    'fylle ut adresse. Det er for sent å vise dette først i kassen.</p>\n'
                    '<p>Dette er en relativt mild regel — den krever bare at informasjonen er tilgjengelig, ikke at '
                    'den er sentralt plassert. Men den skal være "klar og tydelig", ikke gjemt bort.</p>',
  'eksempler': [{'navn': 'Eva',
                 'tekst': 'Eva bor på Svalbard. Hun finner en lampe hun liker på en norsk nettbutikk. Hun fyller '
                          'handlekurven, oppretter konto, taster inn adresse — og får så beskjeden: "Vi leverer ikke '
                          'til Svalbard." Etter § 17 skulle nettbutikken opplyst om dette tidligere — senest ved '
                          'bestillingens start. Hvis informasjonen var skjult eller helt fraværende, kan Eva klage til '
                          'Forbrukertilsynet. Nettbutikker som ofte unnlater dette kan få overtredelsesgebyr.'},
                {'navn': 'Lars',
                 'tekst': 'Lars vil betale et kjøp med faktura. Han bruker en time på å sette sammen en bestilling, '
                          'men da han kommer til kassen ser han at selgeren bare tar Visa og MasterCard. Han har ingen '
                          'kredittkort og må forlate kjøpet. Etter § 17 skulle dette vært tydelig fra start. Lars har '
                          'ikke "rett" på en bestemt betalingsmåte, men selgeren har plikt til å opplyse om hvilke som '
                          'finnes.'}],
  'vanlige_feil': ['Du gir opp uten å klage. Mange forlater bare kjøpet og glemmer det. Men gjentatte brudd på § 17 '
                   'kan rapporteres — det hjelper alle forbrukere på sikt.',
                   'Du tror dette gjelder bare leveringsfrist. Det gjør det ikke. § 17 handler om hvor de leverer '
                   '(geografisk) og hvilke betalingsmidler de godtar. Selve leveringsfristen er regulert i § 8.'],
  'hva_bor_du_html': '<p>Hvis du opplever en nettbutikk som gjemmer leveringsbegrensninger eller betalingsmidler:</p>\n'
                     '<ul>\n'
                     '<li>Klag til Forbrukerrådet</li>\n'
                     '<li>Vurder å bruke en konkurrent som er tydeligere</li>\n'
                     '<li>Hvis du har lagt mye tid og fortsatt vil handle, kontakt kundeservice og se om de kan finne '
                     'en løsning</li>\n'
                     '</ul>',
  'dumme_sporsmal': [],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '8',
               'tittel': 'Selgerens opplysningsplikt før kjøpet',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '14',
               'tittel': 'Krav til avtaler ved netthandel',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '16',
               'tittel': 'Bestillingsknappens utforming',
               'available': True}]},
 {'number': '18',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Bekreftelsen du skal få etter kjøpet',
  'description': 'Etter et nettkjøp skal du få en skriftlig bekreftelse på varig medium senest når varen leveres. Slik '
                 'fungerer kravet til bekreftelse.',
  'kort_svar': 'Etter at du har kjøpt noe på nett eller annen fjernkommunikasjon, har du krav på en skriftlig '
               'bekreftelse på et varig medium — typisk en e-post. Den skal komme innen rimelig tid, og senest når '
               'varen leveres eller tjenesten starter. Bekreftelsen skal inneholde all informasjonen fra § 8 hvis du '
               'ikke har fått den før.',
  'paragraftekst': 'Den næringsdrivende skal innen rimelig tid etter avtaleinngåelsen, og senest på '
                   'leveringstidspunktet for varene eller før levering av tjenesten begynner, gi forbrukeren skriftlig '
                   'bekreftelse på den inngåtte avtalen på et varig medium.\n'
                   '\n'
                   'Bekreftelsen skal inneholde opplysninger nevnt i § 8 første ledd, dersom disse ikke tidligere er '
                   'gitt forbrukeren på et varig medium, og opplysning om at forbrukeren har gitt slikt samtykke som '
                   'nevnt i § 22 bokstav n.',
  'hva_betyr_html': '<p>§ 18 sikrer at du som kjøper sitter igjen med skriftlig dokumentasjon på hva du faktisk har '
                    'kjøpt og hvilke vilkår som gjelder.</p>\n'
                    '<p><strong>Hva er en gyldig bekreftelse?</strong> Den skal være på "varig medium" — typisk '
                    'e-post, PDF, SMS eller papirbrev. En melding på "min side" som selgeren kan endre senere, er ikke '
                    'nok. Du skal kunne lagre bekreftelsen og se den i uendret form senere.</p>\n'
                    '<p><strong>Når skal den komme?</strong> Innen rimelig tid etter at avtalen ble inngått, og senest '
                    'når varen leveres eller før tjenesten begynner. For en vare betyr det at e-posten skal være i '
                    'innboksen din senest når Posten ringer på døra. For et abonnement eller en tjeneste skal du ha '
                    'bekreftelsen før første leveranse.</p>\n'
                    '<p><strong>Hva skal bekreftelsen inneholde?</strong> All informasjonen fra § 8 — pris, angrerett, '
                    'returkostnader, selgerens kontaktinformasjon og resten — hvis du ikke har fått dette tidligere på '
                    'varig medium.</p>\n'
                    '<p>Dette betyr i praksis: hvis nettbutikken bare hadde all info på nettsiden under bestillingen, '
                    'må bekreftelses-e-posten gjenta alt. Hvis nettbutikken sendte en PDF med fullstendig info under '
                    'bestillingen, kan bekreftelses-e-posten henvise til den.</p>\n'
                    '<p><strong>Spesielt for digitalt innhold (§ 22 bokstav n):</strong> Hvis du har samtykket til '
                    'umiddelbar nedlasting og dermed gitt avkall på angreretten, skal bekreftelsen vise dette tydelig. '
                    'Du skal aldri "miste" angreretten uten å bli minnet på det skriftlig.</p>',
  'eksempler': [{'navn': 'Tom',
                 'tekst': 'Tom kjøper en bok hos en norsk nettbutikk. Få sekunder etter at han har klikket "Bestill og '
                          'betal", får han en e-post: ordrebekreftelse med ordre-ID, pris, leveringsestimat, '
                          'returvilkår, angreskjema, og selgerens fulle kontaktinfo. Dette oppfyller § 18. E-posten er '
                          'varig medium, kommer innen rimelig tid, og inneholder all informasjonen Tom har krav på. '
                          'Han kan lagre den og bruke den som dokumentasjon ved en eventuell tvist.'},
                {'navn': 'Ingrid',
                 'tekst': 'Ingrid tegner et abonnement på en strømmetjeneste. Hun får en e-post som bare sier '
                          '"Velkommen! Logg inn på vår nettside for å se vilkårene." Vilkårene på nettsiden endrer seg '
                          'jevnlig. Dette oppfyller ikke § 18. Bekreftelsen skal inneholde all opplysningen i § 8 på '
                          'varig medium — eller henvise til en spesifikk versjon av vilkårene som er låst i tid. En '
                          'lenke til en nettside som selgeren kan endre, er ikke "varig medium". Ingrid kan klage og '
                          'kreve at korrekt bekreftelse sendes.'}],
  'vanlige_feil': ['Du sletter bekreftelses-e-posten. Den er din dokumentasjon. Lagre den i minst angrefristen — og '
                   'helst i hele reklamasjonsperioden (2-5 år).',
                   'Du tror at "min side" er bekreftelsen. Det er den ikke. Selgeren kan endre innholdet der. Du skal '
                   'ha en uendret kopi du selv kontrollerer.',
                   'Du tror ordrebekreftelsen er det samme som faktura. En ordrebekreftelse skal komme før eller ved '
                   'levering. Fakturaen kan komme senere. § 18 handler om bekreftelsen, ikke fakturaen.'],
  'hva_bor_du_html': '<p>Hvis du ikke får skriftlig bekreftelse innen leveringstidspunktet, har selgeren brutt § 18 — '
                     'og dermed sin opplysningsplikt under §§ 8 til 16. Dette kan forlenge angrefristen din til 12 '
                     'måneder etter § 21 tredje ledd.</p>\n'
                     '<p>Etter hvert nettkjøp:</p>\n'
                     '<ul>\n'
                     '<li>Sjekk innboksen for bekreftelses-e-post (også spam-mappen)</li>\n'
                     '<li>Lagre e-posten i en egen mappe eller stjernemerk den</li>\n'
                     '<li>Sjekk at alle nøkkelopplysninger er med: ordre-ID, pris, leveringsdato, angrerett-info, '
                     'kontaktinfo</li>\n'
                     '<li>Hvis bekreftelsen mangler eller er ufullstendig, kontakt selgeren og krev fullstendig '
                     'bekreftelse</li>\n'
                     '</ul>',
  'dumme_sporsmal': [],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '8',
               'tittel': 'Selgerens opplysningsplikt før kjøpet',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '14',
               'tittel': 'Krav til avtaler ved netthandel',
               'available': True},
              {'lov': 'angrerettloven', 'paragraf': '16', 'tittel': 'Krav til bestillingsknappen', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '22',
               'tittel': 'Når angreretten ikke gjelder',
               'available': True}]},
 {'number': '19',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Hvis du vil at en nettjeneste starter umiddelbart',
  'description': 'Vil du at en nettjeneste eller et abonnement skal starte før angrefristen er ute? Da må selger ha '
                 'din uttrykkelige aksept – ellers slipper du å betale.',
  'kort_svar': 'Hvis du har bestilt en tjeneste på nett (for eksempel et abonnement eller en konsulenttime), og du '
               'ønsker at den starter før de 14 dagene av angrefristen er ute, må selgeren ha din uttrykkelige aksept. '
               'Du må også forstå at angreretten faller bort når jobben er fullført.',
  'paragraftekst': 'Ønsker forbrukeren at levering av tjenester starter opp før utløpet av angrefristen, jf. § 21, og '
                   'avtalen innebærer en betalingsforpliktelse for forbrukeren, skal den næringsdrivende kreve at '
                   'forbrukeren uttrykkelig ber om dette. Den næringsdrivende skal også be forbrukeren om å erkjenne '
                   'at angreretten vil gå tapt når avtalen er oppfylt fullt ut av den næringsdrivende.',
  'hva_betyr_html': '<p>§ 19 er fjernsalgs-tvillingen til § 12. Reglene er nesten identiske, men § 19 gjelder når du '
                    'har kjøpt en tjeneste på nett, og § 12 gjelder når kjøpet ble gjort utenfor butikk (hjemme, '
                    'stand, telefon).</p>\n'
                    '<p><strong>Praktisk problemstilling:</strong> Du har bestilt en tjeneste online — kanskje '
                    'konsulentbistand, en kurspåmelding, en streamingtjeneste, eller en avtale med en personlig '
                    'trener. Hovedregelen er at du har 14 dagers angrerett. Men hva hvis du vil starte med en '
                    'gang?</p>\n'
                    '<p><strong>Slik må selger gjøre det:</strong></p>\n'
                    '<ol>\n'
                    '<li>Få din uttrykkelige aksept for at tjenesten skal starte før angrefristen er ute. '
                    '"Uttrykkelig" betyr at det må være en bevisst handling — en haket av boks, en signatur, et '
                    '"ja"-svar på spørsmål.</li>\n'
                    '<li>Be deg om å bekrefte at du forstår at angreretten går tapt når jobben er fullført.</li>\n'
                    '</ol>\n'
                    '<p><strong>Hva skjer hvis du angrer underveis?</strong> Hvis tjenesten har startet men ikke er '
                    'ferdig, har du fortsatt angrerett. Men du må betale en forholdsmessig andel for det som er levert '
                    '(etter § 26). Hvis hele jobben er ferdig, er angreretten borte.</p>\n'
                    '<p>Hvis selger ikke følger reglene — for eksempel ikke ber om uttrykkelig aksept eller ikke '
                    'informerer om tap av angrerett — slipper du å betale for det som er levert (§ 26 andre ledd).</p>',
  'eksempler': [{'navn': 'Petter',
                 'tekst': 'Petter tegner et abonnement på en strømmetjeneste til 129 kr per måned. Når han bestiller, '
                          'må han hake av en boks: "Jeg ønsker at tjenesten skal starte umiddelbart og forstår at '
                          'angreretten faller bort hvis jeg har brukt tjenesten fullt ut." Han haker av og begynner å '
                          'se filmer samme kveld. Etter ti dager bestemmer han seg for å si opp. Han har fortsatt '
                          'angrerett siden tjenesten er løpende og ikke "fullt ut levert". Men han må betale for de ti '
                          'dagene han har brukt — beregnet forholdsmessig etter § 26.'},
                {'navn': 'Sara',
                 'tekst': 'Sara bestiller en konsulenttime online for 1 500 kr. Konsulenten sender en mail: "Når '
                          'passer det at vi tar timen?" Sara svarer "i morgen kl 14". Konsulenten gjennomfører timen. '
                          'To dager etter ombestemmer Sara seg og krever pengene tilbake under angrefristen. '
                          'Konsulenten sier "jeg har jo brukt en time på deg". Men selgeren ba aldri Sara om '
                          'uttrykkelig aksept for å starte før angrefristen var ute, og fortalte heller ikke at '
                          'angreretten ville gå tapt. Etter § 26 andre ledd slipper Sara å betale for det som er '
                          'levert. Hun kan kreve hele beløpet refundert.'}],
  'vanlige_feil': ['Selger antar at bestillingen i seg selv er en aksept for umiddelbar oppstart. Det er den ikke. '
                   'Aksepten skal være uttrykkelig og separat.',
                   'Selger glemmer å informere om tap av angrerett. Da kan kunden angre og slippe å betale, selv om '
                   'tjenesten er utført.',
                   'Du tror at fordi du brukte tjenesten, kan du ikke angre. Du kan fortsatt angre — men du må kanskje '
                   'betale en forholdsmessig andel etter § 26. Du har likevel rett til å trekke deg fra resten.'],
  'hva_bor_du_html': '<p>Når du bestiller en tjeneste online:</p>\n'
                     '<ul>\n'
                     '<li>Sjekk om det er en haket av boks om "oppstart før angrefristen er ute" — vær bevisst hva du '
                     'samtykker til</li>\n'
                     '<li>Hvis du vil ha 14 dager til å tenke deg om, ikke samtykke til umiddelbar oppstart</li>\n'
                     '<li>Hvis du angrer underveis, send angremelding raskt — så slipper du å betale for unødvendig '
                     'mye</li>\n'
                     '<li>Hvis selger ikke fulgte reglene (ingen uttrykkelig aksept, ingen info om tap av angrerett), '
                     'vis til § 19 og § 26 andre ledd</li>\n'
                     '</ul>',
  'dumme_sporsmal': [],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '12',
               'tittel': 'Tilsvarende regel ved hjemmesalg',
               'available': True},
              {'lov': 'angrerettloven', 'paragraf': '21', 'tittel': 'Angrefristen på 14 dager', 'available': True},
              {'lov': 'angrerettloven', 'paragraf': '22', 'tittel': 'Når angreretten ikke gjelder', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '26',
               'tittel': 'Forbrukerens forpliktelser ved tjenester',
               'available': True}]},
 {'number': '20',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Slik bruker du angreretten',
  'description': 'Hvordan angrer du et kjøp i praksis? Du sender en melding før fristen utløper – via angreskjema '
                 'eller annen tydelig erklæring. Slik gjør du det riktig.',
  'kort_svar': 'For å angre et kjøp må du sende en melding til selgeren før angrefristen utløper. Det holder at '
               'meldingen er sendt — den trenger ikke å være mottatt før fristen. Du kan bruke det offisielle '
               'angreskjemaet, eller bare skrive en tydelig melding selv. Hvis du sender elektronisk, skal selger '
               'bekrefte mottak. Det er du selv som må bevise at meldingen er sendt.',
  'paragraftekst': 'Forbrukeren har rett til å gå fra avtalen (angrerett) ved å gi melding til den næringsdrivende før '
                   'utløpet av angrefristen, jf. § 21. Angrefristen anses overholdt dersom melding er sendt før '
                   'utløpet av fristen.\n'
                   '\n'
                   'Meldingen kan fremsettes ved bruk av utfylt angreskjema eller ved fremsettelse av annen utvetydig '
                   'erklæring.\n'
                   '\n'
                   'Dersom den næringsdrivende gir forbrukeren adgang til å gi melding etter annet ledd elektronisk, '
                   'skal den næringsdrivende umiddelbart bekrefte på et varig medium at meldingen er mottatt.\n'
                   '\n'
                   'Bevisbyrden for at melding er gitt, påhviler forbrukeren.',
  'hva_betyr_html': '<p>§ 20 forklarer den praktiske prosedyren for å angre et kjøp. Det er enklere enn mange tror — '
                    'men du må gjøre det riktig.</p>\n'
                    '<p><strong>Du må sende en melding.</strong> Det er ikke nok å bare returnere varen, eller å la '
                    'være å betale, eller å snakke med en kunde&shy;behandler. Du må sende en konkret melding der det '
                    'er klart at du angrer.</p>\n'
                    '<p><strong>Fristen overholdes ved sending.</strong> Hvis du sender meldingen klokken 23.45 på dag '
                    '14, er du innenfor — selv om selgeren ikke åpner e-posten før neste morgen. Det er '
                    'sendetidspunktet som teller, ikke når selgeren mottar eller behandler meldingen.</p>\n'
                    '<p><strong>To måter å sende på:</strong></p>\n'
                    '<ol>\n'
                    '<li><strong>Det offisielle angreskjemaet.</strong> Selgeren skal ha gitt deg dette ved kjøpet (se '
                    '§ 8 bokstav h). Det er et standardisert skjema med felter for navn, ordrenummer, dato og '
                    'signatur. Fyll det ut og send.</li>\n'
                    '<li><strong>Annen utvetydig erklæring.</strong> Du trenger ikke å bruke skjemaet. En e-post som '
                    'tydelig sier "Jeg angrer på kjøpet av X, ordrenummer Y" holder. Det viktige er at meldingen er '
                    'klar. Skriv ikke "jeg vurderer å returnere" — skriv "jeg angrer".</li>\n'
                    '</ol>\n'
                    '<p><strong>Elektronisk angring krever bekreftelse.</strong> Hvis selgeren tilbyr en elektronisk '
                    'angreknapp eller skjema på nettsiden, skal de umiddelbart sende deg en bekreftelse på varig '
                    'medium om at meldingen er mottatt. Hvis du sender via e-post og ikke får bekreftelse, ta vare på '
                    'din sendte e-post som dokumentasjon.</p>\n'
                    '<p><strong>Du har bevisbyrden.</strong> Det er du som må kunne dokumentere at meldingen ble sendt '
                    'før fristen. Dette er motsatt av selgerens opplysningsplikt under § 7. Derfor: send via en kanal '
                    'som etterlater spor — e-post, SMS, signert brev — ikke en telefonsamtale.</p>',
  'eksempler': [{'navn': 'Anne',
                 'tekst': 'Anne kjøpte sko fra Zalando på en mandag og mottok dem onsdag. To uker senere bestemmer hun '
                          'seg for å returnere. Dag 14 nærmer seg. Hun går inn på Zalandos returside, fyller ut '
                          'returskjemaet, og får umiddelbart en e-post: "Vi har mottatt din returforespørsel for ordre '
                          '#1234, datert 22. januar 2026." Hun pakker skoene og sender dem dagen etter. Anne har gjort '
                          'alt riktig. Hun sendte melding før fristen, fikk bekreftelse på varig medium, og har '
                          'e-posten som dokumentasjon hvis det blir tvist.'},
                {'navn': 'Lars',
                 'tekst': 'Lars kjøpte en jakke for 2 400 kr på en nettbutikk han ikke har handlet hos før. Han '
                          'bestemmer seg for å angre. Han ringer kundeservice og sier "jeg vil returnere jakken". '
                          'Kundebehandleren svarer "ok, send den til adressen som står på pakken". To uker senere får '
                          'Lars en faktura. Selgeren hevder han aldri angret. Lars kan vise til at han ringte, men han '
                          'har ingen dokumentasjon på samtalen. Etter § 20 fjerde ledd er det Lars som må bevise at '
                          'meldingen ble sendt. Hvis han hadde sendt en e-post i stedet — selv en kort en — hadde han '
                          'hatt dokumentasjon. Lars taper sannsynligvis tvisten.'}],
  'vanlige_feil': ['Du ringer i stedet for å skrive. Telefon er praktisk, men etterlater ingen dokumentasjon. Skriv '
                   'heller — alltid.',
                   'Du venter til siste dag. Selv om fristen overholdes ved sending, gir du deg selv null buffer hvis '
                   'noe går galt med utsendingen. Send heller noen dager før.',
                   'Du formulerer deg utydelig. "Jeg vurderer å returnere" eller "kan jeg returnere?" er ikke '
                   'utvetydig. Skriv direkte: "Jeg angrer på kjøpet av X, ordrenummer Y. Vennligst bekreft mottak."',
                   'Du bruker selgerens chat uten å sjekke om de bekrefter på varig medium. En chatlogg som forsvinner '
                   'etter samtalen er ikke godt nok.'],
  'hva_bor_du_html': '<p>Når du skal angre:</p>\n'
                     '<ul>\n'
                     '<li>Skriv en kort, tydelig melding: "Jeg angrer på kjøpet av X (ordrenummer Y) gjort dato Z. '
                     'Vennligst bekreft mottak."</li>\n'
                     '<li>Send via e-post — det gir deg dokumentasjon i form av sendt-mappen</li>\n'
                     '<li>Lagre eventuell bekreftelse fra selgeren</li>\n'
                     '<li>Pakk varen og send den tilbake innen 14 dager etter at du angret (§ 25)</li>\n'
                     '<li>Ta vare på sendingskvitteringen fra Posten eller annen transportør</li>\n'
                     '</ul>',
  'dumme_sporsmal': [{'q': 'Må jeg forklare hvorfor jeg angrer?',
                      'a': 'Nei. Du trenger ikke gi noen begrunnelse. Det er nettopp poenget med angreretten — du kan '
                           'ombestemme deg uten å forklare deg.'},
                     {'q': 'Kan selgeren nekte angre?',
                      'a': 'Ikke hvis kjøpet er omfattet av angrerettloven og du er innenfor fristen. Selgeren kan be '
                           'om informasjon for å behandle saken (ordrenummer osv.), men ikke nekte. Hvis de nekter, '
                           'klag til Forbrukerrådet.'},
                     {'q': 'Hva hvis selger ikke har angreskjema?',
                      'a': 'Da kan du fortsatt angre med en utvetydig erklæring (e-post). Du har også krav på utvidet '
                           'frist på 12 måneder etter § 21 tredje ledd, fordi selgeren har brutt opplysningsplikten i '
                           '§ 8.'},
                     {'q': 'Kan jeg angre på deler av kjøpet?',
                      'a': 'Ja. Hvis du har kjøpt flere ting i samme bestilling, kan du angre på noen og beholde '
                           'andre. Spesifiser tydelig hvilke varer du angrer på.'}],
  'related': [{'lov': 'angrerettloven', 'paragraf': '21', 'tittel': 'Angrefristen på 14 dager', 'available': True},
              {'lov': 'angrerettloven', 'paragraf': '22', 'tittel': 'Når angreretten ikke gjelder', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '24',
               'tittel': 'Selgerens plikter når du angrer',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '25',
               'tittel': 'Forbrukerens forpliktelser ved retur',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '26',
               'tittel': 'Forbrukerens forpliktelser ved tjenester',
               'available': True}]},
 {'number': '21',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Når starter angrefristen og hvor lenge varer den?',
  'description': 'Hvor lang er angrefristen og når starter den? 14 dager fra varen er mottatt eller avtalen inngått – '
                 'pluss spesialregler for flere leveranser.',
  'kort_svar': 'Angrefristen er 14 dager. Ved kjøp av varer starter den dagen du mottar varen. Ved kjøp av tjenester '
               'starter den dagen avtalen ble inngått. Hvis selgeren ikke har gitt deg informasjon om angreretten, '
               'forlenges fristen til 12 måneder. Får du info senere, har du 14 dager fra da.',
  'paragraftekst': 'Angrefristen utløper 14 dager fra den dag avtalen om tjeneste ble inngått, eller den dag '
                   'forbrukeren får varen i fysisk besittelse. Dette er:\n'
                   'a. ved varer bestilt samlet og levert ved flere forsendelser, den dag forbrukeren får den siste '
                   'varen i fysisk besittelse,\n'
                   'b. ved varer som består av flere partier eller deler, den dag forbrukeren får det siste partiet '
                   'eller den siste delen i fysisk besittelse,\n'
                   'c. ved avtaler om regelmessig levering av varer, den dag forbrukeren får den første av varene i '
                   'fysisk besittelse.\n'
                   '\n'
                   'Likt med forbrukeren regnes annen tredjeperson enn fraktføreren, som forbrukeren har utpekt i sitt '
                   'sted.\n'
                   '\n'
                   'Gir ikke den næringsdrivende forbrukeren opplysninger om angreretten i henhold til § 8 første ledd '
                   'bokstav h, utløper angrefristen 12 måneder etter utløpet av den opprinnelige angrefristen, jf. '
                   'første ledd.\n'
                   '\n'
                   'Dersom den næringsdrivende gir forbrukeren opplysninger om angreretten etter § 8 første ledd '
                   'bokstav h innen 12 måneder fra dagen omhandlet i første ledd, utløper angrefristen 14 dager etter '
                   'den dagen forbrukeren mottok opplysningene.',
  'hva_betyr_html': '<p>§ 21 forteller hvor lang fristen er og fra hvilken dag den teller.</p>\n'
                    '<p><strong>Hovedregel: 14 dager.</strong></p>\n'
                    '<p><strong>Når starter klokken?</strong></p>\n'
                    '<p>For tjenester: dagen avtalen ble inngått. For et nettkjøp betyr det vanligvis dagen du klikket '
                    '"Bestill og betal".</p>\n'
                    '<p>For varer: dagen du fikk varen i fysisk besittelse. Det er ikke ordrebekreftelse, ikke '
                    'utsendelse, ikke leveringstidspunktet for posten — det er dagen du selv (eller noen på dine '
                    'vegne) tok imot pakken.</p>\n'
                    '<p><strong>Spesialregler for ulike leveranser:</strong></p>\n'
                    '<ul>\n'
                    '<li><strong>a) Bestilt sammen, levert i flere forsendelser.</strong> Du bestiller sofa og bord '
                    'samtidig. Sofaen kommer mandag, bordet onsdag. Fristen starter onsdag — etter siste vare.</li>\n'
                    '<li><strong>b) En vare i flere deler.</strong> En seng som leveres i tre eller fire pakker. '
                    'Fristen starter når siste pakke er kommet.</li>\n'
                    '<li><strong>c) Abonnement med regelmessig levering.</strong> En fruktboks som kommer hver uke. '
                    'Fristen starter når første leveranse kommer.</li>\n'
                    '</ul>\n'
                    '<p><strong>Andre på dine vegne.</strong> Hvis du har bedt noen andre — for eksempel en nabo — om '
                    'å ta imot pakken, regnes den som mottatt av deg samtidig. Men dette gjelder ikke fraktføreren '
                    'selv (Posten, Bring, osv.). Pakken er ikke "mottatt" bare fordi Bring har den på terminalen.</p>\n'
                    '<p><strong>Utvidet frist hvis selger ikke informerte:</strong></p>\n'
                    '<p>Dette er en kraftig sanksjon. Hvis selgeren ikke har gitt deg informasjon om angreretten etter '
                    '§ 8 bokstav h — altså ikke har sagt at angrerett finnes, eller ikke gitt deg angreskjema — '
                    'forlenges fristen din til 14 dager pluss 12 måneder.</p>\n'
                    '<p>Hvis selgeren retter opp og gir deg informasjonen innen disse 12 månedene, "resettes" fristen '
                    'til 14 dager fra du fikk informasjonen.</p>',
  'eksempler': [{'navn': 'Anne',
                 'tekst': 'Anne kjøper sko fra Zalando. Skoene leveres på en mandag. Mandagen teller ikke (etter § 6 '
                          'om fristberegning) — dag 1 er tirsdag. Dag 14 er mandagen to uker senere. Hun har angrerett '
                          'til og med den mandagen.'},
                {'navn': 'Lars',
                 'tekst': 'Lars kjøper et stort møbelsett: et sofabord og en sofa. Sofabordet kommer onsdag, sofaen '
                          'først to uker senere på en torsdag. Etter § 21 første ledd bokstav a starter fristen fra '
                          'siste varen er mottatt — altså torsdagen. Han har 14 dager fra da, ikke fra første '
                          'leveranse.'},
                {'navn': 'Eva',
                 'tekst': 'Eva kjøper en lampe fra en utenlandsk nettbutikk for 1 400 kr. Det er ingen informasjon om '
                          'angrerett verken i bestillingen eller i bekreftelses-e-posten. Tre måneder senere '
                          'ombestemmer hun seg og vil returnere. Hun er innenfor. Etter § 21 tredje ledd er '
                          'angrefristen utvidet til 12 måneder pluss 14 dager fordi selgeren brøt opplysningsplikten i '
                          '§ 8 bokstav h. Eva sender angremelding og krever pengene tilbake.'}],
  'vanlige_feil': ['Du tror fristen starter når selgeren sendte varen. Den starter når du mottok den. Tregt utsendelse '
                   'hos selgeren gir deg ikke kortere frist.',
                   'Du tror "Bring har varen min" betyr at den er mottatt. Det gjør det ikke. Varen må være i din '
                   'fysiske besittelse — på dørmatten, i hånda di, eller hos en utpekt person (ikke transportøren).',
                   'Du tror selger kan korte ned fristen i vilkårene. Det kan de ikke (se § 3). 14 dager er minimum.',
                   'Du tror "12 måneder" gjelder uansett. Den gjelder bare når selgeren ikke har informert om '
                   'angreretten. Hvis selgeren sendte korrekt informasjon, er fristen 14 dager.'],
  'hva_bor_du_html': '<p>Når du har kjøpt noe:</p>\n'
                     '<ul>\n'
                     '<li>Noter dato for mottak — det er starten på fristen</li>\n'
                     '<li>Sett en kalenderpåminnelse for dag 10-12 så du har god tid</li>\n'
                     '<li>Hvis du ikke fikk angrerett-info ved kjøpet, vit at fristen din kan være 12 måneder — du har '
                     'god tid å områ deg</li>\n'
                     '</ul>',
  'dumme_sporsmal': [{'q': 'Hva hvis Posten leverte til naboen uten min tillatelse?',
                      'a': 'Da er varen ikke "mottatt" av deg ennå. Fristen starter når du selv overtar varen. Si fra '
                           'til Posten — leveringen til en uautorisert tredjepart er deres feil, ikke din.'},
                     {'q': 'Hva med Pakkebokser hos Posten?',
                      'a': 'Når varen ligger i pakkeboksen og er klar til avhenting, er den i din rådighet. Mange '
                           'tolker det som "mottatt". For å være sikker: ikke vent unødig lenge med å hente — fristen '
                           'kan starte fra første tilgjengelige dag.'},
                     {'q': 'Hva regnes som "info om angreretten" fra selgeren?',
                      'a': 'Det skal være tydelig informasjon om at angrerett finnes, hvor lang fristen er, hvordan du '
                           'angrer, og et standardisert angreskjema. Småtekst nederst på en faktura er sjelden nok.'}],
  'related': [{'lov': 'angrerettloven', 'paragraf': '6', 'tittel': 'Slik regnes dagene i fristen', 'available': True},
              {'lov': 'angrerettloven', 'paragraf': '20', 'tittel': 'Slik bruker du angreretten', 'available': True},
              {'lov': 'angrerettloven', 'paragraf': '22', 'tittel': 'Når angreretten ikke gjelder', 'available': True},
              {'lov': 'angrerettloven', 'paragraf': '8', 'tittel': 'Selgerens opplysningsplikt', 'available': True}]},
 {'number': '22',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Når du IKKE har angrerett',
  'description': 'Når har du IKKE angrerett? De 14 unntakene fra angrerettloven – fra spesiallagde varer og mat til '
                 'hotellrom og digitalt innhold du har lastet ned.',
  'kort_svar': 'Selv om angrerettloven gjelder for kjøpet ditt, har du ikke angrerett i 14 spesifikke tilfeller. De '
               'viktigste: spesiallagde varer, mat og lett bedervelige varer, åpnede hygieneprodukter, åpnede '
               'CD/programvare, hotell/transport/bilutleie/catering med bestemt dato, og digitalt innhold du har '
               'samtykket til å laste ned umiddelbart.',
  'paragraftekst': 'Angreretten gjelder ikke avtaler om:\n'
                   'a. levering av varer som på grunn av sin art blandes med andre varer etter levering på en slik '
                   'måte at de ikke kan skilles fra hverandre,\n'
                   'b. levering av varer som forringes eller raskt går ut på dato,\n'
                   'c. tjeneste som er levert fullt ut [...]\n'
                   'd. levering av varer eller tjenester der prisen er avhengig av svingninger i finansmarkedet [...]\n'
                   'e. levering av varer som er fremstilt etter forbrukerens spesifikasjoner, eller som har fått et '
                   'tydelig personlig preg,\n'
                   'f. levering av legemidler [...] og medisinsk utstyr,\n'
                   'g. levering av forseglede varer som av hensyn til helsevern eller hygiene ikke er egnet for retur, '
                   'og der forseglingen er blitt brutt etter levering,\n'
                   'h. levering av alkoholholdige drikker til en pris som ble avtalt på avtaletidspunktet [...]\n'
                   'i. reparasjoner eller tjenester som det haster å få utført der forbrukeren uttrykkelig ber den '
                   'næringsdrivende om å besøke forbrukeren [...]\n'
                   'j. levering av forseglede lyd- eller bildeopptak eller forseglet programvare som forbrukeren har '
                   'brutt forseglingen på,\n'
                   'k. levering av en avis, et tidsskrift eller et magasin, med unntak av abonnementsavtaler [...]\n'
                   'l. varer eller tjenester som er inngått ved offentlig auksjon,\n'
                   'm. levering av innkvarteringstjenester for andre formål enn boligformål, transport av varer, '
                   'bilutleietjenester, catering og tjenester knyttet til fritidsaktiviteter når det i avtalen er '
                   'fastsatt en bestemt dato eller et bestemt tidsrom,\n'
                   'n. levering av digitalt innhold som ikke leveres på et fysisk medium, dersom leveringen er begynt '
                   'og forbrukeren har samtykket [...]\n'
                   '\n'
                   'Unntakene fra angreretten i første ledd bokstavene c og e gjelder ikke ved uanmodet dørsalg.\n'
                   '\n'
                   '(Se Lovdata for fullstendig lovtekst.)',
  'hva_betyr_html': '<p>§ 22 er der mange forbrukere blir overrasket. Selv om kjøpet ditt i utgangspunktet er omfattet '
                    'av loven, finnes det 14 unntak der angrerett ikke gjelder. Vi grupperer dem etter logikk:</p>\n'
                    '<h3>Varer som ikke kan returneres på grunn av sin natur (a, b, e)</h3>\n'
                    '<ul>\n'
                    '<li><strong>a)</strong> Varer som blandes med andre etter levering — for eksempel en '
                    'betongleveranse som tømmes i et fundament, eller maling som blandes på stedet</li>\n'
                    '<li><strong>b)</strong> Lett bedervelige varer — melk, kjøtt, fisk, frukt, ferdigmat</li>\n'
                    '<li><strong>e)</strong> Spesiallagde varer eller varer med personlig preg — mål-laget gardin, '
                    'gravert smykke, t-skjorte med eget design</li>\n'
                    '</ul>\n'
                    '<h3>Tjenester og digitalt innhold som er levert (c, n)</h3>\n'
                    '<ul>\n'
                    '<li><strong>c)</strong> Tjeneste som er fullt ut levert — men kun hvis du på forhånd har '
                    'samtykket til at den skulle starte, og bekreftet at du forstår at angreretten faller bort (se § '
                    '12 og § 19)</li>\n'
                    '<li><strong>n)</strong> Digitalt innhold som er levert — Netflix-filmer du har sett, en e-bok du '
                    'har lastet ned, programvare som er installert. Krever ditt uttrykkelige samtykke til oppstart, '
                    'erkjennelse av tap av angrerett, og bekreftelse fra selger</li>\n'
                    '</ul>\n'
                    '<h3>Markedsavhengige priser (d, h)</h3>\n'
                    '<ul>\n'
                    '<li><strong>d)</strong> Pris avhenger av finansmarkedet — aksjer, fond, valutahandel</li>\n'
                    '<li><strong>h)</strong> Alkohol bestilt nå, levert om 30+ dager, med markedsavhengig verdi — '
                    'typisk vininvestering eller vin på terminhandel</li>\n'
                    '</ul>\n'
                    '<h3>Helse, hygiene og forsegling (f, g, j)</h3>\n'
                    '<ul>\n'
                    '<li><strong>f)</strong> Legemidler og medisinsk utstyr — gjelder all reseptfri og reseptpliktig '
                    'medisin</li>\n'
                    '<li><strong>g)</strong> Hygienevarer der forseglingen er brutt — kontaktlinser, parfymer, '
                    'kosmetikk, undertøy. Ubrutt forsegling = du har fortsatt angrerett. Brutt forsegling = ingen '
                    'angrerett</li>\n'
                    '<li><strong>j)</strong> Lyd- og videoopptak og programvare med brutt forsegling — CD-er, DVD-er, '
                    'fysiske spill med plastfolie</li>\n'
                    '</ul>\n'
                    '<h3>Hastetjenester (i)</h3>\n'
                    '<ul>\n'
                    '<li><strong>i)</strong> Akutte reparasjoner hjemme hos deg, som du har bedt om — rørlegger som '
                    'kommer for å fikse vannlekkasje. Tilleggsvarer eller tilleggstjenester som ikke var akutte, er '
                    'IKKE unntatt</li>\n'
                    '</ul>\n'
                    '<h3>Spesielle salgsformer (k, l)</h3>\n'
                    '<ul>\n'
                    '<li><strong>k)</strong> Enkeltutgave av avis, tidsskrift eller magasin — men ikke abonnementer! '
                    'Et magasinabonnement har normal angrerett</li>\n'
                    '<li><strong>l)</strong> Offentlig auksjon — klassisk auksjon med auksjonarius (Blomqvist, kunst). '
                    'Nettauksjoner regnes ikke som "offentlig auksjon"</li>\n'
                    '</ul>\n'
                    '<h3>Tjenester med bestemt dato (m)</h3>\n'
                    '<ul>\n'
                    '<li><strong>m)</strong> Hotell (ikke bolig), transport av varer, bilutleie, catering, '
                    'fritidsaktiviteter — når det er avtalt en bestemt dato eller et bestemt tidsrom. Bestiller du '
                    'hotell for neste lørdag eller restaurantbord til en konkret kveld: ingen angrerett</li>\n'
                    '</ul>\n'
                    '<h3>Spesialregel om dørsalg</h3>\n'
                    '<p>Hvis selgeren kom på døra di uoppfordret, faller unntakene c og e bort. Det betyr at '
                    'spesiallagde varer eller fullført tjeneste fortsatt gir deg angrerett ved uanmodet dørsalg. Loven '
                    'gir ekstra beskyttelse mot push-salg på døra.</p>',
  'eksempler': [{'navn': 'Sara',
                 'tekst': 'Sara bestiller en t-skjorte med eget design og initialene "S.M." trykt på. Hun ombestemmer '
                          'seg dagen etter og vil angre. Selgeren kan nekte. Etter § 22 bokstav e er varer med tydelig '
                          'personlig preg unntatt fra angrerett. Sara har ikke rett til å returnere.'},
                {'navn': 'Petter',
                 'tekst': 'Petter bestiller hotellrom i Bergen for spesifikk dato — fredag 14. mars. To dager senere '
                          'ombestemmer han seg. Hotellet kan nekte. Etter § 22 bokstav m er hotelltjenester med '
                          'bestemt dato unntatt fra angrerett. Han er bundet av reservasjonen (med mindre hotellet har '
                          'egne avbestillingsregler som er mer gunstige).'},
                {'navn': 'Tom',
                 'tekst': 'Tom kjøper en parfyme på nett for 800 kr. Når den kommer, åpner han forseglingen for å '
                          'teste. Han liker ikke duften og vil returnere. Selger kan nekte. Etter § 22 bokstav g er '
                          'hygienevarer med brutt forsegling unntatt. Hadde Tom latt forseglingen være i fred, hadde '
                          'han fortsatt hatt angrerett. Lærdom: lukt på flasken først hvis du tar sjansen, men ikke '
                          'åpne.'},
                {'navn': 'Anne',
                 'tekst': 'Anne tegner et Netflix-abonnement og haker av "Start tjenesten umiddelbart, jeg forstår at '
                          'angreretten faller bort når jeg har brukt tjenesten". Hun ser tre filmer. Etter en uke vil '
                          'hun si opp og kreve penger tilbake for første måned. Hun kan si opp, men ikke kreve full '
                          'refusjon. Hennes umiddelbare bruk og samtykke aktiverer unntaket i bokstav n for det '
                          'digitale innholdet hun allerede har konsumert.'}],
  'vanlige_feil': ['Du tror "spesiallaget" betyr "spesielt bestilt". Det gjør det ikke. En vare må være laget etter '
                   'dine spesifikasjoner eller ha tydelig personlig preg. En standard rød jakke i størrelse M er ikke '
                   '"spesiallaget" bare fordi du bestilte den.',
                   'Du tror forsegling betyr "innpakket". Det betyr en faktisk forsegling — et plastsegl, en '
                   'sikkerhetslukker, en plastfolie som må brytes. Et papplokk eller en eskelukker er sjelden '
                   '"forsegling" i lovens forstand.',
                   'Du tror digitalt innhold = ingen angrerett. Ikke automatisk. Du må ha samtykket til umiddelbar '
                   'oppstart OG erkjent at angreretten går tapt OG selgeren må ha gitt bekreftelse. Hvis ett av disse '
                   'mangler, har du fortsatt angrerett.',
                   'Du tror et abonnement på et magasin er unntatt. Det er det ikke. Bokstav k unntar enkeltutgaver, '
                   'ikke abonnementer.'],
  'hva_bor_du_html': '<p>Før du kjøper noe på nett:</p>\n'
                     '<ul>\n'
                     '<li>Tenk gjennom om varen er spesiallaget, har personlig preg, eller har en forsegling som må '
                     'brytes</li>\n'
                     '<li>Hvis du er usikker på om du vil beholde, ikke åpne forseglede hygienevarer eller programvare '
                     'før du har bestemt deg</li>\n'
                     '<li>Ved hotell, bilutleie, catering med bestemt dato: sjekk avbestillingsvilkårene før du '
                     'bestiller</li>\n'
                     '<li>Ved digitalt innhold: les nøye hva du samtykker til. "Start umiddelbart" kan koste deg '
                     'angreretten</li>\n'
                     '</ul>',
  'dumme_sporsmal': [{'q': 'Hvorfor er det ingen angrerett på t-skjorter med trykk?',
                      'a': 'Fordi selgeren ikke kan selge produktet videre — det er personlig tilpasset. Det er en '
                           'lovlig konsekvens av at varen ikke har verdi for andre.'},
                     {'q': 'Kan jeg angre på Spotify Premium?',
                      'a': 'Avhengig av om du har "lyttet" eller ikke. Hvis du ved bestilling samtykket til umiddelbar '
                           'oppstart og har brukt tjenesten, gjelder unntaket i bokstav n. Mange digitale tjenester '
                           'har likevel egne åpne avbestillingsregler.'},
                     {'q': 'Hva med "skreddersydde" anbefalinger eller pakker?',
                      'a': 'Det er ikke det samme som personlig pregede varer. Hvis du bestiller en standardvare som '
                           'selgeren plukker ut basert på din profil, er den ikke "fremstilt etter dine '
                           'spesifikasjoner". Du har angrerett.'},
                     {'q': 'Kan en selger bare skrive "ingen angrerett" på alt?',
                      'a': 'Nei. Selgeren må vise at kjøpet faktisk faller inn under et av unntakene i § 22. En '
                           'generell "ingen angrerett"-klausul er ugyldig etter § 3.'}],
  'related': [{'lov': 'angrerettloven', 'paragraf': '1', 'tittel': 'Hvilke kjøp loven gjelder for', 'available': True},
              {'lov': 'angrerettloven', 'paragraf': '2', 'tittel': 'Når loven helt ikke gjelder', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '19',
               'tittel': 'Samtykke til umiddelbar oppstart av tjeneste',
               'available': True},
              {'lov': 'angrerettloven', 'paragraf': '21', 'tittel': 'Angrefristen på 14 dager', 'available': True}]},
 {'number': '23',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Hva skjer juridisk når du angrer',
  'description': 'Hva skjer egentlig når du angrer et kjøp? Avtalen oppheves, og begge parter må gjøre opp. Slik '
                 'fungerer virkningene av angreretten i § 23.',
  'kort_svar': 'Når du bruker angreretten, faller hele avtalen bort. Du må sende varen tilbake (§ 25) og selgeren må '
               'betale tilbake pengene (§ 24). Hvis du bare har gitt et tilbud men ikke fått aksept ennå, faller '
               'tilbudet bort.',
  'paragraftekst': 'Ved bruk av angreretten bortfaller partenes forpliktelser til å oppfylle avtalen. I tilfeller der '
                   'forbrukeren har gitt et tilbud, bortfaller tilbudet.',
  'hva_betyr_html': '<p>§ 23 er kort, men viktig. Den fastslår selve konsekvensen av at du angrer.</p>\n'
                    '<p><strong>Avtalen oppheves.</strong> Når du bruker angreretten, opphører avtalen mellom deg og '
                    'selgeren. Det er som om dere aldri inngikk den. Det er ikke en oppsigelse for fremtiden — det er '
                    'en oppheving av hele avtaleforholdet.</p>\n'
                    '<p><strong>Begge parters plikter faller bort.</strong> Selgeren slipper å levere mer. Du slipper '
                    'å betale mer. Det dere allerede har gjort, må reverseres: du sender varen tilbake, selgeren '
                    'betaler tilbake pengene.</p>\n'
                    '<p><strong>Hvis du bare hadde gitt et tilbud.</strong> Noen ganger har du ikke inngått selve '
                    'avtalen ennå — du har bare gitt et tilbud som selgeren ennå ikke har akseptert formelt. I så fall '
                    'trekker du tilbudet ditt tilbake. Selgeren kan ikke senere "akseptere" det.</p>\n'
                    '<p>Detaljene om hvordan oppgjøret skal skje praktisk, står i § 24 (selgerens plikter) og § 25 '
                    '(dine plikter). Hvis det fantes tilknyttede avtaler — for eksempel en mobilforsikring tilknyttet '
                    'et telefonkjøp — faller også de bort (§ 27).</p>',
  'eksempler': [{'navn': 'Anne',
                 'tekst': 'Anne kjøper en stol fra en nettbutikk for 2 400 kr. Etter 10 dager bestemmer hun seg for å '
                          'angre. Hun sender angremeldingen. Etter § 23 er avtalen oppløst. Anne har ikke lenger '
                          'forpliktelse til å beholde stolen, og selger har ikke lenger krav på pengene. Resultatet: '
                          'hun pakker stolen og sender den tilbake (§ 25), og selgeren betaler tilbake hele beløpet (§ '
                          '24).'},
                {'navn': 'Lars',
                 'tekst': 'Lars har gått inn på en nettside og lagt inn et tilbud på en spesialvare som krever '
                          'selgerens godkjenning. Selgeren har ikke svart ennå da Lars ombestemmer seg. Etter § 23 '
                          'andre punktum bortfaller tilbudet hans. Selgeren kan ikke nå dukke opp tre dager senere og '
                          'si "vi godtar tilbudet, du må betale". Lars er fri.'}],
  'vanlige_feil': ['Du tror angring betyr "oppsigelse for fremtiden". Det gjør det ikke. Avtalen oppheves helt — ikke '
                   'bare fra et bestemt punkt og fremover.',
                   'Du tror selgeren kan kreve "skadeerstatning" fordi du angret. Det kan de ikke. Angrerett er en '
                   'lovbestemt rett du har — ikke et brudd på kontrakten. Du skylder ingenting bare fordi du brukte '
                   'den.',
                   'Du fortsetter å bruke varen etter du har angret. Det skal du ikke. Når du har sendt '
                   'angremeldingen, må du behandle varen forsiktig og sende den tilbake. Fortsatt bruk kan gi selger '
                   'krav på verdireduksjon (§ 25 tredje ledd).'],
  'hva_bor_du_html': '<p>Når du har angret:</p>\n'
                     '<ul>\n'
                     '<li>Stopp å bruke varen umiddelbart</li>\n'
                     '<li>Pakk den så godt som mulig — gjerne i originalemballasjen</li>\n'
                     '<li>Send den tilbake innen 14 dager (§ 25)</li>\n'
                     '<li>Vent på refusjon — den skal komme innen 14 dager (§ 24)</li>\n'
                     '</ul>',
  'dumme_sporsmal': [],
  'related': [{'lov': 'angrerettloven', 'paragraf': '20', 'tittel': 'Slik bruker du angreretten', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '24',
               'tittel': 'Selgerens forpliktelser når du angrer',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '25',
               'tittel': 'Dine forpliktelser når du angrer',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '27',
               'tittel': 'Hva skjer med tilknyttede avtaler',
               'available': True}]},
 {'number': '24',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Selgeren har 14 dager på å betale deg tilbake',
  'description': 'Selgeren har 14 dager på å betale deg tilbake etter du har angret. Slik fungerer tilbakebetalingen – '
                 'med samme betalingsmiddel og uten gebyrer.',
  'kort_svar': 'Etter at du har angret, skal selgeren betale tilbake alle pengene du har betalt — innen 14 dager fra '
               'de mottok angremeldingen. Tilbakebetalingen skal skje med samme betalingsmiddel du brukte. Selgeren '
               'kan holde tilbake pengene til varen er mottatt tilbake eller du har dokumentert at den er sendt. Du '
               'skal ikke betale gebyr.',
  'paragraftekst': 'Den næringsdrivende skal tilbakeføre alle betalinger som er mottatt fra forbrukeren. Dersom '
                   'forbrukeren uttrykkelig har valgt en annen type levering enn standardleveringen som den '
                   'næringsdrivende tilbød, skal den næringsdrivende likevel ikke betale tilleggskostnadene dette '
                   'medførte.\n'
                   '\n'
                   'Tilbakebetaling skal skje uten unødig opphold, og senest 14 dager fra da den næringsdrivende fikk '
                   'melding om forbrukerens beslutning om å benytte angreretten etter § 20. Med mindre noe annet '
                   'uttrykkelig er avtalt med forbrukeren, skal tilbakebetalingen skje ved bruk av samme '
                   'betalingsmiddel som forbrukeren benyttet. Forbrukeren skal ikke betale noen form for gebyr som '
                   'følge av tilbakebetalingen.\n'
                   '\n'
                   'Den næringsdrivende kan holde tilbakebetalingen tilbake til varene er mottatt, eller til '
                   'forbrukeren har lagt frem dokumentasjon på at varene er sendt tilbake. Dette gjelder ikke når den '
                   'næringsdrivende har tilbudt seg å hente varene.\n'
                   '\n'
                   'Ved avtaler inngått utenom faste forretningslokaler, og der varene er levert til forbrukerens hjem '
                   'på avtaletidspunktet, skal den næringsdrivende for egen regning hente varene, om disse etter sin '
                   'art normalt ikke kan returneres med alminnelig postgang.\n'
                   '\n'
                   'Er det avtalt at varene skal hentes hos forbrukeren, og dette ikke skjer innen tre måneder fra den '
                   'dagen da den næringsdrivende fikk melding etter § 20, tilfaller varen forbrukeren vederlagsfritt.',
  'hva_betyr_html': '<p>§ 24 regulerer hva selgeren plikter å gjøre når du har angret.</p>\n'
                    '<p><strong>Alle pengene skal tilbake.</strong> Det betyr varens pris, standardfrakt fra selgeren '
                    'til deg, og eventuelle andre kostnader du betalte i forbindelse med kjøpet.</p>\n'
                    '<p><strong>Ett unntak — du valgte dyrere levering.</strong> Hvis du valgte ekspressfrakt eller '
                    'annen oppgradert levering, må selgeren bare refundere standardfrakt. Du må selv bære den ekstra '
                    'kostnaden for å ha valgt det dyrere alternativet.</p>\n'
                    '<p><strong>Frist: 14 dager.</strong> Tilbakebetalingen skal være på din konto eller kort senest '
                    '14 dager etter at selgeren mottok din angremelding. Ikke 14 dager etter at de mottok varen — 14 '
                    'dager etter angremeldingen.</p>\n'
                    '<p><strong>Samme betalingsmiddel.</strong> Betalte du med Vipps, får du tilbake til Vipps. '
                    'Betalte du med Visa, går pengene tilbake til kortet. Selgeren kan ikke gi deg "tilgodelapper" '
                    'eller butikkredit i stedet, med mindre dere uttrykkelig blir enige om det.</p>\n'
                    '<p><strong>Ingen gebyrer.</strong> Selgeren kan ikke trekke "behandlingsgebyr", "returgebyr" '
                    'eller annet av refusjonen. Du skal få tilbake hele beløpet.</p>\n'
                    '<p><strong>Selger kan holde tilbake — midlertidig.</strong> Det er én viktig nyanse: selgeren har '
                    'lov til å vente med tilbakebetalingen til de har:</p>\n'
                    '<ul>\n'
                    '<li>mottatt varen tilbake, eller</li>\n'
                    '<li>du har dokumentert at varen er sendt (typisk sendingskvittering fra Posten)</li>\n'
                    '</ul>\n'
                    '<p>Dette gjelder ikke hvis selgeren har tilbudt seg å hente varen — da må de bare betale tilbake '
                    'innen 14 dager.</p>\n'
                    '<p><strong>Spesialregel for hjemmesalg av store varer:</strong> Hvis selgeren leverte varen hjem '
                    'til deg ved avtaleinngåelsen, og varen ikke kan sendes med vanlig postgang — for eksempel en stor '
                    'sofa eller et tungt apparat — skal selgeren hente den for egen regning.</p>\n'
                    '<p><strong>Tre måneders regel for henting:</strong> Hvis selgeren skal hente varen og ikke kommer '
                    'innen tre måneder etter at de fikk angremeldingen, blir varen din vederlagsfritt. Selgeren har '
                    'ikke krav på den lenger.</p>',
  'eksempler': [{'navn': 'Anne',
                 'tekst': 'Anne kjøpte sko fra Zalando for 1 200 kr og 79 kr i frakt — totalt 1 279 kr. Hun angrer '
                          'etter en uke og sender skoene tilbake med Posten. Hun lagrer sendingskvitteringen og sender '
                          'en kopi til Zalando. Etter § 24 skal Zalando refundere hele 1 279 kr — varens pris pluss '
                          'standardfrakt — innen 14 dager fra angremeldingen.'},
                {'navn': 'Lars',
                 'tekst': 'Lars kjøpte en lampe for 1 800 kr og valgte ekspressfrakt for 199 kr (standardfrakt ville '
                          'vært 79 kr). Han angrer. Selgeren skal refundere 1 800 kr (lampens pris) og 79 kr '
                          '(standardfrakt). De skal ikke refundere ekstrafrakten på 120 kr (199 - 79). Det er Lars som '
                          'valgte ekspressleveringen og må bære den ekstra kostnaden.'},
                {'navn': 'Eva',
                 'tekst': 'Eva fikk hjemmebesøk fra et møbelfirma og kjøpte en stor sofa for 18 000 kr som ble levert '
                          'samtidig. Hun angrer to dager senere. Sofaen kan ikke sendes med vanlig post. Etter § 24 '
                          'fjerde ledd skal selgeren hente sofaen hos henne — for sin egen regning. Selgeren har tre '
                          'måneder på seg. Hvis de ikke kommer innen tre måneder, blir sofaen Evas gratis.'}],
  'vanlige_feil': ['Selgere som tilbyr "tilgodelapp" i stedet for refusjon. Det er ikke lovlig uten ditt samtykke. Du '
                   'har rett på pengene tilbake til samme betalingsmiddel.',
                   'Selgere som trekker "returgebyr" fra refusjonen. Det er ikke lovlig. Tilbakebetalingen skal være '
                   'full og uten gebyr.',
                   'Du venter passivt på pengene. Selger har 14 dager etter mottatt angremelding. Hvis det går lengre, '
                   'send en e-post og vis til § 24.',
                   'Selger sier de venter på varen — uten å nevne dokumentasjon. Hvis du har sendingskvittering fra '
                   'Posten, har selger ikke lenger rett til å holde tilbake refusjonen.'],
  'hva_bor_du_html': '<p>Hvis selger ikke har betalt innen 14 dager, send en betalingspåminnelse. Vis til § 24 og '
                     'oppgi at fristen er utløpt. Hvis det fortsatt ikke skjer noe, klag til Forbrukerrådet eller '
                     'Forbrukertilsynet. Du kan også ta saken til forliksrådet — kostnaden er lav, og angrerettsaker '
                     'er ofte enkle å vinne.</p>\n'
                     '<p>Etter du har angret:</p>\n'
                     '<ul>\n'
                     '<li>Send varen tilbake raskt (innen 14 dager)</li>\n'
                     '<li>Lagre sendingskvitteringen fra Posten — ta gjerne et bilde</li>\n'
                     '<li>Send selgeren en kopi av kvitteringen via e-post</li>\n'
                     '<li>Følg med på kontoen din — refusjonen skal komme innen 14 dager fra angremeldingen</li>\n'
                     '<li>Hvis den ikke kommer, send påminnelse med henvisning til § 24</li>\n'
                     '</ul>',
  'dumme_sporsmal': [{'q': 'Hva med PayPal-gebyrer som ble trukket?',
                      'a': 'Selgeren skal refundere hele kjøpesummen. Hvis PayPal har trukket et gebyr fra selgerens '
                           'andel, er det selgers tap — ikke ditt.'},
                     {'q': 'Kan selger refundere via bankoverføring i stedet for kortet jeg brukte?',
                      'a': 'Bare hvis du sier uttrykkelig ja. Hovedregelen er samme betalingsmiddel som du brukte. Du '
                           'skal ikke måtte oppgi kontonummer for å få tilbake penger.'},
                     {'q': 'Hva hvis selger har gått konkurs?',
                      'a': 'Da blir du en kreditor i konkursboet. Du må melde kravet ditt, men sjansen for full '
                           'utbetaling er ofte liten. Dette er en av risikoene ved netthandel.'}],
  'related': [{'lov': 'angrerettloven', 'paragraf': '20', 'tittel': 'Slik bruker du angreretten', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '23',
               'tittel': 'Hva skjer juridisk når du angrer',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '25',
               'tittel': 'Dine forpliktelser ved retur av varer',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '9',
               'tittel': 'Skjulte kostnader trenger du ikke betale',
               'available': True}]},
 {'number': '24a',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Dine data og innhold når du angrer på en digital tjeneste',
  'description': 'Hva skjer med dataene dine når du angrer på en strømmetjeneste eller skylagring? Selger skal slutte '
                 'å bruke innholdet og gi det tilbake.',
  'kort_svar': 'Når du angrer på et abonnement på digitalt innhold eller en digital tjeneste, skal selgeren slutte å '
               'bruke innholdet du har laget eller lagret. Hvis du ber om det, skal de gi deg en kopi av innholdet '
               'ditt — gratis og i et vanlig brukt format. Det er noen unntak for innhold som ikke har verdi utenfor '
               'tjenesten.',
  'paragraftekst': 'Ved avtaler om digitalt innhold eller digitale tjenester skal den næringsdrivende avstå fra å '
                   'bruke noen form for innhold, med unntak av personopplysninger, som forbrukeren har oppgitt eller '
                   'laget ved bruk av det digitale innholdet eller den digitale tjenesten som er levert av den '
                   'næringsdrivende. Dette gjelder likevel ikke hvis innholdet\n'
                   'a. ikke har noen nytteverdi utenfor rammene for det digitale innholdet eller den digitale '
                   'tjenesten\n'
                   'b. bare gjelder forbrukerens aktivitet ved bruk av det digitale innholdet eller den digitale '
                   'tjenesten\n'
                   'c. er slått sammen med andre data av den næringsdrivende og ikke kan deles opp, eller bare kan '
                   'deles opp med en uforholdsmessig stor innsats, eller\n'
                   'd. er generert i fellesskap av forbrukeren og andre, og andre forbrukere fortsatt kan benytte '
                   'innholdet.\n'
                   '\n'
                   'Hvis forbrukeren ber om det, skal den næringsdrivende gjøre tilgjengelig for forbrukeren enhver '
                   'form for innhold etter første ledd, bortsett fra i tilfeller som nevnt i første ledd bokstav a, b '
                   'og c.\n'
                   '\n'
                   'Forbrukeren har rett til å hente ut dette digitale innholdet gratis, uten hindring fra den '
                   'næringsdrivende, innen en rimelig frist og i et vanlig brukt og maskinlesbart format.',
  'hva_betyr_html': '<p>§ 24 a ble lagt til i 2023 og handler om noe relativt nytt: dine data og det du har skapt i en '
                    'digital tjeneste. Tenk på alle bildene du har lagret i Dropbox, dokumentene i Google Drive, eller '
                    'spillfremgangen i et online spill.</p>\n'
                    '<p><strong>Hovedregelen:</strong> Når du angrer, skal selger slutte å bruke det du har laget '
                    'eller lagret. Personopplysninger reguleres separat under personvernlovgivningen — denne '
                    'paragrafen handler om annet innhold du har generert.</p>\n'
                    '<p><strong>Du har rett til å hente ut innholdet ditt.</strong> Hvis du ber om det:</p>\n'
                    '<ul>\n'
                    '<li>Du skal få tilgang gratis</li>\n'
                    '<li>Innen rimelig frist</li>\n'
                    '<li>I et "vanlig brukt og maskinlesbart format" (typisk en standardisert filtype du kan åpne i '
                    'andre programmer)</li>\n'
                    '</ul>\n'
                    '<p><strong>Fire unntak — selger trenger ikke gi tilbake:</strong></p>\n'
                    '<ul>\n'
                    '<li><strong>a) Innhold uten verdi utenfor tjenesten.</strong> For eksempel: konfigurasjonsdata '
                    'for et spesifikt spill som ikke fungerer andre steder.</li>\n'
                    '<li><strong>b) Innhold som bare gjelder din aktivitet i tjenesten.</strong> Logger over hvilke '
                    'knapper du har trykket på, brukerstatistikk, scorehistorikk.</li>\n'
                    '<li><strong>c) Innhold blandet sammen med andre data.</strong> Hvis selgeren har slått din data '
                    'sammen med andres og det er praktisk umulig å skille — du har ikke krav på å få utdelt det. (Du '
                    'har likevel rett til at de slutter å bruke det.)</li>\n'
                    '<li><strong>d) Innhold skapt sammen med andre, der andre fortsatt bruker det.</strong> For '
                    'eksempel et samarbeidsdokument der andre brukere fortsatt jobber i samme fil.</li>\n'
                    '</ul>',
  'eksempler': [{'navn': 'Eva',
                 'tekst': 'Eva har et abonnement på en skylagringstjeneste der hun har lagret 50 GB med familiebilder, '
                          'dokumenter og videoer. Hun bestemmer seg for å angre innen fristen. Etter § 24 a har Eva '
                          'rett til å hente ut alle filene sine — gratis, innen rimelig tid, og i et vanlig format '
                          '(JPG, PDF, MP4 osv.). Tjenesten skal også slutte å bruke disse filene etter at hun har '
                          'hentet dem ut og kontoen er avsluttet.'},
                {'navn': 'Petter',
                 'tekst': 'Petter har spilt et online rollespill i to uker. Han har en karakter med utstyr, han har '
                          'samlet poeng, og han har sjattet med andre spillere. Han angrer på abonnementet. Etter § 24 '
                          'a kan han ikke kreve å få utlevert spillfiguren sin (bokstav a — har ikke verdi utenfor '
                          'spillet) eller poenglogger (bokstav b — gjelder bare hans aktivitet). Sjatt-historikk i '
                          'fellessamtaler kan også være unntatt (bokstav d). Det selgeren ikke kan: bruke karakteren '
                          'hans til markedsføring etter at avtalen er oppløst.'}],
  'vanlige_feil': ['Du tror "tilbakebetaling = sletting av alt". Det er det ikke. § 24 a sier at selger skal slutte å '
                   'bruke innholdet ditt. Hva som faktisk slettes og når, er en annen sak — regulert av '
                   'personvernlovgivning og selskapets vilkår.',
                   'Du tror du kan kreve "all data om deg". Du har rett til å få det du har laget — ikke nødvendigvis '
                   'interne loggdata, profiler eller statistikk som selgeren har generert om deg.',
                   'Du venter for lenge med å hente ut data. Etter at kontoen er avsluttet, kan tilgang bli vanskelig. '
                   'Hent ut innholdet ditt før eller umiddelbart i forbindelse med at du angrer.'],
  'hva_bor_du_html': '<p>Når du angrer på et abonnement der du har lagret data:</p>\n'
                     '<ul>\n'
                     '<li>Be eksplisitt om å få ut innholdet ditt i bruk av angremeldingen</li>\n'
                     '<li>Sjekk om tjenesten har en "Exportér data"-funksjon — mange har det automatisk</li>\n'
                     '<li>Last ned før kontoen avsluttes, hvis mulig</li>\n'
                     '<li>Hvis selgeren nekter, vis til § 24 a og krev tilgang i rimelig format</li>\n'
                     '</ul>',
  'dumme_sporsmal': [{'q': 'Gjelder dette også sosiale medier som Facebook?',
                      'a': 'Bare hvis du har betalt for tjenesten og angrer innen angrerett-fristen — gratistjenester '
                           'faller utenfor angrerettloven. For gratis tjenester gjelder personvernlovgivningen, som '
                           'også gir rett til dataportabilitet.'},
                     {'q': 'Hva med chatlogger og meldinger til andre?',
                      'a': 'Sjattmeldinger til andre brukere er som regel "skapt i fellesskap" (bokstav d). Du har '
                           'ikke automatisk krav på utlevering av disse, men selgeren kan ikke fortsette å aktivt '
                           'bruke dem.'}],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '19',
               'tittel': 'Samtykke til umiddelbar oppstart av digitale tjenester',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '22',
               'tittel': 'Når digitalt innhold ikke har angrerett',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '24',
               'tittel': 'Selgerens forpliktelser når du angrer',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '26',
               'tittel': 'Forbrukerens forpliktelser ved digitale tjenester',
               'available': True}]},
 {'number': '25',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Slik returnerer du varen riktig',
  'description': 'Hva må du gjøre når du angrer på et varekjøp? Send tilbake innen 14 dager, betal returfrakten – og '
                 'pass på reglene om verdireduksjon ved bruk.',
  'kort_svar': 'Etter du har angret, må du sende varen tilbake innen 14 dager. Du betaler returfrakten selv — med '
               'mindre selgeren har påtatt seg det eller glemt å informere om kostnaden. Selgeren kan kreve at du '
               'betaler for verditap hvis du har behandlet varen mer enn nødvendig for å se hva den er.',
  'paragraftekst': 'Forbrukeren skal uten unødig opphold, og senest 14 dager fra melding etter § 20 ble gitt, sende '
                   'varene tilbake, eller overlevere dem til den næringsdrivende dersom den næringsdrivende ikke har '
                   'tilbudt seg å hente varene.\n'
                   '\n'
                   'Forbrukeren skal bare betale de direkte kostnadene ved å returnere varene. Den næringsdrivende '
                   'skal likevel dekke disse kostnadene hvis denne har påtatt seg å betale disse eller ikke har '
                   'opplyst forbrukeren om at forbrukeren skal betale returkostnadene.\n'
                   '\n'
                   'Den næringsdrivende kan kreve at forbrukeren erstatter verdireduksjon som følge av forbrukerens '
                   'håndtering av varene som ikke har vært nødvendig for å fastslå varenes art, egenskaper og '
                   'funksjon. Dette gjelder bare dersom forbrukeren har mottatt opplysninger om angrerett, jf. § 8 '
                   'første ledd bokstav h.',
  'hva_betyr_html': '<p>§ 25 beskriver dine tre plikter når du har angret på et varekjøp.</p>\n'
                    '<p><strong>1. Send varen tilbake innen 14 dager.</strong> Klokken starter fra dagen du sendte '
                    'angremeldingen — ikke fra dagen selgeren mottok den. Du må ha sendt varen innen 14 dager etter '
                    'angremeldingen.</p>\n'
                    '<p>Hvis selgeren har tilbudt seg å hente varen (typisk ved store eller tunge varer), trenger du '
                    'ikke å sende den selv. Da venter du på at de henter.</p>\n'
                    '<p><strong>2. Du betaler returfrakten.</strong> Direkte kostnader ved retur — typisk porto eller '
                    'fraktkostnader — dekker du selv. Men: selgeren skal dekke det hvis ett av to vilkår er '
                    'oppfylt:</p>\n'
                    '<ul>\n'
                    '<li>Selgeren har påtatt seg å betale returkostnaden (frivillig service)</li>\n'
                    '<li>Selgeren har glemt å informere deg om at du må betale returkostnaden (brudd på § 8 bokstav i, '
                    'jf. § 9)</li>\n'
                    '</ul>\n'
                    '<p>Mange større nettbutikker tilbyr gratis retur som markedsføringsfordel — det er deres egen '
                    'avtale med deg.</p>\n'
                    '<p><strong>3. Verdireduksjon — pass på hvordan du behandler varen.</strong> Du har lov til å '
                    'undersøke varen som om du sto i en fysisk butikk. Du kan løfte den, prøve den, slå den på for å '
                    'se hvordan den fungerer. Du kan prøve en kjole foran speilet.</p>\n'
                    '<p>Men du kan ikke bruke varen normalt i 14 dager og deretter angre. Hvis du har gjort mer enn å '
                    'bare undersøke "art, egenskaper og funksjon", kan selgeren kreve at du betaler for '
                    'verditapet.</p>\n'
                    '<p><strong>Viktig:</strong> Verdireduksjon kan bare kreves hvis selgeren har gitt deg ordentlig '
                    'informasjon om angreretten etter § 8 bokstav h. Har de glemt det, kan de heller ikke kreve '
                    'verdireduksjon.</p>',
  'eksempler': [{'navn': 'Anne',
                 'tekst': 'Anne kjøpte sko fra Zalando. Hun angrer to dager senere og sender angremelding. Hun pakker '
                          'skoene i originalemballasjen og sender dem tilbake fire dager etter angremeldingen. Hun '
                          'betaler 79 kr i returfrakt — Zalando hadde opplyst om dette i kjøpsbekreftelsen. Anne har '
                          'gjort alt riktig. Hun var innenfor 14-dagersfristen, hun bærer selv returkostnaden fordi '
                          'selgeren informerte om det, og hun har ikke brukt skoene. Hun får full refusjon av '
                          'kjøpesummen.'},
                {'navn': 'Lars',
                 'tekst': 'Lars kjøpte en lampe på en utenlandsk nettbutikk for 1 900 kr. Ingen steder i bestillingen '
                          'eller bekreftelsen sto det noe om returkostnader. Han angrer og må sende lampen tilbake til '
                          'Tyskland — fraktkostnaden er 350 kr. Etter § 25 andre ledd skal selgeren dekke disse 350 '
                          'kronene fordi de glemte å opplyse om returkostnaden (brudd på § 8 bokstav i). Lars betaler '
                          'fraktselskapet, tar vare på kvitteringen, og krever refusjon av returfrakten i tillegg til '
                          'kjøpesummen.'},
                {'navn': 'Tom',
                 'tekst': 'Tom kjøpte en flatskjerm-TV for 12 000 kr. Han pakket ut, satt den opp, brukte den hver dag '
                          'i tolv dager — kjørte filmer, spilte spill, brukte den til alt. Så angret han. Selgeren '
                          'godtok angreretten, men krevde 3 000 kr i verdireduksjon. Begrunnelsen: Tom hadde brukt '
                          'TV-en langt utover det som er nødvendig for å "fastslå art, egenskaper og funksjon". For å '
                          'sjekke om den fungerer, holder det å slå den på i noen minutter — ikke å bruke den daglig i '
                          'to uker. Selgeren hadde gitt korrekt angrerett-info, og kravet er lovlig etter § 25 tredje '
                          'ledd.'}],
  'vanlige_feil': ['Du tror du har 14 dager på å angre OG ytterligere 14 dager på å sende tilbake. Du har 14 dager på '
                   'å angre, og deretter 14 dager fra angremeldingen på å sende. Det er to forskjellige frister med '
                   'samme lengde.',
                   'Du tror du må betale frakten uansett. Du må det bare hvis selgeren faktisk har opplyst om dette på '
                   'forhånd. Glemte de å nevne returkostnader, betaler de.',
                   'Du bruker varen "litt" og tror det er greit. "Undersøke" og "bruke" er ikke det samme. Klærne kan '
                   'du prøve på, men ikke bruke ut på byen. Elektronikken kan du slå på, men ikke ta i bruk over flere '
                   'dager.',
                   'Du tror selger må bevise verdireduksjonen. I prinsippet ja, men i praksis er det ofte enkelt for '
                   'selger å vise at en brukt vare er mindre verdt. Vær forsiktig med håndtering hvis du er usikker.'],
  'hva_bor_du_html': '<p>Hvis du ikke sender varen innen 14 dager: Selgeren kan kreve at du beholder varen og betaler '
                     'full pris. Angreretten avhenger av at du faktisk returnerer.</p>\n'
                     '<p>Hvis du har brukt varen for mye: Selgeren kan trekke verdireduksjon fra refusjonen. Beløpet '
                     'skal stå i forhold til hvor mye verdi som er tapt — ikke en straff.</p>\n'
                     '<p>Når du angrer:</p>\n'
                     '<ul>\n'
                     '<li>Pakk varen så fort som mulig — bruk gjerne originalemballasjen</li>\n'
                     '<li>Send med en gang, ikke vent</li>\n'
                     '<li>Ta vare på sendingskvitteringen</li>\n'
                     '<li>Hvis du har brukt varen, vurder hvor mye — har du gjort mer enn å undersøke?</li>\n'
                     '<li>Hvis selgeren krever verdireduksjon du mener er urimelig, klag til Forbrukerrådet</li>\n'
                     '</ul>',
  'dumme_sporsmal': [{'q': 'Må jeg ha originalemballasjen?',
                      'a': 'Ikke etter loven, men det er smart. Hvis du har kastet esken og varen kommer tilbake i en '
                           'posepakke, kan selgeren argumentere for verdireduksjon på grunn av forringet emballasje.'},
                     {'q': 'Kan jeg vaske klærne før jeg returnerer?',
                      'a': 'Nei, det vil normalt regnes som bruk utover det som er nødvendig. Vasking endrer varens '
                           'tilstand. Prøv klærne forsiktig og send dem tilbake i samme stand som du fikk dem.'},
                     {'q': 'Hva med å fjerne plastfolie på elektronikk?',
                      'a': 'Å åpne emballasjen og fjerne beskyttelsesfilm regnes som en normal del av å undersøke '
                           'varen. Det utløser ikke verdireduksjon.'}],
  'related': [{'lov': 'angrerettloven', 'paragraf': '20', 'tittel': 'Slik bruker du angreretten', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '24',
               'tittel': 'Selgerens forpliktelser ved tilbakebetaling',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '9',
               'tittel': 'Hvis selger glemte å opplyse om kostnader',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '8',
               'tittel': 'Selgerens opplysningsplikt før kjøpet',
               'available': True}]},
 {'number': '26',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Hva du betaler hvis du angrer på en delvis levert tjeneste',
  'description': 'Hva betaler du hvis du angrer på en tjeneste som er delvis levert? Forholdsmessig betaling – med '
                 'viktige unntak der du slipper helt unna.',
  'kort_svar': 'Hvis du har bedt om at en tjeneste skal starte før angrefristen er ute, og senere angrer, må du betale '
               'en forholdsmessig del — basert på hvor mye som er levert. Men du slipper å betale helt hvis selgeren '
               'ikke ga deg angrerett-info, ikke fikk din uttrykkelige aksept for oppstart, eller ikke sendte deg '
               'bekreftelse på avtalen.',
  'paragraftekst': 'Ved bruk av angreretten ved tjenester som forbrukeren uttrykkelig har bedt den næringsdrivende om '
                   'å begynne levering av, skal forbrukeren betale et beløp som står i forhold til det som er levert '
                   'frem til det tidspunkt forbrukeren gir melding om bruk av angreretten. Er den samlede prisen '
                   'urimelig høy, skal det forholdsmessige beløpet beregnes på grunnlag av markedsverdien av det som '
                   'er levert.\n'
                   '\n'
                   'Forbrukerens betalingsplikt faller bort når:\n'
                   'a. den næringsdrivende ikke har gitt opplysninger i samsvar med § 8 første ledd bokstav h og j,\n'
                   'b. forbrukeren ikke uttrykkelig har bedt om at leveringen skal begynne innen utløpet av '
                   'angrefristen i samsvar med §§ 12 eller 19, eller\n'
                   'c. levering av digitalt innhold som ikke kan leveres på et fysisk medium, er begynt uten '
                   'forbrukerens uttrykkelige forhåndssamtykke og erkjennelse av at angreretten dermed går tapt, eller '
                   'uten at den næringsdrivende har gitt bekreftelse i samsvar med § 11 annet ledd og § 18 annet '
                   'ledd.\n'
                   '\n'
                   'Ved avtaler om digitalt innhold eller digitale tjenester skal forbrukeren som bruker angreretten, '
                   'avstå fra å bruke det digitale innholdet eller den digitale tjenesten og fra å gjøre den '
                   'tilgjengelig for tredjeparter.',
  'hva_betyr_html': '<p>§ 26 handler om hva du må betale hvis du angrer underveis i en tjeneste — typisk et '
                    'abonnement, en konsulenttjeneste eller en håndverkertjeneste som er startet før angrefristen er '
                    'ute.</p>\n'
                    '<p><strong>Hovedregelen: forholdsmessig betaling.</strong> Hvis du har bedt selgeren om å begynne '
                    'tjenesten før angrefristen er ute (etter § 12 eller § 19), og du angrer underveis, skal du betale '
                    'en del av prisen — i forhold til hvor mye som er levert.</p>\n'
                    '<p><strong>Beregningen:</strong> hvor mye av tjenesten er gjennomført? Hvis selgeren leverte i '
                    'fem av tretti dager, skal du betale 5/30. Hvis tre av seks timer er gjennomført, skal du betale '
                    'halv pris.</p>\n'
                    '<p>Hvis totalprisen er urimelig høy — for eksempel en hjemmebesøk-håndverker som tar 5 000 kr i '
                    'timen — skal det forholdsmessige beløpet beregnes etter markedsverdien, ikke avtaleprisen. Du '
                    'skal ikke betale for at selgeren tok overpris.</p>\n'
                    '<p><strong>Tre situasjoner der du slipper å betale noe som helst:</strong></p>\n'
                    '<ul>\n'
                    '<li><strong>a) Selger ga ikke angrerett-info.</strong> Hvis selgeren ikke har oppfylt '
                    'opplysningsplikten i § 8 bokstav h (om angrerett) eller j (om ansvar for kostnader ved oppstart), '
                    'bortfaller hele betalingsplikten din.</li>\n'
                    '<li><strong>b) Du ba ikke uttrykkelig om oppstart.</strong> Hvis selgeren bare begynte å levere '
                    'uten å få din uttrykkelige forespørsel om å starte før angrefristen (etter §§ 12 eller 19), skal '
                    'du ikke betale for det som er levert.</li>\n'
                    '<li><strong>c) Digitalt innhold uten korrekt samtykke.</strong> Hvis et digitalt produkt (film, '
                    'e-bok, programvare) er begynt levert uten ditt uttrykkelige forhåndssamtykke, eller uten at du '
                    'erkjente tap av angrerett, eller uten at selger ga deg bekreftelse — du slipper å betale.</li>\n'
                    '</ul>\n'
                    '<p><strong>Spesielt for digitalt innhold når du angrer:</strong></p>\n'
                    '<ul>\n'
                    '<li>Du må slutte å bruke tjenesten umiddelbart</li>\n'
                    '<li>Du må ikke dele det videre til andre</li>\n'
                    '<li>Selgeren kan stenge din tilgang</li>\n'
                    '</ul>',
  'eksempler': [{'navn': 'Eva',
                 'tekst': 'Eva tegnet et månedsabonnement på en strømmetjeneste til 199 kr. Hun haket av "Jeg ønsker å '
                          'starte umiddelbart og erkjenner at angreretten faller bort ved fullført bruk". Etter sju '
                          'dager angrer hun. Etter § 26 første ledd skal hun betale forholdsmessig. Sju av tretti '
                          'dager er ca. 23 prosent — så hun skal betale ca. 47 kr og få 152 kr refundert. Hun må '
                          'slutte å bruke tjenesten umiddelbart.'},
                {'navn': 'Petter',
                 'tekst': 'Petter fikk hjemmebesøk fra en hagedesigner som lovte å lage en hageplan for 8 000 kr. '
                          'Designeren begynte å jobbe samme dag, men ba aldri Petter om uttrykkelig samtykke til å '
                          'starte før angrefristen var ute. Tre dager senere angrer Petter. Designeren har brukt 12 '
                          'timer og krever halvparten av honoraret. Men etter § 26 andre ledd bokstav b bortfaller '
                          'Petters betalingsplikt fordi han aldri "uttrykkelig" ba om at leveringen skulle begynne. '
                          'Designeren får ingenting.'},
                {'navn': 'Sara',
                 'tekst': 'Sara tegnet et abonnement på en online-kurs for 2 400 kr. Selgeren glemte å gi henne '
                          'angreskjema og informasjon om angreretten. Hun fullførte halvparten av kurset, deretter '
                          'ombestemte hun seg. Etter § 26 andre ledd bokstav a faller hennes betalingsplikt bort fordi '
                          'selger ikke har gitt korrekt angrerett-info. Hun har rett til full refusjon på 2 400 kr, '
                          'selv om hun har brukt halvparten av kurset.'}],
  'vanlige_feil': ['Du tror du må betale full pris fordi tjenesten har startet. Det stemmer ikke. Du betaler bare '
                   'forholdsmessig — og noen ganger ingenting.',
                   'Du tror "forholdsmessig" alltid er en lineær beregning. Det er en god utgangspunkt, men hvis '
                   'prisen er urimelig høy, beregnes det etter markedsverdien.',
                   'Selger antar at du har samtykket bare fordi du bestilte. Bestillingen er ikke det samme som '
                   '"uttrykkelig forespørsel om å starte før angrefristen". Det skal være en bevisst handling fra '
                   'deg.'],
  'hva_bor_du_html': '<p>Hvis du har angret på en delvis levert tjeneste:</p>\n'
                     '<ul>\n'
                     '<li>Sjekk om selgeren har oppfylt alle vilkår: angrerett-info, ditt uttrykkelige samtykke til '
                     'oppstart, bekreftelse på varig medium</li>\n'
                     '<li>Hvis ett eller flere mangler, krev full refusjon med henvisning til § 26 andre ledd</li>\n'
                     '<li>Hvis alt er i orden, beregn selv hva forholdsmessig betaling skal være — så vet du hva du '
                     'kan akseptere</li>\n'
                     '</ul>\n'
                     '<p>For digitalt innhold:</p>\n'
                     '<ul>\n'
                     '<li>Slutt å bruke tjenesten med en gang du har angret</li>\n'
                     '<li>Forvent at selger stenger tilgangen</li>\n'
                     '<li>Krev å få ut innholdet ditt etter § 24 a hvis det er relevant</li>\n'
                     '</ul>',
  'dumme_sporsmal': [],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '19',
               'tittel': 'Samtykke til umiddelbar oppstart ved fjernsalg',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '22',
               'tittel': 'Når digitalt innhold ikke har angrerett',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '24',
               'tittel': 'Selgerens tilbakebetalingsplikt',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '24a',
               'tittel': 'Dine data ved digitale tjenester',
               'available': True}]},
 {'number': '27',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Tilknyttede avtaler faller automatisk bort',
  'description': 'Du kjøpte en mobil og en mobilforsikring sammen – kan du beholde det ene og angre på det andre? Slik '
                 'fungerer tilknyttede avtaler i § 27.',
  'kort_svar': 'Når du angrer på et kjøp, faller alle tilknyttede avtaler automatisk bort uten ekstra kostnad for deg. '
               'Det betyr at hvis du for eksempel kjøpte en telefon og en mobilforsikring samtidig, faller '
               'forsikringen bort når du angrer på telefonen. Selgeren må selv varsle den tredjeparten som '
               'forsikringen var hos.',
  'paragraftekst': 'Dersom forbrukeren bruker sin angrerett, faller alle tilknyttede avtaler bort uten kostnad for '
                   'forbrukeren. §§ 24 til 26 gjelder tilsvarende.\n'
                   '\n'
                   'Etter å ha mottatt forbrukerens melding om bruk av angrerett skal den næringsdrivende straks gi '
                   'beskjed til tredjeperson som har inngått en tilknyttet avtale med forbrukeren.',
  'hva_betyr_html': '<p>§ 27 forhindrer at du sitter igjen med "halve" avtaler etter at du har angret. Hvis det finnes '
                    'andre avtaler som ble inngått sammen med hovedkjøpet, faller også de bort automatisk.</p>\n'
                    '<p><strong>Hva er en tilknyttet avtale?</strong> Definert i § 5 bokstav g: en avtale der du '
                    'mottar varer eller tjenester i forbindelse med et hovedkjøp, og der varene eller tjenestene '
                    'leveres av selgeren selv eller en tredjepart i samarbeid med selgeren.</p>\n'
                    '<p>Typiske eksempler:</p>\n'
                    '<ul>\n'
                    '<li>Mobiltelefon + mobilforsikring fra et annet selskap</li>\n'
                    '<li>Bil + serviceavtale gjennom forhandleren</li>\n'
                    '<li>TV + utvidet garanti fra tredjepart</li>\n'
                    '<li>Programvare + årlig oppdateringsabonnement</li>\n'
                    '</ul>\n'
                    '<p><strong>Avtalene faller bort uten kostnad for deg.</strong> Du skal ikke betale '
                    '"oppsigelsesgebyr" eller "behandlingsgebyr" på de tilknyttede avtalene. Det er nettopp poenget — '
                    'at angreretten på hovedkjøpet skal ha praktisk virkning.</p>\n'
                    '<p><strong>Selgeren må varsle tredjepart.</strong> Etter at de har mottatt din angremelding, skal '
                    'selgeren "straks" gi beskjed til den tredjeparten du har en tilknyttet avtale med. Du trenger '
                    'ikke selv kontakte tredjeparten.</p>\n'
                    '<p><strong>§§ 24 til 26 gjelder tilsvarende.</strong> Det betyr at tilbakebetaling skal skje '
                    'innen 14 dager (§ 24), du må returnere eventuelle varer (§ 25), og forholdsmessig betaling kan '
                    'gjelde for delvis leverte tjenester (§ 26).</p>',
  'eksempler': [{'navn': 'Anne',
                 'tekst': 'Anne kjøper en ny iPhone på nett for 12 990 kr. Samtidig blir hun tilbudt en '
                          '"telefonforsikring fra Tryg" for 89 kr i måneden — en tilknyttet avtale arrangert av '
                          'forhandleren. Hun haker av begge. Etter åtte dager angrer hun på telefonen. Hun trenger '
                          'ikke å kontakte Tryg separat — forsikringen er en tilknyttet avtale og faller automatisk '
                          'bort etter § 27. Forhandleren skal varsle Tryg om angreretten. Anne får refundert både '
                          'telefonens pris og eventuell innbetalt forsikringspremie.'},
                {'navn': 'Lars',
                 'tekst': 'Lars kjøper en oppvaskmaskin og en utvidet garanti til 1 500 kr fra et separat firma som '
                          'forhandleren samarbeider med. Han angrer på oppvaskmaskinen. Den utvidede garantien er en '
                          'tilknyttet avtale. Etter § 27 faller den automatisk bort. Lars skal ha refundert hele '
                          'garantien på 1 500 kr, og han trenger ikke selv kontakte garantifirmaet — forhandleren skal '
                          'varsle dem.'}],
  'vanlige_feil': ['Du tror du må si opp tilknyttede avtaler separat. Det må du ikke. De faller automatisk bort.',
                   'Du betaler "oppsigelsesgebyr" på en tilknyttet avtale fordi selgeren ber om det. Det er ikke '
                   'lovlig. Tilknyttede avtaler faller bort uten kostnad.',
                   'Du tror dette gjelder alle parallelle avtaler. Det gjør det ikke. Avtalen må være "tilknyttet" i '
                   'lovens forstand — det vil si etablert i forbindelse med hovedkjøpet og av selgeren eller selgerens '
                   'samarbeidspart.'],
  'hva_bor_du_html': '<p>Når du angrer på et hovedkjøp:</p>\n'
                     '<ul>\n'
                     '<li>Tenk gjennom om det fantes tilknyttede avtaler — forsikringer, abonnementer, '
                     'serviceavtaler</li>\n'
                     '<li>Nevn dem i angremeldingen: "Jeg angrer også på den tilknyttede mobilforsikringen fra '
                     'X"</li>\n'
                     '<li>Følg med på at den tilknyttede avtalen faktisk avsluttes — sjekk kontoen din for fremtidige '
                     'trekk</li>\n'
                     '<li>Hvis tredjeparten ikke har mottatt beskjed innen rimelig tid, kontakt dem og vis til § '
                     '27</li>\n'
                     '</ul>',
  'dumme_sporsmal': [{'q': 'Er en bankkreditt for å betale et kjøp en "tilknyttet avtale"?',
                      'a': 'Ofte ja, hvis kreditten ble formidlet av selgeren eller en samarbeidspart. Hvis du '
                           'finansierte via Klarna eller liknende selger-formidlet ordning, faller den bort sammen med '
                           'kjøpet. Hvis du tok opp et helt uavhengig forbrukslån, må du regne med å håndtere det '
                           'selv.'},
                     {'q': 'Hva med uavhengig forsikring jeg tegnet på egen hånd etter kjøpet?',
                      'a': 'Det er ikke en tilknyttet avtale i lovens forstand. Den må du eventuelt si opp etter '
                           'forsikringens egne regler.'}],
  'related': [{'lov': 'angrerettloven', 'paragraf': '20', 'tittel': 'Slik bruker du angreretten', 'available': True},
              {'lov': 'angrerettloven', 'paragraf': '23', 'tittel': 'Hva skjer når du angrer', 'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '5',
               'tittel': 'Definisjonen av tilknyttet avtale',
               'available': True},
              {'lov': 'angrerettloven',
               'paragraf': '24',
               'tittel': 'Selgerens forpliktelser ved tilbakebetaling',
               'available': True}]},
 {'number': '28',
  'lov': 'angrerettloven',
  'lov_display': 'Angrerettloven',
  'title': 'Forbrukertilsynet og Markedsrådet kontrollerer at reglene følges',
  'description': 'Hvem passer på at angrerettloven faktisk håndheves? Forbrukertilsynet og Markedsrådet fører kontroll '
                 'og kan gripe inn ved brudd på reglene.',
  'kort_svar': 'Forbrukertilsynet og Markedsrådet er de offentlige organene som passer på at angrerettloven '
               'etterleves. De kan undersøke selgere, gi pålegg om å rette opp, og bringe saker for Markedsrådet. '
               'Reglene for hvordan de jobber, er de samme som i markedsføringsloven.',
  'paragraftekst': 'Forbrukertilsynet og Markedsrådet skal føre kontroll med at bestemmelser i, eller bestemmelser '
                   'gitt i medhold av denne loven, overholdes. Kontrollen utøves i samsvar med reglene i '
                   'markedsføringsloven §§ 32 til 41, § 42 første ledd annet punktum og § 43.',
  'hva_betyr_html': '<p>§ 28 forteller hvem som har myndighet til å håndheve angrerettloven.</p>\n'
                    '<p><strong>Forbrukertilsynet</strong> er et statlig tilsynsorgan som blant annet:</p>\n'
                    '<ul>\n'
                    '<li>Behandler klager fra forbrukere</li>\n'
                    '<li>Gjennomfører tilsynsaksjoner mot bransjer og enkeltselskaper</li>\n'
                    '<li>Gir pålegg om retting når selgere bryter reglene</li>\n'
                    '<li>Kan ilegge overtredelsesgebyr (se § 29)</li>\n'
                    '</ul>\n'
                    '<p><strong>Markedsrådet</strong> er et uavhengig klageorgan. Hvis Forbrukertilsynet fatter et '
                    'vedtak en bedrift er uenig i, kan saken klages inn til Markedsrådet for vurdering.</p>\n'
                    '<p><strong>Hvordan de jobber:</strong> Bestemmelsene i markedsføringsloven §§ 32 til 41 gjelder '
                    'tilsvarende. Det betyr blant annet at Forbrukertilsynet kan kreve opplysninger fra bedrifter, gi '
                    'pålegg om retting, ilegge tvangsmulkt hvis bedriften ikke retter seg, og bringe saker for '
                    'Markedsrådet.</p>\n'
                    '<p><strong>Hva betyr dette for deg?</strong> Du har et offentlig organ i ryggen hvis en selger '
                    'systematisk bryter angrerettloven. Hvis en sak har prinsipiell betydning — for eksempel en stor '
                    'nettbutikk som nekter alle kundene angrerett — er ikke du alene. Du kan klage til '
                    'Forbrukertilsynet, og de kan gripe inn på vegne av alle forbrukere.</p>\n'
                    '<p><strong>Forbrukerrådet</strong> (ikke å forveksle med Forbrukertilsynet) gir derimot råd og '
                    'bistand i enkeltsaker, og megler i tvister. Mange bruker disse organene parallelt: Forbrukerrådet '
                    'for å løse din konkrete sak, Forbrukertilsynet for å rapportere systematiske brudd.</p>',
  'eksempler': [{'navn': 'Tom',
                 'tekst': 'Tom oppdager at en stor nettbutikk konsekvent skriver "ingen angrerett på elektronikk" i '
                          'vilkårene. Han har selv blitt nektet retur, og ser i kommentarfelt at flere kunder har '
                          'samme erfaring. Tom kan klage saken inn til Forbrukertilsynet. De har myndighet til å '
                          'undersøke selskapets praksis, og kan gi pålegg om at vilkårene endres. Hvis selskapet ikke '
                          'retter seg, kan saken bringes til Markedsrådet eller resultere i overtredelsesgebyr.'},
                {'navn': 'Eva',
                 'tekst': 'Eva blir nektet refusjon etter å ha angret korrekt. Selgeren henviser til egne vilkår som '
                          'strider mot angrerettloven. For Eva personlig er det enklest å gå via Forbrukerrådet, som '
                          'kan mekle. Men hun kan også rapportere saken til Forbrukertilsynet — det hjelper med å '
                          'bygge en sak hvis selgeren har et mønster av lovbrudd.'}],
  'vanlige_feil': ['Du forveksler Forbrukertilsynet og Forbrukerrådet. De er to forskjellige organer. Forbrukerrådet '
                   'hjelper i enkeltsaker (megling). Forbrukertilsynet er tilsynsmyndighet som håndhever loven på '
                   'systemnivå.',
                   'Du tror du må starte med Forbrukertilsynet. Ikke nødvendigvis. Forbrukertilsynet behandler ikke '
                   'alle enkeltsaker, men prioriterer prinsipielle saker og systematiske brudd. For din egen tvist er '
                   'ofte Forbrukerrådet en bedre vei.',
                   'Du tror Forbrukertilsynet kan tvinge selgeren til å betale deg tilbake. Direkte beordring av '
                   'tilbakebetaling i din spesifikke sak er ikke deres primære rolle. De fokuserer på selgers '
                   'fremtidige praksis. For penger tilbake må du gå via Forbrukerrådet, forliksrådet eller '
                   'domstolene.'],
  'hva_bor_du_html': '<p>Hvis en selger nekter å følge angrerettloven:</p>\n'
                     '<ul>\n'
                     '<li>Først: kontakt Forbrukerrådet for hjelp med din sak (forbrukerradet.no)</li>\n'
                     '<li>I tillegg: rapporter selgeren til Forbrukertilsynet (forbrukertilsynet.no) hvis du tror '
                     'flere er rammet</li>\n'
                     '<li>Hvis Forbrukerrådet ikke fører frem: vurder forliksrådet (lave kostnader)</li>\n'
                     '</ul>',
  'dumme_sporsmal': [],
  'related': [{'lov': 'angrerettloven',
               'paragraf': '3',
               'tittel': 'Loven kan ikke fravikes til skade for deg',
               'available': True},
              {'lov': 'markedsforingsloven',
               'paragraf': '32',
               'tittel': 'Kontrollregler som gjelder tilsvarende',
               'available': False}]}]
