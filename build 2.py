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

PARAGRAPHS = _P_BASE + _P_KJOPSLOVEN + _P_HUSLEIELOVEN + _P_AVHENDINGSLOVA + _P_NABOLOVEN

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
  --bg: #FBF8F1;
  --bg-alt: #F4EFE3;
  --bg-card: #FFFFFF;
  --ink: #1A1612;
  --ink-soft: #4E443A;
  --ink-mute: #8A7F70;
  --accent: #B14A2A;
  --accent-deep: #913B20;
  --accent-soft: #E8B5A3;
  --line: rgba(26, 22, 18, 0.10);
  --line-strong: rgba(26, 22, 18, 0.20);
  --shadow-sm: 0 1px 2px rgba(26, 22, 18, 0.04);
  --shadow-md: 0 2px 8px rgba(26, 22, 18, 0.06);
  --shadow-lg: 0 8px 24px rgba(26, 22, 18, 0.08);
  --kat-bolig: #4F6F5E;
  --kat-forbruk: #B14A2A;
  --kat-arbeid: #6B5B95;
  --kat-familie: #B8654A;
  --kat-gjeld: #7A6E5D;
  --kat-tjenester: #4E6E80;
  --serif: 'EB Garamond', Garamond, Georgia, serif;
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
  content: ''; position: fixed; inset: 0; pointer-events: none; z-index: 100; opacity: 0.35;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.12 0 0 0 0 0.1 0 0 0 0 0.08 0 0 0 0.18 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
.container { max-width: 1100px; margin: 0 auto; padding: 0 32px; }
main.page { max-width: 1100px; margin: 0 auto; padding: 0 32px; min-height: calc(100vh - 200px); }
@media (max-width: 720px) {
  .container { padding: 0 20px; }
  main.page { padding: 0 20px; }
}
.narrow { max-width: 740px; margin: 0 auto; padding: 0 32px; }

nav.site-nav { padding: 28px 0; display: flex; justify-content: space-between; align-items: center; }
.logo {
  display: inline-flex; align-items: baseline; gap: 10px;
  text-decoration: none; line-height: 1;
}
.logo .mark {
  font-family: var(--serif); font-weight: 400;
  font-size: 28px; color: var(--accent);
  font-variation-settings: "opsz" 36;
  line-height: 1;
}
.logo .wordmark {
  font-family: var(--serif); font-weight: 500;
  font-size: 22px; letter-spacing: -0.01em;
  color: var(--ink); font-variation-settings: "opsz" 36;
  line-height: 1;
}
.nav-links { display: flex; gap: 32px; list-style: none; }
.nav-links a { color: var(--ink-soft); text-decoration: none; font-size: 14px; font-weight: 500; transition: color 0.2s; letter-spacing: 0.005em; }
.nav-links a:hover { color: var(--accent); }

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
  font-size: clamp(28px, 3.4vw, 40px);
  line-height: 1.12; letter-spacing: -0.015em; margin-bottom: 24px;
  font-variation-settings: "opsz" 40;
}
.article-title .paragraf-num { color: var(--accent); font-style: italic; }
.article-description {
  font-size: 19px; color: var(--ink-soft); line-height: 1.55; max-width: 700px;
}

/* Kort svar — featured callout */
.kort-svar {
  background: var(--bg-alt); border-left: 4px solid var(--accent);
  padding: 28px 32px; border-radius: 0 12px 12px 0;
  margin: 16px 0 48px;
}
.kort-svar .kort-svar-label {
  font-size: 12px; font-weight: 700; color: var(--accent);
  text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 12px;
}
.kort-svar p {
  font-size: 18px; line-height: 1.55; color: var(--ink); margin: 0;
}

/* Article body */
.article-body {
  font-size: 17px; line-height: 1.7;
}
.article-body h2 {
  font-family: var(--serif); font-weight: 500;
  font-size: clamp(26px, 3vw, 34px);
  line-height: 1.2; letter-spacing: -0.01em;
  margin: 56px 0 20px;
  font-variation-settings: "opsz" 36;
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
  background: var(--bg-alt); padding: 80px 0 100px;
  margin-top: 100px;
}
.cta-grid {
  display: grid; grid-template-columns: 1fr 1.2fr; gap: 72px; align-items: start;
}
@media (max-width: 900px) { .cta-grid { grid-template-columns: 1fr; gap: 40px; } }
.cta-intro h2 {
  font-family: var(--serif); font-weight: 400;
  font-size: clamp(30px, 4vw, 44px); line-height: 1.1;
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
.form-note { margin-top: 14px; font-size: 13px; color: var(--ink-mute); text-align: center; }
.form-success { display: none; background: var(--bg); padding: 40px; border-radius: 20px; border: 1px solid var(--accent-soft); text-align: center; }
.form-success.show { display: block; }
form.contact-form.hide { display: none; }
.form-success h3 { font-family: var(--serif); font-size: 24px; margin-bottom: 10px; font-variation-settings: "opsz" 28; }
.form-success p { color: var(--ink-soft); }

/* Footer — redesigned */
footer.site-footer {
  background: #0D0C09;
  color: rgba(250,246,238,0.7);
  padding: 80px 0 44px;
}
.footer-inner {
  display: grid; grid-template-columns: 1.8fr 1fr 1fr 1fr;
  gap: 48px; margin-bottom: 56px;
}
@media (max-width: 900px) { .footer-inner { grid-template-columns: 1fr 1fr; gap: 32px 40px; } }
@media (max-width: 540px) { .footer-inner { grid-template-columns: 1fr; gap: 28px; } }
.footer-logo {
  display: flex; align-items: baseline; gap: 10px;
  text-decoration: none; margin-bottom: 20px; line-height: 1;
}
.footer-logo-mark { font-family: var(--serif); font-size: 28px; color: var(--accent); }
.footer-logo-name { font-family: var(--serif); font-size: 22px; color: rgba(250,246,238,0.9); }
.footer-tagline {
  font-size: 15px; line-height: 1.65;
  color: rgba(250,246,238,0.42); max-width: 260px; margin-bottom: 16px;
}
.footer-entity { font-size: 11px; color: rgba(250,246,238,0.22); text-transform: uppercase; letter-spacing: 0.1em; }
.footer-col-head {
  font-size: 11px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.14em; color: rgba(250,246,238,0.28); margin-bottom: 16px;
}
footer.site-footer ul { list-style: none; }
footer.site-footer li { margin-bottom: 11px; }
footer.site-footer a {
  color: rgba(250,246,238,0.58); text-decoration: none; font-size: 14px; transition: color 0.2s;
}
footer.site-footer a:hover { color: rgba(250,246,238,0.95); }
.footer-bottom {
  display: flex; justify-content: space-between; align-items: center;
  flex-wrap: wrap; gap: 10px;
  padding-top: 28px; border-top: 1px solid rgba(250,246,238,0.07);
  font-size: 12px; color: rgba(250,246,238,0.22); letter-spacing: 0.01em;
}

/* Hub — tjeneste og kontrakt-kort */
.tjenester-hero { padding: 48px 0 40px; }
.tjenester-hero h1 { font-family: var(--serif); font-weight: 400; font-size: clamp(28px, 3.4vw, 40px); line-height: 1.12; letter-spacing: -0.015em; margin-bottom: 16px; }
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

.lov-hero { padding: 56px 0 64px; max-width: 780px; }
.lov-hero h1 {
  font-family: var(--serif); font-weight: 400;
  font-size: clamp(46px, 6vw, 76px); line-height: 1.06;
  letter-spacing: -0.02em; margin-bottom: 24px;
  font-variation-settings: "opsz" 72;
}
.lov-hero h1 em { font-style: italic; color: var(--accent); }
.lov-hero p { font-size: 19px; color: var(--ink-soft); line-height: 1.55; }
.paragraph-list {
  margin: 32px 0 80px; display: grid; gap: 12px;
}
.paragraph-list-item {
  background: white; border: 1px solid var(--line); border-radius: 12px;
  padding: 22px 26px; text-decoration: none; color: inherit; display: block;
  transition: transform 0.2s, border-color 0.2s;
}
.paragraph-list-item:hover { transform: translateX(4px); border-color: var(--accent-soft); }
.paragraph-list-meta {
  font-size: 12px; font-weight: 600; color: var(--accent);
  text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 6px;
}
.paragraph-list-title {
  font-family: var(--serif); font-weight: 500; font-size: 20px;
  line-height: 1.3; color: var(--ink);
  font-variation-settings: "opsz" 22;
}
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
  font-size: clamp(38px, 5vw, 64px);
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
  font-size: clamp(32px, 4vw, 44px);
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
  font-size: clamp(38px, 5vw, 60px);
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
  font-size: clamp(26px, 3vw, 34px); line-height: 1.2;
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
   Hjemmeside — sentrert hero med søk
   ============================================================ */
.home-hero-v2 {
  padding: 88px 0 48px;
  max-width: 760px;
  margin: 0 auto;
  text-align: center;
}
.home-hero-v2 .kicker {
  font-family: var(--sans); font-size: 12px;
  letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--ink-mute); font-weight: 600;
  margin-bottom: 24px; display: block;
}
.home-hero-v2 h1 {
  font-family: var(--serif); font-weight: 500;
  font-size: clamp(28px, 3vw, 36px); line-height: 1.2;
  letter-spacing: -0.005em; margin: 0 auto;
  color: var(--ink);
  max-width: 640px;
}
.home-hero-v2 h1 em {
  font-style: italic; color: var(--accent);
  font-weight: 400;
}
.home-hero-v2 .lead {
  font-family: var(--sans); font-size: 17px;
  line-height: 1.55; color: var(--ink-soft);
  margin: 20px auto 0; max-width: 520px;
}

/* Søkeboks */
.search-wrapper {
  max-width: 580px;
  margin: 36px auto 0;
  position: relative;
}
.search-input-wrap {
  position: relative;
  background: var(--bg-card);
  border: 1px solid var(--line-strong);
  border-radius: 12px;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.search-input-wrap:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 4px var(--accent-soft);
}
.search-input {
  width: 100%;
  padding: 16px 20px 16px 52px;
  font-family: var(--sans); font-size: 16px;
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

/* Stats-band — mindre prominent */
.home-stats {
  display: flex; justify-content: center;
  gap: 48px; padding: 28px 0;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
  margin: 56px 0 56px;
  text-align: center;
}
.home-stat .num {
  font-family: var(--serif); font-size: 24px;
  font-weight: 500; line-height: 1; color: var(--ink);
  letter-spacing: -0.01em;
}
.home-stat .lbl {
  font-family: var(--sans); font-size: 11px;
  letter-spacing: 0.1em; text-transform: uppercase;
  color: var(--ink-mute); margin-top: 6px;
}

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
  font-family: var(--serif); font-size: clamp(20px, 2.2vw, 24px);
  font-weight: 500; letter-spacing: -0.005em; line-height: 1.2;
  margin: 0; color: var(--ink);
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
  font-size: clamp(26px, 3vw, 34px);
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
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}styles.css">
</head>
<body>"""

def site_nav(depth=0):
    prefix = "../" * depth
    return f"""<div class="container">
<nav class="site-nav">
  <a href="{prefix}" class="logo"><span class="mark">§</span><span class="wordmark">Rettsregel</span></a>
  <ul class="nav-links">
    <li><a href="{prefix}sporsmal/">Vanlige spørsmål</a></li>
    <li><a href="{prefix}lover/">Alle lover</a></li>
    <li><a href="{prefix}kontrakter/">Kontrakter</a></li>
    <li><a href="{prefix}tjenester/">Tjenester</a></li>
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
          <span class="footer-logo-mark">§</span>
          <span class="footer-logo-name">Rettsregel</span>
        </a>
        <p class="footer-tagline">Lover er ikke vanskelige.<br>De er bare dårlig forklart.</p>
        <span class="footer-entity">Wombat AS</span>
      </div>
      <div>
        <div class="footer-col-head">Innhold</div>
        <ul>
          <li><a href="{prefix}lover/">Alle lover</a></li>
          <li><a href="{prefix}sporsmal/">Spørsmål og svar</a></li>
          <li><a href="{prefix}kontrakter/">Kontraktsmaler</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-col-head">Verktøy</div>
        <ul>
          <li><a href="{prefix}tjenester/enk-eller-as/">ENK eller AS?</a></li>
          <li><a href="{prefix}tjenester/reklamasjon-bil/">Reklamasjon bil</a></li>
          <li><a href="{prefix}kontrakter/husleiekontrakt/">Husleiekontrakt</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-col-head">Om</div>
        <ul>
          <li><a href="{prefix}om/">Om Rettsregel</a></li>
          <li><a href="{prefix}personvern/">Personvern</a></li>
          <li><a href="mailto:rettsregel@gmail.com">Kontakt oss</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Wombat AS · Rettsregel.no</span>
      <span>Bygget for å forstås.</span>
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

{contact_form(depth=3)}
{site_footer(depth=3)}"""

def render_lov_index(lov_name, lov_display, paragraphs):
    """Overview page for a single law."""
    depth = 2  # /lover/[lov]/index.html
    prefix = "../" * depth
    items_html = ""
    for p in paragraphs:
        items_html += f'''<a href="{prefix}lover/{lov_name}/{p["number"]}/" class="paragraph-list-item">
  <div class="paragraph-list-meta">§ {p["number"]}</div>
  <div class="paragraph-list-title">{p["title"]}</div>
</a>\n'''
    
    return f"""{shared_head(f'{lov_display} — Forklart paragraf for paragraf | Rettsregel', f'Hele {lov_display.lower()} forklart på vanlig norsk. Bla i alle paragrafer.', depth=2, canonical_path=f'/lover/{lov_name}/')}
{site_nav(depth=2)}

<div class="container">
  <nav class="breadcrumbs" aria-label="Brødsmuler">
    <a href="{prefix}">Hjem</a>
    <span class="sep">/</span>
    <a href="{prefix}lover/">Lover</a>
    <span class="sep">/</span>
    <span class="current">{lov_display}</span>
  </nav>

  <header class="lov-hero">
    <h1>{lov_display} — <em>forklart</em></h1>
    <p>Angrerettloven beskytter deg når du handler på nett, telefon eller utenfor en vanlig butikk. Her er paragrafene forklart en etter en, på vanlig norsk.</p>
  </header>

  <div class="paragraph-list">
    {items_html}
  </div>
</div>

{contact_form(depth=2)}
{site_footer(depth=2)}"""

def render_lover_index():
    """Overview page listing all laws — editorial catalog design."""
    depth = 1
    prefix = "../" * depth

    # Lov-metadata
    LOV_INFO = {
        "angrerettloven": {"kat": "forbruk", "kat_label": "Forbruk og kjøp", "desc": "Angrerett ved netthandel og kjøp utenfor butikk"},
        "kjopsloven": {"kat": "forbruk", "kat_label": "Forbruk og kjøp", "desc": "Kjøp og salg mellom privatpersoner og bedrifter"},
        "forbrukerkjopsloven": {"kat": "forbruk", "kat_label": "Forbruk og kjøp", "desc": "Forbrukerkjøp fra næringsdrivende"},
        "husleieloven": {"kat": "bolig", "kat_label": "Bolig og leie", "desc": "Leie av bolig og lokale — rettigheter og plikter"},
        "avhendingslova": {"kat": "bolig", "kat_label": "Bolig og leie", "desc": "Kjøp og salg av bolig, hytte og tomt"},
        "naboloven": {"kat": "bolig", "kat_label": "Bolig og leie", "desc": "Naboforhold og urimelige ulemper"},
        "haandverkertjenesteloven": {"kat": "tjenester", "kat_label": "Tjenester", "desc": "Håndverkertjenester og reklamasjon"},
        "arbeidsmiljoloven": {"kat": "arbeid", "kat_label": "Arbeid og lønn", "desc": "Arbeidsforhold, lønn og oppsigelse"},
        "ferieloven": {"kat": "arbeid", "kat_label": "Arbeid og lønn", "desc": "Ferierettigheter og feriepenger"},
        "inkassoloven": {"kat": "gjeld", "kat_label": "Gjeld og penger", "desc": "Inkasso og inndriving av krav"},
        "ekteskapsloven": {"kat": "familie", "kat_label": "Familie", "desc": "Ekteskap, skilsmisse og felles eiendom"},
        "sameieloven": {"kat": "familie", "kat_label": "Familie", "desc": "Sameie og felles eierskap"},
        "husstandsfellesskapsloven": {"kat": "familie", "kat_label": "Familie", "desc": "Samboerskap og felles husstand"},
    }

    # Grupper lover etter kategori
    by_lov_count = {}
    by_lov_display = {}
    for p in PARAGRAPHS:
        lov = p["lov"]
        by_lov_count[lov] = by_lov_count.get(lov, 0) + 1
        by_lov_display[lov] = p["lov_display"]

    # Gruppér etter kategori
    by_kat = {}
    for lov, antall in by_lov_count.items():
        info = LOV_INFO.get(lov, {"kat": "annet", "kat_label": "Annet", "desc": ""})
        by_kat.setdefault(info["kat"], []).append({
            "lov": lov,
            "display": by_lov_display[lov],
            "antall": antall,
            "desc": info["desc"],
            "kat_label": info["kat_label"],
        })

    # Sorter lover i hver kategori alfabetisk etter visningsnavn
    for kat in by_kat:
        by_kat[kat].sort(key=lambda x: x["display"].lower())

    kat_meta = {
        "bolig": {"display": "Bolig og leie", "klasse": "kat-bolig"},
        "forbruk": {"display": "Forbruk og kjøp", "klasse": "kat-forbruk"},
        "arbeid": {"display": "Arbeid og lønn", "klasse": "kat-arbeid"},
        "familie": {"display": "Familie og samliv", "klasse": "kat-familie"},
        "gjeld": {"display": "Gjeld og penger", "klasse": "kat-gjeld"},
        "tjenester": {"display": "Tjenester", "klasse": "kat-tjenester"},
        "annet": {"display": "Annet", "klasse": ""},
    }

    sections = []
    for kat in ["bolig", "forbruk", "arbeid", "familie", "tjenester", "gjeld", "annet"]:
        if kat not in by_kat:
            continue
        meta = kat_meta[kat]
        total_p = sum(l["antall"] for l in by_kat[kat])
        cards = []
        for l in by_kat[kat]:
            cards.append(f"""
    <a href="{prefix}lover/{l['lov']}/" class="lov-kort">
      <div class="lov-meta">
        <div class="lov-num">{l['antall']}</div>
        <div class="lov-num-lbl">paragrafer</div>
      </div>
      <div class="lov-info">
        <h3>{l['display']}</h3>
        <p>{l['desc']}</p>
      </div>
      <div class="lov-arrow">→</div>
    </a>""")
        sections.append(f"""
<section class="lover-section">
  <div class="lover-section-head">
    <h2>{meta['display']}</h2>
    <span class="ant">{total_p} paragrafer · {len(by_kat[kat])} {'lov' if len(by_kat[kat]) == 1 else 'lover'}</span>
  </div>
  <div class="lov-grid">{chr(10).join(cards)}
  </div>
</section>""")

    total_lover = len(by_lov_count)
    total_paragrafer = len(PARAGRAPHS)

    return f"""{shared_head('Alle lover — Rettsregel', 'Bla i alle norske lover forklart på vanlig språk. Bolig, forbruk, arbeid, familie og mer.', depth=1, canonical_path='/lover/')}
{site_nav(depth=1)}

<main class="page">
  <header class="lover-hero">
    <span class="kicker">Lovsamling</span>
    <h1>Alle lover</h1>
    <p class="lead">Vi tar paragraf for paragraf av norsk lov og oversetter til vanlig norsk. Her er lovene vi har dekket.</p>
    <div class="lover-stats">
      <div class="lover-stat">
        <span class="num">{total_paragrafer}</span>
        <span class="lbl">Paragrafer</span>
      </div>
      <div class="lover-stat">
        <span class="num">{total_lover}</span>
        <span class="lbl">Lover</span>
      </div>
    </div>
  </header>

  {chr(10).join(sections)}
</main>

{contact_form(depth=1)}
{site_footer(depth=1)}"""

# ============================================================
# BUILD
# ============================================================

def render_personvern():
    """Privacy policy page."""
    today = "11. mai 2026"
    depth = 1
    prefix = "../" * depth
    return f"""{shared_head('Personvernerklæring | Rettsregel', 'Slik behandler vi opplysninger du sender inn på Rettsregel.', depth=1, canonical_path='/personvern/')}
{site_nav(depth=1)}

<div class="container">
  <nav class="breadcrumbs" aria-label="Brødsmuler">
    <a href="{prefix}">Hjem</a>
    <span class="sep">/</span>
    <span class="current">Personvern</span>
  </nav>
</div>

<div class="narrow">
  <header class="article-header">
    <div class="article-eyebrow">Personvernerklæring</div>
    <h1 class="article-title">Slik <span class="paragraf-num">behandler</span> vi opplysningene dine</h1>
    <p class="article-description">Kort og forståelig. Ingen advokatsmurfetekst.</p>
  </header>

  <article class="article-body">
    <h2>Hvem står bak Rettsregel?</h2>
    <p>Rettsregel drives av <strong>Walrus AS</strong> (org.nr [ORG.NR — fyll inn]). Vi er behandlingsansvarlig for personopplysninger du sender inn på siden.</p>
    <p>Du når oss på <a href="mailto:rettsregel@gmail.com">rettsregel@gmail.com</a>.</p>

    <h2>Hvilke opplysninger samler vi inn?</h2>
    <p>Når du sender inn skjemaet på siden, lagrer vi:</p>
    <ul>
      <li>Navn (hvis du oppgir det)</li>
      <li>E-postadresse</li>
      <li>Telefonnummer</li>
      <li>Beskrivelsen du skriver av saken din</li>
    </ul>
    <p>Vi samler ikke inn andre data, og vi bruker ingen sporings-cookies eller analyseverktøy som identifiserer deg.</p>

    <h2>Hvorfor lagrer vi opplysningene?</h2>
    <p>Vi bruker informasjonen til å svare på henvendelsen din. Behandlingsgrunnlaget vårt er <em>samtykke</em> — du fyller frivillig ut skjemaet for å få hjelp — og <em>legitim interesse</em> i å besvare deg.</p>

    <h2>Hvor lagres opplysningene?</h2>
    <p>Skjemainnsendinger går via Formspree (en amerikansk leverandør) til vår e-postkasse rettsregel@gmail.com. Vi jobber med å flytte til en europeisk løsning når volumet vokser.</p>
    <p>Vi sletter henvendelser fra e-postkassen etter <strong>90 dager</strong>, med mindre vi har gått inn i et oppdrag med deg. Da følger vi reglene som gjelder for det oppdraget.</p>

    <h2>Deler vi opplysninger med andre?</h2>
    <p>Nei. Vi selger ikke data, og vi deler ikke informasjon med tredjeparter — bortsett fra de tekniske leverandørene vi må bruke for at siden skal virke (Formspree for skjemaer, Google for Gmail). Vi peker deg <em>aldri</em> videre til en advokat eller annen rådgiver uten at du har bedt om det.</p>

    <h2>Hvilke rettigheter har du?</h2>
    <p>Du har rett til:</p>
    <ul>
      <li><strong>Innsyn</strong> — du kan be om å få vite hva vi har lagret om deg</li>
      <li><strong>Retting</strong> — du kan be oss korrigere feil informasjon</li>
      <li><strong>Sletting</strong> — du kan be oss slette opplysningene dine</li>
      <li><strong>Klage</strong> — du kan klage til <a href="https://www.datatilsynet.no" target="_blank" rel="noopener">Datatilsynet</a> hvis du mener vi behandler data feil</li>
    </ul>
    <p>Send oss en e-post til rettsregel@gmail.com hvis du vil bruke noen av disse rettighetene. Vi svarer innen 30 dager.</p>

    <h2>Endringer i denne erklæringen</h2>
    <p>Hvis vi endrer hvordan vi behandler personopplysninger, oppdaterer vi denne siden. Sist oppdatert: {today}.</p>
  </article>
</div>

{site_footer(depth=1)}"""


def render_om():
    n_paragrafer = len(PARAGRAPHS)
    n_sporsmal = len(SPORSMAL)
    n_lover = len(set(p["lov"] for p in PARAGRAPHS))
    return f"""{shared_head(
        'Om Rettsregel — Norske lover på vanlig norsk',
        'Rettsregel forklarer norske lover paragraf for paragraf, på vanlig norsk. Les om prosjektet og filosofien bak.',
        depth=1, canonical_path='/om/'
    )}
{site_nav(depth=1)}

<style>
.om-hero {{
  padding: 72px 0 56px;
  max-width: 820px;
}}
.om-hero .eyebrow {{
  font-size: 13px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.14em; color: var(--accent); margin-bottom: 24px;
}}
.om-hero h1 {{
  font-family: var(--serif); font-weight: 400;
  font-size: clamp(36px, 5vw, 58px);
  line-height: 1.08; letter-spacing: -0.02em; margin-bottom: 28px;
  font-variation-settings: "opsz" 48;
}}
.om-hero h1 em {{ font-style: italic; color: var(--accent); }}
.om-hero .ingress {{
  font-size: 19px; color: var(--ink-soft); line-height: 1.6;
  max-width: 660px;
}}
.om-stats {{
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: 2px; background: var(--line); border-radius: 16px;
  overflow: hidden; margin: 56px 0; border: 1px solid var(--line);
}}
@media (max-width: 600px) {{ .om-stats {{ grid-template-columns: 1fr; }} }}
.om-stat {{
  background: var(--bg-card); padding: 28px 32px;
}}
.om-stat-tall {{
  font-family: var(--serif); font-size: 48px; font-weight: 400;
  color: var(--accent); line-height: 1; margin-bottom: 8px;
  font-variation-settings: "opsz" 48;
}}
.om-stat-label {{ font-size: 14px; color: var(--ink-soft); line-height: 1.4; }}
.om-seksjoner {{
  display: grid; grid-template-columns: 1fr 1fr; gap: 32px;
  margin: 56px 0;
}}
@media (max-width: 680px) {{ .om-seksjoner {{ grid-template-columns: 1fr; }} }}
.om-seksjon {{
  padding: 36px; background: var(--bg-card); border: 1px solid var(--line);
  border-radius: 20px; box-shadow: var(--shadow-sm);
}}
.om-seksjon h2 {{
  font-family: var(--serif); font-size: 22px; font-weight: 400;
  margin-bottom: 14px; line-height: 1.2;
}}
.om-seksjon p {{ font-size: 15px; color: var(--ink-soft); line-height: 1.65; }}
.om-how {{
  margin: 64px 0; max-width: 700px;
}}
.om-how h2 {{
  font-family: var(--serif); font-size: 28px; font-weight: 400;
  margin-bottom: 32px; line-height: 1.2;
}}
.om-trinn {{ display: flex; flex-direction: column; gap: 0; }}
.om-trinn-item {{
  display: flex; gap: 24px; padding: 24px 0;
  border-bottom: 1px solid var(--line);
}}
.om-trinn-item:last-child {{ border-bottom: none; }}
.om-trinn-nr {{
  width: 36px; height: 36px; min-width: 36px;
  background: var(--accent); color: white;
  border-radius: 50%; display: flex; align-items: center;
  justify-content: center; font-family: var(--serif);
  font-size: 18px; font-weight: 400; margin-top: 2px;
}}
.om-trinn-tekst h3 {{ font-size: 16px; font-weight: 600; margin-bottom: 6px; }}
.om-trinn-tekst p {{ font-size: 14px; color: var(--ink-soft); line-height: 1.55; margin: 0; }}
.om-takk {{
  background: var(--bg-alt); border-radius: 20px;
  padding: 48px; margin: 56px 0 80px; text-align: center;
}}
.om-takk h2 {{
  font-family: var(--serif); font-size: 28px; font-weight: 400;
  margin-bottom: 16px;
}}
.om-takk p {{ font-size: 16px; color: var(--ink-soft); line-height: 1.6; max-width: 560px; margin: 0 auto 28px; }}
.om-takk a {{
  display: inline-flex; align-items: center; gap: 8px;
  background: var(--accent); color: white; text-decoration: none;
  font-weight: 600; font-size: 15px; padding: 14px 28px;
  border-radius: 12px; transition: background 0.2s;
}}
.om-takk a:hover {{ background: var(--accent-deep); }}
</style>

<main class="page">
  <div class="container">
    <div class="om-hero">
      <div class="eyebrow">Om Rettsregel</div>
      <h1>Lover er ikke vanskelige.<br><em>De er dårlig forklart.</em></h1>
      <p class="ingress">Rettsregel oversetter norske lover til vanlig norsk — paragraf for paragraf, med eksempler du kjenner deg igjen i. Uten juristsvada. Uten ansvarsfraskrivelser.</p>
    </div>

    <div class="om-stats">
      <div class="om-stat">
        <div class="om-stat-tall">{n_paragrafer}</div>
        <div class="om-stat-label">Paragrafer forklart<br>på vanlig norsk</div>
      </div>
      <div class="om-stat">
        <div class="om-stat-tall">{n_sporsmal}</div>
        <div class="om-stat-label">Spørsmål og svar<br>om rettigheter</div>
      </div>
      <div class="om-stat">
        <div class="om-stat-tall">{n_lover}</div>
        <div class="om-stat-label">Lover dekket<br>og voksende</div>
      </div>
    </div>

    <div class="om-seksjoner">
      <div class="om-seksjon">
        <h2>Problemet</h2>
        <p>Loven gjelder alle. Men den er skrevet av jurister, for jurister. Hverdagsmenneskene som trenger å forstå sine rettigheter — leietakeren, bilkjøperen, den som er sagt opp — sitter igjen uten et brukbart svar.</p>
        <p style="margin-top:14px">Det er ikke mangel på lover. Det er mangel på forklaring.</p>
      </div>
      <div class="om-seksjon">
        <h2>Løsningen</h2>
        <p>Vi tar én paragraf om gangen. Oversetter den til vanlig norsk. Legger til eksempler fra hverdagen. Viser hva folk gjør feil — og hva du faktisk skal gjøre.</p>
        <p style="margin-top:14px">Enkelt. Gratis. Uten agenda annet enn at du skal forstå.</p>
      </div>
      <div class="om-seksjon">
        <h2>Hvem er vi?</h2>
        <p>Rettsregel er drevet av Wombat AS. Innholdet er utarbeidet av jurister med juridisk fagkompetanse, og kvalitetssikret mot gjeldende lover og forarbeider.</p>
        <p style="margin-top:14px">Vi er ikke et advokatfirma og vi er ikke et lovkongres. Vi er en redaksjon som oversetter.</p>
      </div>
      <div class="om-seksjon">
        <h2>Filosofien</h2>
        <p>«Lover er ikke vanskelige. De er bare dårlig forklart» er ikke bare et slagord. Det er en hypotese vi tester daglig.</p>
        <p style="margin-top:14px">Viser det seg at en 67-åring på Dønna kan forstå husleielovens § 9-6 etter å ha lest siden vår — da har vi lykkes.</p>
      </div>
    </div>

    <div class="om-how">
      <h2>Slik fungerer Rettsregel</h2>
      <div class="om-trinn">
        <div class="om-trinn-item">
          <div class="om-trinn-nr">1</div>
          <div class="om-trinn-tekst">
            <h3>Du søker opp loven eller spørsmålet ditt</h3>
            <p>Alle paragrafer er søkbare. Søk direkte på loven, paragrafnummeret, eller still et naturlig spørsmål som «kan jeg trekke meg fra boligkjøpet».</p>
          </div>
        </div>
        <div class="om-trinn-item">
          <div class="om-trinn-nr">2</div>
          <div class="om-trinn-tekst">
            <h3>Du leser forklaringen</h3>
            <p>Hver paragraf er forklart med «Kort svar» øverst, deretter hva det betyr på vanlig norsk, eksempler og vanlige feil. Kildedokumentet er alltid lenket.</p>
          </div>
        </div>
        <div class="om-trinn-item">
          <div class="om-trinn-nr">3</div>
          <div class="om-trinn-tekst">
            <h3>Du bruker verktøyene</h3>
            <p>Under Tjenester finner du kalkulatorer, veivisere og brev-generatorer — alt gratis. Trenger du noe skriftlig og signert, tar vi det for 990 kr.</p>
          </div>
        </div>
        <div class="om-trinn-item">
          <div class="om-trinn-nr">4</div>
          <div class="om-trinn-tekst">
            <h3>Du sender inn saken hvis du trenger mer</h3>
            <p>Kontaktskjemaet på hver paragrafside sender deg rett til oss. Vi leser alle henvendelser og svarer — eller peker deg til noen som kan hjelpe videre.</p>
          </div>
        </div>
      </div>
    </div>

    <div class="om-takk">
      <h2>Har du en sak du lurer på?</h2>
      <p>Skriv til oss. Vi leser alle henvendelser. Hvis vi ikke kan hjelpe direkte, peker vi deg til noen som kan.</p>
      <a href="../#skjema">Send inn saken din →</a>
    </div>
  </div>
</main>
{site_footer(depth=1)}"""



def paragraph_exists(lov, nummer):
    """Sjekker om en paragraf finnes i PARAGRAPHS-listen."""
    return any(p["lov"] == lov and p["number"] == nummer for p in PARAGRAPHS)


def render_sporsmal_page(s):
    """Render en enkelt spørsmål-artikkel."""
    import markdown as md

    # Mapping fra URL-slug til ordentlig norsk visningsnavn
    LOV_DISPLAY = {
        "angrerettloven": "Angrerettloven",
        "kjopsloven": "Kjøpsloven",
        "husleieloven": "Husleieloven",
        "naboloven": "Naboloven",
        "haandverkertjenesteloven": "Håndverkertjenesteloven",
        "forbrukerkjopsloven": "Forbrukerkjøpsloven",
        "plan-og-bygningsloven": "Plan- og bygningsloven",
        "husstandsfellesskapsloven": "Husstandsfellesskapsloven",
        "sameieloven": "Sameieloven",
        "arbeidsmiljoloven": "Arbeidsmiljøloven",
        "ferieloven": "Ferieloven",
        "inkassoloven": "Inkassoloven",
    }

    body_html = md.markdown(s["body_md"], extensions=["extra"])

    # Bygg "Relevante paragrafer"-seksjon — sjekk om hver finnes
    related_items = []
    for rel in s.get("related_paragrafer", []):
        lov = rel["lov"]
        nr = rel["nummer"]
        beskr = rel.get("beskrivelse", "")
        display_name = LOV_DISPLAY.get(lov, lov.capitalize())
        if paragraph_exists(lov, nr):
            related_items.append(
                f'<li><span class="ref"><a href="/lover/{lov}/{nr}/">{display_name} § {nr}</a></span><span class="desc">{beskr}</span></li>'
            )
        else:
            related_items.append(
                f'<li class="pending"><span class="ref">{display_name} § {nr}</span><span class="desc">{beskr}</span></li>'
            )

    related_html = ""
    if related_items:
        related_html = f"""
<section class="sp-related">
  <div class="label">Les videre</div>
  <h3>Relevante paragrafer</h3>
  <ul>
    {chr(10).join(related_items)}
  </ul>
</section>"""

    # Kategori-tag basert på kategorien
    kategori = s.get("kategori", "")
    KAT_LABEL = {
        "bolig": "BOLIG OG LEIE",
        "forbruk": "FORBRUK OG KJØP",
        "arbeid": "ARBEID OG LØNN",
        "familie": "FAMILIE OG SAMLIV",
        "gjeld": "GJELD OG PENGER",
        "tjenester": "TJENESTER",
    }
    kat_label = KAT_LABEL.get(kategori, kategori.upper())

    head = shared_head(s["title"], s.get("description", ""), depth=2)

    return f"""<!DOCTYPE html>
<html lang="nb">
{head}
<body>
{site_nav(depth=2)}
<main class="page kat-{kategori}">
  <article class="sp-hero">
    <div class="kicker">{kat_label}</div>
    <div class="breadcrumb"><a href="../">Vanlige spørsmål</a></div>
    <h1>{s['title']}</h1>
  </article>

  <div class="sp-tldr">
    <p>{s['kort_svar']}</p>
  </div>

  <article class="sp-body">
    {body_html}
  </article>

  {related_html}

{contact_form(depth=2)}

</main>
{site_footer(depth=2)}
</body>
</html>"""


def render_sporsmal_hub():
    """Render hub-side på /sporsmal/index.html — liste over alle spørsmål."""
    # Grupper etter kategori
    by_kat = {}
    for s in SPORSMAL:
        by_kat.setdefault(s.get("kategori", "annet"), []).append(s)

    kat_meta = {
        "bolig": {"display": "Bolig og leie", "label": "BOLIG", "klasse": "kat-bolig"},
        "forbruk": {"display": "Forbruk og kjøp", "label": "FORBRUK", "klasse": "kat-forbruk"},
        "arbeid": {"display": "Arbeid og lønn", "label": "ARBEID", "klasse": "kat-arbeid"},
        "familie": {"display": "Familie og samliv", "label": "FAMILIE", "klasse": "kat-familie"},
        "gjeld": {"display": "Gjeld og penger", "label": "GJELD", "klasse": "kat-gjeld"},
        "tjenester": {"display": "Tjenester og håndverk", "label": "TJENESTER", "klasse": "kat-tjenester"},
        "annet": {"display": "Annet", "label": "ANNET", "klasse": ""},
    }

    sections = []
    for kat in ["bolig", "forbruk", "arbeid", "familie", "gjeld", "tjenester", "annet"]:
        if kat not in by_kat:
            continue
        items = by_kat[kat]
        meta = kat_meta.get(kat, kat_meta["annet"])
        antall = len(items)
        antall_tekst = f"{antall} spørsmål" if antall != 1 else "1 spørsmål"

        # Første kort er featured, resten er vanlige
        cards_html = []
        for i, s in enumerate(items):
            featured_class = " featured" if i == 0 and len(items) > 2 else ""
            cards_html.append(f"""
    <a href="/sporsmal/{s['slug']}/" class="sphub-card {meta['klasse']}{featured_class}">
      <div class="kat-tag">{meta['label']}</div>
      <h3>{s['title']}</h3>
      <p>{s.get('description', '')}</p>
      <span class="read-more">Les svaret</span>
    </a>""")

        sections.append(f"""
<section class="sphub-section {meta['klasse']}">
  <div class="sphub-section-head">
    <span class="sphub-section-kat">{meta['label']}</span>
    <h2>{meta['display']}</h2>
    <span class="sphub-section-count">{antall_tekst}</span>
  </div>
  <div class="sphub-grid">
    {chr(10).join(cards_html)}
  </div>
</section>""")

    total = len(SPORSMAL)
    head = shared_head(
        "Vanlige spørsmål — Rettsregel",
        "Konkrete svar på de vanligste juridiske spørsmålene nordmenn har: depositum, bilkjøp, naboer, arbeid, gjeld.",
        depth=1,
    )

    return f"""<!DOCTYPE html>
<html lang="nb">
{head}
<body>
{site_nav(depth=1)}
<main class="page">
  <header class="sphub-hero">
    <span class="kicker">Spørsmål og svar</span>
    <h1>Vanlige spørsmål</h1>
    <p class="lead">Konkrete svar på problemene folk møter. Skrevet på vanlig norsk, med stegene du kan ta.</p>
    <div class="sphub-meta"><strong>{total}</strong> spørsmål · oppdatert regelmessig</div>
  </header>

  {chr(10).join(sections)}

</main>
{site_footer(depth=1)}
</body>
</html>"""


def render_homepage():
    """Forsiden."""
    depth = 0
    prefix = ""
    # Featured paragrafer — håndplukket etter nytteverdi på tvers av lover
    featured = [
        ("angrerettloven", "16", "forbruk", "FORBRUK · ANGRERETT", "Den viktigste knappen på nett", "Når du kan angre — og når du ikke kan."),
        ("kjopsloven", "32", "forbruk", "PRIVATKJØP · REKLAMASJON", "Reklamasjonsfristene", "To år, fem år, eller noe annet? Her er hva som gjelder."),
        ("kjopsloven", "19", "forbruk", "PRIVATKJØP · FINN.NO", "Solgt «som den er» — hva betyr det?", "Selger slipper ikke alt ansvar — uansett hva kontrakten sier."),
        ("kjopsloven", "39", "forbruk", "PRIVATKJØP · HEVING", "Heving ved mangel", "Når kan du gå fra hele kjøpet — og få pengene tilbake?"),
        ("angrerettloven", "20", "forbruk", "FORBRUK · ANGRERETT", "Slik bruker du angreretten", "Korte steg: meld fra, returner, få pengene tilbake."),
        ("kjopsloven", "17", "forbruk", "PRIVATKJØP · MANGEL", "Når har varen en mangel?", "Forskjellen mellom slitasje og reell feil."),
    ]
    cards_html = ""
    for lov, paragraf, kat, kategori, tittel, beskr in featured:
        cards_html += f"""
    <a href="{prefix}lover/{lov}/{paragraf}/" class="sphub-card kat-{kat}">
      <div class="kat-tag">§ {paragraf} · {kategori}</div>
      <h3>{tittel}</h3>
      <p>{beskr}</p>
      <span class="read-more">Les paragrafen</span>
    </a>"""

    # Spørsmål-artikler — vis opptil 6 på hjemmesiden
    KAT_LABEL = {
        "bolig": "BOLIG",
        "forbruk": "FORBRUK",
        "arbeid": "ARBEID",
        "familie": "FAMILIE",
        "gjeld": "GJELD",
    }
    sporsmal_cards = ""
    for s in SPORSMAL[:6]:
        kat = s.get("kategori", "")
        kat_label = KAT_LABEL.get(kat, kat.upper())
        sporsmal_cards += f"""
    <a href="{prefix}sporsmal/{s['slug']}/" class="sphub-card kat-{kat}">
      <div class="kat-tag">SPØRSMÅL · {kat_label}</div>
      <h3>{s['title']}</h3>
      <p>{s.get('description', '')}</p>
      <span class="read-more">Les svaret</span>
    </a>"""

    # Lov-oversikt — dynamisk basert på antall paragrafer per lov
    LOV_KATEGORI = {
        "angrerettloven": ("forbruk", "Forbruk og kjøp"),
        "kjopsloven": ("forbruk", "Forbruk og kjøp"),
        "forbrukerkjopsloven": ("forbruk", "Forbruk og kjøp"),
        "husleieloven": ("bolig", "Bolig og leie"),
        "avhendingslova": ("bolig", "Bolig og leie"),
        "naboloven": ("bolig", "Bolig og leie"),
        "haandverkertjenesteloven": ("tjenester", "Tjenester"),
        "arbeidsmiljoloven": ("arbeid", "Arbeid og lønn"),
        "ferieloven": ("arbeid", "Arbeid og lønn"),
        "inkassoloven": ("gjeld", "Gjeld og penger"),
        "ekteskapsloven": ("familie", "Familie"),
        "sameieloven": ("familie", "Familie"),
        "husstandsfellesskapsloven": ("familie", "Familie"),
    }
    LOV_DESC_HOME = {
        "angrerettloven": "Angrerett ved netthandel og kjøp utenfor butikk",
        "kjopsloven": "Kjøp og salg mellom privatpersoner og bedrifter",
        "husleieloven": "Leie av bolig — rettigheter og plikter",
        "avhendingslova": "Kjøp og salg av bolig, hytte og tomt",
    }
    by_lov_count = {}
    by_lov_display = {}
    for p in PARAGRAPHS:
        lov = p["lov"]
        by_lov_count[lov] = by_lov_count.get(lov, 0) + 1
        by_lov_display[lov] = p["lov_display"]
    sorted_lover = sorted(by_lov_count.items(), key=lambda x: -x[1])
    lov_cards = ""
    for lov, antall in sorted_lover:
        kat, kat_lbl = LOV_KATEGORI.get(lov, ("", ""))
        desc = LOV_DESC_HOME.get(lov, kat_lbl)
        lov_cards += f"""
      <a href="{prefix}lover/{lov}/" class="lov-kort">
        <div class="lov-meta">
          <div class="lov-num">{antall}</div>
          <div class="lov-num-lbl">paragrafer</div>
        </div>
        <div class="lov-info">
          <h3>{by_lov_display[lov]}</h3>
          <p>{desc}</p>
        </div>
        <div class="lov-arrow">→</div>
      </a>"""

    return f"""{shared_head('Rettsregel — Norske lover på vanlig norsk', 'Lover er ikke vanskelige. De er bare dårlig forklart. Bla i norske lover, paragraf for paragraf.', depth=0, canonical_path='/')}
{site_nav(depth=0)}

<main class="page">
  <header class="home-hero-v2">
    <span class="kicker">Norske lover · på vanlig norsk</span>
    <h1>Lover er ikke vanskelige.<br>De er bare <em>dårlig forklart</em>.</h1>
    <p class="lead">Søk i alle paragrafer og finn svar på det du lurer på.</p>

    <div class="search-wrapper">
      <div class="search-input-wrap">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
        </svg>
        <input type="text" class="search-input" id="rrSearch" placeholder="Søk i paragrafer og spørsmål…" autocomplete="off">
      </div>
      <div class="search-tags">
        <a class="search-tag" data-q="depositum">depositum</a>
        <a class="search-tag" data-q="angrerett">angrerett</a>
        <a class="search-tag" data-q="mangel">mangel</a>
        <a class="search-tag" data-q="oppsigelse">oppsigelse</a>
        <a class="search-tag" data-q="naboer">naboer</a>
      </div>
      <div class="search-results" id="rrSearchResults"></div>
    </div>
  </header>

  <div class="home-stats">
    <div class="home-stat">
      <div class="num">{len(PARAGRAPHS)}</div>
      <div class="lbl">Paragrafer</div>
    </div>
    <div class="home-stat">
      <div class="num">{len(by_lov_count)}</div>
      <div class="lbl">Lover</div>
    </div>
    <div class="home-stat">
      <div class="num">{len(SPORSMAL)}</div>
      <div class="lbl">Spørsmål</div>
    </div>
  </div>

  <section class="home-section-v2">
    <div class="home-section-head-v2">
      <div class="left">
        <h2>Vanlige spørsmål</h2>
      </div>
      <div class="right">
        <a href="{prefix}sporsmal/">Se alle →</a>
      </div>
    </div>
    <div class="sphub-grid">{sporsmal_cards}
    </div>
  </section>

  <section class="home-section-v2">
    <div class="home-section-head-v2">
      <div class="left">
        <h2>Utvalgte paragrafer</h2>
      </div>
    </div>
    <div class="sphub-grid">{cards_html}
    </div>
  </section>

  <section class="home-section-v2">
    <div class="home-section-head-v2">
      <div class="left">
        <h2>Alle lover</h2>
      </div>
      <div class="right">
        <a href="{prefix}lover/">Se alle →</a>
      </div>
    </div>
    <div class="lov-grid">{lov_cards}
    </div>
  </section>
</main>

{contact_form(depth=0)}

<script>
(function() {{
  const input = document.getElementById('rrSearch');
  const results = document.getElementById('rrSearchResults');
  const tags = document.querySelectorAll('.search-tag');
  let index = null;

  // Last index én gang
  fetch('paragraphs-index.json').then(r => r.json()).then(data => {{ index = data; }});

  function score(item, q) {{
    const Q = q.toLowerCase();
    const title = (item.title || '').toLowerCase();
    const lov = (item.lov_display || '').toLowerCase();
    const number = (item.number || '').toLowerCase();
    const ks = (item.kort_svar || '').toLowerCase();
    const desc = (item.description || '').toLowerCase();
    let s = 0;
    if (title.startsWith(Q)) s += 100;
    else if (title.includes(Q)) s += 60;
    if (lov.includes(Q)) s += 20;
    if (number === Q) s += 200;
    if (number.startsWith(Q)) s += 50;
    if (ks.includes(Q)) s += 10;
    if (desc.includes(Q)) s += 8;
    return s;
  }}

  function render(q) {{
    if (!index || !q || q.length < 2) {{
      results.classList.remove('visible');
      results.innerHTML = '';
      return;
    }}
    const matches = index
      .map(i => ({{...i, _s: score(i, q)}}))
      .filter(i => i._s > 0)
      .sort((a,b) => b._s - a._s)
      .slice(0, 8);
    if (matches.length === 0) {{
      results.innerHTML = '<div class="search-empty">Ingen treff for "' + q + '"</div>';
      results.classList.add('visible');
      return;
    }}
    results.innerHTML = matches.map(m => {{
      if (m.type === 'sporsmal') {{
        return '<a class="search-result" href="sporsmal/' + m.slug + '/">' +
          '<div class="sr-title">' + m.title + '</div>' +
          '<div class="sr-meta"><strong>Spørsmål</strong></div>' +
        '</a>';
      }} else {{
        return '<a class="search-result" href="lover/' + m.lov + '/' + m.number + '/">' +
          '<div class="sr-title">' + m.title + '</div>' +
          '<div class="sr-meta"><strong>' + m.lov_display + ' § ' + m.number + '</strong></div>' +
        '</a>';
      }}
    }}).join('');
    results.classList.add('visible');
  }}

  input.addEventListener('input', e => render(e.target.value.trim()));
  input.addEventListener('focus', e => {{ if (e.target.value.trim()) render(e.target.value.trim()); }});
  document.addEventListener('click', e => {{
    if (!e.target.closest('.search-wrapper')) {{
      results.classList.remove('visible');
    }}
  }});
  tags.forEach(tag => {{
    tag.addEventListener('click', e => {{
      e.preventDefault();
      const q = tag.dataset.q;
      input.value = q;
      input.focus();
      render(q);
    }});
  }});
}})();
</script>

{site_footer(depth=0)}"""


def paragraf_sort_key(p):
    """Sort key that handles paragrafs like '1', '6-50', '9a', '14b-2'."""
    num = p["number"]
    m = re.match(r'(\d+)(?:-(\d+))?([a-zA-Z]+)?', num)
    if m:
        main = int(m.group(1))
        sub = int(m.group(2)) if m.group(2) else 0
        letter = m.group(3) or ''
        return (main, sub, letter)
    return (0, 0, '')


def render_tjenester_hub():
    return f"""{shared_head(
        'Juridiske verktøy og tjenester | Rettsregel',
        'Gratis kalkulatorer og verktøy som hjelper deg å ta juridisk riktige valg. ENK eller AS, kontraktsvalg og mer.',
        depth=1, canonical_path='/tjenester/'
    )}
<body>
{site_nav(depth=1)}
<main class="page">
  <div class="container">
    <div class="tjenester-hero">
      <div class="article-eyebrow">Tjenester</div>
      <h1>Juridiske verktøy — gratis å bruke</h1>
      <p>Svar på spørsmålene, og få en klar anbefaling. Trenger du noe skriftlig og signert, hjelper vi med det også.</p>
    </div>

    <div class="tjensters-grid">
      <a href="../tjenester/enk-eller-as/" class="tjeneste-kort">
        <div class="tjeneste-kat">Gratis kalkulator</div>
        <h3>ENK eller AS?</h3>
        <p>Svar på fem spørsmål og finn ut hvilken selskapsform som passer for deg — med skatteillustrasjon og selskapsrettslig begrunnelse.</p>
        <div class="tjeneste-pil">Bruk verktøyet →</div>
      </a>

      <a href="../tjenester/reklamasjon-bil/" class="tjeneste-kort">
        <div class="tjeneste-kat">Gratis brevgenerator</div>
        <h3>Reklamasjon bilkjøp</h3>
        <p>Kjøpte du en bil med feil? Lag et juridisk korrekt reklamasjonsbrev på noen minutter, med fristberegning og lovhenvisninger.</p>
        <div class="tjeneste-pil">Lag brevet →</div>
      </a>

      <div class="tjeneste-kort snart">
        <span class="snart-badge">Snart</span>
        <div class="tjeneste-kat graa">Kalkulator</div>
        <h3>Formuesoppgjør samlivsbrudd</h3>
        <p>Beregn hva du og partneren din har krav på ved brudd. Basert på husstandsfellesskapsloven.</p>
        <div class="tjeneste-pil">Kommer snart</div>
      </div>

      <div class="tjeneste-kort snart">
        <span class="snart-badge">Snart</span>
        <div class="tjeneste-kat graa">Kalkulator</div>
        <h3>Reklamasjon forbrukerkjøp</h3>
        <p>Reklamasjonsveiviser for alt fra hvitevarer til mobiltelefoner. Forbrukerkjøpsloven.</p>
        <div class="tjeneste-pil">Kommer snart</div>
      </div>
    </div>
  </div>
</main>
{site_footer(depth=1)}"""


def render_enk_eller_as():
    return f"""{shared_head(
        'ENK eller AS? Finn ut hva som passer for deg — Rettsregel',
        'Svar på fem spørsmål og få en grundig anbefaling om du bør velge ENK eller AS — med skatteillustrasjon og selskapsrettslig begrunnelse.',
        depth=2, canonical_path='/tjenester/enk-eller-as/'
    )}
<body>
{site_nav(depth=2)}

<style>
.enk-wizard {{ max-width: 780px; margin: 0 auto; }}
.enk-progress {{ margin-bottom: 32px; }}
.enk-pbar {{ height: 5px; background: var(--line); border-radius: 3px; overflow: hidden; margin-bottom: 8px; }}
.enk-pfill {{ height: 100%; background: var(--accent); border-radius: 3px; transition: width 0.35s ease; }}
.enk-ptekst {{ font-size: 13px; color: var(--ink-mute); font-weight: 500; }}
.enk-steg {{ animation: fadeInUp 0.22s ease; }}
.enk-kort {{
  background: var(--bg-card); border: 1px solid var(--line);
  border-radius: 20px; padding: 40px; box-shadow: var(--shadow-md); margin-bottom: 24px;
}}
@media (max-width: 600px) {{ .enk-kort {{ padding: 24px 20px; }} }}
.enk-stegnr {{ font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); margin-bottom: 10px; }}
.enk-q {{ font-family: var(--serif); font-size: 22px; font-weight: 400; line-height: 1.25; margin-bottom: 6px; }}
.enk-hint {{ font-size: 14px; color: var(--ink-mute); margin-bottom: 24px; line-height: 1.5; }}
.enk-input {{
  width: 100%; padding: 13px 16px; border: 1.5px solid var(--line);
  border-radius: 10px; font-family: var(--sans); font-size: 16px;
  background: var(--bg); color: var(--ink); box-sizing: border-box; transition: border-color 0.15s;
}}
.enk-input:focus {{ outline: none; border-color: var(--accent); }}
.ig {{ margin-bottom: 18px; }}
.ig label {{ display: block; font-size: 13px; font-weight: 600; color: var(--ink-soft); margin-bottom: 6px; }}
.vg {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }}
.vg3 {{ grid-template-columns: 1fr 1fr 1fr; }}
@media (max-width: 560px) {{ .vg, .vg3 {{ grid-template-columns: 1fr; }} }}
.vk {{
  border: 1.5px solid var(--line); border-radius: 12px; padding: 14px 16px;
  cursor: pointer; text-align: left; background: var(--bg); transition: all 0.15s;
  font-family: var(--sans); font-size: 14px; color: var(--ink); line-height: 1.35; min-height: 44px;
}}
.vk:hover {{ border-color: var(--accent-soft); background: rgba(177,74,42,0.03); }}
.vk.av {{ border-color: var(--accent); background: rgba(177,74,42,0.06); color: var(--accent); font-weight: 600; }}
.vk-ikon {{ font-size: 22px; display: block; margin-bottom: 6px; }}
.nav-kn {{ display: flex; gap: 10px; margin-top: 28px; }}
.kn-n {{
  flex: 1; background: var(--accent); color: white; border: none;
  border-radius: 12px; font-family: var(--sans); font-size: 16px;
  font-weight: 600; padding: 16px; cursor: pointer; transition: background 0.2s;
}}
.kn-n:hover {{ background: var(--accent-deep); }}
.kn-t {{
  background: transparent; color: var(--ink-soft); border: 1.5px solid var(--line);
  border-radius: 12px; font-family: var(--sans); font-size: 15px;
  font-weight: 500; padding: 14px 20px; cursor: pointer;
}}
.kn-t:hover {{ border-color: var(--ink-soft); }}
/* Resultat */
.res-badge {{
  display: inline-flex; align-items: center; gap: 6px;
  font-size: 12px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.12em; padding: 6px 14px; border-radius: 20px; margin-bottom: 20px;
}}
.res-badge.as {{ background: #e2edf4; color: #2d5970; }}
.res-badge.enk {{ background: #e8f4e8; color: #2d5a2d; }}
.res-badge.as-krav {{ background: #dce8f2; color: #1a4060; }}
.res-tittel {{ font-family: var(--serif); font-size: clamp(24px,3vw,34px); font-weight: 400; margin-bottom: 20px; line-height: 1.15; }}
.res-boks {{
  background: var(--bg-card); border: 1px solid var(--line);
  border-radius: 20px; padding: 40px; box-shadow: var(--shadow-md); margin-bottom: 24px;
}}
@media (max-width: 600px) {{ .res-boks {{ padding: 24px 20px; }} }}
.res-grunner {{ margin: 0 0 28px; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 10px; }}
.res-grunner li {{ display: flex; gap: 10px; font-size: 15px; line-height: 1.5; }}
.res-grunner li::before {{ content: '→'; color: var(--accent); font-weight: 700; flex-shrink: 0; }}
/* Skatt-illustrasjon */
.skatt-panel {{
  background: var(--bg-alt); border-radius: 14px; padding: 24px 28px; margin: 28px 0;
  border: 1px solid var(--line);
}}
.skatt-panel h4 {{ font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--ink-mute); margin-bottom: 16px; }}
.skatt-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
@media (max-width: 560px) {{ .skatt-grid {{ grid-template-columns: 1fr; }} }}
.skatt-kolonne {{ background: white; border-radius: 10px; padding: 16px; border: 1px solid var(--line); }}
.skatt-lov {{ font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--ink-mute); margin-bottom: 10px; }}
.skatt-rad {{ display: flex; justify-content: space-between; font-size: 13px; padding: 5px 0; border-bottom: 1px solid rgba(0,0,0,0.06); }}
.skatt-rad:last-child {{ border-bottom: none; }}
.skatt-rad.total {{ font-weight: 700; font-size: 14px; padding-top: 8px; margin-top: 4px; border-top: 2px solid var(--line); border-bottom: none; }}
.skatt-rad.igjen {{ color: var(--accent); font-weight: 700; font-size: 14px; }}
.skatt-disclaimer {{ font-size: 12px; color: var(--ink-mute); margin-top: 12px; line-height: 1.5; }}
/* Sammenligningstabel */
.res-tbl-wr {{ overflow-x: auto; margin: 28px 0; }}
.res-tbl {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
.res-tbl th {{
  padding: 10px 14px; text-align: left; font-size: 12px;
  font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em;
  background: var(--bg-alt); border-bottom: 2px solid var(--line);
}}
.res-tbl td {{ padding: 11px 14px; border-bottom: 1px solid var(--line); vertical-align: top; line-height: 1.4; }}
.res-tbl tr:last-child td {{ border-bottom: none; }}
.res-tbl td:first-child {{ color: var(--ink-mute); font-size: 12px; font-weight: 600; white-space: nowrap; }}
.anbefalt-kol th, .anbefalt-kol td {{ background: rgba(177,74,42,0.04); }}
.res-tbl th.anbefalt-hd {{ color: var(--accent); }}
/* CTA */
.enk-cta {{ background: var(--bg-alt); border-radius: 16px; padding: 32px; margin: 32px 0 56px; }}
.enk-cta h3 {{ font-family: var(--serif); font-size: 22px; font-weight: 400; margin-bottom: 12px; }}
.enk-cta p {{ font-size: 15px; color: var(--ink-soft); line-height: 1.5; margin-bottom: 16px; max-width: 540px; }}
.btn-aksjon {{
  display: inline-flex; align-items: center; gap: 8px;
  background: var(--accent); color: white; text-decoration: none;
  font-weight: 600; font-size: 15px; padding: 14px 24px;
  border-radius: 10px; transition: background 0.2s;
}}
.btn-aksjon:hover {{ background: var(--accent-deep); }}
.enk-cta-pris {{ font-size: 13px; color: var(--ink-mute); display: block; margin-top: 10px; }}
</style>

<main class="page">
  <div class="narrow">
    <div class="breadcrumbs">
      <a href="../../">Rettsregel</a>
      <span class="sep">›</span>
      <a href="../../tjenester/">Tjenester</a>
      <span class="sep">›</span>
      <span class="current">ENK eller AS?</span>
    </div>

    <div class="article-header">
      <div class="article-eyebrow">Gratis verktøy</div>
      <h1 class="article-title">Skal du velge ENK eller AS?</h1>
      <p class="article-description">Svar på fem spørsmål. Du får en selskapsrettslig anbefaling, begrunnelse, og en forenklet skatteillustrasjon med dine egne tall.</p>
    </div>

    <!-- WIZARD -->
    <div class="enk-wizard" id="wiz">
      <div class="enk-progress">
        <div class="enk-pbar"><div class="enk-pfill" id="pf" style="width:0%"></div></div>
        <span class="enk-ptekst" id="pt">Steg 1 av 5</span>
      </div>

      <!-- Steg 1: Eiere -->
      <div class="enk-steg" id="s1">
        <div class="enk-kort">
          <div class="enk-stegnr">Steg 1 av 5</div>
          <div class="enk-q">Er du alene som eier?</div>
          <div class="enk-hint">ENK kan bare ha én eier. Er dere to eller flere, er AS den eneste løsningen juridisk sett.</div>
          <div class="vg">
            <button class="vk" onclick="velg('eiere','en',this)"><span class="vk-ikon">👤</span><strong>Ja, bare meg</strong></button>
            <button class="vk" onclick="velg('eiere','flere',this)"><span class="vk-ikon">👥</span><strong>Nei, vi er flere</strong><br><span style="font-size:13px;color:var(--ink-mute)">Medeier eller partner</span></button>
          </div>
          <div class="nav-kn"><button class="kn-n" onclick="neste(1)">Neste →</button></div>
        </div>
      </div>

      <!-- Steg 2: Økonomi -->
      <div class="enk-steg" id="s2" style="display:none">
        <div class="enk-kort">
          <div class="enk-stegnr">Steg 2 av 5</div>
          <div class="enk-q">Hva forventer du å tjene — og hva vil du med pengene?</div>
          <div class="enk-hint">Skriv forventet overskudd det første året. Overskudd = inntekter minus kostnader.</div>
          <div class="ig">
            <label for="overskudd">Forventet overskudd år 1 (kr)</label>
            <input type="number" id="overskudd" class="enk-input" placeholder="f.eks. 400000" min="0" step="10000">
          </div>
          <div class="ig" style="margin-top:20px">
            <label>Hva vil du gjøre med overskuddet?</label>
            <div class="vg" style="margin-top:8px">
              <button class="vk" onclick="velg('kapital','ta_ut',this)">💸 Ta ut fortløpende — dette er inntekten min</button>
              <button class="vk" onclick="velg('kapital','beholde',this)">📈 La det stå og vokse i selskapet</button>
              <button class="vk" onclick="velg('kapital','blanding',this)">⚖️ Blanding — litt av begge</button>
              <button class="vk" onclick="velg('kapital','vet_ikke',this)">🤔 Vet ikke ennå</button>
            </div>
          </div>
          <div class="nav-kn">
            <button class="kn-t" onclick="visSteg(1)">← Tilbake</button>
            <button class="kn-n" onclick="neste(2)">Neste →</button>
          </div>
        </div>
      </div>

      <!-- Steg 3: Virksomhet og risiko -->
      <div class="enk-steg" id="s3" style="display:none">
        <div class="enk-kort">
          <div class="enk-stegnr">Steg 3 av 5</div>
          <div class="enk-q">Hva slags virksomhet driver du?</div>
          <div class="enk-hint">Risikoen for erstatningskrav varierer mye etter bransje.</div>
          <div class="vg vg3">
            <button class="vk" onclick="velg('bransje','konsulent',this)"><span class="vk-ikon">💻</span>Rådgivning / konsulent / IT</button>
            <button class="vk" onclick="velg('bransje','haandverk',this)"><span class="vk-ikon">🔨</span>Bygg, håndverk, transport</button>
            <button class="vk" onclick="velg('bransje','handel',this)"><span class="vk-ikon">🛍️</span>Handel, nettbutikk, import</button>
            <button class="vk" onclick="velg('bransje','helse',this)"><span class="vk-ikon">🏥</span>Helse, omsorg, terapi</button>
            <button class="vk" onclick="velg('bransje','kreativ',this)"><span class="vk-ikon">🎨</span>Kreativt, kultur, media</button>
            <button class="vk" onclick="velg('bransje','annet',this)"><span class="vk-ikon">📋</span>Annet / usikker</button>
          </div>
          <div class="nav-kn">
            <button class="kn-t" onclick="visSteg(2)">← Tilbake</button>
            <button class="kn-n" onclick="neste(3)">Neste →</button>
          </div>
        </div>
      </div>

      <!-- Steg 4: Investorer og vekst -->
      <div class="enk-steg" id="s4" style="display:none">
        <div class="enk-kort">
          <div class="enk-stegnr">Steg 4 av 5</div>
          <div class="enk-q">Investorer, kapital og ansatte</div>
          <div class="enk-hint">Disse avgjør mye om ENK er en reell mulighet.</div>
          <div class="ig">
            <label>Planlegger du å hente ekstern kapital eller investorer?</label>
            <div class="vg" style="margin-top:8px">
              <button class="vk" onclick="velg('investorer','ja',this)">Ja — vi ønsker investorer</button>
              <button class="vk" onclick="velg('investorer','nei',this)">Nei — selvfinansiert</button>
            </div>
          </div>
          <div class="ig" style="margin-top:20px">
            <label>Har du 30 000 kr tilgjengelig til aksjekapital? <span style="font-size:12px;color:var(--ink-mute)">(aksjeloven § 3-1)</span></label>
            <div class="vg" style="margin-top:8px">
              <button class="vk" onclick="velg('har30k','ja',this)">Ja</button>
              <button class="vk" onclick="velg('har30k','nei',this)">Nei — ikke akkurat nå</button>
            </div>
          </div>
          <div class="ig" style="margin-top:20px">
            <label>Planlegger du å ansette noen i løpet av det første året?</label>
            <div class="vg" style="margin-top:8px">
              <button class="vk" onclick="velg('ansette','ja',this)">Ja</button>
              <button class="vk" onclick="velg('ansette','nei',this)">Nei — solo foreløpig</button>
            </div>
          </div>
          <div class="nav-kn">
            <button class="kn-t" onclick="visSteg(3)">← Tilbake</button>
            <button class="kn-n" onclick="neste(4)">Neste →</button>
          </div>
        </div>
      </div>

      <!-- Steg 5: Sosiale rettigheter -->
      <div class="enk-steg" id="s5" style="display:none">
        <div class="enk-kort">
          <div class="enk-stegnr">Steg 5 av 5</div>
          <div class="enk-q">Sosiale rettigheter — hvor viktig er dette?</div>
          <div class="enk-hint">ENK og AS gir deg svært ulike rettigheter fra NAV og folketrygden.</div>
          <div class="ig">
            <label>Hvor viktig er det å ha fulle sykepenger fra dag 1?</label>
            <div class="vg" style="margin-top:8px">
              <button class="vk" onclick="velg('sykepenger','kritisk',this)">Veldig viktig — jeg tåler ikke to ukers karensdager</button>
              <button class="vk" onclick="velg('sykepenger','ok',this)">Greit — jeg klarer en kortere periode uten</button>
            </div>
          </div>
          <div class="ig" style="margin-top:20px">
            <label>Er muligheten til å få dagpenger ved nedgang viktig?</label>
            <div class="enk-hint" style="margin-bottom:8px">ENK-eiere har ikke rett til dagpenger. AS-ansatte har det.</div>
            <div class="vg" style="margin-top:0">
              <button class="vk" onclick="velg('dagpenger','ja',this)">Ja — viktig sikkerhetsnett</button>
              <button class="vk" onclick="velg('dagpenger','nei',this)">Nei — ikke avgjørende</button>
            </div>
          </div>
          <div class="nav-kn">
            <button class="kn-t" onclick="visSteg(4)">← Tilbake</button>
            <button class="kn-n" onclick="generer()">Vis anbefaling →</button>
          </div>
        </div>
      </div>
    </div>

    <!-- RESULTAT -->
    <div id="res" style="display:none">
      <div class="res-boks">
        <div id="res-badge"></div>
        <div class="res-tittel" id="res-tittel"></div>
        <ul class="res-grunner" id="res-grunner"></ul>
        <div id="skatt-seksjon"></div>
        <div class="res-tbl-wr"><table class="res-tbl" id="res-tbl"></table></div>
      </div>
      <div class="enk-cta">
        <h3>Vil du ha dette skriftlig og signert?</h3>
        <p>Vi setter opp en kort personlig vurdering av din situasjon — med konkret anbefaling, begrunnelse og sjekkliste for oppstart. Signert av juridisk rådgiver, Wombat AS.</p>
        <a href="mailto:rettsregel@gmail.com?subject=Forespørsel%20om%20selskapsform-vurdering" class="btn-aksjon">Send forespørsel →</a>
        <span class="enk-cta-pris">990 kr · Svar innen 48 timer</span>
      </div>
      <div style="margin-top:8px;text-align:center">
        <button onclick="startNytt()" style="background:none;border:1.5px solid var(--line);border-radius:10px;padding:12px 24px;font-family:var(--sans);font-size:14px;cursor:pointer;color:var(--ink-soft)">← Start på nytt</button>
      </div>
    </div>

    <!-- SEO prose -->
    <div class="prose sp-body" style="margin-top:64px">
      <h2>Hva er forskjellen på ENK og AS?</h2>
      <p>ENK (enkeltpersonforetak) er ikke en egen juridisk person — det er deg. Hele foretakets økonomi er din private økonomi. AS (aksjeselskap) er en egen juridisk enhet med begrenset ansvar for eierne.</p>
      <h3>Ansvar</h3>
      <p>I et ENK hefter du personlig og ubegrenset for all gjeld. Kreditorer kan gå etter hus, bil og sparepenger. I et AS er ansvaret begrenset til aksjekapitalen på 30 000 kr — med mindre du har stilt personlige garantier.</p>
      <h3>Skattebelastning</h3>
      <p>ENK: Overskuddet beskattes som personlig næringsinntekt — trygdeavgift 10,8 % pluss flat 22 % og trinnskatt opptil 17,8 %. Effektiv marginalskatt kan nå 51–52 % ved høye inntekter. AS: Selskapet betaler 22 % selskapsskatt. Vil du ta ut penger som utbytte, betaler du 37,84 % av det som gjenstår — total skattebelastning ca. 51,5 %. Men beholder du overskuddet i selskapet, skjer ingen dobbeltbeskatning.</p>
      <h3>Sosiale rettigheter</h3>
      <p>ENK: Sykepenger fra dag 17 (80 %), ingen dagpenger ved arbeidsledighet. AS med lønnet eier: 100 % sykepenger fra dag 1 (arbeidsgiver betaler de første 16 dagene), opptjening av dagpenger. Dette har en pris — arbeidsgiveravgift 14,1 % av lønn — men gir fulle NAV-rettigheter.</p>
      <h3>Overdragelse og eierskap</h3>
      <p>ENK kan ikke selges som en juridisk enhet. Du kan selge eiendeler, men kjøper må starte nytt foretak. AS kan selges enkelt via aksjesalg — selskapet fortsetter uendret. Det gjør AS langt mer interessant for fremtidig salg eller investorer.</p>
    </div>
  </div>
</main>

<script>
const D = {{}};
const TOTAL = 5;

function velg(felt, verdi, el) {{
  D[felt] = verdi;
  const gruppe = el.closest('.vg, [class*="ig"]');
  if (gruppe) {{
    gruppe.querySelectorAll('.vk').forEach(k => k.classList.remove('av'));
    el.classList.add('av');
  }}
}}

function visSteg(n) {{
  for (let i=1; i<=TOTAL; i++) {{
    const el = document.getElementById('s'+i);
    if (el) el.style.display = i===n ? 'block' : 'none';
  }}
  const pct = Math.round((n-1)/TOTAL*100);
  document.getElementById('pf').style.width = pct+'%';
  document.getElementById('pt').textContent = 'Steg '+n+' av '+TOTAL;
  document.getElementById('wiz').scrollIntoView({{behavior:'smooth',block:'start'}});
}}

function neste(s) {{
  if (s===1) {{
    if (!D.eiere) {{ alert('Velg om du er alene eller flere eiere.'); return; }}
    if (D.eiere === 'flere') {{ generer(); return; }}
  }}
  if (s===2) {{
    if (!D.kapital) {{ alert('Velg hva du vil gjøre med overskuddet.'); return; }}
    D.overskudd = parseInt(document.getElementById('overskudd').value) || 0;
  }}
  if (s===3 && !D.bransje) {{ alert('Velg bransje.'); return; }}
  if (s===4) {{
    if (!D.investorer) {{ alert('Angi om du planlegger investorer.'); return; }}
    if (!D.har30k) {{ alert('Angi om du har 30 000 kr tilgjengelig.'); return; }}
    if (!D.ansette) {{ alert('Angi om du planlegger å ansette.'); return; }}
  }}
  if (s===5) {{ generer(); return; }}
  visSteg(s+1);
}}

function kr(n) {{ return n.toLocaleString('nb-NO') + ' kr'; }}

function beregnEnkSkatt(x) {{
  if (x <= 0) return 0;
  const trygd = x * 0.108;
  const almInntekt = x - trygd;
  const flat = almInntekt * 0.22;
  let trinn = 0;
  if (x > 226100) trinn += (Math.min(x,318300)-226100)*0.017;
  if (x > 318300) trinn += (Math.min(x,725050)-318300)*0.040;
  if (x > 725050) trinn += (Math.min(x,980100)-725050)*0.137;
  if (x > 980100) trinn += (Math.min(x,1467200)-980100)*0.168;
  if (x > 1467200) trinn += (x-1467200)*0.178;
  return Math.round(trygd+flat+trinn);
}}

function beregnAsSkatt(x) {{
  if (x <= 0) return {{ss:0,rest:0,utb:0,tot:0}};
  const ss = Math.round(x*0.22);
  const rest = x-ss;
  const utb = Math.round(rest*0.3784);
  return {{ss, rest, tot: ss+utb}};
}}

function generer() {{
  // Determine recommendation
  let type, tittel, grunner=[];

  if (D.eiere === 'flere') {{
    type='as-krav';
    tittel='Dere er flere eiere. Da kreves AS.';
    grunner=['ENK kan bare ha én eier — det følger av foretaksnavnloven. For felles eierskap er AS den eneste juridiske løsningen.','AS gir dere aksjer som kan fordeles, selges og pantsettes. Dere kan regulere eierforholdet i en aksjonæravtale.','Start med å bestemme eierfordeling og lage vedtekter — det forebygger konflikter fra dag én.'];
  }} else if (D.investorer === 'ja') {{
    type='as-krav';
    tittel='Du trenger AS — investorer krever det.';
    grunner=['Investorer krever aksjer. Det er ikke mulig med ENK — aksjeloven regulerer eierskapet via aksjer.','Investorer trenger rettsvern, utbytte og mulighet for exit. Alt dette forutsetter AS.'];
  }} else if (D.har30k === 'nei') {{
    type='enk';
    tittel='Start som ENK — vurder AS etter ett til to år.';
    grunner=['Aksjekapitalen på 30 000 kr er et lovpålagt krav ved stiftelse av AS. Uten den starter du ikke AS.','ENK er gratis å etablere og enklere å drive. Du kan konvertere til AS når økonomien er på plass — det er en kjent og enkel prosess.'];
    if (D.sykepenger === 'kritisk') grunner.push('Merk: du er avhengig av sykepenger fra dag 1. Det er en reell ulempe med ENK — vurder å spare opp buffer til du konverterer til AS.');
  }} else {{
    let score = 0;
    const risk = {{konsulent:2, haandverk:3, handel:1, helse:3, kreativ:0, annet:1}};
    score += (risk[D.bransje]||1);
    if (D.kapital==='beholde') score += 3;
    if (D.kapital==='blanding') score += 1;
    if (D.ansette==='ja') score += 2;
    if (D.sykepenger==='kritisk') score += 2;
    if (D.dagpenger==='ja') score += 1;
    if (D.overskudd > 600000) score += 1;

    if (score >= 6) {{
      type='as';
      tittel='Vi anbefaler AS.';
      const riskMap = {{haandverk:'Bransjen din har høy risiko for erstatningskrav. AS begrenser ansvaret ditt til aksjekapitalen.',helse:'Helse og omsorg innebærer ansvar for andres liv og helse. AS gir deg det personlige ansvarsvernet du trenger.', konsulent:'Konsulenter kan stilles ansvarlig for feile råd. AS skiller privatøkonomien din fra virksomhetens risiko.'}};
      if (riskMap[D.bransje]) grunner.push(riskMap[D.bransje]);
      if (D.kapital==='beholde') grunner.push('Du vil beholde kapital i selskapet. AS lar deg akkumulere overskudd med kun 22 % selskapsskatt — uten å betale personskatt av det som ikke tas ut.');
      if (D.ansette==='ja') grunner.push('Du planlegger å ansette. AS er bedre egnet som arbeidsgiver — mer formell struktur, og du kan ansette deg selv med fulle NAV-rettigheter.');
      if (D.sykepenger==='kritisk') grunner.push('Du er avhengig av sykepenger fra dag 1. Med lønn fra eget AS har du 100 % sykepenger fra første dag — ikke 80 % fra dag 17 som ENK-eier.');
    }} else if (score >= 3) {{
      type='as';
      tittel='AS er det tryggeste valget — men ENK kan fungere.';
      if (D.kapital==='beholde') grunner.push('Du ønsker å beholde kapital i selskapet. AS er langt bedre egnet til det enn ENK.');
      if (D.sykepenger==='kritisk') grunner.push('Full sykepengedekning fra dag 1 krever at du er lønnet ansatt — mulig bare i AS.');
      grunner.push('ENK er enklere og billigere å starte. Men AS gir deg bedre vern og mer fleksibilitet over tid.');
    }} else {{
      type='enk';
      tittel='ENK er riktig for deg nå.';
      grunner.push('Du er solo, risikoen er lav, og du tar ut det du tjener. Da er ENK den enkleste og billigste løsningen.');
      grunner.push('Du sparer 36 825 kr i oppstartskostnader (gebyr + aksjekapital) og slipper årsregnskap og styrekrav.');
      grunner.push('Du kan alltid konvertere til AS — men spar den overgangen til du faktisk trenger det.');
    }}
  }}

  // Badge og tittel
  const badgeTekst = {{as:'AS anbefales',enk:'ENK anbefales','as-krav':'AS er påkrevd'}};
  document.getElementById('res-badge').innerHTML = `<span class="res-badge ${{type}}">${{badgeTekst[type]}}</span>`;
  document.getElementById('res-tittel').textContent = tittel;
  document.getElementById('res-grunner').innerHTML = grunner.map(g=>`<li>${{g}}</li>`).join('');

  // Skatt-illustrasjon
  let skattHTML = '';
  const ov = D.overskudd || 0;
  if (ov > 0) {{
    const enkSkatt = beregnEnkSkatt(ov);
    const asT = beregnAsSkatt(ov);
    skattHTML = `
    <div class="skatt-panel">
      <h4>Forenklet skatteillustrasjon — ${{kr(ov)}} i overskudd</h4>
      <div class="skatt-grid">
        <div class="skatt-kolonne">
          <div class="skatt-lov">ENK</div>
          <div class="skatt-rad"><span>Trygdeavgift (10,8 %)</span><span>${{kr(Math.round(ov*0.108))}}</span></div>
          <div class="skatt-rad"><span>Flat skatt (22 %)</span><span>${{kr(Math.round((ov-ov*0.108)*0.22))}}</span></div>
          <div class="skatt-rad"><span>Trinnskatt</span><span>${{kr(enkSkatt - Math.round(ov*0.108) - Math.round((ov-ov*0.108)*0.22))}}</span></div>
          <div class="skatt-rad total"><span>Total skatt</span><span>${{kr(enkSkatt)}}</span></div>
          <div class="skatt-rad igjen"><span>Du sitter igjen med</span><span>${{kr(ov-enkSkatt)}}</span></div>
        </div>
        <div class="skatt-kolonne">
          <div class="skatt-lov">AS — beholder i selskapet</div>
          <div class="skatt-rad"><span>Selskapsskatt (22 %)</span><span>${{kr(asT.ss)}}</span></div>
          <div class="skatt-rad igjen"><span>Akkumulert i AS</span><span>${{kr(asT.rest)}}</span></div>
          <div class="skatt-rad" style="margin-top:12px;padding-top:12px;border-top:1px solid var(--line);color:var(--ink-mute);font-size:12px">Tar du ut som utbytte: +${{kr(asT.utb)}} utbytteskatt → ${{kr(asT.tot)}} total</div>
        </div>
      </div>
      <div class="skatt-disclaimer">⚠️ Forenklet illustrasjon basert på 2026-satser. Inkluderer ikke minstefradrag, fradrag for næring, eller andre individuelle forhold. Ikke individuelt skatteråd.</div>
    </div>`;
  }}
  document.getElementById('skatt-seksjon').innerHTML = skattHTML;

  // Sammenligningstabell
  const anbefaltENK = type==='enk';
  const anbefaltAS = type==='as'||type==='as-krav';
  document.getElementById('res-tbl').innerHTML = `
    <thead><tr>
      <th></th>
      <th class="${{anbefaltENK?'anbefalt-hd':''}}">ENK</th>
      <th class="${{anbefaltAS?'anbefalt-hd':''}}">AS</th>
    </tr></thead>
    <tbody>
      <tr><td>Oppstartskostnad</td><td class="${{anbefaltENK?'anbefalt-kol':''}}">0 kr</td><td class="${{anbefaltAS?'anbefalt-kol':''}}">36 825 kr<br><small style="color:var(--ink-mute)">6 825 gebyr + 30 000 aksjekapital</small></td></tr>
      <tr><td>Antall eiere</td><td class="${{anbefaltENK?'anbefalt-kol':''}}">Bare én</td><td class="${{anbefaltAS?'anbefalt-kol':''}}">En eller flere</td></tr>
      <tr><td>Personlig ansvar</td><td class="${{anbefaltENK?'anbefalt-kol':''}}">Fullt — ubegrenset</td><td class="${{anbefaltAS?'anbefalt-kol':''}}">Begrenset til aksjekapitalen</td></tr>
      <tr><td>Skatt på overskudd</td><td class="${{anbefaltENK?'anbefalt-kol':''}}">Personskatt<br><small style="color:var(--ink-mute)">22 % + 10,8 % trygd + trinnskatt</small></td><td class="${{anbefaltAS?'anbefalt-kol':''}}">22 % selskapsskatt<br><small style="color:var(--ink-mute)">+ utbytteskatt 37,84 % ved uttak</small></td></tr>
      <tr><td>Sykepenger</td><td class="${{anbefaltENK?'anbefalt-kol':''}}">Fra dag 17 (80 %)</td><td class="${{anbefaltAS?'anbefalt-kol':''}}">Fra dag 1 (100 %) med lønn</td></tr>
      <tr><td>Dagpenger</td><td class="${{anbefaltENK?'anbefalt-kol':''}}">Nei</td><td class="${{anbefaltAS?'anbefalt-kol':''}}">Ja, ved lønnet ansettelse</td></tr>
      <tr><td>Investorer mulig?</td><td class="${{anbefaltENK?'anbefalt-kol':''}}">Nei</td><td class="${{anbefaltAS?'anbefalt-kol':''}}">Ja</td></tr>
      <tr><td>Kan selges?</td><td class="${{anbefaltENK?'anbefalt-kol':''}}">Bare enkelteiendeler</td><td class="${{anbefaltAS?'anbefalt-kol':''}}">Ja — via aksjesalg</td></tr>
      <tr><td>Regnskapskrav</td><td class="${{anbefaltENK?'anbefalt-kol':''}}">Enkel bokføring</td><td class="${{anbefaltAS?'anbefalt-kol':''}}">Årsregnskap, styre, GF</td></tr>
    </tbody>`;

  document.getElementById('wiz').style.display='none';
  const resEl = document.getElementById('res');
  resEl.style.display='block';
  setTimeout(()=>resEl.scrollIntoView({{behavior:'smooth',block:'start'}}),50);
}}

function startNytt() {{
  Object.keys(D).forEach(k=>delete D[k]);
  document.getElementById('res').style.display='none';
  document.getElementById('wiz').style.display='block';
  document.querySelectorAll('.vk').forEach(k=>k.classList.remove('av'));
  document.getElementById('overskudd').value='';
  visSteg(1);
}}
</script>

{site_footer(depth=2)}"""




def render_kontrakter_hub():
    return f"""{shared_head(
        'Kontraktsmaler og juridiske dokumenter | Rettsregel',
        'Last ned gratis kontraktsmaler basert på norsk lov. Husleiekontrakt, kjøpekontrakt, samboeravtale og mer — fyll ut i nettleseren og last ned som PDF.',
        depth=1, canonical_path='/kontrakter/'
    )}
<body>
{site_nav(depth=1)}
<main class="page">
  <div class="container">
    <div class="tjenester-hero">
      <div class="article-eyebrow">Kontrakter</div>
      <h1>Juridiske maler — gratis å bruke</h1>
      <p>Fyll ut i nettleseren. Last ned som PDF. Alle maler er basert på gjeldende norsk lov.</p>
    </div>
    <div class="tjensters-grid">
      <a href="../kontrakter/husleiekontrakt/" class="tjeneste-kort">
        <div class="tjeneste-kat">Bolig og leie</div>
        <h3>Husleiekontrakt</h3>
        <p>Standard leiekontrakt for bolig. Tidsubestemt eller tidsbestemt. Fyll ut i nettleseren og last ned som PDF.</p>
        <div class="tjeneste-pil">Fyll ut og last ned →</div>
      </a>

      <div class="tjeneste-kort snart">
        <span class="snart-badge">Snart</span>
        <div class="tjeneste-kat graa">Kjøp og salg</div>
        <h3>Kjøpekontrakt bil</h3>
        <p>Juridisk korrekt kjøpekontrakt for privatbilsalg. Basert på kjøpsloven av 1988.</p>
        <div class="tjeneste-pil">Kommer snart</div>
      </div>

      <div class="tjeneste-kort snart">
        <span class="snart-badge">Snart</span>
        <div class="tjeneste-kat graa">Familie og samliv</div>
        <h3>Samboeravtale</h3>
        <p>Avtale om økonomi, bolig og eierskap for samboere. Basert på husstandsfellesskapsloven.</p>
        <div class="tjeneste-pil">Kommer snart</div>
      </div>

      <div class="tjeneste-kort snart">
        <span class="snart-badge">Snart</span>
        <div class="tjeneste-kat graa">Økonomi og gjeld</div>
        <h3>Gjeldsbrev</h3>
        <p>Enkelt gjeldsbrev for private lån. Rentefritt eller med renter og nedbetalingsplan.</p>
        <div class="tjeneste-pil">Kommer snart</div>
      </div>

      <div class="tjeneste-kort snart">
        <span class="snart-badge">Snart</span>
        <div class="tjeneste-kat graa">Selskapsrett</div>
        <h3>Aksjonæravtale</h3>
        <p>Avtale mellom aksjonærer i AS. Forkjøpsrett, stemmerett og utbyttepolitikk.</p>
        <div class="tjeneste-pil">Kommer snart</div>
      </div>

      <div class="tjeneste-kort snart">
        <span class="snart-badge">Snart</span>
        <div class="tjeneste-kat graa">Selskapsrett</div>
        <h3>Generalforsamlingsprotokoll</h3>
        <p>Protokollmal for ordinær og ekstraordinær GF. Klar til å fylle ut og signere.</p>
        <div class="tjeneste-pil">Kommer snart</div>
      </div>
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
@media (max-width: 1024px) {{ .kontrakt-layout {{ grid-template-columns: 1fr; }} }}
.kontrakt-skjema {{
  background: var(--bg-card); border: 1px solid var(--line);
  border-radius: 20px; padding: 28px; box-shadow: var(--shadow-md);
  position: sticky; top: 24px;
}}
@media (max-width: 900px) {{ .kontrakt-skjema {{ position: static; }} }}
.ks-tittel {{ font-family: var(--serif); font-size: 18px; font-weight: 400; margin-bottom: 20px; }}
.ks-seksjon {{ margin-bottom: 20px; border-bottom: 1px solid var(--line); padding-bottom: 20px; }}
.ks-seksjon:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
.ks-seksjon-tittel {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); margin-bottom: 12px; }}
.kf {{ margin-bottom: 10px; }}
.kf label {{ display: block; font-size: 12px; font-weight: 600; color: var(--ink-soft); margin-bottom: 4px; }}
.kf input, .kf select, .kf textarea {{
  width: 100%; padding: 9px 12px; border: 1.5px solid var(--line);
  border-radius: 8px; font-family: var(--sans); font-size: 13px;
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
/* Dokument */
.kontrakt-dokument {{
  background: white; border: 1px solid var(--line); border-radius: 16px;
  padding: 48px 56px; box-shadow: var(--shadow-sm); font-family: 'EB Garamond', Georgia, serif;
  font-size: 15px; line-height: 1.8; color: var(--ink);
}}
@media (max-width: 600px) {{ .kontrakt-dokument {{ padding: 24px 20px; font-size: 14px; }} }}
.kd-tittel {{
  font-size: 20px; font-weight: 500; text-align: center;
  margin-bottom: 6px; letter-spacing: 0.02em;
}}
.kd-undertittel {{ font-size: 13px; text-align: center; color: var(--ink-mute); margin-bottom: 32px; font-family: var(--sans); }}
.kd-h2 {{ font-size: 14px; font-weight: 700; font-family: var(--sans); text-transform: uppercase; letter-spacing: 0.08em; margin: 28px 0 8px; border-bottom: 1px solid var(--line); padding-bottom: 4px; }}
.kd-rad {{ display: flex; gap: 8px; margin-bottom: 4px; }}
.kd-etikettene {{ color: var(--ink-mute); min-width: 140px; font-size: 14px; }}
.kd-v {{ font-size: 15px; }}
.kd-v.tomt {{ color: var(--ink-mute); font-style: italic; }}
.kd-avsnitt {{ margin: 8px 0; }}
.kd-varighet-boks {{
  border: 1px solid var(--line); border-radius: 8px; padding: 12px 16px;
  margin: 8px 0; background: var(--bg);
}}
.kd-sign {{ margin-top: 40px; display: grid; grid-template-columns: 1fr 1fr; gap: 32px; }}
.kd-sign-felt {{ border-top: 1px solid var(--ink); padding-top: 6px; }}
.kd-sign-etikett {{ font-size: 13px; color: var(--ink-mute); font-family: var(--sans); }}
.kd-sign-navn {{ font-size: 14px; margin-top: 4px; }}
.kd-footer {{ font-size: 12px; color: var(--ink-mute); font-family: var(--sans); margin-top: 32px; text-align: center; border-top: 1px solid var(--line); padding-top: 12px; }}
@media print {{
  .no-print {{ display: none !important; }}
  nav.site-nav, footer.site-footer, #chat-toggle, #chat-panel, .breadcrumbs, .article-header, .kontrakt-skjema, .sp-body {{ display: none !important; }}
  .kontrakt-layout {{ grid-template-columns: 1fr; display: block; }}
  .kontrakt-dokument {{ border: none; box-shadow: none; padding: 0; border-radius: 0; font-size: 11pt; line-height: 1.6; }}
  body {{ background: white; }}
}}
</style>

<main class="page">
  <div class="container">
    <div class="breadcrumbs no-print">
      <a href="../../">Rettsregel</a>
      <span class="sep">›</span>
      <a href="../../kontrakter/">Kontrakter</a>
      <span class="sep">›</span>
      <span class="current">Husleiekontrakt</span>
    </div>

    <div class="article-header no-print">
      <div class="article-eyebrow">Kontraktmal</div>
      <h1 class="article-title">Husleiekontrakt for bolig</h1>
      <p class="article-description">Fyll ut feltene til venstre. Kontrakten oppdateres live. Last ned som PDF når du er ferdig.</p>
    </div>

    <div class="kontrakt-layout">
      <!-- SKJEMA -->
      <div class="kontrakt-skjema no-print">
        <div class="ks-tittel">Fyll ut kontrakten</div>

        <div class="ks-seksjon">
          <div class="ks-seksjon-tittel">Utleier</div>
          <div class="kf"><label>Fullt navn</label><input type="text" id="utleier_navn" oninput="oppdater()" placeholder="Ola Nordmann"></div>
          <div class="kf"><label>Adresse</label><input type="text" id="utleier_adresse" oninput="oppdater()" placeholder="Storgata 1, 0000 Oslo"></div>
          <div class="kf"><label>Telefon / e-post</label><input type="text" id="utleier_kontakt" oninput="oppdater()" placeholder="900 00 000 / ola@eksempel.no"></div>
        </div>

        <div class="ks-seksjon">
          <div class="ks-seksjon-tittel">Leietaker</div>
          <div class="kf"><label>Fullt navn</label><input type="text" id="leietaker_navn" oninput="oppdater()" placeholder="Kari Nordmann"></div>
          <div class="kf"><label>Fødselsdato</label><input type="date" id="leietaker_fodsel" oninput="oppdater()"></div>
          <div class="kf"><label>Telefon / e-post</label><input type="text" id="leietaker_kontakt" oninput="oppdater()" placeholder="900 00 000 / kari@eksempel.no"></div>
        </div>

        <div class="ks-seksjon">
          <div class="ks-seksjon-tittel">Leieobjektet</div>
          <div class="kf"><label>Adresse</label><input type="text" id="bolig_adresse" oninput="oppdater()" placeholder="Leiegata 5, 5000 Bergen"></div>
          <div class="kf"><label>Type bolig</label><input type="text" id="bolig_type" oninput="oppdater()" placeholder="f.eks. 2-roms leilighet, 55 m²"></div>
          <div class="kf">
            <label>Møblering</label>
            <div class="kf-radio">
              <label><input type="radio" name="moblert" value="umøblert" onchange="oppdater()" checked> Umøblert</label>
              <label><input type="radio" name="moblert" value="delvis møblert" onchange="oppdater()"> Delvis møblert</label>
              <label><input type="radio" name="moblert" value="møblert" onchange="oppdater()"> Møblert</label>
            </div>
          </div>
        </div>

        <div class="ks-seksjon">
          <div class="ks-seksjon-tittel">Varighet</div>
          <div class="kf">
            <div class="kf-radio">
              <label><input type="radio" name="varighet" value="tidsubestemt" onchange="oppdaterVarighetUI()" checked> Tidsubestemt</label>
              <label><input type="radio" name="varighet" value="tidsbestemt" onchange="oppdaterVarighetUI()"> Tidsbestemt</label>
            </div>
          </div>
          <div class="kf"><label>Startdato</label><input type="date" id="start_dato" oninput="oppdater()"></div>
          <div id="tidsbestemt-felt" style="display:none">
            <div class="kf"><label>Sluttdato</label><input type="date" id="slutt_dato" oninput="oppdater()"></div>
          </div>
          <div id="oppsigelse-felt">
            <div class="kf"><label>Oppsigelsestid (måneder)</label>
              <select id="oppsigelse_tid" onchange="oppdater()">
                <option value="1">1 måned</option>
                <option value="2">2 måneder</option>
                <option value="3" selected>3 måneder</option>
              </select>
            </div>
          </div>
        </div>

        <div class="ks-seksjon">
          <div class="ks-seksjon-tittel">Økonomi</div>
          <div class="kf"><label>Månedlig leie (kr)</label><input type="number" id="leie_kr" oninput="oppdater()" placeholder="12000" min="0"></div>
          <div class="kf"><label>Forfallsdato (dag i mnd)</label><input type="number" id="forfall_dag" oninput="oppdater()" placeholder="1" min="1" max="28"></div>
          <div class="kf"><label>Kontonummer</label><input type="text" id="konto_nr" oninput="oppdater()" placeholder="1234 56 78901"></div>
          <div class="kf"><label>Depositum (kr)</label><input type="number" id="depositum_kr" oninput="oppdater()" placeholder="36000" min="0"></div>
          <div class="kf">
            <label>Strøm og vann</label>
            <div class="kf-radio">
              <label><input type="radio" name="strom" value="Inkludert i leien" onchange="oppdater()" checked> Inkludert</label>
              <label><input type="radio" name="strom" value="Betales i tillegg" onchange="oppdater()"> I tillegg</label>
              <label><input type="radio" name="strom" value="Eget abonnement" onchange="oppdater()"> Eget abonnement</label>
            </div>
          </div>
        </div>

        <div class="ks-seksjon">
          <div class="ks-seksjon-tittel">Særlige vilkår (valgfritt)</div>
          <div class="kf"><textarea id="særlige_vilkår" oninput="oppdater()" placeholder="f.eks. Dyrehold er ikke tillatt. Parkering er inkludert (plass nr. 12)."></textarea></div>
        </div>

        <button class="last-ned-kn" onclick="window.print()">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7,10 12,15 17,10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Last ned som PDF
        </button>
        <p style="font-size:12px;color:var(--ink-mute);text-align:center;margin-top:10px">Trykk «Last ned» → «Lagre som PDF» i utskriftsdialogen</p>
      </div>

      <!-- DOKUMENT -->
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
        <div class="kd-avsnitt">Boligen på <strong id="kd-bolig-adresse">[adresse]</strong> leies ut <strong id="kd-moblert">umøblert</strong>.</div>
        <div class="kd-avsnitt">Boligtype: <span id="kd-bolig-type">[type]</span>.</div>

        <div class="kd-h2">3. Leieforholdets varighet og oppsigelse</div>
        <div class="kd-varighet-boks" id="kd-varighet-boks">
          Tidsubestemt leieforhold. Starter den <strong id="kd-start-dato">[dato]</strong>.
          Kan sies opp av begge parter med <strong id="kd-oppsigelse-tid">3</strong> måneders varsel,
          regnet fra 1. i påfølgende måned, jf. husleieloven §§ 9-3 og 9-6.
        </div>

        <div class="kd-h2">4. Leie, depositum og tillegg</div>
        <div class="kd-rad"><span class="kd-etikettene">Månedlig leie</span><span class="kd-v"><strong id="kd-leie">_______________</strong> kr/mnd</span></div>
        <div class="kd-rad"><span class="kd-etikettene">Forfall</span><span class="kd-v">Den <strong id="kd-forfall">___</strong>. i hver måned</span></div>
        <div class="kd-rad"><span class="kd-etikettene">Konto</span><span class="kd-v" id="kd-konto">_______________</span></div>
        <div class="kd-rad" style="margin-top:8px"><span class="kd-etikettene">Depositum</span><span class="kd-v"><strong id="kd-depositum">_______________</strong> kr. Settes på særskilt depositumskonto i leietakers navn, jf. husleieloven § 3-5.</span></div>
        <div class="kd-rad" style="margin-top:8px"><span class="kd-etikettene">Strøm og vann</span><span class="kd-v" id="kd-strom">Inkludert i leien</span></div>

        <div class="kd-h2">5. Vedlikehold og bruk</div>
        <div class="kd-avsnitt">Leietaker plikter å behandle boligen med tilbørlig aktsomhet, jf. husleieloven § 5-2. Leietaker bekoster vedlikehold av låser, kraner, elektriske kontakter og batteri i røykvarsler, jf. husleieloven § 5-3. Røyking og dyrehold er kun tillatt etter særskilt skriftlig avtale.</div>

        <div class="kd-h2">6. Husordensregler og bruk</div>
        <div class="kd-avsnitt">Leietaker plikter å overholde gjeldende husordensregler. Fremleie er ikke tillatt uten utleiers skriftlige samtykke, jf. husleieloven § 7-2.</div>

        <div class="kd-h2" id="kd-sæ-h" style="display:none">7. Særlige vilkår</div>
        <div class="kd-avsnitt" id="kd-særlige-vilkår" style="display:none"></div>

        <div class="kd-h2">8. Signatur</div>
        <div class="kd-avsnitt" style="margin-bottom:24px">Kontrakten er undertegnet i to eksemplarer, ett til hver part.</div>
        <div class="kd-sign">
          <div>
            <div class="kd-sign-felt"></div>
            <div class="kd-sign-etikett">Sted og dato — Utleier</div>
            <div class="kd-sign-navn" id="kd-sign-utleier">_______________</div>
          </div>
          <div>
            <div class="kd-sign-felt"></div>
            <div class="kd-sign-etikett">Sted og dato — Leietaker</div>
            <div class="kd-sign-navn" id="kd-sign-leietaker">_______________</div>
          </div>
        </div>
        <div class="kd-footer">Kontrakten er utarbeidet i samsvar med husleieloven av 26. mars 1999. Rettsregel.no</div>
      </div>
    </div>

    <div class="prose sp-body no-print">
      <h2>Hva bør en husleiekontrakt inneholde?</h2>
      <p>En gyldig husleiekontrakt trenger partenes navn, boligens adresse, leiens størrelse, forfallsdato og leieperiodens lengde. Alt annet er viktig, men ikke et krav for gyldighet.</p>
      <h3>Depositum — alltid på depositumskonto</h3>
      <p>Depositumet skal stå på en særskilt konto i leietakers navn, adskilt fra utleiers midler, jf. husleieloven § 3-5. Maksimalt 6 månedlige leier. Utleier kan ikke disponere pengene uten leietakers samtykke eller dom.</p>
      <h3>Tidsbestemt eller tidsubestemt?</h3>
      <p>Tidsbestemte kontrakter på 3 år eller mer brukes der begge parter vil sikre en bestemt periode. Kortere tidsbestemte kontrakter er lovlig bare i særskilte tilfeller (jf. husleieloven § 9-3). Usikker? Velg tidsubestemt.</p>
      <h3>Relevante paragrafer</h3>
      <p><a href="../../lover/husleieloven/3-5/">§ 3-5 Depositum</a> · <a href="../../lover/husleieloven/9-3/">§ 9-3 Oppsigelse fra utleier</a> · <a href="../../lover/husleieloven/9-6/">§ 9-6 Oppsigelse fra leietaker</a> · <a href="../../lover/husleieloven/5-2/">§ 5-2 Leietakers vedlikeholdsplikt</a></p>
    </div>
  </div>
</main>

<script>
function v(id) {{ return document.getElementById(id); }}
function sett(id, tekst) {{
  const el = v(id);
  if (!el) return;
  el.textContent = tekst || '';
  el.className = 'kd-v' + (tekst ? '' : ' tomt');
}}

function formDato(iso) {{
  if (!iso) return '';
  return new Date(iso+'T12:00:00').toLocaleDateString('nb-NO',{{day:'numeric',month:'long',year:'numeric'}});
}}

function oppdaterVarighetUI() {{
  const erTidsbestemt = document.querySelector('input[name=varighet]:checked').value === 'tidsbestemt';
  v('tidsbestemt-felt').style.display = erTidsbestemt ? 'block' : 'none';
  v('oppsigelse-felt').style.display = erTidsbestemt ? 'none' : 'block';
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
  sett('kd-moblert', mob ? mob.value : 'umøblert');
  const leieKr = parseInt(v('leie_kr').value);
  sett('kd-leie', leieKr ? leieKr.toLocaleString('nb-NO') : '');
  sett('kd-forfall', v('forfall_dag').value);
  sett('kd-konto', v('konto_nr').value);
  const depKr = parseInt(v('depositum_kr').value);
  sett('kd-depositum', depKr ? depKr.toLocaleString('nb-NO') : '');
  const strom = document.querySelector('input[name=strom]:checked');
  sett('kd-strom', strom ? strom.value : '');

  const erTidsbestemt = document.querySelector('input[name=varighet]:checked').value === 'tidsbestemt';
  const startDato = v('start_dato').value;
  const sluttDato = v('slutt_dato').value;
  const oppsTid = v('oppsigelse_tid') ? v('oppsigelse_tid').value : '3';

  if (erTidsbestemt) {{
    v('kd-varighet-boks').innerHTML =
      'Tidsbestemt leieforhold fra <strong>' + (formDato(startDato)||'[startdato]') + '</strong> til <strong>' +
      (formDato(sluttDato)||'[sluttdato]') + '</strong>. Leieforholdet opphører uten oppsigelse ved utløpsdato, jf. husleieloven § 9-3.';
  }} else {{
    v('kd-varighet-boks').innerHTML =
      'Tidsubestemt leieforhold. Starter den <strong>' + (formDato(startDato)||'[dato]') + '</strong>. ' +
      'Kan sies opp av begge parter med <strong>' + oppsTid + '</strong> måneders varsel, ' +
      'regnet fra 1. i påfølgende måned, jf. husleieloven §§ 9-3 og 9-6.';
  }}

  const særlige = v('særlige_vilkår').value.trim();
  v('kd-sæ-h').style.display = særlige ? 'block' : 'none';
  v('kd-særlige-vilkår').style.display = særlige ? 'block' : 'none';
  v('kd-særlige-vilkår').textContent = særlige;

  sett('kd-sign-utleier', v('utleier_navn').value);
  sett('kd-sign-leietaker', v('leietaker_navn').value);
}}

oppdater();
</script>

{site_footer(depth=2)}"""



def render_tjenester_reklamasjon_bil():
    return f"""{shared_head(
        'Reklamasjon bilkjøp — lag brevet ditt gratis | Rettsregel',
        'Kjøpte du en bil med feil? Svar på noen spørsmål og få et juridisk korrekt reklamasjonsbrev klart til å sende — gratis.',
        depth=2, canonical_path='/tjenester/reklamasjon-bil/'
    )}
<body>
{site_nav(depth=2)}

<style>
.wizard-wrapper {{ max-width: 760px; margin: 0 auto; }}
.wizard-progress {{ margin-bottom: 32px; }}
.progress-bar {{ height: 5px; background: var(--line); border-radius: 3px; overflow: hidden; margin-bottom: 8px; }}
.progress-fill {{ height: 100%; background: var(--accent); border-radius: 3px; transition: width 0.35s ease; }}
.progress-tekst {{ font-size: 13px; color: var(--ink-mute); font-weight: 500; }}
.wizard-steg {{ animation: fadeInUp 0.22s ease; }}
.steg-kort {{
  background: var(--bg-card); border: 1px solid var(--line);
  border-radius: 20px; padding: 40px; box-shadow: var(--shadow-md); margin-bottom: 24px;
}}
@media (max-width: 600px) {{ .steg-kort {{ padding: 24px 20px; }} }}
.steg-nummer {{ font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent); margin-bottom: 10px; }}
.steg-sporsmal {{ font-family: var(--serif); font-size: 22px; font-weight: 400; line-height: 1.25; margin-bottom: 8px; }}
.steg-hint {{ font-size: 14px; color: var(--ink-mute); margin-bottom: 24px; line-height: 1.5; }}
.w-input {{
  width: 100%; padding: 13px 16px; border: 1.5px solid var(--line);
  border-radius: 10px; font-family: var(--sans); font-size: 15px;
  background: var(--bg); color: var(--ink); box-sizing: border-box; transition: border-color 0.15s;
}}
.w-input:focus {{ outline: none; border-color: var(--accent); }}
.w-textarea {{ min-height: 90px; resize: vertical; }}
.ig {{ margin-bottom: 16px; }}
.ig label {{ display: block; font-size: 13px; font-weight: 600; color: var(--ink-soft); margin-bottom: 6px; }}
.valg-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }}
.valg-grid-3 {{ grid-template-columns: 1fr 1fr 1fr; }}
@media (max-width: 640px) {{ .valg-grid {{ grid-template-columns: 1fr; }} }}
@media (max-width: 760px) {{ .valg-grid-3 {{ grid-template-columns: 1fr 1fr; }} }}
@media (max-width: 560px) {{ .valg-grid-3 {{ grid-template-columns: 1fr; }} }}
@media (max-width: 600px) {{ .w-input {{ font-size: 16px; }} }}
.valg-kort {{
  border: 1.5px solid var(--line); border-radius: 12px; padding: 14px 16px;
  cursor: pointer; text-align: left; background: var(--bg); transition: all 0.15s;
  font-family: var(--sans); font-size: 14px; color: var(--ink); line-height: 1.35;
  min-height: 44px;
}}
.valg-kort:hover {{ border-color: var(--accent-soft); }}
.valg-kort.valgt {{ border-color: var(--accent); background: rgba(177,74,42,0.05); color: var(--accent); font-weight: 600; }}
.valg-ikon {{ font-size: 22px; display: block; margin-bottom: 6px; }}
.nav-kn {{ display: flex; gap: 10px; margin-top: 28px; }}
.kn-neste {{
  flex: 1; background: var(--accent); color: white; border: none;
  border-radius: 12px; font-family: var(--sans); font-size: 16px;
  font-weight: 600; padding: 16px; cursor: pointer; transition: background 0.2s;
}}
.kn-neste:hover {{ background: var(--accent-deep); }}
.kn-tilbake {{
  background: transparent; color: var(--ink-soft); border: 1.5px solid var(--line);
  border-radius: 12px; font-family: var(--sans); font-size: 15px;
  font-weight: 500; padding: 14px 20px; cursor: pointer; transition: all 0.15s;
}}
.kn-tilbake:hover {{ border-color: var(--ink-soft); }}
.vurdering-kort {{ border-radius: 16px; padding: 28px 32px; margin-bottom: 24px; }}
.vurdering-kort.ok {{ background: #f0f9f0; border: 1.5px solid #8dcc8d; }}
.vurdering-kort.advarsel {{ background: #fffbec; border: 1.5px solid #e8c840; }}
.vurdering-kort.for-sent {{ background: #fdf0ef; border: 1.5px solid #e8a09a; }}
.vurdering-tittel {{ font-family: var(--serif); font-size: 22px; font-weight: 400; margin-bottom: 14px; }}
.vurdering-liste {{ margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 9px; }}
.vurdering-liste li {{ font-size: 14px; display: flex; gap: 10px; align-items: flex-start; line-height: 1.45; }}
.v-ikon {{ flex-shrink: 0; }}
.brev-wrapper {{ background: white; border: 1px solid var(--line); border-radius: 16px; overflow: hidden; margin-bottom: 24px; }}
.brev-header {{ background: var(--bg-alt); padding: 14px 24px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--line); }}
.brev-header-tittel {{ font-size: 14px; font-weight: 600; color: var(--ink-soft); }}
.brev-kn-wrapper {{ display: flex; gap: 8px; }}
.brev-kn {{
  font-size: 13px; font-weight: 600; padding: 8px 14px; border-radius: 8px;
  border: none; cursor: pointer; font-family: var(--sans);
}}
.brev-kn-kopi {{ background: var(--accent); color: white; }}
.brev-kn-print {{ background: var(--bg-card); border: 1px solid var(--line); color: var(--ink); }}
.brev-innhold {{
  padding: 36px 40px; font-family: 'EB Garamond', Georgia, serif;
  font-size: 16px; line-height: 1.75; white-space: pre-wrap; color: var(--ink);
}}
@media (max-width: 600px) {{ .brev-innhold {{ padding: 20px; font-size: 15px; }} }}
.neste-steg-boks {{ background: var(--bg-alt); border-radius: 16px; padding: 28px 32px; margin-bottom: 24px; }}
.neste-steg-boks h3 {{ font-family: var(--serif); font-size: 20px; font-weight: 400; margin-bottom: 16px; }}
.neste-steg-liste {{ margin: 0; padding: 0; list-style: none; counter-reset: ns; display: flex; flex-direction: column; gap: 12px; }}
.neste-steg-liste li {{ display: flex; gap: 14px; align-items: flex-start; font-size: 14px; line-height: 1.5; }}
.neste-steg-liste li::before {{
  counter-increment: ns; content: counter(ns);
  background: var(--accent); color: white; width: 24px; height: 24px; min-width: 24px;
  border-radius: 50%; display: flex; align-items: center; justify-content: center;
  font-size: 12px; font-weight: 700;
}}
.start-paa-nytt {{
  background: none; border: 1.5px solid var(--line); border-radius: 10px;
  padding: 12px 24px; font-family: var(--sans); font-size: 14px;
  cursor: pointer; color: var(--ink-soft); display: block; margin: 16px auto 0;
}}
@media print {{
  .no-print {{ display: none !important; }}
  nav.site-nav, footer.site-footer, #chat-toggle, #chat-panel, .article-header, .sp-body, .breadcrumbs {{ display: none !important; }}
  body {{ background: white; }}
  .brev-wrapper {{ border: none; box-shadow: none; }}
  .brev-header {{ display: none; }}
  .brev-innhold {{ padding: 0; font-size: 12pt; line-height: 1.7; }}
}}
</style>

<main class="page">
  <div class="narrow">
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
      <p class="article-description">Svar på seks spørsmål. Du får en vurdering av rettighetene dine og et ferdig brev du kan sende med en gang.</p>
    </div>

    <!-- WIZARD -->
    <div class="wizard-wrapper no-print" id="wizard-wrapper">
      <div class="wizard-progress">
        <div class="progress-bar"><div class="progress-fill" id="pfill" style="width:0%"></div></div>
        <span class="progress-tekst" id="ptekst">Steg 1 av 6</span>
      </div>

      <!-- Steg 1 -->
      <div class="wizard-steg" id="steg-1">
        <div class="steg-kort">
          <div class="steg-nummer">Steg 1 av 6</div>
          <div class="steg-sporsmal">Hvem kjøpte du bilen av?</div>
          <div class="steg-hint">Dette avgjør hvilken lov som gjelder og hvilke rettigheter du har.</div>
          <div class="valg-grid">
            <button class="valg-kort" onclick="velg('selger_type','forhandler',this)">
              <span class="valg-ikon">🏢</span>
              <strong>Bilforhandler</strong><br>
              <span style="font-size:13px;color:var(--ink-mute)">Registrert næringsdrivende</span>
            </button>
            <button class="valg-kort" onclick="velg('selger_type','privat',this)">
              <span class="valg-ikon">👤</span>
              <strong>Privatperson</strong><br>
              <span style="font-size:13px;color:var(--ink-mute)">Finn.no, bekjente o.l.</span>
            </button>
          </div>
          <div class="nav-kn"><button class="kn-neste" onclick="nesteFra(1)">Neste →</button></div>
        </div>
      </div>

      <!-- Steg 2 -->
      <div class="wizard-steg" id="steg-2" style="display:none">
        <div class="steg-kort">
          <div class="steg-nummer">Steg 2 av 6</div>
          <div class="steg-sporsmal">Litt om kjøpet</div>
          <div class="steg-hint">Vi bruker dette til fristberegning og til brevet ditt.</div>
          <div class="ig">
            <label for="kjopsdato">Dato du kjøpte / overtok bilen</label>
            <input type="date" id="kjopsdato" class="w-input">
          </div>
          <div class="ig">
            <label for="bil_besk">Bilens merke, modell og regnr</label>
            <input type="text" id="bil_besk" class="w-input" placeholder="f.eks. Toyota RAV4 2019, regnr AB 12345">
          </div>
          <div class="ig">
            <label for="kjopsum">Kjøpesum (kr)</label>
            <input type="number" id="kjopsum" class="w-input" placeholder="f.eks. 350000" min="0">
          </div>
          <div class="nav-kn">
            <button class="kn-tilbake" onclick="visSteg(1)">← Tilbake</button>
            <button class="kn-neste" onclick="nesteFra(2)">Neste →</button>
          </div>
        </div>
      </div>

      <!-- Steg 3 -->
      <div class="wizard-steg" id="steg-3" style="display:none">
        <div class="steg-kort">
          <div class="steg-nummer">Steg 3 av 6</div>
          <div class="steg-sporsmal">Hva er galt med bilen?</div>
          <div class="steg-hint">Velg kategori og beskriv feilen så konkret du kan. Detaljene styrker brevet ditt.</div>
          <div class="valg-grid valg-grid-3" style="margin-bottom:16px">
            <button class="valg-kort" onclick="velg('feil_kat','motor',this)"><span class="valg-ikon">🔧</span>Motor / drivverk</button>
            <button class="valg-kort" onclick="velg('feil_kat','rust',this)"><span class="valg-ikon">🪣</span>Rust / karosseri</button>
            <button class="valg-kort" onclick="velg('feil_kat','el',this)"><span class="valg-ikon">⚡</span>Elektronikk</button>
            <button class="valg-kort" onclick="velg('feil_kat','km',this)"><span class="valg-ikon">📊</span>Feil kilometerstand</button>
            <button class="valg-kort" onclick="velg('feil_kat','vraket',this)"><span class="valg-ikon">💥</span>Skjult ulykkeshistorikk</button>
            <button class="valg-kort" onclick="velg('feil_kat','annet',this)"><span class="valg-ikon">📋</span>Annet</button>
          </div>
          <div class="ig">
            <label for="feil_besk">Beskriv feilen konkret</label>
            <textarea id="feil_besk" class="w-input w-textarea" placeholder="Hva oppdaget du, når skjedde det, og hva er konsekvensen? Jo mer konkret, jo sterkere brev."></textarea>
          </div>
          <div class="nav-kn">
            <button class="kn-tilbake" onclick="visSteg(2)">← Tilbake</button>
            <button class="kn-neste" onclick="nesteFra(3)">Neste →</button>
          </div>
        </div>
      </div>

      <!-- Steg 4 -->
      <div class="wizard-steg" id="steg-4" style="display:none">
        <div class="steg-kort">
          <div class="steg-nummer">Steg 4 av 6</div>
          <div class="steg-sporsmal">Når oppdaget du feilen — og visste selgeren om den?</div>
          <div class="steg-hint">Dette påvirker fristene dine og hva du kan kreve.</div>
          <div class="ig">
            <label for="oppdagelse">Dato du oppdaget feilen</label>
            <input type="date" id="oppdagelse" class="w-input">
          </div>
          <div class="ig" style="margin-top:20px">
            <label>Tror du selgeren visste om feilen da bilen ble solgt?</label>
            <div class="valg-grid" style="margin-top:8px">
              <button class="valg-kort" onclick="velg('selger_visste','ja',this)">Ja, trolig</button>
              <button class="valg-kort" onclick="velg('selger_visste','vet_ikke',this)">Vet ikke</button>
              <button class="valg-kort" onclick="velg('selger_visste','nei',this)">Nei, trolig ikke</button>
            </div>
          </div>
          <div class="nav-kn">
            <button class="kn-tilbake" onclick="visSteg(3)">← Tilbake</button>
            <button class="kn-neste" onclick="nesteFra(4)">Neste →</button>
          </div>
        </div>
      </div>

      <!-- Steg 5 -->
      <div class="wizard-steg" id="steg-5" style="display:none">
        <div class="steg-kort">
          <div class="steg-nummer">Steg 5 av 6</div>
          <div class="steg-sporsmal">Hva vil du kreve av selgeren?</div>
          <div class="steg-hint">Du kan endre kravet etter dialog. Velg det som passer best nå.</div>
          <div class="valg-grid" id="krav-grid">
            <button class="valg-kort" onclick="velg('krav','retting',this)">🔨 Retting av feilen</button>
            <button class="valg-kort" id="krav-omlevering" onclick="velg('krav','omlevering',this)">🔄 Bytte til annen bil</button>
            <button class="valg-kort" onclick="velg('krav','prisavslag',this)">💸 Prisavslag</button>
            <button class="valg-kort" onclick="velg('krav','heving',this)">🚫 Pengene tilbake (heving)</button>
          </div>
          <div class="nav-kn">
            <button class="kn-tilbake" onclick="visSteg(4)">← Tilbake</button>
            <button class="kn-neste" onclick="nesteFra(5)">Neste →</button>
          </div>
        </div>
      </div>

      <!-- Steg 6 -->
      <div class="wizard-steg" id="steg-6" style="display:none">
        <div class="steg-kort">
          <div class="steg-nummer">Steg 6 av 6</div>
          <div class="steg-sporsmal">Hvem er du, og hvem er selgeren?</div>
          <div class="steg-hint">Brukes bare i brevet. Ingenting lagres.</div>
          <div class="ig"><label for="mitt_navn">Ditt navn</label><input type="text" id="mitt_navn" class="w-input" placeholder="Ola Nordmann"></div>
          <div class="ig"><label for="mitt_tlf">Ditt telefonnummer</label><input type="tel" id="mitt_tlf" class="w-input" placeholder="400 00 000"></div>
          <div class="ig"><label for="min_epost">Din e-postadresse</label><input type="email" id="min_epost" class="w-input" placeholder="ola@eksempel.no"></div>
          <div class="ig" style="margin-top:20px"><label for="selger_navn">Selgerens navn eller firma</label><input type="text" id="selger_navn" class="w-input" placeholder="Kari Nordmann eller Bil AS"></div>
          <div class="nav-kn">
            <button class="kn-tilbake" onclick="visSteg(5)">← Tilbake</button>
            <button class="kn-neste" onclick="generer()">Lag reklamasjonsbrevet →</button>
          </div>
        </div>
      </div>
    </div>

    <!-- RESULTAT -->
    <div id="resultat-wrapper" style="display:none">
      <div id="vk" class="vurdering-kort"></div>
      <div class="brev-wrapper">
        <div class="brev-header no-print">
          <span class="brev-header-tittel">Ditt reklamasjonsbrev</span>
          <div class="brev-kn-wrapper">
            <button class="brev-kn brev-kn-kopi" onclick="kopier()">Kopier tekst</button>
            <button class="brev-kn brev-kn-print" onclick="window.print()">Skriv ut / PDF</button>
          </div>
        </div>
        <div class="brev-innhold" id="brev-innhold"></div>
      </div>
      <div class="neste-steg-boks no-print" id="neste-steg"></div>
      <button class="start-paa-nytt no-print" onclick="startNytt()">← Start på nytt</button>
    </div>

    <!-- SEO -->
    <div class="prose sp-body" style="margin-top:64px">
      <h2>Hva har du krav på når bilen har feil?</h2>
      <p>Kjøpte du bilen av en forhandler, gjelder forbrukerkjøpsloven. Du har 5 år til å reklamere (biler er varige varer), og du har 2 måneder på deg etter at du oppdaget feilen. De første 2 år er det selgeren som må bevise at feilen ikke forelå ved kjøpet.</p>
      <p>Kjøpte du av en privatperson, gjelder kjøpsloven. Du har 2 år absolutt frist og må reklamere innen rimelig tid — normalt noen uker — etter at du oppdaget feilen.</p>
      <h3>Hva kan du kreve?</h3>
      <p>Du kan kreve at feilen rettes, at bilen byttes (bare fra forhandler), prisavslag, eller at kjøpet heves og du får pengene tilbake. Heving krever at feilen er vesentlig. Du kan alltid kreve erstatning for konkrete tap i tillegg.</p>
      <h3>Visste selgeren om feilen?</h3>
      <p>Hvis selgeren kjente til feilen og holdt den skjult, bortfaller reklamasjonsfristen etter kjøpsloven § 33. Da kan du reklamere selv om lenger tid har gått. Det samme gjelder hvis selgeren har handlet i strid med god tro.</p>
      <p>Relaterte paragrafer: <a href="../../lover/kjopsloven/32/">§ 32 Reklamasjonsfrister</a> · <a href="../../lover/kjopsloven/39/">§ 39 Heving ved mangel</a> · <a href="../../lover/kjopsloven/25/">§ 25 Heving ved forsinkelse</a></p>
    </div>
  </div>
</main>

<script>
const D = {{}};

function velg(felt, verdi, el) {{
  D[felt] = verdi;
  el.closest('.valg-grid, [class*="valg-grid"]').querySelectorAll('.valg-kort').forEach(k => k.classList.remove('valgt'));
  el.classList.add('valgt');
  if (felt === 'selger_type') {{
    const omEl = document.getElementById('krav-omlevering');
    if (omEl) omEl.style.display = verdi === 'privat' ? 'none' : '';
  }}
}}

function visSteg(n) {{
  document.querySelectorAll('.wizard-steg').forEach(s => s.style.display = 'none');
  const el = document.getElementById('steg-' + n);
  if (el) el.style.display = 'block';
  const pct = Math.round((n-1)/6*100);
  document.getElementById('pfill').style.width = pct + '%';
  document.getElementById('ptekst').textContent = 'Steg ' + n + ' av 6';
  document.getElementById('wizard-wrapper').scrollIntoView({{behavior:'smooth',block:'start'}});
}}

function nesteFra(s) {{
  if (s===1 && !D.selger_type) {{ alert('Velg hvem du kjøpte av.'); return; }}
  if (s===2) {{
    const kd = document.getElementById('kjopsdato').value;
    const bd = document.getElementById('bil_besk').value.trim();
    if (!kd) {{ alert('Angi kjøpsdato.'); return; }}
    if (!bd) {{ alert('Beskriv bilen.'); return; }}
    D.kjopsdato = kd; D.bil_besk = bd;
    D.kjopsum = document.getElementById('kjopsum').value;
  }}
  if (s===3) {{
    const fd = document.getElementById('feil_besk').value.trim();
    if (!D.feil_kat) {{ alert('Velg kategori for feilen.'); return; }}
    if (!fd) {{ alert('Beskriv feilen.'); return; }}
    D.feil_besk = fd;
  }}
  if (s===4) {{
    const od = document.getElementById('oppdagelse').value;
    if (!od) {{ alert('Angi dato du oppdaget feilen.'); return; }}
    if (!D.selger_visste) {{ alert('Angi om selgeren kjente til feilen.'); return; }}
    D.oppdagelse = od;
  }}
  if (s===5 && !D.krav) {{ alert('Velg hva du vil kreve.'); return; }}
  visSteg(s+1);
}}

function formDato(iso) {{
  if (!iso) return '';
  return new Date(iso+'T12:00:00').toLocaleDateString('nb-NO',{{day:'numeric',month:'long',year:'numeric'}});
}}

function beregnFrister() {{
  const kjoep = new Date(D.kjopsdato+'T12:00:00');
  const oppdaget = new Date(D.oppdagelse+'T12:00:00');
  const naa = new Date();
  const ar = D.selger_type === 'forhandler' ? 5 : 2;
  const absolutFrist = new Date(kjoep);
  absolutFrist.setFullYear(absolutFrist.getFullYear()+ar);
  const innenAbsolutt = naa < absolutFrist;
  const dagerTil = Math.floor((absolutFrist-naa)/(864e5));
  const dagerSiden = Math.floor((naa-oppdaget)/(864e5));
  return {{ innenAbsolutt, dagerTil, ar, dagerSiden, absolutFrist }};
}}

function generer() {{
  D.mitt_navn  = document.getElementById('mitt_navn').value.trim()  || '[Ditt navn]';
  D.mitt_tlf   = document.getElementById('mitt_tlf').value.trim()   || '[Telefon]';
  D.min_epost  = document.getElementById('min_epost').value.trim()  || '[E-post]';
  D.selger_nav = document.getElementById('selger_navn').value.trim()|| '[Selgers navn]';

  const f = beregnFrister();
  const lov = D.selger_type === 'forhandler' ? 'forbrukerkjøpsloven' : 'kjøpsloven';
  const lovK = D.selger_type === 'forhandler' ? 'fkjl.' : 'kjl.';

  // Vurdering
  let vKlasse, vTittel, vPunkter;
  if (!f.innenAbsolutt) {{
    vKlasse = 'for-sent';
    vTittel = 'Den absolutte fristen er trolig utløpt';
    vPunkter = [
      {{i:'⛔', t:'Du kjøpte bilen for over '+f.ar+' år siden. Den absolutte fristen etter '+lov+' er '+f.ar+' år.'}},
      {{i:'⚠️', t:'Unntak: visste selgeren om feilen og holdt det skjult? Da kan fristen bortfalle. Kontakt oss.'}},
      {{i:'💡', t:'Har selgeren gitt garanti? Da gjelder garantiperioden i stedet for lovens frist.'}}
    ];
  }} else if (f.dagerSiden > 60 && D.selger_type === 'privat') {{
    vKlasse = 'advarsel';
    vTittel = 'Send brevet i dag — fristen er presset';
    vPunkter = [
      {{i:'⚠️', t:'Det har gått '+f.dagerSiden+' dager siden du oppdaget feilen. «Rimelig tid» er normalt noen uker — dette er lenge.'}},
      {{i:'✅', t:'Du er innenfor '+f.ar+'-årsfristen — '+f.dagerTil+' dager igjen.'}},
      {{i:'📋', t:'Kjøpsloven gjelder (kjøp fra privatperson). Send brevet nå og ta vare på bekreftelse.'}}
    ];
  }} else if (f.dagerSiden > 30) {{
    vKlasse = 'advarsel';
    vTittel = 'Send brevet snarest mulig';
    vPunkter = [
      {{i:'⏰', t:'Det har gått '+f.dagerSiden+' dager siden du oppdaget feilen. Ikke vent lenger.'}},
      {{i:'✅', t:'Du er innenfor den absolutte '+f.ar+'-årsfristen — '+f.dagerTil+' dager igjen.'}},
      {{i:'📋', t:lov.charAt(0).toUpperCase()+lov.slice(1)+' gjelder for kjøpet ditt.'}}
    ];
  }} else {{
    vKlasse = 'ok';
    vTittel = 'Du er godt innenfor fristene';
    vPunkter = [
      {{i:'✅', t:'Oppdaget feilen for '+f.dagerSiden+' dager siden — innenfor rimelig tid.'}},
      {{i:'✅', t:f.ar+'-årsfristen: '+f.dagerTil+' dager igjen.'}},
      {{i:'📋', t:lov.charAt(0).toUpperCase()+lov.slice(1)+' gjelder for kjøpet ditt.'}}
    ];
  }}

  const vEl = document.getElementById('vk');
  vEl.className = 'vurdering-kort '+vKlasse;
  vEl.innerHTML = '<div class="vurdering-tittel">'+vTittel+'</div><ul class="vurdering-liste">'+
    vPunkter.map(p=>'<li><span class="v-ikon">'+p.i+'</span><span>'+p.t+'</span></li>').join('')+'</ul>';

  // Krav-setning
  const kravMap = {{
    retting: D.selger_type==='forhandler'
      ? 'Jeg krever at mangelen rettes vederlagsfritt for meg, jf. forbrukerkjøpsloven § 29.'
      : 'Jeg krever at mangelen rettes vederlagsfritt for meg, jf. kjøpsloven § 34.',
    omlevering: 'Jeg krever omlevering — at bilen erstattes med en tilsvarende mangelfri bil, jf. forbrukerkjøpsloven § 29.',
    prisavslag: D.selger_type==='forhandler'
      ? 'Jeg krever prisavslag tilsvarende mangelens verdi, jf. forbrukerkjøpsloven § 31.'
      : 'Jeg krever prisavslag tilsvarende mangelens verdi, jf. kjøpsloven § 38.',
    heving: D.selger_type==='forhandler'
      ? 'Mangelen er etter min vurdering vesentlig. Jeg hever herved kjøpet, jf. forbrukerkjøpsloven § 32, og krever full tilbakebetaling av kjøpesummen'+(D.kjopsum?' kr '+parseInt(D.kjopsum).toLocaleString('nb-NO')+','':'')+' jf. forbrukerkjøpsloven § 49.'
      : 'Mangelen er etter min vurdering vesentlig. Jeg hever herved kjøpet, jf. kjøpsloven § 39, og krever full tilbakebetaling av kjøpesummen'+(D.kjopsum?' kr '+parseInt(D.kjopsum).toLocaleString('nb-NO')+','':'')+' jf. kjøpsloven § 64.'
  }};

  const vissteNote = D.selger_visste==='ja'
    ? '\n\nJeg gjør oppmerksom på at selgeren etter min vurdering kjente til denne feilen ved salget, jf. '+lovK+' § '+(D.selger_type==='forhandler'?'16':'33')+'. Reklamasjonsfristen gjelder ikke i slike tilfeller.'
    : '';

  const dagensDato = new Date().toLocaleDateString('nb-NO',{{day:'numeric',month:'long',year:'numeric'}});

  const brev =
D.mitt_navn+'\n'+
D.mitt_tlf+' | '+D.min_epost+'\n\n'+
dagensDato+'\n\n'+
'Til: '+D.selger_nav+'\n\n'+
'REKLAMASJON — '+(D.bil_besk||'bilkjøp')+'\n\n'+
'Jeg kjøpte '+(D.bil_besk||'bilen')+' den '+formDato(D.kjopsdato)+(D.kjopsum?' for kr '+parseInt(D.kjopsum).toLocaleString('nb-NO'):'')+'.'+'\n\n'+
'Den '+formDato(D.oppdagelse)+' oppdaget jeg følgende mangel:\n'+D.feil_besk+'\n\n'+
'Mangelen forelå etter min vurdering på tidspunktet for risikoens overgang, jf. '+lovK+' § '+(D.selger_type==='forhandler'?'14':'21')+'. Jeg reklamerer herved innen rimelig tid etter oppdagelsen, jf. '+lovK+' § '+(D.selger_type==='forhandler'?'27':'32')+'.'+vissteNote+'\n\n'+
(kravMap[D.krav]||'')+'\n\n'+
'Jeg ber om skriftlig svar innen 14 dager fra dags dato.\n\n'+
'Med vennlig hilsen\n\n'+
D.mitt_navn+'\n'+D.mitt_tlf+'\n'+D.min_epost;

  document.getElementById('brev-innhold').textContent = brev;

  // Neste steg
  const harHeving = D.krav === 'heving';
  const erForhandler = D.selger_type === 'forhandler';
  document.getElementById('neste-steg').innerHTML =
    '<h3>Hva gjør du nå?</h3><ol class="neste-steg-liste">'+
    '<li>Send brevet til selgeren på e-post med lesebekreftelse — eller rekommandert post. Ta vare på kvitteringen.</li>'+
    '<li>Sett en svarfrist på 14 dager i brevet. Da vet selgeren hva som gjelder.</li>'+
    (D.krav==='retting'?'<li>Gir selgeren beskjed om at han vil rette, gi ham rimelig tid. Men hold øye med at rettingen faktisk løser feilen.</li>':'')+
    (harHeving?'<li>Ikke bruk bilen mer enn nødvendig etter heving — videre bruk kan tolkes som at du aksepterer situasjonen.</li>':'')+
    '<li>Avviser selgeren kravet eller svarer ikke? '+(erForhandler?'Klage til Forbrukerrådet (gratis) er neste steg. Bruk forbrukerradet.no/klage.':'Ta saken til Forliksrådet på Altinn — gebyret er 1 215 kr og du kan kreve det dekket.')+' </li>'+
    '<li>Har du en komplisert sak eller trenger hjelp videre? <a href="mailto:rettsregel@gmail.com" style="color:var(--accent)">Send oss saken</a> — vi ser på den.</li>'+
    '</ol>';

  document.getElementById('wizard-wrapper').style.display = 'none';
  const rw = document.getElementById('resultat-wrapper');
  rw.style.display = 'block';
  setTimeout(()=>rw.scrollIntoView({{behavior:'smooth',block:'start'}}), 50);
}}

function kopier() {{
  const t = document.getElementById('brev-innhold').textContent;
  navigator.clipboard.writeText(t).then(()=>{{
    const k = document.querySelector('.brev-kn-kopi');
    k.textContent='Kopiert ✓'; setTimeout(()=>k.textContent='Kopier tekst',2000);
  }});
}}

function startNytt() {{
  Object.keys(D).forEach(k=>delete D[k]);
  document.getElementById('resultat-wrapper').style.display='none';
  document.getElementById('wizard-wrapper').style.display='block';
  document.querySelectorAll('.wizard-steg').forEach(s=>s.style.display='none');
  document.querySelectorAll('.valg-kort').forEach(k=>k.classList.remove('valgt'));
  document.getElementById('steg-1').style.display='block';
  document.getElementById('pfill').style.width='0%';
  document.getElementById('ptekst').textContent='Steg 1 av 6';
  document.getElementById('wizard-wrapper').scrollIntoView({{behavior:'smooth',block:'start'}});
}}
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

    # Kontrakter
    os.makedirs(f"{out}/kontrakter", exist_ok=True)
    with open(f"{out}/kontrakter/index.html", "w", encoding="utf-8") as f:
        f.write(render_kontrakter_hub())
    os.makedirs(f"{out}/kontrakter/husleiekontrakt", exist_ok=True)
    with open(f"{out}/kontrakter/husleiekontrakt/index.html", "w", encoding="utf-8") as f:
        f.write(render_kontrakter_husleiekontrakt())
    
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
