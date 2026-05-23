# Rettsregel advokatvurdering — Claude Worker

Denne workeren kobler `/advokatvurdering/` til Claude.

## 1. Opprett Worker i Cloudflare

Cloudflare Dashboard → Workers & Pages → Create Worker.

Lim inn innholdet fra `advokatvurdering-worker.js`.

## 2. Legg inn hemmelig nøkkel

I Worker → Settings → Variables → Secrets:

- `ANTHROPIC_API_KEY` = nøkkelen fra Claude/Anthropic Console

Valgfrie variabler:

- `ALLOWED_ORIGIN` = `https://rettsregel.no`
- `CLAUDE_MODEL` = `claude-sonnet-4-5-20250929`

## 3. Deploy

Etter deploy får dere en URL, typisk:

`https://rettsregel-case-assessment.<konto>.workers.dev`

## 4. Koble frontend

Åpne:

`advokatvurdering/index.html`

Finn:

```js
const ASSESSMENT_WORKER_URL = "";
```

Sett inn worker-URL-en:

```js
const ASSESSMENT_WORKER_URL = "https://rettsregel-case-assessment.<konto>.workers.dev";
```

Da bruker siden Claude. Hvis URL-en er tom eller workeren feiler, faller siden tilbake til enkel lokal vurdering.
