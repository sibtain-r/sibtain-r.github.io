---
title: Text normalization with deep learning: my final-year project
dek: How written text becomes something a speech system can say.
group: start
band: b-black
highlight: olive
where: FAST-NUCES (Islamabad)
when: July 2017 to May 2018
tools: Neural networks, Sequence models, Speech synthesis, Speech recognition
featured: no
---

My final-year project at FAST-NUCES was text normalization using deep learning.

## What text normalization is
Speech systems need words, not symbols. A text-to-speech system must turn "$5.20" into "five dollars and twenty cents", and "3/4" into "three quarters" or "March fourth" depending on context. Speech recognition has the inverse problem. Normalization sits at the front of one and the end of the other.

## The traditional approach
Hand-written rules. They work and they are painful: every language, every format and every exception is another rule.

## Neural approaches
The project normalized text for speech synthesis and speech recognition using several neural network architectures, and compared them. Sequence models read the written form and write the spoken form.

## The danger
A neural model can produce a fluent but wrong expansion, such as reading a number incorrectly. In speech systems that error is audible, so the best designs combine a model with checks or rules.

## Why it mattered to me
It was my first end-to-end deep-learning project. It pointed me towards the speech work that followed.
