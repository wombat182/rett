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
  return `Du er Rettsregel sin AI for foreløpig saksvurdering på norsk.

Du er ikke advokat. Du skal ikke late som vurderingen er en endelig advokatvurdering.
Du skal være praktisk, rolig og juridisk forsiktig.
Du skal ikke love resultat, ikke si at brukeren vinner, og ikke gi bastante konklusjoner uten vilkår.
Du skal vurdere norsk rett på et overordnet nivå basert på brukerens opplysninger.
Du skal identifisere dokumentasjon, frister, svakheter og neste steg.

Returner KUN gyldig JSON. Ingen markdown. Ingen tekst før eller etter JSON.

JSON-format:
{
  "badge": "Bør vurderes manuelt" | "Kan haste" | "Trenger mer informasjon" | "Lite grunnlag foreløpig",
  "shortAssessment": "2-5 setninger. Start gjerne med: Basert på det du har skrevet ...",
  "strengths": ["2-4 konkrete punkter"],
  "weaknesses": ["2-4 konkrete punkter"],
  "nextSteps": ["3-5 konkrete steg"],
  "lawyerReviewRecommended": true,
  "urgency": "low" | "medium" | "high",
  "missingInformation": ["0-5 konkrete ting som mangler"],
  "handoffSummary": "Kort advokatvennlig sammendrag av saken."
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
