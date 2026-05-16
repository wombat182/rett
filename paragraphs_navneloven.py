"""Navneloven — paragraf-data for Rettsregel."""

PARAGRAPHS = [
    {
        "number": "1",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Navneplikt — må jeg ha fornavn og etternavn?",
        "kategori": "familie",
        "description": "Alle i Norge må ha fornavn og etternavn. Du kan ikke selv velge å droppe etternavnet eller bytte navn utenfor loven.",
        "kort_svar": "Alle i Norge må ha et fornavn og ett etternavn — enkelt eller dobbelt. Du kan i tillegg ha et mellomnavn. Du kan ikke bare slutte å bruke etternavnet ditt, og du kan ikke bytte navn på egenhånd.",
        "paragraftekst": "Alle skal ha fornavn og ett enkelt eller dobbelt etternavn og kan i tillegg ha mellomnavn. Enhver har plikt til å bruke sitt fornavn og etternavn som personnavn. Ingen kan ta, endre eller sløyfe navn på annen måte enn etter loven her.",
        "hva_betyr_html": """<p>Loven slår fast tre ting: Du må ha fornavn. Du må ha etternavn — enten ett navn eller to navn med bindestrek. Du kan ha mellomnavn, men det er valgfritt.</p>
<p>Du plikter å bruke begge deler. Det betyr at du ikke kan si «jeg heter bare Kari» i offisielle sammenhenger — etternavnet følger med.</p>
<p>Og du kan ikke bare finne på et nytt navn. Alt må gå gjennom navneloven — via skattekontoret.</p>""",
        "eksempler": [
            {
                "navn": "Petter",
                "tekst": "Petter synes etternavnet Johansen er kjedelig og vil bare hete Petter. Det går ikke. Han kan søke om å bytte etternavn til noe annet, men han må alltid ha et etternavn registrert i Folkeregisteret."
            }
        ],
        "vanlige_feil": [
            "Tro at du kan «droppe» etternavnet i det daglige — i offisielle sammenhenger er det påkrevd",
            "Tro at du kan bestemme navnebytte selv uten å melde det inn",
            "Glemme at mellomnavn er valgfritt, ikke påkrevd",
        ],
        "hva_bor_du_html": "<p>Vil du endre navn? Bruk Skatteetatens skjema på skatteetaten.no. Se § 11 for mer om fremgangsmåten.</p>",
        "dumme_sporsmal": [
            {
                "q": "Kan jeg ha bare ett navn, som noen kjendiser?",
                "a": "Ikke i Norge som personnavn. Du må ha fornavn og etternavn. Artistnavn er noe annet — det er ikke et personnavn i lovens forstand."
            },
            {
                "q": "Hva er forskjellen på mellomnavn og dobbelt etternavn?",
                "a": "Mellomnavn brukes mellom fornavn og etternavn, og er valgfritt. Dobbelt etternavn er to etternavn satt sammen med bindestrek. Bare etternavnet er obligatorisk."
            },
            {
                "q": "Kan jeg ha to fornavn?",
                "a": "Ja. Loven forbyr ikke det. Det er vanlig i Norge — for eksempel «Anne Marie»."
            }
        ],
        "related": [
            {"lov": "navneloven", "paragraf": "2", "tittel": "Plikt til å velge navn for barn", "available": True},
            {"lov": "navneloven", "paragraf": "3", "tittel": "Frie, beskyttede og nye etternavn", "available": True},
            {"lov": "navneloven", "paragraf": "10", "tittel": "Alminnelige begrensninger ved navnebytte", "available": True},
        ],
    },
    {
        "number": "2",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Plikt til å velge navn for barn",
        "kategori": "familie",
        "description": "Du har 6 måneder på å velge navn til barnet ditt. Etter det får barnet morens etternavn automatisk.",
        "kort_svar": "Du har 6 måneder på å melde inn navn til barnet ditt. Gjør du ikke det, får barnet automatisk morens etternavn.",
        "paragraftekst": "Senest når barnet fyller seks måneder, skal den eller de som har foreldreansvaret for barnet, sende melding om hvilket navn barnet skal ha.\n\nHar barnet fylt seks måneder uten at melding er sendt eller uten at meldingen kan godtas, får barnet morens etternavn.",
        "hva_betyr_html": """<p>Når barnet er født, har du og den andre forelderen 6 måneder på dere til å bestemme og melde inn navn. Det gjelder fornavn og etternavn.</p>
<p>Hvis dere ikke gjør det innen fristen — eller sender inn noe som ikke godtas — setter systemet inn morens etternavn automatisk. Det skjer uten at noen spør igjen.</p>""",
        "eksempler": [
            {
                "navn": "Sara og Lars",
                "tekst": "Sara og Lars ble uenige om etternavnet til sønnen sin. De utsatte meldingen og glemte alt i stresset. Da gutten nærmet seg 6 måneder, fikk de et varsel — og skjønte at de måtte bestemme seg raskt. De valgte Saras etternavn og fikk det godkjent i tide."
            }
        ],
        "vanlige_feil": [
            "Tro at helsestasjonen eller sykehuset melder inn navnet automatisk — det gjør de ikke",
            "Vente for lenge fordi foreldrene er uenige",
            "Tro at fristen er ett år — den er seks måneder",
        ],
        "hva_bor_du_html": "<p>Meld inn navn via Skatteetatens sider eller på helsestasjonen. Det kan gjøres digitalt med BankID. Gjør det gjerne tidlig — ikke vent til fristen nærmer seg.</p>",
        "dumme_sporsmal": [
            {
                "q": "Hva skjer hvis vi er uenige om etternavnet?",
                "a": "Loven sier at den eller de med foreldreansvar skal sende melding. Hvis dere ikke blir enige og fristen går ut, får barnet morens etternavn."
            },
            {
                "q": "Kan vi endre barnets navn etterpå?",
                "a": "Ja, men det krever en ny melding og følger de vanlige reglene i navneloven — se blant annet § 10 om begrensninger."
            },
            {
                "q": "Gjelder fristen også for fornavn?",
                "a": "Ja. Både fornavn og etternavn må meldes inn innen 6 måneder."
            }
        ],
        "related": [
            {"lov": "navneloven", "paragraf": "1", "tittel": "Navneplikt", "available": True},
            {"lov": "navneloven", "paragraf": "5", "tittel": "Etternavn ved adopsjon", "available": True},
            {"lov": "navneloven", "paragraf": "12", "tittel": "Melding om navn for barn", "available": True},
        ],
    },
    {
        "number": "3",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Frie, beskyttede og nye etternavn",
        "kategori": "familie",
        "description": "Etternavn med over 200 bærere er fritt tilgjengelig. Sjeldnere navn krever samtykke fra alle som har det.",
        "kort_svar": "Har et etternavn over 200 bærere i Norge, kan du ta det fritt. Har det 200 eller færre, må alle som allerede har det si ja. Noen navn kan du ikke ta i det hele tatt — for eksempel kjente varemerkenavn.",
        "paragraftekst": "Navn som flere enn 200 personer her i riket har som etternavn, kan tas som etternavn av andre uten samtykke fra dem som allerede har det.\n\nNavn som 200 eller færre personer her i riket har som etternavn, kan bare tas som etternavn dersom alle som allerede har det som etternavn, samtykker.",
        "hva_betyr_html": """<p>Loven deler etternavn i tre grupper:</p>
<p><strong>Frie navn</strong> — mer enn 200 bærere i Norge. Du tar det bare. «Hansen», «Olsen», «Larsen» er eksempler. Ingen trenger å spørres.</p>
<p><strong>Beskyttede navn</strong> — 200 bærere eller færre. Du må ha skriftlig samtykke fra alle som har navnet. Det kan være én person eller hundre. Alle må si ja.</p>
<p><strong>Nye navn</strong> — navn som ikke finnes i Folkeregisteret som etternavn. Du kan i prinsippet lage noe helt nytt, men det er grenser: Navnet kan ikke forveksles med et beskyttet etternavn, et kjent varemerke eller firmanavn, og det kan ikke være et fornavn.</p>""",
        "eksempler": [
            {
                "navn": "Ingrid",
                "tekst": "Ingrid vil ta etternavnet «Falkenhaug» som hun fant i slektshistorien sin. Hun sjekker og finner at bare 3 familier i Norge har det. Hun trenger samtykke fra alle. Det tar tid, men er mulig."
            },
            {
                "navn": "Tom",
                "tekst": "Tom vil hete «Nike» til etternavn for å skille seg ut. Det godtas ikke — Nike er et kjent varemerke, og berettigede interesser vil lide skade."
            }
        ],
        "vanlige_feil": [
            "Tro at du fritt kan ta et sjeldent navn uten å spørre noen",
            "Ikke sjekke om et «nytt» navn likner på et beskyttet navn",
            "Tro at du kan ta et vanlig fornavn (som «Marte») som etternavn uten videre",
        ],
        "hva_bor_du_html": "<p>Sjekk Folkeregisteret eller kontakt skattekontoret for å finne ut hvor mange som har det aktuelle etternavnet. Trenger du samtykke, må det innhentes skriftlig fra alle.</p>",
        "dumme_sporsmal": [
            {
                "q": "Hvordan vet jeg om et navn er «beskyttet»?",
                "a": "Skattekontoret kan sjekke. Du kan også søke i Folkeregisteret. Under 200 bærere = beskyttet."
            },
            {
                "q": "Hva om én person nekter å gi samtykke?",
                "a": "Da kan du ikke ta navnet. Alle må samtykke — det holder ikke med flertall."
            },
            {
                "q": "Kan jeg lage et helt nytt etternavn?",
                "a": "Ja, i prinsippet. Men det kan ikke ligne på et beskyttet navn, et kjent merkenavn, eller et fornavn."
            }
        ],
        "related": [
            {"lov": "navneloven", "paragraf": "4", "tittel": "Avledede etternavn", "available": True},
            {"lov": "navneloven", "paragraf": "7", "tittel": "Doble etternavn", "available": True},
            {"lov": "navneloven", "paragraf": "10", "tittel": "Alminnelige begrensninger", "available": True},
        ],
    },
    {
        "number": "4",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Avledede etternavn — navn via slekt eller ekteskap",
        "kategori": "familie",
        "description": "Du kan ta etternavnet til ektefelle, foreldre, besteforeldre og lenger opp i slekten uten samtykke fra andre — uavhengig av 200-regelen.",
        "kort_svar": "Selv om et etternavn er sjeldent og «beskyttet» av 200-regelen, kan du ta det hvis du har det i nær slekt — helt tilbake til tippoldeforeldre. Du kan også ta ektefellens eller samboerens etternavn.",
        "paragraftekst": "Uavhengig av begrensningene i § 3 kan følgende navn tas som etternavn: navn som er eller har vært en av tippoldeforeldrenes, oldeforeldrenes, besteforeldrenes eller foreldrenes etternavn eller mellomnavn, navn som er eller har vært ektefellens etternavn eller mellomnavn, navn som er en av steforeldrenes eller fosterforeldrenes etternavn eller mellomnavn, etternavn eller mellomnavn som vedkommende har hatt tidligere.",
        "hva_betyr_html": """<p>§ 4 er «unntakslisten» — navn du kan ta uten å gå via 200-regelen i § 3.</p>
<p><strong>Slektsnavn langt bakover.</strong> Hadde tippoldemoren din etternavnet «Birkeland», kan du ta det — selv om det er sjeldent og «beskyttet».</p>
<p><strong>Ektefellens navn.</strong> Gifter du deg, kan du ta ektefellens etternavn.</p>
<p><strong>Samboerens navn.</strong> Samboere som har bodd sammen i minst 2 år, eller som har felles barn, har samme rett som ektefeller — forutsatt at samboeren samtykker.</p>
<p><strong>Navn du har hatt tidligere.</strong> Har du hatt et annet etternavn og vil tilbake til det, kan du det.</p>
<p><strong>Gårdsbruksnavn.</strong> Driver du eller foreldrene dine en gård med et bestemt navn i minst 10 år, kan du ta gårdsnavnet som etternavn.</p>""",
        "eksempler": [
            {
                "navn": "Eva",
                "tekst": "Eva giftet seg for 15 år siden og tok mannens etternavn. De skilles. Hun vil tilbake til det opprinnelige etternavnet sitt — Haugen. Det kan hun gjøre under § 4 nr. 7 uten å gå via samtykke-reglene."
            },
            {
                "navn": "Marius",
                "tekst": "Marius har funnet ut at tippoldemoren hans het «Fjelstad» — et sjeldent navn med bare 40 bærere. Han har ikke krav på samtykke fra dem — slektsregelen i § 4 nr. 1 gir ham rett til å ta det."
            }
        ],
        "vanlige_feil": [
            "Tro at man trenger samtykke fra alle nåværende bærere selv når man har slektstilknytning",
            "Glemme at navn ervervet ved ekteskap ikke kan brukes videre i neste ekteskap",
            "Ikke vite at samboere har samme rettigheter som ektefeller etter 2 år",
        ],
        "hva_bor_du_html": "<p>Dokumenter slektstilknytningen din — utskrift fra Folkeregisteret eller slektsgransking. Ta med dette til skattekontoret når du melder navnebytte.</p>",
        "dumme_sporsmal": [
            {
                "q": "Kan jeg ta mormors pikenavn selv om ingen i familien bruker det lenger?",
                "a": "Ja, hvis det var hennes etternavn eller mellomnavn. Regelen gjelder navn som «er eller har vært» brukt."
            },
            {
                "q": "Kan samboeren min ta etternavnet mitt uten at vi gifter oss?",
                "a": "Ja — hvis dere har bodd sammen i minst 2 år eller har felles barn, og du samtykker."
            },
            {
                "q": "Kan jeg ta et gårdsbruksnavn hvis foreldrene mine eier gården?",
                "a": "Ja. Loven sier «vedkommende eller en av dennes foreldre eier» — det holder at foreldrene eier den."
            }
        ],
        "related": [
            {"lov": "navneloven", "paragraf": "3", "tittel": "Frie, beskyttede og nye etternavn", "available": True},
            {"lov": "navneloven", "paragraf": "10", "tittel": "Alminnelige begrensninger (10-årsregel)", "available": True},
            {"lov": "navneloven", "paragraf": "11", "tittel": "Slik melder du navnebytte", "available": True},
        ],
    },
    {
        "number": "5",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Etternavn ved adopsjon",
        "kategori": "familie",
        "description": "Adopteres et barn under 18 år, får det som regel adoptantens etternavn. Men foreldrene kan bestemme noe annet i forbindelse med adopsjonen.",
        "kort_svar": "Adopteres et barn under 18 år av én person, får barnet den personens etternavn. Adopterer to ektefeller eller samboere, får barnet adoptivmorens etternavn — med mindre noe annet bestemmes under adopsjonen.",
        "paragraftekst": "Hvis en person under 18 år blir adoptert, får han eller hun adoptantens etternavn med mindre annet er fastsatt i forbindelse med adopsjonen. Når ektefeller eller samboere sammen adopterer noen som er under 18 år, får adoptivbarnet adoptivmorens etternavn med mindre annet er fastsatt i forbindelse med adopsjonen.",
        "hva_betyr_html": """<p>Regelen er enkel: adopsjon gir som utgangspunkt adoptantens etternavn.</p>
<p><strong>Én adoptant:</strong> barnet får den personens etternavn.</p>
<p><strong>To adoptanter (ektepar eller samboere):</strong> barnet får adoptivmorens etternavn.</p>
<p>Men dette er bare utgangspunktet — det kan bestemmes noe annet under selve adopsjonsprosessen.</p>
<p><strong>Unntaket:</strong> Adopterer den ene ektefellen eller samboeren den andres biologiske barn (stebarnsadopsjon), gjelder ikke disse reglene.</p>""",
        "eksempler": [
            {
                "navn": "Anne og Lars",
                "tekst": "Anne og Lars adopterer en 7-åring fra utlandet. Barnet har et fremmed etternavn som foreldrene ønsker å beholde som mellomnavn, mens barnet tar Annes etternavn «Vik». De avklarer dette i adopsjonssaken, og det blir registrert slik i Folkeregisteret."
            }
        ],
        "vanlige_feil": [
            "Tro at barnet automatisk får farens etternavn — det er morens som er utgangspunktet",
            "Glemme at man kan bestemme annet under adopsjonsprosessen",
            "Tro at reglene gjelder stebarnsadopsjon — det gjør de ikke",
        ],
        "hva_bor_du_html": "<p>Diskuter navnespørsmålet tidlig i adopsjonsprosessen — gjerne med advokat eller Bufetat. Ønsker du et annet opplegg enn lovens standard, er adopsjonssaken det rette tidspunktet å si fra.</p>",
        "dumme_sporsmal": [
            {
                "q": "Kan adoptivbarnet beholde sitt opprinnelige etternavn?",
                "a": "Ja, det kan fastsettes i forbindelse med adopsjonen."
            },
            {
                "q": "Kan et adoptert barn senere ta navn fra sin biologiske slekt?",
                "a": "Ja — § 4 sier at den adopterte kan ta navn etter biologisk slekt i tillegg til adoptivslekten."
            }
        ],
        "related": [
            {"lov": "navneloven", "paragraf": "4", "tittel": "Avledede etternavn", "available": True},
            {"lov": "navneloven", "paragraf": "2", "tittel": "Plikt til å velge navn for barn", "available": True},
            {"lov": "navneloven", "paragraf": "12", "tittel": "Melding om navn for barn", "available": True},
        ],
    },
    {
        "number": "6",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Stavemåteendring — er det det samme som navnebytte?",
        "kategori": "familie",
        "description": "Du kan endre stavemåten på etternavnet ditt uten at det regnes som et nytt navn — og slipper da de vanlige begrensningene.",
        "kort_svar": "Vil du endre stavemåten på etternavnet ditt — for eksempel fra «Christiansen» til «Kristiansen» — regnes ikke det som å ta et nytt navn. Det samme gjelder å bytte kjønnsendelse eller tilpasse til internasjonale bokstaver.",
        "paragraftekst": "En endring av stavemåten av et etternavn som bringer stavemåten nærmere den alminnelige uttalen av navnet eller nærmere skriftspråket for øvrig, regnes ikke som å ta et annet navn. Det samme gjelder en endring av stavemåten til bokstaver som er alminnelig kjent i utlandet. En endring av et etternavns kjønnsbestemte ending regnes ikke som å ta et annet navn.",
        "hva_betyr_html": """<p>Noen navneendringer er så små at loven ikke behandler dem som et «nytt» navn. Det gjelder tre tilfeller:</p>
<p><strong>Stavemåte nærmere uttale.</strong> «Christiansen» → «Kristiansen». Eller «Qvale» → «Kvale». Samme navn, enklere å stave.</p>
<p><strong>Internasjonale bokstaver.</strong> «Bjørnsen» → «Bjornsen». Praktisk for nordmenn som bor i utlandet.</p>
<p><strong>Kjønnsendelse.</strong> Å endre endelsen regnes ikke som nytt navn.</p>
<p><strong>Konsekvensen:</strong> Du slipper 10-årsregelen og de andre begrensningene i § 10.</p>""",
        "eksempler": [
            {
                "navn": "Kari",
                "tekst": "Kari heter Christiansen i Folkeregisteret, men har alltid skrevet Kristiansen. Hun melder inn rettingen. Det godtas uten problemer fordi stavemåten nå reflekterer uttalen."
            }
        ],
        "vanlige_feil": [
            "Tro at store stavemåteendringer er «bare» en stavemåteendring — grensen er reell",
            "Glemme at man likevel må melde endringen inn til skattekontoret",
        ],
        "hva_bor_du_html": "<p>Meld endringen til skattekontoret. Begrunn kort at det er en stavemåtejustering mot uttale eller internasjonale bokstaver. Det er raskt og enkelt.</p>",
        "dumme_sporsmal": [
            {
                "q": "Kan jeg endre «Hansen» til «Hanssen» etter § 6?",
                "a": "Muligens — det avhenger av om det bringer stavemåten nærmere uttalen. Skattekontoret vurderer det."
            },
            {
                "q": "Må jeg vente 10 år mellom slike justeringer?",
                "a": "Nei. Siden det ikke regnes som nytt navn, gjelder ikke 10-årsregelen."
            }
        ],
        "related": [
            {"lov": "navneloven", "paragraf": "3", "tittel": "Frie, beskyttede og nye etternavn", "available": True},
            {"lov": "navneloven", "paragraf": "10", "tittel": "Alminnelige begrensninger", "available": True},
            {"lov": "navneloven", "paragraf": "11", "tittel": "Slik melder du navnebytte", "available": True},
        ],
    },
    {
        "number": "7",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Doble etternavn — kan jeg ha to etternavn med bindestrek?",
        "kategori": "familie",
        "description": "Du kan sette sammen to lovlige etternavn med bindestrek til ett dobbelt etternavn. Hvert av de to delene vurderes separat etter navnelovens regler.",
        "kort_svar": "Du kan ta to etternavn og slå dem sammen med bindestrek — for eksempel «Hansen-Berg». Begge navn må hver for seg kunne tas som etternavn etter loven.",
        "paragraftekst": "To navn som kan tas som etternavn, kan tas som et dobbelt etternavn der de to navnene er satt sammen med bindestrek. I forhold til §§ 3 og 4 regnes et dobbelt etternavn som to adskilte etternavn.",
        "hva_betyr_html": """<p>Ønsker du å kombinere to etternavn, kan du det — men begge deler må kvalifisere som etternavn etter reglene i § 3 eller § 4. Det er ingen «rabatt» fordi du setter dem sammen.</p>
<p>Praktisk eksempel: «Persen-Andersen». «Persen» er fritt fordi mange har det. «Andersen» er fritt fordi enda flere har det. Da er kombinasjonen tillatt.</p>
<p>Du kan ikke bruke et dobbelt etternavn som snarveien til å ta et ellers beskyttet navn.</p>""",
        "eksempler": [
            {
                "navn": "Ingrid og Ola",
                "tekst": "Ingrid Bakken og Ola Moen gifter seg. De vil begge ha begges etternavn. Ingrid tar «Bakken-Moen», Ola tar «Moen-Bakken». Begge navn er frie, og kombinasjonene godtas."
            }
        ],
        "vanlige_feil": [
            "Tro at du kan «smugle inn» et beskyttet navn som del av et dobbelnavn uten samtykke",
            "Tro at dobbelt etternavn er det samme som mellomnavn",
        ],
        "hva_bor_du_html": "<p>Sjekk at begge navn er tillatt hver for seg, meld så inn kombinasjonen til skattekontoret.</p>",
        "dumme_sporsmal": [
            {
                "q": "Kan barna mine arve det doble etternavnet mitt?",
                "a": "Ja — de kan ta det etter § 4, som gjelder etternavn foreldren «er eller har vært» bærer av."
            },
            {
                "q": "Kan jeg ha tre etternavn?",
                "a": "Nei. Loven tillater bare ett enkelt eller ett dobbelt etternavn."
            },
            {
                "q": "Er dobbelt etternavn det samme som mellomnavn?",
                "a": "Nei. Mellomnavn står mellom fornavn og etternavn og er valgfritt. Dobbelt etternavn er selve etternavnet."
            }
        ],
        "related": [
            {"lov": "navneloven", "paragraf": "3", "tittel": "Frie, beskyttede og nye etternavn", "available": True},
            {"lov": "navneloven", "paragraf": "9", "tittel": "Mellomnavn", "available": True},
        ],
    },
    {
        "number": "8",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Fornavn — er det noe man ikke kan hete?",
        "kategori": "familie",
        "description": "Du kan ikke velge et navn som er registrert som etternavn i Folkeregisteret — med mindre det har tradisjon som fornavn i Norge eller utlandet.",
        "kort_svar": "Du kan ikke gi barnet ditt et fornavn som er registrert som etternavn i Folkeregisteret — med mindre det har tradisjon som fornavn i Norge eller et annet land. Det finnes ingen liste over «godkjente» fornavn.",
        "paragraftekst": "Som fornavn kan det ikke velges et navn som er registrert i Folkeregisteret som et navn som er eller har vært i bruk som etternavn eller mellomnavn. Navnet kan likevel tas som fornavn dersom det har opphav eller tradisjon som fornavn i Norge eller i utlandet.",
        "hva_betyr_html": """<p>Navneloven setter ikke opp en liste over tillatte fornavn. Det er ganske fritt — men med én grense: du kan ikke ta et navn som brukes eller har blitt brukt som etternavn i Norge, med mindre det finnes tradisjon for å bruke det som fornavn.</p>
<p>«Hansen» er et typisk etternavn. Å kalle barnet «Hansen» som fornavn ville ikke godtas. Men «Markus», «Signe» eller «Astrid» er alltid brukt som fornavn — ingen problem.</p>
<p>Mange utenlandske navn faller i gråsonen. «Kim» kan for eksempel være fornavn i Skandinavia og etternavn i Korea — der vil tradisjon som fornavn i utlandet gi grønt lys.</p>""",
        "eksempler": [
            {
                "navn": "Sara",
                "tekst": "Sara og Petter vil kalle datteren sin «Storm». Det er registrert som etternavn i Folkeregisteret — men skattekontoret godtar det fordi det har voksende tradisjon som fornavn i Norge."
            }
        ],
        "vanlige_feil": [
            "Tro at myndighetene godkjenner alle utenlandske navn automatisk — vurderingen skjer case by case",
            "Tro at det finnes en offisiell liste over tillatte fornavn — det gjør det ikke",
        ],
        "hva_bor_du_html": "<p>Er du usikker på om et navn godtas, kontakt skattekontoret på forhånd. De kan si om et navn trolig vil godkjennes.</p>",
        "dumme_sporsmal": [
            {
                "q": "Kan jeg kalle barnet mitt et kjønnsnøytralt navn?",
                "a": "Ja. Loven sier ingenting om kjønn i fornavn. «Kim», «Robin» og «Alex» er alle tillatt."
            },
            {
                "q": "Kan vi bruke et familienavn som fornavn?",
                "a": "Avhenger av om det er registrert som etternavn i Folkeregisteret, og om det har fornavn-tradisjon."
            }
        ],
        "related": [
            {"lov": "navneloven", "paragraf": "9", "tittel": "Mellomnavn", "available": True},
            {"lov": "navneloven", "paragraf": "10", "tittel": "Alminnelige begrensninger", "available": True},
        ],
    },
    {
        "number": "9",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Mellomnavn",
        "kategori": "familie",
        "description": "Et mellomnavn må kvalifisere som lovlig etternavn. Du kan ikke ta et navn som mellomnavn som du ikke kunne tatt som etternavn.",
        "kort_svar": "Mellomnavn er valgfritt. Men det må følge de samme reglene som etternavn — du kan bare ta et mellomnavn som du faktisk har lov til å ta som etternavn.",
        "paragraftekst": "Navn som kan tas som etternavn, kan tas som mellomnavn.",
        "hva_betyr_html": """<p>Enkelt: reglene for hva du kan bruke som etternavn (§§ 3 og 4) gjelder tilsvarende for mellomnavn. Mellomnavn er ikke en friport der alt er lov.</p>
<p>Vil du for eksempel bruke et sjeldent beskyttet navn som mellomnavn, trenger du samtykke fra alle bærere — akkurat som om du ville bruke det som etternavn.</p>""",
        "eksempler": [
            {
                "navn": "Lars",
                "tekst": "Lars vil ha morens pikenavn «Skomedal» som mellomnavn. Det er et sjeldent etternavn. Fordi det var morens etternavn, kan han ta det etter § 4 nr. 1 — og dermed kan han også bruke det som mellomnavn."
            }
        ],
        "vanlige_feil": [
            "Tro at mellomnavn er unntatt fra 200-regelen og samtykke-kravene",
        ],
        "hva_bor_du_html": "<p>Vil du ta et beskyttet navn som mellomnavn, sjekk om du har krav på det via § 4 (slekt eller ekteskap) — da trenger du ikke samtykke.</p>",
        "dumme_sporsmal": [
            {
                "q": "Kan jeg droppe mellomnavnet mitt?",
                "a": "Ja — mellomnavn er valgfritt og kan sløyfes. Det meldes inn til skattekontoret."
            },
            {
                "q": "Kan mellomnavn forveksles med dobbelt etternavn?",
                "a": "I dagligtale ja — men juridisk er det forskjell. Mellomnavn står mellom fornavn og etternavn, og brukes ikke alene som etternavn."
            }
        ],
        "related": [
            {"lov": "navneloven", "paragraf": "3", "tittel": "Frie, beskyttede og nye etternavn", "available": True},
            {"lov": "navneloven", "paragraf": "7", "tittel": "Doble etternavn", "available": True},
        ],
    },
    {
        "number": "10",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Alminnelige begrensninger — hvor ofte kan jeg bytte navn?",
        "kategori": "familie",
        "description": "Over 16 år kan du som regel bare bytte navn én gang per 10 år. Det finnes unntak — blant annet ved ekteskap, skilsmisse og særlige grunner.",
        "kort_svar": "Du kan normalt bare bytte navn én gang per 10 år etter du er fylt 16 år. Unntak finnes ved ekteskap, skilsmisse og stebarnsadopsjon — og hvis det foreligger særlige grunner.",
        "paragraftekst": "Selv om de øvrige vilkår er oppfylt, skal en melding om å ta, endre eller sløyfe navn ikke godtas dersom vedkommendes personnavn ellers kan bli til vesentlig ulempe for vedkommende eller andre sterke grunner tilsier det.\n\nPersoner over 16 år kan ikke ta, endre eller sløyfe fornavn eller etternavn mer enn en gang hvert tiende år.",
        "hva_betyr_html": """<p><strong>Vesentlig ulempe-regelen.</strong> Selv om du oppfyller alle vilkår, kan skattekontoret avslå hvis navnet vil skape vesentlig ulempe — for deg eller andre.</p>
<p><strong>10-årsregelen.</strong> Etter du er 16, kan du normalt bare bytte navn én gang per tiår. Det gjelder både fornavn og etternavn.</p>
<p>Men unntakene er viktige: du kan bytte ut over én gang på 10 år hvis du gifter deg eller inngår samboerskap, tar tilbake et gammelt navn, tar navn etter stef- eller fosterforeldre, angrer på et navnebytte og vil tilbake — eller hvis det foreligger særlige grunner.</p>""",
        "eksempler": [
            {
                "navn": "Eva",
                "tekst": "Eva byttet fornavn for 3 år siden. Nå angrer hun og vil ha det gamle fornavnet tilbake. Det er tillatt — hun kan gå tilbake til det opprinnelige fornavnet uten å vente ut 10-årsperioden."
            },
            {
                "navn": "Marius",
                "tekst": "Marius byttet etternavn for 2 år siden. Nå vil han bytte igjen — bare fordi han ombestemte seg. Det godtas trolig ikke. Han er inne i 10-årsperioden og har ingen livshendelse å vise til."
            }
        ],
        "vanlige_feil": [
            "Tro at man kan bytte navn fritt så mange ganger man vil",
            "Glemme at giftemål åpner for navnebytte utenfor 10-årsregelen",
            "Ikke vite at «angre-retten» gjelder — du kan gå tilbake til fornavnet du hadde",
        ],
        "hva_bor_du_html": "<p>Tenk deg godt om før du bytter navn. Er du innenfor 10-årsperioden og vil bytte likevel, sjekk om ett av unntakene gjelder. Ta kontakt med skattekontoret hvis du er usikker.</p>",
        "dumme_sporsmal": [
            {
                "q": "Kan jeg bytte navn igjen hvis jeg gifter meg etter å ha byttet for 2 år siden?",
                "a": "Ja — ekteskap er et eksplisitt unntak fra 10-årsregelen."
            },
            {
                "q": "Hva er «særlige grunner»?",
                "a": "Et skjønnsmessig unntak. Typisk: forfølgelse, alvorlig ulempe med nåværende navn, eller tilsvarende sterke personlige grunner."
            },
            {
                "q": "Gjelder 10-årsregelen for barn?",
                "a": "Nei — den gjelder bare for personer over 16 år."
            }
        ],
        "related": [
            {"lov": "navneloven", "paragraf": "3", "tittel": "Frie, beskyttede og nye etternavn", "available": True},
            {"lov": "navneloven", "paragraf": "4", "tittel": "Avledede etternavn", "available": True},
            {"lov": "navneloven", "paragraf": "11", "tittel": "Slik melder du navnebytte", "available": True},
        ],
    },
    {
        "number": "11",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Slik melder du navnebytte",
        "kategori": "familie",
        "description": "Navnebytter meldes til skattekontoret. Avslag kan klages til statsforvalteren.",
        "kort_svar": "Du melder navnebytte til skattekontoret. De godtar eller avslår. Får du avslag, kan du klage til statsforvalteren.",
        "paragraftekst": "Den som vil ta, endre eller sløyfe navn, må gi melding om det til skattekontoret, som avgjør om meldingen skal godtas. Vedtak om å godta eller nekte å godta en melding kan påklages til statsforvalteren.",
        "hva_betyr_html": """<p>Vil du bytte navn, er skattekontoret rett adresse — ikke tingretten, ikke kommunen. Du sender inn en melding (skjema), og skattekontoret avgjør om det godtas etter navnelovens regler.</p>
<p>Får du nei, kan du klage til statsforvalteren i ditt fylke. Klagen er gratis.</p>""",
        "eksempler": [],
        "vanlige_feil": [
            "Kontakte tingretten eller kommunen i stedet for skattekontoret",
            "Ikke klage på avslag — klageadgangen er gratis og reell",
        ],
        "hva_bor_du_html": "<p>Gå til skatteetaten.no og bruk det digitale skjemaet for navnemelding. Du trenger BankID. Behandlingstiden er vanligvis noen uker.</p>",
        "dumme_sporsmal": [
            {
                "q": "Er navnebytte gratis?",
                "a": "Ja, det er ingen gebyr for å melde navnebytte."
            },
            {
                "q": "Hvor lang tid tar det?",
                "a": "Vanligvis 2–4 uker, men det varierer."
            },
            {
                "q": "Kan jeg klage hvis jeg får avslag?",
                "a": "Ja — til statsforvalteren i ditt fylke. Klagen sendes via skattekontoret."
            }
        ],
        "related": [
            {"lov": "navneloven", "paragraf": "10", "tittel": "Alminnelige begrensninger", "available": True},
            {"lov": "navneloven", "paragraf": "12", "tittel": "Melding om navn for barn", "available": True},
        ],
    },
    {
        "number": "12",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Melding om navn for barn — hvem kan bytte?",
        "kategori": "familie",
        "description": "Navnebytte for barn under 16 år krever samtykke fra den med foreldreansvar. Barn over 12 år må selv samtykke.",
        "kort_svar": "For barn under 16 år er det foreldrene med foreldreansvar som melder navnebytte. Er barnet over 12 år, må barnet selv si ja. Er barnet under 16 men over 12, kreves altså begge delers samtykke.",
        "paragraftekst": "Melding om å ta, endre eller sløyfe navn for noen som ikke har fylt 16 år, skal fremsettes av den eller de som har foreldreansvaret, eller disse må ha samtykket i meldingen. Gjelder meldingen et barn over 12 år, må også barnet selv ha samtykket.",
        "hva_betyr_html": """<p>Tre alderstrinn:</p>
<p><strong>Under 12 år:</strong> Foreldrene med foreldreansvar bestemmer alene.</p>
<p><strong>12–15 år:</strong> Foreldrene bestemmer, men barnet må si ja.</p>
<p><strong>16 år og over:</strong> Barnet melder selv — og 10-årsregelen begynner å gjelde.</p>
<p>Hvis én forelder vil bytte barnets navn uten at den andre (med foreldreansvar) er enig, kan ikke meldingen godtas. Begge med foreldreansvar må stå bak.</p>""",
        "eksempler": [
            {
                "navn": "Petter og Kari",
                "tekst": "Petter og Kari er skilt. Kari vil bytte etternavnet til sin 10-årige datter. Petter har del i foreldreansvaret og nekter. Skattekontoret godtar ikke meldingen — begge med foreldreansvar må samtykke."
            }
        ],
        "vanlige_feil": [
            "Tro at den ene forelderen kan bytte barnets navn alene ved delt foreldreansvar",
            "Glemme å innhente barnets eget samtykke når det er over 12 år",
        ],
        "hva_bor_du_html": "<p>Avklar med den andre forelderen før du sender inn melding. Er barnet over 12, sørg for at barnet signerer eller bekrefter samtykke.</p>",
        "dumme_sporsmal": [
            {
                "q": "Kan skattekontoret godta meldingen uten samtykke i spesielle situasjoner?",
                "a": "Ja — loven sier at meldingen kan godtas «dersom det foreligger særlig grunn», selv uten samtykke."
            },
            {
                "q": "Kan barnet selv bytte navn fra fylte 16?",
                "a": "Ja — fra 16 år sender barnet selv meldingen, og 10-årsregelen gjelder fra da av."
            }
        ],
        "related": [
            {"lov": "navneloven", "paragraf": "10", "tittel": "Alminnelige begrensninger", "available": True},
            {"lov": "navneloven", "paragraf": "11", "tittel": "Slik melder du navnebytte", "available": True},
        ],
    },
    {
        "number": "13",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Søksmål ved navnekrenkelse",
        "kategori": "familie",
        "description": "Mener du at et navnebytte krenker dine rettigheter, kan du gå til retten — men du må gjøre det innen 2 år fra du fikk vite om vedtaket.",
        "kort_svar": "Har skattekontoret godkjent at noen tar et navn du mener de ikke har rett til, kan du reise søksmål. Fristen er 2 år fra du fikk vite om vedtaket — og uansett senest 10 år etter at vedtaket ble fattet.",
        "paragraftekst": "Er noens rettigheter krenket ved et vedtak som godtar en melding om å ta, endre eller sløyfe navn, kan vedkommende gjøre sin rett gjeldende ved søksmål innen to år etter at vedkommende fikk eller burde skaffet seg kunnskap om vedtaket. Søksmålet må være reist innen 10 år etter at vedtaket ble truffet.",
        "hva_betyr_html": """<p>Loven gir deg rett til å gå til retten hvis du mener at noen urettmessig har fått lov til å ta et navn som krenker rettighetene dine — for eksempel et beskyttet familienavn der samtykke ble omgått.</p>
<p>To frister: Du har 2 år fra du visste (eller burde visst) om vedtaket. Søksmålet må uansett reises innen 10 år fra vedtaket. Begge frister gjelder — den strengeste styrer.</p>""",
        "eksempler": [],
        "vanlige_feil": [
            "Vente for lenge — 2-årsfristen løper fra du fikk kunnskap, ikke fra du bestemte deg",
            "Tro at klagen til statsforvalteren stopper fristen for søksmål",
        ],
        "hva_bor_du_html": "<p>Mener du at noen ulovlig har tatt «ditt» navn — kontakt advokat raskt. Fristene er absolutte.</p>",
        "dumme_sporsmal": [
            {
                "q": "Hvem kan reise søksmål?",
                "a": "Den hvis rettigheter er krenket — typisk noen som allerede bærer et beskyttet navn."
            },
            {
                "q": "Hva kan retten bestemme?",
                "a": "At vedtaket var ugyldig og at navnet ikke kan brukes."
            }
        ],
        "related": [
            {"lov": "navneloven", "paragraf": "3", "tittel": "Frie, beskyttede og nye etternavn", "available": True},
            {"lov": "navneloven", "paragraf": "11", "tittel": "Meldeplikt og forvaltningsorgan", "available": True},
        ],
    },
    {
        "number": "14",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Hvem gjelder loven for?",
        "kategori": "familie",
        "description": "Navneloven gjelder alle som er registrert bosatt i Norge og har til hensikt å bli boende her. Utenlandske statsborgere kan også melde navneendring etter hjemlandets regler.",
        "kort_svar": "Navneloven gjelder deg hvis du er registrert bosatt i Norge i Folkeregisteret og har til hensikt å bli boende her — uansett om du er norsk eller utenlandsk statsborger.",
        "paragraftekst": "Loven gjelder for alle som i Folkeregisteret er registrert som bosatt her i riket og har til hensikt å bli boende her varig.\n\nDen som omfattes av første ledd og er utenlandsk statsborger, kan her i riket inngi melding om å ta, endre eller sløyfe navn i samsvar med avgjørelse truffet av statsborgerlandets myndigheter.",
        "hva_betyr_html": """<p><strong>Norske statsborgere bosatt i Norge:</strong> Loven gjelder fullt ut.</p>
<p><strong>Utenlandske statsborgere bosatt i Norge:</strong> Loven gjelder, men de kan i tillegg bruke navnerettsregler fra hjemlandet — for eksempel hvis hjemlandet allerede har godkjent et navnebytte.</p>
<p><strong>Nordmenn bosatt i utlandet:</strong> Kongen kan gi forskrifter om hva som gjelder. Sjekk med nærmeste norske ambassade.</p>""",
        "eksempler": [],
        "vanlige_feil": [
            "Tro at loven ikke gjelder for EU-borgere som jobber og bor i Norge",
        ],
        "hva_bor_du_html": "<p>Er du utenlandsk statsborger med et navnebytte godkjent i hjemlandet, kan du melde det inn til norsk skattekontor med dokumentasjon fra hjemlandets myndigheter.</p>",
        "dumme_sporsmal": [
            {
                "q": "Jeg er EU-borger og jobber i Norge — gjelder loven meg?",
                "a": "Ja, hvis du er registrert i Folkeregisteret og har til hensikt å bli boende her varig."
            },
            {
                "q": "Kan jeg bruke et navnebytte godkjent i hjemlandet mitt?",
                "a": "Ja — som utenlandsk statsborger kan du melde inn en navneendring som er godkjent av myndighetene i statsborgerlandet."
            }
        ],
        "related": [
            {"lov": "navneloven", "paragraf": "1", "tittel": "Navneplikt", "available": True},
            {"lov": "navneloven", "paragraf": "11", "tittel": "Meldeplikt og forvaltningsorgan", "available": True},
        ],
    },
    {
        "number": "15",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Ikrafttredelse",
        "kategori": "familie",
        "description": "Navneloven trådte i kraft 1. januar 2003 og erstattet den tidligere loven om personnamn fra 1964.",
        "kort_svar": "Navneloven trådte i kraft 1. januar 2003. Fra samme dato opphørte den gamle loven om personnamn fra 1964 å gjelde.",
        "paragraftekst": "Loven gjelder fra den tid Kongen bestemmer. Fra samme tid opphører lov 29. mai 1964 nr. 1 om personnamn å gjelde.",
        "hva_betyr_html": "<p>Dette er en ren teknisk bestemmelse. Resolusjonen ble fattet 7. juni 2002, og loven trådte i kraft 1. januar 2003. For deg som bruker betyr det at alle navnesaker etter 1. januar 2003 følger denne loven.</p>",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "<p>Denne paragrafen har ingen praktisk betydning for de fleste navnesaker i dag.</p>",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "navneloven", "paragraf": "16", "tittel": "Overgangsregler", "available": True},
        ],
    },
    {
        "number": "16",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Overgangsregler — doble etternavn uten bindestrek fra før 2003",
        "kategori": "familie",
        "description": "Hadde du et dobbelt etternavn uten bindestrek før navneloven trådte i kraft i 2003, kan du beholde det slik.",
        "kort_svar": "Hadde du et dobbelt etternavn skrevet med mellomrom (ikke bindestrek) da loven trådte i kraft 1. januar 2003, kan du beholde det i den formen. Du trenger ikke endre det.",
        "paragraftekst": "Den som ved lovens ikrafttredelse har etternavn som består av to navn adskilt av mellomrom, kan selv beholde navnet i denne formen.\n\nEtternavn som ved lovens ikrafttredelse består av to navn forbundet med bindestrek, anses som et dobbelt etternavn bestående av to etternavn.",
        "hva_betyr_html": """<p>Den nye navneloven fra 2003 krever bindestrek i doble etternavn. Men noen hadde allerede slike navn skrevet med mellomrom — for eksempel «Hansen Berg» i stedet for «Hansen-Berg».</p>
<p>Loven sier: du trenger ikke endre det. Du kan beholde mellomromsformen livet ut hvis du vil.</p>""",
        "eksempler": [
            {
                "navn": "Ingrid",
                "tekst": "Ingrid het «Holm Berg» (med mellomrom) siden 1987. Da navneloven kom i 2003, fikk hun beskjed om at hun kunne beholde formen. Hun valgte det — og heter fortsatt «Holm Berg» i Folkeregisteret."
            }
        ],
        "vanlige_feil": [
            "Tro at overgangsregelen gjelder for barna — barna registreres etter gjeldende rett med bindestrek",
        ],
        "hva_bor_du_html": "<p>Vil du frivillig gå over til bindestrekformen, kan det gjøres via § 6 som en stavemåtejustering.</p>",
        "dumme_sporsmal": [
            {
                "q": "Kan jeg frivillig gå over til bindestrekformen?",
                "a": "Ja — det kan gjøres via § 6, siden det ikke regnes som å ta et nytt navn."
            },
            {
                "q": "Gjelder overgangsregelen også for barna mine?",
                "a": "Nei. Barna registreres etter gjeldende rett og må ha bindestrek i et dobbelt etternavn."
            }
        ],
        "related": [
            {"lov": "navneloven", "paragraf": "7", "tittel": "Doble etternavn", "available": True},
            {"lov": "navneloven", "paragraf": "6", "tittel": "Endringer i samme etternavn", "available": True},
        ],
    },
    {
        "number": "17",
        "lov": "navneloven",
        "lov_display": "Navneloven",
        "title": "Endringer i andre lover",
        "kategori": "familie",
        "description": "Da navneloven trådte i kraft i 2003 ble en rekke andre lover endret tilsvarende. Denne paragrafen er rent teknisk.",
        "kort_svar": "§ 17 er en teknisk følgeparagraf. Den listet opp hvilke andre lover som måtte endres da navneloven kom i 2003. Den har ingen praktisk betydning for navnesaker i dag.",
        "paragraftekst": "Fra den tid loven her trer i kraft, gjøres følgende endringer i andre lover: – – –",
        "hva_betyr_html": "<p>Når en ny lov vedtas, må ofte en rekke andre lover oppdateres. § 17 er stedet der slike tekniske endringer ble samlet. Selve innholdet i endringene er nå innarbeidet i de respektive lovene og gjelder ikke lenger som eget regelsett.</p>",
        "eksempler": [],
        "vanlige_feil": [],
        "hva_bor_du_html": "<p>Du trenger ikke forholde deg til denne paragrafen.</p>",
        "dumme_sporsmal": [],
        "related": [
            {"lov": "navneloven", "paragraf": "15", "tittel": "Ikrafttredelse", "available": True},
            {"lov": "navneloven", "paragraf": "16", "tittel": "Overgangsregler", "available": True},
        ],
    },
]
