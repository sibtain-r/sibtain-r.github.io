---
title: Deep Speech on medical audio: from sound to codes
dek: Speech recognition, a language model on top, and information extraction from transcripts.
group: speech
band: b-olive
highlight: olive
where: Care Cloud (Islamabad)
when: 2018 to 2020
tools: Deep Speech, PyTorch, Wav2vec, spaCy, BERT, DistilBERT, BART
featured: no
---

Doctors speak faster than they type. Speech recognition on medical audio was one of the first serious problems I worked on, at Care Cloud.

## Deep Speech
I worked with the PyTorch implementation of Deep Speech, an end-to-end speech recognition model trained with CTC loss, and trained and fine-tuned it on audio of medical notes. I also annotated audio from IVR (interactive voice response) calls.

## A language model on top
Acoustic models hear sounds. They do not know which words are likely. I added a statistical language model on top of Deep Speech, so decoding prefers plausible word sequences. In medicine that matters, because the vocabulary is full of terms that sound alike.

## From transcript to information
A transcript is not yet useful. I analyzed it with spaCy and a text classifier to extract relevant information from the calls. My work with medical dictation also used Wav2vec, and transformers like BERT, DistilBERT and BART to extract medical entities such as ICD-10 codes, procedure codes and SNOMED CT concepts from raw transcripts.

## An earlier cousin
Before Deep Speech, I trained a convolutional-recurrent speech-to-text model to transcribe voice commands for a chatbot, in 2018.

## Lessons
- Annotation is the bottleneck. Clean transcripts of domain audio are worth more than a bigger model.
- Domain vocabulary should be modeled, not hoped for.
- Measure what the downstream task needs, not just word error rate.
