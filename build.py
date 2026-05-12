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

PARAGRAPHS = _P_BASE + _P_KJOPSLOVEN + _P_HUSLEIELOVEN + _P_AVHENDINGSLOVA

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
  --bg: #FAF6EE;
  --bg-alt: #F2EBDD;
  --bg-card: #FFFCF6;
  --ink: #1F1A14;
  --ink-soft: #5A4F40;
  --ink-mute: #8A7F70;
  --accent: #C25434;
  --accent-deep: #A8451F;
  --accent-soft: #E8B5A3;
  --line: rgba(31, 26, 20, 0.12);
  --line-strong: rgba(31, 26, 20, 0.22);
  --shadow-sm: 0 1px 3px rgba(31, 26, 20, 0.06), 0 1px 2px rgba(31, 26, 20, 0.04);
  --shadow-md: 0 4px 12px rgba(31, 26, 20, 0.08), 0 2px 4px rgba(31, 26, 20, 0.04);
  --shadow-lg: 0 12px 32px rgba(31, 26, 20, 0.10), 0 4px 8px rgba(31, 26, 20, 0.04);
  --kat-bolig: #4F6F5E;
  --kat-forbruk: #C25434;
  --kat-arbeid: #6B5B95;
  --kat-familie: #B8654A;
  --kat-gjeld: #7A6E5D;
  --kat-tjenester: #4E6E80;
  --serif: 'Newsreader', Georgia, serif;
  --sans: 'Manrope', system-ui, sans-serif;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  background: var(--bg); color: var(--ink); font-family: var(--sans);
  font-size: 17px; line-height: 1.6; -webkit-font-smoothing: antialiased;
  position: relative;
}
body::before {
  content: ''; position: fixed; inset: 0; pointer-events: none; z-index: 100; opacity: 0.35;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.12 0 0 0 0 0.1 0 0 0 0 0.08 0 0 0 0.18 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
.container { max-width: 1200px; margin: 0 auto; padding: 0 32px; }
.narrow { max-width: 740px; margin: 0 auto; padding: 0 32px; }

nav.site-nav { padding: 32px 0; display: flex; justify-content: space-between; align-items: center; }
.logo {
  font-family: var(--serif); font-weight: 400; font-size: 32px; letter-spacing: -0.025em;
  color: var(--ink); text-decoration: none; font-variation-settings: "opsz" 48;
  line-height: 1;
}
.logo span { color: var(--accent); font-style: italic; }
.nav-links { display: flex; gap: 36px; list-style: none; }
.nav-links a { color: var(--ink-soft); text-decoration: none; font-size: 15px; font-weight: 500; transition: color 0.2s; }
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

/* Footer */
footer.site-footer { background: var(--ink); color: var(--bg); padding: 64px 0 32px; }
.footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 60px; margin-bottom: 48px; }
@media (max-width: 700px) { .footer-grid { grid-template-columns: 1fr; gap: 32px; } }
.footer-brand {
  font-family: var(--serif); font-size: 32px; font-weight: 400; letter-spacing: -0.015em;
  margin-bottom: 12px; font-variation-settings: "opsz" 72;
}
.footer-brand span { color: var(--accent-soft); }
.footer-tagline { color: rgba(250,246,238,0.6); font-size: 15px; max-width: 320px; line-height: 1.5; }
footer.site-footer h4 {
  font-family: var(--sans); font-size: 12px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.12em; color: var(--accent-soft); margin-bottom: 18px;
}
footer.site-footer ul { list-style: none; }
footer.site-footer li { margin-bottom: 10px; }
footer.site-footer a {
  color: rgba(250,246,238,0.7); text-decoration: none; font-size: 15px; transition: color 0.2s;
}
footer.site-footer a:hover { color: var(--bg); }
.footer-bottom {
  padding-top: 24px; border-top: 1px solid rgba(250,246,238,0.1);
  font-size: 13px; color: rgba(250,246,238,0.5);
  display: flex; justify-content: space-between; flex-wrap: wrap; gap: 16px;
}

/* Index page (lov overview) */
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

/* Hero — store editorial titler med kicker */
.sp-hero {
  max-width: 880px; padding: 64px 0 32px;
  position: relative;
}
.sp-hero .kicker {
  font-family: var(--sans); font-size: 13px;
  letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--accent); font-weight: 600;
  margin-bottom: 24px; display: inline-block;
  padding-bottom: 6px; border-bottom: 2px solid var(--accent);
}
.sp-hero .breadcrumb {
  font-family: var(--sans); font-size: 13px;
  color: var(--ink-mute); margin-bottom: 24px;
  letter-spacing: 0.04em;
}
.sp-hero .breadcrumb a {
  color: var(--ink-mute); text-decoration: none;
  border-bottom: 1px solid transparent; transition: border-color 0.2s, color 0.2s;
}
.sp-hero .breadcrumb a:hover {
  color: var(--accent); border-bottom-color: var(--accent);
}
.sp-hero h1 {
  font-family: var(--serif); font-weight: 500;
  font-size: clamp(26px, 3vw, 40px); line-height: 1.15;
  letter-spacing: -0.015em; color: var(--ink);
  font-variation-settings: "opsz" 48;
  margin: 0; max-width: 760px;
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
  max-width: 880px; padding: 80px 0 40px;
}
.sphub-hero .kicker {
  font-family: var(--sans); font-size: 12px;
  letter-spacing: 0.16em; text-transform: uppercase;
  color: var(--accent); font-weight: 700;
  margin-bottom: 16px; display: block;
}
.sphub-hero h1 {
  font-family: var(--serif); font-weight: 500;
  font-size: clamp(32px, 3.5vw, 44px); line-height: 1.1;
  letter-spacing: -0.02em; margin: 0 0 16px;
  font-variation-settings: "opsz" 48;
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
  max-width: 880px; padding: 80px 0 40px;
}
.lover-hero .kicker {
  font-family: var(--sans); font-size: 12px;
  letter-spacing: 0.16em; text-transform: uppercase;
  color: var(--accent); font-weight: 700;
  margin-bottom: 16px; display: block;
}
.lover-hero h1 {
  font-family: var(--serif); font-weight: 500;
  font-size: clamp(32px, 3.5vw, 44px); line-height: 1.1;
  letter-spacing: -0.02em; margin: 0 0 16px;
  font-variation-settings: "opsz" 48;
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
   Hjemmeside — redesigned editorial layout
   ============================================================ */
.home-hero-v2 {
  padding: 80px 0 56px;
  max-width: 1100px;
}
.home-hero-v2 .kicker {
  font-family: var(--sans); font-size: 12px;
  letter-spacing: 0.16em; text-transform: uppercase;
  color: var(--accent); font-weight: 700;
  margin-bottom: 20px; display: block;
}
.home-hero-v2 h1 {
  font-family: var(--serif); font-weight: 500;
  font-size: clamp(36px, 4.5vw, 60px); line-height: 1.05;
  letter-spacing: -0.025em; margin: 0;
  font-variation-settings: "opsz" 60;
  max-width: 880px;
}
.home-hero-v2 h1 em {
  font-style: italic; color: var(--accent);
  font-weight: 400;
}
.home-hero-v2 .lead {
  font-family: var(--sans); font-size: 18px;
  line-height: 1.55; color: var(--ink-soft);
  margin: 24px 0 0; max-width: 580px;
}
.home-hero-v2 .cta-row {
  display: flex; gap: 14px; margin-top: 36px;
  flex-wrap: wrap;
}

/* Stats-band under hero */
.home-stats {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 24px; padding: 36px 0;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
  margin-bottom: 64px;
}
.home-stat .num {
  font-family: var(--serif); font-size: 36px;
  font-weight: 500; line-height: 1; color: var(--accent);
  letter-spacing: -0.02em; font-variation-settings: "opsz" 48;
}
.home-stat .lbl {
  font-family: var(--sans); font-size: 12px;
  letter-spacing: 0.1em; text-transform: uppercase;
  color: var(--ink-soft); margin-top: 8px;
}

/* Section headers — strammere */
.home-section-v2 {
  margin: 64px 0;
}
.home-section-head-v2 {
  display: flex; align-items: baseline; justify-content: space-between;
  margin-bottom: 28px; flex-wrap: wrap; gap: 16px;
  padding-bottom: 16px; border-bottom: 1px solid var(--line-strong);
}
.home-section-head-v2 .left .kicker {
  font-family: var(--sans); font-size: 11px;
  letter-spacing: 0.16em; text-transform: uppercase;
  color: var(--accent); font-weight: 700;
  margin-bottom: 6px;
}
.home-section-head-v2 h2 {
  font-family: var(--serif); font-size: clamp(24px, 2.8vw, 32px);
  font-weight: 500; letter-spacing: -0.015em; line-height: 1.15;
  margin: 0; color: var(--ink);
}
.home-section-head-v2 .right a {
  font-family: var(--sans); font-size: 13px;
  color: var(--accent); font-weight: 600;
  text-decoration: none; display: inline-flex; gap: 6px;
  border-bottom: 1px solid transparent; padding-bottom: 2px;
  transition: border-color 0.2s;
}
.home-section-head-v2 .right a:hover { border-bottom-color: var(--accent); }

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
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}styles.css">
</head>
<body>"""

def site_nav(depth=0):
    prefix = "../" * depth
    return f"""<div class="container">
<nav class="site-nav">
  <a href="{prefix}" class="logo">Retts<span>regel</span></a>
  <ul class="nav-links">
    <li><a href="{prefix}sporsmal/">Vanlige spørsmål</a></li>
    <li><a href="{prefix}lover/">Alle lover</a></li>
    <li><a href="{prefix}om/">Om</a></li>
    <li><a href="{prefix}#skjema">Send inn sak</a></li>
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
    <div class="footer-grid">
      <div>
        <div class="footer-brand">Retts<span>regel</span></div>
        <p class="footer-tagline">Lover forklart for vanlige folk. En paragraf om gangen.</p>
      </div>
      <div>
        <h4>Innhold</h4>
        <ul>
          <li><a href="{prefix}lover/">Alle lover</a></li>
          <li><a href="{prefix}lover/angrerettloven/">Angrerettloven</a></li>
        </ul>
      </div>
      <div>
        <h4>Nettstedet</h4>
        <ul>
          <li><a href="{prefix}om/">Om Rettsregel</a></li>
          <li><a href="{prefix}#skjema">Send inn sak</a></li>
          <li><a href="{prefix}personvern/">Personvern</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Rettsregel</span>
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
    """Om-siden."""
    depth = 1
    return f"""{shared_head('Om Rettsregel', 'Norske lover, forklart for folk. Slik bygger vi Rettsregel.', depth=1, canonical_path='/om/')}
{site_nav(depth=1)}

<div class="container">
  <article class="om-article">
    <header class="om-header">
      <h1>Norske lover,<br><em>forklart for folk.</em></h1>
    </header>

    <section class="om-section">
      <p class="om-lead">Loven angår alle. Men den er skrevet for jurister.</p>
      <p>Rettsregel tar en paragraf om gangen og oversetter den til vanlig norsk. Med eksempler du kjenner deg igjen i. Vanlige feil folk gjør. Og hva du faktisk skal gjøre hvis du står i det.</p>
    </section>

    <section class="om-section">
      <h2>Hvordan</h2>
      <p>Vi bruker avansert språkteknologi bygget på deep learning og store språkmodeller til å skrive første utkast, og jurister til å gjennomgå. Det gir oss to ting på en gang: omfang og presisjon. En enkeltperson kunne ikke skrevet en hel lov. En maskin alene kunne ikke gjort det riktig. Sammen kan vi.</p>
    </section>

    <section class="om-section">
      <h2>Hvorfor</h2>
      <p>Tenk fra bunnen: hvorfor må noen betale for å forstå reglene de allerede må forholde seg til? Det finnes ikke en god grunn. Bare en gammel grunn.</p>
      <p>Teknologien finnes nå til å gjøre det annerledes. Så vi gjør det.</p>
    </section>

    <section class="om-section om-cta">
      <a href="../#skjema" class="cta-button">Har du en sak? Skriv til oss →</a>
    </section>
  </article>
</div>

{contact_form(depth=1)}
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
    <h1>Lover er ikke <em>vanskelige</em>.<br>De er bare <em>dårlig forklart</em>.</h1>
    <p class="lead">Vi tar paragraf for paragraf og oversetter til vanlig norsk. Med eksempler, vanlige feil, og hva du faktisk skal gjøre når det skjer noe.</p>
    <div class="cta-row">
      <a href="#skjema" class="cta-button">Har du en sak? Skriv til oss →</a>
      <a href="{prefix}sporsmal/" class="cta-button-secondary">Vanlige spørsmål</a>
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
      <div class="lbl">Vanlige spørsmål</div>
    </div>
  </div>

  <section class="home-section-v2">
    <div class="home-section-head-v2">
      <div class="left">
        <div class="kicker">Vanlige spørsmål</div>
        <h2>Når noe har skjedd — hva nå?</h2>
      </div>
      <div class="right">
        <a href="{prefix}sporsmal/">Se alle spørsmål →</a>
      </div>
    </div>
    <div class="sphub-grid">{sporsmal_cards}
    </div>
  </section>

  <section class="home-section-v2">
    <div class="home-section-head-v2">
      <div class="left">
        <div class="kicker">Utvalgte paragrafer</div>
        <h2>Det folk faktisk søker</h2>
      </div>
    </div>
    <div class="sphub-grid">{cards_html}
    </div>
  </section>

  <section class="home-section-v2">
    <div class="home-section-head-v2">
      <div class="left">
        <div class="kicker">Lovsamling</div>
        <h2>Bla i alle lover</h2>
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
    
    # paragraphs-index.json — kompakt indeks for chatbot
    # Inneholder bare metadata som boten trenger for å klassifisere problemer
    index = []
    for p in PARAGRAPHS:
        index.append({
            "number": p["number"],
            "lov": p["lov"],
            "lov_display": p["lov_display"],
            "title": p["title"],
            "kort_svar": p.get("kort_svar", ""),
            "kategori": p.get("kategori", ""),
        })
    with open(f"{out}/paragraphs-index.json", "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=None, separators=(",", ":"))
    
    print(f"Built {len(PARAGRAPHS)} paragraph pages + {len(SPORSMAL)} sporsmal-artikler + homepage + lov index + lover index + personvern + om")
    print(f"Plus: sitemap.xml ({len(urls)} URLs), robots.txt, CNAME, paragraphs-index.json")
    print(f"Output: {out}")

if __name__ == "__main__":
    build()
