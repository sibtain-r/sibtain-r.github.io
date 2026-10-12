---
title: Classifying claim notes: BERT, ULMFiT and an ensemble
dek: Multi-class, multi-label, imbalanced, and served from a dockerized Flask app.
group: speech
band: b-navy
highlight: navy
where: Care Cloud (Islamabad)
when: 2019
tools: BERT, ULMFiT, PyTorch, Flask, Docker
featured: no
---

Insurance claim notes are short, messy and important. The task was to assign each message to the right categories.

## The setup
A multi-class, multi-label text classification problem across ten classes of message, built in 2019 at Care Cloud. The data was imbalanced, with a few common classes and a long tail of rare ones.

## The model
I fine-tuned a six-layer BERT model on the ten classes, and trained a ULMFiT model as well, then combined them in an ensemble neural network. BERT embeddings plus a custom layer handled the classification itself. ULMFiT is a method that pretrains a language model and then fine-tunes it with gradual unfreezing, and it gave a different view of the same text.

## Why an ensemble
Two models with different pre-training make different mistakes. A small network that learns how to combine their outputs often beats either alone.

## Imbalance
Rare classes are where the value is and where models fail. Options include class weights, resampling, and judging by per-class F1 rather than accuracy. Accuracy rewards a model for ignoring rare classes.

## Serving
The model was served from a dockerized Flask application on a Linux server.

## Lessons
- Report per-class metrics. A single number hides the classes you care about.
- A smaller model, such as a six-layer BERT, is much cheaper to serve.
- Ensembles cost latency, so check you can afford it.
