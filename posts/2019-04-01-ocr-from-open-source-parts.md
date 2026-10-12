---
title: Building OCR from parts: an English pipeline and a Conv-BiLSTM-CTC recognizer
dek: Before big pretrained models, OCR was something you assembled.
group: doc
band: b-olive
highlight: olive
where: Personal projects
when: 2019
tools: Open-source OCR modules, Convolutional network, BiLSTM, CTC loss
featured: no
---

Before big pretrained models, OCR was something you assembled. Two of my early projects were exactly that.

## An English OCR pipeline
I created a pipeline for English OCR using open-source modules, plus custom components I wrote to fill the gaps: image in, text out.

## Training a text recognizer
In 2019 I trained a Convolution-BiLSTM-CTC model for text recognition from images. The convolutional layers read the visual features, the bidirectional LSTM reads them as a sequence in both directions, and CTC loss aligns the output characters with the image without requiring character-level annotation.

## Detection and recognition are two problems
Finding where text is and reading what it says are separate tasks. Pipelines usually detect first, crop, and then recognize each crop. Mistakes in the first step flow into the second.

## What I learned
- Preprocessing such as deskewing, binarization and resizing often gives a bigger gain than a fancier model.
- A pipeline is only as good as its weakest stage, so evaluate each stage on its own.
- Understanding these parts made me far better at using modern OCR and layout models later.
