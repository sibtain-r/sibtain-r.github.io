---
title: Redacting personal data from PDFs with OCR and layout models
dek: GDPR turns documents into liabilities. Finding and masking the personal data automatically.
group: doc
band: b-navy
highlight: navy
where: VisionX (Islamabad)
when: 2020 to 2021
tools: OCR, Text detection, LayoutLMv2, PyTorch
featured: yes
---

Privacy law turns documents into liabilities. GDPR requires that personal data is handled carefully, and a pile of invoices, passports, resumes and pay stubs is full of it.

## The goal
Find personal data in documents and mask it, automatically. The documents I worked with included invoices, receipts, passports, resumes and pay stubs, financial and healthcare documents alike.

## The pipeline
1. OCR and text detection locate every piece of text and its bounding box on the page.
2. A layout-aware transformer, such as LayoutLMv2, classifies what each piece is: name, address, ID number, amount.
3. Pieces classified as personal data are masked by covering those exact coordinates in the output.

## Why detection quality is the whole game
A missed name is a privacy failure. A masked total is a usability failure. The two errors are not equally costly, so I would tune for recall on personal-data classes and accept some over-redaction.

## Details that bite
- Redaction must remove the data, not just cover it. If the original text layer survives under a black box, the document is not redacted.
- Scans and digital PDFs behave differently, and many are a mix.
- Names and addresses vary across countries and scripts.

## What it is not
Automated redaction reduces effort and risk, but high-stakes documents still deserve a human review of the result.
