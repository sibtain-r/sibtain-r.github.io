---
title: Urdu OCR: a conv-GRU-CTC model trained on synthetic data
dek: A right-to-left, connected script and no dataset, so I made one.
group: doc
band: b-olive
highlight: olive
where: Personal project
when: July to August 2019
tools: Convolutional network, GRU, CTC loss, Synthetic data
featured: no
---

Urdu is written right to left in a flowing, connected script, and it has historically had far less OCR tooling than English. In 2019 I built an Urdu OCR model.

## Architecture
A convolutional front end extracts visual features from a line of text. A GRU reads those features as a sequence. Connectionist Temporal Classification (CTC) loss lets the model learn to output characters without needing each character located in the image, which is essential when letters join.

## The dataset problem
Labeled Urdu text images were scarce, so I made the dataset myself using synthetic data generation. Render text in a range of fonts, sizes and backgrounds, add noise and distortion, and you get unlimited labeled examples.

## What synthetic data can and cannot do
It is excellent for covering variety and for volume. It cannot fully reproduce real scans, so check on real images before trusting any number.

## Lessons
- For scripts with shaping and joining, character-level CTC models are a natural fit.
- Synthetic data is a starting point. Mix in real examples as soon as you have them.
- Fonts are your annotation budget, and diversity of fonts decides how well the model generalizes.
