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

PARAGRAPHS = _P_BASE + _P_KJOPSLOVEN + _P_HUSLEIELOVEN + _P_AVHENDINGSLOVA + _P_NABOLOVEN + _P_NAVNELOVEN + _P_FKL + _P_ARVELOVEN + _P_BUSTAD

# Spørsmål-artikler (lever på /sporsmal/[slug]/)
try:
    from sporsmal_data import SPORSMAL
except ImportError:
    SPORSMAL = []

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
  --ink-mute: #9B8E82;
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
  --serif: 'Fraunces', 'Palatino', 'Palatino Linotype', 'Book Antiqua', Georgia, serif;
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

nav.site-nav {
  padding: 44px 0 38px; display: flex;
  justify-content: space-between; align-items: center;
  border-bottom: 1px solid var(--line);
  margin-bottom: 0;
}
.logo {
  display: inline-flex; align-items: center; gap: 10px;
  text-decoration: none; line-height: 1;
}
.logo-mark {
  width: 32px; height: 32px; flex-shrink: 0;
  display: inline-flex; align-items: center; justify-content: center;
  position: relative; top: -1px;
}
.logo-mark svg { width: 100%; height: 100%; display: block; }
.logo-mark .glyph { fill: var(--accent); transition: fill 0.2s; }
.logo-wordmark {
  font-family: var(--serif); font-weight: 400;
  font-size: 44px; letter-spacing: -0.022em;
  color: var(--ink); line-height: 1;
  transition: color 0.2s;
  font-feature-settings: "liga" 1, "dlig" 1, "kern" 1;
  font-variation-settings: "opsz" 60, "SOFT" 50;
}
.logo-tld {
  color: var(--accent); font-weight: 500;
  letter-spacing: -0.025em;
}
.logo:hover .logo-wordmark { color: var(--ink-soft); }
.nav-links { display: flex; gap: 36px; list-style: none; }
.nav-links a {
  color: var(--ink-mute); text-decoration: none;
  font-size: 13.5px; font-weight: 500; transition: color 0.18s;
  letter-spacing: 0.01em;
}
.nav-links a:hover { color: var(--ink); }
@media (max-width: 720px) {
  .nav-links { gap: 20px; }
  .nav-links a { font-size: 13px; }
  .logo-wordmark { font-size: 32px; }
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
  font-variation-settings: "opsz" 48;
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
  font-variation-settings: "opsz" 22;
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
  font-variation-settings: "opsz" 36;
  color: var(--ink);
}
.article-body h2 + p, .article-body h2 + ul, .article-body h2 + ol { margin-top: 0; }
.article-body h3 {
  font-family: var(--serif); font-weight: 500; font-size: 22px;
  line-height: 1.3; margin: 32px 0 12px; letter-spacing: -0.005em;
  font-variation-settings: "opsz" 24;
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
  font-variation-settings: "opsz" 18;
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
  font-variation-settings: "opsz" 18;
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
  font-variation-settings: "opsz" 24;
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
  font-variation-settings: "opsz" 20;
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
  font-variation-settings: "opsz" 60;
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
.form-success h3 { font-family: var(--serif); font-size: 24px; margin-bottom: 10px; font-variation-settings: "opsz" 28; }
.form-success p { color: var(--ink-soft); }

/* Footer — warm light redesign */
footer.site-footer {
  background: var(--bg);
  color: var(--ink-soft);
  padding: 64px 0 40px;
  margin-top: 80px;
  border-top: 1px solid var(--line);
}
.footer-inner {
  display: grid; grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 48px; margin-bottom: 48px;
}
@media (max-width: 900px) { .footer-inner { grid-template-columns: 1fr 1fr; gap: 32px 40px; } }
@media (max-width: 540px) { .footer-inner { grid-template-columns: 1fr; gap: 28px; } }
.footer-logo {
  display: flex; align-items: baseline; gap: 9px;
  text-decoration: none; margin-bottom: 16px; line-height: 1;
}
.footer-logo-mark {
  font-family: var(--serif); font-size: 30px;
  color: var(--accent); line-height: 0.85; position: relative; top: 3px;
}
.footer-logo-name {
  font-family: var(--serif); font-size: 36px;
  letter-spacing: -0.022em; color: var(--ink);
  font-variation-settings: "opsz" 60;
}
.footer-tagline {
  font-family: var(--serif); font-size: 15px; line-height: 1.65; font-style: italic;
  color: var(--ink-mute); max-width: 240px; margin-bottom: 20px;
}
.footer-entity {
  font-size: 11px; color: var(--ink-mute);
  text-transform: uppercase; letter-spacing: 0.12em;
}
.footer-col-head {
  font-size: 11px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.16em; color: var(--ink-soft); margin-bottom: 18px;
}
footer.site-footer ul { list-style: none; }
footer.site-footer li { margin-bottom: 12px; }
footer.site-footer a {
  color: var(--ink-mute); text-decoration: none; font-size: 14px;
  transition: color 0.18s;
}
footer.site-footer a:hover { color: var(--accent); }
.footer-bottom {
  display: flex; justify-content: space-between; align-items: center;
  flex-wrap: wrap; gap: 10px;
  padding-top: 24px; border-top: 1px solid var(--line);
  font-size: 12px; color: var(--ink-mute); letter-spacing: 0.01em;
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
  font-variation-settings: "opsz" 60;
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
  font-variation-settings: "opsz" 36;
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
  font-variation-settings: "opsz" 60;
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
  font-variation-settings: "opsz" 28;
}
.om-section p {
  font-family: var(--serif);
  font-weight: 400;
  font-size: 21px;
  line-height: 1.6;
  color: var(--ink);
  margin-bottom: 18px;
  font-variation-settings: "opsz" 22;
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
  font-family: var(--serif); font-size: clamp(22px, 2.4vw, 28px);
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
  font-family: var(--serif); font-size: clamp(22px, 2.4vw, 28px);
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
  font-variation-settings: "opsz" 48;
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
.chat-toggle {
  position: fixed; bottom: 24px; right: 24px; z-index: 1000;
  background: var(--accent); color: white;
  border: none; border-radius: 999px;
  padding: 14px 22px; font-family: var(--sans);
  font-size: 15px; font-weight: 600;
  cursor: pointer; box-shadow: 0 4px 16px rgba(31,26,20,0.18);
  transition: transform 0.15s, box-shadow 0.15s;
  display: inline-flex; align-items: center; gap: 8px;
}
.chat-toggle:hover { transform: translateY(-1px); box-shadow: 0 6px 20px rgba(31,26,20,0.22); }
.chat-toggle:focus { outline: 2px solid var(--accent); outline-offset: 3px; }
.chat-toggle .chat-toggle-icon { font-size: 18px; line-height: 1; }
.chat-toggle.open { display: none; }

.chat-panel {
  position: fixed; bottom: 24px; right: 24px; z-index: 1001;
  width: 380px; max-width: calc(100vw - 32px);
  height: 560px; max-height: calc(100vh - 48px);
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 16px;
  box-shadow: 0 12px 40px rgba(31,26,20,0.22);
  display: none; flex-direction: column; overflow: hidden;
}
.chat-panel.open { display: flex; }

.chat-header {
  background: var(--ink); color: var(--bg);
  padding: 14px 18px; display: flex; align-items: center; justify-content: space-between;
}
.chat-header-title { font-family: var(--serif); font-size: 18px; font-weight: 500; }
.chat-header-sub { font-size: 12px; color: rgba(250,246,238,0.65); margin-top: 2px; }
.chat-close {
  background: transparent; color: var(--bg); border: none;
  font-size: 22px; line-height: 1; cursor: pointer; padding: 4px 10px;
  border-radius: 6px;
}
.chat-close:hover { background: rgba(250,246,238,0.1); }

.chat-disclaimer {
  background: rgba(194,84,52,0.08);
  border-bottom: 1px solid var(--line);
  padding: 10px 16px; font-size: 12px; color: var(--ink-soft);
  font-family: var(--sans); line-height: 1.45;
}

.chat-messages {
  flex: 1; overflow-y: auto; padding: 16px;
  display: flex; flex-direction: column; gap: 12px;
  font-family: var(--sans); font-size: 14px;
}
.chat-message {
  padding: 10px 14px; border-radius: 12px;
  max-width: 88%; line-height: 1.5;
  word-wrap: break-word;
}
.chat-message.user {
  background: var(--accent); color: white;
  align-self: flex-end; border-bottom-right-radius: 4px;
}
.chat-message.bot {
  background: white; color: var(--ink);
  align-self: flex-start; border: 1px solid var(--line);
  border-bottom-left-radius: 4px;
}
.chat-message a {
  color: var(--accent); text-decoration: underline;
}
.chat-message.user a { color: white; }
.chat-message a.chat-cta { text-decoration: none; }
.chat-message.bot.loading { font-style: italic; color: var(--ink-soft); }

.chat-ctas {
  margin-top: 12px;
  display: flex !important; gap: 8px; flex-wrap: wrap;
}
.chat-cta {
  display: inline-block; padding: 8px 14px;
  border-radius: 8px; font-size: 13px; font-weight: 600;
  text-decoration: none !important;
  font-family: var(--sans);
  transition: background 0.15s, transform 0.1s;
  cursor: pointer; border: none;
  line-height: 1.3;
}
.chat-cta:hover { transform: translateY(-1px); }
.chat-message .chat-cta-secondary {
  background: rgba(31,26,20,0.06); color: var(--ink);
}
.chat-message .chat-cta-secondary:hover { background: rgba(31,26,20,0.12); }
.chat-message .chat-cta-primary {
  background: var(--accent); color: white;
}
.chat-message .chat-cta-primary:hover { background: #A8451F; }

.chat-input-bar {
  border-top: 1px solid var(--line);
  padding: 12px 14px; display: flex; gap: 8px;
  background: white;
}
.chat-input {
  flex: 1; font-family: var(--sans); font-size: 14px;
  padding: 10px 12px; border: 1px solid var(--line);
  border-radius: 8px; background: var(--bg); color: var(--ink);
}
.chat-input:focus { outline: none; border-color: var(--accent); }
.chat-send {
  background: var(--accent); color: white; border: none;
  border-radius: 8px; padding: 10px 16px;
  font-family: var(--sans); font-weight: 600; font-size: 14px;
  cursor: pointer;
}
.chat-send:hover { background: #A8451F; }
.chat-send:disabled { opacity: 0.5; cursor: not-allowed; }

@media (max-width: 480px) {
  .chat-panel {
    width: calc(100vw - 16px); height: calc(100vh - 80px);
    bottom: 70px; right: 8px;
  }
  .chat-toggle { bottom: 16px; right: 16px; padding: 12px 18px; font-size: 14px; }
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
<meta property="og:type" content="website">
<meta property="og:site_name" content="Rettsregel">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical_url}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT,WONK@9..144,300..700,30..100,0..1&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}styles.css">
</head>
<body>"""

def site_nav(depth=0):
    prefix = "../" * depth
    return f"""<div class="container">
<nav class="site-nav">
  <a href="{prefix}" class="logo"><span class="logo-wordmark">Rettsregel<span class="logo-tld">.no</span></span></a>
  <ul class="nav-links">
    <li><a href="{prefix}tjenester/">Verktøy</a></li>
    <li><a href="{prefix}lover/">Lover</a></li>
    <li><a href="{prefix}sporsmal/">Spørsmål</a></li>
    <li><a href="{prefix}om/">Om</a></li>
  </ul>
</nav>
</div>"""

def chat_widget():
    """Returns HTML + JS for the chat widget. Inserted before </body> on every page."""
    return """<!-- Rettsregel chat widget -->
<button id="chat-toggle" class="chat-toggle" aria-label="Åpne Roy">
  <span class="chat-toggle-icon">💬</span>
  <span>Spør Roy</span>
</button>
<div id="chat-panel" class="chat-panel" role="dialog" aria-labelledby="chat-title">
  <div class="chat-header">
    <div>
      <div id="chat-title" class="chat-header-title">Roy</div>
      <div class="chat-header-sub">Forklarer loven på vanlig norsk</div>
    </div>
    <button id="chat-close" class="chat-close" aria-label="Lukk">×</button>
  </div>
  <div class="chat-disclaimer">
    AI-assistent. Generell informasjon — kan gjøre feil.
  </div>
  <div id="chat-messages" class="chat-messages">
    <div class="chat-message bot">Hei, jeg er Roy. Beskriv problemet ditt med dine egne ord — så finner jeg riktig paragraf og forklarer hva som gjelder.</div>
  </div>
  <form id="chat-form" class="chat-input-bar">
    <input type="text" id="chat-input" class="chat-input" placeholder="Skriv som du tenker..." maxlength="1000" autocomplete="off">
    <button type="submit" id="chat-send" class="chat-send">Send</button>
  </form>
</div>
<script>
(function() {
  var WORKER_URL = "https://rettsregel-bot.brys4ypd5x.workers.dev";
  var toggle = document.getElementById('chat-toggle');
  var panel = document.getElementById('chat-panel');
  var closeBtn = document.getElementById('chat-close');
  var messages = document.getElementById('chat-messages');
  var form = document.getElementById('chat-form');
  var input = document.getElementById('chat-input');
  var sendBtn = document.getElementById('chat-send');
  var history = [];

  function openPanel() {
    panel.classList.add('open');
    toggle.classList.add('open');
    setTimeout(function(){ input.focus(); }, 100);
  }
  function closePanel() {
    panel.classList.remove('open');
    toggle.classList.remove('open');
  }
  toggle.addEventListener('click', openPanel);
  closeBtn.addEventListener('click', closePanel);

  function escapeHtml(s) {
    return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  function extractAndStripUrl(text) {
    // Henter ut paragraf-URL fra slutten av svaret, fjerner "Les hele..."-linjen
    var match = text.match(/(https:\\/\\/rettsregel\\.no\\/lover\\/[^\\s]+?\\/)/);
    if (!match) return { text: text, url: null };
    var url = match[1];
    // Fjern hele linjen "Les hele forklaringen på: URL" eller bare URLen
    var cleaned = text
      .replace(/\\s*Les hele forklaringen på:?\\s*https:\\/\\/rettsregel\\.no\\/lover\\/[^\\s]+\\/?\\s*$/i, '')
      .replace(/\\s*https:\\/\\/rettsregel\\.no\\/lover\\/[^\\s]+\\/?\\s*$/i, '')
      .trim();
    return { text: cleaned, url: url };
  }

  function addUserMessage(content) {
    var div = document.createElement('div');
    div.className = 'chat-message user';
    div.textContent = content;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  function addBotMessage(rawContent) {
    var parsed = extractAndStripUrl(rawContent);
    var div = document.createElement('div');
    div.className = 'chat-message bot';
    div.innerHTML = escapeHtml(parsed.text).replace(/\\n/g, '<br>');

    if (parsed.url) {
      var ctas = document.createElement('div');
      ctas.className = 'chat-ctas';
      ctas.innerHTML =
        '<a href="' + parsed.url + '" class="chat-cta chat-cta-secondary">Les hele paragrafen</a>' +
        '<a href="' + parsed.url + '#skjema" class="chat-cta chat-cta-primary">Send inn saken</a>';
      div.appendChild(ctas);
    }
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  function addLoading() {
    var div = document.createElement('div');
    div.className = 'chat-message bot loading';
    div.id = 'chat-loading';
    div.textContent = 'Tenker...';
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }
  function removeLoading() {
    var el = document.getElementById('chat-loading');
    if (el) el.remove();
  }

  form.addEventListener('submit', function(e) {
    e.preventDefault();
    var text = input.value.trim();
    if (!text) return;
    addUserMessage(text);
    input.value = '';
    sendBtn.disabled = true;
    addLoading();

    fetch(WORKER_URL, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({message: text, history: history})
    })
    .then(function(res) { return res.json(); })
    .then(function(data) {
      removeLoading();
      sendBtn.disabled = false;
      if (data.error) {
        addBotMessage(data.error);
      } else {
        addBotMessage(data.reply);
        history.push({role: 'user', content: text});
        history.push({role: 'assistant', content: data.reply});
        if (history.length > 12) history = history.slice(-12);
      }
    })
    .catch(function() {
      removeLoading();
      sendBtn.disabled = false;
      addBotMessage('Noe gikk galt. Sjekk nettforbindelsen og prøv igjen.');
    });
  });
})();
</script>"""

def site_footer(depth=0):
    prefix = "../" * depth
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-inner">
      <div>
        <a href="{prefix}" class="footer-logo">
          <span class="footer-logo-name">Rettsregel<span style="color:var(--accent);font-weight:500">.no</span></span>
        </a>
        <p class="footer-tagline">Lover er ikke vanskelige.<br>De er bare dårlig forklart.</p>
        <span class="footer-entity">Walrus AS</span>
      </div>
      <div>
        <div class="footer-col-head">Lover</div>
        <ul>
          <li><a href="{prefix}lover/">Lover</a></li>
          <li><a href="{prefix}lover/husleieloven/">Husleieloven</a></li>
          <li><a href="{prefix}lover/arveloven/">Arveloven</a></li>
          <li><a href="{prefix}lover/kjopsloven/">Kjøpsloven</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-col-head">Verktøy</div>
        <ul>
          <li><a href="{prefix}tjenester/">Alle verktøy</a></li>
          <li><a href="{prefix}tjenester/reklamasjon/">Reklamasjonsbrev</a></li>
          <li><a href="{prefix}tjenester/arv/">Arveoppgjør</a></li>
          <li><a href="{prefix}kontrakter/samboeravtale/">Samboeravtale</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-col-head">Om</div>
        <ul>
          <li><a href="{prefix}om/">Om Rettsregel</a></li>
          <li><a href="{prefix}sporsmal/">Spørsmål og svar</a></li>
          <li><a href="{prefix}personvern/">Personvern</a></li>
          <li><a href="mailto:rettsregel@gmail.com">Kontakt</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Walrus AS · Rettsregel.no</span>
      <span>Juridisk informasjon, ikke rådgivning.</span>
    </div>
  </div>
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
    depth = 3  # /lover/[lov]/[n]/index.html
    prefix = "../" * depth
    
    # Auto-compute which related paragraphs actually exist
    available_set = set()
    for ap in PARAGRAPHS:
        ap_lov_url = ap["lov"].replace("ø", "o").replace("æ", "ae").replace("å", "aa")
        available_set.add(f"{ap_lov_url}/{ap['number']}")
    
    # Build sections
    examples_html = ""
    for ex in p["eksempler"]:
        examples_html += f'<div class="example"><div class="example-name">{ex["navn"]}</div><p>{ex["tekst"]}</p></div>\n'
    
    vanlige_feil_html = '<ul>' + ''.join(f'<li>{vf}</li>' for vf in p["vanlige_feil"]) + '</ul>'
    
    faq_html = ""
    if p["dumme_sporsmal"]:
        faq_html = '<h2>Dumme spørsmål</h2>\n<div class="faq">\n'
        for qa in p["dumme_sporsmal"]:
            faq_html += f'<div class="faq-item">\n<div class="faq-q">{qa["q"]}</div>\n<div class="faq-a">{qa["a"]}</div>\n</div>\n'
        faq_html += '</div>\n'
    
    related_html = '<div class="related-cards">\n'
    for r in p["related"]:
        r_lov_url = r["lov"].replace("ø", "o").replace("æ", "ae").replace("å", "aa")
        # Auto-detect availability based on actual PARAGRAPHS list
        is_available = f"{r_lov_url}/{r['paragraf']}" in available_set
        cls = "related-card" if is_available else "related-card unavailable"
        href = f'{prefix}lover/{r_lov_url}/{r["paragraf"]}/' if is_available else '#'
        lov_display_map = {
            "angrerettloven": "Angrerettloven",
            "kjopsloven": "Kjøpsloven",
            "husleieloven": "Husleieloven",
            "forbrukerkjopsloven": "Forbrukerkjøpsloven",
            "avhendingslova": "Avhendingslova",
            "bustadoppforingslova": "Bustadoppføringslova",
            "haandverkertjenesteloven": "Håndverkertjenesteloven",
            "pakkereiseloven": "Pakkereiseloven",
            "ehandelsloven": "Ehandelsloven",
            "finansavtaleloven": "Finansavtaleloven",
            "forsikringsavtaleloven": "Forsikringsavtaleloven",
            "skatteloven": "Skatteloven",
            "markedsforingsloven": "Markedsføringsloven",
        }
        lov_display = lov_display_map.get(r["lov"], r["lov"].capitalize())
        related_html += f'<a href="{href}" class="{cls}"><div class="related-card-meta">{lov_display} § {r["paragraf"]}</div><div class="related-card-title">{r["tittel"]}</div></a>\n'
    related_html += '</div>'
    
    # Auto-link paragraph references in the prose (depth=3 for paragraph pages)
    hva_betyr = auto_link_paragraphs(p["hva_betyr_html"], p["lov"], depth=3)
    hva_bor_du = auto_link_paragraphs(p["hva_bor_du_html"], p["lov"], depth=3)
    
    lov_url = p["lov"].replace("ø", "o").replace("æ", "ae").replace("å", "aa")
    canonical = f"/lover/{lov_url}/{p['number']}/"
    return f"""{shared_head(title_tag, p["description"], depth=3, canonical_path=canonical)}
{site_nav(depth=3)}

<div class="container">
  <nav class="breadcrumbs" aria-label="Brødsmuler">
    <a href="{prefix}">Hjem</a>
    <span class="sep">/</span>
    <a href="{prefix}lover/">Lover</a>
    <span class="sep">/</span>
    <a href="{prefix}lover/{lov_url}/">{p["lov_display"]}</a>
    <span class="sep">/</span>
    <span class="current">§ {p["number"]}</span>
  </nav>
</div>

<div class="narrow">
  <header class="article-header">
    <div class="article-eyebrow">{p["lov_display"]}</div>
    <h1 class="article-title"><span class="paragraf-num">§ {p["number"]}</span> — {p["title"]}</h1>
    <p class="article-description">{p["description"]}</p>
  </header>

  <div class="kort-svar">
    <div class="kort-svar-label">Kort svar</div>
    <p>{p["kort_svar"]}</p>
  </div>

  <article class="article-body">
    <h2>Paragraftekst</h2>
    <div class="lovtekst">{p["paragraftekst"]}<div class="lovtekst-attr">Kilde: Lovdata</div></div>

    <h2>Hva betyr dette på vanlig norsk?</h2>
    {hva_betyr}

    <h2>Eksempel{"er" if len(p["eksempler"]) > 1 else ""}</h2>
    {examples_html}

    <h2>Vanlige feil</h2>
    {vanlige_feil_html}

    <h2>Hva bør du gjøre?</h2>
    {hva_bor_du}

    {faq_html}
  </article>

  <div class="related-section">
    <div class="related-label">Relaterte paragrafer</div>
    {related_html}
  </div>
</div>


<div class="innhold-attest">
  <span class="innhold-attest-body"><strong>Juridisk informasjon, ikke rådgivning.</strong> Innholdet er basert på gjeldende norsk lov og gjennomgått av juridisk fagperson. Ved tvil — kontakt advokat. <a href="../../../om/">Mer om Rettsregel →</a></span>
</div>

{contact_form(depth=3)}
{site_footer(depth=3)}"""

def render_lov_index(lov_name, lov_display, paragraphs):
    """Overview page for a single law — redesignet mai 2026."""
    depth = 2
    prefix = "../" * depth

    # Law-specific metadata (description + most important paragraphs)
    LOV_META = {
        "angrerettloven": {
            "desc": "Du har 14 dagers angrerett ved netthandel og kjøp utenfor butikk. Her er alle rettighetene dine forklart på vanlig norsk.",
            "cat": "Forbruk", "featured": ["16", "20"],
        },
        "kjopsloven": {
            "desc": "Kjøpsloven gjelder alle kjøp mellom privatpersoner og bedrifter. Her er reglene om mangel, reklamasjon og heving.",
            "cat": "Forbruk", "featured": ["17", "32"],
        },
        "forbrukerkjopsloven": {
            "desc": "Forbrukerkjøpsloven gir deg sterke rettigheter når du kjøper varer fra en næringsdrivende. Her er alt du trenger å vite.",
            "cat": "Forbruk", "featured": ["16", "26"],
        },
        "husleieloven": {
            "desc": "Husleieloven regulerer alle leieforhold for bolig — rettigheter for leietaker og plikter for utleier. Fra depositum til oppsigelse.",
            "cat": "Bolig", "featured": ["3-5", "9-5"],
        },
        "avhendingslova": {
            "desc": "Avhendingslova regulerer kjøp og salg av bolig, hytte og tomt. Her er reglene om mangler, selgers opplysningsplikt og reklamasjon.",
            "cat": "Bolig", "featured": ["3-7", "4-19"],
        },
        "naboloven": {
            "desc": "Naboloven setter grenser for hva du kan gjøre på din eiendom. Her er reglene om trær, gjerde, støy, graving og tålegrensen.",
            "cat": "Bolig", "featured": ["2", "3"],
        },
        "navneloven": {
            "desc": "Navneloven regulerer fornavn, etternavn og navnebytte for deg og familien. Her er reglene forklart.",
            "cat": "Familie", "featured": ["2", "7"],
        },
        "arveloven": {
            "desc": "Arveloven bestemmer hvem som arver hva. Her er reglene om pliktdel, testament, uskifte og arvegangsrekkefølge.",
            "cat": "Arv", "featured": ["2", "29"],
        },
        "bustadoppforingslova": {
            "desc": "Bustadoppføringslova beskytter deg når du bygger nytt hus eller kjøper bolig under oppføring. Bankgaranti, dagmulkt og overtakelse forklart.",
            "cat": "Bolig", "featured": ["12", "14"],
        },
    }

    meta = LOV_META.get(lov_name, {
        "desc": f"{lov_display} forklart paragraf for paragraf på vanlig norsk.",
        "cat": "Lov", "featured": [],
    })

    n = len(paragraphs)
    featured_nums = set(meta.get("featured", []))
    by_num = {p["number"]: p for p in paragraphs}

    # ── Featured cards ───────────────────────────────────────────────────────
    feat_cards = ""
    for fn in meta.get("featured", []):
        fp = by_num.get(fn)
        if not fp:
            continue
        excerpt = fp.get("kort_svar", fp.get("description", ""))
        if len(excerpt) > 140:
            excerpt = excerpt[:140].rsplit(" ", 1)[0] + "…"
        feat_cards += f'''<a href="{prefix}lover/{lov_name}/{fp["number"]}/" class="lov-feat-kort">
  <div class="lov-feat-num">§ {fp["number"]}</div>
  <h3 class="lov-feat-tittel">{fp["title"]}</h3>
  <p class="lov-feat-txt">{excerpt}</p>
  <div class="lov-feat-cta">Les paragrafen →</div>
</a>'''

    feat_html = ""
    if feat_cards:
        feat_html = f'''<div class="lov-feat-sek">
  <span class="lov-sek-lbl">Viktigst å kjenne til</span>
  <div class="lov-feat-grid">{feat_cards}</div>
</div>'''

    # ── Paragraph grid ───────────────────────────────────────────────────────
    grid_html = ""
    for p in paragraphs:
        excerpt = p.get("kort_svar", p.get("description", ""))
        if len(excerpt) > 110:
            excerpt = excerpt[:110].rsplit(" ", 1)[0] + "…"
        flagg = "plist-flagg" if p["number"] in featured_nums else ""
        grid_html += f'''<a href="{prefix}lover/{lov_name}/{p["number"]}/" class="plist-kort {flagg}">
  <div class="plist-kort-num">§ {p["number"]}</div>
  <div class="plist-kort-body">
    <div class="plist-kort-tittel">{p["title"]}</div>
    {f'<div class="plist-kort-excerpt">{excerpt}</div>' if excerpt else ""}
  </div>
  <div class="plist-kort-pil">→</div>
</a>'''

    return f"""{shared_head(f'{lov_display} — Forklart paragraf for paragraf | Rettsregel',
        f'{meta["desc"]}', depth=2, canonical_path=f'/lover/{lov_name}/')}
{site_nav(depth=2)}

<div class="container">
  <nav class="breadcrumbs" aria-label="Brødsmuler">
    <a href="{prefix}">Hjem</a><span class="sep">/</span>
    <a href="{prefix}lover/">Lover</a><span class="sep">/</span>
    <span class="current">{lov_display}</span>
  </nav>

  <header class="lov-side-hero">
    <span class="lov-hero-mark">§</span>
    <h1 class="lov-hero-h1">{lov_display} — <em>forklart</em></h1>
    <p class="lov-hero-desc">{meta["desc"]}</p>
    <div class="lov-hero-pills">
      <span class="lov-hero-pill">📋 {n} paragrafer</span>
      <span class="lov-hero-pill">📂 {meta["cat"]}</span>
      <span class="lov-hero-pill">✓ Oppdatert 2026</span>
    </div>
  </header>

  {feat_html}

  <div class="lov-sok-wrap">
    <svg class="lov-sok-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
    </svg>
    <input type="text" class="lov-sok-input" id="lovSok"
      placeholder="Søk blant {n} paragrafer…" autocomplete="off">
  </div>
  <div class="lov-sok-count" id="lovSokCount">{n} paragrafer</div>

  <div class="plist-grid" id="plistGrid">
    {grid_html}
    <div class="plist-ingen" id="plistIngen">Ingen paragrafer matcher søket.</div>
  </div>
</div>

<div class="innhold-attest">
  <span class="innhold-attest-body"><strong>Juridisk informasjon, ikke rådgivning.</strong> Innholdet er basert på gjeldende norsk lov og gjennomgått av juridisk fagperson. Ved tvil — kontakt advokat. <a href="../../om/">Mer om Rettsregel →</a></span>
</div>

<script>
(function(){{
  var inp=document.getElementById('lovSok');
  var items=document.querySelectorAll('.plist-kort');
  var cnt=document.getElementById('lovSokCount');
  var ingen=document.getElementById('plistIngen');
  var total=items.length;
  inp.addEventListener('input',function(){{
    var q=this.value.toLowerCase().trim();
    var vis=0;
    items.forEach(function(el){{
      var match=!q||el.textContent.toLowerCase().includes(q);
      el.classList.toggle('plist-hidden',!match);
      if(match)vis++;
    }});
    cnt.textContent=q?(vis+' av '+total+' paragrafer'):(total+' paragrafer');
    ingen.classList.toggle('vis',vis===0&&q.length>0);
  }});
}})();
</script>

{contact_form(depth=2)}
{site_footer(depth=2)}"""

def render_lover_index():
    """Lov-oversikt — Apple-aktig kompakt liste-design."""

    # Grupper etter kategori
    LOV_KATEGORI = {
        "angrerettloven": ("kjop", "Forbruk og kjøp"),
        "kjopsloven": ("kjop", "Forbruk og kjøp"),
        "forbrukerkjopsloven": ("kjop", "Forbruk og kjøp"),
        "husleieloven": ("bolig", "Bolig"),
        "avhendingslova": ("bolig", "Bolig"),
        "naboloven": ("bolig", "Bolig"),
        "bustadoppforingslova": ("bolig", "Bolig"),
        "navneloven": ("familie", "Familie"),
        "arveloven": ("arv", "Arv og familie"),
    }
    LOV_KORT_DESC = {
        "angrerettloven": "Angrerett ved netthandel og kjøp utenfor butikk",
        "kjopsloven": "Kjøp og salg — privat og bedrift",
        "forbrukerkjopsloven": "Kjøp som forbruker — strengeste forbrukervern",
        "husleieloven": "Leie av bolig — rettigheter for begge parter",
        "avhendingslova": "Kjøp og salg av bolig, hytte, tomt",
        "naboloven": "Konflikter og avstander til naboer",
        "bustadoppforingslova": "Bygging av ny bolig eller hytte",
        "navneloven": "Navnevalg og navneendring",
        "arveloven": "Arv, testament og pliktdel",
    }

    # Tell paragrafer per lov
    counts = {}
    displays = {}
    for p in PARAGRAPHS:
        lov = p["lov"]
        counts[lov] = counts.get(lov, 0) + 1
        displays[lov] = p["lov_display"]

    # Grupper etter kategori
    KAT_ORDER = ["bolig", "kjop", "arv", "familie"]
    KAT_TITLER = {
        "bolig": "Bolig",
        "kjop": "Kjøp og forbruk",
        "arv": "Arv og familie",
        "familie": "Familie",
    }
    grouped = {}
    for lov, antall in counts.items():
        kat, _ = LOV_KATEGORI.get(lov, ("annet", "Annet"))
        grouped.setdefault(kat, []).append((lov, antall))

    seksjoner_html = ""
    for kat in KAT_ORDER:
        if kat not in grouped:
            continue
        lover = sorted(grouped[kat], key=lambda x: -x[1])
        n_para = sum(a for _, a in lover)
        n_lov = len(lover)
        rader = ""
        for lov, antall in lover:
            navn = displays[lov]
            desc = LOV_KORT_DESC.get(lov, "")
            rader += f'''        <a href="{lov}/" class="lk-rad">
          <div class="lk-info">
            <h3 class="lk-navn">{navn}</h3>
            <p class="lk-desc">{desc}</p>
          </div>
          <div class="lk-meta">
            <span class="lk-antall">{antall}</span>
            <span class="lk-pil">→</span>
          </div>
        </a>
'''
        seksjoner_html += f'''    <section class="lk-seksjon">
      <header class="lk-seksjon-hd">
        <h2>{KAT_TITLER[kat]}</h2>
        <span class="lk-seksjon-meta">{n_para} paragrafer · {n_lov} {"lov" if n_lov==1 else "lover"}</span>
      </header>
      <div class="lk-liste">
{rader}      </div>
    </section>
'''

    total_para = sum(counts.values())
    total_lov = len(counts)

    return f"""{shared_head(
        'Alle lover — forklart på vanlig norsk | Rettsregel',
        f'{total_para} paragrafer i {total_lov} norske lover, forklart på vanlig norsk. Bla i lovene.',
        depth=1, canonical_path='/lover/'
    )}
<body>
{site_nav(depth=1)}
<style>
.lk-page {{ max-width: 880px; margin: 0 auto; padding: 0 24px; }}
.lk-hero {{ padding: 56px 0 40px; border-bottom: 1px solid var(--line); margin-bottom: 48px; }}
.lk-hero .lk-kicker {{ font-family: var(--sans); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.18em; color: var(--accent); margin-bottom: 14px; display: block; }}
.lk-hero h1 {{ font-family: var(--serif); font-weight: 400; font-size: clamp(28px, 3.4vw, 40px); letter-spacing: -0.022em; line-height: 1.1; margin: 0 0 16px 0; }}
.lk-hero .lk-lead {{ font-size: 17px; color: var(--ink-soft); line-height: 1.6; max-width: 540px; margin: 0; }}

.lk-stats {{ display: flex; gap: 32px; margin-top: 24px; padding-top: 0; }}
.lk-stat-num {{ font-family: var(--serif); font-size: 30px; font-weight: 400; line-height: 1; color: var(--ink); }}
.lk-stat-lbl {{ font-family: var(--sans); font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.12em; color: var(--ink-mute); margin-top: 6px; }}

.lk-seksjon {{ margin-bottom: 56px; }}
.lk-seksjon-hd {{ display: flex; justify-content: space-between; align-items: baseline; padding-bottom: 14px; border-bottom: 1px solid var(--line); margin-bottom: 4px; }}
.lk-seksjon-hd h2 {{ font-family: var(--serif); font-weight: 400; font-size: 22px; letter-spacing: -0.01em; margin: 0; line-height: 1.2; }}
.lk-seksjon-meta {{ font-family: var(--sans); font-size: 12px; color: var(--ink-mute); letter-spacing: 0.04em; }}

.lk-liste {{}}
.lk-rad {{
  display: flex; align-items: center; justify-content: space-between; gap: 24px;
  padding: 20px 4px; border-bottom: 1px solid var(--line);
  text-decoration: none; color: var(--ink);
  transition: padding 0.13s;
}}
.lk-rad:last-child {{ border-bottom: none; }}
.lk-rad:hover {{ padding-left: 12px; }}
.lk-rad:hover .lk-pil {{ transform: translateX(4px); color: var(--accent); }}
.lk-info {{ min-width: 0; flex: 1; }}
.lk-navn {{ font-family: var(--serif); font-weight: 400; font-size: 19px; letter-spacing: -0.01em; margin: 0 0 4px 0; line-height: 1.25; }}
.lk-desc {{ font-size: 13px; color: var(--ink-soft); margin: 0; line-height: 1.5; }}
.lk-meta {{ display: flex; align-items: center; gap: 14px; flex-shrink: 0; }}
.lk-antall {{ font-family: var(--sans); font-size: 13px; color: var(--ink-mute); font-variant-numeric: tabular-nums; }}
.lk-pil {{ font-size: 16px; color: var(--ink-mute); transition: transform 0.13s, color 0.13s; }}

@media (max-width: 600px) {{
  .lk-hero {{ padding: 36px 0 28px; margin-bottom: 36px; }}
  .lk-stats {{ gap: 24px; }}
  .lk-stat-num {{ font-size: 24px; }}
  .lk-rad {{ padding: 16px 4px; }}
  .lk-navn {{ font-size: 17px; }}
  .lk-desc {{ font-size: 12.5px; }}
}}
</style>

<main>
  <div class="lk-page">

    <header class="lk-hero">
      <span class="lk-kicker">Lovsamling</span>
      <h1>Norske lover, paragraf for paragraf</h1>
      <p class="lk-lead">Vi tar lovteksten slik den står og forklarer hva den faktisk betyr.</p>
      <div class="lk-stats">
        <div><div class="lk-stat-num">{total_para}</div><div class="lk-stat-lbl">paragrafer</div></div>
        <div><div class="lk-stat-num">{total_lov}</div><div class="lk-stat-lbl">lover</div></div>
      </div>
    </header>

{seksjoner_html}
  </div>
</main>

{site_footer(depth=1)}"""


def render_personvern():
    return f"""{shared_head('Personvern | Rettsregel', 'Personvernerklæring for Rettsregel.no — Walrus AS.', depth=1, canonical_path='/personvern/')}
<body>
{site_nav(depth=1)}
<main class="page">
  <div style="max-width: 740px; padding: 64px 0 80px;">
    <div class="article-eyebrow">Personvern</div>
    <h1 class="article-title">Personvernerklæring</h1>
    <div class="article-body">
      <p>Rettsregel.no drives av Walrus AS, org.nr. [ORG.NR — fyll inn]. Vi tar personvern på alvor og behandler ikke mer data enn nødvendig.</p>
      <h2>Hva vi samler inn</h2>
      <p>Når du sender inn kontaktskjema samler vi inn navn, telefonnummer og e-postadresse. Denne informasjonen brukes utelukkende for å besvare henvendelsen din.</p>
      <p>Nettstedet bruker ingen tracking-cookies, ingen annonse-nettverk og ingen tredjeparts analyse utover det som er nødvendig for drift.</p>
      <h2>Tredjeparter</h2>
      <p>Kontaktskjema behandles via Formspree (formspree.io). Formsprees personvernerklæring gjelder for denne databehandlingen. Vi har databehandleravtale med Formspree.</p>
      <h2>Dine rettigheter</h2>
      <p>Du har rett til innsyn, retting og sletting av personopplysninger vi har om deg. Ta kontakt på rettsregel@gmail.com for å utøve disse rettighetene.</p>
      <h2>Kontakt</h2>
      <p>Behandlingsansvarlig: Walrus AS · rettsregel@gmail.com</p>
    </div>
  </div>
</main>
{site_footer(depth=1)}"""


def render_om():
    """Om-side i samme Apple-slide-stil som forsiden."""
    total_paragrafer = len(PARAGRAPHS)
    total_lover = len(set(p["lov"] for p in PARAGRAPHS))
    total_sporsmal = len(SPORSMAL)

    return f"""{shared_head(
        'Om Rettsregel — norske lover på vanlig norsk',
        'Vi gjør norske lover forståelige — paragraf for paragraf. Bygd av Walrus AS for å gi alle tilgang til hva loven faktisk sier.',
        depth=1, canonical_path='/om/'
    )}
<body>
{site_nav(depth=1)}

<style>
.om-slide {{ padding: 128px 24px; border-bottom: 1px solid var(--line); }}
.om-slide-inner {{ max-width: 1080px; margin: 0 auto; }}
.om-slide.tight {{ padding: 96px 24px; }}
.om-slide.alt {{ background: var(--bg-alt); }}

/* HERO */
.om-hero {{
  min-height: calc(75vh - 80px);
  display: flex; flex-direction: column; justify-content: center;
  padding: 120px 24px 100px;
  border-bottom: 1px solid var(--line);
  text-align: left;
}}
.om-hero-inner {{ max-width: 1080px; margin: 0 auto; width: 100%; }}
.om-kicker {{
  font-family: var(--sans); font-size: 11px;
  font-weight: 700; text-transform: uppercase; letter-spacing: 0.2em;
  color: var(--accent); margin-bottom: 24px; display: block;
}}
.om-h1 {{
  font-family: var(--serif); font-weight: 400;
  font-size: clamp(40px, 7vw, 88px); line-height: 1.02;
  letter-spacing: -0.032em; margin: 0 0 28px 0; max-width: 920px;
  font-variation-settings: "opsz" 96, "SOFT" 50;
}}
.om-h1 em {{ font-style: italic; color: var(--accent); font-weight: 400; }}
.om-lead-hero {{
  font-family: var(--serif-prose);
  font-size: clamp(20px, 2.2vw, 26px); line-height: 1.45; color: var(--ink-soft);
  max-width: 720px; margin: 0; font-weight: 400;
}}

.om-h2 {{
  font-family: var(--serif); font-weight: 400;
  font-size: clamp(32px, 4.6vw, 52px); line-height: 1.05;
  letter-spacing: -0.026em; margin: 0 0 24px 0; max-width: 800px;
  font-variation-settings: "opsz" 72, "SOFT" 50;
}}
.om-h2 em {{ font-style: italic; color: var(--accent); font-weight: 400; }}
.om-lead {{
  font-family: var(--serif-prose);
  font-size: 19px; color: var(--ink-soft); line-height: 1.55;
  max-width: 620px; margin: 0 0 56px 0; font-weight: 400;
}}

/* STORE TALL */
.om-stats {{
  display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1px; background: var(--line);
  border: 1px solid var(--line); border-radius: 24px; overflow: hidden;
  margin-top: 8px;
}}
.om-stat {{ background: var(--bg-card); padding: 44px 32px; }}
.om-stat-num {{
  font-family: var(--serif); font-size: clamp(48px, 6vw, 76px);
  font-weight: 400; line-height: 1; letter-spacing: -0.028em;
  color: var(--ink); margin-bottom: 12px;
  font-variation-settings: "opsz" 96;
  font-variant-numeric: tabular-nums;
}}
.om-stat-lbl {{
  font-family: var(--sans); font-size: 12px; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.14em; color: var(--ink-mute);
}}

/* PRINSIPP-KORT */
.om-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px; }}
.om-prinsipp {{
  background: var(--bg-card); border: 1px solid var(--line); border-radius: 24px;
  padding: 36px 32px; display: flex; flex-direction: column;
  transition: border-color 0.2s, transform 0.2s, box-shadow 0.2s;
}}
.om-prinsipp:hover {{
  border-color: var(--accent-soft); transform: translateY(-2px);
  box-shadow: 0 12px 28px rgba(0,0,0,0.04);
}}
.om-prinsipp-em {{
  font-size: 32px; line-height: 1; margin-bottom: 18px;
  width: 60px; height: 60px;
  background: linear-gradient(135deg, rgba(177,74,42,0.10), rgba(177,74,42,0.04));
  border-radius: 16px;
  display: flex; align-items: center; justify-content: center;
}}
.om-prinsipp h3 {{
  font-family: var(--serif); font-size: 22px; font-weight: 400;
  letter-spacing: -0.012em; line-height: 1.2; margin: 0 0 10px 0;
  font-variation-settings: "opsz" 28;
}}
.om-prinsipp p {{
  font-family: var(--serif-prose); font-size: 15.5px; line-height: 1.55;
  color: var(--ink-soft); margin: 0;
}}

/* QUOTE / LARGE STATEMENT */
.om-quote {{
  font-family: var(--serif); font-weight: 400; font-style: italic;
  font-size: clamp(28px, 4vw, 44px); line-height: 1.2;
  letter-spacing: -0.018em; color: var(--ink);
  max-width: 900px; margin: 0;
  font-variation-settings: "opsz" 60;
}}
.om-quote-attr {{
  font-family: var(--sans); font-size: 13px; font-weight: 500;
  color: var(--ink-mute); letter-spacing: 0.04em; margin-top: 32px;
}}

/* METODE-RAD */
.om-metode {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1px; background: var(--line); border: 1px solid var(--line); border-radius: 24px; overflow: hidden; }}
.om-steg {{ background: var(--bg-card); padding: 36px 30px; }}
.om-steg-tall {{
  font-family: var(--serif); font-size: 48px; font-weight: 400;
  line-height: 1; color: var(--accent); margin-bottom: 16px;
  letter-spacing: -0.02em;
  font-variation-settings: "opsz" 60;
}}
.om-steg h4 {{
  font-family: var(--serif); font-size: 19px; font-weight: 400;
  letter-spacing: -0.01em; margin: 0 0 8px 0; line-height: 1.25;
}}
.om-steg p {{
  font-family: var(--serif-prose); font-size: 14.5px; line-height: 1.55;
  color: var(--ink-soft); margin: 0;
}}

/* INFO-BOKS */
.om-info-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1px; background: var(--line); border: 1px solid var(--line); border-radius: 24px; overflow: hidden; }}
.om-info-rad {{ background: var(--bg-card); padding: 32px 30px; }}
.om-info-lbl {{
  font-family: var(--sans); font-size: 11px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.16em; color: var(--ink-mute);
  margin-bottom: 12px;
}}
.om-info-val {{
  font-family: var(--serif); font-size: 22px; font-weight: 400;
  letter-spacing: -0.012em; line-height: 1.25; color: var(--ink);
  margin: 0;
  font-variation-settings: "opsz" 28;
}}
.om-info-val a {{ color: var(--ink); text-decoration: none; border-bottom: 1px solid var(--line); transition: border-color 0.15s; }}
.om-info-val a:hover {{ border-bottom-color: var(--accent); }}

/* CTA */
.om-cta-rad {{ display: flex; gap: 14px; flex-wrap: wrap; align-items: center; margin-top: 48px; }}
.om-cta {{
  font-family: var(--sans); font-size: 14.5px; font-weight: 600;
  text-decoration: none; padding: 14px 28px; border-radius: 100px;
  transition: all 0.2s; display: inline-flex; align-items: center; gap: 10px;
}}
.om-cta-primary {{ background: var(--ink); color: var(--bg); }}
.om-cta-primary:hover {{ background: var(--accent); transform: translateY(-1px); box-shadow: 0 8px 20px rgba(177,74,42,0.25); }}
.om-cta-ghost {{ color: var(--ink-soft); border: 1px solid var(--line); }}
.om-cta-ghost:hover {{ border-color: var(--accent); color: var(--accent); }}

@media (max-width: 700px) {{
  .om-slide {{ padding: 80px 24px; }}
  .om-slide.tight {{ padding: 64px 24px; }}
  .om-hero {{ padding: 80px 24px 60px; min-height: auto; }}
  .om-prinsipp {{ padding: 28px 24px; border-radius: 20px; }}
  .om-stats, .om-info-grid, .om-metode {{ border-radius: 20px; }}
  .om-stat {{ padding: 30px 24px; }}
}}
</style>

<main>

  <section class="om-hero">
    <div class="om-hero-inner">
      <span class="om-kicker">Om Rettsregel</span>
      <h1 class="om-h1">Lover er ikke vanskelige.<br><em>De er bare dårlig forklart.</em></h1>
      <p class="om-lead-hero">Vi tar lovteksten slik den står og oversetter den til vanlig norsk — paragraf for paragraf. Gratis, uten registrering. Bygd for alle som trenger å vite hva loven faktisk sier.</p>
    </div>
  </section>

  <section class="om-slide">
    <div class="om-slide-inner">
      <span class="om-kicker">Innholdet</span>
      <h2 class="om-h2">Et helt jus-bibliotek.<br>Oversatt til folkemunne.</h2>
      <div class="om-stats">
        <div class="om-stat"><div class="om-stat-num">{total_paragrafer}</div><div class="om-stat-lbl">Paragrafer</div></div>
        <div class="om-stat"><div class="om-stat-num">{total_lover}</div><div class="om-stat-lbl">Lover</div></div>
        <div class="om-stat"><div class="om-stat-num">92</div><div class="om-stat-lbl">Verktøy</div></div>
        <div class="om-stat"><div class="om-stat-num">{total_sporsmal}</div><div class="om-stat-lbl">Spørsmål</div></div>
      </div>
    </div>
  </section>

  <section class="om-slide alt">
    <div class="om-slide-inner">
      <span class="om-kicker">Hvorfor</span>
      <h2 class="om-h2">For mange faller mellom to stoler</h2>
      <p class="om-lead">Lovverket gjelder for alle — men er skrevet for jurister. Du skal egentlig kunne lese loven selv. I praksis betyr ord som "<em>rimelig tid</em>", "<em>vesentlig mangel</em>" og "<em>særskilt tilfelle</em>" at de fleste gir opp før de er ferdig med første setning.</p>
      <blockquote class="om-quote">«Det er ikke nok at loven er gratis. Den må også være forståelig.»</blockquote>
      <div class="om-quote-attr">— Rettsregels grunntese</div>
    </div>
  </section>

  <section class="om-slide">
    <div class="om-slide-inner">
      <span class="om-kicker">Slik jobber vi</span>
      <h2 class="om-h2">Fra lovtekst til hverdagsnorsk</h2>
      <p class="om-lead">Hver paragraf gjennomgår samme prosess — strukturert, transparent, gjennomtenkt.</p>
      <div class="om-metode">
        <div class="om-steg">
          <div class="om-steg-tall">01</div>
          <h4>Original</h4>
          <p>Vi viser deg lovteksten ordrett. Ingen skjult omskriving.</p>
        </div>
        <div class="om-steg">
          <div class="om-steg-tall">02</div>
          <h4>Oversettelse</h4>
          <p>Forklart på vanlig norsk — uten å miste det juridisk essensielle.</p>
        </div>
        <div class="om-steg">
          <div class="om-steg-tall">03</div>
          <h4>Konkret</h4>
          <p>Hverdagseksempler som viser hvordan paragrafen faktisk slår ut.</p>
        </div>
        <div class="om-steg">
          <div class="om-steg-tall">04</div>
          <h4>Kontroll</h4>
          <p>Gjennomgått av jurist før publisering. Oppdateres ved lovendring.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="om-slide alt">
    <div class="om-slide-inner">
      <span class="om-kicker">Prinsipper</span>
      <h2 class="om-h2">Det vi ikke gjør</h2>
      <p class="om-lead">Like viktig som hva Rettsregel er — er hva Rettsregel ikke er.</p>
      <div class="om-grid">
        <div class="om-prinsipp">
          <div class="om-prinsipp-em">🚫</div>
          <h3>Ingen registrering</h3>
          <p>Du trenger ikke konto. Du trenger ikke e-post. Du bare bruker det.</p>
        </div>
        <div class="om-prinsipp">
          <div class="om-prinsipp-em">📭</div>
          <h3>Ingen reklame</h3>
          <p>Ingen tracking, ingen ad-nettverk, ingen popups. Bare lov.</p>
        </div>
        <div class="om-prinsipp">
          <div class="om-prinsipp-em">⚖️</div>
          <h3>Ikke rådgivning</h3>
          <p>Vi forklarer hva loven sier — men erstatter ikke en advokat ved konkrete saker.</p>
        </div>
        <div class="om-prinsipp">
          <div class="om-prinsipp-em">🤖</div>
          <h3>Ikke et chatbot-bibliotek</h3>
          <p>Hver paragraf er menneskelig redigert. Roy er bonus, ikke grunnlaget.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="om-slide">
    <div class="om-slide-inner">
      <span class="om-kicker">Bak siden</span>
      <h2 class="om-h2">Walrus AS</h2>
      <p class="om-lead">Rettsregel.no driftes av <strong>Walrus AS</strong>, et lite norsk selskap som tror at åpen kunnskap er en samfunnsoppgave. Vi har ingen investorer, ingen sponsoravtaler og ingen lojalitet utenfor brukeren.</p>
      <div class="om-info-grid">
        <div class="om-info-rad">
          <div class="om-info-lbl">Selskap</div>
          <p class="om-info-val">Walrus AS</p>
        </div>
        <div class="om-info-rad">
          <div class="om-info-lbl">Kontakt</div>
          <p class="om-info-val"><a href="mailto:rettsregel@gmail.com">rettsregel@gmail.com</a></p>
        </div>
        <div class="om-info-rad">
          <div class="om-info-lbl">Beliggenhet</div>
          <p class="om-info-val">Dønna, Nordland</p>
        </div>
      </div>
    </div>
  </section>

  <section class="om-slide alt">
    <div class="om-slide-inner">
      <span class="om-kicker">Kom i gang</span>
      <h2 class="om-h2">Begynn å bla.</h2>
      <p class="om-lead">Lovverket er åpent. Du har lov til å vite hva som gjelder.</p>
      <div class="om-cta-rad">
        <a href="../tjenester/" class="om-cta om-cta-primary">Se alle 92 verktøy <span>→</span></a>
        <a href="../lover/" class="om-cta om-cta-ghost">Bla i lovene</a>
      </div>
    </div>
  </section>

</main>

{site_footer(depth=1)}"""


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
    content_raw = s.get("content", "")
    kort_svar = s.get("kort_svar", "")
    related = s.get("related", [])

    body_html = md.markdown(content_raw, extensions=["tables"]) if content_raw else ""

    # Related paragraphs
    related_html = ""
    if related:
        related_cards = []
        for r in related:
            lov = r.get("lov", "")
            paragraf = r.get("paragraf", "")
            tittel = r.get("tittel", "")
            available = r.get("available", False)
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

    return f"""{shared_head(
        f"{title} — Rettsregel",
        description,
        depth=2, canonical_path=f"/sporsmal/{slug}/"
    )}
<body>
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
</div>
</main>
<div class="innhold-attest">
  <span class="innhold-attest-body"><strong>Juridisk informasjon, ikke rådgivning.</strong> Innholdet er basert på gjeldende norsk lov og gjennomgått av juridisk fagperson. Ved tvil — kontakt advokat. <a href="../../om/">Mer om Rettsregel →</a></span>
</div>
{site_footer(depth=2)}
</body>
</html>"""


def render_sporsmal_hub():
    """Spørsmål-hub — skalerbar for 1000+ artikler. Søk + kategori-filter + compact liste."""

    KAT_LABEL = {
        "bolig": "Bolig",
        "forbruk": "Forbruk og kjøp",
        "arbeid": "Arbeid",
        "familie": "Familie",
        "gjeld": "Gjeld og penger",
        "tjenester": "Tjenester",
        "arv": "Arv",
    }

    # Tell etter kategori
    by_kat = {}
    for s in SPORSMAL:
        kat = s.get("kategori", "annet")
        by_kat.setdefault(kat, []).append(s)

    # Sortert etter antall (mest brukte først)
    kat_sorted = sorted(by_kat.items(), key=lambda x: -len(x[1]))

    # Lag kategori-pills for filter
    pills_html = '<button class="sp-pill active" data-kat="alle">Alle <span class="sp-pill-n">' + str(len(SPORSMAL)) + '</span></button>\n'
    for kat, items in kat_sorted:
        navn = KAT_LABEL.get(kat, kat.capitalize())
        pills_html += f'    <button class="sp-pill" data-kat="{kat}">{navn} <span class="sp-pill-n">{len(items)}</span></button>\n'

    # Bygg liste — alle spørsmål, gruppert etter kategori
    liste_html = ""
    for kat, items in kat_sorted:
        kat_label = KAT_LABEL.get(kat, kat.capitalize())
        rader = ""
        for s in items:
            slug = s.get("slug", "")
            tittel = s.get("title", "")
            desc = s.get("description", "")
            rader += f'''        <a href="{slug}/" class="sp-rad" data-kat="{kat}" data-search="{tittel.lower()} {desc.lower()}">
          <div class="sp-rad-info">
            <div class="sp-rad-tittel">{tittel}</div>
            <div class="sp-rad-desc">{desc}</div>
          </div>
          <div class="sp-rad-meta">
            <span class="sp-rad-kat">{kat_label}</span>
            <span class="sp-rad-pil">→</span>
          </div>
        </a>
'''
        liste_html += f'''    <div class="sp-gruppe" data-kat="{kat}">
      <h2 class="sp-gruppe-tittel">{kat_label} <span class="sp-gruppe-meta">{len(items)}</span></h2>
      <div class="sp-rader">
{rader}      </div>
    </div>
'''

    return f"""{shared_head(
        'Spørsmål og svar — vanlige juridiske spørsmål | Rettsregel',
        f'{len(SPORSMAL)} spørsmål om norsk lov. Konkrete svar, ikke generelle floskler.',
        depth=1, canonical_path='/sporsmal/'
    )}
<body>
{site_nav(depth=1)}
<style>
.sp-page {{ max-width: 900px; margin: 0 auto; padding: 0 24px; }}
.sp-hero {{ padding: 56px 0 36px; border-bottom: 1px solid var(--line); margin-bottom: 28px; }}
.sp-hero .sp-kicker {{ font-family: var(--sans); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.18em; color: var(--accent); margin-bottom: 14px; display: block; }}
.sp-hero h1 {{ font-family: var(--serif); font-weight: 400; font-size: clamp(28px, 3.4vw, 40px); letter-spacing: -0.022em; line-height: 1.1; margin: 0 0 16px 0; }}
.sp-hero .sp-lead {{ font-size: 17px; color: var(--ink-soft); line-height: 1.6; max-width: 560px; margin: 0; }}

.sp-toolbar {{ position: sticky; top: 0; background: var(--bg); padding: 14px 0 16px; margin-bottom: 8px; z-index: 5; border-bottom: 1px solid var(--line); }}
.sp-sok-wrap {{ position: relative; margin-bottom: 12px; }}
.sp-sok-icon {{ position: absolute; left: 14px; top: 50%; transform: translateY(-50%); color: var(--ink-mute); width: 16px; height: 16px; pointer-events: none; }}
.sp-sok-input {{ width: 100%; padding: 11px 14px 11px 40px; border: 1.5px solid var(--line); border-radius: 10px; font-family: var(--sans); font-size: 14px; background: var(--bg-card); color: var(--ink); box-sizing: border-box; transition: border-color 0.13s; }}
.sp-sok-input:focus {{ outline: none; border-color: var(--accent); }}
.sp-pills {{ display: flex; gap: 6px; overflow-x: auto; padding-bottom: 2px; -webkit-overflow-scrolling: touch; }}
.sp-pills::-webkit-scrollbar {{ display: none; }}
.sp-pill {{ background: var(--bg-card); border: 1px solid var(--line); color: var(--ink-soft); font-family: var(--sans); font-size: 12.5px; font-weight: 500; padding: 6px 12px; border-radius: 100px; cursor: pointer; white-space: nowrap; transition: all 0.13s; display: inline-flex; align-items: center; gap: 6px; }}
.sp-pill:hover {{ border-color: var(--accent-soft); }}
.sp-pill.active {{ background: var(--ink); color: var(--bg); border-color: var(--ink); }}
.sp-pill-n {{ font-size: 11px; opacity: 0.7; font-variant-numeric: tabular-nums; }}

.sp-gruppe {{ margin-bottom: 40px; }}
.sp-gruppe-tittel {{ font-family: var(--serif); font-weight: 400; font-size: 20px; letter-spacing: -0.01em; margin: 0 0 4px 0; padding: 16px 0 10px; border-bottom: 1px solid var(--line); display: flex; justify-content: space-between; align-items: baseline; }}
.sp-gruppe-meta {{ font-family: var(--sans); font-size: 12px; color: var(--ink-mute); font-weight: 500; font-variant-numeric: tabular-nums; }}

.sp-rader {{}}
.sp-rad {{
  display: flex; align-items: flex-start; justify-content: space-between; gap: 16px;
  padding: 16px 4px; border-bottom: 1px solid var(--line);
  text-decoration: none; color: var(--ink); transition: padding 0.13s;
}}
.sp-rad:last-child {{ border-bottom: none; }}
.sp-rad:hover {{ padding-left: 10px; }}
.sp-rad:hover .sp-rad-pil {{ transform: translateX(4px); color: var(--accent); }}
.sp-rad-info {{ min-width: 0; flex: 1; }}
.sp-rad-tittel {{ font-family: var(--serif); font-size: 16px; font-weight: 400; line-height: 1.3; letter-spacing: -0.005em; margin-bottom: 4px; }}
.sp-rad-desc {{ font-size: 13px; color: var(--ink-soft); line-height: 1.5; }}
.sp-rad-meta {{ display: flex; align-items: center; gap: 10px; flex-shrink: 0; padding-top: 3px; }}
.sp-rad-kat {{ font-family: var(--sans); font-size: 10.5px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: var(--ink-mute); padding: 3px 9px; background: var(--bg-card); border: 1px solid var(--line); border-radius: 100px; white-space: nowrap; }}
.sp-rad-pil {{ font-size: 14px; color: var(--ink-mute); transition: transform 0.13s, color 0.13s; }}

.sp-ingen {{ display: none; padding: 60px 0; text-align: center; color: var(--ink-mute); font-style: italic; }}
.sp-ingen.show {{ display: block; }}

@media (max-width: 600px) {{
  .sp-hero {{ padding: 36px 0 24px; margin-bottom: 24px; }}
  .sp-rad-meta {{ flex-direction: column; align-items: flex-end; gap: 4px; }}
  .sp-rad-tittel {{ font-size: 15px; }}
}}
</style>

<main>
  <div class="sp-page">

    <header class="sp-hero">
      <span class="sp-kicker">Spørsmål og svar</span>
      <h1>Vanlige spørsmål — konkrete svar</h1>
      <p class="sp-lead">Skrevet på vanlig norsk, med stegene du kan ta. Søk i listen eller filtrer på kategori.</p>
    </header>

    <div class="sp-toolbar">
      <div class="sp-sok-wrap">
        <svg class="sp-sok-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" id="spSok" class="sp-sok-input" placeholder="Søk blant {len(SPORSMAL)} spørsmål…" autocomplete="off">
      </div>
      <div class="sp-pills" id="spPills">
        {pills_html}
      </div>
    </div>

{liste_html}

    <div class="sp-ingen" id="spIngen">Ingen spørsmål matcher.</div>

  </div>
</main>

<script>
(function(){{
  var sok = document.getElementById('spSok');
  var pills = document.querySelectorAll('.sp-pill');
  var rader = document.querySelectorAll('.sp-rad');
  var grupper = document.querySelectorAll('.sp-gruppe');
  var ingen = document.getElementById('spIngen');
  var aktivKat = 'alle';

  function filtrer() {{
    var q = sok.value.toLowerCase().trim();
    var synlig = 0;
    rader.forEach(function(r) {{
      var matchKat = (aktivKat === 'alle' || r.dataset.kat === aktivKat);
      var matchSok = (!q || r.dataset.search.indexOf(q) !== -1);
      var vis = matchKat && matchSok;
      r.style.display = vis ? '' : 'none';
      if (vis) synlig++;
    }});
    // Skjul tomme grupper
    grupper.forEach(function(g) {{
      var aktive = g.querySelectorAll('.sp-rad:not([style*="none"])').length > 0 ||
                   Array.from(g.querySelectorAll('.sp-rad')).some(function(r){{ return r.style.display !== 'none'; }});
      g.style.display = aktive ? '' : 'none';
    }});
    ingen.classList.toggle('show', synlig === 0);
  }}

  sok.addEventListener('input', filtrer);
  pills.forEach(function(p) {{
    p.addEventListener('click', function() {{
      pills.forEach(function(x){{ x.classList.remove('active'); }});
      p.classList.add('active');
      aktivKat = p.dataset.kat;
      filtrer();
    }});
  }});
}})();
</script>

{site_footer(depth=1)}"""


def render_homepage():
    """Forsiden — minimalistisk, slide-basert. Ingen søk."""

    total_paragrafer = len(PARAGRAPHS)
    total_lover = len(set(p["lov"] for p in PARAGRAPHS))

    # Slide 2 — viktige kontrakter og maler
    KONTRAKTER = [
        ("tjenester/testament-mal/", "📜", "Testament", "Skriv testament med vitnefelt, klart for signering."),
        ("kontrakter/samboeravtale/", "🤝", "Samboeravtale", "Hvem eier hva ved brudd? Beskytt deg i dag."),
        ("kontrakter/husleiekontrakt/", "🔑", "Husleiekontrakt", "Tidsubestemt eller tidsbestemt. Husleieloven."),
        ("kontrakter/arbeidsavtale/", "✍️", "Arbeidsavtale", "Alle aml. § 14-6-krav. Fyll ut og signer."),
        ("kontrakter/fremtidsfullmakt/", "🤲", "Fremtidsfullmakt", "Hvem ivaretar deg ved sviktende helse."),
        ("tjenester/reklamasjon/", "✉️", "Reklamasjonsbrev", "Juridisk korrekt klage på et kjøp."),
    ]
    kontrakter_html = ""
    for url, em, navn, beskr in KONTRAKTER:
        kontrakter_html += f'''      <a href="{url}" class="sl-kort">
        <div class="sl-em">{em}</div>
        <div class="sl-info">
          <div class="sl-navn">{navn}</div>
          <div class="sl-beskr">{beskr}</div>
        </div>
        <div class="sl-pil">→</div>
      </a>
'''

    # Slide 3 — viktige lover
    counts = {}
    displays = {}
    for p in PARAGRAPHS:
        counts[p["lov"]] = counts.get(p["lov"], 0) + 1
        displays[p["lov"]] = p["lov_display"]
    LOV_DESC = {
        "arveloven": "Arv, testament og pliktdel",
        "husleieloven": "Rettigheter ved leie av bolig",
        "kjopsloven": "Kjøp privat — privatperson til privatperson",
        "forbrukerkjopsloven": "Kjøp som forbruker — strengeste vern",
        "avhendingslova": "Kjøp og salg av bolig, hytte, tomt",
        "angrerettloven": "Angre kjøp gjort på nett og utenfor butikk",
    }
    TOP_LOVER = ["arveloven", "husleieloven", "kjopsloven", "forbrukerkjopsloven", "avhendingslova", "angrerettloven"]
    lover_html = ""
    for lov in TOP_LOVER:
        if lov in counts:
            lover_html += f'''      <a href="lover/{lov}/" class="sl-kort">
        <div class="sl-info">
          <div class="sl-navn">{displays[lov]}</div>
          <div class="sl-beskr">{LOV_DESC.get(lov, "")}</div>
        </div>
        <div class="sl-tall">{counts[lov]}</div>
        <div class="sl-pil">→</div>
      </a>
'''

    return f"""{shared_head('rettsregel.no — Norske lover på vanlig norsk', 'Lover er ikke vanskelige. De er bare dårlig forklart. Bla i norske lover, paragraf for paragraf.', depth=0, canonical_path='/')}
{site_nav(depth=0)}

<style>
/* === SLIDE-FORSIDE — Apple-raffinert === */
.home-slide {{
  padding: 128px 24px;
  border-bottom: 1px solid var(--line);
}}
.home-slide-inner {{ max-width: 1080px; margin: 0 auto; }}

/* HERO */
.sl-hero {{
  min-height: calc(100vh - 80px);
  display: flex; flex-direction: column; justify-content: center;
  padding: 100px 24px 80px;
  border-bottom: 1px solid var(--line);
  position: relative;
}}
.sl-hero-inner {{ max-width: 1080px; margin: 0 auto; width: 100%; }}
.sl-hero h1 {{
  font-family: var(--serif); font-weight: 400;
  font-size: clamp(46px, 8vw, 104px); line-height: 1.0;
  letter-spacing: -0.035em; margin: 0;
  font-feature-settings: "liga" 1, "dlig" 1;
  font-variation-settings: "opsz" 120, "SOFT" 50, "WONK" 0;
}}
.sl-hero h1 em {{ font-style: italic; color: var(--accent); font-weight: 400; }}
.sl-hero .sl-hero-meta {{
  font-family: var(--sans); font-size: 13px;
  color: var(--ink-mute); letter-spacing: 0.06em;
  margin-top: 56px;
  display: flex; gap: 18px; flex-wrap: wrap; align-items: center;
}}
.sl-hero .sl-hero-meta .dot {{ opacity: 0.3; }}
.sl-hero .sl-hero-scroll {{
  position: absolute; bottom: 44px; left: 50%; transform: translateX(-50%);
  display: flex; flex-direction: column; align-items: center; gap: 10px;
  font-family: var(--sans); font-size: 10.5px;
  color: var(--ink-mute); letter-spacing: 0.2em; text-transform: uppercase;
  text-decoration: none; font-weight: 500;
  animation: sl-bob 2.6s ease-in-out infinite;
}}
.sl-hero .sl-hero-scroll svg {{ stroke: var(--ink-mute); }}
@keyframes sl-bob {{
  0%, 100% {{ transform: translate(-50%, 0); opacity: 0.55; }}
  50% {{ transform: translate(-50%, 6px); opacity: 1; }}
}}

/* GENERELL SLIDE */
.sl-kicker {{
  font-family: var(--sans); font-size: 11px;
  font-weight: 700; text-transform: uppercase; letter-spacing: 0.2em;
  color: var(--accent); margin-bottom: 20px; display: block;
}}
.sl-h2 {{
  font-family: var(--serif); font-weight: 400;
  font-size: clamp(32px, 4.6vw, 52px); line-height: 1.05;
  letter-spacing: -0.026em; margin: 0 0 20px 0; max-width: 760px;
  font-variation-settings: "opsz" 72, "SOFT" 50;
}}
.sl-lead {{
  font-size: 18px; color: var(--ink-soft); line-height: 1.55;
  max-width: 580px; margin: 0 0 56px 0;
  font-weight: 400;
}}

/* KORT-GRID */
.sl-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 12px; }}
.sl-kort {{
  background: var(--bg-card); border: 1px solid var(--line); border-radius: 22px;
  padding: 28px 28px; text-decoration: none; color: var(--ink);
  display: flex; align-items: center; gap: 20px;
  transition: border-color 0.2s, box-shadow 0.2s, transform 0.18s;
}}
.sl-kort:hover {{
  border-color: var(--accent-soft);
  box-shadow: 0 12px 32px rgba(0,0,0,0.05);
  transform: translateY(-2px);
}}
.sl-kort:hover .sl-pil {{ transform: translateX(5px); color: var(--accent); }}
.sl-em {{
  font-size: 26px; width: 52px; height: 52px;
  background: linear-gradient(135deg, rgba(177,74,42,0.10), rgba(177,74,42,0.04));
  border-radius: 14px;
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}}
.sl-info {{ flex: 1; min-width: 0; }}
.sl-navn {{ font-family: var(--serif); font-size: 20px; font-weight: 400; letter-spacing: -0.012em; line-height: 1.2; margin-bottom: 5px; font-variation-settings: "opsz" 24; }}
.sl-beskr {{ font-size: 13.5px; line-height: 1.5; color: var(--ink-soft); }}
.sl-tall {{ font-family: var(--serif); font-size: 28px; color: var(--ink); font-variant-numeric: tabular-nums; font-weight: 400; letter-spacing: -0.02em; font-variation-settings: "opsz" 36; }}
.sl-pil {{ font-size: 18px; color: var(--ink-mute); transition: transform 0.2s, color 0.2s; flex-shrink: 0; }}

.sl-cta-rad {{ margin-top: 56px; display: flex; gap: 14px; flex-wrap: wrap; align-items: center; }}
.sl-cta {{
  font-family: var(--sans); font-size: 14px; font-weight: 600;
  text-decoration: none; padding: 14px 26px; border-radius: 100px;
  transition: all 0.2s; display: inline-flex; align-items: center; gap: 10px;
}}
.sl-cta-primary {{ background: var(--ink); color: var(--bg); }}
.sl-cta-primary:hover {{ background: var(--accent); transform: translateY(-1px); box-shadow: 0 8px 20px rgba(177,74,42,0.25); }}
.sl-cta-ghost {{ color: var(--ink-soft); border: 1px solid var(--line); }}
.sl-cta-ghost:hover {{ border-color: var(--accent); color: var(--accent); }}

/* SLIDE 4 — KATEGORIER */
.sl-kat-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; }}
.sl-kat {{
  background: var(--bg-card); border: 1px solid var(--line); border-radius: 24px;
  padding: 40px 32px; text-decoration: none; color: var(--ink); display: block;
  transition: border-color 0.2s, transform 0.2s, box-shadow 0.2s;
}}
.sl-kat:hover {{
  border-color: var(--accent-soft);
  transform: translateY(-3px);
  box-shadow: 0 16px 36px rgba(0,0,0,0.06);
}}
.sl-kat-em {{
  font-size: 40px; line-height: 1; margin-bottom: 22px;
  width: 72px; height: 72px;
  background: linear-gradient(135deg, rgba(177,74,42,0.10), rgba(177,74,42,0.04));
  border-radius: 18px;
  display: flex; align-items: center; justify-content: center;
}}
.sl-kat-navn {{ font-family: var(--serif); font-size: 24px; font-weight: 400; letter-spacing: -0.012em; line-height: 1.2; margin-bottom: 8px; font-variation-settings: "opsz" 28; }}
.sl-kat-beskr {{ font-size: 13.5px; color: var(--ink-soft); line-height: 1.55; }}

@media (max-width: 700px) {{
  .home-slide {{ padding: 80px 24px; }}
  .sl-hero {{ padding: 70px 24px 50px; min-height: calc(100vh - 60px); }}
  .sl-hero-scroll {{ bottom: 28px; }}
  .sl-kort {{ padding: 22px 22px; border-radius: 18px; }}
  .sl-kat {{ padding: 30px 24px; border-radius: 20px; }}
}}
</style>

<main>

  <section class="sl-hero">
    <div class="sl-hero-inner">
      <h1>Lover er ikke vanskelige.<br><em>De er bare dårlig forklart.</em></h1>
      <div class="sl-hero-meta">
        <span>{total_paragrafer} paragrafer</span>
        <span class="dot">·</span>
        <span>{total_lover} lover</span>
        <span class="dot">·</span>
        <span>92 verktøy</span>
        <span class="dot">·</span>
        <span>på vanlig norsk</span>
      </div>
    </div>
    <a href="#begynn" class="sl-hero-scroll">
      <span>Bla</span>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
    </a>
  </section>

  <section class="home-slide" id="begynn">
    <div class="home-slide-inner">
      <span class="sl-kicker">Begynn her</span>
      <h2 class="sl-h2">Viktige kontrakter og maler</h2>
      <p class="sl-lead">Seks dokumenter de fleste nordmenn trenger en eller annen gang i livet. Fyll ut og signer — gratis, basert på norsk lov.</p>
      <div class="sl-grid">
{kontrakter_html}      </div>
      <div class="sl-cta-rad">
        <a href="tjenester/" class="sl-cta sl-cta-primary">Se alle 92 verktøy <span>→</span></a>
      </div>
    </div>
  </section>

  <section class="home-slide" style="background:var(--bg-alt)">
    <div class="home-slide-inner">
      <span class="sl-kicker">Lovsamling</span>
      <h2 class="sl-h2">{total_paragrafer} paragrafer, forklart</h2>
      <p class="sl-lead">Lovteksten slik den står — og hva den faktisk betyr. På vanlig norsk.</p>
      <div class="sl-grid">
{lover_html}      </div>
      <div class="sl-cta-rad">
        <a href="lover/" class="sl-cta sl-cta-primary">Se alle lover <span>→</span></a>
      </div>
    </div>
  </section>

  <section class="home-slide">
    <div class="home-slide-inner">
      <span class="sl-kicker">Verktøy</span>
      <h2 class="sl-h2">Hva trenger du hjelp med?</h2>
      <p class="sl-lead">Velg en livssituasjon — så finner du verktøyene som hører til.</p>
      <div class="sl-kat-grid">
        <a href="tjenester/#leier-bolig" class="sl-kat">
          <div class="sl-kat-em">🏠</div>
          <div class="sl-kat-navn">Bolig og leie</div>
          <div class="sl-kat-beskr">Husleiekontrakt, depositum, leieøkning, oppsigelse.</div>
        </a>
        <a href="tjenester/#arv-og-familie" class="sl-kat">
          <div class="sl-kat-em">👨‍👩‍👧</div>
          <div class="sl-kat-navn">Arv og familie</div>
          <div class="sl-kat-beskr">Testament, samboeravtale, ektepakt, samvær.</div>
        </a>
        <a href="tjenester/#jobber" class="sl-kat">
          <div class="sl-kat-em">💼</div>
          <div class="sl-kat-navn">Arbeid</div>
          <div class="sl-kat-beskr">Arbeidsavtale, feriepenger, oppsigelse, overtid.</div>
        </a>
        <a href="tjenester/#kjop" class="sl-kat">
          <div class="sl-kat-em">🛒</div>
          <div class="sl-kat-navn">Kjøp og forbruk</div>
          <div class="sl-kat-beskr">Reklamasjon, angrerett, mangel, prisavslag.</div>
        </a>
      </div>
    </div>
  </section>

  <section class="home-slide" style="background:var(--bg-alt)">
    <div class="home-slide-inner">
      <span class="sl-kicker">Spørsmål</span>
      <h2 class="sl-h2">Har du et konkret spørsmål?</h2>
      <p class="sl-lead">Roy svarer på vanlig norsk og peker deg til paragrafen som gjelder. Eller bla i {len(SPORSMAL)} ferdige spørsmål-og-svar.</p>
      <div class="sl-cta-rad">
        <a href="sporsmal/" class="sl-cta sl-cta-primary">Bla i spørsmål <span>→</span></a>
        <a href="#" onclick="document.getElementById('chat-toggle').click();return false;" class="sl-cta sl-cta-ghost">💬 Spør Roy nå</a>
      </div>
    </div>
  </section>

{contact_form(depth=0)}

</main>

{site_footer(depth=0)}"""


def render_tjenester_hub():
    """Verktøy-hub — varmt, menneskelig, levende. Med emojis og puls."""

    # (url, navn, beskrivelse, emoji)
    SEKSJONER = [
        ("📮", "Når noe har gått galt med et kjøp", [
            ("../tjenester/reklamasjon/", "Reklamasjonsbrev", "Juridisk korrekt klage med riktige lovhenvisninger.", "✉️"),
            ("../tjenester/reklamasjonsfrist/", "Reklamasjonsfrist", "Har du fortsatt rett til å klage? 2 eller 5 år.", "⏰"),
            ("../tjenester/angrefrist/", "Angrefrist", "Har du fortsatt rett til å angre kjøpet?", "↩️"),
            ("../tjenester/angreskjema/", "Angrerettskjema", "EU-standardskjema, ferdig utfylt.", "📋"),
            ("../tjenester/mangel/", "Mangel-sjekker", "Er feilen en juridisk mangel — eller bare slitasje?", "🔍"),
            ("../tjenester/heving/", "Heving av kjøp", "Kan du gå fra hele kjøpet og få pengene tilbake?", "💸"),
            ("../tjenester/prisavslag/", "Prisavslag", "Hvor mye kan du kreve i avslag for feilen?", "💰"),
            ("../tjenester/reklamasjon-bil/", "Reklamasjon bil", "Brev ved feil på bilen du kjøpte.", "🚗"),
            ("../tjenester/kredittkjop/", "Kredittkjøp-sjekker", "Er banken medansvarlig når selger svikter?", "💳"),
            ("../tjenester/handverker-reklamasjon/", "Håndverker-reklamasjon", "Brev ved dårlig utført håndverkertjeneste.", "🔨"),
        ]),
        ("🏠", "Når du leier bolig", [
            ("../kontrakter/husleiekontrakt/", "Husleiekontrakt", "Tidsubestemt eller tidsbestemt. Fyll ut og signer.", "📝"),
            ("../kontrakter/fremleiekontrakt/", "Fremleiekontrakt", "Fremleie hele eller deler av boligen din.", "🔑"),
            ("../tjenester/leie-okning/", "Leieøkning", "Maks lovlig økning etter KPI — pluss ferdig varselbrev.", "📈"),
            ("../tjenester/depositum/", "Depositum-kalkulator", "Maks lovlig depositum basert på månedsleien.", "💵"),
            ("../tjenester/depositum-tilbake/", "Depositum tilbake", "Depositum + renter du har krav på.", "↩️"),
            ("../tjenester/husleie-oppsigelse/", "Oppsigelsestid", "Lovlig oppsigelsestid for utleier og leietaker.", "📅"),
            ("../tjenester/vedlikehold/", "Vedlikeholdsansvar", "Utleier eller leietaker — hvem fikser hva?", "🛠️"),
            ("../tjenester/fremleie/", "Fremleie-sjekker", "Kan du fremleie? Kan utleier nekte?", "❓"),
            ("../kontrakter/depositumavtale/", "Depositumavtale", "Sperret konto, maks 6 mnd. Husleieloven § 3-5.", "🏦"),
            ("../kontrakter/leiekontrakt-naring/", "Leiekontrakt næring", "Kontor, butikk, lager. KPI-regulering.", "🏢"),
        ]),
        ("🔑", "Når du kjøper, eier eller selger bolig", [
            ("../tjenester/reklamasjonsfrist-bolig/", "Reklamasjonsfrist bolig", "5-årsregel + 2-månedersfrist for å klage.", "⏳"),
            ("../tjenester/vesentlig-mangel-bolig/", "Vesentlig mangel bolig", "Over Høyesteretts 3–6 %-terskel?", "⚖️"),
            ("../tjenester/selger-opplysningsplikt/", "Selgers opplysningsplikt", "Holdt selger tilbake info? §§ 3-7 og 3-8.", "🗣️"),
            ("../tjenester/prisavslag-bolig/", "Prisavslag bolig", "Beregn krav basert på utbedringskostnad.", "💷"),
            ("../tjenester/dagmulkt/", "Dagmulkt", "Dagmulkt ved forsinket boligovertakelse.", "📆"),
            ("../tjenester/boligkjoper-sjekkliste/", "Boligkjøper-sjekkliste", "8 punkter — ivareta undersøkelsesplikten.", "✅"),
            ("../kontrakter/overtakelsesprotokoll/", "Overtakelsesprotokoll", "Målere, nøkler, feil. Avgjørende dokumentasjon.", "🗝️"),
            ("../kontrakter/nabovarsel/", "Nabovarsel", "Påkrevd før byggesøknad. 2 ukers merknadsfrist.", "🏘️"),
            ("../kontrakter/kjopekontrakthytte/", "Kjøpekontrakt hytte", "Fritidseiendom og tomt. Avhendingslova.", "🏕️"),
            ("../kontrakter/sameieandel/", "Sameierklæring", "Hvem eier hva? Dokumentér sameieandeler.", "🤝"),
            ("../kontrakter/bruksrettsavtale/", "Bruksrettsavtale", "Gi rett til å bruke noe — uten å overdra eierskap.", "📜"),
        ]),
        ("💼", "Når du jobber", [
            ("../tjenester/feriepenger/", "Feriepenger", "Standard, tariff og over 60. Med utregning.", "🌴"),
            ("../tjenester/arbeid-oppsigelse/", "Oppsigelsestid", "Lovlig varsel basert på ansettelsestid + alder.", "📤"),
            ("../tjenester/overtid/", "Overtid-kalkulator", "Beregn overtid med lovpålagt tillegg.", "⏱️"),
            ("../tjenester/usaklig-oppsigelse/", "Usaklig oppsigelse", "Saklig grunn, saksbehandling, sykevern.", "⚠️"),
            ("../tjenester/sykmelding-vern/", "Sykmelding-vern", "Er du vernet de første 12 månedene?", "🤒"),
            ("../tjenester/permittering/", "Permittering-sjekker", "Lovlig varsel og arbeidsgiverperiode?", "📋"),
            ("../tjenester/konkurranse-klausul/", "Konkurranse-/kundeklausul", "Gyldig? Kompensasjon og maksvarighet.", "🚫"),
            ("../tjenester/arbeidskontrakt/", "Arbeidskontrakt-sjekker", "Alle lovpålagte minimumsopplysninger?", "📑"),
            ("../kontrakter/arbeidsavtale/", "Arbeidsavtale (fast)", "Alle aml. § 14-6-krav. Fyll ut og signer.", "✍️"),
            ("../kontrakter/arbeidsavtale-deltid/", "Arbeidsavtale (deltid)", "Stillingsprosent og fortrinnsrett.", "📝"),
            ("../kontrakter/arbeidsavtale-midlertidig/", "Arbeidsavtale (midlertidig)", "Vikariat, prosjekt og sesong.", "⏲️"),
            ("../kontrakter/sluttavtale/", "Sluttavtale", "Frivillig avslutning av arbeidsforhold.", "👋"),
            ("../kontrakter/taushetserklaring/", "Taushetserklæring (NDA)", "For ansatte, konsulenter, samarbeidspartnere.", "🤐"),
            ("../kontrakter/arbeidsattest/", "Arbeidsattest", "Alle ansatte har rett på attest. Aml. § 15-15.", "📜"),
        ]),
        ("👨‍👩‍👧", "Når det handler om arv og familie", [
            ("../tjenester/arv/", "Arvefordeling", "Visuell oversikt basert på familiesituasjonen.", "⚖️"),
            ("../tjenester/testament-mal/", "Testament-mal", "Generer testament-utkast med vitnefelt.", "📜"),
            ("../tjenester/pliktdel/", "Pliktdel", "Hva kan du testamentere bort? 2/3-regelen.", "🧮"),
            ("../tjenester/uskifte/", "Uskifte-sjekker", "Kan gjenlevende sitte i uskifte?", "👴"),
            ("../tjenester/samboer-arverett/", "Samboer-arverett", "Arver samboeren din uten testament?", "❤️"),
            ("../tjenester/arvegjeld/", "Arvegjeld-sjekker", "Overtar du avdødes gjeld?", "💸"),
            ("../kontrakter/gavebrev/", "Gavebrev", "Med særeie-klausul og arveforskudd.", "🎁"),
            ("../kontrakter/ektepakt/", "Ektepakt (særeie)", "Gjør formue til særeie. Husk tinglysning.", "💍"),
            ("../kontrakter/ektepakt-felleseie/", "Ektepakt (arv som særeie)", "Felleseie, men arv og gaver beskyttes.", "🛡️"),
            ("../kontrakter/fremtidsfullmakt/", "Fremtidsfullmakt", "Hvem ivaretar deg ved sviktende helse.", "🤲"),
            ("../kontrakter/samvaersavtale/", "Samværsavtale", "Barnets hverdag etter samlivsbrudd.", "👶"),
            ("../kontrakter/skifteavtale/", "Skifteavtale", "Bolig, bil, gjeld ved samlivsbrudd.", "🔀"),
            ("../kontrakter/samboeravtale/", "Samboeravtale", "Hvem eier hva ved brudd? Signer i dag.", "🤝"),
        ]),
        ("🏢", "Når du driver virksomhet", [
            ("../tjenester/enk-eller-as/", "ENK eller AS?", "Optimal selskapsform med skatteillustrasjon.", "🏗️"),
            ("../tjenester/utbytte-skatt/", "Utbytte-skatt", "Effektiv sats 37,84 %. Netto utbytte.", "📊"),
            ("../tjenester/omdanning-enk-as/", "Omdanning ENK→AS", "Er det lønnsomt? Skattesammenligning.", "🔄"),
            ("../tjenester/styreansvar/", "Styreansvar-sjekker", "Personlig ansvar? Handleplikt og insolvens.", "🚨"),
            ("../tjenester/aksjekapital/", "Aksjekapital-sjekker", "Handleplikt og utbytteregler.", "💼"),
            ("../tjenester/aksjonaravtale/", "Aksjonæravtale-sjekker", "10-punkts sjekkliste.", "📋"),
            ("../kontrakter/stiftelsesdokument/", "Stiftelsesdokument AS", "Stift AS med vedtekter. Registrer i Altinn.", "🏛️"),
            ("../kontrakter/aksjonaravtale2/", "Aksjonæravtale", "Forkjøpsrett, tag-along, utbytte, exit.", "🤝"),
            ("../kontrakter/aksjekjopekontrakt/", "Aksjekjøpekontrakt", "Overdragelse av aksjer med garantier.", "📈"),
            ("../kontrakter/opsjonsavtale/", "Opsjonsavtale ansatte", "Vesting-periode og innløsningspris.", "🎯"),
            ("../kontrakter/styreprotokoll/", "Styreprotokoll", "Protokollér styremøtet riktig. Asl. § 6-29.", "🗒️"),
            ("../kontrakter/generalforsamlingsprotokoll/", "Generalforsamlingsprotokoll", "Protokollér GF riktig. Asl. § 5-16.", "📜"),
            ("../kontrakter/konsulentavtale/", "Konsulentavtale", "For frilansere og selvstendige konsulenter.", "💻"),
            ("../kontrakter/leverandoravtale/", "Leverandøravtale", "Kjøp av varer og tjenester over tid.", "📦"),
            ("../kontrakter/samarbeidsavtale/", "Samarbeidsavtale", "Strategisk samarbeid mellom virksomheter.", "🤝"),
            ("../kontrakter/overdragelsesavtale/", "Overdragelsesavtale", "Salg av virksomhet. Goodwill, kunder, inventar.", "🔄"),
            ("../kontrakter/tjenesteavtale/", "Tjenesteavtale", "For malere, vaskehjelp, håndverkere.", "🧹"),
            ("../kontrakter/consignmentavtale/", "Consignmentavtale", "Selg kunst eller varer på vegne av en annen.", "🎨"),
        ]),
        ("💰", "Når du har gjeld eller låner", [
            ("../tjenester/inkasso/", "Inkasso-sjekk", "Er kravet lovlig? Foreldelse og gebyrer.", "🔎"),
            ("../kontrakter/gjeldsbrev/", "Gjeldsbrev", "Privatlån mellom venner og familie.", "📃"),
            ("../kontrakter/panteavtale/", "Panteavtale", "Sikre lån med pant i bil eller løsøre.", "🔒"),
            ("../kontrakter/kausjonsavtale/", "Kausjonsavtale", "Simpel eller selvskyldnerkausjon.", "✋"),
            ("../kontrakter/betalingsplan/", "Betalingsplan", "Nedbetaling av gjeld i avdrag.", "📅"),
            ("../kontrakter/misligholdsvarsel/", "Misligholdsvarsel", "Siste varsel før inkasso. Auto-beregner beløp.", "⚠️"),
        ]),
        ("✉️", "Brev, klager og personvern", [
            ("../tjenester/fullmakt-mal/", "Fullmakt-mal", "Fullmakt for Nav, bank, eiendom m.m.", "🖊️"),
            ("../tjenester/gdpr-innsyn/", "GDPR-innsynskrav", "Be selskaper om å vise dine data.", "🔐"),
            ("../tjenester/forsikringsavslag/", "Forsikringsavslag", "Grunnlag for klage? Finansklagenemnda.", "🛡️"),
            ("../tjenester/klagefrist/", "Klagefrist forvaltning", "3 uker etter vedtak. Utløpt?", "⏲️"),
            ("../tjenester/pakkereis/", "Pakkereis-kalkulator", "250–600 EUR ved forsinkelse. EU 261/2004.", "✈️"),
            ("../kontrakter/kvittering/", "Kvittering", "Kontantbetaling, depositum og håndverk.", "🧾"),
            ("../kontrakter/kjopekontraktbil/", "Kjøpekontrakt bil", "Privatbilsalg, basert på kjøpsloven.", "🚙"),
            ("../kontrakter/kjopekontraktbat/", "Kjøpekontrakt båt", "Privat båtsalg med tilstandsklausul.", "⛵"),
            ("../kontrakter/kjopekontraktgjenstand/", "Kjøpekontrakt eiendeler", "Finn.no-kjøp: møbler, elektronikk, mer.", "📦"),
        ]),
    ]

    seksjoner_html = ""
    total = 0
    for emoji_h, tittel, verktoy in SEKSJONER:
        total += len(verktoy)
        kort = ""
        for url, navn, beskr, em in verktoy:
            kort += f'''        <a href="{url}" class="vh-kort">
          <div class="vh-em">{em}</div>
          <div class="vh-tx">
            <div class="vh-navn">{navn}</div>
            <div class="vh-beskr">{beskr}</div>
          </div>
          <div class="vh-pil">→</div>
        </a>
'''
        seksjoner_html += f'''    <section class="vh-seksjon">
      <h2 class="vh-seksjon-tittel"><span class="vh-seksjon-em">{emoji_h}</span> {tittel}</h2>
      <div class="vh-grid">
{kort}      </div>
    </section>
'''

    return f"""{shared_head(
        'Verktøy — alle juridiske kalkulatorer og kontraktsmaler | Rettsregel',
        f'{total} gratis juridiske verktøy basert på norsk lov. Kalkulatorer, brevgeneratorer, kontraktsmaler. Ingen registrering.',
        depth=1, canonical_path='/tjenester/'
    )}
<body>
{site_nav(depth=1)}
<style>
.vh-page {{ max-width: 1140px; margin: 0 auto; padding: 0 24px; }}
.vh-hero {{ padding: 56px 0 44px; margin-bottom: 24px; }}
.vh-hero h1 {{ font-family: var(--serif); font-weight: 400; font-size: clamp(34px, 4.6vw, 56px); letter-spacing: -0.025em; line-height: 1.04; margin: 0 0 18px 0; max-width: 760px; }}
.vh-hero h1 em {{ font-style: italic; color: var(--accent); font-weight: 400; }}
.vh-hero .vh-lead {{ font-size: 18px; line-height: 1.55; color: var(--ink-soft); max-width: 580px; margin: 0; }}
.vh-hero .vh-meta {{ font-family: var(--sans); font-size: 13px; color: var(--ink-mute); letter-spacing: 0.02em; margin-top: 24px; }}
.vh-hero .vh-meta strong {{ color: var(--accent); font-weight: 700; }}

.vh-seksjon {{ margin-bottom: 56px; }}
.vh-seksjon-tittel {{ font-family: var(--serif); font-weight: 400; font-size: clamp(22px, 2.6vw, 28px); letter-spacing: -0.015em; line-height: 1.2; margin: 0 0 24px 0; display: flex; align-items: center; gap: 12px; padding-bottom: 14px; border-bottom: 1px solid var(--line); }}
.vh-seksjon-em {{ font-size: 26px; line-height: 1; }}

.vh-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 14px; }}
.vh-kort {{ background: var(--bg-card); border: 1px solid var(--line); border-radius: 14px; padding: 18px 20px; text-decoration: none; color: var(--ink); display: flex; align-items: flex-start; gap: 14px; transition: border-color 0.15s, box-shadow 0.15s, transform 0.13s; position: relative; }}
.vh-kort:hover {{ border-color: var(--accent-soft); box-shadow: 0 6px 20px rgba(0,0,0,0.04); transform: translateY(-1px); }}
.vh-kort:hover .vh-pil {{ transform: translateX(4px); color: var(--accent); }}

.vh-em {{ font-size: 22px; line-height: 1; width: 42px; height: 42px; display: flex; align-items: center; justify-content: center; background: rgba(177,74,42,0.06); border-radius: 10px; flex-shrink: 0; }}
.vh-tx {{ flex: 1; min-width: 0; }}
.vh-navn {{ font-family: var(--serif); font-size: 17px; font-weight: 400; letter-spacing: -0.005em; line-height: 1.25; margin-bottom: 4px; }}
.vh-beskr {{ font-size: 13px; line-height: 1.5; color: var(--ink-soft); }}
.vh-pil {{ font-size: 16px; color: var(--ink-mute); align-self: center; transition: transform 0.13s, color 0.13s; flex-shrink: 0; }}

@media (max-width: 600px) {{
  .vh-hero {{ padding: 36px 0 28px; margin-bottom: 16px; }}
  .vh-seksjon {{ margin-bottom: 44px; }}
  .vh-grid {{ grid-template-columns: 1fr; }}
}}
</style>

<main>
  <div class="vh-page">

    <header class="vh-hero">
      <h1>Gjør det <em>selv</em>.</h1>
      <p class="vh-lead">{total} verktøy som faktisk virker. Skrevet for å løse problemet ditt på minutter, ikke timer.</p>
      <div class="vh-meta"><strong>Gratis.</strong> Ingen registrering. Basert på gjeldende norsk rett.</div>
    </header>

{seksjoner_html}

  </div>
</main>

{site_footer(depth=1)}"""


def render_enk_eller_as():
    return f"""{shared_head(
        'ENK eller AS? Finn ut hva som passer for deg — Rettsregel',
        'Fyll ut skjemaet og få en selskapsrettslig anbefaling med skatteillustrasjon — gratis.',
        depth=2, canonical_path='/tjenester/enk-eller-as/'
    )}
<body>
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
<body>
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
<body>
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
<body>
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
<body>
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
<body>
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
<body>
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
<body>
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
<body>
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
<body>
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
