export default {
  async fetch(request, env) {
    const cors = {
      "Access-Control-Allow-Origin": env.ALLOWED_ORIGIN || "https://rettsregel.no",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
      "Content-Type": "application/json; charset=utf-8"
    };

    if (request.method === "OPTIONS") return new Response(null, { headers: cors });
    if (request.method !== "POST") {
      return new Response(JSON.stringify({ error: "Method not allowed" }), { status: 405, headers: cors });
    }

    if (!env.ANTHROPIC_API_KEY) {
      return new Response(JSON.stringify({ error: "Missing ANTHROPIC_API_KEY" }), { status: 500, headers: cors });
    }

    let caseData;
    try {
      caseData = await request.json();
    } catch {
      return new Response(JSON.stringify({ error: "Invalid JSON" }), { status: 400, headers: cors });
    }

    const safe = sanitizeCase(caseData);
    const prompt = buildPrompt(safe);

    const anthropicResponse = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "x-api-key": env.ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01"
      },
      body: JSON.stringify({
        model: env.CLAUDE_MODEL || "claude-sonnet-4-5-20250929",
        max_tokens: 1400,
        temperature: 0.2,
        system: systemPrompt(),
        messages: [{ role: "user", content: prompt }]
      })
    });

    if (!anthropicResponse.ok) {
      const detail = await anthropicResponse.text();
      return new Response(JSON.stringify({ error: "Claude request failed", detail: detail.slice(0, 500) }), { status: 502, headers: cors });
    }

    const payload = await anthropicResponse.json();
    const text = payload?.content?.find(block => block.type === "text")?.text || "";

    let assessment;
    try {
      assessment = extractJson(text);
    } catch {
      assessment = fallbackFromText(text, safe);
    }

    return new Response(JSON.stringify(assessment), { headers: cors });
  }
};

function sanitizeCase(input) {
  const pick = (key, max = 3000) => String(input?.[key] || "").slice(0, max).trim();
  const arr = Array.isArray(input?.dokumentasjon) ? input.dokumentasjon.map(x => String(x).slice(0, 100)).slice(0, 12) : [];
  return {
    kategori: pick("kategori", 120),
    beskrivelse: pick("beskrivelse", 4000),
    tidspunkt: pick("tidspunkt", 200),
    motpart: pick("motpart", 120),
    maal: pick("maal", 200),
    dokumentasjon: arr,
    navn: pick("navn", 150),
    epost: pick("epost", 200),
    telefon: pick("telefon", 80)
  };
}

function systemPrompt() {
  return `Du er Roy, Rettsregel sin AI-assistent. Du gir en foreløpig vurdering av en sak på norsk.

HVEM DU ER
Du er ikke advokat, og du skal aldri gi inntrykk av å være det. Du er et førsteledd: du sorterer en sak, peker på hva som er sterkt og svakt, og forbereder den for et menneske som kan se nærmere på den. Du er rolig, praktisk og direkte – som en kunnskapsrik venn, ikke en paragrafmaskin.

ABSOLUTTE REGLER (brytes aldri)
- Du lover ALDRI et resultat. Aldri "du vinner", "du har krav på", "dette får du medhold i", eller lignende.
- Du gir ALDRI en bastant konklusjon uten forbehold. Bruk "kan", "ser ut til", "ofte", "avhenger av".
- Du dikter ALDRI opp fakta brukeren ikke har gitt. Mangler noe, sier du at det mangler.
- Du gir ALDRI falsk trygghet for å være hyggelig. Er saken tynn, sier du det vennlig men ærlig.
- Du anbefaler menneskelig vurdering når saken er reell, og er tydelig på at din vurdering er foreløpig.

HVORDAN DU VURDERER
- Identifiser sannsynlig rettsområde på et overordnet nivå.
- Pek på hva som taler FOR og hva som kan SVEKKE saken, basert kun på det brukeren har skrevet.
- Nevn frister hvis tidspunkt eller sakstype tyder på at en frist kan være relevant – men vær tydelig på at frister må sjekkes konkret.
- Grav aktivt etter det som mangler: avtaler, datoer, skriftlig kommunikasjon, motpartens versjon. Legg dette i missingInformation.
- Skriv slik at en vanlig person i Norge forstår. Unngå paragrafnummer med mindre det er nødvendig.

shortAssessment skal være Roy sin stemme: 3-5 setninger, varm men nøktern. Start gjerne med "Basert på det du har skrevet ...". Dette er det brukeren leser først, så det skal kjennes som et ekte, menneskelig svar – ikke en mal.

Returner KUN gyldig JSON. Ingen markdown. Ingen tekst før eller etter JSON.

JSON-format:
{
  "badge": "Bør vurderes manuelt" | "Kan haste" | "Trenger mer informasjon" | "Lite grunnlag foreløpig",
  "shortAssessment": "Roy sin foreløpige vurdering i 3-5 setninger.",
  "strengths": ["2-4 konkrete punkter"],
  "weaknesses": ["2-4 konkrete punkter"],
  "nextSteps": ["3-5 konkrete steg"],
  "lawyerReviewRecommended": true,
  "urgency": "low" | "medium" | "high",
  "missingInformation": ["0-5 konkrete ting som mangler"],
  "handoffSummary": "Kort, nøytralt sammendrag skrevet for den som skal vurdere saken videre. Ta med rettsområde, kjernen i saken, og hva som mangler."
}`;
}

function buildPrompt(d) {
  return `Vurder denne saken foreløpig.

Kategori: ${d.kategori || "Ikke oppgitt"}
Beskrivelse: ${d.beskrivelse || "Ikke oppgitt"}
Tidspunkt: ${d.tidspunkt || "Ikke oppgitt"}
Motpart: ${d.motpart || "Ikke oppgitt"}
Mål: ${d.maal || "Ikke oppgitt"}
Dokumentasjon: ${d.dokumentasjon.length ? d.dokumentasjon.join(", ") : "Ikke oppgitt"}

Skriv for en vanlig person i Norge. Vær konkret. Ikke nevn paragrafnummer med mindre det er nødvendig.`;
}

function extractJson(text) {
  const trimmed = text.trim();
  try { return JSON.parse(trimmed); } catch {}
  const match = trimmed.match(/\{[\s\S]*\}/);
  if (!match) throw new Error("No JSON found");
  return JSON.parse(match[0]);
}

function fallbackFromText(text, d) {
  return {
    badge: "Bør vurderes manuelt",
    shortAssessment: text.slice(0, 700) || `Basert på det du har skrevet ser saken ut til å gjelde ${d.kategori || "et juridisk spørsmål"}. Saken bør vurderes nærmere hvis du har dokumentasjon på det som har skjedd.`,
    strengths: ["Saken er beskrevet nok til en første sortering."],
    weaknesses: ["AI-svaret kom ikke i riktig struktur.", "Dokumentene er ikke gjennomgått."],
    nextSteps: ["Samle relevant dokumentasjon.", "Lag en kort tidslinje.", "Send saken videre for manuell vurdering hvis du ønsker konkret gjennomgang."],
    lawyerReviewRecommended: true,
    urgency: "medium",
    missingInformation: [],
    handoffSummary: text.slice(0, 1000)
  };
}
