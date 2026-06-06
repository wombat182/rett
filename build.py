#!/usr/bin/env python3
"""
Rettsregel page builder.
Takes structured paragraph content and produces static HTML pages
matching the homepage design.
"""

import os
import re
import json
import shutil

# ============================================================
# DATA — content for each paragraph
# ============================================================

from paragraphs_data import PARAGRAPHS as _P_BASE
try:
    from paragraphs_kjopsloven import PARAGRAPHS as _P_KJOPSLOVEN
except ImportError:
    _P_KJOPSLOVEN = []
try:
    from paragraphs_husleieloven import PARAGRAPHS as _P_HUSLEIELOVEN
except ImportError:
    _P_HUSLEIELOVEN = []
try:
    from paragraphs_avhendingslova import PARAGRAPHS as _P_AVHENDINGSLOVA
except ImportError:
    _P_AVHENDINGSLOVA = []
try:
    from paragraphs_naboloven import PARAGRAPHS as _P_NABOLOVEN
except ImportError:
    _P_NABOLOVEN = []
try:
    from paragraphs_navneloven import PARAGRAPHS as _P_NAVNELOVEN
except ImportError:
    _P_NAVNELOVEN = []
try:
    from paragraphs_forbrukerkjopsloven import PARAGRAPHS as _P_FKL
except ImportError:
    _P_FKL = []
try:
    from paragraphs_arveloven import PARAGRAPHS as _P_ARVELOVEN
except ImportError:
    _P_ARVELOVEN = []

try:
    from paragraphs_bustadoppforingslova import PARAGRAPHS as _P_BUSTAD
except ImportError:
    _P_BUSTAD = []

try:
    from paragraphs_tomtefesteloven import PARAGRAPHS as _P_TOMTEFESTELOVEN
except ImportError:
    _P_TOMTEFESTELOVEN = []

try:
    from paragraphs_ekteskapsloven import PARAGRAPHS as _P_EKTESKAP
except ImportError:
    _P_EKTESKAP = []

try:
    from paragraphs_voldserstatningsloven import PARAGRAPHS as _P_VOLDSERSTATNING
except ImportError:
    _P_VOLDSERSTATNING = []

try:
    from paragraphs_arbeidsmiljoloven import PARAGRAPHS as _P_ARBEIDSMILJO
except ImportError:
    _P_ARBEIDSMILJO = []

try:
    from paragraphs_inkassoloven import PARAGRAPHS as _P_INKASSO
except ImportError:
    _P_INKASSO = []

try:
    from paragraphs_pasientskadeloven import PARAGRAPHS as _P_PASIENTSKADE
except ImportError:
    _P_PASIENTSKADE = []

try:
    from paragraphs_yrkesskadeforsikringsloven import PARAGRAPHS as _P_YRKESSKADE
except ImportError:
    _P_YRKESSKADE = []

try:
    from paragraphs_oreigningslova import PARAGRAPHS as _P_OREIGNING
except ImportError:
    _P_OREIGNING = []

try:
    from paragraphs_foreldelsesloven import PARAGRAPHS as _P_FORELDELSE
except ImportError:
    _P_FORELDELSE = []

try:
    from paragraphs_universitetsloven import PARAGRAPHS as _P_UHL
except ImportError:
    _P_UHL = []

try:
    from paragraphs_barnelova import PARAGRAPHS as _P_BARNELOVA
except ImportError:
    _P_BARNELOVA = []

try:
    from paragraphs_ferieloven import PARAGRAPHS as _P_FERIE
except ImportError:
    _P_FERIE = []

try:
    from paragraphs_forvaltningsloven import PARAGRAPHS as _P_FORVALTNING
except ImportError:
    _P_FORVALTNING = []

try:
    from paragraphs_eierseksjonsloven import PARAGRAPHS as _P_EIERSEKSJON
except ImportError:
    _P_EIERSEKSJON = []

try:
    from paragraphs_burettslagslova import PARAGRAPHS as _P_BURETTSLAG
except ImportError:
    _P_BURETTSLAG = []

PARAGRAPHS = _P_BASE + _P_KJOPSLOVEN + _P_HUSLEIELOVEN + _P_AVHENDINGSLOVA + _P_NABOLOVEN + _P_NAVNELOVEN + _P_FKL + _P_ARVELOVEN + _P_BUSTAD + _P_TOMTEFESTELOVEN + _P_EKTESKAP + _P_VOLDSERSTATNING + _P_ARBEIDSMILJO + _P_INKASSO + _P_PASIENTSKADE + _P_YRKESSKADE + _P_OREIGNING + _P_FORELDELSE + _P_UHL + _P_BARNELOVA + _P_FERIE + _P_FORVALTNING + _P_EIERSEKSJON + _P_BURETTSLAG

# Spørsmål-artikler (lever på /sporsmal/[slug]/)
try:
    from sporsmal_data import SPORSMAL as _SP_BASE
except ImportError:
    _SP_BASE = []

try:
    from sporsmal_kjopsloven import SPORSMAL as _SP_KJOPSLOVEN
except ImportError:
    _SP_KJOPSLOVEN = []

try:
    from sporsmal_ekteskapsloven import SPORSMAL as _SP_EKTESKAPSLOVEN
except ImportError:
    _SP_EKTESKAPSLOVEN = []

SPORSMAL = _SP_BASE + _SP_KJOPSLOVEN + _SP_EKTESKAPSLOVEN

# ============================================================
# SHARED CSS (same look as homepage)
# ============================================================

CSS = """
:root {
  --bg: #F4F1EA;
  --bg-alt: #EDE8DF;
  --bg-card: #FDFAF5;
  --ink: #1C1710;
  --ink-soft: #5C5146;
  --ink-mute: #6B5F52;
  --accent: #C04A26;
  --accent-deep: #A03B1A;
  --accent-soft: #E8C4B4;
  --line: rgba(28, 23, 16, 0.09);
  --line-strong: rgba(28, 23, 16, 0.18);
  --shadow-sm: 0 1px 3px rgba(28, 23, 16, 0.05);
  --shadow-md: 0 2px 12px rgba(28, 23, 16, 0.07);
  --shadow-lg: 0 12px 32px rgba(28, 23, 16, 0.09);
  --footer-bg: #EAE4DC;
  --kat-bolig: #4F6F5E;
  --kat-forbruk: #C04A26;
  --kat-arbeid: #6B5B95;
  --kat-familie: #B8654A;
  --kat-gjeld: #7A6E5D;
  --kat-tjenester: #4E6E80;
  --serif: Optima, 'Optima Nova', 'URW Classico', Candara, 'Lucida Sans', 'Lucida Sans Unicode', 'Trebuchet MS', sans-serif;
  --serif-prose: 'Palatino', 'Palatino Linotype', 'Book Antiqua', Georgia, serif;
  --sans: 'Manrope', system-ui, sans-serif;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  background: var(--bg); color: var(--ink); font-family: var(--sans);
  font-size: 16px; line-height: 1.6; -webkit-font-smoothing: antialiased;
  position: relative;
}
body::before {
  content: ''; position: fixed; inset: 0; pointer-events: none; z-index: 100; opacity: 0.22;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.12 0 0 0 0 0.1 0 0 0 0 0.08 0 0 0 0.18 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
.container { max-width: 1100px; margin: 0 auto; padding: 0 32px; }
main.page { max-width: 1100px; margin: 0 auto; padding: 0 32px; min-height: calc(100vh - 200px); }
@media (max-width: 720px) {
  .container { padding: 0 20px; }
  main.page { padding: 0 20px; }
}
.narrow { max-width: 740px; margin: 0 auto; padding: 0 32px; }

/* ---------- Site header (R-logo + minimal Optima nav) ---------- */
.site-header {
  max-width: 1180px; margin: 0 auto;
  padding: 32px 32px 0;
  display: flex; justify-content: space-between; align-items: center;
  position: relative;
}
.site-logo {
  display: inline-flex; align-items: center;
  text-decoration: none; color: var(--ink);
  transition: opacity 0.2s ease;
}
.site-logo:hover { opacity: 0.7; }
.site-logo svg { width: 32px; height: 42px; display: block; color: var(--ink); }

.site-nav-links {
  display: flex; gap: 30px; align-items: center;
  list-style: none; margin: 0; padding: 0;
}
.site-nav-links a {
  font-family: var(--serif);
  font-size: 14px; font-weight: 500;
  color: var(--ink-mute); text-decoration: none;
  letter-spacing: 0.01em;
  transition: color 0.18s ease;
}
.site-nav-links a:hover { color: var(--ink); }
.site-nav-links a.site-nav-cta {
  color: var(--accent);
  display: inline-flex; align-items: center; gap: 5px;
}
.site-nav-links a.site-nav-cta:hover { color: var(--accent-deep); }

.site-nav-toggle { display: none; }
.site-nav-toggle-label {
  display: none; cursor: pointer;
  padding: 8px; margin: -8px;
}
.site-nav-toggle-label svg { width: 22px; height: 22px; color: var(--ink); display: block; }

@media (max-width: 720px) {
  .site-header { padding: 24px 20px 0; }
  .site-logo svg { width: 28px; height: 36px; }
  .site-nav-toggle-label { display: inline-flex; align-items: center; justify-content: center; }
  .site-nav-links {
    display: none; position: absolute;
    top: calc(100% + 8px); right: 20px;
    background: var(--bg-card); flex-direction: column;
    align-items: flex-start; gap: 14px;
    padding: 22px 28px; border-radius: 12px;
    box-shadow: 0 10px 36px rgba(28, 23, 16, 0.10);
    z-index: 50; border: 1px solid var(--line);
  }
  .site-nav-toggle:checked ~ .site-nav-links { display: flex; }
  .site-nav-links a { font-size: 15px; }
}

/* Breadcrumbs */
.breadcrumbs {
  font-size: 14px; color: var(--ink-mute); margin: 24px 0 32px;
  display: flex; align-items: center; gap: 10px; flex-wrap: wrap;
}
.breadcrumbs a { color: var(--ink-soft); text-decoration: none; transition: color 0.2s; }
.breadcrumbs a:hover { color: var(--accent); }
.breadcrumbs .sep { opacity: 0.4; }
.breadcrumbs .current { color: var(--ink); }

/* Article header */
.article-header { padding: 24px 0 56px; max-width: 880px; }
.article-eyebrow {
  font-size: 13px; font-weight: 600; color: var(--accent);
  text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 24px;
}
.article-title {
  font-family: var(--serif); font-weight: 400;
  font-size: clamp(26px, 3.2vw, 40px);
  line-height: 1.08; letter-spacing: -0.022em; margin-bottom: 28px;
}
.article-title .paragraf-num { color: var(--accent); font-style: italic; }
.article-description {
  font-size: 19px; color: var(--ink-soft); line-height: 1.55; max-width: 700px;
}

/* Kort svar — featured callout */
.kort-svar {
  background: var(--bg-card); border: 1px solid var(--line);
  border-left: 4px solid var(--accent);
  padding: 32px 36px; border-radius: 0 16px 16px 0;
  margin: 20px 0 56px;
  box-shadow: var(--shadow-sm);
}
.kort-svar .kort-svar-label {
  font-size: 11px; font-weight: 700; color: var(--accent);
  text-transform: uppercase; letter-spacing: 0.18em; margin-bottom: 14px;
}
.kort-svar p {
  font-family: var(--serif); font-size: 20px; line-height: 1.6;
  color: var(--ink); margin: 0; letter-spacing: -0.005em;
}

/* Article body */
.article-body {
  font-family: var(--serif-prose);
  font-size: 18px; line-height: 1.7;
  color: var(--ink-soft);
}
.article-body h2 {
  font-family: var(--serif); font-weight: 400;
  font-size: clamp(24px, 2.8vw, 32px);
  line-height: 1.15; letter-spacing: -0.015em;
  margin: 64px 0 20px;
  color: var(--ink);
}
.article-body h2 + p, .article-body h2 + ul, .article-body h2 + ol { margin-top: 0; }
.article-body h3 {
  font-family: var(--serif); font-weight: 500; font-size: 22px;
  line-height: 1.3; margin: 32px 0 12px; letter-spacing: -0.005em;
}
.article-body p { margin-bottom: 18px; color: var(--ink); }
.article-body ul, .article-body ol { margin: 18px 0 18px 24px; }
.article-body li { margin-bottom: 10px; }
.article-body strong { font-weight: 600; }
.article-body em { font-style: italic; }
.article-body a { color: var(--accent); text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 3px; }
.article-body a:hover { color: var(--ink); }

/* Lovtekst blockquote */
.lovtekst {
  background: white; border: 1px solid var(--line); border-radius: 12px;
  padding: 28px 32px; margin: 24px 0;
  font-family: var(--serif); font-size: 17px; line-height: 1.6; color: var(--ink-soft);
  font-style: italic; white-space: pre-wrap;
}
.lovtekst-attr {
  margin-top: 16px; font-family: var(--sans); font-style: normal; font-size: 13px;
  color: var(--ink-mute); display: flex; align-items: center; gap: 8px;
}
.lovtekst-attr::before {
  content: ''; width: 24px; height: 1px; background: var(--ink-mute); display: inline-block;
}

/* Example */
.example {
  background: var(--bg-alt); border-radius: 12px;
  padding: 24px 28px; margin: 24px 0;
}
.example-name {
  font-family: var(--serif); font-weight: 600; font-size: 16px;
  color: var(--accent); margin-bottom: 8px;
  letter-spacing: 0.02em;
}
.example-name::before { content: 'Eksempel · '; color: var(--ink-mute); font-weight: 500; }
.example p { margin: 0; color: var(--ink); }

/* FAQ — Dumme spørsmål */
.faq { margin: 16px 0; }
.faq-item {
  border-top: 1px solid var(--line); padding: 24px 0;
}
.faq-item:last-child { border-bottom: 1px solid var(--line); }
.faq-q {
  font-family: var(--serif); font-weight: 500; font-size: 19px;
  line-height: 1.35; color: var(--ink); margin-bottom: 10px;
  letter-spacing: -0.005em;
}
.faq-a { color: var(--ink-soft); line-height: 1.6; }

/* Related */
.related-section {
  margin-top: 72px; padding-top: 48px; border-top: 1px solid var(--line);
}
.related-label {
  font-size: 12px; font-weight: 700; color: var(--accent);
  text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 24px;
}
.related-cards { display: grid; gap: 12px; }
.related-card {
  background: white; border: 1px solid var(--line); border-radius: 12px;
  padding: 20px 24px; text-decoration: none; color: inherit; display: block;
  transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
}
.related-card:hover {
  transform: translateY(-2px); border-color: var(--accent-soft);
  box-shadow: 0 8px 24px rgba(31,26,20,0.06);
}
.related-card-meta {
  font-size: 12px; font-weight: 600; color: var(--accent);
  text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 6px;
}
.related-card-title {
  font-family: var(--serif); font-weight: 500; font-size: 18px;
  line-height: 1.3; color: var(--ink);
}
.related-card.unavailable { opacity: 0.6; pointer-events: none; }
.related-card.unavailable .related-card-meta::after {
  content: ' · KOMMER SNART';
  color: var(--ink-mute);
}

/* Form CTA section */
.cta-section {
  background: var(--bg); padding: 80px 0 60px;
  margin-top: 80px;
  border-top: 1px solid var(--line);
}
.cta-grid {
  display: grid; grid-template-columns: 1fr 1.2fr; gap: 72px; align-items: start;
}
@media (max-width: 900px) { .cta-grid { grid-template-columns: 1fr; gap: 40px; } }
.cta-intro h2 {
  font-family: var(--serif); font-weight: 400;
  font-size: clamp(24px, 3vw, 36px); line-height: 1.1;
  letter-spacing: -0.015em; margin-bottom: 20px;
}
.cta-intro h2 em { font-style: italic; color: var(--accent); }
.cta-intro p { font-size: 17px; color: var(--ink-soft); line-height: 1.55; max-width: 420px; }

form.contact-form {
  background: var(--bg); padding: 40px; border-radius: 20px; border: 1px solid var(--line);
}
@media (max-width: 600px) { form.contact-form { padding: 28px 22px; } }
.form-field { margin-bottom: 20px; }
.form-field label {
  display: block; font-size: 14px; font-weight: 600; margin-bottom: 8px; color: var(--ink);
}
.form-field input, .form-field textarea {
  width: 100%; padding: 14px 16px; border: 1.5px solid var(--line); border-radius: 10px;
  font-family: var(--sans); font-size: 16px; background: var(--bg-alt); color: var(--ink);
  transition: border-color 0.2s, box-shadow 0.2s;
}
.form-field input:focus, .form-field textarea:focus {
  outline: none; border-color: var(--accent);
  box-shadow: 0 0 0 4px rgba(194,84,52,0.12);
}
.form-field textarea {
  min-height: 120px; resize: vertical; font-family: var(--sans); line-height: 1.5;
}
.form-field input::placeholder, .form-field textarea::placeholder { color: var(--ink-mute); }
.form-submit {
  width: 100%; background: var(--ink); color: var(--bg); padding: 16px; border: none;
  border-radius: 10px; font-size: 16px; font-weight: 600; cursor: pointer;
  font-family: var(--sans); transition: background 0.2s, transform 0.2s;
  display: flex; align-items: center; justify-content: center; gap: 10px;
}
.form-submit:hover { background: var(--accent); transform: translateY(-1px); }
.form-note { margin-top: 14px; font-size: 13px; color: var(--ink-mute); text-align: center; line-height: 1.5; }
.form-note a { color: var(--accent); text-decoration: none; font-weight: 600; border-bottom: 1px solid transparent; transition: border-color 0.15s; }
.form-note a:hover { border-bottom-color: var(--accent); }
.form-success { display: none; background: var(--bg); padding: 40px; border-radius: 20px; border: 1px solid var(--accent-soft); text-align: center; }
.form-success.show { display: block; }
form.contact-form.hide { display: none; }
.form-success h3 { font-family: var(--serif); font-size: 24px; margin-bottom: 10px; }
.form-success p { color: var(--ink-soft); }

/* Footer — warm light redesign */
/* ---------- Minimal site footer ---------- */
.site-footer {
  max-width: 1180px; margin: 64px auto 0;
  padding: 24px 32px 32px;
  border-top: 1px solid var(--line);
  display: flex; justify-content: space-between; align-items: center;
  font-family: var(--serif); font-size: 13px;
  color: var(--ink-mute);
  background: transparent;
}
.site-footer-copy { letter-spacing: 0.005em; }
.site-footer-links { display: inline-flex; gap: 24px; }
.site-footer-links a,
.site-footer a {
  color: var(--ink-mute); text-decoration: none;
  transition: color 0.18s ease;
  font-size: 13px;
}
.site-footer-links a:hover,
.site-footer a:hover { color: var(--ink); }

@media (max-width: 540px) {
  .site-footer {
    padding: 20px 20px 24px;
    font-size: 12.5px;
    flex-wrap: wrap; gap: 10px;
  }
  .site-footer-links { gap: 18px; }
}
/* Hub — tjeneste og kontrakt-kort */
.tjenester-hero { padding: 48px 0 40px; }
.tjenester-hero h1 { font-family: var(--serif); font-weight: 400; font-size: clamp(24px, 3vw, 34px); line-height: 1.12; letter-spacing: -0.015em; margin-bottom: 16px; }
.tjenester-hero p { font-size: 17px; color: var(--ink-soft); max-width: 580px; line-height: 1.55; }
.tjenester-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 18px; margin: 36px 0 64px; }
.tjeneste-kort {
  background: var(--bg-card); border: 1px solid var(--line); border-radius: 20px;
  padding: 28px 32px; text-decoration: none; color: var(--ink);
  transition: box-shadow 0.2s, transform 0.15s, border-color 0.2s;
  display: flex; flex-direction: column; gap: 8px; position: relative; min-height: 190px;
}
.tjeneste-kort:not(.snart):hover { box-shadow: var(--shadow-md); transform: translateY(-2px); border-color: rgba(177,74,42,0.25); }
.tjeneste-kort.snart { pointer-events: none; }
.tjeneste-kat {
  font-size: 11px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.14em; color: var(--accent); margin-bottom: 4px;
}
.tjeneste-kat.graa { color: var(--ink-mute); }
.tjeneste-kort h3 { font-family: var(--serif); font-weight: 400; font-size: 21px; line-height: 1.2; margin: 0; }
.tjeneste-kort.snart h3 { color: var(--ink-soft); }
.tjeneste-kort p { font-size: 14px; color: var(--ink-soft); line-height: 1.55; flex: 1; margin: 0; }
.tjeneste-pil { font-size: 13px; color: var(--accent); font-weight: 600; margin-top: 10px; }
.tjeneste-kort.snart .tjeneste-pil { color: var(--ink-mute); }
.snart-badge {
  position: absolute; top: 16px; right: 16px;
  font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em;
  background: var(--bg-alt); color: var(--ink-mute); padding: 3px 9px; border-radius: 20px;
}

/* Mobile wizard fixes — applied globally */
@media (max-width: 640px) {
  .vg, .vg3 { grid-template-columns: 1fr !important; }
  .enk-kort, .steg-kort, .kalkulator { padding: 20px 16px !important; }
  .kalkulator-valg label { padding: 11px 14px; }
  .w-input, .wizard-input { font-size: 16px; } /* prevent iOS zoom */
}
@media (max-width: 760px) {
  .vg3 { grid-template-columns: 1fr 1fr !important; }
}
/* Grid overflow fix — all two-column layouts */
.kontrakt-layout > *, .rek-layout > * { min-width: 0; }
@media (max-width: 1024px) {
  .kontrakt-layout, .rek-layout { grid-template-columns: 1fr !important; }
  .kontrakt-skjema, .rek-skjema { position: static !important; }
}

/* ── Lovside-redesign ── */
.lov-side-hero { padding: 56px 0 44px; }
.lov-hero-mark { font-family: var(--serif); font-size: 36px; color: var(--accent); margin-bottom: 10px; display: block; line-height: 1; }
.lov-hero-h1 { font-family: var(--serif); font-weight: 400; font-size: clamp(28px, 3.8vw, 44px); line-height: 1.08; letter-spacing: -0.025em; margin-bottom: 18px; }
.lov-hero-h1 em { font-style: italic; color: var(--accent); }
.lov-hero-desc { font-size: 18px; color: var(--ink-soft); line-height: 1.65; max-width: 640px; margin-bottom: 24px; }
.lov-hero-pills { display: flex; gap: 8px; flex-wrap: wrap; }
.lov-hero-pill { display: inline-flex; align-items: center; gap: 5px; padding: 6px 14px; background: var(--bg-card); border: 1px solid var(--line); border-radius: 100px; font-size: 12px; font-weight: 600; color: var(--ink-soft); white-space: nowrap; }
/* Featured */
.lov-feat-sek { margin-bottom: 44px; }
.lov-sek-lbl { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .18em; color: var(--ink-mute); margin-bottom: 14px; display: block; }
.lov-feat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
@media(max-width:700px) { .lov-feat-grid { grid-template-columns: 1fr; } }
.lov-feat-kort { background: var(--bg-card); border: 1.5px solid var(--line); border-radius: 18px; padding: 28px; text-decoration: none; color: var(--ink); display: flex; flex-direction: column; transition: box-shadow .15s, border-color .15s, transform .13s; }
.lov-feat-kort:hover { border-color: var(--accent); box-shadow: 0 8px 32px rgba(28,23,16,.1); transform: translateY(-2px); }
.lov-feat-num { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .16em; color: var(--accent); margin-bottom: 10px; }
.lov-feat-tittel { font-family: var(--serif); font-size: 21px; font-weight: 400; line-height: 1.25; margin-bottom: 10px; }
.lov-feat-txt { font-size: 13px; color: var(--ink-soft); line-height: 1.65; flex: 1; margin-bottom: 16px; }
.lov-feat-cta { font-size: 13px; font-weight: 700; color: var(--accent); }
/* Search */
.lov-sok-wrap { position: relative; margin-bottom: 12px; }
.lov-sok-icon { position: absolute; left: 14px; top: 50%; transform: translateY(-50%); color: var(--ink-mute); pointer-events: none; width: 16px; height: 16px; }
.lov-sok-input { width: 100%; padding: 13px 14px 13px 42px; border: 1.5px solid var(--line); border-radius: 12px; font-family: var(--sans); font-size: 15px; background: var(--bg-card); color: var(--ink); box-sizing: border-box; transition: border-color .15s; }
.lov-sok-input:focus { outline: none; border-color: var(--accent); }
.lov-sok-count { font-size: 12px; color: var(--ink-mute); margin-bottom: 16px; min-height: 18px; }
/* Paragraph grid */
.plist-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 80px; }
@media(max-width:700px) { .plist-grid { grid-template-columns: 1fr; } }
.plist-kort { background: var(--bg-card); border: 1px solid var(--line); border-radius: 14px; padding: 18px 20px; text-decoration: none; color: var(--ink); display: flex; align-items: flex-start; gap: 14px; transition: border-color .13s, box-shadow .13s; }
.plist-kort:hover { border-color: var(--accent); box-shadow: 0 3px 16px rgba(28,23,16,.07); }
.plist-kort.plist-flagg { border-color: rgba(177,74,42,.25); }
.plist-kort-num { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .1em; color: var(--accent); min-width: 40px; padding-top: 3px; white-space: nowrap; flex-shrink: 0; }
.plist-kort-body { flex: 1; min-width: 0; }
.plist-kort-tittel { font-family: var(--serif); font-size: 17px; font-weight: 400; line-height: 1.28; margin-bottom: 5px; }
.plist-kort-excerpt { font-size: 12px; color: var(--ink-soft); line-height: 1.6; }
.plist-kort-pil { font-size: 14px; color: var(--accent); opacity: 0; transition: opacity .13s; align-self: center; flex-shrink: 0; }
.plist-kort:hover .plist-kort-pil { opacity: 1; }
.plist-hidden { display: none !important; }
.plist-ingen { display: none; font-size: 14px; color: var(--ink-mute); padding: 32px 0; text-align: center; grid-column: 1/-1; }
.plist-ingen.vis { display: block; }
.rule-table {
  width: 100%; border-collapse: collapse; margin: 1.5rem 0;
  font-size: 15px; background: var(--paper-warm);
  border: 1px solid var(--accent-soft);
}
.rule-table th, .rule-table td {
  padding: 12px 16px; text-align: left;
  border-bottom: 1px solid var(--accent-soft);
  vertical-align: top;
}
.rule-table th {
  font-family: var(--sans); font-weight: 600; font-size: 13px;
  color: var(--accent); text-transform: uppercase; letter-spacing: 0.05em;
  background: rgba(194, 84, 52, 0.05);
}
.rule-table tr:last-child td { border-bottom: none; }
.rule-table tr:hover td { background: rgba(194, 84, 52, 0.03); }

/* ============================================================
   Disclaimer (innhold-attest) — bunntekst på paragrafsider
   ============================================================ */
.innhold-attest {
  max-width: 760px; margin: 48px auto 0;
  padding: 18px 22px;
  background: var(--bg-card);
  border: 1px solid var(--line);
  border-left: 3px solid var(--accent);
  border-radius: 10px;
  font-family: var(--sans);
  font-size: 13px; line-height: 1.65;
  color: var(--ink-soft);
  display: flex; gap: 12px; align-items: flex-start;
}
.innhold-attest::before {
  content: "§"; flex-shrink: 0;
  font-family: var(--serif); font-size: 22px;
  line-height: 1; color: var(--accent);
  position: relative; top: -1px;
}
.innhold-attest a {
  color: var(--accent); text-decoration: none;
  font-weight: 600; border-bottom: 1px solid transparent;
  transition: border-color 0.15s;
}
.innhold-attest a:hover { border-bottom-color: var(--accent); }
.innhold-attest .innhold-attest-body strong { color: var(--ink); font-weight: 600; }

/* ============================================================
   TJENESTER — hub og kalkulator
   ============================================================ */
/* Kalkulator */
.kalkulator-intro { margin-bottom: 40px; }
.kalkulator {
  background: var(--bg-card); border: 1px solid var(--line);
  border-radius: 20px; padding: 40px; box-shadow: var(--shadow-md);
  margin-bottom: 32px;
}
@media (max-width: 600px) { .kalkulator { padding: 24px 20px; } }
.kalkulator-tittel { font-family: var(--serif); font-size: 20px; font-weight: 500; margin-bottom: 28px; color: var(--ink); }
.kalkulator-sporsmal { margin-bottom: 28px; }
.kalkulator-sporsmal legend {
  font-size: 15px; font-weight: 600; color: var(--ink); margin-bottom: 12px;
  display: block; line-height: 1.4;
}
.kalkulator-sporsmal .hint { font-size: 13px; color: var(--ink-mute); font-weight: 400; display: block; margin-top: 3px; }
.kalkulator-valg { display: flex; flex-direction: column; gap: 8px; }
.kalkulator-valg label {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 16px; border: 1.5px solid var(--line);
  border-radius: 10px; cursor: pointer; font-size: 15px;
  transition: border-color 0.15s, background 0.15s; line-height: 1.35;
  background: var(--bg);
}
.kalkulator-valg label:hover { border-color: var(--accent-soft); }
.kalkulator-valg input[type=radio] { accent-color: var(--accent); width: 18px; height: 18px; flex-shrink: 0; }
.kalkulator-valg input[type=radio]:checked + span { color: var(--accent); font-weight: 600; }
.kalkulator-valg label:has(input:checked) { border-color: var(--accent); background: rgba(177,74,42,0.04); }
.kalkulator-divider { border: none; border-top: 1px solid var(--line); margin: 4px 0 28px; }
.kalkulator-knapp {
  background: var(--accent); color: white; border: none; border-radius: 12px;
  font-family: var(--sans); font-size: 16px; font-weight: 600; cursor: pointer;
  padding: 16px 32px; width: 100%; transition: background 0.2s;
  letter-spacing: 0.01em;
}
.kalkulator-knapp:hover { background: var(--accent-deep); }

/* Resultat */
.kalkulator-resultat {
  background: var(--bg-card); border: 2px solid var(--accent);
  border-radius: 20px; padding: 40px; margin-bottom: 32px;
  animation: fadeInUp 0.3s ease;
}
@media (max-width: 600px) { .kalkulator-resultat { padding: 24px 20px; } }
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}
.resultat-badge {
  display: inline-block; font-size: 11px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.12em; padding: 5px 12px; border-radius: 20px; margin-bottom: 16px;
}
.resultat-badge.as { background: #e8f0f4; color: #2d5970; }
.resultat-badge.enk { background: #f0f4e8; color: #3d5a2d; }
.resultat-badge.begge { background: #f4f0e8; color: #5a4a2d; }
.resultat-tittel { font-family: var(--serif); font-size: clamp(22px, 3vw, 30px); font-weight: 400; margin-bottom: 20px; line-height: 1.15; }
.resultat-grunner { margin: 0 0 28px; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 10px; }
.resultat-grunner li { display: flex; gap: 10px; font-size: 15px; line-height: 1.45; }
.resultat-grunner li::before { content: '→'; color: var(--accent); font-weight: 700; flex-shrink: 0; }
.resultat-tabell-wrapper { overflow-x: auto; margin: 28px 0; }
.resultat-tabell {
  width: 100%; border-collapse: collapse; font-size: 14px;
  border: 1px solid var(--line);
}
.resultat-tabell th {
  padding: 10px 14px; text-align: left; font-size: 13px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.06em; background: var(--bg-alt);
  border-bottom: 2px solid var(--line);
}
.resultat-tabell td { padding: 11px 14px; border-bottom: 1px solid var(--line); vertical-align: top; }
.resultat-tabell tr:last-child td { border-bottom: none; }
.resultat-tabell td:first-child { color: var(--ink-mute); font-size: 13px; font-weight: 600; white-space: nowrap; }
.col-anbefalt { background: rgba(177,74,42,0.03); }
.col-anbefalt th, .col-anbefalt td { color: var(--accent); font-weight: 600; }
.resultat-notat { font-size: 13px; color: var(--ink-mute); margin-top: 16px; line-height: 1.5; }

/* CTA-boks */
.tjeneste-cta-boks {
  background: var(--bg-alt); border-radius: 16px; padding: 36px;
  margin: 32px 0 56px; display: flex; flex-direction: column; gap: 16px;
}
.tjeneste-cta-boks h3 { font-family: var(--serif); font-size: 22px; font-weight: 400; }
.tjeneste-cta-boks p { font-size: 15px; color: var(--ink-soft); line-height: 1.5; max-width: 560px; }
.btn-aksjon {
  display: inline-flex; align-items: center; gap: 8px;
  background: var(--accent); color: white; text-decoration: none;
  font-weight: 600; font-size: 15px; padding: 14px 24px;
  border-radius: 10px; transition: background 0.2s; width: fit-content;
}
.btn-aksjon:hover { background: var(--accent-deep); }
.tjeneste-cta-pris { font-size: 13px; color: var(--ink-mute); }

/* ============================================================
   HOMEPAGE — strammere, vakrere, mer luft
   ============================================================ */

.homepage-hero {
  padding: 120px 0 80px;
  max-width: 880px;
}
.homepage-hero .eyebrow {
  font-family: var(--sans);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 36px;
}
.homepage-hero h1 {
  font-family: var(--serif);
  font-weight: 400;
  font-size: clamp(30px, 4vw, 46px);
  line-height: 1.06;
  letter-spacing: -0.022em;
  margin-bottom: 0;
}
.homepage-hero h1 + h1 { margin-bottom: 32px; }
.homepage-hero h1 em {
  font-style: italic;
  color: var(--accent);
}
.homepage-hero p {
  font-size: 21px;
  color: var(--ink-soft);
  line-height: 1.55;
  max-width: 620px;
  margin-bottom: 0;
}
.hero-cta {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  margin-top: 48px;
}
.cta-button {
  display: inline-block;
  background: var(--accent);
  color: white;
  padding: 18px 32px;
  border-radius: 999px;
  font-family: var(--sans);
  font-weight: 600;
  font-size: 16px;
  text-decoration: none;
  transition: transform 0.15s, background 0.2s, box-shadow 0.2s;
  border: 1px solid var(--accent);
  box-shadow: 0 1px 0 rgba(0,0,0,0.05);
}
.cta-button:hover {
  transform: translateY(-1px);
  background: #A8462C;
  box-shadow: 0 6px 20px rgba(194, 84, 52, 0.25);
}
.cta-button-secondary {
  display: inline-block;
  background: transparent;
  color: var(--ink);
  padding: 18px 32px;
  border-radius: 999px;
  font-family: var(--sans);
  font-weight: 600;
  font-size: 16px;
  text-decoration: none;
  transition: transform 0.15s, border-color 0.2s, background 0.2s;
  border: 1px solid var(--line);
}
.cta-button-secondary:hover {
  transform: translateY(-1px);
  border-color: var(--ink);
  background: rgba(0,0,0,0.02);
}

.home-section { margin-top: 112px; }
.section-header { margin-bottom: 32px; max-width: 720px; }
.section-header h2 {
  font-family: var(--serif);
  font-weight: 400;
  font-size: clamp(24px, 3vw, 36px);
  line-height: 1.1;
  letter-spacing: -0.015em;
  margin-bottom: 10px;
}
.section-sub {
  color: var(--ink-mute);
  font-size: 17px;
  font-family: var(--serif);
  font-style: italic;
}

/* ============================================================
   OM-SIDEN — minimalistisk, vakker
   ============================================================ */

.om-article {
  max-width: 680px;
  margin: 0 auto;
  padding: 80px 0 40px;
}
.om-header { margin-bottom: 72px; }
.om-header h1 {
  font-family: var(--serif);
  font-weight: 400;
  font-size: clamp(24px, 3vw, 36px);
  line-height: 1.08;
  letter-spacing: -0.022em;
}
.om-header h1 em {
  font-style: italic;
  color: var(--accent);
}
.om-section {
  margin-bottom: 56px;
}
.om-section h2 {
  font-family: var(--serif);
  font-weight: 500;
  font-style: italic;
  font-size: 28px;
  letter-spacing: -0.01em;
  color: var(--accent);
  margin-bottom: 20px;
}
.om-section p {
  font-family: var(--serif);
  font-weight: 400;
  font-size: 21px;
  line-height: 1.6;
  color: var(--ink);
  margin-bottom: 18px;
}
.om-lead {
  font-size: 26px !important;
  line-height: 1.45 !important;
  color: var(--ink) !important;
  font-style: italic;
  margin-bottom: 24px !important;
}
.om-cta {
  margin-top: 80px;
  padding-top: 48px;
  border-top: 1px solid var(--line);
  text-align: left;
}

/* ============================================================
   Spørsmål-sider — editorial newsroom design
   ============================================================ */

/* Hero */
.sp-hero {
  max-width: 760px; padding: 56px 0 24px;
}
.sp-hero .kicker {
  font-family: var(--sans); font-size: 11px;
  letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--ink-mute); font-weight: 600;
  margin-bottom: 16px; display: block;
}
.sp-hero .breadcrumb {
  display: none;
}
.sp-hero h1 {
  font-family: var(--serif); font-weight: 500;
  font-size: clamp(24px, 2.6vw, 32px); line-height: 1.2;
  letter-spacing: -0.01em; color: var(--ink);
  margin: 0; max-width: 720px;
}

/* Kort svar — fremhevet boks med drop quote feel */
.sp-tldr {
  background: var(--bg-card);
  border-left: 4px solid var(--accent);
  padding: 32px 36px;
  margin: 40px 0 56px;
  max-width: 760px;
  box-shadow: var(--shadow-sm);
  border-radius: 0 8px 8px 0;
  position: relative;
}
.sp-tldr::before {
  content: "KORT SVAR";
  position: absolute;
  top: -10px; left: 28px;
  background: var(--bg);
  padding: 0 10px;
  font-family: var(--sans); font-size: 11px;
  font-weight: 700; letter-spacing: 0.15em;
  color: var(--accent);
}
.sp-tldr p {
  font-family: var(--sans);
  font-size: 19px; line-height: 1.55;
  color: var(--ink); margin: 0;
}

/* Body — editorial typografi */
.sp-body {
  max-width: 720px;
  font-family: var(--sans);
}
.sp-body > h2 {
  font-family: var(--serif); font-weight: 500;
  font-size: clamp(22px, 2.6vw, 30px); line-height: 1.2;
  letter-spacing: -0.015em; color: var(--ink);
  margin: 64px 0 20px;
  padding-top: 12px;
  position: relative;
}
.sp-body > h2:first-child { margin-top: 0; padding-top: 0; }
.sp-body > h2::before {
  content: ""; position: absolute; top: 0; left: 0;
  width: 48px; height: 2px; background: var(--accent);
}
.sp-body > h2:first-child::before { display: none; }
.sp-body p {
  font-size: 17.5px; line-height: 1.7;
  margin-bottom: 18px; color: var(--ink);
}
.sp-body p:first-of-type::first-letter {
  /* Subtil dropcap for første avsnitt */
  font-family: var(--serif);
  font-size: 1em; font-weight: 500;
}
.sp-body a {
  color: var(--accent); text-decoration: none;
  border-bottom: 1px solid var(--accent-soft);
  transition: border-color 0.15s;
}
.sp-body a:hover { border-bottom-color: var(--accent); }
.sp-body strong { font-weight: 600; color: var(--ink); }

/* Ordnede lister som visuell timeline (steg) */
.sp-body ol {
  list-style: none; counter-reset: step;
  margin: 28px 0 36px; padding: 0;
}
.sp-body ol > li {
  counter-increment: step;
  position: relative;
  padding: 20px 0 20px 64px;
  border-bottom: 1px solid var(--line);
  font-size: 17px; line-height: 1.65;
}
.sp-body ol > li:last-child { border-bottom: none; }
.sp-body ol > li::before {
  content: counter(step);
  position: absolute; left: 0; top: 18px;
  width: 44px; height: 44px;
  background: var(--bg-card);
  border: 1.5px solid var(--accent);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--serif); font-size: 18px; font-weight: 500;
  color: var(--accent);
}
.sp-body ol > li strong {
  display: block; margin-bottom: 4px;
  color: var(--ink); font-weight: 600;
  font-size: 17px;
}

/* Uordnede lister — "vanlige feil"-stil */
.sp-body > h2:has(+ ul) + ul,
.sp-body ul {
  list-style: none; padding: 0;
  margin: 20px 0 36px;
}
.sp-body ul > li {
  position: relative; padding: 14px 0 14px 32px;
  border-bottom: 1px dashed var(--line);
  font-size: 16.5px; line-height: 1.6; color: var(--ink-soft);
}
.sp-body ul > li:last-child { border-bottom: none; }
.sp-body ul > li::before {
  content: ""; position: absolute; left: 4px; top: 24px;
  width: 14px; height: 1.5px; background: var(--accent);
}

/* Sitatblokker */
.sp-body blockquote {
  border-left: 3px solid var(--accent-soft);
  margin: 24px 0; padding: 4px 0 4px 24px;
  font-family: var(--serif); font-style: italic;
  font-size: 19px; color: var(--ink-soft); line-height: 1.5;
}

/* Tabeller */
.sp-body table, .rule-table {
  width: 100%; max-width: 720px;
  border-collapse: collapse; margin: 28px 0 36px;
  font-family: var(--sans); font-size: 15px;
}
.sp-body table th, .rule-table th {
  text-align: left; padding: 14px 16px;
  font-weight: 600; font-size: 13px;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--ink-soft); background: var(--bg-alt);
  border-bottom: 2px solid var(--line-strong);
}
.sp-body table td, .rule-table td {
  padding: 14px 16px; border-bottom: 1px solid var(--line);
  vertical-align: top; line-height: 1.5;
}

/* Relevante paragrafer — som "Les videre" på et magasin */
.sp-related {
  max-width: 880px;
  margin: 72px 0 0;
  padding: 40px 0 0;
  border-top: 1px solid var(--line-strong);
}
.sp-related .label {
  font-family: var(--sans); font-size: 12px;
  letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--accent); font-weight: 700;
  margin-bottom: 16px;
}
.sp-related h3 {
  font-family: var(--serif); font-size: 28px; font-weight: 500;
  margin-bottom: 28px; letter-spacing: -0.01em;
}
.sp-related ul { list-style: none; padding: 0; margin: 0; }
.sp-related li {
  padding: 18px 0;
  border-bottom: 1px solid var(--line);
  display: flex; gap: 24px; align-items: baseline;
}
.sp-related li:last-child { border-bottom: none; }
.sp-related .ref {
  font-family: var(--serif); font-size: 17px;
  font-weight: 500; flex-shrink: 0; min-width: 200px;
}
.sp-related .ref a {
  color: var(--ink); text-decoration: none;
  border-bottom: 1px solid var(--accent-soft);
  padding-bottom: 1px; transition: border-color 0.2s;
}
.sp-related .ref a:hover { border-bottom-color: var(--accent); }
.sp-related .desc { color: var(--ink-soft); font-size: 16px; line-height: 1.5; }
.sp-related .pending .ref {
  color: var(--ink-mute); font-style: italic;
}
.sp-related .pending .ref::after {
  content: " · kommer snart"; font-size: 12px;
  color: var(--accent-soft); font-style: italic;
  letter-spacing: 0.02em;
}

/* ============================================================
   Spørsmål-hub (/sporsmal/)
   ============================================================ */
.sphub-hero {
  max-width: 760px; padding: 72px 0 32px;
}
.sphub-hero .kicker {
  display: none;
}
.sphub-hero h1 {
  font-family: var(--serif); font-weight: 500;
  font-size: clamp(24px, 2.6vw, 32px); line-height: 1.2;
  letter-spacing: -0.01em; margin: 0 0 12px;
  color: var(--ink);
}
.sphub-hero h1 em {
  font-style: italic; color: var(--accent);
  font-weight: 400;
}
.sphub-hero .lead {
  font-family: var(--sans); font-size: 17px;
  line-height: 1.55; color: var(--ink-soft);
  max-width: 580px; margin: 0;
}
.sphub-meta {
  font-family: var(--sans); font-size: 12px;
  color: var(--ink-mute); letter-spacing: 0.04em;
  margin-top: 20px;
}
.sphub-meta strong { color: var(--accent); font-weight: 600; }

/* Kategori-seksjon */
.sphub-section {
  margin: 56px 0 0;
  padding-top: 28px;
  border-top: 1px solid var(--line);
}
.sphub-section:first-of-type { border-top: none; padding-top: 0; }
.sphub-section-head {
  display: flex; align-items: baseline; gap: 16px;
  margin-bottom: 24px; flex-wrap: wrap;
}
.sphub-section-kat {
  font-family: var(--sans); font-size: 10px;
  letter-spacing: 0.16em; text-transform: uppercase;
  font-weight: 700; padding: 4px 10px;
  border-radius: 999px; color: white;
}
.sphub-section h2 {
  font-family: var(--serif); font-size: clamp(20px, 2.2vw, 24px);
  font-weight: 500; letter-spacing: -0.015em; line-height: 1.15;
  margin: 0; color: var(--ink);
}
.sphub-section-count {
  font-family: var(--sans); font-size: 12px;
  color: var(--ink-mute); margin-left: auto;
}

/* Grid for spørsmål-kort */
.sphub-grid {
  display: grid; gap: 14px;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  max-width: 1100px;
}
.sphub-card {
  background: var(--bg-card);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 22px 24px 24px;
  text-decoration: none; color: inherit;
  display: flex; flex-direction: column;
  transition: border-color 0.2s, transform 0.2s;
  position: relative;
}
.sphub-card:hover {
  border-color: var(--kat-color, var(--accent));
}
.sphub-card .kat-tag {
  font-family: var(--sans); font-size: 10px;
  letter-spacing: 0.14em; text-transform: uppercase;
  font-weight: 700; color: var(--kat-color, var(--accent));
  margin-bottom: 10px;
}
.sphub-card h3 {
  font-family: var(--serif); font-size: 19px;
  font-weight: 500; line-height: 1.3; letter-spacing: -0.01em;
  margin-bottom: 8px; color: var(--ink);
}
.sphub-card p {
  font-family: var(--sans); font-size: 14px;
  line-height: 1.5; color: var(--ink-soft);
  margin: 0; flex-grow: 1;
}
.sphub-card .read-more {
  display: inline-flex; align-items: center; gap: 6px;
  margin-top: 16px; font-family: var(--sans);
  font-size: 12px; font-weight: 600;
  color: var(--kat-color, var(--accent));
  letter-spacing: 0.02em;
}
.sphub-card .read-more::after {
  content: "→"; transition: transform 0.2s;
}
.sphub-card:hover .read-more::after { transform: translateX(3px); }

/* Featured fjernet — alle kort like store for konsistens */

/* Kategori-farger som CSS-vars per kort */
.kat-bolig { --kat-color: var(--kat-bolig); }
.kat-forbruk { --kat-color: var(--kat-forbruk); }
.kat-arbeid { --kat-color: var(--kat-arbeid); }
.kat-familie { --kat-color: var(--kat-familie); }
.kat-gjeld { --kat-color: var(--kat-gjeld); }
.kat-tjenester { --kat-color: var(--kat-tjenester); }

/* Section-kicker har sin egen farge */
.sphub-section.kat-bolig .sphub-section-kat { background: var(--kat-bolig); }
.sphub-section.kat-forbruk .sphub-section-kat { background: var(--kat-forbruk); }
.sphub-section.kat-arbeid .sphub-section-kat { background: var(--kat-arbeid); }
.sphub-section.kat-familie .sphub-section-kat { background: var(--kat-familie); }
.sphub-section.kat-gjeld .sphub-section-kat { background: var(--kat-gjeld); }
.sphub-section.kat-tjenester .sphub-section-kat { background: var(--kat-tjenester); }

/* ============================================================
   Alle lover-side
   ============================================================ */
.lover-hero {
  max-width: 760px; padding: 72px 0 32px;
}
.lover-hero .kicker {
  display: none;
}
.lover-hero h1 {
  font-family: var(--serif); font-weight: 500;
  font-size: clamp(24px, 2.6vw, 32px); line-height: 1.2;
  letter-spacing: -0.01em; margin: 0 0 12px;
  color: var(--ink);
}
.lover-hero h1 em {
  font-style: italic; color: var(--accent);
  font-weight: 400;
}
.lover-hero .lead {
  font-family: var(--sans); font-size: 17px;
  line-height: 1.55; color: var(--ink-soft);
  max-width: 580px;
}
.lover-stats {
  display: flex; gap: 40px; margin: 28px 0 0;
  font-family: var(--sans);
}
.lover-stat {
  display: flex; flex-direction: column;
}
.lover-stat .num {
  font-family: var(--serif); font-size: 32px;
  font-weight: 500; line-height: 1; color: var(--accent);
  letter-spacing: -0.02em;
}
.lover-stat .lbl {
  font-size: 11px; letter-spacing: 0.1em;
  text-transform: uppercase; color: var(--ink-mute);
  margin-top: 4px;
}

/* Kategori-grupperinger */
.lover-section {
  margin: 56px 0 0;
  padding-top: 28px;
  border-top: 1px solid var(--line);
}
.lover-section:first-of-type { border-top: none; padding-top: 0; }
.lover-section-head {
  margin-bottom: 20px;
  display: flex; align-items: baseline; gap: 14px;
}
.lover-section h2 {
  font-family: var(--serif); font-size: clamp(20px, 2.2vw, 24px);
  font-weight: 500; letter-spacing: -0.015em;
  margin: 0; color: var(--ink);
}
.lover-section .ant {
  font-family: var(--sans); font-size: 12px;
  color: var(--ink-mute); letter-spacing: 0.04em;
}

/* Lov-kort som editorial registerkort */
.lov-grid {
  display: grid; gap: 12px;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  max-width: 1100px;
}
.lov-kort {
  background: var(--bg-card);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 20px 24px;
  text-decoration: none; color: inherit;
  display: flex; align-items: center; gap: 20px;
  transition: transform 0.2s, border-color 0.2s;
  position: relative;
}
.lov-kort:hover {
  border-color: var(--accent);
}
.lov-kort .lov-num {
  font-family: var(--serif); font-size: 32px;
  font-weight: 500; line-height: 1; color: var(--accent);
  letter-spacing: -0.02em; flex-shrink: 0;
}
.lov-kort .lov-num-lbl {
  font-family: var(--sans); font-size: 10px;
  letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--ink-mute); margin-top: 2px;
}
.lov-kort .lov-meta { flex-shrink: 0; min-width: 64px; }
.lov-kort .lov-info { flex-grow: 1; }
.lov-kort .lov-info h3 {
  font-family: var(--serif); font-size: 20px;
  font-weight: 500; letter-spacing: -0.01em;
  margin: 0 0 2px; color: var(--ink); line-height: 1.25;
}
.lov-kort .lov-info p {
  font-family: var(--sans); font-size: 13px;
  color: var(--ink-soft); margin: 0; line-height: 1.4;
}
.lov-kort .lov-arrow {
  font-family: var(--serif); font-size: 20px;
  color: var(--accent); flex-shrink: 0;
  opacity: 0.5; transition: opacity 0.2s, transform 0.2s;
}
.lov-kort:hover .lov-arrow {
  opacity: 1; transform: translateX(3px);
}

/* ============================================================
   Hjemmeside — minimalistisk søk-fokusert hero (Jony Ive-modus)
   ============================================================ */
.home-hero-v3 {
  padding: 56px 0 40px;
  max-width: 700px;
  margin: 0 auto;
  text-align: center;
}
.home-hero-v3 .hero-line {
  font-family: var(--sans); font-size: 12px;
  color: var(--ink-mute); font-weight: 500;
  letter-spacing: 0.04em; margin-bottom: 28px;
  display: flex; justify-content: center; align-items: center;
  gap: 10px; flex-wrap: wrap;
}
.home-hero-v3 .hero-dot { color: var(--ink-mute); opacity: 0.4; }
.home-hero-v3 .hero-count { white-space: nowrap; }
@media (max-width: 600px) {
  .home-hero-v3 { padding: 36px 0 30px; }
  .home-hero-v3 .hero-line { font-size: 11px; gap: 6px; }
}

/* Søkeboks */
.search-wrapper {
  max-width: 600px;
  margin: 44px auto 0;
  position: relative;
}
.search-input-wrap {
  position: relative;
  background: var(--bg-card);
  border: 1px solid var(--line-strong);
  border-radius: 16px;
  transition: border-color 0.2s, box-shadow 0.2s;
  box-shadow: var(--shadow-sm);
}
.search-input-wrap:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 5px rgba(192,74,38,0.10);
}
.search-input {
  width: 100%;
  padding: 18px 22px 18px 54px;
  font-family: var(--sans); font-size: 17px;
  background: transparent; border: none; outline: none;
  color: var(--ink);
  border-radius: 12px;
}
.search-input::placeholder { color: var(--ink-mute); }
.search-icon {
  position: absolute; left: 18px; top: 50%;
  transform: translateY(-50%);
  width: 18px; height: 18px;
  color: var(--ink-mute);
  pointer-events: none;
}
.search-tags {
  display: flex; gap: 8px; flex-wrap: wrap;
  justify-content: center;
  margin-top: 16px;
}
.search-tag {
  font-family: var(--sans); font-size: 13px;
  padding: 6px 12px; border-radius: 999px;
  background: var(--bg-card); border: 1px solid var(--line);
  color: var(--ink-soft); cursor: pointer;
  text-decoration: none;
  transition: border-color 0.2s, color 0.2s, background 0.2s;
}
.search-tag:hover {
  border-color: var(--accent); color: var(--accent);
}
.search-results {
  position: absolute; top: calc(100% + 8px);
  left: 0; right: 0;
  background: var(--bg-card);
  border: 1px solid var(--line-strong);
  border-radius: 12px;
  box-shadow: var(--shadow-lg);
  max-height: 420px; overflow-y: auto;
  z-index: 50; display: none;
}
.search-results.visible { display: block; }
.search-result {
  display: block; padding: 14px 20px;
  text-decoration: none; color: inherit;
  border-bottom: 1px solid var(--line);
  transition: background 0.15s;
}
.search-result:last-child { border-bottom: none; }
.search-result:hover, .search-result.active {
  background: var(--bg-alt);
}
.search-result .sr-title {
  font-family: var(--serif); font-size: 16px;
  font-weight: 500; color: var(--ink);
  margin-bottom: 2px;
}
.search-result .sr-meta {
  font-family: var(--sans); font-size: 12px;
  color: var(--ink-mute); letter-spacing: 0.02em;
}
.search-result .sr-meta strong { color: var(--accent); font-weight: 600; }
.search-empty {
  padding: 20px; text-align: center;
  color: var(--ink-mute); font-size: 14px;
}

.home-hero-v2 .cta-row {
  display: none;
}

/* Verktøy-seksjon på forsiden — prime position */
.home-vtoy { margin: 0 0 56px; }
.home-vtoy-hd { display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 20px; }
.home-vtoy-hd h2 { font-family: var(--serif); font-size: 28px; font-weight: 400; }
.home-vtoy-alle { font-size: 14px; font-weight: 600; color: var(--accent); text-decoration: none; }
.home-vtoy-alle:hover { color: var(--accent-deep); }
.home-feat-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 14px; }
@media(max-width:960px) { .home-feat-grid { grid-template-columns: repeat(2, 1fr); } }
@media(max-width:500px) { .home-feat-grid { grid-template-columns: 1fr; } }
.home-feat { background: var(--bg-card); border: 1px solid var(--line); border-radius: 16px; padding: 22px 20px; text-decoration: none; color: var(--ink); display: block; transition: box-shadow .15s, border-color .15s, transform .12s; }
.home-feat:hover { border-color: var(--accent); box-shadow: 0 6px 24px rgba(28,23,16,.1); transform: translateY(-2px); }
.home-feat-ikon { font-size: 30px; display: block; margin-bottom: 14px; }
.home-feat-tittel { font-family: var(--serif); font-size: 18px; font-weight: 400; margin-bottom: 8px; line-height: 1.2; }
.home-feat-beskr { font-size: 13px; color: var(--ink-soft); line-height: 1.6; }
.home-quick { display: flex; flex-wrap: wrap; gap: 8px; }
.home-quick a { display: inline-flex; align-items: center; gap: 6px; padding: 8px 14px; background: var(--bg); border: 1px solid var(--line); border-radius: 100px; font-size: 13px; font-weight: 500; color: var(--ink); text-decoration: none; transition: border-color .13s, background .13s; white-space: nowrap; }
.home-quick a:hover { border-color: var(--accent); background: var(--bg-alt); color: var(--accent); }
.home-quick a span { font-size: 15px; }
@media(max-width:600px) { .home-quick a { font-size: 12px; padding: 7px 12px; } }

/* Section headers — strammere */
.home-section-v2 {
  margin: 64px 0;
}
.home-section-head-v2 {
  display: flex; align-items: baseline; justify-content: space-between;
  margin-bottom: 24px; flex-wrap: wrap; gap: 12px;
  padding-bottom: 12px; border-bottom: 1px solid var(--line);
}
.home-section-head-v2 .left .kicker {
  display: none;
}
.home-section-head-v2 h2 {
  font-family: var(--sans); font-size: 13px;
  font-weight: 700; letter-spacing: 0.14em; line-height: 1;
  margin: 0; color: var(--ink); text-transform: uppercase;
}
.home-section-head-v2 .right a {
  font-family: var(--sans); font-size: 13px;
  color: var(--accent); font-weight: 500;
  text-decoration: none; display: inline-flex; gap: 6px;
  transition: opacity 0.2s;
}
.home-section-head-v2 .right a:hover { opacity: 0.7; }

/* Editorial featured-grid for spørsmål på hjemmesiden */
.home-featured-q {
  display: grid; gap: 20px;
  grid-template-columns: 2fr 1fr 1fr;
}
.home-featured-q > a:first-child {
  grid-row: 1 / span 2; padding: 36px 40px;
}
.home-featured-q > a:first-child h3 {
  font-size: clamp(22px, 2.6vw, 30px);
}
@media (max-width: 900px) {
  .home-featured-q { grid-template-columns: 1fr; }
  .home-featured-q > a:first-child { grid-row: auto; }
}

/* ============================================================
   Chat widget
   ============================================================ */
.av-float-cta {
  position: fixed; bottom: 26px; right: 26px; z-index: 1000;
  background: var(--accent); color: #FDFAF5;
  border: none; border-radius: 999px;
  padding: 15px 24px 15px 20px; font-family: var(--sans);
  font-size: 15px; font-weight: 600; letter-spacing: -0.01em; text-decoration: none;
  box-shadow: 0 6px 22px rgba(192,74,38,0.32), 0 2px 6px rgba(31,26,20,0.12);
  transition: transform .22s cubic-bezier(.34,1.56,.64,1), box-shadow .22s ease, background .2s ease;
  display: inline-flex; align-items: center; gap: 10px;
  animation: avCtaIn .5s cubic-bezier(.34,1.56,.64,1) .4s both;
}
.av-float-cta::before {
  content: ""; width: 9px; height: 9px; border-radius: 50%;
  background: #FDFAF5; flex: none;
  box-shadow: 0 0 0 0 rgba(253,250,245,0.7);
  animation: avPulse 2.4s ease-out infinite;
}
.av-float-cta:hover { transform: translateY(-3px) scale(1.02); box-shadow: 0 12px 30px rgba(192,74,38,0.42), 0 3px 8px rgba(31,26,20,0.16); background: var(--accent-deep); color: #FDFAF5; }
.av-float-cta:active { transform: translateY(-1px) scale(.99); }
.av-float-cta:focus-visible { outline: 2px solid var(--accent); outline-offset: 4px; }
.av-float-cta .av-float-cta-icon { display: none; }
@keyframes avCtaIn { from { opacity: 0; transform: translateY(20px) scale(.9); } to { opacity: 1; transform: translateY(0) scale(1); } }
@keyframes avPulse { 0% { box-shadow: 0 0 0 0 rgba(253,250,245,0.6); } 70% { box-shadow: 0 0 0 7px rgba(253,250,245,0); } 100% { box-shadow: 0 0 0 0 rgba(253,250,245,0); } }
@media (prefers-reduced-motion: reduce) { .av-float-cta, .av-float-cta::before { animation: none; } }
@media (max-width: 480px) {
  .av-float-cta { bottom: 16px; right: 16px; padding: 13px 18px 13px 16px; font-size: 13px; gap: 8px; }
}

/* ---------- Advokatvurdering: skjema + resultatkort ---------- */
.av-wrap { max-width: 920px; margin: 0 auto; padding: 56px 24px 80px; }
.av-result-card { display: none; background: linear-gradient(180deg, var(--bg-card) 0%, rgba(253,250,245,.7) 100%); border: 1px solid var(--line-strong); border-radius: 28px; padding: clamp(26px, 4vw, 48px); box-shadow: 0 30px 80px rgba(35,30,25,.12), 0 2px 8px rgba(35,30,25,.04); }
.av-result-card.show { display: block; }
.av-result-card.show > * { opacity: 0; animation: avRise .55s cubic-bezier(.22,1,.36,1) forwards; }
.av-result-card.show > *:nth-child(1) { animation-delay: .02s; }
.av-result-card.show > *:nth-child(2) { animation-delay: .10s; }
.av-result-card.show > *:nth-child(3) { animation-delay: .18s; }
.av-result-card.show > *:nth-child(4) { animation-delay: .26s; }
.av-result-card.show > *:nth-child(5) { animation-delay: .32s; }
.av-result-card.show > *:nth-child(6) { animation-delay: .38s; }
.av-result-card.show > *:nth-child(7) { animation-delay: .44s; }
@keyframes avRise { from { opacity: 0; transform: translateY(16px); } to { opacity: 1; transform: translateY(0); } }
@media (prefers-reduced-motion: reduce) { .av-result-card.show > * { animation: none; opacity: 1; } }
.av-kicker { font-size: 12px; font-weight: 800; color: var(--accent); text-transform: uppercase; letter-spacing: .18em; margin-bottom: 14px; }
.av-result-top { display: flex; justify-content: space-between; gap: 22px; align-items: flex-start; margin-bottom: 18px; }
.av-result-top h2 { font-family: var(--serif); font-weight: 400; font-size: clamp(28px, 3.4vw, 42px); line-height: 1.04; letter-spacing: -.04em; max-width: 620px; }
.av-badge { white-space: nowrap; padding: 9px 15px; border-radius: 999px; background: rgba(194,84,52,.10); color: var(--accent-deep); font-size: 12px; font-weight: 700; letter-spacing: .02em; border: 1px solid rgba(192,74,38,.18); display: inline-flex; align-items: center; gap: 7px; }
.av-badge::before { content: ""; width: 7px; height: 7px; border-radius: 50%; background: var(--accent); flex: none; }
.av-disclaimer { display: flex; gap: 11px; align-items: flex-start; background: var(--bg-alt); border-radius: 14px; padding: 13px 17px; font-size: 13.5px; color: var(--ink-soft); line-height: 1.5; margin-bottom: 24px; max-width: 820px; }
.av-disclaimer::before { content: "\\2696"; font-size: 16px; line-height: 1.3; opacity: .55; flex: none; }
.av-short-box { position: relative; background: var(--ink); color: #F0E9DD; border-radius: 20px; padding: clamp(26px, 3vw, 36px) clamp(24px, 3vw, 34px) clamp(22px, 3vw, 30px); margin: 0 0 28px; overflow: hidden; }
.av-short-box::before { content: "\\201C"; position: absolute; top: 44px; right: 24px; font-family: var(--serif-prose); font-size: 110px; line-height: 1; color: rgba(232,196,180,.10); pointer-events: none; }
.av-short-attr { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; position: relative; }
.av-short-attr .av-roy-dot { width: 30px; height: 30px; border-radius: 50%; background: var(--accent); color: #FDFAF5; font-family: var(--serif); font-size: 15px; font-weight: 600; display: inline-flex; align-items: center; justify-content: center; flex: none; }
.av-short-attr .av-roy-name { font-size: 13px; font-weight: 700; color: #F0E9DD; letter-spacing: .01em; }
.av-short-attr .av-roy-role { font-size: 11.5px; color: rgba(240,233,221,.55); }
.av-short-box p { position: relative; font-family: var(--serif-prose); font-size: clamp(17px, 1.7vw, 21px); line-height: 1.5; letter-spacing: 0; color: #F0E9DD; }
.av-result-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 0 0 16px; }
.av-result-section { background: var(--bg-card); border: 1px solid var(--line); border-radius: 18px; padding: 20px 22px; }
.av-result-section.good { border-left: 3px solid #4E8060; }
.av-result-section.warn { border-left: 3px solid #C28A2E; }
.av-result-section h4 { font-size: 11px; text-transform: uppercase; letter-spacing: .15em; color: var(--ink-mute); margin-bottom: 13px; font-weight: 700; display: flex; align-items: center; gap: 7px; }
.av-result-section.good h4 { color: #3C6B4E; }
.av-result-section.warn h4 { color: #9A6B1E; }
.av-result-section ul, .av-result-section ol { padding-left: 4px; list-style: none; color: var(--ink); font-size: 14.5px; line-height: 1.6; }
.av-result-section ol { counter-reset: avstep; }
.av-result-section li { margin-bottom: 10px; padding-left: 24px; position: relative; }
.av-result-section ul li::before { content: ""; position: absolute; left: 4px; top: 9px; width: 6px; height: 6px; border-radius: 50%; background: currentColor; opacity: .4; }
.av-result-section.good ul li::before { background: #4E8060; opacity: 1; }
.av-result-section.warn ul li::before { background: #C28A2E; opacity: 1; }
.av-result-section ol li { counter-increment: avstep; }
.av-result-section ol li::before { content: counter(avstep); position: absolute; left: 0; top: 1px; width: 19px; height: 19px; border-radius: 50%; background: var(--accent); color: #FDFAF5; font-size: 11px; font-weight: 700; display: flex; align-items: center; justify-content: center; }
.av-result-section.next { margin-top: 16px; background: rgba(194,84,52,.04); border-color: rgba(192,74,38,.14); }
.av-result-section.next h4 { color: var(--accent-deep); }
.av-result-section.missing { margin-top: 16px; background: rgba(78,110,128,.06); border-color: rgba(78,110,128,.18); }
.av-result-section.missing h4 { color: #44606E; }
.av-result-section.missing li::before { background: #4E6E80; opacity: 1; }
.av-result-actions { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 26px; }
.av-btn { font-family: var(--sans); font-size: 15px; font-weight: 600; padding: 13px 24px; border-radius: 999px; border: 1px solid var(--line-strong); cursor: pointer; text-decoration: none; transition: background .15s ease, transform .15s ease; }
.av-btn.primary { background: var(--ink); color: var(--bg-card); border-color: var(--ink); }
.av-btn.primary:hover { transform: translateY(-1px); }
.av-btn.secondary { background: transparent; color: var(--ink); }
.av-btn.secondary:hover { background: var(--bg-alt); }
@media (max-width: 680px) { .av-result-grid { grid-template-columns: 1fr; } .av-result-top { flex-direction: column; } }

/* ---------- Typographic index pages (lover, sporsmal, verktoy) ---------- */
.tk-page { max-width: 1180px; margin: 0 auto; padding: 0 32px; }

.tk-hero { padding: 56px 0 28px; max-width: 760px; }
.tk-hero-label {
  font-family: var(--serif); font-size: 12px;
  font-weight: 500; letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
  margin: 0 0 22px 0;
}
.tk-hero h1 {
  font-family: var(--serif); font-weight: 500;
  font-size: clamp(20px, 2.6vw, 26px);
  line-height: 1.1;
  letter-spacing: -0.022em;
  margin: 0 0 20px 0;
  color: var(--ink);
}
.tk-hero-lead {
  font-family: var(--serif);
  font-size: 15px; line-height: 1.45;
  color: var(--ink-soft);
  margin: 0 0 28px 0;
  max-width: 560px;
}
.tk-hero-meta {
  font-family: var(--serif);
  font-size: 13px; color: var(--ink-mute);
  letter-spacing: 0.005em;
  margin: 0;
}
.tk-hero-meta-sep { margin: 0 12px; opacity: 0.5; }

.tk-cat-bar {
  display: flex; flex-wrap: wrap;
  align-items: baseline; gap: 30px;
  padding: 16px 0 14px 0;
  margin: 32px 0 64px 0;
  border-bottom: 1px solid var(--line);
  position: sticky; top: 0;
  background: linear-gradient(to bottom, var(--bg) 88%, transparent);
  z-index: 20;
}
.tk-cat {
  font-family: var(--serif);
  font-size: 15px; font-weight: 500;
  color: var(--ink-mute); text-decoration: none;
  padding-bottom: 6px;
  border-bottom: 1px solid transparent;
  transition: color 0.18s ease, border-color 0.18s ease;
  letter-spacing: 0.002em;
}
.tk-cat:hover { color: var(--ink); }
.tk-cat.is-active {
  color: var(--ink);
  border-bottom-color: var(--accent);
}

.tk-section { margin: 0 0 80px 0; scroll-margin-top: 80px; }
.tk-section-title {
  font-family: var(--serif); font-weight: 500;
  font-size: clamp(18px, 2vw, 22px);
  letter-spacing: -0.02em;
  line-height: 1.15;
  color: var(--ink);
  margin: 0 0 28px 0;
}

.tk-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: 56px; row-gap: 0;
  border-top: 1px solid var(--line);
}
.tk-row {
  display: grid;
  grid-template-columns: 1fr auto;
  grid-template-rows: auto auto;
  column-gap: 16px; row-gap: 4px;
  align-items: baseline;
  padding: 18px 0;
  border-bottom: 1px solid var(--line);
  text-decoration: none; color: inherit;
  transition: color 0.18s ease;
}
.tk-row-name {
  font-family: var(--serif);
  font-size: 15px; font-weight: 500;
  color: var(--ink);
  letter-spacing: -0.005em;
  grid-column: 1; grid-row: 1;
  letter-spacing: 0.002em;
}
.tk-row-desc {
  font-family: var(--serif);
  font-size: 14px; color: var(--ink-soft);
  line-height: 1.45;
  grid-column: 1; grid-row: 2;
}
.tk-row-arrow {
  grid-column: 2; grid-row: 1 / span 2;
  align-self: center;
  font-family: var(--serif); font-size: 16px;
  color: var(--ink-mute);
  transition: color 0.18s ease, transform 0.2s ease;
  font-weight: 400;
}
.tk-row:hover .tk-row-name { color: var(--ink); }
.tk-row:hover .tk-row-arrow {
  color: var(--accent);
  transform: translateX(3px);
}

@media (min-width: 720px) {
  .tk-grid { position: relative; }
  .tk-grid::before {
    content: "";
    position: absolute;
    left: 50%; top: 0; bottom: 0;
    width: 1px;
    background: var(--line);
    opacity: 0.4;
    pointer-events: none;
  }
}

@media (max-width: 720px) {
  .tk-page { padding: 0 20px; }
  .tk-hero { padding: 40px 0 20px; }
  .tk-cat-bar {
    gap: 18px; margin: 24px 0 40px 0;
    overflow-x: auto; flex-wrap: nowrap;
    scrollbar-width: none;
  }
  .tk-cat-bar::-webkit-scrollbar { display: none; }
  .tk-cat { flex-shrink: 0; font-size: 14px; }
  .tk-section { margin-bottom: 56px; }
  .tk-section-title { font-size: 22px; margin-bottom: 18px; }
  .tk-grid { grid-template-columns: 1fr; column-gap: 0; }
  .tk-row { padding: 16px 0; }
}

/* ---------- Unified site header (homepage + all subpages) ---------- */
.rr-header {
  max-width: 1200px; margin: 0 auto;
  padding: 0 40px;
}
.rr-header-row {
  display: flex; align-items: center; gap: 20px;
  height: 78px;
  border-bottom: 1px solid var(--line);
  position: relative;
}
.rr-logo {
  display: inline-flex; align-items: center; flex: none;
  text-decoration: none; color: var(--ink);
}
.rr-logo svg { display: block; }
.rr-search {
  flex: 1 1 360px; max-width: 400px;
  position: relative; display: flex; align-items: center;
}
.rr-search input {
  width: 100%; height: 42px;
  padding: 0 42px 0 17px;
  border: 1px solid var(--line-strong); border-radius: 12px;
  background: var(--bg-card); color: var(--ink);
  font-family: var(--sans); font-size: 14px;
  transition: border-color .18s ease, box-shadow .18s ease;
}
.rr-search input::placeholder { color: var(--ink-mute); }
.rr-search input:focus {
  outline: none; border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(192,74,38,.10);
}
.rr-search-icon {
  position: absolute; right: 14px; top: 50%; transform: translateY(-50%);
  color: var(--ink-mute); pointer-events: none; display: flex;
}
.rr-search-icon svg { display: block; }
.rr-search-results {
  display: none; position: absolute; top: calc(100% + 8px); left: 0; right: 0;
  background: var(--bg-card); border: 1px solid var(--line-strong); border-radius: 14px;
  box-shadow: 0 16px 40px rgba(35,30,25,.14); padding: 6px; z-index: 100;
  max-height: 420px; overflow-y: auto;
}
.rr-search-results.show { display: block; }
.rr-search-hit {
  display: flex; flex-direction: column; gap: 3px; padding: 10px 13px;
  border-radius: 9px; text-decoration: none; transition: background .12s ease;
}
.rr-search-hit:hover { background: var(--bg-alt); }
.rr-search-tag {
  font-family: var(--sans); font-size: 10px; font-weight: 700; text-transform: uppercase;
  letter-spacing: .1em; color: var(--accent);
}
.rr-search-label { font-family: var(--sans); font-size: 14px; color: var(--ink); line-height: 1.35; }
.rr-search-empty { padding: 14px; font-family: var(--sans); font-size: 14px; color: var(--ink-mute); text-align: center; }
.rr-nav {
  flex: none; margin-left: auto; display: flex; align-items: center;
  gap: 26px;
  font-family: var(--sans);
  font-size: 14px; font-weight: 500;
  letter-spacing: -0.005em;
}
.rr-nav a {
  color: var(--ink); text-decoration: none;
  transition: color 0.15s ease; white-space: nowrap;
}
.rr-nav a:hover { color: var(--accent); }
.rr-nav-cta { color: var(--accent) !important; }
.rr-nav-cta:hover { color: var(--accent-deep) !important; }
.rr-nav a.rr-nav-active { color: var(--accent); }


.rr-burger { display: none; }
.rr-burger-toggle { display: none; }

@media (max-width: 860px) {
  .rr-header { padding: 0 20px; }
  .rr-header-row { flex-wrap: wrap; height: auto; padding: 14px 0; gap: 12px; }
  .rr-logo { order: 1; flex: none; }
  .rr-burger { order: 2; margin-left: auto; }
  .rr-search { order: 3; flex-basis: 100%; max-width: none; }
  .rr-nav { order: 4; margin-left: 0; }

  .rr-burger {
    display: inline-flex; flex-direction: column;
    gap: 5px; padding: 8px; cursor: pointer;
    background: transparent; border: none;
  }
  .rr-burger span {
    display: block; width: 22px; height: 1px; background: var(--ink);
  }
  .rr-nav {
    display: none;
    width: 100%;
    flex-direction: column; gap: 18px;
    align-items: flex-start;
  }
  .rr-burger-toggle:checked ~ .rr-nav { display: flex; }
}

/* ---------- Tjenester page extras (search, progressive disclosure) ---------- */
.tk-search-wrap {
  margin: 24px 0 8px 0;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
  padding: 14px 0;
  display: flex; align-items: center; gap: 16px;
}
.tk-search-icon {
  color: var(--ink-mute); flex-shrink: 0;
  display: inline-flex;
}
.tk-search-input {
  flex: 1; border: none; outline: none; background: transparent;
  font-family: var(--serif);
  font-size: 16px; color: var(--ink);
  letter-spacing: 0.002em;
  padding: 4px 0;
}
.tk-search-input::placeholder { color: var(--ink-mute); }
.tk-search-hint {
  font-family: var(--serif); font-size: 12px;
  color: var(--ink-mute); flex-shrink: 0;
  letter-spacing: 0.01em;
}
@media (max-width: 720px) { .tk-search-hint { display: none; } }

/* Progressive disclosure */
.tk-section[data-collapsed] .tk-row.tk-row-extra { display: none; }
.tk-section:not([data-collapsed]) .tk-show-all { display: none; }
.tk-show-all {
  display: inline-block;
  margin-top: 14px;
  font-family: var(--serif); font-size: 14px;
  color: var(--accent); text-decoration: none;
  letter-spacing: 0.005em;
  transition: color 0.18s ease;
}
.tk-show-all:hover { color: var(--accent-deep); }
.tk-show-all-arrow { transition: transform 0.2s ease; display: inline-block; }
.tk-show-all:hover .tk-show-all-arrow { transform: translateX(3px); }

/* Search filtering states */
.tk-row[data-hidden-by-search] { display: none !important; }
.tk-section[data-hidden-by-search] { display: none !important; }

/* Compact hero for tjenester */
.tk-hero-compact {
  padding: 48px 0 14px;
  max-width: 760px;
}
.tk-hero-compact h1 {
  font-family: var(--serif); font-weight: 500;
  font-size: clamp(24px, 3vw, 32px);
  line-height: 1.08;
  letter-spacing: -0.024em;
  margin: 0 0 14px 0;
  color: var(--ink);
}
.tk-hero-compact-lead {
  font-family: var(--serif);
  font-size: 15px; line-height: 1.4;
  color: var(--ink-soft);
  margin: 0;
  max-width: 540px;
}

/* ---------- Lover rows with metadata (X paragrafer) ---------- */
.tk-row-with-meta {
  grid-template-columns: 1fr auto auto;
  column-gap: 16px;
}
.tk-row-with-meta .tk-row-meta {
  grid-column: 2; grid-row: 1 / span 2;
  align-self: center;
  font-family: var(--serif);
  font-size: 13px;
  color: var(--ink-mute);
  white-space: nowrap;
  letter-spacing: 0.005em;
}
.tk-row-with-meta .tk-row-arrow { grid-column: 3; }
@media (max-width: 720px) {
  .tk-row-with-meta {
    grid-template-columns: 1fr auto;
    grid-template-rows: auto auto auto;
  }
  .tk-row-with-meta .tk-row-name { grid-column: 1; grid-row: 1; }
  .tk-row-with-meta .tk-row-desc { grid-column: 1; grid-row: 2; }
  .tk-row-with-meta .tk-row-meta { grid-column: 1; grid-row: 3; align-self: start; }
  .tk-row-with-meta .tk-row-arrow { grid-column: 2; grid-row: 1 / span 3; }
}

"""

# ============================================================
# HTML TEMPLATES
# ============================================================

SITE_URL = "https://rettsregel.no"

def shared_head(title, description, depth=0, canonical_path=""):
    """depth=0 for homepage, depth=1 for /lover/index.html or /personvern/index.html,
    depth=2 for /lover/[lov]/index.html, depth=3 for /lover/[lov]/[n]/index.html
    canonical_path is the path from site root, e.g. '/lover/angrerettloven/16/'"""
    prefix = "../" * depth
    canonical_url = f"{SITE_URL}{canonical_path}"
    og_title = title.replace(' | Rettsregel', '').replace(' — Rettsregel', '')
    return f"""<!DOCTYPE html>
<html lang="nb">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical_url}">
<link rel="icon" type="image/svg+xml" href="{prefix}favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="{prefix}favicon-32.png">
<link rel="apple-touch-icon" href="{prefix}apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Rettsregel">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical_url}">
<meta property="og:image" content="{SITE_URL}/favicon-512.png">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE_URL}/favicon-512.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}styles.css">
</head>
<body>"""

def site_nav(depth=1, active=None):
    """Unified header med søk — brukes på alle sider. Path prefix from depth.
    active: 'lover' | 'sporsmal' | 'tjenester' | 'om' | None
    """
    if depth == 0:
        prefix = ""
    else:
        prefix = "../" * depth

    def cls(name):
        return ' class="rr-nav-active"' if active == name else ""

    return f"""<div class="rr-header">
  <div class="rr-header-row">
    <a href="{prefix or '/'}" class="rr-logo" aria-label="Rettsregel forside">
      <svg width="44" height="44" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <circle cx="50" cy="50" r="50" fill="#C84A28"/>
        <g fill="#FFF6EC">
          <path d="M33 28 C36 28 38 28 41 28 L41 72 C38 72 36 72 33 72 C34 60 34 40 33 28 Z"/>
          <path d="M40 28 L53 28 C61.5 28 66.5 33 66.5 40 C66.5 46.5 61.5 50.8 53.5 51 L40 51 L40 46 L51.5 46 C56 46 58.8 43.5 58.8 39.6 C58.8 35.6 56 33 51.5 33 L40 33 Z"/>
          <path d="M48 49 L55 49 L68 72 L60 72 L48 51 Z"/>
          <path d="M30 71 L44 71 L44 73.5 L30 73.5 Z"/>
          <path d="M57 71 L71 71 L71 73.5 L57 73.5 Z"/>
          <path d="M30 27 L44 27 L44 29 L30 29 Z"/>
        </g>
      </svg>
    </a>
    <form class="rr-search" role="search" onsubmit="return false;">
      <input type="search" id="rr-search-input" placeholder="Søk i lover, paragrafer, spørsmål og maler..." aria-label="Søk" autocomplete="off">
      <span class="rr-search-icon" aria-hidden="true">
        <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      </span>
      <div class="rr-search-results" id="rr-search-results" role="listbox"></div>
    </form>
    <input type="checkbox" id="rr-burger-toggle" class="rr-burger-toggle" aria-label="Meny">
    <label for="rr-burger-toggle" class="rr-burger" aria-label="Åpne meny">
      <span></span><span></span><span></span>
    </label>
    <nav class="rr-nav" aria-label="Hovedmeny">
      <a href="{prefix}lover/"{cls('lover')}>Lover</a>
      <a href="{prefix}sporsmal/"{cls('sporsmal')}>Spørsmål</a>
      <a href="{prefix}tjenester/"{cls('tjenester')}>Verktøy/maler</a>
      <a href="{prefix}advokatvurdering/" class="rr-nav-cta">Få saken din vurdert →</a>
    </nav>
  </div>
</div>
<script>
(function(){{
  var PREFIX = "{prefix}";
  var input = document.getElementById('rr-search-input');
  var box = document.getElementById('rr-search-results');
  if (!input || !box) return;
  var index = null, loading = false;
  function load(){{
    if (index || loading) return;
    loading = true;
    fetch(PREFIX + 'paragraphs-index.json').then(function(r){{ return r.json(); }}).then(function(d){{ index = d; render(input.value); }}).catch(function(){{}});
  }}
  function urlFor(item){{
    if (item.type === 'sporsmal') return PREFIX + 'sporsmal/' + item.slug + '/';
    return PREFIX + 'lover/' + item.lov + '/' + item.number + '/';
  }}
  function label(item){{
    if (item.type === 'sporsmal') return item.title;
    return item.lov_display + ' § ' + item.number + ' — ' + item.title;
  }}
  function render(q){{
    q = (q || '').trim().toLowerCase();
    if (!index || q.length < 2){{ box.classList.remove('show'); box.innerHTML = ''; return; }}
    var hits = [];
    for (var i = 0; i < index.length && hits.length < 8; i++){{
      var it = index[i];
      var hay = (label(it) + ' ' + (it.kort_svar || '')).toLowerCase();
      if (hay.indexOf(q) !== -1) hits.push(it);
    }}
    if (!hits.length){{ box.innerHTML = '<div class="rr-search-empty">Ingen treff på «' + q + '»</div>'; box.classList.add('show'); return; }}
    box.innerHTML = hits.map(function(it){{
      var tag = it.type === 'sporsmal' ? 'Spørsmål' : 'Paragraf';
      return '<a class="rr-search-hit" href="' + urlFor(it) + '"><span class="rr-search-tag">' + tag + '</span><span class="rr-search-label">' + label(it) + '</span></a>';
    }}).join('');
    box.classList.add('show');
  }}
  input.addEventListener('focus', load);
  input.addEventListener('input', function(){{ render(input.value); }});
  document.addEventListener('click', function(e){{ if (!e.target.closest('.rr-search')) box.classList.remove('show'); }});
}})();
</script>
"""

def chat_widget():
    """Returns a floating CTA button linking to the guided case assessment (advokatvurdering)."""
    return """<!-- Rettsregel advokatvurdering CTA -->
<a href="/advokatvurdering/" id="av-float-cta" class="av-float-cta" aria-label="Gratis vurdering av din sak">
  <span>Gratis vurdering av din sak</span>
</a>"""

def site_footer(depth=0):
    """Minimal site footer — single line, three links. Shared across all pages."""
    prefix = "../" * depth
    return f"""<footer class="site-footer">
  <span class="site-footer-copy">© 2026 Walrus AS</span>
  <span class="site-footer-links">
    <a href="{prefix}om/">Om</a>
    <a href="{prefix}personvern/">Personvern</a>
    <a href="mailto:rettsregel@gmail.com">Kontakt</a>
  </span>
</footer>
{chat_widget()}
</body>
</html>"""


def contact_form(depth=0):
    prefix = "../" * depth
    return f"""<section class="cta-section" id="skjema">
  <div class="container">
    <div class="cta-grid">
      <div class="cta-intro">
        <h2>Har du en <em>sak</em> du lurer på?</h2>
        <p>Beskriv kort hva det gjelder, så tar vi kontakt og forteller deg hva du kan gjøre videre.</p>
      </div>
      <div>
        <form class="contact-form" id="kontaktskjema" action="https://formspree.io/f/mvzldpwj" method="POST">
          <div class="form-field">
            <label for="beskrivelse">Beskriv saken din</label>
            <textarea id="beskrivelse" name="beskrivelse" placeholder="Skriv kort hva det gjelder. Du trenger ikke å bruke juridiske ord." required></textarea>
          </div>
          <div class="form-field">
            <label for="telefon">Telefonnummer</label>
            <input type="tel" id="telefon" name="telefon" placeholder="12 34 56 78" required>
          </div>
          <div class="form-field">
            <label for="epost">E-post</label>
            <input type="email" id="epost" name="epost" placeholder="navn@eksempel.no" required>
          </div>
          <button type="submit" class="form-submit">
            Send inn
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
          <p class="form-note">Vi leser alle henvendelser. Hvis vi ikke kan hjelpe direkte, peker vi deg til noen som kan. Ved å sende godtar du vår <a href="{prefix}personvern/">personvernerklæring</a>.</p>
        </form>
        <div id="form-success" class="form-success">
          <h3>Takk!</h3>
          <p>Vi har mottatt saken din og tar kontakt så snart vi kan.</p>
        </div>
      </div>
    </div>
  </div>
</section>
<script>
document.getElementById('kontaktskjema').addEventListener('submit', async function(e) {{
  const form = e.target;
  e.preventDefault();
  try {{
    const res = await fetch(form.action, {{
      method: 'POST', body: new FormData(form),
      headers: {{ 'Accept': 'application/json' }}
    }});
    if (res.ok) {{
      form.classList.add('hide');
      document.getElementById('form-success').classList.add('show');
    }} else {{
      alert('Noe gikk galt. Prøv igjen, eller send oss en e-post på rettsregel@gmail.com');
    }}
  }} catch (err) {{
    console.error(err);
    alert('Noe gikk galt. Prøv igjen, eller send oss en e-post på rettsregel@gmail.com');
  }}
}});
</script>"""

def auto_link_paragraphs(text, current_lov, depth=3):
    """Convert references like '§ 6-50' or 'skatteloven § 6-50' to links.
    depth is the depth of the current page (3 for paragraph pages)."""
    prefix = "../" * depth
    # Pattern: optional lov name, then § number
    pattern = r'(?:([a-zæøå]+loven)\s+)?§\s*(\d+(?:-\d+)?[a-z]?)'
    def replace(m):
        lov = m.group(1) or current_lov
        # Normalize lov name (remove special chars)
        lov_url = lov.replace("ø", "o").replace("æ", "ae").replace("å", "aa")
        paragraf = m.group(2)
        # Display version keeps original lov name
        if m.group(1):
            display = f"{m.group(1)} § {paragraf}"
        else:
            display = f"§ {paragraf}"
        return f'<a href="{prefix}lover/{lov_url}/{paragraf}/">{display}</a>'
    return re.sub(pattern, replace, text)

def paragraf_sort_key(p):
    """Sortér paragrafer numerisk: § 2-1 før § 10, § 88a etter § 88."""
    num = str(p.get("number", ""))
    parts = []
    cur = ""
    is_digit = None
    for ch in num:
        ch_digit = ch.isdigit()
        if is_digit is None:
            is_digit = ch_digit
            cur = ch
        elif ch_digit == is_digit:
            cur += ch
        else:
            parts.append(int(cur) if is_digit else cur)
            cur = ch
            is_digit = ch_digit
    if cur:
        parts.append(int(cur) if is_digit else cur)
    # Sammenligning: konverter alle til (type, value) for å sortere safe
    return tuple((0, p) if isinstance(p, int) else (1, p) for p in parts)


def render_paragraph_page(p):
    lov_url = p["lov"].replace("ø", "o").replace("æ", "ae").replace("å", "aa")
    title_tag = f'{p["lov_display"]} § {p["number"]} — {p["title"]} | Rettsregel'
    depth = 3
    prefix = "../" * depth

    available_set = set()
    for ap in PARAGRAPHS:
        ap_lov_url = ap["lov"].replace("ø", "o").replace("æ", "ae").replace("å", "aa")
        available_set.add(f"{ap_lov_url}/{ap['number']}")

    LOV_DISPLAY_MAP = {
        "angrerettloven": "Angrerettloven", "kjopsloven": "Kjøpsloven",
        "husleieloven": "Husleieloven", "forbrukerkjopsloven": "Forbrukerkjøpsloven",
        "avhendingslova": "Avhendingslova", "bustadoppforingslova": "Bustadoppføringslova",
        "naboloven": "Naboloven", "navneloven": "Navneloven", "arveloven": "Arveloven",
        "tomtefesteloven": "Tomtefesteloven", "ekteskapsloven": "Ekteskapsloven",
    }

    # ── Eksempler ────────────────────────────────────────────────────────────
    examples_html = ""
    for ex in p["eksempler"]:
        examples_html += (f'<div class="lap-ex"><p class="lap-ex-label">Eksempel '
                          f'<span class="lap-ex-dot">·</span> {ex["navn"]}</p>'
                          f'<p class="lap-ex-txt">{ex["tekst"]}</p></div>')

    # ── Vanlige feil ───────────────────────────────────────────────────────
    vanlige_feil_html = '<ul class="lap-list">' + "".join(f"<li>{vf}</li>" for vf in p["vanlige_feil"]) + "</ul>"

    # ── Dumme spørsmål (beholdt) ─────────────────────────────────────────────
    faq_html = ""
    if p["dumme_sporsmal"]:
        faq_items = ""
        for qa in p["dumme_sporsmal"]:
            faq_items += f'<div class="lap-faq-item"><p class="lap-faq-q">{qa["q"]}</p><p class="lap-faq-a">{qa["a"]}</p></div>'
        faq_html = f'<h2 class="lap-h2">Dumme spørsmål</h2><div class="lap-faq">{faq_items}</div>'

    # ── Relaterte (sidebar-rader) ────────────────────────────────────────────
    related_rows = ""
    for r in p["related"]:
        r_lov_url = r["lov"].replace("ø", "o").replace("æ", "ae").replace("å", "aa")
        if f"{r_lov_url}/{r['paragraf']}" not in available_set:
            continue
        related_rows += (f'<a class="lap-rel-row" href="{prefix}lover/{r_lov_url}/{r["paragraf"]}/">'
                         f'<span class="lap-rel-num">§ {r["paragraf"]}</span>'
                         f'<span class="lap-rel-title">{r["tittel"]}</span>'
                         f'<span class="lap-rel-arrow" aria-hidden="true">&rarr;</span></a>')
    related_block = ""
    if related_rows:
        related_block = (f'<div class="lap-side-block"><p class="lap-side-label">Relaterte paragrafer</p>'
                         f'<div class="lap-rel">{related_rows}</div>'
                         f'<a class="lap-side-more" href="{prefix}lover/{lov_url}/">Se alle paragrafer i {p["lov_display"]} &rarr;</a></div>')

    # ── Prosa (auto-lenket) ──────────────────────────────────────────────────
    hva_betyr = auto_link_paragraphs(p["hva_betyr_html"], p["lov"], depth=3)
    hva_bor_du = auto_link_paragraphs(p.get("hva_bor_du_html", ""), p["lov"], depth=3) if p.get("hva_bor_du_html") else ""

    canonical = f"/lover/{lov_url}/{p['number']}/"
    head = shared_head(title_tag, p["description"], depth=3, canonical_path=canonical)
    nav = site_nav(depth=3, active="lover")
    footer = site_footer(depth=3)

    STYLE = """<style>
.lap-page { max-width: 1140px; margin: 0 auto; padding: 32px 48px 40px; }

.lap-crumb { font-family: var(--serif); font-size: 13px; color: var(--ink-mute); margin-bottom: 40px; letter-spacing: 0.01em; }
.lap-crumb a { color: var(--ink-mute); text-decoration: none; }
.lap-crumb a:hover { color: var(--ink); }
.lap-crumb .sep { margin: 0 9px; opacity: 0.45; }
.lap-crumb .cur { color: var(--accent); }

.lap-layout { display: grid; grid-template-columns: minmax(0, 720px) 300px; gap: 0; justify-content: center; align-items: start; }
.lap-main { min-width: 0; max-width: 720px; }

/* Header */
.lap-eyebrow { font-family: var(--serif); font-size: 11px; font-weight: 500; letter-spacing: 0.22em; text-transform: uppercase; color: var(--accent); margin: 0 0 18px; }
.lap-title { font-family: var(--serif); font-weight: 500; font-size: clamp(26px, 3.3vw, 36px); line-height: 1.12; letter-spacing: -0.024em; color: var(--ink); margin: 0 0 18px; }
.lap-title .num { color: var(--accent); }
.lap-intro { font-family: var(--serif-prose); font-size: 18px; line-height: 1.6; color: var(--ink-soft); margin: 0 0 44px; }

/* Kort svar — rust venstrelinje, nesten usynlig cream */
.lap-kort { border-left: 2px solid var(--accent); background: rgba(192,74,38,0.035); padding: 18px 24px; margin: 0 0 48px; border-radius: 0 4px 4px 0; }
.lap-kort-label { font-family: var(--serif); font-size: 10.5px; font-weight: 500; letter-spacing: 0.22em; text-transform: uppercase; color: var(--accent); margin: 0 0 10px; }
.lap-kort p { font-family: var(--serif-prose); font-size: 17px; line-height: 1.6; color: var(--ink); margin: 0; }

/* Seksjonsoverskrifter */
.lap-h2 { font-family: var(--serif); font-weight: 500; font-size: 21px; line-height: 1.2; letter-spacing: -0.018em; color: var(--ink); margin: 48px 0 18px; }

/* Lovtekst — kildetekst, ikke kort */
.lap-lovtekst { border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); padding: 22px 0; margin: 0; font-family: var(--serif-prose); font-size: 16px; line-height: 1.75; color: var(--ink-soft); white-space: pre-line; }
.lap-lovtekst p { margin: 0 0 14px; }
.lap-lovtekst p:last-of-type { margin-bottom: 0; }
.lap-lovtekst ol, .lap-lovtekst ul { margin: 0 0 14px 22px; }
.lap-lovtekst li { margin-bottom: 8px; }
.lap-kilde { display: block; margin-top: 16px; font-family: var(--serif); font-size: 12.5px; color: var(--ink-mute); letter-spacing: 0.01em; }

/* Prosa */
.lap-prose { font-family: var(--serif-prose); font-size: 18px; line-height: 1.7; color: var(--ink); }
.lap-prose p { margin: 0 0 18px; }
.lap-prose p:last-child { margin-bottom: 0; }
.lap-prose strong { font-weight: 600; color: var(--ink); }
.lap-prose ul, .lap-prose ol { margin: 18px 0 18px 24px; }
.lap-prose li { margin-bottom: 9px; }
.lap-prose h3 { font-family: var(--serif); font-weight: 500; font-size: 17px; color: var(--ink); margin: 28px 0 12px; }
.lap-prose a { color: var(--accent); text-decoration: none; border-bottom: 1px solid rgba(192,74,38,0.3); }
.lap-prose a:hover { border-bottom-color: var(--accent); }

/* Eksempler — svak cream, ikke kort */
.lap-ex { background: rgba(28,23,16,0.025); border-radius: 6px; padding: 18px 22px; margin: 0 0 14px; }
.lap-ex:last-child { margin-bottom: 0; }
.lap-ex-label { font-family: var(--serif); font-size: 13px; font-weight: 500; letter-spacing: 0.04em; color: var(--accent); margin: 0 0 8px; }
.lap-ex-dot { opacity: 0.55; margin: 0 2px; }
.lap-ex-txt { font-family: var(--serif-prose); font-size: 16.5px; line-height: 1.6; color: var(--ink); margin: 0; }

/* Vanlige feil — enkel liste */
.lap-list { font-family: var(--serif-prose); font-size: 17px; line-height: 1.6; color: var(--ink); margin: 0; padding-left: 22px; }
.lap-list li { margin-bottom: 10px; }
.lap-list li:last-child { margin-bottom: 0; }

/* Dumme spørsmål */
.lap-faq { display: flex; flex-direction: column; }
.lap-faq-item { padding: 18px 0; border-bottom: 1px solid var(--line); }
.lap-faq-item:last-child { border-bottom: none; }
.lap-faq-q { font-family: var(--serif); font-weight: 500; font-size: 16.5px; color: var(--ink); margin: 0 0 7px; }
.lap-faq-a { font-family: var(--serif-prose); font-size: 16.5px; line-height: 1.6; color: var(--ink-soft); margin: 0; }

/* Sidebar */
.lap-side { padding-left: 48px; border-left: 1px solid var(--line); position: sticky; top: 32px; }
.lap-side-block { margin-bottom: 40px; }
.lap-side-block:last-child { margin-bottom: 0; }
.lap-side-label { font-family: var(--serif); font-size: 10.5px; font-weight: 500; letter-spacing: 0.22em; text-transform: uppercase; color: var(--accent); margin: 0 0 16px; }

.lap-rel { display: flex; flex-direction: column; }
.lap-rel-row { display: grid; grid-template-columns: auto 1fr auto; align-items: baseline; gap: 12px; padding: 12px 0; border-bottom: 1px solid var(--line); text-decoration: none; color: inherit; }
.lap-rel-row:first-child { padding-top: 0; }
.lap-rel-num { font-family: var(--serif); font-size: 13px; color: var(--accent); white-space: nowrap; }
.lap-rel-title { font-family: var(--serif); font-size: 14px; color: var(--ink-soft); line-height: 1.35; transition: color .15s; }
.lap-rel-arrow { font-family: var(--serif); font-size: 14px; color: var(--ink-mute); transition: color .18s, transform .22s; }
.lap-rel-row:hover .lap-rel-title { color: var(--ink); }
.lap-rel-row:hover .lap-rel-arrow { color: var(--accent); transform: translateX(4px); }
.lap-side-more { display: inline-block; margin-top: 16px; font-family: var(--serif); font-size: 13px; color: var(--ink-mute); text-decoration: none; line-height: 1.4; transition: color .15s; }
.lap-side-more:hover { color: var(--accent); }

.lap-disc { border-left: 2px solid var(--accent); padding-left: 16px; }
.lap-disc p { font-family: var(--serif); font-size: 13px; line-height: 1.55; color: var(--ink-mute); margin: 0; }
.lap-disc a { color: var(--accent); text-decoration: none; }
.lap-disc a:hover { color: var(--accent-deep); }

.lap-cta-title { font-family: var(--serif); font-weight: 500; font-size: 16px; color: var(--ink); margin: 0 0 8px; line-height: 1.3; }
.lap-cta-txt { font-family: var(--serif); font-size: 14px; line-height: 1.5; color: var(--ink-mute); margin: 0 0 12px; }
.lap-cta-link { font-family: var(--serif); font-size: 15px; color: var(--accent); text-decoration: none; }
.lap-cta-link:hover { color: var(--accent-deep); }

@media (max-width: 920px) {
  .lap-page { padding: 26px 22px 48px; }
  .lap-crumb { margin-bottom: 30px; }
  .lap-layout { grid-template-columns: 1fr; }
  .lap-main { max-width: 100%; }
  .lap-side { padding-left: 0; border-left: none; position: static; margin-top: 56px; padding-top: 40px; border-top: 1px solid var(--line); }
}
</style>"""

    BODY = f"""{STYLE}
<main class="lap-page">
  <nav class="lap-crumb" aria-label="Brødsmuler">
    <a href="{prefix}">Hjem</a><span class="sep">/</span><a href="{prefix}lover/">Lover</a><span class="sep">/</span><a href="{prefix}lover/{lov_url}/">{p["lov_display"]}</a><span class="sep">/</span><span class="cur">§ {p["number"]}</span>
  </nav>

  <div class="lap-layout">
    <article class="lap-main">
      <header>
        <p class="lap-eyebrow">{p["lov_display"]}</p>
        <h1 class="lap-title"><span class="num">§ {p["number"]}</span> — {p["title"]}</h1>
        <p class="lap-intro">{p["description"]}</p>
      </header>

      <div class="lap-kort">
        <p class="lap-kort-label">Kort svar</p>
        <p>{p["kort_svar"]}</p>
      </div>

      <h2 class="lap-h2">Paragraftekst</h2>
      <div class="lap-lovtekst">{p["paragraftekst"]}<span class="lap-kilde">— Kilde: Lovdata</span></div>

      <h2 class="lap-h2">Hva betyr dette på vanlig norsk?</h2>
      <div class="lap-prose">{hva_betyr}</div>

      <h2 class="lap-h2">Eksempel{"er" if len(p["eksempler"]) > 1 else ""}</h2>
      {examples_html}

      <h2 class="lap-h2">Vanlige feil</h2>
      {vanlige_feil_html}

      <h2 class="lap-h2">Hva bør du gjøre?</h2>
      <div class="lap-prose">{hva_bor_du}</div>

      {faq_html}
    </article>

    <aside class="lap-side">
      {related_block}

      <div class="lap-side-block">
        <div class="lap-disc">
          <p>Juridisk informasjon, ikke rådgivning. Innholdet bygger på gjeldende norsk lov. Ved tvil — kontakt advokat. <a href="{prefix}om/">Mer om Rettsregel &rarr;</a></p>
        </div>
      </div>

      <div class="lap-side-block">
        <p class="lap-cta-title">Trenger du hjelp med en konkret sak?</p>
        <p class="lap-cta-txt">Beskriv kort hva det gjelder, så kan vi peke deg videre.</p>
        <a class="lap-cta-link" href="{prefix}kontakt/">Send inn sak &rarr;</a>
      </div>
    </aside>
  </div>
</main>
"""

    return head + "\n" + nav + "\n" + BODY + "\n" + footer

def render_lov_index(lov_name, lov_display, paragraphs):
    """Lov-oversikt — varm, navigerbar innholdsfortegnelse."""
    import re as _re
    depth = 2
    prefix = "../" * depth

    LOV_META = {
        "angrerettloven": {"desc": "Angrerett ved netthandel og kjøp utenfor butikk — frister, unntak og hvordan du går fram.", "cat": "Forbruk", "featured": ["16", "20", "21", "22"]},
        "kjopsloven": {"desc": "Kjøp mellom private og mellom bedrifter — mangel, reklamasjon, forsinkelse og heving.", "cat": "Forbruk", "featured": ["17", "32", "39", "30"]},
        "forbrukerkjopsloven": {"desc": "Dine rettigheter når du kjøper varer fra en næringsdrivende — mangel, retting, omlevering og heving.", "cat": "Forbruk", "featured": ["16", "26", "27", "33"]},
        "husleieloven": {"desc": "Leie av bolig — depositum, vedlikehold, leieforhøyelse, oppsigelse og tilbakelevering.", "cat": "Bolig", "featured": ["3-5", "9-5", "10-2", "2-10", "5-3"]},
        "avhendingslova": {"desc": "Kjøp og salg av bolig, hytte og tomt — mangler, selgers opplysningsplikt og reklamasjon.", "cat": "Bolig", "featured": ["3-7", "4-19", "3-9", "4-8"]},
        "naboloven": {"desc": "Grenser for hva naboer kan gjøre — trær, gjerde, støy, graving og tålegrensen.", "cat": "Bolig", "featured": ["2", "3", "6", "10"]},
        "navneloven": {"desc": "Fornavn, etternavn og navnebytte for deg og familien.", "cat": "Familie", "featured": ["2", "7", "8", "9"]},
        "arveloven": {"desc": "Hvem som arver hva — pliktdel, testament, uskifte og arvegangsrekkefølge.", "cat": "Arv", "featured": ["2", "29", "50", "8"]},
        "bustadoppforingslova": {"desc": "Når du bygger nytt eller kjøper bolig under oppføring — garanti, dagmulkt og overtakelse.", "cat": "Bolig", "featured": ["12", "14", "18", "30"]},
        "tomtefesteloven": {"desc": "Når du leier tomt til hus du eier — festeavgift, regulering, innløsning og lenging.", "cat": "Bolig", "featured": ["1", "7", "32", "37"]},
        "ekteskapsloven": {"desc": "Hvem kan gifte seg, og hvordan — vilkår, prøvingsattest, vigsling og ugyldighet.", "cat": "Familie", "featured": ["1", "1a", "1b", "11"]},
    }
    meta = LOV_META.get(lov_name, {"desc": f"{lov_display} paragraf for paragraf, på vanlig norsk.", "cat": "Lov", "featured": []})

    n = len(paragraphs)
    by_num = {p["number"]: p for p in paragraphs}

    def pkey(num):
        out = []
        for part in num.split("-"):
            m = _re.match(r"(\d+)([a-z]*)", part)
            out.append((int(m.group(1)), m.group(2)) if m else (0, part))
        return out

    def excerpt_of(p, lim=92):
        e = p.get("kort_svar") or p.get("description") or ""
        e = e.replace("\n", " ").strip()
        if len(e) > lim:
            e = e[:lim].rsplit(" ", 1)[0] + "…"
        return e

    def row_html(p):
        d = excerpt_of(p)
        desc = f'<span class="lovx-row-desc">{d}</span>' if d else ""
        return (f'<a class="lovx-row" href="{prefix}lover/{lov_name}/{p["number"]}/">'
                f'<span class="lovx-row-num">§ {p["number"]}</span>'
                f'<span class="lovx-row-body"><span class="lovx-row-title">{p["title"]}</span>{desc}</span>'
                f'<span class="lovx-row-arrow" aria-hidden="true">&rarr;</span></a>')

    chaptered = n > 0 and all("-" in p["number"] for p in paragraphs)

    if chaptered:
        chaps = {}
        for p in sorted(paragraphs, key=lambda x: pkey(x["number"])):
            chaps.setdefault(p["number"].split("-")[0], []).append(p)
        chap_keys = sorted(chaps, key=lambda k: (int(re.match(r"\d+", k).group()), k))
        main_sections = ""
        chap_links = ""
        for k in chap_keys:
            rows = "".join(row_html(p) for p in chaps[k])
            main_sections += (f'<section class="lovx-chapter" id="kap-{k}">'
                              f'<h2 class="lovx-chapter-h">Kapittel {k}</h2>'
                              f'<div class="lovx-rows">{rows}</div></section>')
            chap_links += f'<a class="lovx-chap" href="#kap-{k}">Kapittel {k}</a>'
        innhold_block = (f'<div class="lovx-side-block"><p class="lovx-side-label">Innhold</p>'
                         f'<nav class="lovx-chaplist">{chap_links}</nav></div>')
    else:
        rows = "".join(row_html(p) for p in sorted(paragraphs, key=lambda x: pkey(x["number"])))
        main_sections = f'<section class="lovx-chapter"><div class="lovx-rows">{rows}</div></section>'
        innhold_block = ""

    mest_items = ""
    for fn in meta.get("featured", []):
        fp = by_num.get(fn)
        if not fp:
            continue
        mest_items += (f'<a class="lovx-mest-item" href="{prefix}lover/{lov_name}/{fp["number"]}/">'
                       f'<span class="lovx-mest-num">§ {fp["number"]}</span>'
                       f'<span class="lovx-mest-title">{fp["title"]}</span></a>')
    mest_block = ""
    if mest_items:
        mest_block = (f'<div class="lovx-side-block"><p class="lovx-side-label">Mest lest</p>'
                      f'<div class="lovx-mest">{mest_items}</div>'
                      f'<a class="lovx-side-more" href="#lovx-list">Se alle paragrafer &rarr;</a></div>')

    head = shared_head(
        f"{lov_display} forklart på vanlig norsk | Rettsregel",
        meta["desc"], depth=2, canonical_path=f"/lover/{lov_name}/")
    nav = site_nav(depth=2, active="lover")
    footer = site_footer(depth=2)

    STYLE = """<style>
.lovx-page { max-width: 1080px; margin: 0 auto; padding: 36px 48px 72px; }

.lovx-crumb { font-family: var(--serif); font-size: 13px; color: var(--ink-mute); margin-bottom: 44px; letter-spacing: 0.01em; }
.lovx-crumb a { color: var(--ink-mute); text-decoration: none; }
.lovx-crumb a:hover { color: var(--ink); }
.lovx-crumb .sep { margin: 0 9px; opacity: 0.45; }
.lovx-crumb .cur { color: var(--accent); }

.lovx-head { margin-bottom: 30px; }
.lovx-title { font-family: var(--serif); font-weight: 500; font-size: clamp(28px, 3.4vw, 38px); line-height: 1.06; letter-spacing: -0.026em; color: var(--ink); margin: 0 0 16px; }
.lovx-desc { font-family: var(--serif); font-size: 17px; line-height: 1.5; color: var(--ink-soft); margin: 0 0 16px; max-width: 580px; }
.lovx-meta { font-family: var(--serif); font-size: 14px; color: var(--ink-mute); letter-spacing: 0.01em; }
.lovx-meta .dot { margin: 0 10px; opacity: 0.45; }

.lovx-search-wrap { position: relative; margin-bottom: 4px; }
.lovx-search { width: 100%; box-sizing: border-box; font-family: var(--serif); font-size: 16px; color: var(--ink); background: transparent; border: none; border-bottom: 1px solid var(--ink); padding: 13px 4px 13px 28px; outline: none; }
.lovx-search::placeholder { color: var(--ink-mute); }
.lovx-search:focus { border-bottom-color: var(--accent); }
.lovx-search-icon { position: absolute; left: 2px; top: 50%; transform: translateY(-50%); width: 16px; height: 16px; color: var(--ink-mute); pointer-events: none; }

.lovx-layout { display: grid; grid-template-columns: 232px 1fr; gap: 0; margin-top: 48px; align-items: start; }

.lovx-side { position: sticky; top: 32px; padding-right: 40px; }
.lovx-side-block { margin-bottom: 40px; }
.lovx-side-block:last-child { margin-bottom: 0; }
.lovx-side-label { font-family: var(--serif); font-size: 10.5px; font-weight: 500; letter-spacing: 0.22em; text-transform: uppercase; color: var(--accent); margin: 0 0 16px; }
.lovx-chaplist { display: flex; flex-direction: column; }
.lovx-chap { font-family: var(--serif); font-size: 14.5px; color: var(--ink-soft); text-decoration: none; padding: 7px 0 7px 14px; border-left: 2px solid transparent; line-height: 1.3; transition: color .15s, border-color .15s; }
.lovx-chap:hover { color: var(--ink); border-left-color: var(--accent); }

.lovx-mest { display: flex; flex-direction: column; }
.lovx-mest-item { display: block; text-decoration: none; padding: 10px 0; border-bottom: 1px solid var(--line); }
.lovx-mest-item:first-child { padding-top: 0; }
.lovx-mest-item:last-child { border-bottom: none; }
.lovx-mest-num { font-family: var(--serif); font-size: 13px; color: var(--accent); }
.lovx-mest-title { font-family: var(--serif); font-size: 14px; color: var(--ink-soft); display: block; margin-top: 3px; line-height: 1.35; transition: color .15s; }
.lovx-mest-item:hover .lovx-mest-title { color: var(--ink); }
.lovx-side-more { display: inline-block; margin-top: 16px; font-family: var(--serif); font-size: 13px; color: var(--ink-mute); text-decoration: none; transition: color .15s; }
.lovx-side-more:hover { color: var(--accent); }

.lovx-main { min-width: 0; border-left: 1px solid var(--line); padding-left: 48px; }
.lovx-chapter { margin-bottom: 40px; }
.lovx-chapter:last-child { margin-bottom: 0; }
.lovx-chapter-h { font-family: var(--serif); font-weight: 500; font-size: 14px; letter-spacing: 0.05em; text-transform: uppercase; color: var(--ink-mute); margin: 0; padding-bottom: 14px; border-bottom: 1px solid var(--ink); }

.lovx-rows { display: flex; flex-direction: column; }
.lovx-row { display: grid; grid-template-columns: 60px 1fr 24px; align-items: baseline; gap: 16px; padding: 19px 0; border-bottom: 1px solid var(--line); text-decoration: none; color: inherit; }
.lovx-row-num { font-family: var(--serif); font-size: 14px; color: var(--accent); white-space: nowrap; }
.lovx-row-body { min-width: 0; }
.lovx-row-title { font-family: var(--serif); font-size: 17px; font-weight: 500; color: var(--ink); line-height: 1.25; letter-spacing: -0.012em; display: block; transition: color .15s; }
.lovx-row-desc { font-family: var(--serif); font-size: 14.5px; color: var(--ink-mute); line-height: 1.45; margin-top: 5px; display: block; }
.lovx-row-arrow { font-family: var(--serif); font-size: 17px; color: var(--ink-mute); line-height: 1; text-align: right; transition: color .18s, transform .22s; }
.lovx-row:hover .lovx-row-arrow { color: var(--accent); transform: translateX(6px); }
.lovx-row:hover .lovx-row-title { color: var(--ink); }

.lovx-empty { display: none; font-family: var(--serif); font-size: 16px; color: var(--ink-mute); padding: 28px 0; }

.lovx-attest { max-width: 1080px; margin: 56px auto 0; padding: 0 48px; }
.lovx-attest-inner { border-top: 1px solid var(--line); padding-top: 20px; font-family: var(--serif); font-size: 12.5px; color: var(--ink-mute); line-height: 1.55; max-width: 640px; }
.lovx-attest-inner a { color: var(--accent); text-decoration: none; }
.lovx-attest-inner a:hover { color: var(--accent-deep); }

@media (max-width: 860px) {
  .lovx-page { padding: 26px 22px 56px; }
  .lovx-crumb { margin-bottom: 32px; }
  .lovx-layout { grid-template-columns: 1fr; margin-top: 36px; }
  .lovx-side { position: static; padding-right: 0; margin-bottom: 8px; }
  .lovx-side-block { margin-bottom: 32px; }
  .lovx-chaplist { flex-direction: row; overflow-x: auto; gap: 22px; padding-bottom: 6px; -webkit-overflow-scrolling: touch; }
  .lovx-chap { border-left: none; padding: 4px 0; white-space: nowrap; }
  .lovx-chap:hover { border-left: none; }
  .lovx-main { border-left: none; padding-left: 0; }
  .lovx-attest { padding: 0 22px; }
}
</style>"""

    SCRIPT = """<script>
(function(){
  var inp = document.getElementById('lovxSearch');
  if(!inp) return;
  var rows = [].slice.call(document.querySelectorAll('.lovx-row'));
  var chapters = [].slice.call(document.querySelectorAll('.lovx-chapter'));
  var empty = document.getElementById('lovxEmpty');
  inp.addEventListener('input', function(){
    var q = this.value.toLowerCase().trim();
    var visible = 0;
    rows.forEach(function(r){
      var m = !q || r.textContent.toLowerCase().indexOf(q) !== -1;
      r.style.display = m ? '' : 'none';
      if(m) visible++;
    });
    chapters.forEach(function(c){
      var any = false;
      var rs = c.querySelectorAll('.lovx-row');
      for(var i=0;i<rs.length;i++){ if(rs[i].style.display !== 'none'){ any = true; break; } }
      c.style.display = any ? '' : 'none';
    });
    if(empty) empty.style.display = (visible === 0 && q) ? 'block' : 'none';
  });
})();
</script>"""

    BODY = f"""{STYLE}
<main class="lovx-page">
  <nav class="lovx-crumb" aria-label="Brødsmuler">
    <a href="{prefix}">Hjem</a><span class="sep">/</span><a href="{prefix}lover/">Lover</a><span class="sep">/</span><span class="cur">{lov_display}</span>
  </nav>

  <header class="lovx-head">
    <h1 class="lovx-title">{lov_display}</h1>
    <p class="lovx-desc">{meta["desc"]}</p>
    <p class="lovx-meta">{n} paragrafer<span class="dot">·</span>{meta["cat"]}<span class="dot">·</span>Oppdatert 2026</p>
  </header>

  <div class="lovx-search-wrap">
    <svg class="lovx-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
    <input type="text" class="lovx-search" id="lovxSearch" placeholder="Søk i {lov_display} …" autocomplete="off">
  </div>

  <div class="lovx-layout">
    <aside class="lovx-side">
      {innhold_block}
      {mest_block}
    </aside>
    <div class="lovx-main" id="lovx-list">
      {main_sections}
      <p class="lovx-empty" id="lovxEmpty">Ingen paragrafer matcher søket.</p>
    </div>
  </div>
</main>

<div class="lovx-attest">
  <p class="lovx-attest-inner">Juridisk informasjon, ikke rådgivning. Innholdet bygger på gjeldende norsk lov. Ved en konkret sak — kontakt advokat. <a href="{prefix}om/">Mer om Rettsregel &rarr;</a></p>
</div>
"""

    return head + "\n" + nav + "\n" + BODY + "\n" + SCRIPT + "\n" + footer

def render_lover_index():
    """Lover-indeks — kompakt header, søk, intent-kategorier, progressive disclosure."""

    # Map lov_slug -> (display_name, kategori_slug, beskrivelse)
    LOV_INFO = {
        # Bolig
        "husleieloven": ("Husleieloven", "bolig", "Leie av bolig og rettigheter ved leie."),
        "avhendingslova": ("Avhendingslova", "bolig", "Kjøp og salg av bolig, hytte og tomt."),
        "naboloven": ("Naboloven", "bolig", "Grenser, trær, støy og naboforhold."),
        "bustadoppforingslova": ("Bustadoppføringslova", "bolig", "Bygging av ny bolig eller hytte."),
        "tomtefesteloven": ("Tomtefesteloven", "bolig", "Leie av tomt til hus du eier — festeavgift og innløsning."),
        # Kjøp og klage
        "angrerettloven": ("Angrerettloven", "kjop-og-klage", "Angrerett ved netthandel og kjøp utenfor butikk."),
        "kjopsloven": ("Kjøpsloven", "kjop-og-klage", "Kjøp og salg — privat og bedrift."),
        "forbrukerkjopsloven": ("Forbrukerkjøpsloven", "kjop-og-klage", "Kjøp som forbruker — strengeste forbrukervern."),
        # Arbeid
        "arbeidsmiljoloven": ("Arbeidsmiljøloven", "arbeid", "Rettigheter på jobben — arbeidstid, oppsigelse, permisjon og varsling."),
        "ferieloven": ("Ferieloven", "arbeid", "Ferie, feriepenger og når du har rett til fri."),
        # Arv og familie
        "barnelova": ("Barnelova", "arv-og-familie", "Foreldreansvar, fast bosted, samvær og farskap."),
        "arveloven": ("Arveloven", "arv-og-familie", "Arv, testament og pliktdel."),
        "navneloven": ("Navneloven", "arv-og-famille", "Navnevalg og navneendring."),
        "ekteskapsloven": ("Ekteskapsloven", "arv-og-familie", "Vilkår for ekteskap, vigsling og ugyldighet."),
        # Erstatning
        "voldserstatningsloven": ("Voldserstatningsloven", "erstatning", "Erstatning fra staten ved vold og seksuallovbrudd."),
        "pasientskadeloven": ("Pasientskadeloven", "erstatning", "Erstatning ved skade i helsevesenet."),
        "yrkesskadeforsikringsloven": ("Yrkesskadeforsikringsloven", "erstatning", "Erstatning ved skade eller sykdom påført i arbeid."),
        # Økonomi og gjeld
        "inkassoloven": ("Inkassoloven", "gjeld", "Inkasso, inkassovarsel, gebyrer og dine rettigheter som skyldner."),
        "foreldelsesloven": ("Foreldelsesloven", "gjeld", "Når et krav blir foreldet — frister for gjeld og andre krav."),
        # Eiendom
        "oreigningslova": ("Oreigningslova", "eiendom", "Ekspropriasjon — når det offentlige kan ta eiendom mot erstatning."),
        "eierseksjonsloven": ("Eierseksjonsloven", "bolig", "Eierseksjoner — sameie, felleskostnader og vedtak på årsmøtet."),
        "burettslagslova": ("Burettslagslova", "bolig", "Borettslag — andeler, borett, fellesgjeld og generalforsamling."),
        # Utdanning
        "universitets-og-hoyskoleloven": ("Universitets- og høyskoleloven", "utdanning", "Rettigheter som student — eksamen, klage og utestenging."),
        # Forvaltning
        "forvaltningsloven": ("Forvaltningsloven", "forvaltning", "Dine rettigheter i møte med det offentlige — vedtak, innsyn og klage."),
    }

    # All categories — order matters. Empty ones will be excluded from nav and sections.
    KATEGORIER = [
        ("bolig", "Bolig"),
        ("eiendom", "Eiendom"),
        ("kjop-og-klage", "Kjøp og klage"),
        ("arbeid", "Arbeid"),
        ("utdanning", "Utdanning"),
        ("arv-og-familie", "Arv og familie"),
        ("erstatning", "Erstatning"),
        ("gjeld", "Gjeld"),
        ("selskap", "Selskap"),
        ("personvern", "Personvern"),
        ("okonomi-og-skatt", "Økonomi og skatt"),
        ("straff-og-politi", "Straff og politi"),
        ("forvaltning", "Forvaltning"),
        ("helse", "Helse"),
    ]

    # Count paragrafer per lov
    counts = {}
    for p in PARAGRAPHS:
        lov = p["lov"]
        counts[lov] = counts.get(lov, 0) + 1

    # Group laws by category, only including those with paragraph content
    by_kat = {}
    for slug, (display, kat, desc) in LOV_INFO.items():
        antall = counts.get(slug, 0)
        if antall == 0:
            continue
        by_kat.setdefault(kat, []).append((slug, display, desc, antall))

    total_lover = sum(len(v) for v in by_kat.values())
    total_paragrafer = sum(counts.values())
    VISIBLE = 8

    # Build category nav — only categories with content + "Alle"
    active_kategorier = [(s, t) for s, t in KATEGORIER if s in by_kat]
    nav_items = ""
    for slug, tittel in active_kategorier:
        nav_items += f'    <a href="#{slug}" class="tk-cat" data-cat="{slug}">{tittel}</a>\n'
    nav_items += '    <a href="#alle" class="tk-cat" data-cat="alle">Alle lover</a>\n'

    # Build sections
    sections = ""
    for slug, tittel in active_kategorier:
        lover_i_kat = by_kat[slug]
        collapsed_attr = ' data-collapsed' if len(lover_i_kat) > VISIBLE else ''
        rows = ""
        for i, (lov_slug, display, desc, antall) in enumerate(lover_i_kat):
            extra_cls = ' tk-row-extra' if i >= VISIBLE else ''
            meta_label = "paragraf" if antall == 1 else "paragrafer"
            search_data = f"{display.lower()} {desc.lower()}"
            rows += (
                f'      <a href="{lov_slug}/" class="tk-row tk-row-with-meta{extra_cls}" data-search="{search_data}">\n'
                f'        <span class="tk-row-name">{display}</span>\n'
                f'        <span class="tk-row-desc">{desc}</span>\n'
                f'        <span class="tk-row-meta">{antall} {meta_label}</span>\n'
                f'        <span class="tk-row-arrow" aria-hidden="true">→</span>\n'
                f'      </a>\n'
            )
        show_all = ""
        if len(lover_i_kat) > VISIBLE:
            show_all = (
                f'    <a href="#" class="tk-show-all" data-section="{slug}">'
                f'Vis alle {len(lover_i_kat)} lover i {tittel} '
                f'<span class="tk-show-all-arrow" aria-hidden="true">→</span></a>\n'
            )
        sections += (
            f'  <section class="tk-section" id="{slug}"{collapsed_attr}>\n'
            f'    <h2 class="tk-section-title">{tittel}</h2>\n'
            f'    <div class="tk-grid">\n'
            f'{rows}'
            f'    </div>\n'
            f'{show_all}'
            f'  </section>\n\n'
        )

    chat = chat_widget()

    return f"""{shared_head(
        'Lover — alle norske lover forklart på vanlig norsk | Rettsregel',
        f'{total_lover} norske lover, {total_paragrafer} paragrafer forklart på vanlig norsk. Husleieloven, arveloven, kjøpsloven og flere.',
        depth=1, canonical_path='/lover/'
    )}
{site_nav(depth=1, active='lover')}

<main class="tk-page">

  <section class="tk-hero-compact" id="alle">
    <h1>Finn loven som gjelder deg.</h1>
    <p class="tk-hero-compact-lead">Norske lover forklart på vanlig språk.</p>
  </section>

  <div class="tk-search-wrap">
    <span class="tk-search-icon" aria-hidden="true">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="21" y2="21"/></svg>
    </span>
    <input type="search" class="tk-search-input" id="tk-search" placeholder="Søk etter lov, paragraf eller situasjon …" aria-label="Søk i lover">
    <span class="tk-search-hint">Filtreres mens du skriver</span>
  </div>

  <nav class="tk-cat-bar" aria-label="Kategorier">
{nav_items}  </nav>

{sections}

</main>

{site_footer(depth=1)}

<script>
(function() {{
  document.querySelectorAll('.tk-show-all').forEach(function(link) {{
    link.addEventListener('click', function(e) {{
      e.preventDefault();
      var section = link.closest('.tk-section');
      if (section) section.removeAttribute('data-collapsed');
    }});
  }});
  var cats = document.querySelectorAll('.tk-cat');
  var sections = document.querySelectorAll('.tk-section');
  function setActive(slug) {{
    cats.forEach(function(c) {{
      if (c.getAttribute('data-cat') === slug) c.classList.add('is-active');
      else c.classList.remove('is-active');
    }});
  }}
  if ('IntersectionObserver' in window && cats.length > 0 && sections.length > 0) {{
    var observer = new IntersectionObserver(function(entries) {{
      var visible = entries.filter(function(e) {{ return e.isIntersecting; }});
      if (visible.length === 0) return;
      visible.sort(function(a, b) {{ return a.target.offsetTop - b.target.offsetTop; }});
      setActive(visible[0].target.id);
    }}, {{ rootMargin: '-20% 0px -60% 0px', threshold: 0 }});
    sections.forEach(function(s) {{ observer.observe(s); }});
  }}
  var input = document.getElementById('tk-search');
  if (!input) return;
  var allRows = Array.from(document.querySelectorAll('.tk-row'));
  var allSections = Array.from(document.querySelectorAll('.tk-section'));
  var allShowAll = Array.from(document.querySelectorAll('.tk-show-all'));
  function applyFilter() {{
    var q = input.value.trim().toLowerCase();
    if (q === '') {{
      allRows.forEach(function(r) {{ r.removeAttribute('data-hidden-by-search'); }});
      allSections.forEach(function(s) {{
        s.removeAttribute('data-hidden-by-search');
        var rows = s.querySelectorAll('.tk-row');
        if (rows.length > 8) s.setAttribute('data-collapsed', '');
      }});
      allShowAll.forEach(function(a) {{ a.style.display = ''; }});
      return;
    }}
    allSections.forEach(function(section) {{
      var rows = section.querySelectorAll('.tk-row');
      var anyVisible = false;
      rows.forEach(function(r) {{
        var hay = r.getAttribute('data-search') || '';
        if (hay.indexOf(q) === -1) r.setAttribute('data-hidden-by-search', '');
        else {{ r.removeAttribute('data-hidden-by-search'); anyVisible = true; }}
      }});
      section.removeAttribute('data-collapsed');
      if (anyVisible) section.removeAttribute('data-hidden-by-search');
      else section.setAttribute('data-hidden-by-search', '');
    }});
    allShowAll.forEach(function(a) {{ a.style.display = 'none'; }});
  }}
  input.addEventListener('input', applyFilter);
}})();
</script>

{chat}
</body>
</html>"""


def render_kontakt():
    """Egen side — kun kontaktskjema. Sender til rettsregel@gmail.com via Formspree."""
    return f"""{shared_head('Send inn sak | Rettsregel', 'Beskriv saken din, så tar vi kontakt og forteller deg hva du kan gjøre videre.', depth=1, canonical_path='/kontakt/')}
{site_nav(depth=1)}

<style>
.kt-page {{
  max-width: 540px; margin: 0 auto;
  padding: 96px 32px 104px;
}}
.kt-head {{
  text-align: center;
  margin-bottom: 48px;
}}
.kt-head h1 {{
  font-family: var(--serif);
  font-weight: 500;
  font-size: clamp(26px, 3vw, 34px);
  line-height: 1.1;
  letter-spacing: -0.022em;
  color: var(--ink);
  margin: 0 0 16px 0;
}}
.kt-head p {{
  font-family: var(--serif);
  font-size: 16px;
  line-height: 1.5;
  color: var(--ink-soft);
  margin: 0 auto;
  max-width: 380px;
}}
@media (max-width: 720px) {{
  .kt-page {{ padding: 64px 22px 80px; }}
}}
</style>

<main class="kt-page">
  <div class="kt-head">
    <h1>Send inn sak</h1>
    <p>Beskriv kort hva det gjelder. Du trenger ikke bruke juridiske ord.</p>
  </div>

  <form class="contact-form" id="kontaktskjema" action="https://formspree.io/f/mvzldpwj" method="POST">
    <div class="form-field">
      <label for="beskrivelse">Beskriv saken din</label>
      <textarea id="beskrivelse" name="beskrivelse" placeholder="Skriv kort hva det gjelder." required></textarea>
    </div>
    <div class="form-field">
      <label for="telefon">Telefonnummer</label>
      <input type="tel" id="telefon" name="telefon" placeholder="12 34 56 78" required>
    </div>
    <div class="form-field">
      <label for="epost">E-post</label>
      <input type="email" id="epost" name="epost" placeholder="navn@eksempel.no" required>
    </div>
    <button type="submit" class="form-submit">
      Send inn
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
    </button>
    <p class="form-note">Vi leser alle henvendelser. Hvis vi ikke kan hjelpe direkte, peker vi deg til noen som kan. Ved å sende godtar du vår <a href="../personvern/">personvernerklæring</a>.</p>
  </form>
  <div id="form-success" class="form-success">
    <h3>Takk!</h3>
    <p>Vi har mottatt saken din og tar kontakt så snart vi kan.</p>
  </div>
</main>

{site_footer(depth=1)}

<script>
document.getElementById('kontaktskjema').addEventListener('submit', async function(e) {{
  const form = e.target;
  e.preventDefault();
  try {{
    const res = await fetch(form.action, {{
      method: 'POST', body: new FormData(form),
      headers: {{ 'Accept': 'application/json' }}
    }});
    if (res.ok) {{
      form.classList.add('hide');
      document.getElementById('form-success').classList.add('show');
    }} else {{
      alert('Noe gikk galt. Prøv igjen, eller send oss en e-post på rettsregel@gmail.com');
    }}
  }} catch (err) {{
    console.error(err);
    alert('Noe gikk galt. Prøv igjen, eller send oss en e-post på rettsregel@gmail.com');
  }}
}});
</script>"""


def render_personvern():
    """Personvern — visuelt refinet, i stil med om-siden."""
    return f"""{shared_head('Personvern | Rettsregel', 'Personvernerklæring for Rettsregel.no — Walrus AS.', depth=1, canonical_path='/personvern/')}
{site_nav(depth=1)}

<style>
.pv-page {{
  max-width: 680px; margin: 0 auto;
  padding: 96px 32px 104px;
}}
.pv-header {{
  margin-bottom: 56px;
  padding-bottom: 40px;
  border-bottom: 1px solid var(--line);
}}
.pv-eyebrow {{
  font-family: var(--serif);
  font-size: 10.5px;
  font-weight: 500;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: var(--accent);
  margin: 0 0 22px 0;
}}
.pv-title {{
  font-family: var(--serif);
  font-weight: 500;
  font-size: clamp(26px, 3vw, 34px);
  line-height: 1.1;
  letter-spacing: -0.022em;
  color: var(--ink);
  margin: 0;
}}
.pv-body {{
  font-family: var(--serif);
  font-size: 16.5px;
  line-height: 1.7;
  color: var(--ink);
}}
.pv-body h2 {{
  font-family: var(--serif);
  font-weight: 500;
  font-size: 11px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--accent);
  margin: 52px 0 18px 0;
}}
.pv-body p {{
  margin: 0 0 18px 0;
  max-width: 600px;
}}
.pv-body p:last-child {{ margin-bottom: 0; }}
.pv-body a {{
  color: var(--accent);
  text-decoration: none;
  border-bottom: 1px solid currentColor;
  transition: color 0.15s ease;
}}
.pv-body a:hover {{ color: var(--accent-deep); }}

@media (max-width: 720px) {{
  .pv-page {{ padding: 64px 22px 80px; }}
  .pv-header {{ margin-bottom: 44px; padding-bottom: 32px; }}
  .pv-body h2 {{ margin-top: 44px; }}
}}
</style>

<main class="pv-page">
  <header class="pv-header">
    <p class="pv-eyebrow">Personvern</p>
    <h1 class="pv-title">Personvernerklæring</h1>
  </header>

  <div class="pv-body">
    <!-- TODO: legg til org.nr når klart: Walrus AS, org.nr. XXX XXX XXX -->
    <p>Rettsregel.no drives av Walrus AS. Vi behandler ikke mer data enn nødvendig, og selger aldri informasjon videre.</p>

    <h2>Hva vi samler inn</h2>
    <p>Når du sender inn kontaktskjemaet, lagrer vi navn, telefonnummer og e-postadresse. Det brukes utelukkende til å svare på henvendelsen.</p>
    <p>Nettstedet bruker ingen sporings-cookies, ingen annonsenettverk og ingen tredjeparts analyse utover det som trengs for ren drift.</p>

    <h2>Tredjeparter</h2>
    <p>Kontaktskjemaet behandles via Formspree. Deres personvernerklæring gjelder for den databehandlingen, og vi har databehandleravtale med dem.</p>

    <h2>Dine rettigheter</h2>
    <p>Du har rett til innsyn, retting og sletting av opplysningene vi har om deg. Skriv til <a href="mailto:rettsregel@gmail.com">rettsregel@gmail.com</a> for å bruke rettighetene.</p>

    <h2>Kontakt</h2>
    <p>Behandlingsansvarlig: Walrus AS · <a href="mailto:rettsregel@gmail.com">rettsregel@gmail.com</a></p>
  </div>
</main>

{site_footer(depth=1)}"""


def render_om():
    """Om-side v5 — Jony Ive minimal, site-skala."""
    chat = chat_widget()

    return f"""{shared_head(
        'Om Rettsregel',
        'Norske lover, oversatt til vanlig norsk.',
        depth=1, canonical_path='/om/'
    )}
{site_nav(depth=1, active='om')}

<style>
.om-page {{
  max-width: 680px; margin: 0 auto;
  padding: 120px 32px 128px;
  text-align: center;
}}

/* Hero — site-skala, samme som tk-hero-compact */
.om-hero h1 {{
  font-family: var(--serif);
  font-weight: 500;
  font-size: clamp(24px, 3vw, 32px);
  line-height: 1.14;
  letter-spacing: -0.024em;
  color: var(--ink);
  margin: 0 auto;
  max-width: 460px;
}}
.om-hero h1 em {{ font-style: italic; font-weight: 500; }}

/* Stille statements — descending hierarki via størrelse + farge */
.om-statements {{ margin-top: 112px; }}
.om-statement {{
  font-family: var(--serif);
  font-size: 18px;
  line-height: 1.55;
  color: var(--ink-soft);
  margin: 0 auto;
  max-width: 420px;
}}
.om-statement + .om-statement {{ margin-top: 60px; }}

/* Foten — stille kontakt */
.om-foot {{ margin-top: 112px; }}
.om-foot-rule {{
  width: 40px; height: 1px;
  background: var(--ink-mute);
  opacity: 0.4;
  margin: 0 auto 44px;
}}
.om-foot p {{
  font-family: var(--serif);
  font-size: 15px;
  line-height: 1.9;
  color: var(--ink-mute);
  margin: 0;
}}
.om-foot a {{
  color: var(--accent);
  text-decoration: none;
  border-bottom: 1px solid currentColor;
  transition: color 0.15s ease;
}}
.om-foot a:hover {{ color: var(--accent-deep); }}

@media (max-width: 720px) {{
  .om-page {{ padding: 80px 22px 88px; }}
  .om-statements {{ margin-top: 80px; }}
  .om-statement + .om-statement {{ margin-top: 48px; }}
  .om-foot {{ margin-top: 80px; }}
}}
</style>

<main class="om-page">

  <section class="om-hero">
    <h1>Norske lover, oversatt til <em>vanlig norsk</em>.</h1>
  </section>

  <div class="om-statements">
    <p class="om-statement">Loven gjelder for alle. Den er skrevet for jurister.</p>
    <p class="om-statement">Vi lager forståelig juridisk innhold — forklaringer av lover, ferdige kontrakter og maler, og svar på vanlige spørsmål.</p>
    <p class="om-statement">Alt er bygget med moderne språkteknologi og dyp tekstanalyse, som gjør tungt lovspråk om til klar norsk.</p>
  </div>

  <div class="om-foot" id="kontakt">
    <div class="om-foot-rule" aria-hidden="true"></div>
    <p>
      <a href="mailto:rettsregel@gmail.com">rettsregel@gmail.com</a><br>
      Walrus AS
    </p>
  </div>

</main>

{site_footer(depth=1)}

{chat}
</body>
</html>"""


def render_sporsmal_page(s):
    """Render en enkelt spørsmål-artikkel."""
    import markdown as md

    LOV_DISPLAY = {
        "angrerettloven": "Angrerettloven", "kjopsloven": "Kjøpsloven",
        "husleieloven": "Husleieloven", "naboloven": "Naboloven",
        "haandverkertjenesteloven": "Håndverkertjenesteloven",
        "forbrukerkjopsloven": "Forbrukerkjøpsloven",
        "plan-og-bygningsloven": "Plan- og bygningsloven",
        "husstandsfellesskapsloven": "Husstandsfellesskapsloven",
        "sameieloven": "Sameieloven", "arbeidsmiljoloven": "Arbeidsmiljøloven",
        "ferieloven": "Ferieloven", "inkassoloven": "Inkassoloven",
        "avhendingslova": "Avhendingslova", "navneloven": "Navneloven",
        "arveloven": "Arveloven",
        "tomtefesteloven": "Tomtefesteloven",
        "ekteskapsloven": "Ekteskapsloven",
    }

    KAT_LABEL = {
        "bolig": "Bolig og leie", "forbruk": "Forbruk og kjøp",
        "arbeid": "Arbeid og lønn", "familie": "Familie og samliv",
        "gjeld": "Gjeld og penger", "tjenester": "Tjenester",
        "arv": "Arv og skifte",
    }

    slug = s.get("slug", "")
    title = s.get("title", "")
    description = s.get("description", "")
    kategori = s.get("kategori", "")
    kat_label = KAT_LABEL.get(kategori, kategori.capitalize())
    content_raw = s.get("body_md") or s.get("content", "")
    kort_svar = s.get("kort_svar", "")
    related = s.get("related_paragrafer") or s.get("related", [])
    related_sp = s.get("related_sporsmal", [])
    avail_paras = {(p["lov"], p["number"]) for p in PARAGRAPHS}

    body_html = md.markdown(content_raw, extensions=["tables"]) if content_raw else ""

    # Related paragraphs
    related_html = ""
    if related:
        related_cards = []
        for r in related:
            lov = r.get("lov", "")
            paragraf = r.get("paragraf") or r.get("nummer", "")
            tittel = r.get("tittel") or r.get("beskrivelse", "")
            available = r.get("available", (lov, paragraf) in avail_paras)
            lov_display = LOV_DISPLAY.get(lov, lov)
            unavail_class = "" if available else " unavailable"
            href = f"../../lover/{lov}/{paragraf}/"
            related_cards.append(f"""<a href="{href}" class="related-card{unavail_class}">
  <div class="related-card-meta">{lov_display} § {paragraf}</div>
  <div class="related-card-title">{tittel}</div>
</a>""")
        related_html = f"""<div class="related-section">
  <div class="related-label">Relaterte paragrafer</div>
  <div class="related-cards">{"".join(related_cards)}</div>
</div>"""

    kort_svar_html = ""
    if kort_svar:
        kort_svar_html = f"""<div class="kort-svar">
  <div class="kort-svar-label">Kort svar</div>
  <p>{kort_svar}</p>
</div>"""

    related_sp_html = ""
    if related_sp:
        sp_cards = []
        for r in related_sp:
            rslug = r.get("slug", "")
            rtitle = r.get("title", "")
            sp_cards.append(f"""<a href="../../sporsmal/{rslug}/" class="related-card">
  <div class="related-card-title">{rtitle}</div>
</a>""")
        related_sp_html = f"""<div class="related-section">
  <div class="related-label">Relaterte spørsmål</div>
  <div class="related-cards">{"".join(sp_cards)}</div>
</div>"""

    return f"""{shared_head(
        f"{title} — Rettsregel",
        description,
        depth=2, canonical_path=f"/sporsmal/{slug}/"
    )}
{site_nav(depth=2)}
<main class="page">
<div class="container">
  <div class="breadcrumbs">
    <a href="../../">Rettsregel</a><span class="sep">›</span>
    <a href="../../sporsmal/">Spørsmål og svar</a><span class="sep">›</span>
    <span class="current">{kat_label}</span>
  </div>
  <article>
    <div class="article-header">
      <div class="article-eyebrow">{kat_label}</div>
      <h1 class="article-title">{title}</h1>
      <p class="article-description">{description}</p>
    </div>
    {kort_svar_html}
    <div class="article-body sp-body">
      {body_html}
    </div>
    <div class="om-takk">
      <h2>Har du en sak du lurer på?</h2>
      <p>Skriv til oss. Vi leser alle henvendelser. Hvis vi ikke kan hjelpe direkte, peker vi deg til noen som kan.</p>
      <a href="../../#skjema">Send inn saken din →</a>
    </div>
  </article>
  {related_html}
  {related_sp_html}
</div>
</main>
<div class="innhold-attest">
  <span class="innhold-attest-body"><strong>Juridisk informasjon, ikke rådgivning.</strong> Innholdet er basert på gjeldende norsk lov og gjennomgått av juridisk fagperson. Ved tvil — kontakt advokat. <a href="../../om/">Mer om Rettsregel →</a></span>
</div>
{site_footer(depth=2)}
</body>
</html>"""


def render_sporsmal_hub():
    """Spørsmål-hub — kompakt header, søk, intent-kategorier, progressive disclosure."""

    # Map current kategori -> new intent-based category
    # Bolig items also split: "nabo" in title -> nabo-og-eiendom
    KAT_MAP_BOLIG_DEFAULT = "bolig-og-leie"
    KAT_MAP = {
        "bolig": KAT_MAP_BOLIG_DEFAULT,  # split below
        "forbruk": "kjop-og-klage",
        "arbeid": "arbeid-og-oppsigelse",
        "familie": "familie-og-samliv",
        "arv": "arv-og-testament",
        "gjeld": "penger-og-gjeld",
        "tjenester": "selskap",
    }

    KATEGORIER = [
        ("bolig-og-leie", "Bolig og leie"),
        ("kjop-og-klage", "Kjøp og klage"),
        ("arbeid-og-oppsigelse", "Arbeid og oppsigelse"),
        ("familie-og-samliv", "Familie og samliv"),
        ("arv-og-testament", "Arv og testament"),
        ("penger-og-gjeld", "Penger og gjeld"),
        ("nabo-og-eiendom", "Nabo og eiendom"),
        ("bil-og-kjoretoy", "Bil og kjøretøy"),
    ]

    # Group sporsmal under new categories
    by_kat = {}
    for s in SPORSMAL:
        old_kat = s.get("kategori", "annet")
        new_kat = KAT_MAP.get(old_kat, KAT_MAP_BOLIG_DEFAULT)
        # Heuristic: bolig items with "nabo" in title -> nabo-og-eiendom
        if old_kat == "bolig" and "nabo" in s.get("title", "").lower():
            new_kat = "nabo-og-eiendom"
        by_kat.setdefault(new_kat, []).append(s)

    total = sum(len(v) for v in by_kat.values())
    VISIBLE = 8

    active_kategorier = [(s, t) for s, t in KATEGORIER if s in by_kat]
    nav_items = ""
    for slug, tittel in active_kategorier:
        nav_items += f'    <a href="#{slug}" class="tk-cat" data-cat="{slug}">{tittel}</a>\n'
    nav_items += '    <a href="#alle" class="tk-cat" data-cat="alle">Alle spørsmål</a>\n'

    sections = ""
    for slug, tittel in active_kategorier:
        items = by_kat[slug]
        collapsed_attr = ' data-collapsed' if len(items) > VISIBLE else ''
        rows = ""
        for i, s in enumerate(items):
            extra_cls = ' tk-row-extra' if i >= VISIBLE else ''
            url = s.get("slug", "")
            tittel_s = s.get("title", "")
            desc = s.get("description", "")
            search_data = f"{tittel_s.lower()} {desc.lower()}"
            rows += (
                f'      <a href="{url}/" class="tk-row{extra_cls}" data-search="{search_data}">\n'
                f'        <span class="tk-row-name">{tittel_s}</span>\n'
                f'        <span class="tk-row-desc">{desc}</span>\n'
                f'        <span class="tk-row-arrow" aria-hidden="true">→</span>\n'
                f'      </a>\n'
            )
        show_all = ""
        if len(items) > VISIBLE:
            show_all = (
                f'    <a href="#" class="tk-show-all" data-section="{slug}">'
                f'Vis alle {len(items)} spørsmål i {tittel} '
                f'<span class="tk-show-all-arrow" aria-hidden="true">→</span></a>\n'
            )
        sections += (
            f'  <section class="tk-section" id="{slug}"{collapsed_attr}>\n'
            f'    <h2 class="tk-section-title">{tittel}</h2>\n'
            f'    <div class="tk-grid">\n'
            f'{rows}'
            f'    </div>\n'
            f'{show_all}'
            f'  </section>\n\n'
        )

    chat = chat_widget()

    return f"""{shared_head(
        'Spørsmål og svar — vanlige juridiske spørsmål forklart | Rettsregel',
        f'{total} spørsmål om norsk lov, med konkrete svar. Husleie, boligkjøp, naboforhold, arbeid og mer.',
        depth=1, canonical_path='/sporsmal/'
    )}
{site_nav(depth=1, active='sporsmal')}

<main class="tk-page">

  <section class="tk-hero-compact" id="alle">
    <h1>Hva lurer du på?</h1>
    <p class="tk-hero-compact-lead">Finn svar på juridiske spørsmål.</p>
  </section>

  <div class="tk-search-wrap">
    <span class="tk-search-icon" aria-hidden="true">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="21" y2="21"/></svg>
    </span>
    <input type="search" class="tk-search-input" id="tk-search" placeholder="Søk etter spørsmål, situasjon eller tema …" aria-label="Søk i spørsmål">
    <span class="tk-search-hint">Filtreres mens du skriver</span>
  </div>

  <nav class="tk-cat-bar" aria-label="Kategorier">
{nav_items}  </nav>

{sections}

</main>

{site_footer(depth=1)}

<script>
(function() {{
  document.querySelectorAll('.tk-show-all').forEach(function(link) {{
    link.addEventListener('click', function(e) {{
      e.preventDefault();
      var section = link.closest('.tk-section');
      if (section) section.removeAttribute('data-collapsed');
    }});
  }});
  var cats = document.querySelectorAll('.tk-cat');
  var sections = document.querySelectorAll('.tk-section');
  function setActive(slug) {{
    cats.forEach(function(c) {{
      if (c.getAttribute('data-cat') === slug) c.classList.add('is-active');
      else c.classList.remove('is-active');
    }});
  }}
  if ('IntersectionObserver' in window && cats.length > 0 && sections.length > 0) {{
    var observer = new IntersectionObserver(function(entries) {{
      var visible = entries.filter(function(e) {{ return e.isIntersecting; }});
      if (visible.length === 0) return;
      visible.sort(function(a, b) {{ return a.target.offsetTop - b.target.offsetTop; }});
      setActive(visible[0].target.id);
    }}, {{ rootMargin: '-20% 0px -60% 0px', threshold: 0 }});
    sections.forEach(function(s) {{ observer.observe(s); }});
  }}
  var input = document.getElementById('tk-search');
  if (!input) return;
  var allRows = Array.from(document.querySelectorAll('.tk-row'));
  var allSections = Array.from(document.querySelectorAll('.tk-section'));
  var allShowAll = Array.from(document.querySelectorAll('.tk-show-all'));
  function applyFilter() {{
    var q = input.value.trim().toLowerCase();
    if (q === '') {{
      allRows.forEach(function(r) {{ r.removeAttribute('data-hidden-by-search'); }});
      allSections.forEach(function(s) {{
        s.removeAttribute('data-hidden-by-search');
        var rows = s.querySelectorAll('.tk-row');
        if (rows.length > 8) s.setAttribute('data-collapsed', '');
      }});
      allShowAll.forEach(function(a) {{ a.style.display = ''; }});
      return;
    }}
    allSections.forEach(function(section) {{
      var rows = section.querySelectorAll('.tk-row');
      var anyVisible = false;
      rows.forEach(function(r) {{
        var hay = r.getAttribute('data-search') || '';
        if (hay.indexOf(q) === -1) r.setAttribute('data-hidden-by-search', '');
        else {{ r.removeAttribute('data-hidden-by-search'); anyVisible = true; }}
      }});
      section.removeAttribute('data-collapsed');
      if (anyVisible) section.removeAttribute('data-hidden-by-search');
      else section.setAttribute('data-hidden-by-search', '');
    }});
    allShowAll.forEach(function(a) {{ a.style.display = 'none'; }});
  }}
  input.addEventListener('input', applyFilter);
}})();
</script>

{chat}
</body>
</html>"""


def render_homepage():
    """Forside — premium, rolig, nyttig. Egen header med søk (kun forsiden)."""
    chat = chat_widget()
    n_paragrafer = len(PARAGRAPHS)
    n_lover = len(set(p["lov"] for p in PARAGRAPHS))
    n_sporsmal = len(SPORSMAL)

    return f"""{shared_head(
        'Rettsregel — norske lover, forklart på vanlig norsk',
        'Norske lover paragraf for paragraf, verktøy og maler, og svar på vanlige juridiske spørsmål.',
        depth=0, canonical_path='/'
    )}
<style>
.hp-body {{ background: var(--bg); }}

/* ---------- Egen forside-header med søk ---------- */
.hp-header {{ border-bottom: 1px solid var(--line); background: var(--bg); }}
.hp-header-row {{
  max-width: 1200px; margin: 0 auto;
  padding: 0 40px; height: 80px;
  display: flex; align-items: center; gap: 28px;
}}
.hp-logo {{ flex: none; color: var(--ink); display: flex; align-items: center; text-decoration: none; }}
.hp-logo svg {{ display: block; }}
.hp-search {{
  flex: 1; max-width: 460px;
  position: relative; display: flex; align-items: center;
}}
.hp-search input {{
  width: 100%; height: 44px;
  padding: 0 44px 0 18px;
  border: 1px solid var(--line-strong); border-radius: 12px;
  background: var(--bg-card); color: var(--ink);
  font-family: var(--sans); font-size: 14.5px;
  transition: border-color .18s ease, box-shadow .18s ease;
}}
.hp-search input::placeholder {{ color: var(--ink-mute); }}
.hp-search input:focus {{
  outline: none; border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(192,74,38,.10);
}}
.hp-search-icon {{
  position: absolute; right: 15px; top: 50%; transform: translateY(-50%);
  color: var(--ink-mute); pointer-events: none; display: flex;
}}
.hp-search-icon svg {{ display: block; }}
.hp-nav {{ margin-left: auto; display: flex; align-items: center; gap: 30px; }}
.hp-nav a {{
  font-family: var(--sans); font-size: 14.5px; font-weight: 500;
  color: var(--ink); text-decoration: none; letter-spacing: -0.005em;
  transition: color .15s ease;
}}
.hp-nav a:hover {{ color: var(--accent); }}
.hp-nav a.hp-nav-cta {{ color: var(--accent); }}
.hp-nav a.hp-nav-cta:hover {{ color: var(--accent-deep); }}

.hp-burger-toggle, .hp-burger {{ display: none; }}

/* ---------- Container ---------- */
.hp-main {{ max-width: 1200px; margin: 0 auto; padding: 0 40px; }}

/* ---------- Hero ---------- */
.hp-hero {{
  display: grid; grid-template-columns: 1.1fr 0.9fr;
  align-items: center; gap: 40px;
  padding: 52px 0 44px;
}}
.hp-hero-title {{
  font-family: var(--serif); font-weight: 400;
  font-size: clamp(30px, 3.6vw, 46px); line-height: 1.03;
  letter-spacing: -0.035em; color: var(--ink); margin: 0;
}}
.hp-hero-title .accent {{ color: var(--accent); }}
.hp-hero-art {{ display: flex; justify-content: center; align-items: center; }}
.hp-hero-art svg {{ width: 100%; max-width: 240px; height: auto; display: block; }}

/* ---------- Stats ---------- */
.hp-stats {{
  display: grid; grid-template-columns: repeat(4, 1fr);
  border: 1px solid var(--line-strong); border-radius: 18px;
  background: var(--bg-card);
  overflow: hidden; margin-bottom: 64px;
}}
.hp-stat {{
  padding: 22px 24px; text-align: center;
  border-left: 1px solid var(--line);
}}
.hp-stat:first-child {{ border-left: none; }}
.hp-stat-num {{
  font-family: var(--serif); font-weight: 400;
  font-size: clamp(20px, 1.9vw, 26px); line-height: 1;
  color: var(--accent); letter-spacing: -0.02em;
}}
.hp-stat-label {{
  margin-top: 8px; font-family: var(--sans);
  font-size: 10.5px; font-weight: 700; letter-spacing: 0.13em;
  text-transform: uppercase; color: var(--ink-soft);
}}

/* ---------- Section heads ---------- */
.hp-sec-head {{
  display: flex; justify-content: space-between; align-items: baseline;
  margin-bottom: 8px;
}}
.hp-sec-title {{
  font-family: var(--serif); font-weight: 500;
  font-size: clamp(21px, 2.4vw, 26px); letter-spacing: -0.02em; color: var(--ink);
}}
.hp-sec-link {{
  font-family: var(--sans); font-size: 13.5px; font-weight: 600;
  color: var(--accent); text-decoration: none; white-space: nowrap;
  transition: color .15s ease;
}}
.hp-sec-link:hover {{ color: var(--accent-deep); }}

/* ---------- Two-column row ---------- */
.hp-cols {{
  display: grid; grid-template-columns: 1fr 1fr; gap: 56px;
  margin-bottom: 80px;
  align-items: stretch;
}}
.hp-col {{ display: flex; flex-direction: column; }}

/* List rows (laws + questions) */
.hp-list {{
  border-top: 1px solid var(--line); margin-top: 14px;
  flex: 1; display: flex; flex-direction: column;
}}
.hp-row {{
  display: flex; align-items: center; gap: 18px;
  padding: 17px 2px; border-bottom: 1px solid var(--line);
  text-decoration: none; color: inherit;
  flex: 1;
}}
.hp-row-body {{ flex: 1; min-width: 0; }}
.hp-row-title {{
  display: block;
  font-family: var(--serif); font-weight: 500; font-size: 17px;
  letter-spacing: -0.01em; color: var(--ink); line-height: 1.25;
}}
.hp-row-desc {{
  display: block;
  font-family: var(--sans); font-size: 13.5px; color: var(--ink-mute);
  line-height: 1.4; margin-top: 3px;
}}
.hp-row-arrow {{
  flex: none; font-family: var(--serif); font-size: 18px;
  color: var(--ink-mute); line-height: 1;
  transition: color .18s ease, transform .22s ease;
}}
.hp-row:hover .hp-row-arrow {{ color: var(--accent); transform: translateX(5px); }}
.hp-row:hover .hp-row-title {{ color: var(--accent-deep); }}
/* Compact variant for questions (no desc) */
.hp-row.compact {{ padding: 15px 2px; }}
.hp-row.compact .hp-row-title {{ font-size: 16px; font-weight: 400; }}

/* ---------- Tools grid ---------- */
.hp-tools-sec {{ margin-bottom: 72px; }}
.hp-tools {{
  display: grid; grid-template-columns: repeat(4, 1fr);
  gap: 16px; margin-top: 22px;
}}
.hp-tool {{
  display: flex; flex-direction: column;
  background: var(--bg-card); border: 1px solid var(--line);
  border-radius: 16px; padding: 20px 20px 18px;
  text-decoration: none; color: inherit; min-height: 150px;
  transition: border-color .18s ease, transform .18s ease;
}}
.hp-tool:hover {{ border-color: var(--accent-soft); transform: translateY(-2px); }}
.hp-tool-icon {{ color: var(--accent); margin-bottom: 14px; display: flex; }}
.hp-tool-icon svg {{ display: block; }}
.hp-tool-title {{
  font-family: var(--serif); font-weight: 500; font-size: 17px;
  letter-spacing: -0.01em; color: var(--ink);
}}
.hp-tool-desc {{
  font-family: var(--sans); font-size: 13px; color: var(--ink-mute);
  line-height: 1.45; margin-top: 6px; flex: 1;
}}
.hp-tool-arrow {{
  align-self: flex-end; font-family: var(--serif); font-size: 17px;
  color: var(--ink-mute); line-height: 1; margin-top: 12px;
  transition: color .18s ease, transform .22s ease;
}}
.hp-tool:hover .hp-tool-arrow {{ color: var(--accent); transform: translateX(4px); }}

/* ---------- Contact strip ---------- */
.hp-contact {{
  display: flex; align-items: center; gap: 22px;
  border: 1px solid var(--line-strong); border-radius: 20px;
  background: var(--bg-card); padding: 26px 32px;
  margin-bottom: 80px; text-decoration: none;
}}
.hp-contact-icon {{
  flex: none; width: 46px; height: 46px; border-radius: 50%;
  background: rgba(192,74,38,.10); color: var(--accent);
  display: flex; align-items: center; justify-content: center;
}}
.hp-contact-icon svg {{ display: block; }}
.hp-contact-body {{ flex: 1; }}
.hp-contact-title {{
  font-family: var(--serif); font-weight: 500; font-size: 19px;
  letter-spacing: -0.015em; color: var(--ink);
}}
.hp-contact-sub {{
  font-family: var(--sans); font-size: 14px; color: var(--ink-mute);
  margin-top: 3px; line-height: 1.4;
}}
.hp-contact-link {{
  flex: none; font-family: var(--sans); font-size: 14.5px; font-weight: 600;
  color: var(--accent); text-decoration: none; white-space: nowrap;
  transition: color .15s ease;
}}
.hp-contact:hover .hp-contact-link {{ color: var(--accent-deep); }}

/* ---------- Footer ---------- */
.hp-foot {{
  max-width: 1200px; margin: 0 auto; padding: 0 40px 44px;
}}
.hp-foot-row {{
  display: flex; justify-content: space-between; align-items: center;
  padding-top: 28px; border-top: 1px solid var(--line);
  font-family: var(--sans); font-size: 13px; color: var(--ink-mute);
}}
.hp-foot-links {{ display: flex; gap: 30px; }}
.hp-foot a {{ color: var(--ink-mute); text-decoration: none; }}
.hp-foot a:hover {{ color: var(--ink); }}

/* ---------- Responsive ---------- */
@media (max-width: 980px) {{
  .hp-tools {{ grid-template-columns: repeat(2, 1fr); }}
}}
@media (max-width: 860px) {{
  .hp-header-row {{ flex-wrap: wrap; height: auto; padding: 16px 22px; gap: 14px; }}
  .hp-nav {{ order: 3; width: 100%; margin-left: 0; gap: 20px; flex-wrap: wrap; }}
  .hp-search {{ order: 2; max-width: none; flex-basis: 100%; }}
  .hp-logo {{ order: 1; }}
  .hp-main, .hp-foot {{ padding-left: 22px; padding-right: 22px; }}
  .hp-hero {{ grid-template-columns: 1fr; gap: 8px; padding: 48px 0 40px; }}
  .hp-hero-art {{ display: none; }}
  .hp-stats {{ grid-template-columns: 1fr 1fr; }}
  .hp-stat {{ border-left: 1px solid var(--line); border-top: 1px solid var(--line); }}
  .hp-stat:first-child, .hp-stat:nth-child(2) {{ border-top: none; }}
  .hp-stat:nth-child(odd) {{ border-left: none; }}
  .hp-cols {{ grid-template-columns: 1fr; gap: 48px; }}
  .hp-foot-row {{ flex-direction: column; gap: 14px; align-items: flex-start; }}
}}
@media (max-width: 480px) {{
  .hp-tools {{ grid-template-columns: 1fr; }}
  .hp-contact {{ flex-direction: column; align-items: flex-start; gap: 14px; padding: 22px; }}
}}
</style>

{site_nav(depth=0)}

<main class="hp-main">

  <section class="hp-hero">
    <h1 class="hp-hero-title">Norsk rett,<br><span class="accent">på vanlig språk.</span></h1>
    <div class="hp-hero-art" aria-hidden="true">
      <svg viewBox="0 0 240 180" xmlns="http://www.w3.org/2000/svg">
        <circle cx="120" cy="90" r="66" fill="var(--accent)" opacity="0.12"/>
        <g fill="none" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
          <path d="M120 58 C100 46 74 45 54 51 L54 128 C74 122 100 123 120 135 C140 123 166 122 186 128 L186 51 C166 45 140 46 120 58 Z"/>
          <line x1="120" y1="58" x2="120" y2="135"/>
          <path d="M68 66 C82 63 98 64 110 70" opacity="0.45"/>
          <path d="M130 70 C142 64 158 63 172 66" opacity="0.45"/>
        </g>
      </svg>
    </div>
  </section>

  <section class="hp-stats" aria-label="Nøkkeltall">
    <div class="hp-stat"><div class="hp-stat-num">{n_sporsmal}</div><div class="hp-stat-label">Spørsmål</div></div>
    <div class="hp-stat"><div class="hp-stat-num">{n_lover}</div><div class="hp-stat-label">Lover</div></div>
    <div class="hp-stat"><div class="hp-stat-num">{n_paragrafer}</div><div class="hp-stat-label">Lovparagrafer</div></div>
    <div class="hp-stat"><div class="hp-stat-num">91</div><div class="hp-stat-label">Verktøy/maler</div></div>
  </section>

  <div class="hp-cols">

    <div class="hp-col">
      <div class="hp-sec-head">
        <h2 class="hp-sec-title">Mest brukte lover</h2>
        <a href="lover/" class="hp-sec-link">Se alle lover →</a>
      </div>
      <div class="hp-list">
        <a href="lover/husleieloven/" class="hp-row">
          <span class="hp-row-body">
            <span class="hp-row-title">Husleieloven</span>
            <span class="hp-row-desc">Regler om leie av bolig og lokale</span>
          </span>
          <span class="hp-row-arrow" aria-hidden="true">→</span>
        </a>
        <a href="lover/" class="hp-row">
          <span class="hp-row-body">
            <span class="hp-row-title">Arbeidsmiljøloven</span>
            <span class="hp-row-desc">Regler om arbeidsmiljø, arbeidstid og stillingsvern</span>
          </span>
          <span class="hp-row-arrow" aria-hidden="true">→</span>
        </a>
        <a href="lover/forbrukerkjopsloven/" class="hp-row">
          <span class="hp-row-body">
            <span class="hp-row-title">Forbrukerkjøpsloven</span>
            <span class="hp-row-desc">Regler om kjøp av varer og tjenester</span>
          </span>
          <span class="hp-row-arrow" aria-hidden="true">→</span>
        </a>
        <a href="lover/avhendingslova/" class="hp-row">
          <span class="hp-row-body">
            <span class="hp-row-title">Avhendingslova</span>
            <span class="hp-row-desc">Regler om kjøp og salg av fast eiendom</span>
          </span>
          <span class="hp-row-arrow" aria-hidden="true">→</span>
        </a>
        <a href="lover/arveloven/" class="hp-row">
          <span class="hp-row-body">
            <span class="hp-row-title">Arveloven</span>
            <span class="hp-row-desc">Regler om arv og testament</span>
          </span>
          <span class="hp-row-arrow" aria-hidden="true">→</span>
        </a>
      </div>
    </div>

    <div class="hp-col">
      <div class="hp-sec-head">
        <h2 class="hp-sec-title">Mest leste spørsmål</h2>
        <a href="sporsmal/" class="hp-sec-link">Se alle spørsmål →</a>
      </div>
      <div class="hp-list">
        <a href="sporsmal/utleier-nekter-depositum/" class="hp-row compact">
          <span class="hp-row-body"><span class="hp-row-title">Utleier nekter å gi tilbake depositumet — hva gjør du?</span></span>
          <span class="hp-row-arrow" aria-hidden="true">→</span>
        </a>
        <a href="sporsmal/" class="hp-row compact">
          <span class="hp-row-body"><span class="hp-row-title">Kan arbeidsgiver kreve at du jobber overtid?</span></span>
          <span class="hp-row-arrow" aria-hidden="true">→</span>
        </a>
        <a href="sporsmal/" class="hp-row compact">
          <span class="hp-row-body"><span class="hp-row-title">Hva har du krav på ved oppsigelse?</span></span>
          <span class="hp-row-arrow" aria-hidden="true">→</span>
        </a>
        <a href="sporsmal/" class="hp-row compact">
          <span class="hp-row-body"><span class="hp-row-title">Kan utleier kreve penger for vanlig slitasje?</span></span>
          <span class="hp-row-arrow" aria-hidden="true">→</span>
        </a>
        <a href="sporsmal/" class="hp-row compact">
          <span class="hp-row-body"><span class="hp-row-title">Hvor lang tid tar Husleietvistutvalget?</span></span>
          <span class="hp-row-arrow" aria-hidden="true">→</span>
        </a>
      </div>
    </div>

  </div>

  <section class="hp-tools-sec">
    <div class="hp-sec-head">
      <h2 class="hp-sec-title">Mest brukte verktøy og maler</h2>
      <a href="tjenester/" class="hp-sec-link">Se alle verktøy og maler →</a>
    </div>
    <div class="hp-tools">
      {hp_tool('kontrakter/husleiekontrakt/', 'home', 'Husleiekontrakt', 'Leieavtale for bolig — klar til å fylle ut')}
      {hp_tool('tjenester/arbeid-oppsigelse/', 'log-out', 'Oppsigelse av jobb', 'Mal for å si opp arbeidsforholdet ditt')}
      {hp_tool('tjenester/inkasso/', 'mail', 'Kravbrev', 'Krev betaling for noe noen skylder deg')}
      {hp_tool('tjenester/reklamasjon/', 'message', 'Reklamasjon', 'Klage på vare eller tjeneste med mangel')}
      {hp_tool('kontrakter/arbeidsavtale/', 'briefcase', 'Arbeidsavtale', 'Avtale mellom arbeidsgiver og arbeidstaker')}
      {hp_tool('tjenester/testament-mal/', 'feather', 'Testament', 'Bestem hvordan arven din skal fordeles')}
      {hp_tool('kontrakter/samboeravtale/', 'users', 'Samboeravtale', 'Avklar økonomi og eiendeler som samboere')}
      {hp_tool('kontrakter/fremtidsfullmakt/', 'shield', 'Fremtidsfullmakt', 'Bestem hvem som styrer for deg senere i livet')}
    </div>
  </section>

</main>

<footer class="hp-foot">
  <div class="hp-foot-row">
    <span>© Walrus AS</span>
    <div class="hp-foot-links">
      <a href="om/">Om</a>
      <a href="personvern/">Personvern</a>
      <a href="kontakt/">Kontakt</a>
    </div>
  </div>
</footer>

{chat}
</body>
</html>"""


def hp_tool(href, icon, title, desc):
    """En verktøy-kort på forsiden."""
    icons = {
        'home': '<path d="M3 10.5L12 3l9 7.5"/><path d="M5 9.5V20a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V9.5"/><path d="M9.5 21v-6h5v6"/>',
        'log-out': '<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/>',
        'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
        'message': '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>',
        'briefcase': '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
        'feather': '<path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"/><line x1="16" y1="8" x2="2" y2="22"/><line x1="17.5" y1="15" x2="9" y2="15"/>',
        'users': '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
        'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
        'file-text': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="14" y2="17"/>',
    }
    path = icons.get(icon, icons['file-text'])
    return f"""<a href="{href}" class="hp-tool">
        <span class="hp-tool-icon" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{path}</svg></span>
        <span class="hp-tool-title">{title}</span>
        <span class="hp-tool-desc">{desc}</span>
        <span class="hp-tool-arrow" aria-hidden="true">→</span>
      </a>"""


def render_tjenester_hub():
    """Verktøy/maler — funksjonell indeks med søk og progressive disclosure."""

    # Intent-based kategorier (slug, tittel, [(url, navn, beskrivelse), ...])
    # Order within each: most useful/most common first (first 8 shown by default)
    KATEGORIER = [
        ("klage-og-krav", "Klage og krav", [
            ("../tjenester/reklamasjon/", "Reklamasjonsbrev", "Klage med riktige lovhenvisninger."),
            ("../tjenester/heving/", "Heving av kjøp", "Få pengene tilbake ved vesentlig feil."),
            ("../tjenester/prisavslag/", "Prisavslag", "Hvor mye kan du kreve i avslag?"),
            ("../tjenester/mangel/", "Mangel-sjekker", "Er feilen juridisk mangel — eller bare slitasje?"),
            ("../tjenester/angreskjema/", "Angrerettskjema", "EU-standardskjema, klart til utfylling."),
            ("../tjenester/inkasso/", "Inkasso-sjekk", "Er kravet lovlig? Foreldelse og gebyrer."),
            ("../tjenester/forsikringsavslag/", "Forsikringsavslag", "Grunnlag for klage? Finansklagenemnda."),
            ("../tjenester/handverker-reklamasjon/", "Håndverker-reklamasjon", "Brev ved dårlig håndverkertjeneste."),
            # Extras
            ("../tjenester/reklamasjon-bil/", "Reklamasjon bil", "Brev ved feil på bilen du kjøpte."),
            ("../tjenester/kredittkjop/", "Kredittkjøp-sjekker", "Er banken medansvarlig når selger svikter?"),
            ("../tjenester/klagefrist/", "Klagefrist forvaltning", "3 uker etter vedtak. Utløpt?"),
            ("../tjenester/pakkereis/", "Pakkereise-kalkulator", "250–600 EUR ved forsinkelse. EU 261/2004."),
            ("../tjenester/gdpr-innsyn/", "GDPR-innsynskrav", "Be selskaper om å vise dine data."),
            ("../kontrakter/misligholdsvarsel/", "Misligholdsvarsel", "Siste varsel før inkasso."),
        ]),
        ("arbeid-og-oppsigelse", "Arbeid og oppsigelse", [
            ("../tjenester/arbeid-oppsigelse/", "Oppsigelsestid", "Lovlig varsel basert på ansettelsestid og alder."),
            ("../tjenester/usaklig-oppsigelse/", "Usaklig oppsigelse", "Saklig grunn, saksbehandling, sykevern."),
            ("../tjenester/arbeidskontrakt/", "Arbeidskontrakt-sjekker", "Alle lovpålagte minimumsopplysninger?"),
            ("../kontrakter/arbeidsavtale/", "Arbeidsavtale", "Fast ansettelse — alle aml. § 14-6-krav."),
            ("../tjenester/sykmelding-vern/", "Sykmelding-vern", "Er du vernet de første 12 månedene?"),
            ("../tjenester/permittering/", "Permittering-sjekker", "Lovlig varsel og arbeidsgiverperiode?"),
            ("../tjenester/konkurranse-klausul/", "Konkurranse-/kundeklausul", "Gyldig? Kompensasjon og maksvarighet."),
            ("../kontrakter/sluttavtale/", "Sluttavtale", "Frivillig avslutning av arbeidsforhold."),
            # Extras
            ("../kontrakter/arbeidsavtale-deltid/", "Arbeidsavtale (deltid)", "Stillingsprosent og fortrinnsrett."),
            ("../kontrakter/arbeidsavtale-midlertidig/", "Arbeidsavtale (midlertidig)", "Vikariat, prosjekt og sesong."),
            ("../kontrakter/taushetserklaring/", "Taushetserklæring (NDA)", "For ansatte, konsulenter, samarbeidspartnere."),
            ("../kontrakter/arbeidsattest/", "Arbeidsattest", "Alle ansatte har rett på attest. Aml. § 15-15."),
        ]),
        ("bolig-og-leie", "Bolig og leie", [
            ("../kontrakter/husleiekontrakt/", "Husleiekontrakt", "Tidsubestemt eller tidsbestemt."),
            ("../tjenester/depositum-tilbake/", "Depositum tilbake", "Depositum og renter du har krav på."),
            ("../tjenester/husleie-oppsigelse/", "Oppsigelsestid leie", "Lovlig oppsigelsestid for utleier og leietaker."),
            ("../tjenester/leie-okning/", "Leieøkning", "Maks lovlig økning etter KPI, med varselbrev."),
            ("../tjenester/vedlikehold/", "Vedlikeholdsansvar", "Utleier eller leietaker — hvem fikser hva?"),
            ("../tjenester/boligkjoper-sjekkliste/", "Boligkjøper-sjekkliste", "8 punkter — ivareta undersøkelsesplikten."),
            ("../tjenester/vesentlig-mangel-bolig/", "Vesentlig mangel bolig", "Over Høyesteretts 3–6 %-terskel?"),
            ("../tjenester/selger-opplysningsplikt/", "Selgers opplysningsplikt", "Holdt selger tilbake info? §§ 3-7 og 3-8."),
            # Extras
            ("../kontrakter/fremleiekontrakt/", "Fremleiekontrakt", "Fremleie hele eller deler av boligen din."),
            ("../tjenester/fremleie/", "Fremleie-sjekker", "Kan du fremleie? Kan utleier nekte?"),
            ("../kontrakter/depositumavtale/", "Depositumavtale", "Sperret konto, maks 6 mnd. Husleieloven § 3-5."),
            ("../tjenester/prisavslag-bolig/", "Prisavslag bolig", "Beregn krav basert på utbedringskostnad."),
            ("../kontrakter/overtakelsesprotokoll/", "Overtakelsesprotokoll", "Målere, nøkler, feil. Avgjørende dokumentasjon."),
            ("../kontrakter/nabovarsel/", "Nabovarsel", "Påkrevd før byggesøknad. 2 ukers merknadsfrist."),
            ("../kontrakter/kjopekontrakthytte/", "Kjøpekontrakt hytte", "Fritidseiendom og tomt."),
            ("../kontrakter/leiekontrakt-naring/", "Leiekontrakt næring", "Kontor, butikk, lager. KPI-regulering."),
            ("../kontrakter/sameieandel/", "Sameieerklæring", "Hvem eier hva? Dokumentér sameieandeler."),
        ]),
        ("avtaler-og-fullmakter", "Avtaler og fullmakter", [
            ("../tjenester/fullmakt-mal/", "Fullmakt-mal", "Fullmakt for Nav, bank, eiendom."),
            ("../kontrakter/kjopekontraktbil/", "Kjøpekontrakt bil", "Privatbilsalg, basert på kjøpsloven."),
            ("../kontrakter/kvittering/", "Kvittering", "Kontantbetaling, depositum og håndverk."),
            ("../kontrakter/gjeldsbrev/", "Gjeldsbrev", "Privatlån mellom venner og familie."),
            ("../kontrakter/kausjonsavtale/", "Kausjonsavtale", "Simpel eller selvskyldnerkausjon."),
            ("../kontrakter/betalingsplan/", "Betalingsplan", "Nedbetaling av gjeld i avdrag."),
            ("../kontrakter/konsulentavtale/", "Konsulentavtale", "For frilansere og selvstendige konsulenter."),
            ("../kontrakter/aksjonaravtale2/", "Aksjonæravtale", "Forkjøpsrett, tag-along, utbytte, exit."),
            # Extras
            ("../kontrakter/kjopekontraktbat/", "Kjøpekontrakt båt", "Privat båtsalg med tilstandsklausul."),
            ("../kontrakter/kjopekontraktgjenstand/", "Kjøpekontrakt eiendeler", "Finn.no-kjøp: møbler, elektronikk, mer."),
            ("../kontrakter/panteavtale/", "Panteavtale", "Sikre lån med pant i bil eller løsøre."),
            ("../kontrakter/bruksrettsavtale/", "Bruksrettsavtale", "Gi rett til å bruke noe uten å overdra eierskap."),
            ("../kontrakter/stiftelsesdokument/", "Stiftelsesdokument AS", "Stift AS med vedtekter."),
            ("../kontrakter/aksjekjopekontrakt/", "Aksjekjøpekontrakt", "Overdragelse av aksjer med garantier."),
            ("../kontrakter/opsjonsavtale/", "Opsjonsavtale ansatte", "Vesting-periode og innløsningspris."),
            ("../kontrakter/styreprotokoll/", "Styreprotokoll", "Protokollér styremøtet riktig. Asl. § 6-29."),
            ("../kontrakter/generalforsamlingsprotokoll/", "GF-protokoll", "Protokollér GF riktig. Asl. § 5-16."),
            ("../kontrakter/leverandoravtale/", "Leverandøravtale", "Kjøp av varer og tjenester over tid."),
            ("../kontrakter/samarbeidsavtale/", "Samarbeidsavtale", "Strategisk samarbeid mellom virksomheter."),
            ("../kontrakter/overdragelsesavtale/", "Overdragelsesavtale", "Salg av virksomhet. Goodwill, kunder, inventar."),
            ("../kontrakter/tjenesteavtale/", "Tjenesteavtale", "For malere, vaskehjelp, håndverkere."),
            ("../kontrakter/consignmentavtale/", "Consignmentavtale", "Selg kunst eller varer på vegne av en annen."),
        ]),
        ("arv-og-testament", "Arv og testament", [
            ("../tjenester/arv/", "Arvefordeling", "Visuell oversikt basert på familiesituasjonen."),
            ("../tjenester/testament-mal/", "Testament-mal", "Generer testament-utkast med vitnefelt."),
            ("../tjenester/pliktdel/", "Pliktdel", "Hva kan du testamentere bort? 2/3-regelen."),
            ("../tjenester/uskifte/", "Uskifte-sjekker", "Kan gjenlevende sitte i uskifte?"),
            ("../tjenester/samboer-arverett/", "Samboer-arverett", "Arver samboeren din uten testament?"),
            ("../kontrakter/fremtidsfullmakt/", "Fremtidsfullmakt", "Hvem ivaretar deg ved sviktende helse."),
            ("../kontrakter/samboeravtale/", "Samboeravtale", "Hvem eier hva ved brudd?"),
            ("../kontrakter/ektepakt/", "Ektepakt (særeie)", "Gjør formue til særeie."),
            # Extras
            ("../tjenester/arvegjeld/", "Arvegjeld-sjekker", "Overtar du avdødes gjeld?"),
            ("../kontrakter/gavebrev/", "Gavebrev", "Med særeie-klausul og arveforskudd."),
            ("../kontrakter/ektepakt-felleseie/", "Ektepakt (arv som særeie)", "Felleseie, men arv og gaver beskyttes."),
            ("../kontrakter/samvaersavtale/", "Samværsavtale", "Barnets hverdag etter samlivsbrudd."),
            ("../kontrakter/skifteavtale/", "Skifteavtale", "Bolig, bil, gjeld ved samlivsbrudd."),
        ]),
        ("frister-og-kalkulatorer", "Frister og kalkulatorer", [
            ("../tjenester/reklamasjonsfrist/", "Reklamasjonsfrist", "Har du fortsatt rett til å klage?"),
            ("../tjenester/angrefrist/", "Angrefrist", "Har du fortsatt rett til å angre kjøpet?"),
            ("../tjenester/feriepenger/", "Feriepenger-kalkulator", "Standard, tariff og over 60."),
            ("../tjenester/overtid/", "Overtid-kalkulator", "Beregn overtid med lovpålagt tillegg."),
            ("../tjenester/depositum/", "Depositum-kalkulator", "Maks lovlig depositum basert på månedsleien."),
            ("../tjenester/enk-eller-as/", "ENK eller AS?", "Optimal selskapsform med skatteillustrasjon."),
            ("../tjenester/utbytte-skatt/", "Utbytte-skatt", "Effektiv sats 37,84 %. Netto utbytte."),
            ("../tjenester/omdanning-enk-as/", "Omdanning ENK→AS", "Er det lønnsomt? Skattesammenligning."),
            # Extras
            ("../tjenester/reklamasjonsfrist-bolig/", "Reklamasjonsfrist bolig", "5-årsregel og 2-månedersfrist."),
            ("../tjenester/dagmulkt/", "Dagmulkt", "Dagmulkt ved forsinket boligovertakelse."),
            ("../tjenester/styreansvar/", "Styreansvar-sjekker", "Personlig ansvar? Handleplikt og insolvens."),
            ("../tjenester/aksjekapital/", "Aksjekapital-sjekker", "Handleplikt og utbytteregler."),
            ("../tjenester/aksjonaravtale/", "Aksjonæravtale-sjekker", "10-punkts sjekkliste."),
        ]),
    ]

    total = sum(len(verktoy) for _, _, verktoy in KATEGORIER)
    VISIBLE_BY_DEFAULT = 8

    # Build category nav
    nav_items = ""
    for slug, tittel, _ in KATEGORIER:
        nav_items += f'    <a href="#{slug}" class="tk-cat" data-cat="{slug}">{tittel}</a>\n'
    nav_items += '    <a href="#alle" class="tk-cat" data-cat="alle">Alle</a>\n'

    # Build sections
    sections = ""
    for slug, tittel, verktoy in KATEGORIER:
        collapsed_attr = ' data-collapsed' if len(verktoy) > VISIBLE_BY_DEFAULT else ''
        rows = ""
        for i, (url, navn, beskr) in enumerate(verktoy):
            extra_cls = ' tk-row-extra' if i >= VISIBLE_BY_DEFAULT else ''
            search_data = f"{navn.lower()} {beskr.lower()}"
            rows += (
                f'      <a href="{url}" class="tk-row{extra_cls}" data-search="{search_data}">\n'
                f'        <span class="tk-row-name">{navn}</span>\n'
                f'        <span class="tk-row-desc">{beskr}</span>\n'
                f'        <span class="tk-row-arrow" aria-hidden="true">→</span>\n'
                f'      </a>\n'
            )
        show_all = ""
        if len(verktoy) > VISIBLE_BY_DEFAULT:
            show_all = (
                f'    <a href="#" class="tk-show-all" data-section="{slug}">'
                f'Vis alle {len(verktoy)} i {tittel} '
                f'<span class="tk-show-all-arrow" aria-hidden="true">→</span></a>\n'
            )
        sections += (
            f'  <section class="tk-section" id="{slug}"{collapsed_attr}>\n'
            f'    <h2 class="tk-section-title">{tittel}</h2>\n'
            f'    <div class="tk-grid">\n'
            f'{rows}'
            f'    </div>\n'
            f'{show_all}'
            f'  </section>\n\n'
        )

    chat = chat_widget()

    return f"""{shared_head(
        'Verktøy og maler — juridiske dokumenter, kontrakter og kalkulatorer | Rettsregel',
        f'{total} ferdige juridiske verktøy, kontrakter, brev og kalkulatorer — basert på norsk rett. Klar til bruk, gratis.',
        depth=1, canonical_path='/tjenester/'
    )}
{site_nav(depth=1, active='tjenester')}

<main class="tk-page">

  <section class="tk-hero-compact" id="alle">
    <h1>Hva skal du lage?</h1>
    <p class="tk-hero-compact-lead">Kontrakter, brev, skjemaer og sjekker — klare til bruk.</p>
  </section>

  <div class="tk-search-wrap">
    <span class="tk-search-icon" aria-hidden="true">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="21" y2="21"/></svg>
    </span>
    <input type="search" class="tk-search-input" id="tk-search" placeholder="Søk etter dokument, brev eller situasjon …" aria-label="Søk i verktøy">
    <span class="tk-search-hint">Filtreres mens du skriver</span>
  </div>

  <nav class="tk-cat-bar" aria-label="Kategorier">
{nav_items}  </nav>

{sections}

</main>

{site_footer(depth=1)}

<script>
(function() {{
  // Progressive disclosure
  document.querySelectorAll('.tk-show-all').forEach(function(link) {{
    link.addEventListener('click', function(e) {{
      e.preventDefault();
      var section = link.closest('.tk-section');
      if (section) section.removeAttribute('data-collapsed');
    }});
  }});

  // Scrollspy
  var cats = document.querySelectorAll('.tk-cat');
  var sections = document.querySelectorAll('.tk-section');
  function setActive(slug) {{
    cats.forEach(function(c) {{
      if (c.getAttribute('data-cat') === slug) c.classList.add('is-active');
      else c.classList.remove('is-active');
    }});
  }}
  if ('IntersectionObserver' in window && cats.length > 0 && sections.length > 0) {{
    var observer = new IntersectionObserver(function(entries) {{
      var visible = entries.filter(function(e) {{ return e.isIntersecting; }});
      if (visible.length === 0) return;
      visible.sort(function(a, b) {{ return a.target.offsetTop - b.target.offsetTop; }});
      setActive(visible[0].target.id);
    }}, {{ rootMargin: '-20% 0px -60% 0px', threshold: 0 }});
    sections.forEach(function(s) {{ observer.observe(s); }});
  }}

  // Search
  var input = document.getElementById('tk-search');
  if (!input) return;
  var allRows = Array.from(document.querySelectorAll('.tk-row'));
  var allSections = Array.from(document.querySelectorAll('.tk-section'));
  var allShowAll = Array.from(document.querySelectorAll('.tk-show-all'));

  function applyFilter() {{
    var q = input.value.trim().toLowerCase();
    if (q === '') {{
      // Reset to default view
      allRows.forEach(function(r) {{ r.removeAttribute('data-hidden-by-search'); }});
      allSections.forEach(function(s) {{
        s.removeAttribute('data-hidden-by-search');
        // Restore collapsed state if it had >8 rows
        var rows = s.querySelectorAll('.tk-row');
        if (rows.length > 8) s.setAttribute('data-collapsed', '');
      }});
      allShowAll.forEach(function(a) {{ a.style.display = ''; }});
      return;
    }}
    // Filter rows
    allSections.forEach(function(section) {{
      var rows = section.querySelectorAll('.tk-row');
      var anyVisible = false;
      rows.forEach(function(r) {{
        var hay = r.getAttribute('data-search') || '';
        if (hay.indexOf(q) === -1) {{
          r.setAttribute('data-hidden-by-search', '');
        }} else {{
          r.removeAttribute('data-hidden-by-search');
          anyVisible = true;
        }}
      }});
      // Expand section (show all rows) during search
      section.removeAttribute('data-collapsed');
      if (anyVisible) section.removeAttribute('data-hidden-by-search');
      else section.setAttribute('data-hidden-by-search', '');
    }});
    // Hide show-all links during search
    allShowAll.forEach(function(a) {{ a.style.display = 'none'; }});
  }}
  input.addEventListener('input', applyFilter);
}})();
</script>

{chat}
</body>
</html>"""


def render_enk_eller_as():
    return f"""{shared_head(
        'ENK eller AS? Finn ut hva som passer for deg — Rettsregel',
        'Fyll ut skjemaet og få en selskapsrettslig anbefaling med skatteillustrasjon — gratis.',
        depth=2, canonical_path='/tjenester/enk-eller-as/'
    )}
{site_nav(depth=2)}

<style>
.enk-layout {{
  display: grid; grid-template-columns: 380px 1fr; gap: 32px;
  align-items: start; margin-bottom: 64px;
}}
@media (max-width: 1024px) {{ .enk-layout {{ grid-template-columns: 1fr; }} }}
.enk-layout > * {{ min-width: 0; }}
.enk-skjema {{
  background: var(--bg-card); border: 1px solid var(--line);
  border-radius: 20px; padding: 28px; box-shadow: var(--shadow-md);
  position: sticky; top: 24px;
}}
@media (max-width: 1024px) {{ .enk-skjema {{ position: static; }} }}
.es-tittel {{ font-family: var(--serif); font-size: 18px; font-weight: 400; margin-bottom: 20px; }}
.es-sek {{ margin-bottom: 18px; border-bottom: 1px solid var(--line); padding-bottom: 18px; }}
.es-sek:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
.es-sek-tittel {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); margin-bottom: 10px; }}
.ef {{ margin-bottom: 10px; }}
.ef label {{ display: block; font-size: 12px; font-weight: 600; color: var(--ink-soft); margin-bottom: 4px; }}
.ef input[type=number] {{
  width: 100%; padding: 9px 12px; border: 1.5px solid var(--line);
  border-radius: 8px; font-family: var(--sans); font-size: 16px;
  background: var(--bg); color: var(--ink); box-sizing: border-box; transition: border-color 0.15s;
}}
.ef input:focus {{ outline: none; border-color: var(--accent); }}
.ef-radio {{ display: flex; flex-direction: column; gap: 6px; margin-top: 4px; }}
.ef-radio label {{
  display: flex; align-items: center; gap: 8px; font-size: 13px;
  font-weight: 500; color: var(--ink); cursor: pointer; padding: 8px 12px;
  border: 1.5px solid var(--line); border-radius: 8px; line-height: 1.35;
}}
.ef-radio input[type=radio] {{ width: auto; margin: 0; accent-color: var(--accent); flex-shrink: 0; }}
.ef-radio label:has(input:checked) {{ border-color: var(--accent); background: rgba(177,74,42,0.05); color: var(--accent); font-weight: 600; }}
/* Resultat */
.enk-res {{ display: flex; flex-direction: column; gap: 20px; }}
.enk-vurdering {{
  border-radius: 14px; padding: 20px 24px;
  display: none; border: 1.5px solid var(--line);
}}
.enk-vurdering.as {{ background: #e2edf4; border-color: #8dbcd4; }}
.enk-vurdering.enk {{ background: #e8f4e8; border-color: #8dcc8d; }}
.enk-vurdering.as-krav {{ background: #dce8f2; border-color: #6aacd0; }}
.ev-badge {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 10px; display: block; }}
.ev-tittel {{ font-family: var(--serif); font-size: 22px; font-weight: 400; margin-bottom: 14px; line-height: 1.2; }}
.ev-grunner {{ margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 8px; }}
.ev-grunner li {{ display: flex; gap: 8px; font-size: 14px; line-height: 1.5; }}
.ev-grunner li::before {{ content: '→'; color: var(--accent); font-weight: 700; flex-shrink: 0; }}
/* Skatt */
.enk-skatt {{ background: var(--bg-alt); border-radius: 14px; padding: 20px 24px; border: 1px solid var(--line); display: none; }}
.enk-skatt h4 {{ font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--ink-mute); margin-bottom: 14px; }}
.skatt-g {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
@media (max-width: 600px) {{ .skatt-g {{ grid-template-columns: 1fr; }} }}
.sk {{ background: white; border-radius: 10px; padding: 14px; border: 1px solid var(--line); }}
.sk-lov {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--ink-mute); margin-bottom: 8px; }}
.sk-r {{ display: flex; justify-content: space-between; font-size: 13px; padding: 4px 0; border-bottom: 1px solid rgba(0,0,0,0.06); }}
.sk-r:last-child {{ border-bottom: none; }}
.sk-r.tot {{ font-weight: 700; font-size: 14px; padding-top: 6px; border-top: 2px solid var(--line); border-bottom: none; }}
.sk-r.igjen {{ color: var(--accent); font-weight: 700; font-size: 14px; }}
.skatt-note {{ font-size: 12px; color: var(--ink-mute); margin-top: 10px; line-height: 1.5; }}
/* Tabell */
.enk-tbl-wrap {{ overflow-x: auto; display: none; }}
.enk-tbl {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
.enk-tbl th {{ padding: 9px 12px; text-align: left; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; background: var(--bg-alt); border-bottom: 2px solid var(--line); }}
.enk-tbl td {{ padding: 10px 12px; border-bottom: 1px solid var(--line); vertical-align: top; line-height: 1.4; }}
.enk-tbl tr:last-child td {{ border-bottom: none; }}
.enk-tbl td:first-child {{ color: var(--ink-mute); font-size: 12px; font-weight: 600; white-space: nowrap; }}
.enk-tbl th.anbefalt, .enk-tbl td.anbefalt {{ background: rgba(177,74,42,0.04); color: var(--accent); font-weight: 600; }}
/* CTA */
.enk-cta {{ background: var(--bg-alt); border-radius: 16px; padding: 28px; }}
.enk-cta h3 {{ font-family: var(--serif); font-size: 20px; font-weight: 400; margin-bottom: 10px; }}
.enk-cta p {{ font-size: 14px; color: var(--ink-soft); line-height: 1.55; margin-bottom: 14px; max-width: 520px; }}
.btn-aksjon {{ display: inline-flex; align-items: center; gap: 8px; background: var(--accent); color: white; text-decoration: none; font-weight: 600; font-size: 14px; padding: 12px 20px; border-radius: 10px; transition: background 0.2s; }}
.btn-aksjon:hover {{ background: var(--accent-deep); }}
.enk-cta-pris {{ font-size: 12px; color: var(--ink-mute); display: block; margin-top: 8px; }}
</style>

<main class="page">
  <div class="container">
    <div class="breadcrumbs no-print">
      <a href="../../">Rettsregel</a><span class="sep">›</span>
      <a href="../../tjenester/">Tjenester</a><span class="sep">›</span>
      <span class="current">ENK eller AS?</span>
    </div>
    <div class="article-header no-print">
      <div class="article-eyebrow">Gratis verktøy</div>
      <h1 class="article-title">Skal du velge ENK eller AS?</h1>
      <p class="article-description">Fyll ut feltene til venstre. Anbefalingen oppdateres live basert på svarene dine.</p>
    </div>

    <div class="enk-layout">
      <!-- SKJEMA -->
      <div class="enk-skjema no-print">
        <div class="es-tittel">Fortell om virksomheten</div>

        <div class="es-sek">
          <div class="es-sek-tittel">Eiere</div>
          <div class="ef">
            <div class="ef-radio">
              <label><input type="radio" name="eiere" value="en" onchange="oppdater()"> Bare meg — én eier</label>
              <label><input type="radio" name="eiere" value="flere" onchange="oppdater()"> Vi er to eller flere eiere</label>
            </div>
          </div>
        </div>

        <div class="es-sek">
          <div class="es-sek-tittel">Økonomi</div>
          <div class="ef">
            <label for="overskudd">Forventet overskudd år 1 (kr)</label>
            <input type="number" id="overskudd" placeholder="f.eks. 400000" min="0" step="10000" oninput="oppdater()">
          </div>
          <div class="ef" style="margin-top:12px">
            <div style="font-size:12px;font-weight:600;color:var(--ink-soft);margin-bottom:6px">Hva vil du gjøre med overskuddet?</div>
            <div class="ef-radio">
              <label><input type="radio" name="kapital" value="ta_ut" onchange="oppdater()"> Ta ut fortløpende — dette er inntekten min</label>
              <label><input type="radio" name="kapital" value="beholde" onchange="oppdater()"> La det stå og vokse i selskapet</label>
              <label><input type="radio" name="kapital" value="blanding" onchange="oppdater()"> Blanding</label>
            </div>
          </div>
        </div>

        <div class="es-sek">
          <div class="es-sek-tittel">Virksomhet og risiko</div>
          <div class="ef">
            <div class="ef-radio">
              <label><input type="radio" name="bransje" value="konsulent" onchange="oppdater()"> Rådgivning / konsulent / IT</label>
              <label><input type="radio" name="bransje" value="haandverk" onchange="oppdater()"> Bygg, håndverk, transport</label>
              <label><input type="radio" name="bransje" value="handel" onchange="oppdater()"> Handel, nettbutikk</label>
              <label><input type="radio" name="bransje" value="helse" onchange="oppdater()"> Helse, omsorg, terapi</label>
              <label><input type="radio" name="bransje" value="kreativ" onchange="oppdater()"> Kreativt, kultur, media</label>
              <label><input type="radio" name="bransje" value="annet" onchange="oppdater()"> Annet / usikker</label>
            </div>
          </div>
        </div>

        <div class="es-sek">
          <div class="es-sek-tittel">Investorer og kapital</div>
          <div class="ef">
            <div style="font-size:12px;font-weight:600;color:var(--ink-soft);margin-bottom:6px">Planlegger du å hente investorer?</div>
            <div class="ef-radio">
              <label><input type="radio" name="investorer" value="ja" onchange="oppdater()"> Ja</label>
              <label><input type="radio" name="investorer" value="nei" onchange="oppdater()"> Nei</label>
            </div>
          </div>
          <div class="ef" style="margin-top:12px">
            <div style="font-size:12px;font-weight:600;color:var(--ink-soft);margin-bottom:6px">Har du 30 000 kr til aksjekapital? <span style="font-weight:400;color:var(--ink-mute)">(aksjeloven § 3-1)</span></div>
            <div class="ef-radio">
              <label><input type="radio" name="har30k" value="ja" onchange="oppdater()"> Ja</label>
              <label><input type="radio" name="har30k" value="nei" onchange="oppdater()"> Ikke akkurat nå</label>
            </div>
          </div>
        </div>

        <div class="es-sek">
          <div class="es-sek-tittel">Sosiale rettigheter</div>
          <div class="ef">
            <div style="font-size:12px;font-weight:600;color:var(--ink-soft);margin-bottom:6px">Viktig med sykepenger fra dag 1?</div>
            <div class="ef-radio">
              <label><input type="radio" name="sykepenger" value="ja" onchange="oppdater()"> Ja — kritisk for meg</label>
              <label><input type="radio" name="sykepenger" value="nei" onchange="oppdater()"> Nei — tåler to uker uten</label>
            </div>
          </div>
          <div class="ef" style="margin-top:12px">
            <div style="font-size:12px;font-weight:600;color:var(--ink-soft);margin-bottom:6px">Vil du ansette noen?</div>
            <div class="ef-radio">
              <label><input type="radio" name="ansette" value="ja" onchange="oppdater()"> Ja</label>
              <label><input type="radio" name="ansette" value="nei" onchange="oppdater()"> Nei — solo foreløpig</label>
            </div>
          </div>
        </div>
      </div>

      <!-- RESULTAT -->
      <div class="enk-res">
        <div id="enk-vurdering" class="enk-vurdering">
          <span class="ev-badge" id="ev-badge"></span>
          <div class="ev-tittel" id="ev-tittel">Fyll ut feltene til venstre — anbefalingen bygger seg her.</div>
          <ul class="ev-grunner" id="ev-grunner"></ul>
        </div>

        <div class="enk-skatt" id="enk-skatt">
          <h4 id="skatt-tittel">Forenklet skatteillustrasjon</h4>
          <div class="skatt-g" id="skatt-grid"></div>
          <div class="skatt-note">⚠️ Forenklet illustrasjon basert på 2026-satser (trygdeavgift 10,8 %, selskapsskatt 22 %, utbytteskatt 37,84 %). Ikke individuelt skatteråd.</div>
        </div>

        <div class="enk-tbl-wrap" id="enk-tbl-wrap">
          <table class="enk-tbl" id="enk-tbl"></table>
        </div>

        <div class="enk-cta">
          <h3>Vil du ha dette skriftlig og signert?</h3>
          <p>Vi setter opp en personlig vurdering av din situasjon — med anbefaling, begrunnelse og sjekkliste for oppstart. Signert av juridisk rådgiver, Walrus AS.</p>
          <a href="mailto:rettsregel@gmail.com?subject=Forespørsel%20om%20selskapsform-vurdering" class="btn-aksjon">Send forespørsel →</a>
          <span class="enk-cta-pris">990 kr · Svar innen 48 timer</span>
        </div>
      </div>
    </div>

    <div class="prose sp-body no-print" style="margin-top:0">
      <h2>Hva er forskjellen på ENK og AS?</h2>
      <p>I et ENK er du personlig ansvarlig for all gjeld — kreditorer kan gå etter privatøkonomien din. I et AS er ansvaret begrenset til aksjekapitalen (minimum 30 000 kr).</p>
      <p>ENK: Overskuddet beskattes som personlig næringsinntekt — trygdeavgift 10,8 % pluss flat 22 % og trinnskatt opptil 17,8 %. AS: Selskapet betaler 22 % selskapsskatt. Tar du ut som utbytte betaler du 37,84 % utbytteskatt — ca. 51,5 % totalt. Men beholder du pengene i selskapet: kun 22 %.</p>
      <p>ENK: Sykepenger fra dag 17 (80 %), ingen dagpenger. AS med lønnet eier: 100 % sykepenger fra dag 1, dagpenger ved arbeidsledighet.</p>
      <p>ENK kan bare ha én eier og kan ikke selges som juridisk enhet. AS kan ha mange eiere, selges via aksjer, og hente investorer.</p>
    </div>
  </div>
</main>

<script>
function radio(name) {{
  const el = document.querySelector('input[name="'+name+'"]:checked');
  return el ? el.value : null;
}}
function kr(n) {{ return n ? parseInt(n).toLocaleString('nb-NO') + ' kr' : '—'; }}

function beregnEnkSkatt(x) {{
  if (!x || x <= 0) return 0;
  const trygd = x * 0.108;
  const flat = (x - trygd) * 0.22;
  let trinn = 0;
  if (x > 226100) trinn += (Math.min(x,318300)-226100)*0.017;
  if (x > 318300) trinn += (Math.min(x,725050)-318300)*0.040;
  if (x > 725050) trinn += (Math.min(x,980100)-725050)*0.137;
  if (x > 980100) trinn += (Math.min(x,1467200)-980100)*0.168;
  if (x > 1467200) trinn += (x-1467200)*0.178;
  return Math.round(trygd + flat + trinn);
}}

function oppdater() {{
  const eiere     = radio('eiere');
  const kapital   = radio('kapital');
  const bransje   = radio('bransje');
  const investorer= radio('investorer');
  const har30k    = radio('har30k');
  const sykepen   = radio('sykepenger');
  const ansette   = radio('ansette');
  const overskudd = parseInt(document.getElementById('overskudd').value) || 0;

  const vEl  = document.getElementById('enk-vurdering');
  const sEl  = document.getElementById('enk-skatt');
  const tEl  = document.getElementById('enk-tbl-wrap');

  // Trenger minimum: eiere + én til
  if (!eiere) {{
    vEl.style.display='none'; sEl.style.display='none'; tEl.style.display='none';
    return;
  }}

  let type, tittel, grunner=[];

  if (eiere === 'flere') {{
    type='as-krav'; tittel='Dere er flere eiere — da kreves AS.';
    grunner=['ENK kan bare ha én eier. For felles eierskap er AS den eneste juridiske løsningen.',
             'AS gir dere aksjer som kan fordeles, selges og pantsettes. Reguler eierforholdet i en aksjonæravtale.'];
  }} else if (investorer === 'ja') {{
    type='as-krav'; tittel='Du trenger AS — investorer krever det.';
    grunner=['Investorer krever aksjer. Det er ikke mulig med ENK.',
             'Aksjeloven gir investorer rettsvern, utbytte og mulighet for exit. Alt forutsetter AS.'];
  }} else if (har30k === 'nei') {{
    type='enk'; tittel='Start som ENK — vurder AS om ett til to år.';
    grunner=['Aksjekapitalen på 30 000 kr er et lovpålagt krav ved stiftelse av AS.',
             'ENK er gratis å etablere. Du kan konvertere til AS når du er klar.'];
    if (sykepen === 'ja') grunner.push('Merk: ENK gir sykepenger fra dag 17 (80 %) — ikke dag 1. Bygg en buffer til du konverterer.');
  }} else {{
    let score = 0;
    const risk = {{konsulent:2, haandverk:3, handel:1, helse:3, kreativ:0, annet:1}};
    if (bransje) score += (risk[bransje]||1);
    if (kapital==='beholde') score+=3; else if (kapital==='blanding') score+=1;
    if (ansette==='ja') score+=2;
    if (sykepen==='ja') score+=2;
    if (overskudd > 600000) score+=1;

    if (score >= 5) {{
      type='as'; tittel='Vi anbefaler AS.';
      const riskMap = {{haandverk:'Bransjen har høy risiko for erstatningskrav. AS begrenser ditt personlige ansvar.',helse:'Helse og omsorg innebærer ansvar for andres velvære. AS gir deg ansvarsvernet du trenger.',konsulent:'Konsulenter kan stilles ansvarlig for feile råd. AS skiller privatøkonomien fra virksomhetens risiko.'}};
      if (bransje && riskMap[bransje]) grunner.push(riskMap[bransje]);
      if (kapital==='beholde') grunner.push('Du vil beholde kapital i selskapet. AS lar deg akkumulere overskudd med kun 22 % selskapsskatt uten å ta det ut som personinntekt.');
      if (ansette==='ja') grunner.push('Du planlegger å ansette. AS er bedre egnet som arbeidsgiver — du kan ansette deg selv med fulle NAV-rettigheter.');
      if (sykepen==='ja') grunner.push('Du trenger sykepenger fra dag 1. Med lønn fra eget AS har du 100 % sykepengedekning fra første dag.');
    }} else if (score >= 3) {{
      type='as'; tittel='AS er det tryggeste valget.';
      if (kapital==='beholde') grunner.push('Du vil beholde kapital i selskapet — AS er langt bedre egnet enn ENK til det.');
      if (sykepen==='ja') grunner.push('Full sykepengedekning fra dag 1 forutsetter at du er lønnet ansatt, noe som bare er mulig i AS.');
      grunner.push('ENK er enklere å starte, men AS gir bedre vern og mer fleksibilitet over tid.');
    }} else {{
      type='enk'; tittel='ENK er riktig for deg nå.';
      grunner.push('Du er solo, risikoen er lav, og du tar ut det du tjener. Da er ENK den enkleste og billigste løsningen.');
      grunner.push('Du sparer 36 825 kr i oppstartskostnader og slipper årsregnskap og styrekrav.');
      grunner.push('Du kan konvertere til AS når du faktisk trenger det.');
    }}
  }}

  const badgeTekst = {{as:'AS anbefales',enk:'ENK anbefales','as-krav':'AS er påkrevd'}};
  vEl.className = 'enk-vurdering ' + type;
  vEl.style.display = 'block';
  document.getElementById('ev-badge').textContent = badgeTekst[type];
  document.getElementById('ev-tittel').textContent = tittel;
  document.getElementById('ev-grunner').innerHTML = grunner.map(g=>'<li>'+g+'</li>').join('');

  // Skatteillustrasjon
  if (overskudd > 0) {{
    const enkSkatt = beregnEnkSkatt(overskudd);
    const ss = Math.round(overskudd*0.22);
    const rest = overskudd - ss;
    const utb = Math.round(rest*0.3784);
    const trygd = Math.round(overskudd*0.108);
    const flat = Math.round((overskudd-trygd)*0.22);
    const trinn = enkSkatt - trygd - flat;
    document.getElementById('skatt-tittel').textContent = 'Forenklet skatteillustrasjon — ' + overskudd.toLocaleString('nb-NO') + ' kr i overskudd';
    document.getElementById('skatt-grid').innerHTML =
      '<div class="sk"><div class="sk-lov">ENK</div>'+
      '<div class="sk-r"><span>Trygdeavgift (10,8 %)</span><span>'+kr(trygd)+'</span></div>'+
      '<div class="sk-r"><span>Flat skatt (22 %)</span><span>'+kr(flat)+'</span></div>'+
      '<div class="sk-r"><span>Trinnskatt</span><span>'+kr(trinn)+'</span></div>'+
      '<div class="sk-r tot"><span>Total skatt</span><span>'+kr(enkSkatt)+'</span></div>'+
      '<div class="sk-r igjen"><span>Du sitter igjen med</span><span>'+kr(overskudd-enkSkatt)+'</span></div></div>'+
      '<div class="sk"><div class="sk-lov">AS — beholder i selskapet</div>'+
      '<div class="sk-r"><span>Selskapsskatt (22 %)</span><span>'+kr(ss)+'</span></div>'+
      '<div class="sk-r igjen"><span>Akkumulert i AS</span><span>'+kr(rest)+'</span></div>'+
      '<div class="sk-r" style="margin-top:10px;padding-top:10px;border-top:1px solid var(--line);color:var(--ink-mute);font-size:12px"><span>Tar du ut som utbytte:</span><span>+'+kr(utb)+' skatt</span></div></div>';
    sEl.style.display = 'block';
  }} else {{
    sEl.style.display = 'none';
  }}

  // Sammenligningstabel
  const anEN = type==='enk', anAS = (type==='as'||type==='as-krav');
  document.getElementById('enk-tbl').innerHTML =
    '<thead><tr><th></th><th'+(anEN?' class="anbefalt"':'')+'>ENK</th><th'+(anAS?' class="anbefalt"':'')+'>AS</th></tr></thead>'+
    '<tbody>'+
    '<tr><td>Oppstartskostnad</td><td'+(anEN?' class="anbefalt"':'')+'>0 kr</td><td'+(anAS?' class="anbefalt"':'')+'>36 825 kr</td></tr>'+
    '<tr><td>Antall eiere</td><td'+(anEN?' class="anbefalt"':'')+'>Bare én</td><td'+(anAS?' class="anbefalt"':'')+'>En eller flere</td></tr>'+
    '<tr><td>Personlig ansvar</td><td'+(anEN?' class="anbefalt"':'')+'>Fullt ansvar</td><td'+(anAS?' class="anbefalt"':'')+'>Begrenset til 30 000 kr</td></tr>'+
    '<tr><td>Skatt på overskudd</td><td'+(anEN?' class="anbefalt"':'')+'>Personskatt (22 %+10,8 %+trinn)</td><td'+(anAS?' class="anbefalt"':'')+'>22 % selskapsskatt</td></tr>'+
    '<tr><td>Sykepenger</td><td'+(anEN?' class="anbefalt"':'')+'>Fra dag 17 (80 %)</td><td'+(anAS?' class="anbefalt"':'')+'>Fra dag 1 (100 %) med lønn</td></tr>'+
    '<tr><td>Dagpenger</td><td'+(anEN?' class="anbefalt"':'')+'>Nei</td><td'+(anAS?' class="anbefalt"':'')+'>Ja, ved lønnet ansettelse</td></tr>'+
    '<tr><td>Investorer mulig?</td><td'+(anEN?' class="anbefalt"':'')+'>Nei</td><td'+(anAS?' class="anbefalt"':'')+'>Ja</td></tr>'+
    '<tr><td>Kan selges?</td><td'+(anEN?' class="anbefalt"':'')+'>Bare enkelteiendeler</td><td'+(anAS?' class="anbefalt"':'')+'>Ja — via aksjesalg</td></tr>'+
    '</tbody>';
  tEl.style.display = 'block';
}}
</script>

{site_footer(depth=2)}"""




def render_kontrakter_hub():
    return f"""{shared_head(
        'Kontraktsmaler — fyll ut og last ned gratis | Rettsregel',
        'Gratis juridiske kontraktsmaler basert på norsk lov. Husleiekontrakt, samboeravtale og kjøpekontrakt bil. Fyll ut i nettleseren, last ned som PDF.',
        depth=1, canonical_path='/kontrakter/'
    )}
{site_nav(depth=1)}
<style>
.kontr-hero {{ padding: 72px 0 64px; max-width: 800px; }}
.kontr-hero .kicker {{ font-family: var(--sans); font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.18em; color: var(--accent); display: block; margin-bottom: 20px; }}
.kontr-hero h1 {{ font-family: var(--serif); font-weight: 400; font-size: clamp(26px, 3.4vw, 40px); letter-spacing: -0.02em; line-height: 1.06; margin-bottom: 24px; }}
.kontr-hero .lead {{ font-size: 18px; color: var(--ink-soft); line-height: 1.6; max-width: 560px; }}

/* Kontrakt document cards */
.kontr-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; margin-bottom: 80px; }}
.kontr-kort {{
  display: block; text-decoration: none; color: var(--ink);
  background: var(--bg-card); border: 1px solid var(--line);
  border-radius: 16px; padding: 32px; position: relative;
  transition: box-shadow 0.2s, border-color 0.2s; overflow: hidden;
}}
.kontr-kort::before {{
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
  background: var(--accent); transform: scaleX(0); transform-origin: left;
  transition: transform 0.25s ease;
}}
.kontr-kort:hover {{ box-shadow: 0 8px 32px rgba(0,0,0,0.1); border-color: transparent; }}
.kontr-kort:hover::before {{ transform: scaleX(1); }}
.kontr-kort:hover .kontr-arrow {{ color: var(--accent); transform: translateX(4px); }}
.kontr-ikon {{ width: 48px; height: 48px; background: var(--bg-alt); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 22px; margin-bottom: 24px; }}
.kontr-kat {{ font-family: var(--sans); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; color: var(--accent); margin-bottom: 10px; }}
.kontr-tittel {{ font-family: var(--serif); font-size: 22px; font-weight: 400; letter-spacing: -0.01em; line-height: 1.2; margin-bottom: 12px; }}
.kontr-beskr {{ font-family: var(--sans); font-size: 14px; color: var(--ink-soft); line-height: 1.6; margin-bottom: 28px; }}
.kontr-footer {{ display: flex; justify-content: space-between; align-items: center; padding-top: 20px; border-top: 1px solid var(--line); }}
.kontr-lov-ref {{ font-family: var(--sans); font-size: 11px; font-weight: 600; color: var(--ink-mute); text-transform: uppercase; letter-spacing: 0.1em; }}
.kontr-arrow {{ font-size: 16px; color: var(--ink-mute); transition: color 0.15s, transform 0.15s; }}
.kontr-kort.snart {{ opacity: 0.55; pointer-events: none; }}
.kontr-kort.snart::before {{ display: none; }}
.kontr-snart-tag {{ font-family: var(--sans); font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--ink-mute); background: var(--bg-alt); padding: 3px 9px; border-radius: 4px; margin-bottom: 10px; display: inline-block; }}

/* Kommende-seksjon */
.kontr-kommende-hd {{ font-family: var(--sans); font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; color: var(--ink); padding-bottom: 16px; border-bottom: 1.5px solid var(--ink); margin-bottom: 0; }}
.kontr-kommende-liste {{ display: flex; flex-direction: column; margin-bottom: 64px; }}
.kontr-kommende-rad {{ display: flex; align-items: center; justify-content: space-between; padding: 18px 0; border-bottom: 1px solid var(--line); }}
.kontr-kommende-rad:last-child {{ border-bottom: none; }}
.kontr-kommende-navn {{ font-family: var(--serif); font-size: 18px; font-weight: 400; color: var(--ink-soft); }}
.kontr-kommende-tag {{ font-family: var(--sans); font-size: 11px; font-weight: 600; color: var(--ink-mute); text-transform: uppercase; letter-spacing: 0.1em; }}

@media (max-width: 600px) {{
  .kontr-hero {{ padding: 48px 0 40px; }}
  .kontr-grid {{ grid-template-columns: 1fr; }}
}}
</style>
<main class="page">
  <div class="kontr-hero">
    <span class="kicker">Kontraktsmaler</span>
    <h1>Fyll ut. Last ned. Send.</h1>
    <p class="lead">Juridisk korrekte maler basert på norsk lov. Gratis å bruke. Ingen registrering.</p>
  </div>

  <div class="kontr-grid">
    <a href="../kontrakter/husleiekontrakt/" class="kontr-kort">
      <div class="kontr-ikon">🏠</div>
      <div class="kontr-kat">Bolig og leie</div>
      <h2 class="kontr-tittel">Husleiekontrakt</h2>
      <p class="kontr-beskr">Standard leiekontrakt for bolig. Tidsubestemt eller tidsbestemt. Dekker depositum, oppsigelsestid, vedlikehold og betaling.</p>
      <div class="kontr-footer">
        <span class="kontr-lov-ref">Husleieloven</span>
        <span class="kontr-arrow">→</span>
      </div>
    </a>
    <a href="../kontrakter/samboeravtale/" class="kontr-kort">
      <div class="kontr-ikon">💑</div>
      <div class="kontr-kat">Familie og samliv</div>
      <h2 class="kontr-tittel">Samboeravtale</h2>
      <p class="kontr-beskr">Regner hvem som eier hva, fordeling av utgifter og hva som skjer ved brudd. Norges mest forsømte dokument.</p>
      <div class="kontr-footer">
        <span class="kontr-lov-ref">Husstandsfellesskapsloven</span>
        <span class="kontr-arrow">→</span>
      </div>
    </a>
    <a href="../kontrakter/kjopekontraktbil/" class="kontr-kort">
      <div class="kontr-ikon">🚗</div>
      <div class="kontr-kat">Kjøp og salg</div>
      <h2 class="kontr-tittel">Kjøpekontrakt bil</h2>
      <p class="kontr-beskr">Privatbilsalg uten kontrakt er risikabelt for begge parter. Fyll ut kjøper, selger, bilen, tilstand og betaling.</p>
      <div class="kontr-footer">
        <span class="kontr-lov-ref">Kjøpsloven</span>
        <span class="kontr-arrow">→</span>
      </div>
    </a>
  </div>

  <div>
    <div class="kontr-kommende-hd">Under utvikling</div>
    <div class="kontr-kommende-liste">
      <div class="kontr-kommende-rad"><span class="kontr-kommende-navn">Gjeldsbrev</span><span class="kontr-kommende-tag">Snart</span></div>
      <div class="kontr-kommende-rad"><span class="kontr-kommende-navn">Aksjonæravtale</span><span class="kontr-kommende-tag">Snart</span></div>
      <div class="kontr-kommende-rad"><span class="kontr-kommende-navn">Oppdragsavtale konsulent</span><span class="kontr-kommende-tag">Snart</span></div>
      <div class="kontr-kommende-rad"><span class="kontr-kommende-navn">Generalforsamlingsprotokoll</span><span class="kontr-kommende-tag">Snart</span></div>
    </div>
  </div>
</main>
{site_footer(depth=1)}"""


def render_kontrakter_husleiekontrakt():
    return f"""{shared_head(
        'Husleiekontrakt — fyll ut og last ned gratis | Rettsregel',
        'Gratis husleiekontrakt for bolig. Fyll ut i nettleseren og last ned som PDF. Basert på husleieloven av 26. mars 1999.',
        depth=2, canonical_path='/kontrakter/husleiekontrakt/'
    )}
{site_nav(depth=2)}

<style>
.kontrakt-layout {{
  display: grid; grid-template-columns: 380px 1fr; gap: 32px;
  align-items: start; margin-bottom: 64px;
}}
.kontrakt-layout > * {{ min-width: 0; }}
@media (max-width: 1024px) {{ .kontrakt-layout {{ grid-template-columns: 1fr !important; }} }}
.kontrakt-skjema {{
  background: var(--bg-card); border: 1px solid var(--line);
  border-radius: 20px; padding: 28px; box-shadow: var(--shadow-md);
  position: sticky; top: 24px;
}}
@media (max-width: 1024px) {{ .kontrakt-skjema {{ position: static !important; }} }}
.ks-tittel {{ font-family: var(--serif); font-size: 18px; font-weight: 400; margin-bottom: 20px; }}
.ks-seksjon {{ margin-bottom: 20px; border-bottom: 1px solid var(--line); padding-bottom: 20px; }}
.ks-seksjon:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
.ks-seksjon-tittel {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); margin-bottom: 12px; }}
.kf {{ margin-bottom: 10px; }}
.kf label {{ display: block; font-size: 12px; font-weight: 600; color: var(--ink-soft); margin-bottom: 4px; }}
.kf input, .kf select, .kf textarea {{
  width: 100%; padding: 9px 12px; border: 1.5px solid var(--line);
  border-radius: 8px; font-family: var(--sans); font-size: 16px;
  background: var(--bg); color: var(--ink); box-sizing: border-box; transition: border-color 0.15s;
}}
.kf input:focus, .kf select:focus, .kf textarea:focus {{ outline: none; border-color: var(--accent); }}
.kf textarea {{ min-height: 60px; resize: vertical; }}
.kf-radio {{ display: flex; gap: 8px; flex-wrap: wrap; }}
.kf-radio label {{
  display: flex; align-items: center; gap: 5px; font-size: 13px;
  font-weight: 500; color: var(--ink); cursor: pointer; padding: 6px 10px;
  border: 1.5px solid var(--line); border-radius: 8px; white-space: nowrap;
}}
.kf-radio input[type=radio] {{ width: auto; margin: 0; accent-color: var(--accent); }}
.kf-radio label:has(input:checked) {{ border-color: var(--accent); background: rgba(177,74,42,0.05); color: var(--accent); font-weight: 600; }}
.last-ned-kn {{
  width: 100%; background: var(--accent); color: white; border: none;
  border-radius: 12px; font-family: var(--sans); font-size: 15px;
  font-weight: 600; padding: 15px; cursor: pointer; margin-top: 20px;
  transition: background 0.2s; display: flex; align-items: center;
  justify-content: center; gap: 8px;
}}
.last-ned-kn:hover {{ background: var(--accent-deep); }}
.kontrakt-dokument {{
  background: white; border: 1px solid var(--line); border-radius: 16px;
  padding: 48px 56px; box-shadow: var(--shadow-sm); font-family: 'EB Garamond', Georgia, serif;
  font-size: 16px; line-height: 1.8; color: var(--ink);
}}
@media (max-width: 600px) {{ .kontrakt-dokument {{ padding: 24px 20px; font-size: 15px; }} }}
.kd-tittel {{ font-size: 20px; font-weight: 500; text-align: center; margin-bottom: 6px; }}
.kd-undertittel {{ font-size: 13px; text-align: center; color: var(--ink-mute); margin-bottom: 32px; font-family: var(--sans); }}
.kd-h2 {{ font-size: 14px; font-weight: 700; font-family: var(--sans); text-transform: uppercase; letter-spacing: 0.08em; margin: 28px 0 8px; border-bottom: 1px solid var(--line); padding-bottom: 4px; }}
.kd-rad {{ display: flex; gap: 8px; margin-bottom: 4px; }}
.kd-etikettene {{ color: var(--ink-mute); min-width: 140px; font-size: 14px; }}
.kd-v {{ font-size: 15px; }}
.kd-varighet-boks {{ border: 1px solid var(--line); border-radius: 8px; padding: 12px 16px; margin: 8px 0; background: var(--bg); }}
.kd-sign {{ margin-top: 40px; display: grid; grid-template-columns: 1fr 1fr; gap: 32px; }}
.kd-sign-felt {{ border-top: 1px solid var(--ink); padding-top: 6px; }}
.kd-sign-etikett {{ font-size: 13px; color: var(--ink-mute); font-family: var(--sans); }}
.kd-sign-navn {{ font-size: 14px; margin-top: 4px; }}
.kd-footer {{ font-size: 12px; color: var(--ink-mute); font-family: var(--sans); margin-top: 32px; text-align: center; border-top: 1px solid var(--line); padding-top: 12px; }}
@media print {{
  .no-print {{ display: none !important; }}
  nav.site-nav, footer.site-footer, #chat-toggle, #chat-panel, .breadcrumbs, .article-header, .kontrakt-skjema, .sp-body {{ display: none !important; }}
  .kontrakt-layout {{ grid-template-columns: 1fr; display: block; }}
  .kontrakt-dokument {{ border: none; box-shadow: none; padding: 0; border-radius: 0; font-size: 12pt; line-height: 1.6; }}
  body {{ background: white; }}
}}
</style>

<main class="page">
  <div class="container">
    <div class="breadcrumbs no-print">
      <a href="../../">Rettsregel</a><span class="sep">›</span>
      <a href="../../kontrakter/">Kontrakter</a><span class="sep">›</span>
      <span class="current">Husleiekontrakt</span>
    </div>
    <div class="article-header no-print">
      <div class="article-eyebrow">Kontraktmal</div>
      <h1 class="article-title">Husleiekontrakt for bolig</h1>
      <p class="article-description">Fyll ut feltene til venstre. Kontrakten oppdateres live. Last ned som PDF når du er ferdig.</p>
    </div>

    <div class="kontrakt-layout">
      <div class="kontrakt-skjema no-print">
        <div class="ks-tittel">Fyll ut kontrakten</div>
        <div class="ks-seksjon">
          <div class="ks-seksjon-tittel">Utleier</div>
          <div class="kf"><label>Fullt navn</label><input type="text" id="utleier_navn" oninput="oppdater()" placeholder="Ola Nordmann"></div>
          <div class="kf"><label>Adresse</label><input type="text" id="utleier_adresse" oninput="oppdater()" placeholder="Storgata 1, 0000 Oslo"></div>
          <div class="kf"><label>Telefon / e-post</label><input type="text" id="utleier_kontakt" oninput="oppdater()" placeholder="900 00 000"></div>
        </div>
        <div class="ks-seksjon">
          <div class="ks-seksjon-tittel">Leietaker</div>
          <div class="kf"><label>Fullt navn</label><input type="text" id="leietaker_navn" oninput="oppdater()" placeholder="Kari Nordmann"></div>
          <div class="kf"><label>Fødselsdato</label><input type="date" id="leietaker_fodsel" oninput="oppdater()"></div>
          <div class="kf"><label>Telefon / e-post</label><input type="text" id="leietaker_kontakt" oninput="oppdater()" placeholder="900 00 000"></div>
        </div>
        <div class="ks-seksjon">
          <div class="ks-seksjon-tittel">Leieobjektet</div>
          <div class="kf"><label>Adresse</label><input type="text" id="bolig_adresse" oninput="oppdater()" placeholder="Leiegata 5, 5000 Bergen"></div>
          <div class="kf"><label>Type bolig</label><input type="text" id="bolig_type" oninput="oppdater()" placeholder="f.eks. 2-roms leilighet, 55 m²"></div>
          <div class="kf"><label>Møblering</label>
            <div class="kf-radio">
              <label><input type="radio" name="moblert" value="umøblert" onchange="oppdater()" checked> Umøblert</label>
              <label><input type="radio" name="moblert" value="delvis møblert" onchange="oppdater()"> Delvis møblert</label>
              <label><input type="radio" name="moblert" value="møblert" onchange="oppdater()"> Møblert</label>
            </div>
          </div>
        </div>
        <div class="ks-seksjon">
          <div class="ks-seksjon-tittel">Varighet</div>
          <div class="kf"><div class="kf-radio">
            <label><input type="radio" name="varighet" value="tidsubestemt" onchange="oppdaterVarighetUI()" checked> Tidsubestemt</label>
            <label><input type="radio" name="varighet" value="tidsbestemt" onchange="oppdaterVarighetUI()"> Tidsbestemt</label>
          </div></div>
          <div class="kf"><label>Startdato</label><input type="date" id="start_dato" oninput="oppdater()"></div>
          <div id="tidsbestemt-felt" style="display:none"><div class="kf"><label>Sluttdato</label><input type="date" id="slutt_dato" oninput="oppdater()"></div></div>
          <div id="oppsigelse-felt"><div class="kf"><label>Oppsigelsestid</label>
            <select id="oppsigelse_tid" onchange="oppdater()">
              <option value="1">1 måned</option><option value="2">2 måneder</option><option value="3" selected>3 måneder</option>
            </select>
          </div></div>
        </div>
        <div class="ks-seksjon">
          <div class="ks-seksjon-tittel">Økonomi</div>
          <div class="kf"><label>Månedlig leie (kr)</label><input type="number" id="leie_kr" oninput="oppdater()" placeholder="12000" min="0"></div>
          <div class="kf"><label>Forfallsdato (dag i mnd)</label><input type="number" id="forfall_dag" oninput="oppdater()" placeholder="1" min="1" max="28"></div>
          <div class="kf"><label>Kontonummer</label><input type="text" id="konto_nr" oninput="oppdater()" placeholder="1234 56 78901"></div>
          <div class="kf"><label>Depositum (kr)</label><input type="number" id="depositum_kr" oninput="oppdater()" placeholder="36000" min="0"></div>
          <div class="kf"><label>Strøm og vann</label>
            <div class="kf-radio">
              <label><input type="radio" name="strom" value="Inkludert i leien" onchange="oppdater()" checked> Inkludert</label>
              <label><input type="radio" name="strom" value="Betales i tillegg" onchange="oppdater()"> I tillegg</label>
              <label><input type="radio" name="strom" value="Eget abonnement" onchange="oppdater()"> Eget abonnement</label>
            </div>
          </div>
        </div>
        <div class="ks-seksjon">
          <div class="ks-seksjon-tittel">Særlige vilkår (valgfritt)</div>
          <div class="kf"><textarea id="saerlige_vilkaar" oninput="oppdater()" placeholder="f.eks. Dyrehold er ikke tillatt."></textarea></div>
        </div>
        <button class="last-ned-kn" onclick="window.print()">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7,10 12,15 17,10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Last ned som PDF
        </button>
        <p style="font-size:12px;color:var(--ink-mute);text-align:center;margin-top:8px">Trykk «Last ned» → «Lagre som PDF» i utskriftsdialogen</p>
      </div>

      <div class="kontrakt-dokument" id="kd">
        <div class="kd-tittel">HUSLEIEKONTRAKT FOR BOLIG</div>
        <div class="kd-undertittel">Utarbeidet i samsvar med husleieloven av 26. mars 1999</div>
        <div class="kd-h2">1. Parter</div>
        <div class="kd-rad"><span class="kd-etikettene">Utleier</span><span class="kd-v" id="kd-utleier-navn">_______________</span></div>
        <div class="kd-rad"><span class="kd-etikettene">Adresse</span><span class="kd-v" id="kd-utleier-adresse">_______________</span></div>
        <div class="kd-rad"><span class="kd-etikettene">Kontakt</span><span class="kd-v" id="kd-utleier-kontakt">_______________</span></div>
        <div class="kd-rad" style="margin-top:12px"><span class="kd-etikettene">Leietaker</span><span class="kd-v" id="kd-leietaker-navn">_______________</span></div>
        <div class="kd-rad"><span class="kd-etikettene">Fødselsdato</span><span class="kd-v" id="kd-leietaker-fodsel">_______________</span></div>
        <div class="kd-rad"><span class="kd-etikettene">Kontakt</span><span class="kd-v" id="kd-leietaker-kontakt">_______________</span></div>
        <div class="kd-h2">2. Leieobjektet</div>
        <div class="kd-rad"><span class="kd-etikettene">Adresse</span><span class="kd-v" id="kd-bolig-adresse">[adresse]</span></div>
        <div class="kd-rad"><span class="kd-etikettene">Type</span><span class="kd-v" id="kd-bolig-type">[type]</span></div>
        <div class="kd-rad"><span class="kd-etikettene">Møblering</span><span class="kd-v" id="kd-moblert">Umøblert</span></div>
        <div class="kd-h2">3. Varighet og oppsigelse</div>
        <div class="kd-varighet-boks" id="kd-varighet-boks">Tidsubestemt leieforhold. Starter den <strong id="kd-start-dato">[dato]</strong>. Kan sies opp av begge parter med <strong id="kd-oppsigelse-tid">3</strong> måneders varsel, regnet fra 1. i påfølgende måned, jf. husleieloven §§ 9-3 og 9-6.</div>
        <div class="kd-h2">4. Leie og økonomi</div>
        <div class="kd-rad"><span class="kd-etikettene">Månedlig leie</span><span class="kd-v"><strong id="kd-leie">___</strong> kr/mnd</span></div>
        <div class="kd-rad"><span class="kd-etikettene">Forfall</span><span class="kd-v">Den <strong id="kd-forfall">___</strong>. i hver måned</span></div>
        <div class="kd-rad"><span class="kd-etikettene">Konto</span><span class="kd-v" id="kd-konto">_______________</span></div>
        <div class="kd-rad" style="margin-top:8px"><span class="kd-etikettene">Depositum</span><span class="kd-v"><strong id="kd-depositum">___</strong> kr. Settes på særskilt depositumskonto i leietakers navn, jf. husleieloven § 3-5.</span></div>
        <div class="kd-rad" style="margin-top:8px"><span class="kd-etikettene">Strøm og vann</span><span class="kd-v" id="kd-strom">Inkludert i leien</span></div>
        <div class="kd-h2">5. Vedlikehold og bruk</div>
        <div style="font-size:15px;line-height:1.7">Leietaker plikter å behandle boligen med tilbørlig aktsomhet, jf. husleieloven § 5-2. Leietaker bekoster vedlikehold av låser, kraner og batteri i røykvarsler, jf. husleieloven § 5-3. Røyking og dyrehold er kun tillatt etter skriftlig avtale. Fremleie er ikke tillatt uten utleiers skriftlige samtykke, jf. husleieloven § 7-2.</div>
        <div class="kd-h2" id="kd-sae-h" style="display:none">6. Særlige vilkår</div>
        <div id="kd-saerlige-vilkaar" style="display:none;font-size:15px;line-height:1.7"></div>
        <div class="kd-h2">7. Signatur</div>
        <div style="font-size:15px;margin-bottom:24px">Kontrakten er undertegnet i to eksemplarer, ett til hver part.</div>
        <div class="kd-sign">
          <div><div class="kd-sign-felt"></div><div class="kd-sign-etikett">Sted og dato — Utleier</div><div class="kd-sign-navn" id="kd-sign-utleier">_______________</div></div>
          <div><div class="kd-sign-felt"></div><div class="kd-sign-etikett">Sted og dato — Leietaker</div><div class="kd-sign-navn" id="kd-sign-leietaker">_______________</div></div>
        </div>
        <div class="kd-footer">Kontrakten er utarbeidet i samsvar med husleieloven av 26. mars 1999. Rettsregel.no</div>
      </div>
    </div>

    <div class="prose sp-body no-print">
      <h2>Hva bør en husleiekontrakt inneholde?</h2>
      <p>En gyldig husleiekontrakt trenger partenes navn, boligens adresse, leiens størrelse, forfallsdato og leieperiodens lengde.</p>
      <h3>Depositum — alltid på depositumskonto</h3>
      <p>Depositumet skal stå på en særskilt konto i leietakers navn, adskilt fra utleiers midler, jf. husleieloven § 3-5. Maksimalt 6 månedlige leier.</p>
      <h3>Tidsbestemt eller tidsubestemt?</h3>
      <p>Tidsbestemte kontrakter på 3 år eller mer brukes der begge parter vil sikre en bestemt periode. Kortere tidsbestemte kontrakter er lovlig bare i særskilte tilfeller, jf. husleieloven § 9-3. Usikker? Velg tidsubestemt.</p>
      <p>Relevante paragrafer: <a href="../../lover/husleieloven/3-5/">§ 3-5 Depositum</a> · <a href="../../lover/husleieloven/9-3/">§ 9-3 Oppsigelse fra utleier</a> · <a href="../../lover/husleieloven/9-6/">§ 9-6 Oppsigelse fra leietaker</a></p>
    </div>
  </div>
</main>

<script>
function v(id) {{ return document.getElementById(id); }}
function sett(id, tekst) {{ const el = v(id); if (!el) return; el.textContent = tekst || ''; }}
function formDato(iso) {{
  if (!iso) return '';
  return new Date(iso+'T12:00:00').toLocaleDateString('nb-NO',{{day:'numeric',month:'long',year:'numeric'}});
}}
function oppdaterVarighetUI() {{
  const erTB = document.querySelector('input[name=varighet]:checked').value === 'tidsbestemt';
  v('tidsbestemt-felt').style.display = erTB ? 'block' : 'none';
  v('oppsigelse-felt').style.display = erTB ? 'none' : 'block';
  oppdater();
}}
function oppdater() {{
  sett('kd-utleier-navn', v('utleier_navn').value);
  sett('kd-utleier-adresse', v('utleier_adresse').value);
  sett('kd-utleier-kontakt', v('utleier_kontakt').value);
  sett('kd-leietaker-navn', v('leietaker_navn').value);
  const fd = v('leietaker_fodsel').value;
  sett('kd-leietaker-fodsel', fd ? formDato(fd) : '');
  sett('kd-leietaker-kontakt', v('leietaker_kontakt').value);
  sett('kd-bolig-adresse', v('bolig_adresse').value || '[adresse]');
  sett('kd-bolig-type', v('bolig_type').value || '[type]');
  const mob = document.querySelector('input[name=moblert]:checked');
  sett('kd-moblert', mob ? mob.value : 'Umøblert');
  const leieKr = parseInt(v('leie_kr').value);
  sett('kd-leie', leieKr ? leieKr.toLocaleString('nb-NO') : '___');
  sett('kd-forfall', v('forfall_dag').value || '___');
  sett('kd-konto', v('konto_nr').value || '_______________');
  const depKr = parseInt(v('depositum_kr').value);
  sett('kd-depositum', depKr ? depKr.toLocaleString('nb-NO') : '___');
  const strom = document.querySelector('input[name=strom]:checked');
  sett('kd-strom', strom ? strom.value : '');
  const erTB = document.querySelector('input[name=varighet]:checked').value === 'tidsbestemt';
  const startDato = v('start_dato').value;
  const sluttDato = v('slutt_dato').value;
  const oppsTid = v('oppsigelse_tid') ? v('oppsigelse_tid').value : '3';
  if (erTB) {{
    v('kd-varighet-boks').innerHTML = 'Tidsbestemt leieforhold fra <strong>'+(formDato(startDato)||'[startdato]')+'</strong> til <strong>'+(formDato(sluttDato)||'[sluttdato]')+'</strong>. Leieforholdet opphører uten oppsigelse ved utløpsdato, jf. husleieloven § 9-3.';
  }} else {{
    v('kd-varighet-boks').innerHTML = 'Tidsubestemt leieforhold. Starter den <strong>'+(formDato(startDato)||'[dato]')+'</strong>. Kan sies opp av begge parter med <strong>'+oppsTid+'</strong> måneders varsel, regnet fra 1. i påfølgende måned, jf. husleieloven §§ 9-3 og 9-6.';
  }}
  const saer = v('saerlige_vilkaar').value.trim();
  v('kd-sae-h').style.display = saer ? 'block' : 'none';
  v('kd-saerlige-vilkaar').style.display = saer ? 'block' : 'none';
  v('kd-saerlige-vilkaar').textContent = saer;
  sett('kd-sign-utleier', v('utleier_navn').value || '_______________');
  sett('kd-sign-leietaker', v('leietaker_navn').value || '_______________');
}}
oppdater();
</script>

{site_footer(depth=2)}"""



def render_tjenester_reklamasjon_bil():
    return f"""{shared_head(
        'Reklamasjon bilkjøp — lag brevet ditt gratis | Rettsregel',
        'Fyll ut skjemaet og se reklamasjonsbrevet bygge seg live. Gratis verktøy med fristberegning basert på kjøpsloven og forbrukerkjøpsloven.',
        depth=2, canonical_path='/tjenester/reklamasjon-bil/'
    )}
{site_nav(depth=2)}

<style>
.rek-layout {{
  display: grid; grid-template-columns: 380px 1fr; gap: 32px;
  align-items: start; margin-bottom: 64px;
}}
@media (max-width: 1024px) {{ .rek-layout {{ grid-template-columns: 1fr; }} }}
.rek-skjema {{
  background: var(--bg-card); border: 1px solid var(--line);
  border-radius: 20px; padding: 28px; box-shadow: var(--shadow-md);
  position: sticky; top: 24px;
}}
@media (max-width: 1024px) {{ .rek-skjema {{ position: static; }} }}
.rs-tittel {{ font-family: var(--serif); font-size: 18px; font-weight: 400; margin-bottom: 20px; }}
.rs-sek {{ margin-bottom: 20px; border-bottom: 1px solid var(--line); padding-bottom: 20px; }}
.rs-sek:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
.rs-sek-tittel {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); margin-bottom: 12px; }}
.rf {{ margin-bottom: 10px; }}
.rf label {{ display: block; font-size: 12px; font-weight: 600; color: var(--ink-soft); margin-bottom: 4px; }}
.rf input, .rf select, .rf textarea {{
  width: 100%; padding: 9px 12px; border: 1.5px solid var(--line);
  border-radius: 8px; font-family: var(--sans); font-size: 16px;
  background: var(--bg); color: var(--ink); box-sizing: border-box; transition: border-color 0.15s;
}}
.rf input:focus, .rf select:focus, .rf textarea:focus {{ outline: none; border-color: var(--accent); }}
.rf textarea {{ min-height: 70px; resize: vertical; }}
.rf-radio {{ display: flex; flex-direction: column; gap: 6px; margin-top: 4px; }}
.rf-radio label {{
  display: flex; align-items: center; gap: 8px; font-size: 13px;
  font-weight: 500; color: var(--ink); cursor: pointer; padding: 8px 12px;
  border: 1.5px solid var(--line); border-radius: 8px;
}}
.rf-radio input[type=radio] {{ width: auto; margin: 0; accent-color: var(--accent); flex-shrink: 0; }}
.rf-radio label:has(input:checked) {{ border-color: var(--accent); background: rgba(177,74,42,0.05); color: var(--accent); font-weight: 600; }}
.rf-radio-2 {{ flex-direction: row; flex-wrap: wrap; }}
.rf-radio-2 label {{ flex: 1; min-width: 120px; }}
.gen-kn {{
  width: 100%; background: var(--accent); color: white; border: none;
  border-radius: 12px; font-family: var(--sans); font-size: 15px;
  font-weight: 600; padding: 15px; cursor: pointer; margin-top: 20px;
  transition: background 0.2s; display: flex; align-items: center;
  justify-content: center; gap: 8px;
}}
.gen-kn:hover {{ background: var(--accent-deep); }}
/* Vurdering */
.rek-vurdering {{
  border-radius: 12px; padding: 16px 20px; margin-bottom: 20px;
  font-size: 13px; line-height: 1.55; display: none;
}}
.rek-vurdering.ok {{ background: #f0f9f0; border: 1px solid #8dcc8d; }}
.rek-vurdering.advarsel {{ background: #fffbec; border: 1px solid #e8c840; }}
.rek-vurdering.for-sent {{ background: #fdf0ef; border: 1px solid #e8a09a; }}
.rek-vurdering ul {{ margin: 6px 0 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 4px; }}
.rek-vurdering li {{ display: flex; gap: 8px; }}
.rv-tittel {{ font-weight: 700; margin-bottom: 4px; font-size: 14px; }}
/* Brev */
.rek-dokument {{
  background: white; border: 1px solid var(--line); border-radius: 16px;
  padding: 48px 56px; font-family: 'EB Garamond', Georgia, serif;
  font-size: 16px; line-height: 1.8; color: var(--ink);
}}
@media (max-width: 600px) {{ .rek-dokument {{ padding: 24px 20px; font-size: 15px; }} }}
.rek-brev-header {{
  background: var(--bg-alt); padding: 14px 24px;
  display: flex; justify-content: space-between; align-items: center;
  border-bottom: 1px solid var(--line);
}}
.rek-brev-wrapper {{ background: white; border: 1px solid var(--line); border-radius: 16px; overflow: hidden; margin-bottom: 24px; }}
.rek-brev-kn-wrap {{ display: flex; gap: 8px; }}
.rek-brev-kn {{
  font-size: 13px; font-weight: 600; padding: 8px 14px; border-radius: 8px;
  border: none; cursor: pointer; font-family: var(--sans);
}}
.rek-brev-kopi {{ background: var(--accent); color: white; }}
.rek-brev-print {{ background: var(--bg-card); border: 1px solid var(--line); color: var(--ink); }}
.brev-tekst {{
  padding: 36px 40px; font-family: 'EB Garamond', Georgia, serif;
  font-size: 15px; line-height: 1.8; white-space: pre-wrap; color: var(--ink);
}}
@media (max-width: 600px) {{ .brev-tekst {{ padding: 20px; font-size: 14px; }} }}
.neste-steg-boks {{ background: var(--bg-alt); border-radius: 16px; padding: 28px 32px; }}
.neste-steg-boks h3 {{ font-family: var(--serif); font-size: 20px; font-weight: 400; margin-bottom: 16px; }}
.nsl {{ margin: 0; padding: 0; list-style: none; counter-reset: ns; display: flex; flex-direction: column; gap: 12px; }}
.nsl li {{ display: flex; gap: 14px; align-items: flex-start; font-size: 14px; line-height: 1.5; }}
.nsl li::before {{
  counter-increment: ns; content: counter(ns);
  background: var(--accent); color: white; width: 24px; height: 24px; min-width: 24px;
  border-radius: 50%; display: flex; align-items: center; justify-content: center;
  font-size: 12px; font-weight: 700;
}}
@media print {{
  .no-print {{ display: none !important; }}
  nav.site-nav, footer.site-footer, #chat-toggle, #chat-panel, .breadcrumbs, .article-header, .rek-skjema, .sp-body, .neste-steg-boks {{ display: none !important; }}
  .rek-layout {{ display: block; }}
  .rek-brev-wrapper {{ border: none; box-shadow: none; }}
  .rek-brev-header {{ display: none; }}
  .brev-tekst {{ padding: 0; font-size: 12pt; line-height: 1.7; }}
  body {{ background: white; }}
}}
</style>

<main class="page">
  <div class="container">
    <div class="breadcrumbs no-print">
      <a href="../../">Rettsregel</a>
      <span class="sep">›</span>
      <a href="../../tjenester/">Tjenester</a>
      <span class="sep">›</span>
      <span class="current">Reklamasjon bilkjøp</span>
    </div>

    <div class="article-header no-print">
      <div class="article-eyebrow">Gratis verktøy</div>
      <h1 class="article-title">Vil du reklamere på et bilkjøp?</h1>
      <p class="article-description">Fyll ut feltene til venstre. Brevet bygger seg live. Last ned eller kopier når du er ferdig.</p>
    </div>

    <div class="rek-layout">
      <!-- SKJEMA -->
      <div class="rek-skjema no-print">
        <div class="rs-tittel">Fyll ut om kjøpet</div>

        <div class="rs-sek">
          <div class="rs-sek-tittel">Hvem kjøpte du av?</div>
          <div class="rf">
            <div class="rf-radio">
              <label><input type="radio" name="selger_type" value="forhandler" onchange="oppdater()"> Bilforhandler / næringsdrivende</label>
              <label><input type="radio" name="selger_type" value="privat" onchange="oppdater()"> Privatperson (Finn.no, bekjente)</label>
            </div>
          </div>
          <div class="rf" id="lov-info" style="display:none">
            <div style="font-size:12px;color:var(--ink-mute);padding:8px 12px;background:var(--bg-alt);border-radius:8px;line-height:1.5" id="lov-info-tekst"></div>
          </div>
        </div>

        <div class="rs-sek">
          <div class="rs-sek-tittel">Bilens detaljer</div>
          <div class="rf"><label>Kjøpsdato</label><input type="date" id="kjopsdato" oninput="oppdater()"></div>
          <div class="rf"><label>Bilens merke, modell og regnr</label><input type="text" id="bil_besk" oninput="oppdater()" placeholder="f.eks. Toyota RAV4 2019, regnr AB 12345"></div>
          <div class="rf"><label>Kjøpesum (kr)</label><input type="number" id="kjopsum" oninput="oppdater()" placeholder="f.eks. 350000" min="0"></div>
        </div>

        <div class="rs-sek">
          <div class="rs-sek-tittel">Mangelen</div>
          <div class="rf">
            <label>Kategori</label>
            <select id="feil_kat" onchange="oppdater()">
              <option value="">— Velg kategori —</option>
              <option value="motor">Motor / drivverk / girkasse</option>
              <option value="rust">Rust / karosseri</option>
              <option value="el">Elektronikk / el-anlegg</option>
              <option value="km">Feil kilometerstand</option>
              <option value="vraket">Skjult ulykkeshistorikk</option>
              <option value="annet">Annet</option>
            </select>
          </div>
          <div class="rf"><label>Beskriv mangelen konkret</label><textarea id="feil_besk" oninput="oppdater()" placeholder="Hva oppdaget du, og hva er konsekvensen? Jo mer konkret, jo sterkere brev."></textarea></div>
        </div>

        <div class="rs-sek">
          <div class="rs-sek-tittel">Oppdagelse og selgers kunnskap</div>
          <div class="rf"><label>Dato du oppdaget mangelen</label><input type="date" id="oppdagelse" oninput="oppdater()"></div>
          <div class="rf">
            <label>Visste selgeren om mangelen?</label>
            <div class="rf-radio">
              <label><input type="radio" name="visste" value="ja" onchange="oppdater()"> Ja, trolig — selgeren kjente til det</label>
              <label><input type="radio" name="visste" value="vet_ikke" onchange="oppdater()"> Vet ikke / usikker</label>
              <label><input type="radio" name="visste" value="nei" onchange="oppdater()"> Nei, trolig ikke</label>
            </div>
          </div>
        </div>

        <div class="rs-sek">
          <div class="rs-sek-tittel">Ditt krav</div>
          <div class="rf">
            <div class="rf-radio">
              <label><input type="radio" name="krav" value="retting" onchange="oppdater()"> Retting av mangelen</label>
              <label id="krav-omlevering-label" style="display:none"><input type="radio" name="krav" value="omlevering" onchange="oppdater()"> Omlevering (bytte)</label>
              <label><input type="radio" name="krav" value="prisavslag" onchange="oppdater()"> Prisavslag</label>
              <label><input type="radio" name="krav" value="heving" onchange="oppdater()"> Heving — pengene tilbake</label>
            </div>
          </div>
        </div>

        <div class="rs-sek">
          <div class="rs-sek-tittel">Dine opplysninger</div>
          <div class="rf"><label>Ditt navn</label><input type="text" id="mitt_navn" oninput="oppdater()" placeholder="Ola Nordmann"></div>
          <div class="rf"><label>Telefon</label><input type="tel" id="mitt_tlf" oninput="oppdater()" placeholder="400 00 000"></div>
          <div class="rf"><label>E-post</label><input type="email" id="min_epost" oninput="oppdater()" placeholder="ola@eksempel.no"></div>
          <div class="rf"><label>Selgerens navn / firma</label><input type="text" id="selger_navn" oninput="oppdater()" placeholder="Kari Nordmann eller Bil AS"></div>
        </div>
      </div>

      <!-- BREV + VURDERING -->
      <div>
        <div class="rek-vurdering" id="rek-vurdering">
          <div class="rv-tittel" id="rv-tittel"></div>
          <ul id="rv-liste"></ul>
        </div>

        <div class="rek-brev-wrapper">
          <div class="rek-brev-header no-print">
            <span style="font-size:14px;font-weight:600;color:var(--ink-soft)">Ditt reklamasjonsbrev</span>
            <div class="rek-brev-kn-wrap">
              <button class="rek-brev-kn rek-brev-kopi" onclick="kopier()">Kopier</button>
              <button class="rek-brev-kn rek-brev-print" onclick="window.print()">Last ned PDF</button>
            </div>
          </div>
          <div class="brev-tekst" id="brev-tekst">Fyll ut feltene til venstre — brevet bygger seg her.</div>
        </div>

        <div class="neste-steg-boks no-print" id="neste-steg" style="display:none">
          <h3>Hva gjør du nå?</h3>
          <ol class="nsl">
            <li>Send brevet til selgeren på e-post med lesebekreftelse — eller rekommandert post. Ta vare på kvitteringen.</li>
            <li>Sett svarfrist 14 dager. Da vet selgeren hva som gjelder.</li>
            <li id="nsl-krav-spesifikk">Avviser selgeren kravet? Klag til Forbrukerrådet (gratis) eller Forliksrådet.</li>
            <li>Komplisert sak? <a href="mailto:rettsregel@gmail.com" style="color:var(--accent)">Send oss saken</a> — vi hjelper deg videre.</li>
          </ol>
        </div>
      </div>
    </div>

    <div class="prose sp-body no-print">
      <h2>Kjøpte du fra forhandler eller privatperson?</h2>
      <p>Fra forhandler gjelder forbrukerkjøpsloven. Du har 5 år til å reklamere og minimum 2 måneder fra du oppdaget feilen. Fra privatperson gjelder kjøpsloven — 2 år absolutt frist og «rimelig tid» fra oppdagelse (normalt noen uker).</p>
      <h3>Relevante paragrafer</h3>
      <p><a href="../../lover/kjopsloven/32/">§ 32 Reklamasjonsfrister</a> · <a href="../../lover/kjopsloven/39/">§ 39 Heving ved mangel</a> · <a href="../../lover/kjopsloven/33/">§ 33 Unntak ved uærlighet</a></p>
    </div>
  </div>
</main>

<script>
function v(id) {{ return document.getElementById(id); }}
function radio(name) {{ const el = document.querySelector('input[name="'+name+'"]:checked'); return el ? el.value : null; }}
function formDato(iso) {{
  if (!iso) return '';
  return new Date(iso+'T12:00:00').toLocaleDateString('nb-NO',{{day:'numeric',month:'long',year:'numeric'}});
}}
function kr(n) {{ return n ? parseInt(n).toLocaleString('nb-NO') + ' kr' : ''; }}

function beregnFrister() {{
  const selger = radio('selger_type');
  const kjop = v('kjopsdato').value;
  const oppdaget = v('oppdagelse').value;
  if (!selger || !kjop || !oppdaget) return null;
  const kjoepD = new Date(kjop+'T12:00:00');
  const oppdagetD = new Date(oppdaget+'T12:00:00');
  const naa = new Date();
  const ar = selger === 'forhandler' ? 5 : 2;
  const absolutFrist = new Date(kjoepD);
  absolutFrist.setFullYear(absolutFrist.getFullYear()+ar);
  const innenAbsolutt = naa < absolutFrist;
  const dagerTil = Math.floor((absolutFrist-naa)/(864e5));
  const dagerSiden = Math.floor((naa-oppdagetD)/(864e5));
  return {{ selger, ar, innenAbsolutt, dagerTil, dagerSiden }};
}}

function oppdaterVurdering(f) {{
  const el = v('rek-vurdering');
  if (!f) {{ el.style.display='none'; return; }}
  let klasse, tittel, punkter;
  if (!f.innenAbsolutt) {{
    klasse='for-sent'; tittel='⛔ Absolutt frist er trolig utløpt';
    punkter=['Du kjøpte for over '+f.ar+' år siden. Kontakt oss — unntak kan finnes ved uærlighet.'];
  }} else if (f.dagerSiden > 60 && f.selger==='privat') {{
    klasse='advarsel'; tittel='⚠️ Send brevet i dag — fristen er presset';
    punkter=['Det er '+f.dagerSiden+' dager siden du oppdaget mangelen. «Rimelig tid» er normalt noen uker.',f.ar+'-årsfristen: '+f.dagerTil+' dager igjen.'];
  }} else if (f.dagerSiden > 28) {{
    klasse='advarsel'; tittel='⏰ Send brevet snarest';
    punkter=[f.dagerSiden+' dager siden oppdagelse. Ikke vent.',f.ar+'-årsfristen: '+f.dagerTil+' dager igjen.'];
  }} else {{
    klasse='ok'; tittel='✅ Du er godt innenfor fristene';
    punkter=['Oppdaget for '+f.dagerSiden+' dager siden — innenfor rimelig tid.',f.ar+'-årsfristen: '+f.dagerTil+' dager igjen.'];
  }}
  el.className='rek-vurdering '+klasse;
  v('rv-tittel').textContent=tittel;
  v('rv-liste').innerHTML=punkter.map(p=>'<li><span>'+p+'</span></li>').join('');
  el.style.display='block';
}}

function oppdater() {{
  const selger = radio('selger_type');
  const lovInfo = v('lov-info');
  const lovInfoTekst = v('lov-info-tekst');
  if (selger) {{
    lovInfo.style.display='block';
    lovInfoTekst.textContent = selger==='forhandler'
      ? 'Forbrukerkjøpsloven gjelder. Du har 5 år til å reklamere og min. 2 måneder fra du oppdaget feilen.'
      : 'Kjøpsloven gjelder. Du har 2 år absolutt frist og rimelig tid (normalt noen uker) fra oppdagelse.';
    const omlevEl = v('krav-omlevering-label');
    if (omlevEl) omlevEl.style.display = selger==='forhandler' ? 'flex' : 'none';
  }} else {{ lovInfo.style.display='none'; }}

  const f = beregnFrister();
  oppdaterVurdering(f);

  // Generer brev-tekst
  const lov = selger==='forhandler' ? 'forbrukerkjøpsloven' : 'kjøpsloven';
  const lovK = selger==='forhandler' ? 'fkjl.' : 'kjl.';
  const rekPara = selger==='forhandler' ? '27' : '32';
  const risiPara = selger==='forhandler' ? '14' : '21';
  const krav = radio('krav');
  const visste = radio('visste');

  const kravTekster = {{
    retting: 'Jeg krever at mangelen rettes vederlagsfritt for meg, jf. '+lovK+' § '+(selger==='forhandler'?'29':'34')+'.',
    omlevering: 'Jeg krever omlevering — at bilen byttes mot en tilsvarende mangelfri bil, jf. fkjl. § 29.',
    prisavslag: 'Jeg krever prisavslag tilsvarende mangelens verdi, jf. '+lovK+' § '+(selger==='forhandler'?'31':'38')+'.',
    heving: 'Mangelen er etter min vurdering vesentlig. Jeg hever herved kjøpet, jf. '+lovK+' § '+(selger==='forhandler'?'32':'39')+', og krever full tilbakebetaling av kjøpesummen'+(v('kjopsum').value?' kr '+kr(v('kjopsum').value):'')+'.'
  }};

  const vissteNote = visste==='ja'
    ? `\\n\\nJeg gjør oppmerksom på at selgeren etter min vurdering kjente til mangelen ved salget, jf. ${{lovK}} § ${{selger==='forhandler'?'16':'33'}}. Reklamasjonsfristen gjelder ikke i slike tilfeller.`
    : '';

  const navn = v('mitt_navn').value || '[Ditt navn]';
  const tlf = v('mitt_tlf').value || '[Telefon]';
  const epost = v('min_epost').value || '[E-post]';
  const selgerNavn = v('selger_navn').value || '[Selgerens navn]';
  const bilBesk = v('bil_besk').value || '[bilbeskrivelse]';
  const feilBesk = v('feil_besk').value || '[beskriv mangelen]';
  const dagensDato = new Date().toLocaleDateString('nb-NO',{{day:'numeric',month:'long',year:'numeric'}});

  if (!selger) {{
    v('brev-tekst').textContent = 'Velg hvem du kjøpte bilen av for å starte.';
    return;
  }}

  const brev =
`${{navn}}
${{tlf}} | ${{epost}}

${{dagensDato}}

Til: ${{selgerNavn}}

REKLAMASJON — ${{bilBesk}}

Jeg kjøpte ${{bilBesk}} den ${{formDato(v('kjopsdato').value)}}${{v('kjopsum').value ? ' for ' + kr(v('kjopsum').value) : ''}}.

Den ${{formDato(v('oppdagelse').value)}} oppdaget jeg følgende mangel:
${{feilBesk}}

Mangelen forelå etter min vurdering på tidspunktet for risikoens overgang, jf. ${{lovK}} § ${{risiPara}}. Jeg reklamerer herved innen rimelig tid, jf. ${{lovK}} § ${{rekPara}}.${{vissteNote}}

${{kravTekster[krav] || '[Velg hva du vil kreve]'}}

Jeg ber om skriftlig svar innen 14 dager.

Med vennlig hilsen

${{navn}}
${{tlf}}
${{epost}}`;

  v('brev-tekst').textContent = brev;

  const harNokTilNeste = selger && feilBesk && feilBesk !== '[beskriv mangelen]' && krav;
  v('neste-steg').style.display = harNokTilNeste ? 'block' : 'none';
  if (harNokTilNeste) {{
    const kravSpesifikk = v('nsl-krav-spesifikk');
    if (krav==='heving') kravSpesifikk.textContent = 'Ikke bruk bilen mer enn nødvendig etter at du har hevet — det kan tolkes som aksept av situasjonen.';
    else if (selger==='forhandler') kravSpesifikk.textContent = 'Avviser forhandleren kravet? Klag til Forbrukerrådet (gratis) på forbrukerradet.no/klage.';
    else kravSpesifikk.textContent = 'Avviser selgeren kravet? Ta saken til Forliksrådet via Altinn — gebyret er 1 215 kr.';
  }}
}}

function kopier() {{
  const t = v('brev-tekst').textContent;
  navigator.clipboard.writeText(t).then(()=>{{
    const k = document.querySelector('.rek-brev-kopi');
    k.textContent='Kopiert ✓'; setTimeout(()=>k.textContent='Kopier',2000);
  }});
}}

oppdater();
</script>

{site_footer(depth=2)}"""




# ─────────────────────────────────────────────────────────────────────────────
# TJENESTE 1: REKLAMASJONSBREV (GENERELL)
# ─────────────────────────────────────────────────────────────────────────────
def render_tjenester_reklamasjon():
    return f"""{shared_head(
        'Reklamasjonsbrev — skriv klagen din gratis | Rettsregel',
        'Skriv et juridisk korrekt reklamasjonsbrev på sekunder. Fungerer for alle varer fra butikk eller netthandel. Basert på forbrukerkjøpsloven.',
        depth=2, canonical_path='/tjenester/reklamasjon/'
    )}
{site_nav(depth=2)}
<style>
.rek2-layout {{ display: grid; grid-template-columns: 380px 1fr; gap: 32px; align-items: start; margin-bottom: 64px; }}
.rek2-layout > * {{ min-width: 0; }}
@media (max-width: 1024px) {{ .rek2-layout {{ grid-template-columns: 1fr !important; }} }}
.rek2-skjema {{ background: var(--bg-card); border: 1px solid var(--line); border-radius: 20px; padding: 28px; box-shadow: var(--shadow-md); position: sticky; top: 24px; }}
@media (max-width: 1024px) {{ .rek2-skjema {{ position: static !important; }} }}
.rek2-sek {{ margin-bottom: 18px; border-bottom: 1px solid var(--line); padding-bottom: 18px; }}
.rek2-sek:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
.rek2-tittel {{ font-family: var(--serif); font-size: 18px; font-weight: 400; margin-bottom: 20px; }}
.rek2-sek-hd {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); margin-bottom: 10px; }}
.rf {{ margin-bottom: 10px; }}
.rf label {{ display: block; font-size: 12px; font-weight: 600; color: var(--ink-soft); margin-bottom: 4px; }}
.rf input, .rf select, .rf textarea {{
  width: 100%; padding: 9px 12px; border: 1.5px solid var(--line);
  border-radius: 8px; font-family: var(--sans); font-size: 16px;
  background: var(--bg); color: var(--ink); box-sizing: border-box;
}}
.rf input:focus, .rf select:focus, .rf textarea:focus {{ outline: none; border-color: var(--accent); }}
.rf textarea {{ min-height: 70px; resize: vertical; }}
.rf-radio {{ display: flex; flex-direction: column; gap: 6px; }}
.rf-radio label {{
  display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 500;
  cursor: pointer; padding: 8px 12px; border: 1.5px solid var(--line);
  border-radius: 8px; line-height: 1.35;
}}
.rf-radio input[type=radio] {{ width: auto; margin: 0; accent-color: var(--accent); flex-shrink: 0; }}
.rf-radio label:has(input:checked) {{ border-color: var(--accent); background: rgba(177,74,42,0.05); color: var(--accent); font-weight: 600; }}
.last-ned-kn {{ width: 100%; background: var(--accent); color: white; border: none; border-radius: 12px; font-family: var(--sans); font-size: 15px; font-weight: 600; padding: 15px; cursor: pointer; margin-top: 20px; transition: background 0.2s; }}
.last-ned-kn:hover {{ background: var(--accent-deep); }}
/* Status badge */
.rek2-status {{ padding: 10px 16px; border-radius: 10px; font-size: 13px; font-weight: 600; display: none; margin-bottom: 16px; }}
.rek2-status.ok {{ background: #e8f4e8; color: #2d6a2d; border: 1px solid #8dcc8d; }}
.rek2-status.advarsel {{ background: #fff3cd; color: #7d6008; border: 1px solid #ffc107; }}
.rek2-status.feil {{ background: #fde8e8; color: #8b2020; border: 1px solid #f0a0a0; }}
/* Dokument */
.brev-wrap {{ background: var(--bg-alt); border-radius: 16px; padding: 24px; border: 1px solid var(--line); }}
.brev-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }}
.brev-header h3 {{ font-family: var(--serif); font-size: 18px; font-weight: 400; margin: 0; }}
.brev-kn-rad {{ display: flex; gap: 10px; }}
.brev-kn {{ padding: 8px 16px; border-radius: 8px; font-family: var(--sans); font-size: 13px; font-weight: 600; cursor: pointer; border: none; }}
.brev-kn.kopier {{ background: var(--accent); color: white; }}
.brev-kn.skriv {{ background: var(--bg-card); border: 1.5px solid var(--line); color: var(--ink); }}
.brev-kn:hover {{ opacity: 0.85; }}
.brev-dokument {{ background: white; border-radius: 12px; padding: 36px 40px; font-family: 'EB Garamond', Georgia, serif; font-size: 16px; line-height: 1.8; color: var(--ink); border: 1px solid var(--line); min-height: 200px; }}
@media (max-width: 600px) {{ .brev-dokument {{ padding: 20px 16px; font-size: 15px; }} }}
.brev-tom {{ color: var(--ink-mute); font-style: italic; font-family: var(--sans); font-size: 14px; }}
.brev-lov-ref {{ font-size: 13px; color: var(--ink-mute); margin-top: 16px; padding-top: 12px; border-top: 1px solid var(--line); font-family: var(--sans); }}
@media print {{
  .no-print {{ display: none !important; }}
  nav.site-nav, footer.site-footer, #chat-toggle, #chat-panel, .breadcrumbs, .article-header, .rek2-skjema, .sp-body {{ display: none !important; }}
  .rek2-layout {{ display: block; }}
  .brev-wrap {{ border: none; padding: 0; background: white; }}
  .brev-dokument {{ border: none; padding: 0; box-shadow: none; }}
  body {{ background: white; }}
}}
</style>
<main class="page">
  <div class="container">
    <div class="breadcrumbs no-print">
      <a href="../../">Rettsregel</a><span class="sep">›</span>
      <a href="../../tjenester/">Tjenester</a><span class="sep">›</span>
      <span class="current">Reklamasjonsbrev</span>
    </div>
    <div class="article-header no-print">
      <div class="article-eyebrow">Gratis verktøy</div>
      <h1 class="article-title">Skriv reklamasjonsbrevet ditt</h1>
      <p class="article-description">Fyll ut om kjøpet og feilen. Brevet bygger seg live og er klart til å sende.</p>
    </div>
    <div class="rek2-layout">
      <div class="rek2-skjema no-print">
        <div class="rek2-tittel">Om kjøpet</div>
        <div class="rek2-sek">
          <div class="rek2-sek-hd">Hvem kjøpte du av?</div>
          <div class="rf">
            <div class="rf-radio">
              <label><input type="radio" name="selger_type" value="bedrift" onchange="oppdater()" checked> Butikk eller nettbutikk (bedrift)</label>
              <label><input type="radio" name="selger_type" value="privat" onchange="oppdater()"> Privatperson (Finn.no, bekjente)</label>
            </div>
          </div>
        </div>
        <div class="rek2-sek">
          <div class="rek2-sek-hd">Selgeren</div>
          <div class="rf"><label>Butikkens / selgerens navn</label><input type="text" id="selger_navn" oninput="oppdater()" placeholder="f.eks. Elkjøp / Kari Nordmann"></div>
          <div class="rf"><label>Adresse (hvis kjent)</label><input type="text" id="selger_adresse" oninput="oppdater()" placeholder="Storgata 1, 0000 Oslo"></div>
          <div class="rf"><label>E-post / kundeservice-adresse</label><input type="text" id="selger_epost" oninput="oppdater()" placeholder="kundeservice@butikk.no"></div>
        </div>
        <div class="rek2-sek">
          <div class="rek2-sek-hd">Varen og kjøpet</div>
          <div class="rf"><label>Hva kjøpte du?</label><input type="text" id="vare_navn" oninput="oppdater()" placeholder="f.eks. Samsung TV 55 tommer"></div>
          <div class="rf"><label>Kjøpsdato</label><input type="date" id="kjops_dato" oninput="oppdater()"></div>
          <div class="rf"><label>Betalt sum (kr)</label><input type="number" id="betalt_sum" oninput="oppdater()" placeholder="4990" min="0"></div>
          <div class="rf"><label>Ordrenummer / kvitteringsnummer (valgfritt)</label><input type="text" id="ordre_nr" oninput="oppdater()" placeholder="ORD-12345"></div>
        </div>
        <div class="rek2-sek">
          <div class="rek2-sek-hd">Feilen</div>
          <div class="rf"><label>Kategori</label>
            <select id="feil_kategori" onchange="oppdater()">
              <option value="">— Velg kategori —</option>
              <option value="stopper">Slutter å fungere / virker ikke</option>
              <option value="feil_info">Ikke som beskrevet i annonse eller på esken</option>
              <option value="mangler_deler">Mangler deler, tilbehør eller bruksanvisning</option>
              <option value="feil_montering">Feil montering eller installasjon av selger</option>
              <option value="kvalitet">Dårlig kvalitet, slitasje eller holdbarhet</option>
              <option value="annet">Annet</option>
            </select>
          </div>
          <div class="rf"><label>Beskriv feilen kort</label><textarea id="feil_beskrivelse" oninput="oppdater()" placeholder="f.eks. Skjermen ble svart etter 3 uker uten at jeg har utsatt den for støt eller fukt."></textarea></div>
          <div class="rf"><label>Når oppdaget du feilen?</label><input type="date" id="feil_dato" oninput="oppdater()"></div>
        </div>
        <div class="rek2-sek">
          <div class="rek2-sek-hd">Hva krever du?</div>
          <div class="rf">
            <div class="rf-radio">
              <label><input type="radio" name="krav" value="reparasjon" onchange="oppdater()" checked> Reparasjon (retting av feilen)</label>
              <label><input type="radio" name="krav" value="ny_vare" onchange="oppdater()"> Ny vare (omlevering)</label>
              <label><input type="radio" name="krav" value="heving" onchange="oppdater()"> Pengene tilbake (heving)</label>
              <label><input type="radio" name="krav" value="prisavslag" onchange="oppdater()"> Prisavslag</label>
            </div>
          </div>
        </div>
        <div class="rek2-sek">
          <div class="rek2-sek-hd">Dine opplysninger</div>
          <div class="rf"><label>Ditt fulle navn</label><input type="text" id="mitt_navn" oninput="oppdater()" placeholder="Ola Nordmann"></div>
          <div class="rf"><label>Din adresse</label><input type="text" id="min_adresse" oninput="oppdater()" placeholder="Veien 5, 5000 Bergen"></div>
          <div class="rf"><label>Din e-post</label><input type="text" id="min_epost" oninput="oppdater()" placeholder="ola@epost.no"></div>
          <div class="rf"><label>Din telefon</label><input type="text" id="min_tlf" oninput="oppdater()" placeholder="900 00 000"></div>
        </div>
        <button class="last-ned-kn no-print" onclick="window.print()">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="display:inline;vertical-align:middle;margin-right:6px"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7,10 12,15 17,10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Last ned som PDF
        </button>
      </div>
      <div>
        <div class="rek2-status" id="rek2-status"></div>
        <div class="brev-wrap">
          <div class="brev-header">
            <h3>Ditt reklamasjonsbrev</h3>
            <div class="brev-kn-rad no-print">
              <button class="brev-kn kopier" onclick="kopierBrev()">Kopier tekst</button>
              <button class="brev-kn skriv" onclick="window.print()">Last ned PDF</button>
            </div>
          </div>
          <div class="brev-dokument" id="brev-innhold"><p class="brev-tom">Fyll ut feltene til venstre — brevet bygger seg her.</p></div>
          <div class="brev-lov-ref" id="brev-lov-ref"></div>
        </div>
      </div>
    </div>
    <div class="prose sp-body no-print">
      <h2>Hvordan reklamerer du?</h2>
      <p>Reklamasjon betyr at du sier ifra til selgeren om en feil ved varen. Du har alltid minst to måneder fra du oppdaget feilen til å klage. For varige varer (TV, bil, hvitevarer, telefon) har du fem år på deg totalt.</p>
      <p>Send brevet på e-post slik at du har bevis med dato og klokkeslett. Be om lesebekreftelse. Ta vare på e-posten i «Sendt»-mappen.</p>
      <p>Kjøpte du av en butikk? Da gjelder forbrukerkjøpsloven og du har sterke rettigheter. Kjøpte du av en privatperson? Da gjelder kjøpsloven, som gir noe færre rettigheter.</p>
    </div>
  </div>
</main>
<script>
function dato(iso) {{
  if (!iso) return '________';
  return new Date(iso+'T12:00:00').toLocaleDateString('nb-NO', {{day:'numeric',month:'long',year:'numeric'}});
}}
function kr(n) {{
  const num = parseInt(n);
  if (!num) return '';
  return num.toLocaleString('nb-NO') + ' kr';
}}
function radio(name) {{
  const el = document.querySelector('input[name="'+name+'"]:checked');
  return el ? el.value : null;
}}
function beregnFristStatus() {{
  const kjopsStr = document.getElementById('kjops_dato').value;
  const feilStr = document.getElementById('feil_dato').value;
  if (!kjopsStr) return null;
  const kjops = new Date(kjopsStr);
  const feil = feilStr ? new Date(feilStr) : new Date();
  const naa = new Date();
  const aar5 = new Date(kjops); aar5.setFullYear(aar5.getFullYear()+5);
  const aar2 = new Date(kjops); aar2.setFullYear(aar2.getFullYear()+2);
  const maaneder2 = new Date(feil); maaneder2.setMonth(maaneder2.getMonth()+2);
  if (naa > aar5) return 'foreldet5';
  if (naa > aar2) return 'aar2_5'; // possible for varige
  if (naa > maaneder2) return 'for_sent_relativ';
  return 'ok';
}}
function oppdater() {{
  const selgerType = radio('selger_type') || 'bedrift';
  const selgerNavn = document.getElementById('selger_navn').value.trim();
  const selgerAdresse = document.getElementById('selger_adresse').value.trim();
  const selgerEpost = document.getElementById('selger_epost').value.trim();
  const vareNavn = document.getElementById('vare_navn').value.trim();
  const kjopsDato = document.getElementById('kjops_dato').value;
  const betaltSum = document.getElementById('betalt_sum').value;
  const ordreNr = document.getElementById('ordre_nr').value.trim();
  const feilKat = document.getElementById('feil_kategori').value;
  const feilBesk = document.getElementById('feil_beskrivelse').value.trim();
  const feilDato = document.getElementById('feil_dato').value;
  const krav = radio('krav') || 'reparasjon';
  const mittNavn = document.getElementById('mitt_navn').value.trim();
  const minAdresse = document.getElementById('min_adresse').value.trim();
  const minEpost = document.getElementById('min_epost').value.trim();
  const minTlf = document.getElementById('min_tlf').value.trim();
  const erBedrift = selgerType === 'bedrift';
  const lov = erBedrift ? 'forbrukerkjøpsloven' : 'kjøpsloven';

  // Status
  const statusEl = document.getElementById('rek2-status');
  if (kjopsDato) {{
    const fristStatus = beregnFristStatus();
    if (fristStatus === 'foreldet5') {{
      statusEl.className = 'rek2-status feil'; statusEl.style.display='block';
      statusEl.textContent = '⚠️ Varen ble kjøpt for mer enn 5 år siden. Reklamasjonsretten er sannsynligvis utløpt.';
    }} else if (fristStatus === 'for_sent_relativ') {{
      statusEl.className = 'rek2-status advarsel'; statusEl.style.display='block';
      statusEl.textContent = '⚠️ Det er mer enn 2 måneder siden du oppdaget feilen. Du bør sende klagen snarest og argumentere for at du handlet innen rimelig tid.';
    }} else if (fristStatus === 'ok') {{
      statusEl.className = 'rek2-status ok'; statusEl.style.display='block';
      statusEl.textContent = '✓ Klagen er innenfor reklamasjonsfristen. Du er i tide.';
    }} else {{ statusEl.style.display='none'; }}
  }} else {{ statusEl.style.display='none'; }}

  // Krav-tekst
  const kravMap = {{
    reparasjon: 'jeg krever at feilen rettes (reparasjon) innen rimelig tid, og uten kostnad for meg, jf. ' + (erBedrift ? 'forbrukerkjøpsloven § 29 og § 30' : 'kjøpsloven § 34'),
    ny_vare: 'jeg krever at tingen byttes ut med en tilsvarende ny vare (omlevering), jf. ' + (erBedrift ? 'forbrukerkjøpsloven § 29' : 'kjøpsloven § 34'),
    heving: 'jeg hever kjøpet og krever kjøpesummen refundert i sin helhet, jf. ' + (erBedrift ? 'forbrukerkjøpsloven § 32' : 'kjøpsloven § 39'),
    prisavslag: 'jeg krever et prisavslag som gjenspeiler verditapet feilen har påført tingen, jf. ' + (erBedrift ? 'forbrukerkjøpsloven § 31' : 'kjøpsloven § 38'),
  }};
  const feilKatMap = {{
    stopper: 'Tingen slutter å fungere / virker ikke',
    feil_info: 'Tingen samsvarer ikke med opplysningene i markedsføringen eller på innpakningen',
    mangler_deler: 'Tingen mangler deler, tilbehør eller bruksanvisning som følger av avtalen',
    feil_montering: 'Feilen skyldes uriktig installering/montering utført av selger',
    kvalitet: 'Tingen holder ikke den standarden man med rimelighet kan forvente',
    annet: 'Annet',
  }};

  if (!mittNavn && !selgerNavn && !vareNavn) {{
    document.getElementById('brev-innhold').innerHTML = '<p class="brev-tom">Fyll ut feltene til venstre — brevet bygger seg her.</p>';
    document.getElementById('brev-lov-ref').innerHTML = '';
    return;
  }}

  const idag = new Date().toLocaleDateString('nb-NO', {{day:'numeric',month:'long',year:'numeric'}});
  let brev = '';
  // Avsender
  brev += `<div style="margin-bottom:24px;font-size:14px;">`;
  if (mittNavn) brev += `<strong>${{mittNavn}}</strong><br>`;
  if (minAdresse) brev += `${{minAdresse}}<br>`;
  if (minEpost) brev += `${{minEpost}}<br>`;
  if (minTlf) brev += `${{minTlf}}<br>`;
  brev += `</div>`;
  // Mottaker
  brev += `<div style="margin-bottom:24px;font-size:14px;">`;
  if (selgerNavn) brev += `<strong>${{selgerNavn}}</strong><br>`;
  if (selgerAdresse) brev += `${{selgerAdresse}}<br>`;
  if (selgerEpost) brev += `${{selgerEpost}}<br>`;
  brev += `</div>`;
  // Dato
  brev += `<div style="margin-bottom:24px;font-size:14px;">${{idag}}</div>`;
  // Tittel
  brev += `<div style="font-weight:700;font-size:17px;margin-bottom:20px;font-family:var(--sans);">REKLAMASJON${{ordreNr ? ' — ' + ordreNr : ''}}</div>`;
  // Innledning
  brev += `<p>`;
  if (mittNavn && selgerNavn) brev += `Jeg, ${{mittNavn}}, reklamerer herved på følgende kjøp hos ${{selgerNavn}}.`;
  else if (mittNavn) brev += `Jeg, ${{mittNavn}}, reklamerer herved på følgende kjøp.`;
  else brev += `Jeg reklamerer herved på følgende kjøp.`;
  brev += `</p>`;
  // Kjøpsinfo
  brev += `<p style="margin-top:16px;"><strong>Vare:</strong> ${{vareNavn || '[vare ikke angitt]'}}<br>`;
  if (kjopsDato) brev += `<strong>Kjøpsdato:</strong> ${{dato(kjopsDato)}}<br>`;
  if (betaltSum) brev += `<strong>Kjøpesum:</strong> ${{kr(betaltSum)}}<br>`;
  if (ordreNr) brev += `<strong>Ordrenr.:</strong> ${{ordreNr}}<br>`;
  brev += `</p>`;
  // Feil
  brev += `<p style="margin-top:16px;"><strong>Mangel:</strong> `;
  if (feilKat) brev += feilKatMap[feilKat] + '.';
  if (feilBesk) brev += `<br><br>${{feilBesk}}`;
  if (feilDato) brev += `<br><br>Feilen ble oppdaget ${{dato(feilDato)}}.`;
  brev += `</p>`;
  // Krav
  brev += `<p style="margin-top:16px;">På denne bakgrunn, ${{kravMap[krav] || 'krever jeg utbedring'}}.</p>`;
  // Juridisk forankring
  if (erBedrift) {{
    brev += `<p style="margin-top:16px;">Jeg gjør gjeldende mine rettigheter etter forbrukerkjøpsloven. `;
    brev += `Feilen formodes å ha eksistert ved leveringen, jf. forbrukerkjøpsloven § 18. `;
    if (krav === 'heving') brev += `Jeg minner om at selgeren har bevisbyrden for at mangelen er uvesentlig, jf. § 32. `;
    brev += `Klagen fremsettes innen rimelig tid etter at feilen ble oppdaget, jf. § 27.</p>`;
  }} else {{
    brev += `<p style="margin-top:16px;">Jeg gjør gjeldende mine rettigheter etter kjøpsloven, som gjelder ved privatpersoners salg til privatpersoner.</p>`;
  }}
  // Frist
  brev += `<p style="margin-top:16px;">Jeg ber om tilbakemelding innen <strong>14 dager</strong> fra dags dato.</p>`;
  // Avslutning
  brev += `<div style="margin-top:32px;">`;
  brev += `Med vennlig hilsen<br><br>`;
  if (mittNavn) brev += `<strong>${{mittNavn}}</strong>`;
  brev += `</div>`;

  document.getElementById('brev-innhold').innerHTML = brev;
  const lovRef = erBedrift
    ? '⚖️ Lovgrunnlag: Forbrukerkjøpsloven §§ 15, 16, 18, 27' + (krav==='reparasjon'?' og 29–30':krav==='ny_vare'?' og 29':krav==='heving'?' og 32':krav==='prisavslag'?' og 31':'')
    : '⚖️ Lovgrunnlag: Kjøpsloven §§ 17, 30–33';
  document.getElementById('brev-lov-ref').textContent = lovRef;
}}
function kopierBrev() {{
  const el = document.getElementById('brev-innhold');
  const txt = el.innerText;
  navigator.clipboard.writeText(txt).then(() => {{
    const kn = document.querySelector('.brev-kn.kopier');
    kn.textContent = '✓ Kopiert!';
    setTimeout(() => kn.textContent = 'Kopier tekst', 2500);
  }});
}}
oppdater();
</script>
{site_footer(depth=2)}"""


# ─────────────────────────────────────────────────────────────────────────────
# TJENESTE 2: ARVEOPPGJØR KALKULATOR
# ─────────────────────────────────────────────────────────────────────────────
def render_tjenester_arv():
    return f"""{shared_head(
        'Arveoppgjør — hvem arver hva? | Rettsregel',
        'Beregn arvefordeling etter norsk arvelov. Se hvem som arver hva basert på familiesituasjon, ektefelle, samboer, barn og testament.',
        depth=2, canonical_path='/tjenester/arv/'
    )}
{site_nav(depth=2)}
<style>
.arv-layout {{ display: grid; grid-template-columns: 360px 1fr; gap: 32px; align-items: start; margin-bottom: 64px; }}
.arv-layout > * {{ min-width: 0; }}
@media (max-width: 1024px) {{ .arv-layout {{ grid-template-columns: 1fr !important; }} }}
.arv-skjema {{ background: var(--bg-card); border: 1px solid var(--line); border-radius: 20px; padding: 28px; box-shadow: var(--shadow-md); position: sticky; top: 24px; }}
@media (max-width: 1024px) {{ .arv-skjema {{ position: static !important; }} }}
.arv-tittel {{ font-family: var(--serif); font-size: 18px; font-weight: 400; margin-bottom: 20px; }}
.arv-sek {{ margin-bottom: 18px; border-bottom: 1px solid var(--line); padding-bottom: 18px; }}
.arv-sek:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
.arv-sek-hd {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); margin-bottom: 10px; }}
.af {{ margin-bottom: 10px; }}
.af label {{ display: block; font-size: 12px; font-weight: 600; color: var(--ink-soft); margin-bottom: 4px; }}
.af input, .af select {{ width: 100%; padding: 9px 12px; border: 1.5px solid var(--line); border-radius: 8px; font-family: var(--sans); font-size: 16px; background: var(--bg); color: var(--ink); box-sizing: border-box; }}
.af input:focus, .af select:focus {{ outline: none; border-color: var(--accent); }}
.af-radio {{ display: flex; flex-direction: column; gap: 6px; }}
.af-radio label {{ display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 500; cursor: pointer; padding: 8px 12px; border: 1.5px solid var(--line); border-radius: 8px; }}
.af-radio input[type=radio] {{ width: auto; margin: 0; accent-color: var(--accent); flex-shrink: 0; }}
.af-radio label:has(input:checked) {{ border-color: var(--accent); background: rgba(177,74,42,0.05); color: var(--accent); font-weight: 600; }}
/* Resultat */
.arv-res-wrap {{ display: none; }}
.arv-tom {{ color: var(--ink-mute); font-style: italic; font-family: var(--sans); font-size: 14px; padding: 32px 0; text-align: center; }}
/* Arv-kort (én per arving) */
.arving-grid {{ display: flex; flex-direction: column; gap: 16px; }}
.arving-kort {{ border-radius: 16px; overflow: hidden; border: 1px solid var(--line); }}
.arving-header {{ display: flex; justify-content: space-between; align-items: center; padding: 16px 20px; }}
.arving-rolle {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; opacity: 0.8; }}
.arving-navn {{ font-family: var(--serif); font-size: 19px; font-weight: 400; }}
.arving-prosent {{ font-family: var(--serif); font-size: 28px; font-weight: 400; }}
.arving-sum {{ font-size: 13px; font-weight: 600; opacity: 0.8; }}
.arving-bar-wrap {{ height: 6px; background: rgba(0,0,0,0.1); }}
.arving-bar {{ height: 100%; transition: width 0.4s ease; }}
.arving-detaljer {{ padding: 12px 20px 16px; background: rgba(255,255,255,0.6); border-top: 1px solid rgba(0,0,0,0.06); }}
.arving-detaljer p {{ font-size: 13px; line-height: 1.5; margin: 0; color: var(--ink-soft); }}
/* Farger per arving */
.arv-color-0 {{ background: #e8f4f0; }} .arv-color-0 .arving-bar {{ background: #2d7a5e; }}
.arv-color-1 {{ background: #e8eef4; }} .arv-color-1 .arving-bar {{ background: #2d5a8a; }}
.arv-color-2 {{ background: #f4f0e8; }} .arv-color-2 .arving-bar {{ background: #8a6b2d; }}
.arv-color-3 {{ background: #f0e8f4; }} .arv-color-3 .arving-bar {{ background: #6b2d8a; }}
.arv-color-4 {{ background: #f4e8e8; }} .arv-color-4 .arving-bar {{ background: #8a2d2d; }}
/* Info-boks */
.arv-info {{ background: var(--bg-alt); border: 1px solid var(--line); border-radius: 14px; padding: 20px; margin-top: 20px; }}
.arv-info h4 {{ font-size: 14px; font-weight: 700; margin-bottom: 8px; }}
.arv-info p {{ font-size: 13px; line-height: 1.6; color: var(--ink-soft); margin: 0; }}
.arv-merk {{ font-size: 12px; color: var(--ink-mute); margin-top: 16px; font-family: var(--sans); padding: 12px; border-top: 1px solid var(--line); }}
</style>
<main class="page">
  <div class="container">
    <div class="breadcrumbs no-print">
      <a href="../../">Rettsregel</a><span class="sep">›</span>
      <a href="../../tjenester/">Tjenester</a><span class="sep">›</span>
      <span class="current">Arveoppgjør</span>
    </div>
    <div class="article-header no-print">
      <div class="article-eyebrow">Kalkulator</div>
      <h1 class="article-title">Hvem arver hva?</h1>
      <p class="article-description">Fyll ut familiesituasjon og formue. Kalkulatoren viser arvefordelingen etter norsk arvelov — live.</p>
    </div>
    <div class="arv-layout">
      <div class="arv-skjema no-print">
        <div class="arv-tittel">Beskriv situasjonen</div>
        <div class="arv-sek">
          <div class="arv-sek-hd">Sivilstatus</div>
          <div class="af">
            <div class="af-radio">
              <label><input type="radio" name="sivil" value="gift" onchange="oppdater()" checked> Gift</label>
              <label><input type="radio" name="sivil" value="samboer" onchange="oppdater()"> Samboer (registrert / felles barn)</label>
              <label><input type="radio" name="sivil" value="enslig" onchange="oppdater()"> Enslig (aldri gift, ingen samboer)</label>
              <label><input type="radio" name="sivil" value="skilt" onchange="oppdater()"> Skilt / separert</label>
            </div>
          </div>
        </div>
        <div class="arv-sek">
          <div class="arv-sek-hd">Barn</div>
          <div class="af"><label>Felles barn (med ektefelle/samboer)</label>
            <select id="felles_barn" onchange="oppdater()">
              <option value="0">Ingen felles barn</option><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5 eller flere</option>
            </select>
          </div>
          <div class="af"><label>Særkullsbarn (fra tidligere forhold)</label>
            <select id="saerkull_barn" onchange="oppdater()">
              <option value="0">Ingen særkullsbarn</option><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5 eller flere</option>
            </select>
          </div>
        </div>
        <div class="arv-sek">
          <div class="arv-sek-hd">Testament</div>
          <div class="af">
            <div class="af-radio">
              <label><input type="radio" name="testament" value="nei" onchange="oppdater()" checked> Ingen testament</label>
              <label><input type="radio" name="testament" value="ja" onchange="oppdater()"> Har testament</label>
            </div>
          </div>
          <div id="testament-info" style="display:none;margin-top:8px;font-size:12px;color:var(--ink-mute);padding:10px;background:var(--bg-alt);border-radius:8px;">Med testament kan du fritt fordele det som overstiger pliktarven til barna (2/3 av boet, min 15G per barn ≈ 1,8 mill kr). Ektefelle/samboer kan styrkes, men barn kan ikke arve under sin pliktarv.</div>
        </div>
        <div class="arv-sek">
          <div class="arv-sek-hd">Formue</div>
          <div class="af"><label>Estimert nettoverdi av boet (kr)</label><input type="number" id="formue" oninput="oppdater()" placeholder="f.eks. 3000000" min="0"></div>
          <div style="font-size:12px;color:var(--ink-mute);margin-top:4px;">Tips: Legg sammen bolig, hytte, bil, bankkonto, aksjer. Trekk fra gjeld og begravelsesutgifter.</div>
        </div>
      </div>
      <div>
        <div id="arv-tom" class="arv-tom">Fyll ut situasjonen til venstre — arvefordelingen beregnes her.</div>
        <div class="arv-res-wrap" id="arv-res">
          <div class="arving-grid" id="arving-grid"></div>
          <div class="arv-info" id="arv-info"></div>
          <div class="arv-merk">⚠️ Forenklet beregning etter arveloven av 2021. Tar ikke hensyn til ektepakt, samboeravtale, livsforsikring, særeie eller andre særlige forhold. Rådgivning fra advokat anbefales ved komplekse situasjoner.</div>
        </div>
      </div>
    </div>
    <div class="prose sp-body no-print">
      <h2>Grunnreglene i arveloven</h2>
      <p>Norsk arvelov av 2021 gir ektefellen rett til minst en firedel av arven, men aldri under 4G (ca. 500 000 kr). Barn arver likt seg imellom, begrenset oppad til pliktarven. Særkullsbarn har krav på sin pliktarv umiddelbart — de kan ikke holdes tilbake av uskiftet bo.</p>
      <p>Samboere med felles barn eller registrert samboerskap har rett til 4G fra arven. Uten felles barn: ingenting, med mindre det er testament.</p>
      <p>Testament kan endre fordelingen, men aldri krenke pliktarven til barna (2/3 av boet, minimum 15G per barn).</p>
    </div>
  </div>
</main>
<script>
const G = 124028; // Grunnbeløp 2026 (ca.)
function radio(name) {{
  const el = document.querySelector('input[name="'+name+'"]:checked');
  return el ? el.value : null;
}}
function kr(n) {{
  return Math.round(n).toLocaleString('nb-NO') + ' kr';
}}
function pst(andel, total) {{
  if (!total) return '—';
  return Math.round(andel/total*100) + ' %';
}}
function oppdater() {{
  const sivil = radio('sivil') || 'enslig';
  const fellesBarn = parseInt(document.getElementById('felles_barn').value) || 0;
  const saerkullBarn = parseInt(document.getElementById('saerkull_barn').value) || 0;
  const harTestament = radio('testament') === 'ja';
  const formue = parseFloat(document.getElementById('formue').value) || 0;
  const totalBarn = fellesBarn + saerkullBarn;
  document.getElementById('testament-info').style.display = harTestament ? 'block' : 'none';

  let arvinger = [];
  let info = '';

  if (sivil === 'gift') {{
    const minEktefelle = Math.max(formue * 0.25, 4 * G);
    if (totalBarn === 0) {{
      // Ektefelle arver alt
      arvinger = [{{rolle:'Ektefelle', andel: formue, info:'Arver hele boet når det ikke finnes barn, jf. arveloven § 9.'}}];
      info = 'Ingen barn: Ektefellen arver alt.';
    }} else {{
      let ektefellesAndel, resttilBarn;
      if (saerkullBarn === 0) {{
        // Kan sitte i uskiftet bo med fellesbarn
        ektefellesAndel = Math.max(formue * 0.25, 4 * G);
        ektefellesAndel = Math.min(ektefellesAndel, formue);
        resttilBarn = Math.max(0, formue - ektefellesAndel);
        const perFellesbarn = fellesBarn > 0 ? resttilBarn / fellesBarn : 0;
        arvinger.push({{rolle:'Ektefelle', andel: ektefellesAndel, info:'Minstearv ¼ av boet, min 4G ('+kr(4*G)+'). Kan velge uskiftet bo med fellesbarna.'}});
        for (let i = 0; i < Math.min(fellesBarn, 4); i++) {{
          arvinger.push({{rolle:'Fellesbarn '+(i+1), andel: perFellesbarn, info:'Arver likt med sine søsken. Kan skyves ut dersom ektefellen velger uskiftet bo.'}});
        }}
        if (fellesBarn > 4) arvinger.push({{rolle:'Fellesbarn 5+', andel: perFellesbarn * (fellesBarn - 4), info:'Resterende fellesbarn.'}});
        info = 'Ektefellen kan velge uskiftet bo med fellesbarna — det vil si skifte utsettes til ektefellen dør. Særkullsbarna (ingen her) har krav på sin arv med en gang.';
      }} else {{
        // Særkullsbarn kan ikke utsettes
        const saerkullAndel = formue / (totalBarn + 0.25) * saerkullBarn;
        ektefellesAndel = Math.max(formue * 0.25, 4 * G);
        ektefellesAndel = Math.min(ektefellesAndel, formue - saerkullAndel * 0.5);
        resttilBarn = Math.max(0, formue - ektefellesAndel);
        const perBarn = totalBarn > 0 ? resttilBarn / totalBarn : 0;
        arvinger.push({{rolle:'Ektefelle', andel: ektefellesAndel, info:'Minstearv ¼ av boet, min 4G. Kan ikke sitte i uskiftet bo — særkullsbarna krever sitt med én gang.'}});
        for (let i = 0; i < Math.min(saerkullBarn, 3); i++) {{
          arvinger.push({{rolle:'Særkullsbarn '+(i+1), andel: perBarn, info:'Arver likt med søsken. Krever sitt nå — kan ikke vente til ektefellens død.'}});
        }}
        for (let i = 0; i < Math.min(fellesBarn, 3); i++) {{
          arvinger.push({{rolle:'Fellesbarn '+(i+1), andel: perBarn, info:'Arver likt med søsken.'}});
        }}
        if (saerkullBarn + fellesBarn > 6) arvinger.push({{rolle:'Øvrige barn', andel: perBarn * (totalBarn - Math.min(saerkullBarn,3) - Math.min(fellesBarn,3)), info:''}});
        info = '⚠️ Særkullsbarn krever sin arv umiddelbart. Ektefellen kan IKKE velge uskiftet bo uten særkullsbarnas samtykke.';
      }}
    }}
  }} else if (sivil === 'samboer') {{
    const samboerArv = Math.min(4 * G, formue);
    const resttilBarn = Math.max(0, formue - samboerArv);
    const perBarn = totalBarn > 0 ? resttilBarn / totalBarn : 0;
    if (totalBarn === 0) {{
      arvinger = [{{rolle:'Samboer', andel: formue, info:'Arver alt når det ikke finnes barn — forutsatt felles barn eller registrert samboerskap, jf. arveloven § 13.'}}];
      info = harTestament ? 'Med testament kan samboeren tilgodeses ytterligere.' : 'Samboer med felles barn eller registrert samboerskap arver 4G.';
    }} else {{
      arvinger.push({{rolle:'Samboer', andel: samboerArv, info:'Rett til 4G ('+kr(4*G)+') forutsatt felles barn eller registrert samboerskap, jf. arveloven § 13.'}});
      for (let i = 0; i < Math.min(totalBarn, 4); i++) {{
        arvinger.push({{rolle:'Barn '+(i+1), andel: perBarn, info:'Arver likt med søsken etter at samboerens minstearv er trukket.'}});
      }}
      if (totalBarn > 4) arvinger.push({{rolle:'Øvrige barn', andel: perBarn*(totalBarn-4), info:''}});
      info = 'Samboer uten felles barn eller registrert samboerskap arver ingenting etter loven — kun testament hjelper.';
    }}
  }} else {{
    // Enslig/skilt
    if (totalBarn > 0) {{
      const perBarn = formue / totalBarn;
      for (let i = 0; i < Math.min(totalBarn, 5); i++) {{
        arvinger.push({{rolle:'Barn '+(i+1), andel: perBarn, info:'Arver likt med sine søsken, jf. arveloven § 6.'}});
      }}
      if (totalBarn > 5) arvinger.push({{rolle:'Øvrige barn', andel: perBarn*(totalBarn-5), info:''}});
      info = 'Ingen ektefelle/samboer: Barna arver alt, likt fordelt.';
    }} else {{
      arvinger = [{{rolle:'Foreldre', andel: formue * 0.5, info:'Deler likt, jf. arveloven § 10.'}}, {{rolle:'Søsken / søskens etterkommere', andel: formue * 0.5, info:'Arver hvis en forelder er død.'}}];
      info = 'Ingen barn: Foreldrene arver likt. Er de døde, arver søsken.';
    }}
  }}

  if (arvinger.length === 0) {{
    document.getElementById('arv-tom').style.display = 'block';
    document.getElementById('arv-res').style.display = 'none';
    return;
  }}
  document.getElementById('arv-tom').style.display = 'none';
  document.getElementById('arv-res').style.display = 'block';

  const total = arvinger.reduce((s,a)=>s+a.andel, 0) || formue || 1;
  const grid = document.getElementById('arving-grid');
  grid.innerHTML = arvinger.map((a,i) => {{
    const pstTall = Math.round(a.andel/total*100);
    const sumTekst = formue > 0 ? kr(a.andel) : '';
    return `<div class="arving-kort arv-color-${{i%5}}">
      <div class="arving-header">
        <div><div class="arving-rolle">${{a.rolle}}</div></div>
        <div style="text-align:right"><div class="arving-prosent">${{pstTall}} %</div>${{sumTekst ? '<div class="arving-sum">'+sumTekst+'</div>' : ''}}</div>
      </div>
      <div class="arving-bar-wrap"><div class="arving-bar" style="width:${{pstTall}}%"></div></div>
      <div class="arving-detaljer"><p>${{a.info}}</p></div>
    </div>`;
  }}).join('');
  document.getElementById('arv-info').innerHTML = info ? `<h4>Viktig å vite</h4><p>${{info}}</p>` : '';
}}
oppdater();
</script>
{site_footer(depth=2)}"""


# ─────────────────────────────────────────────────────────────────────────────
# TJENESTE 3: LEIEØKNING KALKULATOR
# ─────────────────────────────────────────────────────────────────────────────
def render_tjenester_leie_okning():
    return f"""{shared_head(
        'Leieøkning-kalkulator — beregn maks leieøkning og skriv varsel | Rettsregel',
        'Beregn maksimal lovlig leieøkning etter KPI og husleieloven § 4-2. Gratis varselbrev som du kan sende direkte til leietaker.',
        depth=2, canonical_path='/tjenester/leie-okning/'
    )}
{site_nav(depth=2)}
<style>
.lo-layout {{ display: grid; grid-template-columns: 380px 1fr; gap: 32px; align-items: start; margin-bottom: 64px; }}
.lo-layout > * {{ min-width: 0; }}
@media (max-width: 1024px) {{ .lo-layout {{ grid-template-columns: 1fr !important; }} }}
.lo-skjema {{ background: var(--bg-card); border: 1px solid var(--line); border-radius: 20px; padding: 28px; box-shadow: var(--shadow-md); position: sticky; top: 24px; }}
@media (max-width: 1024px) {{ .lo-skjema {{ position: static !important; }} }}
.lo-tittel {{ font-family: var(--serif); font-size: 18px; font-weight: 400; margin-bottom: 20px; }}
.lo-sek {{ margin-bottom: 18px; border-bottom: 1px solid var(--line); padding-bottom: 18px; }}
.lo-sek:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
.lo-sek-hd {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); margin-bottom: 10px; }}
.lf {{ margin-bottom: 10px; }}
.lf label {{ display: block; font-size: 12px; font-weight: 600; color: var(--ink-soft); margin-bottom: 4px; }}
.lf input {{ width: 100%; padding: 9px 12px; border: 1.5px solid var(--line); border-radius: 8px; font-family: var(--sans); font-size: 16px; background: var(--bg); color: var(--ink); box-sizing: border-box; }}
.lf input:focus {{ outline: none; border-color: var(--accent); }}
.last-ned-kn {{ width: 100%; background: var(--accent); color: white; border: none; border-radius: 12px; font-family: var(--sans); font-size: 15px; font-weight: 600; padding: 15px; cursor: pointer; margin-top: 20px; transition: background 0.2s; }}
.last-ned-kn:hover {{ background: var(--accent-deep); }}
/* Resultat-display */
.lo-res-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 24px; }}
@media (max-width: 600px) {{ .lo-res-grid {{ grid-template-columns: 1fr; }} }}
.lo-res-kort {{ background: var(--bg-card); border: 1px solid var(--line); border-radius: 16px; padding: 20px; }}
.lo-res-kort .lo-res-label {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--ink-mute); margin-bottom: 6px; }}
.lo-res-kort .lo-res-val {{ font-family: var(--serif); font-size: 28px; font-weight: 400; color: var(--accent); }}
.lo-res-kort .lo-res-sub {{ font-size: 12px; color: var(--ink-mute); margin-top: 4px; }}
.lo-res-kort.groen .lo-res-val {{ color: #2d6a2d; }}
/* Brev */
.brev-wrap {{ background: var(--bg-alt); border-radius: 16px; padding: 24px; border: 1px solid var(--line); }}
.brev-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }}
.brev-header h3 {{ font-family: var(--serif); font-size: 18px; font-weight: 400; margin: 0; }}
.brev-kn-rad {{ display: flex; gap: 10px; }}
.brev-kn {{ padding: 8px 16px; border-radius: 8px; font-family: var(--sans); font-size: 13px; font-weight: 600; cursor: pointer; border: none; }}
.brev-kn.kopier {{ background: var(--accent); color: white; }}
.brev-kn.skriv {{ background: var(--bg-card); border: 1.5px solid var(--line); color: var(--ink); }}
.brev-dokument {{ background: white; border-radius: 12px; padding: 36px 40px; font-family: 'EB Garamond', Georgia, serif; font-size: 16px; line-height: 1.8; color: var(--ink); border: 1px solid var(--line); }}
@media (max-width: 600px) {{ .brev-dokument {{ padding: 20px 16px; font-size: 15px; }} }}
.brev-tom {{ color: var(--ink-mute); font-style: italic; font-family: var(--sans); font-size: 14px; }}
@media print {{
  .no-print {{ display: none !important; }}
  nav.site-nav, footer.site-footer, #chat-toggle, #chat-panel, .breadcrumbs, .article-header, .lo-skjema, .sp-body, .lo-res-grid {{ display: none !important; }}
  .lo-layout {{ display: block; }}
  .brev-wrap {{ border: none; padding: 0; background: white; }}
  .brev-dokument {{ border: none; padding: 0; box-shadow: none; }}
  body {{ background: white; }}
}}
</style>
<main class="page">
  <div class="container">
    <div class="breadcrumbs no-print">
      <a href="../../">Rettsregel</a><span class="sep">›</span>
      <a href="../../tjenester/">Tjenester</a><span class="sep">›</span>
      <span class="current">Leieøkning</span>
    </div>
    <div class="article-header no-print">
      <div class="article-eyebrow">Kalkulator + varselbrev</div>
      <h1 class="article-title">Leieøkning — beregn og varsle</h1>
      <p class="article-description">Fyll ut nåværende leie og KPI-endring. Du får maks lovlig økning og et ferdig varselbrev til leietaker.</p>
    </div>
    <div class="lo-layout">
      <div class="lo-skjema no-print">
        <div class="lo-tittel">Leieforholdet</div>
        <div class="lo-sek">
          <div class="lo-sek-hd">Utleier</div>
          <div class="lf"><label>Ditt navn (utleier)</label><input type="text" id="utleier_navn" oninput="oppdater()" placeholder="Ola Nordmann"></div>
          <div class="lf"><label>Din adresse</label><input type="text" id="utleier_adresse" oninput="oppdater()" placeholder="Storgata 1, 0000 Oslo"></div>
        </div>
        <div class="lo-sek">
          <div class="lo-sek-hd">Leietaker</div>
          <div class="lf"><label>Leietakers navn</label><input type="text" id="leietaker_navn" oninput="oppdater()" placeholder="Kari Nordmann"></div>
          <div class="lf"><label>Leieobjektets adresse</label><input type="text" id="bolig_adresse" oninput="oppdater()" placeholder="Leiegata 5, 5000 Bergen"></div>
        </div>
        <div class="lo-sek">
          <div class="lo-sek-hd">Leie og tidspunkt</div>
          <div class="lf"><label>Nåværende månedlig leie (kr)</label><input type="number" id="naaleie" oninput="oppdater()" placeholder="12000" min="0"></div>
          <div class="lf"><label>Dato for siste leieøkning (eller leiestart)</label><input type="date" id="siste_okning" oninput="oppdater()"></div>
        </div>
        <div class="lo-sek">
          <div class="lo-sek-hd">KPI-endring</div>
          <div class="lf">
            <label>12-måneders KPI-endring (%)</label>
            <input type="number" id="kpi_pst" oninput="oppdater()" placeholder="f.eks. 4.2" step="0.1">
            <div style="font-size:11px;color:var(--ink-mute);margin-top:4px;">Finn siste 12-mnd konsumprisindeks på ssb.no/statistikk/kpi</div>
          </div>
        </div>
        <div class="lo-sek">
          <div class="lo-sek-hd">Varsel</div>
          <div class="lf"><label>Dato for ønsket ikrafttredelse</label><input type="date" id="ikraft_dato" oninput="oppdater()"></div>
          <div style="font-size:11px;color:var(--ink-mute);">Husleieloven krever 6 ukers skriftlig varsel (§ 4-3).</div>
        </div>
        <button class="last-ned-kn no-print" onclick="window.print()">Last ned som PDF</button>
      </div>
      <div>
        <!-- Resultat-tall -->
        <div class="lo-res-grid" id="lo-res-grid" style="display:none">
          <div class="lo-res-kort groen">
            <div class="lo-res-label">Maks ny leie</div>
            <div class="lo-res-val" id="res-ny-leie">—</div>
            <div class="lo-res-sub">per måned</div>
          </div>
          <div class="lo-res-kort">
            <div class="lo-res-label">Økning</div>
            <div class="lo-res-val" id="res-okning">—</div>
            <div class="lo-res-sub" id="res-okning-sub">per måned</div>
          </div>
          <div class="lo-res-kort">
            <div class="lo-res-label">Tidligst ikrafttredelse</div>
            <div class="lo-res-val" id="res-frist" style="font-size:18px">—</div>
            <div class="lo-res-sub">6 uker fra varseldato</div>
          </div>
          <div class="lo-res-kort">
            <div class="lo-res-label">Status</div>
            <div class="lo-res-val" id="res-status" style="font-size:16px">—</div>
            <div class="lo-res-sub" id="res-status-sub"></div>
          </div>
        </div>
        <!-- Varselbrev -->
        <div class="brev-wrap">
          <div class="brev-header">
            <h3>Varselbrev til leietaker</h3>
            <div class="brev-kn-rad no-print">
              <button class="brev-kn kopier" onclick="kopierBrev()">Kopier tekst</button>
              <button class="brev-kn skriv" onclick="window.print()">Last ned PDF</button>
            </div>
          </div>
          <div class="brev-dokument" id="lo-brev"><p class="brev-tom">Fyll ut feltene til venstre — varselbrevet bygger seg her.</p></div>
        </div>
      </div>
    </div>
    <div class="prose sp-body no-print">
      <h2>Reglene for leieøkning</h2>
      <p>Etter husleieloven § 4-2 kan leien reguleres én gang per 12 måneder. Økningen er begrenset til endringen i konsumprisindeksen (KPI) i samme periode. Du kan aldri sette opp leien mer enn det KPI-endringen tilsier — men du kan sette opp mindre.</p>
      <p>Varselet må fremsettes skriftlig med minst 6 ukers frist, jf. husleieloven § 4-3. Varselet kan sendes på e-post dersom leietaker har akseptert elektronisk kommunikasjon.</p>
      <p>Ønsker du å sette leien til gjengs leie (markedsleie), gjelder egne regler etter husleieloven § 4-3. Det er en annen prosess enn KPI-regulering.</p>
    </div>
  </div>
</main>
<script>
function dato(iso) {{
  if (!iso) return '________';
  return new Date(iso+'T12:00:00').toLocaleDateString('nb-NO', {{day:'numeric',month:'long',year:'numeric'}});
}}
function kr(n) {{
  return Math.round(n).toLocaleString('nb-NO') + ' kr';
}}
function addDager(isoStr, dager) {{
  if (!isoStr) return null;
  const d = new Date(isoStr+'T12:00:00');
  d.setDate(d.getDate() + dager);
  return d;
}}
function oppdater() {{
  const utleierNavn = document.getElementById('utleier_navn').value.trim();
  const utleierAdresse = document.getElementById('utleier_adresse').value.trim();
  const leietakerNavn = document.getElementById('leietaker_navn').value.trim();
  const boligAdresse = document.getElementById('bolig_adresse').value.trim();
  const naaLeie = parseFloat(document.getElementById('naaleie').value) || 0;
  const sisteOkning = document.getElementById('siste_okning').value;
  const kpiPst = parseFloat(document.getElementById('kpi_pst').value);
  const ikraftDato = document.getElementById('ikraft_dato').value;

  // Beregn
  const nyLeie = naaLeie && !isNaN(kpiPst) ? naaLeie * (1 + kpiPst/100) : 0;
  const okning = nyLeie - naaLeie;
  const naa = new Date();
  const varseldato = naa;
  const tidligstIkraft = addDager(naa.toISOString().split('T')[0], 42); // 6 uker

  // Status: kan vi øke?
  let kanOke = true, statusTekst = '✓ Kan økes nå', statusSub = '';
  if (sisteOkning) {{
    const siste = new Date(sisteOkning+'T12:00:00');
    const nesteMulig = new Date(siste);
    nesteMulig.setFullYear(nesteMulig.getFullYear() + 1);
    if (naa < nesteMulig) {{
      kanOke = false;
      statusTekst = '⏳ For tidlig';
      statusSub = 'Tidligst ' + nesteMulig.toLocaleDateString('nb-NO', {{day:'numeric',month:'short',year:'numeric'}});
    }}
  }}

  // Vis tall
  if (naaLeie && !isNaN(kpiPst)) {{
    document.getElementById('lo-res-grid').style.display = 'grid';
    document.getElementById('res-ny-leie').textContent = kr(nyLeie) + '/mnd';
    document.getElementById('res-okning').textContent = '+' + kr(okning) + '/mnd';
    document.getElementById('res-okning-sub').textContent = '+' + kr(okning*12) + ' per år';
    document.getElementById('res-frist').textContent = tidligstIkraft ? tidligstIkraft.toLocaleDateString('nb-NO',{{day:'numeric',month:'short'}}) : '—';
    document.getElementById('res-status').textContent = statusTekst;
    document.getElementById('res-status-sub').textContent = statusSub;
  }} else {{
    document.getElementById('lo-res-grid').style.display = 'none';
  }}

  // Varselbrev
  if (!utleierNavn && !leietakerNavn && !naaLeie) {{
    document.getElementById('lo-brev').innerHTML = '<p class="brev-tom">Fyll ut feltene til venstre — varselbrevet bygger seg her.</p>';
    return;
  }}
  const idag = naa.toLocaleDateString('nb-NO', {{day:'numeric',month:'long',year:'numeric'}});
  const nyLeieStr = nyLeie > 0 ? kr(nyLeie) : '[ny leie]';
  const ikraft = ikraftDato ? dato(ikraftDato) : (tidligstIkraft ? dato(tidligstIkraft.toISOString().split('T')[0]) : '[ikrafttredelsesdato]');
  let brev = '';
  brev += `<div style="margin-bottom:24px;font-size:14px;">`;
  if (utleierNavn) brev += `<strong>${{utleierNavn}}</strong><br>`;
  if (utleierAdresse) brev += `${{utleierAdresse}}<br>`;
  brev += `</div>`;
  brev += `<div style="margin-bottom:24px;font-size:14px;">`;
  if (leietakerNavn) brev += `<strong>${{leietakerNavn}}</strong><br>`;
  if (boligAdresse) brev += `${{boligAdresse}}<br>`;
  brev += `</div>`;
  brev += `<div style="margin-bottom:24px;font-size:14px;">${{idag}}</div>`;
  brev += `<div style="font-weight:700;font-size:17px;margin-bottom:20px;font-family:var(--sans);">VARSEL OM LEIEØKNING</div>`;
  brev += `<p>Leiebolig: <strong>${{boligAdresse || '[adresse]'}}</strong></p>`;
  brev += `<p style="margin-top:12px;">Du varsles herved om at husleien reguleres i samsvar med konsumprisindeksen, jf. husleieloven § 4-2.</p>`;
  brev += `<p style="margin-top:12px;"><strong>Nåværende månedlig leie:</strong> ${{naaLeie ? kr(naaLeie)+'/mnd' : '[nåværende leie]'}}<br>`;
  if (!isNaN(kpiPst)) brev += `<strong>KPI-endring (12 mnd):</strong> ${{kpiPst}} %<br>`;
  brev += `<strong>Ny månedlig leie:</strong> ${{nyLeieStr}}/mnd</p>`;
  brev += `<p style="margin-top:12px;">Den nye leien trer i kraft fra <strong>${{ikraft}}</strong>.</p>`;
  brev += `<p style="margin-top:12px;">Fristen for dette varselet er 6 uker, jf. husleieloven § 4-3. Ønsker du å bestride reguleringsgrunnlaget, ta skriftlig kontakt innen denne fristen.</p>`;
  brev += `<div style="margin-top:32px;">Med vennlig hilsen<br><br>${{utleierNavn || '________________'}}</div>`;
  document.getElementById('lo-brev').innerHTML = brev;
}}
function kopierBrev() {{
  const el = document.getElementById('lo-brev');
  navigator.clipboard.writeText(el.innerText).then(() => {{
    const kn = document.querySelector('.brev-kn.kopier');
    kn.textContent = '✓ Kopiert!';
    setTimeout(() => kn.textContent = 'Kopier tekst', 2500);
  }});
}}
oppdater();
</script>
{site_footer(depth=2)}"""


# ─────────────────────────────────────────────────────────────────────────────
# TJENESTE 4: INKASSO-SJEKK
# ─────────────────────────────────────────────────────────────────────────────
def render_tjenester_inkasso():
    return f"""{shared_head(
        'Inkasso-sjekk — er kravet lovlig? | Rettsregel',
        'Sjekk om inkassokravet du har fått er lovlig og innenfor fristen. Gratis verktøy med ferdig innsigelse-mal om nødvendig.',
        depth=2, canonical_path='/tjenester/inkasso/'
    )}
{site_nav(depth=2)}
<style>
.ink-layout {{ display: grid; grid-template-columns: 380px 1fr; gap: 32px; align-items: start; margin-bottom: 64px; }}
.ink-layout > * {{ min-width: 0; }}
@media (max-width: 1024px) {{ .ink-layout {{ grid-template-columns: 1fr !important; }} }}
.ink-skjema {{ background: var(--bg-card); border: 1px solid var(--line); border-radius: 20px; padding: 28px; box-shadow: var(--shadow-md); position: sticky; top: 24px; }}
@media (max-width: 1024px) {{ .ink-skjema {{ position: static !important; }} }}
.ink-tittel {{ font-family: var(--serif); font-size: 18px; font-weight: 400; margin-bottom: 20px; }}
.ink-sek {{ margin-bottom: 18px; border-bottom: 1px solid var(--line); padding-bottom: 18px; }}
.ink-sek:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
.ink-sek-hd {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); margin-bottom: 10px; }}
.inkf {{ margin-bottom: 10px; }}
.inkf label {{ display: block; font-size: 12px; font-weight: 600; color: var(--ink-soft); margin-bottom: 4px; }}
.inkf input, .inkf select, .inkf textarea {{
  width: 100%; padding: 9px 12px; border: 1.5px solid var(--line);
  border-radius: 8px; font-family: var(--sans); font-size: 16px;
  background: var(--bg); color: var(--ink); box-sizing: border-box;
}}
.inkf input:focus, .inkf select:focus, .inkf textarea:focus {{ outline: none; border-color: var(--accent); }}
.inkf textarea {{ min-height: 70px; resize: vertical; }}
.inkf-radio {{ display: flex; flex-direction: column; gap: 6px; }}
.inkf-radio label {{ display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 500; cursor: pointer; padding: 8px 12px; border: 1.5px solid var(--line); border-radius: 8px; line-height: 1.35; }}
.inkf-radio input[type=radio] {{ width: auto; margin: 0; accent-color: var(--accent); flex-shrink: 0; }}
.inkf-radio label:has(input:checked) {{ border-color: var(--accent); background: rgba(177,74,42,0.05); color: var(--accent); font-weight: 600; }}
/* Analyse */
.ink-analyse {{ display: none; }}
.ink-dom-kort {{ border-radius: 14px; padding: 20px 24px; margin-bottom: 20px; }}
.ink-dom-kort.rod {{ background: #fde8e8; border: 1.5px solid #f0a0a0; }}
.ink-dom-kort.gul {{ background: #fff3cd; border: 1.5px solid #ffc107; }}
.ink-dom-kort.groen {{ background: #e8f4e8; border: 1.5px solid #8dcc8d; }}
.ink-dom-tittel {{ font-family: var(--serif); font-size: 20px; font-weight: 400; margin-bottom: 10px; }}
.ink-dom-tekst {{ font-size: 14px; line-height: 1.65; }}
/* Sjekkliste */
.ink-sjekk-liste {{ display: flex; flex-direction: column; gap: 8px; margin-bottom: 20px; }}
.ink-sjekk-item {{ display: flex; gap: 10px; padding: 12px 16px; border-radius: 10px; background: var(--bg-card); border: 1px solid var(--line); font-size: 13px; line-height: 1.5; }}
.ink-sjekk-item .ink-icon {{ font-size: 16px; flex-shrink: 0; }}
/* Brevboks */
.brev-wrap {{ background: var(--bg-alt); border-radius: 16px; padding: 24px; border: 1px solid var(--line); }}
.brev-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }}
.brev-header h3 {{ font-family: var(--serif); font-size: 18px; font-weight: 400; margin: 0; }}
.brev-kn-rad {{ display: flex; gap: 10px; }}
.brev-kn {{ padding: 8px 16px; border-radius: 8px; font-family: var(--sans); font-size: 13px; font-weight: 600; cursor: pointer; border: none; }}
.brev-kn.kopier {{ background: var(--accent); color: white; }}
.brev-kn.skriv {{ background: var(--bg-card); border: 1.5px solid var(--line); color: var(--ink); }}
.brev-dokument {{ background: white; border-radius: 12px; padding: 36px 40px; font-family: 'EB Garamond', Georgia, serif; font-size: 16px; line-height: 1.8; color: var(--ink); border: 1px solid var(--line); }}
@media (max-width: 600px) {{ .brev-dokument {{ padding: 20px 16px; font-size: 15px; }} }}
.brev-tom {{ color: var(--ink-mute); font-style: italic; font-family: var(--sans); font-size: 14px; }}
@media print {{
  .no-print {{ display: none !important; }}
  nav.site-nav, footer.site-footer, #chat-toggle, #chat-panel, .breadcrumbs, .article-header, .ink-skjema, .sp-body {{ display: none !important; }}
  .ink-layout {{ display: block; }}
  .brev-wrap {{ border: none; padding: 0; background: white; }}
  .brev-dokument {{ border: none; padding: 0; box-shadow: none; }}
  body {{ background: white; }}
}}
</style>
<main class="page">
  <div class="container">
    <div class="breadcrumbs no-print">
      <a href="../../">Rettsregel</a><span class="sep">›</span>
      <a href="../../tjenester/">Tjenester</a><span class="sep">›</span>
      <span class="current">Inkasso-sjekk</span>
    </div>
    <div class="article-header no-print">
      <div class="article-eyebrow">Gratis verktøy</div>
      <h1 class="article-title">Er inkassokravet ditt lovlig?</h1>
      <p class="article-description">Fyll ut hva du har mottatt. Vi sjekker foreldelse, formalia og gir deg riktig respons — med ferdig innsigelse-mal om du trenger det.</p>
    </div>
    <div class="ink-layout">
      <div class="ink-skjema no-print">
        <div class="ink-tittel">Kravet du har fått</div>
        <div class="ink-sek">
          <div class="ink-sek-hd">Grunnlaget</div>
          <div class="inkf"><label>Hva gjelder kravet?</label>
            <select id="krav_type" onchange="oppdater()">
              <option value="">— Velg —</option>
              <option value="faktura">Ubetalt faktura fra bedrift</option>
              <option value="leie">Husleie / strøm / abonnement</option>
              <option value="lan">Lån (privat eller bank)</option>
              <option value="erstatning">Erstatningskrav</option>
              <option value="annet">Annet / vet ikke</option>
            </select>
          </div>
          <div class="inkf"><label>Kroppens navn / inkassoselskapet</label><input type="text" id="inkasso_navn" oninput="oppdater()" placeholder="f.eks. Lindorff / Kredinor"></div>
        </div>
        <div class="ink-sek">
          <div class="ink-sek-hd">Beløp</div>
          <div class="inkf"><label>Opprinnelig krav (kr) — fra kvitteringen</label><input type="number" id="oppr_krav" oninput="oppdater()" placeholder="f.eks. 3000" min="0"></div>
          <div class="inkf"><label>Totalt krevd inkl. gebyrer (kr)</label><input type="number" id="totalt_krav" oninput="oppdater()" placeholder="f.eks. 6800" min="0"></div>
        </div>
        <div class="ink-sek">
          <div class="ink-sek-hd">Datoer</div>
          <div class="inkf"><label>Når var kravet opprinnelig forfalt?</label><input type="date" id="forfall_dato" oninput="oppdater()"></div>
          <div class="inkf"><label>Fikk du inkassovarsel (purring) før inkasso?</label>
            <div class="inkf-radio">
              <label><input type="radio" name="hadde_varsel" value="ja" onchange="oppdater()" checked> Ja</label>
              <label><input type="radio" name="hadde_varsel" value="nei" onchange="oppdater()"> Nei — ingen purring</label>
              <label><input type="radio" name="hadde_varsel" value="vet_ikke" onchange="oppdater()"> Vet ikke</label>
            </div>
          </div>
        </div>
        <div class="ink-sek">
          <div class="ink-sek-hd">Din situasjon</div>
          <div class="inkf"><label>Kjenner du igjen kravet?</label>
            <div class="inkf-radio">
              <label><input type="radio" name="kjenner_krav" value="ja" onchange="oppdater()" checked> Ja, jeg kjenner det igjen</label>
              <label><input type="radio" name="kjenner_krav" value="delvis" onchange="oppdater()"> Delvis — bestrider deler av det</label>
              <label><input type="radio" name="kjenner_krav" value="nei" onchange="oppdater()"> Nei, ukjent krav</label>
            </div>
          </div>
          <div class="inkf"><label>Ditt fulle navn</label><input type="text" id="mitt_navn_ink" oninput="oppdater()" placeholder="Ola Nordmann"></div>
          <div class="inkf"><label>Din adresse</label><input type="text" id="min_adresse_ink" oninput="oppdater()" placeholder="Veien 5, 0000 Oslo"></div>
        </div>
      </div>
      <div>
        <div id="ink-tom" class="brev-wrap" style="margin-bottom:24px">
          <p class="brev-tom">Fyll ut feltene til venstre — analysen bygger seg her.</p>
        </div>
        <div class="ink-analyse" id="ink-analyse">
          <div id="ink-dom-kort"></div>
          <div class="ink-sjekk-liste" id="ink-sjekk-liste"></div>
          <div class="brev-wrap" id="ink-brev-seksjon" style="display:none">
            <div class="brev-header">
              <h3 id="brev-tittel-ink">Innsigelse til inkassoselskapet</h3>
              <div class="brev-kn-rad no-print">
                <button class="brev-kn kopier" onclick="kopierBrev()">Kopier tekst</button>
                <button class="brev-kn skriv" onclick="window.print()">Last ned PDF</button>
              </div>
            </div>
            <div class="brev-dokument" id="ink-brev"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="prose sp-body no-print">
      <h2>Dine rettigheter overfor inkasso</h2>
      <p>Et gyldig inkassokrav krever at det er sendt ett inkassovarsel med minst 14 dagers frist, og ett purrebrev med minst 14 dagers frist, før inkassosaken starter. Mangler disse stegene, er inkassosalæret ulovlig.</p>
      <p>Alle krav foreldes. Vanlig foreldelsesfrist er 3 år fra forfallsdato. Dommer og gjeldsbrev har 10 år. Etter foreldelse er du ikke lenger juridisk forpliktet til å betale.</p>
      <p>Er du uenig i kravet eller mener det er foreldet: Send skriftlig innsigelse til inkassoselskapet. De plikter da å stanse innkrevingen og sette saken i bero, jf. inkassoloven § 12.</p>
    </div>
  </div>
</main>
<script>
function radio(name) {{
  const el = document.querySelector('input[name="'+name+'"]:checked');
  return el ? el.value : null;
}}
function dato(iso) {{
  if (!iso) return '________';
  return new Date(iso+'T12:00:00').toLocaleDateString('nb-NO', {{day:'numeric',month:'long',year:'numeric'}});
}}
function kr(n) {{
  return parseInt(n).toLocaleString('nb-NO') + ' kr';
}}
function oppdater() {{
  const kravType = document.getElementById('krav_type').value;
  const inkassoNavn = document.getElementById('inkasso_navn').value.trim();
  const opprKrav = parseFloat(document.getElementById('oppr_krav').value) || 0;
  const totaltKrav = parseFloat(document.getElementById('totalt_krav').value) || 0;
  const forfallDato = document.getElementById('forfall_dato').value;
  const haddeVarsel = radio('hadde_varsel');
  const kjennerKrav = radio('kjenner_krav');
  const mittNavn = document.getElementById('mitt_navn_ink').value.trim();
  const minAdresse = document.getElementById('min_adresse_ink').value.trim();

  // Trenger minimum ett felt
  if (!kravType && !opprKrav && !forfallDato) {{
    document.getElementById('ink-tom').style.display = 'block';
    document.getElementById('ink-analyse').style.display = 'none';
    return;
  }}
  document.getElementById('ink-tom').style.display = 'none';
  document.getElementById('ink-analyse').style.display = 'block';

  // Sjekk foreldelse
  let erForeldet = false, aarTil3 = null;
  if (forfallDato) {{
    const forfall = new Date(forfallDato+'T12:00:00');
    const naa = new Date();
    const ms3aar = 3 * 365.25 * 24 * 3600 * 1000;
    const alder = (naa - forfall) / ms3aar;
    erForeldet = alder > 3;
    aarTil3 = alder.toFixed(1);
  }}

  // Gebyrer sjekk
  const gebyrer = totaltKrav && opprKrav ? totaltKrav - opprKrav : 0;
  const gebyrHoey = gebyrer > opprKrav * 0.25 + 1300; // Grovt anslag

  // Dom
  let domKlasse, domTittel, domTekst;
  if (erForeldet) {{
    domKlasse = 'rod';
    domTittel = 'Kravet er sannsynligvis foreldet';
    domTekst = `Kravet forfalt for over 3 år siden. Den ordinære foreldelsesfristen er 3 år fra forfallsdato, jf. foreldelsesloven § 2. Du er sannsynligvis ikke lenger juridisk forpliktet til å betale. Send innsigelse med én gang.`;
  }} else if (kjennerKrav === 'nei') {{
    domKlasse = 'gul';
    domTittel = 'Ukjent krav — send innsigelse';
    domTekst = `Du kjenner ikke igjen kravet. Det kan skyldes forveksling, identitetstyveri, eller at kravet rett og slett tilhører noen andre. Send skriftlig innsigelse til inkassoselskapet umiddelbart. De har da plikt til å stanse innkrevingen og dokumentere grunnlaget.`;
  }} else if (haddeVarsel === 'nei') {{
    domKlasse = 'gul';
    domTittel = 'Mangler inkassovarsel — salæret kan være ulovlig';
    domTekst = `Inkassoselskapet har ikke lov til å kreve inkassosalær uten at det er sendt et inkassovarsel med minst 14 dagers frist først, jf. inkassoloven § 9 og § 10. Mangler dette steget, kan du nekte å betale salæret.`;
  }} else if (kjennerKrav === 'delvis') {{
    domKlasse = 'gul';
    domTittel = 'Del av kravet er omtvistet';
    domTekst = `Du bestrider deler av kravet. Du kan betale det du erkjenner og sende innsigelse på det du er uenig i. Inkassoselskapet plikter å behandle innsigelsen og kan ikke sende den omtvistede delen til namsmannen før uenigheten er avklart.`;
  }} else if (gebyrHoey) {{
    domKlasse = 'gul';
    domTittel = 'Mulig for høye gebyrer';
    domTekst = `Gebyrene (${{kr(gebyrer)}}) ser høye ut i forhold til opprinnelig krav (${{kr(opprKrav)}}). Maksimale inkassosatser er fastsatt i inkassoforskriften. Du kan be om spesifisert opprinnelse og lovhjemmel for hvert gebyr.`;
  }} else {{
    domKlasse = 'groen';
    domTittel = 'Kravet virker legitimt';
    domTekst = `Basert på opplysningene du har gitt virker inkassokravet legitimt — innenfor foreldelsesfristen, med varsel, og med kjent grunnlag. Kravet bør betales for å unngå videre gebyrer og eventuell namsmannsbehandling.`;
  }}
  document.getElementById('ink-dom-kort').innerHTML = `<div class="ink-dom-kort ${{domKlasse}}"><div class="ink-dom-tittel">${{domTittel}}</div><div class="ink-dom-tekst">${{domTekst}}</div></div>`;

  // Sjekkliste
  const sjekkItems = [];
  if (forfallDato) {{
    sjekkItems.push({{
      icon: erForeldet ? '🔴' : '🟢',
      tekst: erForeldet
        ? `Forfallsdato: ${{dato(forfallDato)}} — <strong>over 3 år siden</strong>. Kravet er sannsynligvis foreldet.`
        : `Forfallsdato: ${{dato(forfallDato)}} — ${{aarTil3}} år siden. Innenfor 3-årsfristen.`
    }});
  }}
  sjekkItems.push({{
    icon: haddeVarsel === 'ja' ? '🟢' : haddeVarsel === 'nei' ? '🔴' : '🟡',
    tekst: haddeVarsel === 'ja' ? 'Inkassovarsel er mottatt ✓' : haddeVarsel === 'nei' ? '<strong>Mangler inkassovarsel</strong> — salæret kan kreves fratrukket' : 'Usikkert om inkassovarsel ble sendt'
  }});
  if (opprKrav && totaltKrav) {{
    sjekkItems.push({{
      icon: gebyrHoey ? '🟡' : '🟢',
      tekst: `Gebyrer: ${{kr(gebyrer)}} utover opprinnelig krav (${{kr(opprKrav)}}). ${{gebyrHoey ? 'Virker høyt — be om spesifikasjon.' : 'Virker rimelig.'}}`
    }});
  }}
  sjekkItems.push({{
    icon: kjennerKrav === 'ja' ? '🟢' : kjennerKrav === 'nei' ? '🔴' : '🟡',
    tekst: kjennerKrav === 'ja' ? 'Kravet er kjent' : kjennerKrav === 'nei' ? '<strong>Ukjent krav</strong> — send innsigelse umiddelbart' : 'Deler av kravet er bestridt'
  }});
  document.getElementById('ink-sjekk-liste').innerHTML = sjekkItems.map(i =>
    `<div class="ink-sjekk-item"><span class="ink-icon">${{i.icon}}</span><span>${{i.tekst}}</span></div>`
  ).join('');

  // Brev — vis hvis krav er problematisk
  const trengerBrev = erForeldet || kjennerKrav === 'nei' || kjennerKrav === 'delvis' || haddeVarsel === 'nei';
  const brevSeksjon = document.getElementById('ink-brev-seksjon');
  if (trengerBrev) {{
    brevSeksjon.style.display = 'block';
    const idag = new Date().toLocaleDateString('nb-NO', {{day:'numeric',month:'long',year:'numeric'}});
    let brevTittel, brevTekst;
    if (erForeldet) {{
      brevTittel = 'Innsigelse — foreldet krav';
      brevTekst = `Jeg bestrider herved ovennevnte krav som foreldet. Kravet forfalt ${{dato(forfallDato)}}, og den ordinære foreldelsesfristen på 3 år etter foreldelsesloven § 2 er dermed overskredet. Jeg er ikke lenger juridisk forpliktet til å betale, jf. foreldelsesloven § 24. Jeg ber om at kravet omgående frafalles og at registreringer hos kredittopplysningsbyråer slettes.`;
    }} else if (kjennerKrav === 'nei') {{
      brevTittel = 'Innsigelse — ukjent krav';
      brevTekst = `Jeg bestrider herved ovennevnte krav i sin helhet. Kravet er meg fullstendig ukjent, og jeg har ingen kjennskap til noe rettslig grunnlag for det. I henhold til inkassoloven § 12 ber jeg om at innkrevingen stanses umiddelbart og at dere dokumenterer grunnlaget for kravet skriftlig, herunder original faktura, kontrakt eller annet avtalegrunnlag. Jeg forbeholder meg retten til å anmelde forholdet til Finanstilsynet og politiet ved urettmessig inkasso.`;
    }} else if (kjennerKrav === 'delvis') {{
      brevTekst = `Jeg erkjenner deler av ovennevnte krav, men bestrider det overskytende. Jeg ber om en detaljert spesifikasjon av alle gebyrer og om hvilken hjemmel i inkassoforskriften hvert enkelt gebyr er begrunnet i. Det bestridte beløpet kreves satt i bero, jf. inkassoloven § 12, inntil uenigheten er avklart.`;
      brevTittel = 'Innsigelse — delvis bestridt krav';
    }} else {{
      brevTekst = `Jeg bestrider herved ovennevnte inkassosalær. Kravet ble sendt til inkasso uten at det forutgående ble sendt et inkassovarsel med 14 dagers betalingsfrist, slik inkassoloven §§ 9 og 10 krever. Inkassosalæret er dermed ulovlig pålagt. Jeg betaler det opprinnelige kravet på ${{kr(opprKrav)}}, men nekter å betale det ulovlig pålagte salæret.`;
      brevTittel = 'Innsigelse — manglende inkassovarsel';
    }}
    document.getElementById('brev-tittel-ink').textContent = brevTittel;
    const brev = `<div style="margin-bottom:24px;font-size:14px;"><strong>${{mittNavn || '[Ditt navn]'}}</strong><br>${{minAdresse || '[Din adresse]'}}</div>`+
      `<div style="margin-bottom:24px;font-size:14px;"><strong>${{inkassoNavn || '[Inkassoselskapet]'}}</strong></div>`+
      `<div style="margin-bottom:24px;font-size:14px;">${{idag}}</div>`+
      `<div style="font-weight:700;font-size:17px;margin-bottom:20px;font-family:var(--sans);">INNSIGELSE MOT INKASSOKRAV</div>`+
      `<p>Referanse: ${{inkassoNavn || '[inkassoselskap]'}}${{opprKrav ? ' — opprinnelig krav ' + kr(opprKrav) : ''}}</p>`+
      `<p style="margin-top:16px;">${{brevTekst}}</p>`+
      `<div style="margin-top:32px;">Med vennlig hilsen<br><br><strong>${{mittNavn || '[Ditt navn]'}}</strong></div>`;
    document.getElementById('ink-brev').innerHTML = brev;
  }} else {{
    brevSeksjon.style.display = 'none';
  }}
}}
function kopierBrev() {{
  const el = document.getElementById('ink-brev');
  navigator.clipboard.writeText(el.innerText).then(() => {{
    const kn = document.querySelector('.brev-kn.kopier');
    kn.textContent = '✓ Kopiert!';
    setTimeout(() => kn.textContent = 'Kopier tekst', 2500);
  }});
}}
oppdater();
</script>
{site_footer(depth=2)}"""



# ─────────────────────────────────────────────────────────────────────────────
# KONTRAKT 1: SAMBOERAVTALE
# ─────────────────────────────────────────────────────────────────────────────
def render_kontrakter_samboeravtale():
    return f"""{shared_head(
        'Samboeravtale — fyll ut og last ned gratis | Rettsregel',
        'Lag en juridisk korrekt samboeravtale gratis. Dekker bolig, gjeld, felles utgifter og hva som skjer ved samlivsbrudd. Last ned som PDF.',
        depth=2, canonical_path='/kontrakter/samboeravtale/'
    )}
{site_nav(depth=2)}
<style>
.samb-layout {{ display: grid; grid-template-columns: 400px 1fr; gap: 32px; align-items: start; margin-bottom: 64px; }}
.samb-layout > * {{ min-width: 0; }}
@media (max-width: 1100px) {{ .samb-layout {{ grid-template-columns: 1fr !important; }} }}
.samb-skjema {{ background: var(--bg-card); border: 1px solid var(--line); border-radius: 20px; padding: 28px; box-shadow: var(--shadow-md); position: sticky; top: 24px; }}
@media (max-width: 1100px) {{ .samb-skjema {{ position: static !important; }} }}
.samb-sek {{ margin-bottom: 20px; border-bottom: 1px solid var(--line); padding-bottom: 20px; }}
.samb-sek:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
.samb-sek-hd {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); margin-bottom: 12px; }}
.sf {{ margin-bottom: 10px; }}
.sf label {{ display: block; font-size: 12px; font-weight: 600; color: var(--ink-soft); margin-bottom: 4px; }}
.sf input, .sf select, .sf textarea {{ width: 100%; padding: 9px 12px; border: 1.5px solid var(--line); border-radius: 8px; font-family: var(--sans); font-size: 16px; background: var(--bg); color: var(--ink); box-sizing: border-box; }}
.sf input:focus, .sf select:focus, .sf textarea:focus {{ outline: none; border-color: var(--accent); }}
.sf textarea {{ min-height: 60px; resize: vertical; }}
.sf-rad {{ display: flex; flex-direction: column; gap: 6px; }}
.sf-rad label {{ display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 500; cursor: pointer; padding: 8px 12px; border: 1.5px solid var(--line); border-radius: 8px; line-height: 1.35; }}
.sf-rad input[type=radio] {{ width: auto; margin: 0; accent-color: var(--accent); flex-shrink: 0; }}
.sf-rad label:has(input:checked) {{ border-color: var(--accent); background: rgba(177,74,42,0.06); color: var(--accent); font-weight: 600; }}
.sf-2kol {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }}
.last-ned-kn {{ width: 100%; background: var(--accent); color: white; border: none; border-radius: 12px; font-family: var(--sans); font-size: 15px; font-weight: 600; padding: 15px; cursor: pointer; margin-top: 20px; transition: background 0.2s; }}
.last-ned-kn:hover {{ background: var(--accent-deep); }}
/* Dokument */
.dok-wrap {{ background: var(--bg-alt); border-radius: 16px; padding: 24px; border: 1px solid var(--line); }}
.dok-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 10px; }}
.dok-header h3 {{ font-family: var(--serif); font-size: 18px; font-weight: 400; margin: 0; }}
.dok-kn-rad {{ display: flex; gap: 10px; }}
.dok-kn {{ padding: 8px 16px; border-radius: 8px; font-family: var(--sans); font-size: 13px; font-weight: 600; cursor: pointer; border: none; }}
.dok-kn.kopier {{ background: var(--accent); color: white; }}
.dok-kn.skriv {{ background: var(--bg-card); border: 1.5px solid var(--line); color: var(--ink); }}
.dok-dokument {{ background: white; border-radius: 12px; padding: 48px 52px; font-family: 'EB Garamond', Georgia, serif; font-size: 16px; line-height: 1.85; color: #1a1612; border: 1px solid var(--line); }}
@media (max-width: 600px) {{ .dok-dokument {{ padding: 24px 18px; font-size: 15px; }} }}
.dok-tom {{ color: var(--ink-mute); font-style: italic; font-family: var(--sans); font-size: 14px; padding: 32px 0; text-align: center; }}
.dok-tittel-blokk {{ text-align: center; margin-bottom: 36px; }}
.dok-tittel-blokk h1 {{ font-size: 22px; font-weight: 700; font-family: var(--sans); letter-spacing: 0.04em; text-transform: uppercase; margin-bottom: 6px; }}
.dok-tittel-blokk .dok-sub {{ font-size: 14px; color: #555; font-family: var(--sans); }}
.dok-sek {{ margin-bottom: 28px; }}
.dok-sek h2 {{ font-family: var(--sans); font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 10px; border-bottom: 1.5px solid #1a1612; padding-bottom: 5px; }}
.sign-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin-top: 48px; }}
.sign-boks {{ border-top: 1px solid #888; padding-top: 10px; font-family: var(--sans); font-size: 13px; color: #555; }}
@media (max-width: 600px) {{ .sign-grid {{ grid-template-columns: 1fr; }} }}
@media print {{
  .no-print {{ display: none !important; }}
  nav.site-nav, footer.site-footer, #chat-toggle, #chat-panel, .breadcrumbs, .article-header, .samb-skjema, .sp-body {{ display: none !important; }}
  .samb-layout {{ display: block; }}
  .dok-wrap {{ border: none; padding: 0; background: white; }}
  .dok-dokument {{ border: none; padding: 0; box-shadow: none; font-size: 13pt; line-height: 1.7; }}
  body {{ background: white; }}
}}
</style>
<main class="page">
  <div class="container">
    <div class="breadcrumbs no-print">
      <a href="../../">Rettsregel</a><span class="sep">›</span>
      <a href="../../kontrakter/">Kontrakter</a><span class="sep">›</span>
      <span class="current">Samboeravtale</span>
    </div>
    <div class="article-header no-print">
      <div class="article-eyebrow">Gratis kontraktsmal</div>
      <h1 class="article-title">Samboeravtale</h1>
      <p class="article-description">Fyll ut om dere og boligen. Avtalen bygger seg live — last ned ferdig PDF.</p>
    </div>
    <div class="samb-layout">
      <div class="samb-skjema no-print">

        <div class="samb-sek">
          <div class="samb-sek-hd">Part 1</div>
          <div class="sf"><label>Fullt navn</label><input id="p1_navn" oninput="oppdater()" placeholder="Ola Nordmann"></div>
          <div class="sf"><label>Fødselsdato (valgfritt)</label><input id="p1_fodt" oninput="oppdater()" placeholder="01.01.1990" type="text"></div>
          <div class="sf"><label>Adresse</label><input id="p1_adr" oninput="oppdater()" placeholder="Veien 1, 0000 Oslo"></div>
        </div>

        <div class="samb-sek">
          <div class="samb-sek-hd">Part 2</div>
          <div class="sf"><label>Fullt navn</label><input id="p2_navn" oninput="oppdater()" placeholder="Kari Nordmann"></div>
          <div class="sf"><label>Fødselsdato (valgfritt)</label><input id="p2_fodt" oninput="oppdater()" placeholder="01.01.1992" type="text"></div>
          <div class="sf"><label>Adresse</label><input id="p2_adr" oninput="oppdater()" placeholder="Veien 1, 0000 Oslo"></div>
        </div>

        <div class="samb-sek">
          <div class="samb-sek-hd">Boligen</div>
          <div class="sf"><label>Boligens adresse</label><input id="bol_adr" oninput="oppdater()" placeholder="Felles adresse, 0000 Oslo"></div>
          <div class="sf"><label>Eierforhold</label>
            <div class="sf-rad">
              <label><input type="radio" name="eier" value="felles" onchange="oppdater()" checked> Eies i fellesskap</label>
              <label><input type="radio" name="eier" value="p1" onchange="oppdater()"> Eies av Part 1 alene</label>
              <label><input type="radio" name="eier" value="p2" onchange="oppdater()"> Eies av Part 2 alene</label>
              <label><input type="radio" name="eier" value="leier" onchange="oppdater()"> Begge leier (ingen av oss eier)</label>
            </div>
          </div>
          <div id="andel-seksjon" class="sf-2kol">
            <div class="sf"><label>Part 1 sin eierandel (%)</label><input id="andel_p1" oninput="oppdaterAndel()" type="number" min="1" max="99" placeholder="50"></div>
            <div class="sf"><label>Part 2 sin eierandel (%)</label><input id="andel_p2" type="number" min="1" max="99" placeholder="50" readonly style="background:var(--bg-alt);color:var(--ink-mute)"></div>
          </div>
          <div class="sf"><label>Kjøpesum / takst (kr, valgfritt)</label><input id="bol_verdi" oninput="oppdater()" type="number" placeholder="4500000" min="0"></div>
        </div>

        <div class="samb-sek">
          <div class="samb-sek-hd">Felles økonomi</div>
          <div class="sf"><label>Fordeling av felles boutgifter</label>
            <div class="sf-rad">
              <label><input type="radio" name="utgifter" value="likt" onchange="oppdater()" checked> Deles likt (50/50)</label>
              <label><input type="radio" name="utgifter" value="andel" onchange="oppdater()"> Deles etter eierandel</label>
              <label><input type="radio" name="utgifter" value="inntekt" onchange="oppdater()"> Deles etter inntekt</label>
              <label><input type="radio" name="utgifter" value="annet" onchange="oppdater()"> Annen fordeling</label>
            </div>
          </div>
          <div id="annen-fordeling-boks" class="sf" style="display:none">
            <label>Beskriv fordelingen</label>
            <textarea id="annen_fordeling" oninput="oppdater()" placeholder="f.eks. Part 1 dekker boliglån, Part 2 dekker strøm og felleskostnader"></textarea>
          </div>
          <div class="sf"><label>Felles bankkonto for boutgifter?</label>
            <div class="sf-rad">
              <label><input type="radio" name="felleskonto" value="ja" onchange="oppdater()" checked> Ja, vi oppretter / bruker felles konto</label>
              <label><input type="radio" name="felleskonto" value="nei" onchange="oppdater()"> Nei, vi betaler separat</label>
            </div>
          </div>
        </div>

        <div class="samb-sek">
          <div class="samb-sek-hd">Ved samlivsbrudd</div>
          <div class="sf"><label>Hvem kan overta boligen ved brudd?</label>
            <div class="sf-rad">
              <label><input type="radio" name="brudd_bol" value="forkjop" onchange="oppdater()" checked> Den ene kan kreve å kjøpe ut den andre til takst</label>
              <label><input type="radio" name="brudd_bol" value="selges" onchange="oppdater()"> Boligen selges og overskuddet fordeles etter eierandel</label>
              <label><input type="radio" name="brudd_bol" value="forhandle" onchange="oppdater()"> Partene forhandler ved brudd</label>
            </div>
          </div>
          <div class="sf"><label>Frist for å avklare boligen etter brudd</label>
            <div class="sf-rad">
              <label><input type="radio" name="brudd_frist" value="3" onchange="oppdater()" checked> 3 måneder</label>
              <label><input type="radio" name="brudd_frist" value="6" onchange="oppdater()"> 6 måneder</label>
              <label><input type="radio" name="brudd_frist" value="12" onchange="oppdater()"> 12 måneder</label>
            </div>
          </div>
        </div>

        <div class="samb-sek">
          <div class="samb-sek-hd">Særeie og gjeld</div>
          <div class="sf"><label>Verdier eid av Part 1 FØR samboerskapet (valgfritt)</label>
            <textarea id="saereie_p1" oninput="oppdater()" placeholder="f.eks. hytte på Hafjell verdsatt til 1 500 000 kr, arvede møbler"></textarea>
          </div>
          <div class="sf"><label>Verdier eid av Part 2 FØR samboerskapet (valgfritt)</label>
            <textarea id="saereie_p2" oninput="oppdater()" placeholder="f.eks. bil av merke Toyota, reg.nr AB 12345, verdi 250 000 kr"></textarea>
          </div>
          <div class="sf"><label>Felles gjeld (valgfritt)</label>
            <textarea id="felles_gjeld" oninput="oppdater()" placeholder="f.eks. felles boliglån i DNB, lånenr. 12345, total restgjeld 3 200 000 kr. Deles likt."></textarea>
          </div>
        </div>

        <div class="samb-sek">
          <div class="samb-sek-hd">Underskrift</div>
          <div class="sf"><label>Sted og dato</label><input id="sign_sted_dato" oninput="oppdater()" placeholder="Oslo, 14. mai 2026"></div>
        </div>

        <button class="last-ned-kn no-print" onclick="window.print()">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="display:inline;vertical-align:middle;margin-right:6px"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7,10 12,15 17,10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Last ned som PDF
        </button>
      </div>

      <div>
        <div class="dok-wrap">
          <div class="dok-header">
            <h3>Din samboeravtale</h3>
            <div class="dok-kn-rad no-print">
              <button class="dok-kn kopier" onclick="kopier()">Kopier tekst</button>
              <button class="dok-kn skriv" onclick="window.print()">Last ned PDF</button>
            </div>
          </div>
          <div class="dok-dokument" id="dok-innhold">
            <p class="dok-tom">Fyll ut feltene til venstre — avtalen bygger seg her.</p>
          </div>
        </div>
      </div>
    </div>

    <div class="prose sp-body no-print">
      <h2>Hvorfor trenger samboere en samboeravtale?</h2>
      <p>Samboere har langt svakere juridiske rettigheter enn gifte par. Ved samlivsbrudd gjelder ingen automatisk likedeling — du har rett til det du eide inn, og ingenting mer. Uten en samboeravtale kan det oppstå uklarhet om hvem som eier hva, hvem som har betalt hva, og hvem som har rett til å bli boende.</p>
      <p>Samboeravtalen er særlig viktig hvis du har betalt mer inn i en felles bolig enn din formelle eierandel tilsier, hvis du har hatt inntektsforskjell underveis i samboerskapet, eller hvis dere eier ting med veldig ulik verdi fra før.</p>
      <p>Avtalen er gyldig uten notarius publicus. To eksemplarer skrives ut og begge signerer begge eksemplarene. Begge beholder hvert sitt eksemplar.</p>
    </div>
  </div>
</main>
<script>
function radio(name) {{ return (document.querySelector('input[name="'+name+'"]:checked')||{{}}).value || ''; }}
function v(id) {{ const el=document.getElementById(id); return el ? el.value.trim() : ''; }}
function kr(n) {{ const num=parseInt(n); return num ? num.toLocaleString('nb-NO')+' kr' : ''; }}
function oppdaterAndel() {{
  const a1 = parseInt(document.getElementById('andel_p1').value)||50;
  const a2 = Math.max(1, Math.min(99, 100-a1));
  document.getElementById('andel_p2').value = a2;
  oppdater();
}}
function vis(id, show) {{ document.getElementById(id).style.display = show ? '' : 'none'; }}

function oppdater() {{
  const p1 = v('p1_navn') || 'Part 1';
  const p2 = v('p2_navn') || 'Part 2';
  const p1f = v('p1_fodt');
  const p2f = v('p2_fodt');
  const p1a = v('p1_adr');
  const p2a = v('p2_adr');
  const bolAdr = v('bol_adr');
  const eier = radio('eier') || 'felles';
  const andel1 = parseInt(v('andel_p1'))||50;
  const andel2 = 100-andel1;
  const bolVerdi = v('bol_verdi');
  const utgifter = radio('utgifter') || 'likt';
  const felleskonto = radio('felleskonto') || 'ja';
  const bruddBol = radio('brudd_bol') || 'forkjop';
  const bruddFrist = radio('brudd_frist') || '3';
  const saereieP1 = v('saereie_p1');
  const saereieP2 = v('saereie_p2');
  const fellesGjeld = v('felles_gjeld');
  const signStedDato = v('sign_sted_dato');
  const annenFordeling = v('annen_fordeling');

  // Toggle visibility
  vis('andel-seksjon', eier === 'felles');
  vis('annen-fordeling-boks', utgifter === 'annet');

  if (!v('p1_navn') && !v('p2_navn') && !bolAdr) {{
    document.getElementById('dok-innhold').innerHTML = '<p class="dok-tom">Fyll ut feltene til venstre — avtalen bygger seg her.</p>';
    return;
  }}

  // Eierforhold-tekst
  let eierTekst = '';
  if (eier === 'felles') {{
    eierTekst = `${{p1}} eier ${{andel1}} % og ${{p2}} eier ${{andel2}} % av boligen${{bolAdr?' i '+bolAdr:''}}.`;
    if (bolVerdi) eierTekst += ` Boligen er ved avtaleinngåelsen verdsatt til ${{kr(bolVerdi)}}.`;
  }} else if (eier === 'p1') {{
    eierTekst = `Boligen${{bolAdr?' i '+bolAdr:''}} eies av ${{p1}} alene. ${{p2}} har bruksrett til boligen gjennom samboerskapet.`;
  }} else if (eier === 'p2') {{
    eierTekst = `Boligen${{bolAdr?' i '+bolAdr:''}} eies av ${{p2}} alene. ${{p1}} har bruksrett til boligen gjennom samboerskapet.`;
  }} else {{
    eierTekst = `Begge parter leier boligen${{bolAdr?' i '+bolAdr:''}}. Ingen av partene er eiere.`;
  }}

  // Utgifter-tekst
  let utgifterTekst = '';
  if (utgifter === 'likt') utgifterTekst = 'Felles boutgifter (boliglån/husleie, strøm, forsikring og andre løpende kostnader knyttet til felles bolig) deles likt mellom partene med 50 % på hver.';
  else if (utgifter === 'andel') utgifterTekst = `Felles boutgifter deles i henhold til eierandel: ${{p1}} dekker ${{andel1}} % og ${{p2}} dekker ${{andel2}} %.`;
  else if (utgifter === 'inntekt') utgifterTekst = 'Felles boutgifter fordeles forholdsmessig etter partenes løpende inntekt. Fordelingen justeres ved vesentlig endring i inntektsforholdet.';
  else if (annenFordeling) utgifterTekst = annenFordeling;
  else utgifterTekst = 'Partene avtaler fordeling av felles boutgifter særskilt.';

  if (felleskonto === 'ja') utgifterTekst += ' Partene oppretter eller benytter en felles bankkonto til boutgifter, og overfører sin andel månedlig.';

  // Brudd-tekst
  let bruddTekst = '';
  if (bruddBol === 'forkjop') {{
    bruddTekst = `Enhver av partene kan kreve å overta den andres eierandel i boligen til takstverdi fastsatt av uavhengig takstmann. Den parten som ønsker å overta, må gi skriftlig beskjed innen ${{bruddFrist}} måneder etter samlivsbruddet. Kan partene ikke enes om takstmann, oppnevnes én av Norges Takseringsforbund.`;
  }} else if (bruddBol === 'selges') {{
    bruddTekst = `Ved samlivsbrudd selges boligen til markedspris via eiendomsmegler, og salgssummen etter fratrekk av gjeld og omkostninger fordeles mellom partene i henhold til eierandel. Salget skal igangsettes innen ${{bruddFrist}} måneder etter samlivsbruddet.`;
  }} else {{
    bruddTekst = `Ved samlivsbrudd forhandler partene i god tro om den videre disponeringen av boligen. Dersom enighet ikke oppnås innen ${{bruddFrist}} måneder, selges boligen og nettoprovenyet fordeles etter eierandel.`;
  }}

  let dok = `
  <div class="dok-tittel-blokk">
    <h1>Samboeravtale</h1>
    <div class="dok-sub">Inngått mellom ${{p1}} og ${{p2}}</div>
  </div>

  <div class="dok-sek">
    <h2>§ 1 — Partene</h2>
    <p><strong>Part 1:</strong> ${{p1}}${{p1f?' (f. '+p1f+')':''}}${{p1a?', '+p1a:''}}</p>
    <p style="margin-top:8px"><strong>Part 2:</strong> ${{p2}}${{p2f?' (f. '+p2f+')':''}}${{p2a?', '+p2a:''}}</p>
    <p style="margin-top:12px">Partene er samboere og ønsker med denne avtalen å regulere sine økonomiske rettigheter og forpliktelser i samboerskapet og ved eventuelt brudd.</p>
  </div>

  <div class="dok-sek">
    <h2>§ 2 — Boligen</h2>
    <p>${{eierTekst}}</p>
    <p style="margin-top:12px">Verdier den enkelte part har tilført boligen utover den formelle eierandelen (f.eks. arv øremerket nedbetaling av boliglån), dokumenteres separat og kan kreves tilbakeført ved brudd.</p>
  </div>

  <div class="dok-sek">
    <h2>§ 3 — Felles økonomi</h2>
    <p>${{utgifterTekst}}</p>
    <p style="margin-top:12px">Personlige utgifter (klær, egne fritidsaktiviteter, gaver til egen familie m.v.) dekkes av den enkelte part for seg selv.</p>
  </div>`;

  if (saereieP1 || saereieP2) {{
    dok += `<div class="dok-sek"><h2>§ 4 — Eiendeler eid før samboerskapet</h2>`;
    if (saereieP1) dok += `<p><strong>${{p1}}s eiendeler ved avtaleinngåelsen:</strong> ${{saereieP1}}</p>`;
    if (saereieP2) dok += `<p style="margin-top:8px"><strong>${{p2}}s eiendeler ved avtaleinngåelsen:</strong> ${{saereieP2}}</p>`;
    dok += `<p style="margin-top:12px">Ovennevnte eiendeler er og forblir den respektive parts private eiendom og kan ikke kreves delt ved samlivsbrudd.</p></div>`;
  }}

  if (fellesGjeld) {{
    dok += `<div class="dok-sek"><h2>§ ${{(saereieP1||saereieP2)?'5':'4'}} — Gjeld</h2><p>${{fellesGjeld}}</p></div>`;
  }}

  const neste = (saereieP1||saereieP2) ? (fellesGjeld?'6':'5') : (fellesGjeld?'5':'4');
  dok += `
  <div class="dok-sek">
    <h2>§ ${{neste}} — Ved samlivsbrudd</h2>
    <p>${{bruddTekst}}</p>
    <p style="margin-top:12px">Innbo og løsøre som en part har med seg inn i samboerskapet, beholder den samme part ved brudd. Innbo og løsøre kjøpt i fellesskap deles etter verdi slik at begge parter mottar halvparten av samlet verdi, enten ved at den ene overtar mot kompensasjon, eller ved salg.</p>
    <p style="margin-top:12px">Denne avtalen kan endres ved ny skriftlig avtale signert av begge parter.</p>
  </div>

  <div class="dok-sek">
    <h2>§ ${{parseInt(neste)+1}} — Lovvalg og tvisteløsning</h2>
    <p>Denne avtalen er regulert av norsk rett. Tvister søkes løst ved forhandlinger mellom partene. Oppnås ikke enighet, avgjøres tvisten av de ordinære domstoler med verneting der boligen er beliggende.</p>
  </div>

  <div style="margin-top:48px;font-family:var(--sans);font-size:14px;color:#555;border-top:1px solid #ddd;padding-top:20px;">
    <p>Avtalen er utferdiget i to originale eksemplarer. Hver part beholder ett eksemplar.</p>
    <p style="margin-top:8px">Sted og dato: <strong>${{signStedDato || '________________________'}}</strong></p>
  </div>

  <div class="sign-grid">
    <div class="sign-boks">
      <div style="margin-bottom:36px">&nbsp;</div>
      <strong>${{p1}}</strong><br>Part 1
    </div>
    <div class="sign-boks">
      <div style="margin-bottom:36px">&nbsp;</div>
      <strong>${{p2}}</strong><br>Part 2
    </div>
  </div>`;

  document.getElementById('dok-innhold').innerHTML = dok;
}}

function kopier() {{
  const el = document.getElementById('dok-innhold');
  navigator.clipboard.writeText(el.innerText).then(() => {{
    const kn = document.querySelector('.dok-kn.kopier');
    kn.textContent = '✓ Kopiert!';
    setTimeout(() => kn.textContent = 'Kopier tekst', 2500);
  }});
}}
oppdater();
</script>
{site_footer(depth=2)}"""


# ─────────────────────────────────────────────────────────────────────────────
# KONTRAKT 2: KJØPEKONTRAKT BIL
# ─────────────────────────────────────────────────────────────────────────────
def render_kontrakter_kjopekontraktbil():
    return f"""{shared_head(
        'Kjøpekontrakt bil — fyll ut og last ned gratis | Rettsregel',
        'Lag en juridisk korrekt kjøpekontrakt for privatbilsalg gratis. Dekker kjøper og selger, bilens tilstand, heftelser og betalingsbetingelser. Last ned som PDF.',
        depth=2, canonical_path='/kontrakter/kjopekontraktbil/'
    )}
{site_nav(depth=2)}
<style>
.bil-layout {{ display: grid; grid-template-columns: 400px 1fr; gap: 32px; align-items: start; margin-bottom: 64px; }}
.bil-layout > * {{ min-width: 0; }}
@media (max-width: 1100px) {{ .bil-layout {{ grid-template-columns: 1fr !important; }} }}
.bil-skjema {{ background: var(--bg-card); border: 1px solid var(--line); border-radius: 20px; padding: 28px; box-shadow: var(--shadow-md); position: sticky; top: 24px; }}
@media (max-width: 1100px) {{ .bil-skjema {{ position: static !important; }} }}
.bil-sek {{ margin-bottom: 20px; border-bottom: 1px solid var(--line); padding-bottom: 20px; }}
.bil-sek:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
.bil-sek-hd {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); margin-bottom: 12px; }}
.bf {{ margin-bottom: 10px; }}
.bf label {{ display: block; font-size: 12px; font-weight: 600; color: var(--ink-soft); margin-bottom: 4px; }}
.bf input, .bf select, .bf textarea {{ width: 100%; padding: 9px 12px; border: 1.5px solid var(--line); border-radius: 8px; font-family: var(--sans); font-size: 16px; background: var(--bg); color: var(--ink); box-sizing: border-box; }}
.bf input:focus, .bf select:focus, .bf textarea:focus {{ outline: none; border-color: var(--accent); }}
.bf textarea {{ min-height: 60px; resize: vertical; }}
.bf-rad {{ display: flex; flex-direction: column; gap: 6px; }}
.bf-rad label {{ display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 500; cursor: pointer; padding: 8px 12px; border: 1.5px solid var(--line); border-radius: 8px; line-height: 1.35; }}
.bf-rad input[type=radio], .bf-rad input[type=checkbox] {{ width: auto; margin: 0; accent-color: var(--accent); flex-shrink: 0; }}
.bf-rad label:has(input:checked) {{ border-color: var(--accent); background: rgba(177,74,42,0.06); color: var(--accent); font-weight: 600; }}
.bf-2kol {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }}
.status-badge {{ display: inline-flex; align-items: center; gap: 6px; padding: 8px 14px; border-radius: 8px; font-size: 12px; font-weight: 700; margin-bottom: 14px; }}
.status-badge.ok {{ background: #e8f4e8; color: #2d6a2d; border: 1px solid #8dcc8d; }}
.status-badge.advarsel {{ background: #fff3cd; color: #7d5f00; border: 1px solid #f0c040; }}
.last-ned-kn {{ width: 100%; background: var(--accent); color: white; border: none; border-radius: 12px; font-family: var(--sans); font-size: 15px; font-weight: 600; padding: 15px; cursor: pointer; margin-top: 20px; transition: background 0.2s; }}
.last-ned-kn:hover {{ background: var(--accent-deep); }}
/* Dokument */
.dok-wrap {{ background: var(--bg-alt); border-radius: 16px; padding: 24px; border: 1px solid var(--line); }}
.dok-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 10px; }}
.dok-header h3 {{ font-family: var(--serif); font-size: 18px; font-weight: 400; margin: 0; }}
.dok-kn-rad {{ display: flex; gap: 10px; }}
.dok-kn {{ padding: 8px 16px; border-radius: 8px; font-family: var(--sans); font-size: 13px; font-weight: 600; cursor: pointer; border: none; }}
.dok-kn.kopier {{ background: var(--accent); color: white; }}
.dok-kn.skriv {{ background: var(--bg-card); border: 1.5px solid var(--line); color: var(--ink); }}
.dok-dokument {{ background: white; border-radius: 12px; padding: 48px 52px; font-family: 'EB Garamond', Georgia, serif; font-size: 16px; line-height: 1.85; color: #1a1612; border: 1px solid var(--line); }}
@media (max-width: 600px) {{ .dok-dokument {{ padding: 24px 18px; font-size: 15px; }} }}
.dok-tom {{ color: var(--ink-mute); font-style: italic; font-family: var(--sans); font-size: 14px; padding: 32px 0; text-align: center; }}
.bil-boks {{ background: var(--bg-alt); border: 1.5px solid var(--line); border-radius: 12px; padding: 18px 20px; margin-bottom: 20px; font-family: var(--sans); font-size: 13px; }}
.bil-boks-rad {{ display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid var(--line); }}
.bil-boks-rad:last-child {{ border-bottom: none; }}
.bil-boks-rad span:first-child {{ color: var(--ink-soft); }}
.bil-boks-rad span:last-child {{ font-weight: 600; }}
.dok-sek {{ margin-bottom: 24px; }}
.dok-sek h2 {{ font-family: var(--sans); font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 10px; border-bottom: 1.5px solid #1a1612; padding-bottom: 5px; }}
.sign-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin-top: 48px; }}
.sign-boks {{ border-top: 1px solid #888; padding-top: 10px; font-family: var(--sans); font-size: 13px; color: #555; }}
@media (max-width: 600px) {{ .sign-grid {{ grid-template-columns: 1fr; }} }}
@media print {{
  .no-print {{ display: none !important; }}
  nav.site-nav, footer.site-footer, #chat-toggle, #chat-panel, .breadcrumbs, .article-header, .bil-skjema, .sp-body, .bil-boks, .status-badge {{ display: none !important; }}
  .bil-layout {{ display: block; }}
  .dok-wrap {{ border: none; padding: 0; background: white; }}
  .dok-dokument {{ border: none; padding: 0; box-shadow: none; font-size: 13pt; line-height: 1.7; }}
  body {{ background: white; }}
}}
</style>
<main class="page">
  <div class="container">
    <div class="breadcrumbs no-print">
      <a href="../../">Rettsregel</a><span class="sep">›</span>
      <a href="../../kontrakter/">Kontrakter</a><span class="sep">›</span>
      <span class="current">Kjøpekontrakt bil</span>
    </div>
    <div class="article-header no-print">
      <div class="article-eyebrow">Gratis kontraktsmal</div>
      <h1 class="article-title">Kjøpekontrakt bil — privatbilsalg</h1>
      <p class="article-description">Fyll ut om kjøper, selger og bilen. Kontrakten bygger seg live — last ned ferdig PDF.</p>
    </div>
    <div class="bil-layout">
      <div class="bil-skjema no-print">

        <div class="bil-sek">
          <div class="bil-sek-hd">Selger</div>
          <div class="bf"><label>Fullt navn</label><input id="s_navn" oninput="oppdater()" placeholder="Ola Nordmann"></div>
          <div class="bf"><label>Adresse</label><input id="s_adr" oninput="oppdater()" placeholder="Veien 1, 0000 Oslo"></div>
          <div class="bf"><label>Telefon / e-post</label><input id="s_kontakt" oninput="oppdater()" placeholder="900 00 000 / ola@epost.no"></div>
        </div>

        <div class="bil-sek">
          <div class="bil-sek-hd">Kjøper</div>
          <div class="bf"><label>Fullt navn</label><input id="k_navn" oninput="oppdater()" placeholder="Kari Nordmann"></div>
          <div class="bf"><label>Adresse</label><input id="k_adr" oninput="oppdater()" placeholder="Gata 2, 5000 Bergen"></div>
          <div class="bf"><label>Telefon / e-post</label><input id="k_kontakt" oninput="oppdater()" placeholder="911 22 333 / kari@epost.no"></div>
        </div>

        <div class="bil-sek">
          <div class="bil-sek-hd">Bilen</div>
          <div class="bf-2kol">
            <div class="bf"><label>Registreringsnummer</label><input id="bil_reg" oninput="oppdater()" placeholder="AB 12345" style="text-transform:uppercase"></div>
            <div class="bf"><label>Årsmodell</label><input id="bil_aar" oninput="oppdater()" type="number" placeholder="2018" min="1900" max="2030"></div>
          </div>
          <div class="bf-2kol">
            <div class="bf"><label>Merke</label><input id="bil_merke" oninput="oppdater()" placeholder="Toyota"></div>
            <div class="bf"><label>Modell</label><input id="bil_modell" oninput="oppdater()" placeholder="Corolla"></div>
          </div>
          <div class="bf-2kol">
            <div class="bf"><label>Kilometerstand</label><input id="bil_km" oninput="oppdater()" type="number" placeholder="87500" min="0"></div>
            <div class="bf"><label>Drivstoff</label>
              <select id="bil_drivstoff" onchange="oppdater()">
                <option value="Bensin">Bensin</option>
                <option value="Diesel">Diesel</option>
                <option value="Elektrisk">Elektrisk</option>
                <option value="Hybrid">Hybrid (plug-in)</option>
                <option value="Hybrid mild">Hybrid (mild)</option>
              </select>
            </div>
          </div>
          <div class="bf"><label>Chassisnummer (VIN) — valgfritt</label><input id="bil_vin" oninput="oppdater()" placeholder="XXXXXXXXXXXXXXXXX" maxlength="17" style="text-transform:uppercase"></div>
          <div class="bf"><label>EU-kontroll gyldig til</label><input id="bil_eu" oninput="oppdater()" type="month" placeholder="2026-10"></div>
        </div>

        <div class="bil-sek">
          <div class="bil-sek-hd">Pris og betaling</div>
          <div class="bf"><label>Avtalt kjøpesum (kr)</label><input id="pris" oninput="oppdater()" type="number" placeholder="185000" min="0"></div>
          <div class="bf"><label>Betalingsmåte</label>
            <div class="bf-rad">
              <label><input type="radio" name="betaling" value="overfor" onchange="oppdater()" checked> Bankoverføring</label>
              <label><input type="radio" name="betaling" value="vipps" onchange="oppdater()"> Vipps</label>
              <label><input type="radio" name="betaling" value="kontant" onchange="oppdater()"> Kontant</label>
            </div>
          </div>
          <div class="bf"><label>Betalingsfrist / overtagelsesdato</label><input id="dato" oninput="oppdater()" type="date"></div>
        </div>

        <div class="bil-sek">
          <div class="bil-sek-hd">Tilstand og heftelser</div>
          <div class="bf"><label>Er bilen fri for heftelser (pant, lån)?</label>
            <div class="bf-rad">
              <label><input type="radio" name="heftelser" value="fri" onchange="oppdater()" checked> Ja — fri for heftelser</label>
              <label><input type="radio" name="heftelser" value="har" onchange="oppdater()"> Nei — det er heftelser</label>
            </div>
          </div>
          <div id="heftelse-detaljer" class="bf" style="display:none">
            <label>Beskriv heftelsen(e)</label>
            <textarea id="heftelse_tekst" oninput="oppdater()" placeholder="f.eks. pant til DNB, restgjeld ca. 45 000 kr, innfris av selger ved overlevering"></textarea>
          </div>
          <div class="bf"><label>Kjente feil og mangler (valgfritt)</label>
            <textarea id="feil" oninput="oppdater()" placeholder="f.eks. ripe i venstre bakskjerm, klimaanlegg lader sakte. Selges ellers i kjørt stand."></textarea>
          </div>
          <div class="bf"><label>Medfølgende utstyr</label>
            <div class="bf-rad">
              <label><input type="checkbox" id="ekstra_hjul" onchange="oppdater()"> Ekstra hjulsett (sommerdekk / vinterdekk)</label>
              <label><input type="checkbox" id="ekstra_nokkel" onchange="oppdater()"> Ekstra nøkkel</label>
              <label><input type="checkbox" id="serviceheftet" onchange="oppdater()"> Serviceheftet</label>
            </div>
          </div>
          <div class="bf"><label>Annet utstyr som medfølger (valgfritt)</label>
            <input id="annet_utstyr" oninput="oppdater()" placeholder="f.eks. takboks, hengerfeste, varmekabler"></div>
        </div>

        <div class="bil-sek">
          <div class="bil-sek-hd">Garanti</div>
          <div class="bf">
            <div class="bf-rad">
              <label><input type="radio" name="garanti" value="ingen" onchange="oppdater()" checked> Selges uten garanti — «as is»</label>
              <label><input type="radio" name="garanti" value="garanti" onchange="oppdater()"> Selger gir begrenset garanti</label>
            </div>
          </div>
          <div id="garanti-detaljer" class="bf" style="display:none">
            <label>Beskriv garantien</label>
            <textarea id="garanti_tekst" oninput="oppdater()" placeholder="f.eks. 3 måneder garanti på motor og girkasse"></textarea>
          </div>
        </div>

        <div class="bil-sek">
          <div class="bil-sek-hd">Underskrift</div>
          <div class="bf"><label>Sted og dato</label><input id="sign_dato" oninput="oppdater()" placeholder="Oslo, 14. mai 2026"></div>
        </div>

        <button class="last-ned-kn no-print" onclick="window.print()">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="display:inline;vertical-align:middle;margin-right:6px"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7,10 12,15 17,10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Last ned som PDF
        </button>
      </div>

      <div>
        <!-- Live sammendrag -->
        <div class="bil-boks no-print" id="bil-sammendrag" style="display:none">
          <div class="bil-boks-rad"><span>Bil</span><span id="s-bil">—</span></div>
          <div class="bil-boks-rad"><span>Registreringsnr.</span><span id="s-reg">—</span></div>
          <div class="bil-boks-rad"><span>Kilometerstand</span><span id="s-km">—</span></div>
          <div class="bil-boks-rad"><span>EU-kontroll</span><span id="s-eu">—</span></div>
          <div class="bil-boks-rad"><span>Kjøpesum</span><span id="s-pris">—</span></div>
        </div>

        <div class="dok-wrap">
          <div class="dok-header">
            <h3>Din kjøpekontrakt</h3>
            <div class="dok-kn-rad no-print">
              <button class="dok-kn kopier" onclick="kopier()">Kopier tekst</button>
              <button class="dok-kn skriv" onclick="window.print()">Last ned PDF</button>
            </div>
          </div>
          <div class="dok-dokument" id="dok-innhold">
            <p class="dok-tom">Fyll ut feltene til venstre — kontrakten bygger seg her.</p>
          </div>
        </div>
      </div>
    </div>

    <div class="prose sp-body no-print">
      <h2>Hvorfor trenger du kjøpekontrakt ved privatbilsalg?</h2>
      <p>En kjøpekontrakt er det viktigste dokumentet ved privatbilsalg. Den beskytter begge parter: Selgeren er beskyttet mot senere krav om feil og mangler du ikke visste om, og kjøperen er beskyttet mot at selgeren kan nekte for hva som ble avtalt om pris, km-stand og tilstand.</p>
      <p>Uten kontrakt er det ord mot ord om hva som ble sagt over telefon eller på Finn.no. Med kontrakt er alt dokumentert.</p>
      <p>Husk alltid å sjekke bilen i Brønnøysundregistrene for heftelser (pant) FØR du betaler. Dette gjør du gratis på brreg.no. Heftelser på bilen kan i verste fall bety at banken tar bilen tilbake selv om du har betalt kjøpesummen til selgeren.</p>
      <p>Kontrakten skal signeres i to eksemplarer. Kjøper og selger beholder ett eksemplar hver.</p>
    </div>
  </div>
</main>
<script>
function radio(name) {{ return (document.querySelector('input[name="'+name+'"]:checked')||{{}}).value || ''; }}
function v(id) {{ const el=document.getElementById(id); return el ? el.value.trim() : ''; }}
function checked(id) {{ const el=document.getElementById(id); return el ? el.checked : false; }}
function kr(n) {{ const num=parseInt(n); return num ? num.toLocaleString('nb-NO')+' kr' : ''; }}
function dato(isoStr) {{
  if (!isoStr) return '';
  try {{
    const d = new Date(isoStr+'T12:00:00');
    return d.toLocaleDateString('nb-NO', {{day:'numeric',month:'long',year:'numeric'}});
  }} catch(e) {{ return isoStr; }}
}}
function euDato(monthStr) {{
  if (!monthStr) return '';
  const [y,m] = monthStr.split('-');
  const mnd = ['januar','februar','mars','april','mai','juni','juli','august','september','oktober','november','desember'];
  return mnd[parseInt(m)-1]+' '+y;
}}

function oppdater() {{
  const sNavn = v('s_navn') || 'Selger';
  const sAdr = v('s_adr');
  const sKontakt = v('s_kontakt');
  const kNavn = v('k_navn') || 'Kjøper';
  const kAdr = v('k_adr');
  const kKontakt = v('k_kontakt');
  const bilReg = v('bil_reg').toUpperCase();
  const bilAar = v('bil_aar');
  const bilMerke = v('bil_merke');
  const bilModell = v('bil_modell');
  const bilKm = v('bil_km');
  const bilDrivstoff = v('bil_drivstoff') || 'Bensin';
  const bilVin = v('bil_vin').toUpperCase();
  const bilEU = v('bil_eu');
  const pris = v('pris');
  const betaling = radio('betaling') || 'overfor';
  const datoStr = v('dato');
  const heftelser = radio('heftelser') || 'fri';
  const heftelserTekst = v('heftelse_tekst');
  const feil = v('feil');
  const garanti = radio('garanti') || 'ingen';
  const garantiTekst = v('garanti_tekst');
  const signDato = v('sign_dato');
  const harHjul = checked('ekstra_hjul');
  const harNokkel = checked('ekstra_nokkel');
  const harService = checked('serviceheftet');
  const annetUtstyr = v('annet_utstyr');

  // Toggle visibility
  document.getElementById('heftelse-detaljer').style.display = (heftelser === 'har') ? '' : 'none';
  document.getElementById('garanti-detaljer').style.display = (garanti === 'garanti') ? '' : 'none';

  const bilNavn = [bilAar, bilMerke, bilModell].filter(Boolean).join(' ') || 'Kjøretøyet';

  // Sammendrag
  const sammendrag = document.getElementById('bil-sammendrag');
  if (bilMerke || bilReg || pris) {{
    sammendrag.style.display = 'block';
    document.getElementById('s-bil').textContent = bilNavn || '—';
    document.getElementById('s-reg').textContent = bilReg || '—';
    document.getElementById('s-km').textContent = bilKm ? parseInt(bilKm).toLocaleString('nb-NO')+' km' : '—';
    document.getElementById('s-eu').textContent = bilEU ? euDato(bilEU) : '—';
    document.getElementById('s-pris').textContent = kr(pris) || '—';
  }} else {{
    sammendrag.style.display = 'none';
  }}

  if (!v('s_navn') && !v('k_navn') && !bilMerke && !pris) {{
    document.getElementById('dok-innhold').innerHTML = '<p class="dok-tom">Fyll ut feltene til venstre — kontrakten bygger seg her.</p>';
    return;
  }}

  // Betalings-tekst
  const betalingMap = {{ overfor: 'bankoverføring', vipps: 'Vipps', kontant: 'kontant' }};
  const betalingTekst = betalingMap[betaling] || 'bankoverføring';

  // Utstyr-liste
  let utstyrListe = [];
  if (harHjul) utstyrListe.push('ekstra hjulsett');
  if (harNokkel) utstyrListe.push('ekstra nøkkel');
  if (harService) utstyrListe.push('serviceheftet');
  if (annetUtstyr) utstyrListe.push(annetUtstyr);

  let dok = `
  <div style="text-align:center;margin-bottom:36px">
    <div style="font-family:var(--sans);font-size:11px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#888;margin-bottom:8px">Privatbilsalg</div>
    <h1 style="font-family:var(--sans);font-size:22px;font-weight:700;text-transform:uppercase;letter-spacing:0.04em;margin:0">Kjøpekontrakt</h1>
    <div style="font-family:var(--sans);font-size:14px;color:#555;margin-top:6px">${{bilNavn}}${{bilReg?' — Reg.nr. '+bilReg:''}}</div>
  </div>

  <div class="dok-sek">
    <h2>§ 1 — Parter</h2>
    <p><strong>Selger:</strong> ${{sNavn}}${{sAdr?', '+sAdr:''}}${{sKontakt?', '+sKontakt:''}}</p>
    <p style="margin-top:8px"><strong>Kjøper:</strong> ${{kNavn}}${{kAdr?', '+kAdr:''}}${{kKontakt?', '+kKontakt:''}}</p>
  </div>

  <div class="dok-sek">
    <h2>§ 2 — Kjøretøy</h2>
    <table style="width:100%;border-collapse:collapse;font-family:var(--sans);font-size:14px">
      ${{bilMerke?'<tr><td style="padding:5px 0;color:#666;width:40%">Merke og modell</td><td style="padding:5px 0;font-weight:600">'+[bilMerke,bilModell].filter(Boolean).join(' ')+'</td></tr>':''}}
      ${{bilReg?'<tr><td style="padding:5px 0;color:#666">Registreringsnr.</td><td style="padding:5px 0;font-weight:600">'+bilReg+'</td></tr>':''}}
      ${{bilAar?'<tr><td style="padding:5px 0;color:#666">Årsmodell</td><td style="padding:5px 0;font-weight:600">'+bilAar+'</td></tr>':''}}
      ${{bilDrivstoff?'<tr><td style="padding:5px 0;color:#666">Drivstoff</td><td style="padding:5px 0;font-weight:600">'+bilDrivstoff+'</td></tr>':''}}
      ${{bilKm?'<tr><td style="padding:5px 0;color:#666">Kilometerstand</td><td style="padding:5px 0;font-weight:600">'+parseInt(bilKm).toLocaleString('nb-NO')+' km ved salg</td></tr>':''}}
      ${{bilEU?'<tr><td style="padding:5px 0;color:#666">EU-kontroll gyldig til</td><td style="padding:5px 0;font-weight:600">'+euDato(bilEU)+'</td></tr>':''}}
      ${{bilVin?'<tr><td style="padding:5px 0;color:#666">Chassisnummer (VIN)</td><td style="padding:5px 0;font-weight:600">'+bilVin+'</td></tr>':''}}
    </table>
  </div>

  <div class="dok-sek">
    <h2>§ 3 — Kjøpesum og betaling</h2>
    <p>Avtalt kjøpesum er <strong>${{kr(pris) || '[sum ikke angitt]'}}</strong>, å betale ved ${{betalingTekst}}${{datoStr?' innen '+dato(datoStr):''}}.</p>
    <p style="margin-top:10px">Kjøretøyet overleveres til kjøper når kjøpesummen er mottatt og bekreftet av selger. Eierskifte registreres av kjøper og selger på vegne av hverandre i Statens vegvesen sitt eierskiftesystem.</p>
  </div>

  <div class="dok-sek">
    <h2>§ 4 — Heftelser</h2>`;

  if (heftelser === 'fri') {{
    dok += `<p>Selger bekrefter at kjøretøyet er fritt for heftelser, herunder pant og registrert i Løsøreregisteret. Kjøper oppfordres til å kontrollere dette på brreg.no eller via tinglysing.no.</p>`;
  }} else {{
    dok += `<p>Kjøretøyet har følgende registrerte heftelser: ${{heftelserTekst || '[beskriv heftelsene]'}}</p>`;
  }}

  dok += `</div>

  <div class="dok-sek">
    <h2>§ 5 — Tilstand og kjente feil</h2>`;

  if (feil) {{
    dok += `<p>Selger gjør kjøper oppmerksom på følgende kjente feil og mangler ved kjøretøyet:</p><p style="margin-top:8px;font-style:italic">${{feil}}</p>`;
  }} else {{
    dok += `<p>Selger kjenner ikke til andre feil eller mangler enn det som fremkommer av bilens naturlige slitasje ved ${{bilKm?parseInt(bilKm).toLocaleString('nb-NO')+' km':'oppgitt kilometerstand'}} og alder.</p>`;
  }}

  if (garanti === 'ingen') {{
    dok += `<p style="margin-top:10px">Kjøretøyet selges i den stand det er ved besiktigelse, og uten garanti fra selger. Kjøper har hatt anledning til å besiktige bilen og er kjent med dens stand.</p>`;
  }} else {{
    dok += `<p style="margin-top:10px">Selger gir følgende garanti: ${{garantiTekst || '[beskriv garantien]'}}</p>`;
  }}

  dok += `</div>`;

  if (utstyrListe.length > 0) {{
    dok += `<div class="dok-sek"><h2>§ 6 — Medfølgende utstyr</h2><p>Følgende utstyr inngår i handelen: ${{utstyrListe.join(', ')}}.</p></div>`;
  }}

  const neste = utstyrListe.length > 0 ? '7' : '6';

  dok += `
  <div class="dok-sek">
    <h2>§ ${{neste}} — Ansvar og reklamasjon</h2>
    <p>Denne kontrakten er et privatbilsalg mellom to privatpersoner. Kjøpsloven gjelder for handelen. Kjøper er kjent med at selger ikke er næringsdrivende og at reklamasjonsrettighetene etter forbrukerkjøpsloven dermed ikke gjelder.</p>
    <p style="margin-top:10px">Eventuelle reklamasjoner på feil og mangler som selger hadde kunnskap om men unnlot å opplyse om, behandles etter kjøpslovens bestemmelser om heving og prisavslag.</p>
  </div>

  <div style="margin-top:40px;font-family:var(--sans);font-size:14px;color:#555;border-top:1px solid #ddd;padding-top:16px;">
    <p>Kontrakten er utferdiget i to originale eksemplarer. Kjøper og selger beholder ett eksemplar hver.</p>
    <p style="margin-top:6px">Sted og dato: <strong>${{signDato || '________________________'}}</strong></p>
  </div>

  <div class="sign-grid">
    <div class="sign-boks">
      <div style="margin-bottom:40px">&nbsp;</div>
      <strong>${{sNavn}}</strong><br>Selger
    </div>
    <div class="sign-boks">
      <div style="margin-bottom:40px">&nbsp;</div>
      <strong>${{kNavn}}</strong><br>Kjøper
    </div>
  </div>`;

  document.getElementById('dok-innhold').innerHTML = dok;
}}

function kopier() {{
  const el = document.getElementById('dok-innhold');
  navigator.clipboard.writeText(el.innerText).then(() => {{
    const kn = document.querySelector('.dok-kn.kopier');
    kn.textContent = '✓ Kopiert!';
    setTimeout(() => kn.textContent = 'Kopier tekst', 2500);
  }});
}}
oppdater();
</script>
{site_footer(depth=2)}"""


def build():
    out = "/home/claude/site/dist"
    # Bygg fortsatt til dist/ i Claudes workdir — men zip-leveransen pakker flat
    # slik at filene havner direkte i rota av Martins rett-mappe.
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
    
    # Shared CSS at root
    with open(f"{out}/styles.css", "w", encoding="utf-8") as f:
        f.write(CSS)
    
    # Homepage
    with open(f"{out}/index.html", "w", encoding="utf-8") as f:
        f.write(render_homepage())
    
    # Personvern page
    os.makedirs(f"{out}/personvern", exist_ok=True)
    with open(f"{out}/personvern/index.html", "w", encoding="utf-8") as f:
        f.write(render_personvern())
    
    # Om page
    os.makedirs(f"{out}/om", exist_ok=True)
    with open(f"{out}/om/index.html", "w", encoding="utf-8") as f:
        f.write(render_om())
    
    # Kontakt page (kun skjema)
    os.makedirs(f"{out}/kontakt", exist_ok=True)
    with open(f"{out}/kontakt/index.html", "w", encoding="utf-8") as f:
        f.write(render_kontakt())
    
    # Lover index
    os.makedirs(f"{out}/lover", exist_ok=True)
    with open(f"{out}/lover/index.html", "w", encoding="utf-8") as f:
        f.write(render_lover_index())
    
    # Group paragraphs by lov
    by_lov = {}
    for p in PARAGRAPHS:
        by_lov.setdefault(p["lov"], []).append(p)
    
    # For each lov: build index + paragraph pages
    for lov_name, items in by_lov.items():
        items.sort(key=paragraf_sort_key)
        lov_display = items[0]["lov_display"]
        
        os.makedirs(f"{out}/lover/{lov_name}", exist_ok=True)
        with open(f"{out}/lover/{lov_name}/index.html", "w", encoding="utf-8") as f:
            f.write(render_lov_index(lov_name, lov_display, items))
        
        for p in items:
            os.makedirs(f"{out}/lover/{lov_name}/{p['number']}", exist_ok=True)
            with open(f"{out}/lover/{lov_name}/{p['number']}/index.html", "w", encoding="utf-8") as f:
                f.write(render_paragraph_page(p))
    
    # Spørsmål-artikler
    if SPORSMAL:
        os.makedirs(f"{out}/sporsmal", exist_ok=True)
        with open(f"{out}/sporsmal/index.html", "w", encoding="utf-8") as f:
            f.write(render_sporsmal_hub())
        for s in SPORSMAL:
            os.makedirs(f"{out}/sporsmal/{s['slug']}", exist_ok=True)
            with open(f"{out}/sporsmal/{s['slug']}/index.html", "w", encoding="utf-8") as f:
                f.write(render_sporsmal_page(s))

    # Tjenester
    os.makedirs(f"{out}/tjenester", exist_ok=True)
    with open(f"{out}/tjenester/index.html", "w", encoding="utf-8") as f:
        f.write(render_tjenester_hub())
    os.makedirs(f"{out}/tjenester/enk-eller-as", exist_ok=True)
    with open(f"{out}/tjenester/enk-eller-as/index.html", "w", encoding="utf-8") as f:
        f.write(render_enk_eller_as())
    os.makedirs(f"{out}/tjenester/reklamasjon-bil", exist_ok=True)
    with open(f"{out}/tjenester/reklamasjon-bil/index.html", "w", encoding="utf-8") as f:
        f.write(render_tjenester_reklamasjon_bil())
    os.makedirs(f"{out}/tjenester/reklamasjon", exist_ok=True)
    with open(f"{out}/tjenester/reklamasjon/index.html", "w", encoding="utf-8") as f:
        f.write(render_tjenester_reklamasjon())
    os.makedirs(f"{out}/tjenester/arv", exist_ok=True)
    with open(f"{out}/tjenester/arv/index.html", "w", encoding="utf-8") as f:
        f.write(render_tjenester_arv())
    os.makedirs(f"{out}/tjenester/leie-okning", exist_ok=True)
    with open(f"{out}/tjenester/leie-okning/index.html", "w", encoding="utf-8") as f:
        f.write(render_tjenester_leie_okning())
    os.makedirs(f"{out}/tjenester/inkasso", exist_ok=True)
    with open(f"{out}/tjenester/inkasso/index.html", "w", encoding="utf-8") as f:
        f.write(render_tjenester_inkasso())

    # Kontrakter
    os.makedirs(f"{out}/kontrakter", exist_ok=True)
    with open(f"{out}/kontrakter/index.html", "w", encoding="utf-8") as f:
        f.write(render_kontrakter_hub())
    os.makedirs(f"{out}/kontrakter/husleiekontrakt", exist_ok=True)
    with open(f"{out}/kontrakter/husleiekontrakt/index.html", "w", encoding="utf-8") as f:
        f.write(render_kontrakter_husleiekontrakt())
    os.makedirs(f"{out}/kontrakter/samboeravtale", exist_ok=True)
    with open(f"{out}/kontrakter/samboeravtale/index.html", "w", encoding="utf-8") as f:
        f.write(render_kontrakter_samboeravtale())
    os.makedirs(f"{out}/kontrakter/kjopekontraktbil", exist_ok=True)
    with open(f"{out}/kontrakter/kjopekontraktbil/index.html", "w", encoding="utf-8") as f:
        f.write(render_kontrakter_kjopekontraktbil())
    
    # Sitemap.xml
    today = "2026-05-11"
    urls = [
        ("/", "1.0"),
        ("/lover/", "0.9"),
        ("/om/", "0.5"),
        ("/kontakt/", "0.7"),
        ("/personvern/", "0.3"),
    ]
    for lov_name, items in by_lov.items():
        lov_url = lov_name.replace("ø", "o").replace("æ", "ae").replace("å", "aa")
        urls.append((f"/lover/{lov_url}/", "0.8"))
        for p in items:
            urls.append((f"/lover/{lov_url}/{p['number']}/", "0.7"))
    
    if SPORSMAL:
        urls.append(("/sporsmal/", "0.9"))
        for s in SPORSMAL:
            urls.append((f"/sporsmal/{s['slug']}/", "0.8"))

    urls.append(("/tjenester/", "0.8"))
    urls.append(("/tjenester/enk-eller-as/", "0.8"))
    urls.append(("/tjenester/reklamasjon-bil/", "0.8"))
    urls.append(("/kontrakter/", "0.8"))
    urls.append(("/kontrakter/husleiekontrakt/", "0.8"))
    urls.append(("/advokatvurdering/", "0.9"))
    
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for path, priority in urls:
        sitemap += f'  <url>\n    <loc>{SITE_URL}{path}</loc>\n    <lastmod>{today}</lastmod>\n    <priority>{priority}</priority>\n  </url>\n'
    sitemap += '</urlset>\n'
    with open(f"{out}/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)
    
    # robots.txt
    robots = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    with open(f"{out}/robots.txt", "w", encoding="utf-8") as f:
        f.write(robots)
    
    # CNAME (forteller GitHub Pages om custom domain)
    with open(f"{out}/CNAME", "w", encoding="utf-8") as f:
        f.write("rettsregel.no\n")
    
    # advokatvurdering — statisk side, kopieres direkte til dist
    _src_dir = os.path.dirname(os.path.abspath(__file__))
    _av_src = os.path.join(_src_dir, "advokatvurdering", "index.html")
    if os.path.exists(_av_src):
        os.makedirs(f"{out}/advokatvurdering", exist_ok=True)
        shutil.copy(_av_src, f"{out}/advokatvurdering/index.html")

    # Logo-assets + favicons (kopieres fra repo-roten)
    src_dir = os.path.dirname(os.path.abspath(__file__))
    for asset in ("logo.svg", "logo.png", "favicon.svg", "favicon-32.png", "favicon-180.png", "favicon-512.png", "apple-touch-icon.png"):
        src_path = os.path.join(src_dir, asset)
        if os.path.exists(src_path):
            shutil.copy(src_path, os.path.join(out, asset))
    
    # paragraphs-index.json — kompakt indeks for søk og chatbot
    # Inneholder både paragrafer og spørsmål-artikler
    index = []
    for p in PARAGRAPHS:
        index.append({
            "type": "paragraf",
            "number": p["number"],
            "lov": p["lov"],
            "lov_display": p["lov_display"],
            "title": p["title"],
            "kort_svar": p.get("kort_svar", ""),
            "kategori": p.get("kategori", ""),
        })
    for s in SPORSMAL:
        index.append({
            "type": "sporsmal",
            "slug": s["slug"],
            "title": s["title"],
            "kort_svar": s.get("kort_svar", ""),
            "description": s.get("description", ""),
            "kategori": s.get("kategori", ""),
        })
    with open(f"{out}/paragraphs-index.json", "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=None, separators=(",", ":"))
    
    print(f"Built {len(PARAGRAPHS)} paragraph pages + {len(SPORSMAL)} sporsmal-artikler + homepage + lov index + lover index + personvern + om")
    print(f"Plus: sitemap.xml ({len(urls)} URLs), robots.txt, CNAME, paragraphs-index.json")
    print(f"Output: {out}")

if __name__ == "__main__":
    build()
