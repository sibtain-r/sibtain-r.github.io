---
title: Reading receipts in English and Arabic, then reading thousands of templates
dek: From ReceiptX for Dubai Mall invoices to a 0.92 F1 field-level extraction pipeline.
group: doc
band: b-maroon
highlight: maroon
where: VisionX (Islamabad)
when: 2020 to 2021
tools: OCR, LayoutLM, LayoutLMv2, LayoutLMv3, PyTorch, AWS SageMaker
featured: no
---

One of my first projects at VisionX was ReceiptX for Emaar: pulling data out of invoices from Dubai Mall.

## What had to come out
- Store name
- Date and time
- Invoice total
- Total number of items purchased
- Line items: description in English and Arabic, quantity, and price in AED

## The pipeline
Image preprocessing came first. Then text detection to get the text and its bounding boxes. Then a transformer-based model that combines the text, the boxes and the image, which is how LayoutLM-style models work.

## Why layout matters
A total is not just a number. It is a number in a certain place, near certain words. Plain text models lose that. Layout-aware models see where each word sits, so they can tell a price from a quantity.

## Two scripts on one page
Receipts that mix English and Arabic add right-to-left text and bilingual descriptions on the same line. The detection step and the model both have to cope.

## From one client to a pipeline
The same approach grew into a custom MLOps pipeline for key-information extraction from invoices and receipts. With LayoutLMv2 and LayoutLMv3 it reached a 0.92 F1-score at field level across thousands of image templates. A new template should not need new code. That is the real measure of a document pipeline.

## Lessons
- Measure at the field level. A model can look good on tokens and still get the total wrong.
- Preprocessing is not optional. Skew, blur and low contrast cost accuracy before the model ever sees the page.
- Watch templates the model has never seen. Generalization is the whole point.
