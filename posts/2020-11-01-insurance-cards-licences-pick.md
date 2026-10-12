---
title: Insurance cards and driving licences: Tesseract meets a graph model
dek: Small rectangles, endless layouts. Why PICK reads cards better than rules do.
group: doc
band: b-olive
highlight: olive
where: VisionX (Islamabad)
when: 2020 to 2021
tools: Tesseract OCR, PICK, PyTorch
featured: no
---

Insurance cards and driving licences look simple: a handful of fields on a small rectangle. In practice every issuer has its own layout, fonts and photo placement.

## The approach
I combined Tesseract OCR with a PICK model. Tesseract reads the text and gives the position of each piece. PICK decides what each piece means.

## What PICK does
PICK is a graph-learning approach to key information extraction. Treat each text segment as a node in a graph, connect nodes by their spatial relationships, and let a graph convolutional network learn how neighbors inform each other. A number beside the word "ID" is probably an identifier. The same number elsewhere is not. This captures layout in a way that reading the text left to right cannot.

## Why not rules
Rule-based extraction, such as "take the line under the label", breaks the moment a new issuer's card arrives. A learned model generalizes to layouts it has not seen, as long as the training set reflects the variety.

## What made it work
- Tesseract's output was good enough as an input but never perfect, so the model has to tolerate OCR noise.
- Training data needed variety of issuers, not just volume.
- Cards contain personal data, so storage and logging have to be handled with care.

## Where it fits
This was part of VisionX's wider document-extraction work, alongside invoices, receipts and parcels.
