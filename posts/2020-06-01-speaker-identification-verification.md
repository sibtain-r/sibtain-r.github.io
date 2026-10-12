---
title: Voices as identity: from Gaussian mixtures to GE2E
dek: Speaker identification in 2018, speaker verification behind a REST API in 2020.
group: speech
band: b-navy
highlight: navy
where: Personal project and VisionX
when: 2018 to 2020
tools: GMM, GE2E loss, PyTorch, Docker, Flask
featured: no
---

A voice is a biometric you carry everywhere. Two of my projects dealt with it: speaker identification in 2018 and speaker verification in 2020.

## Identification versus verification
- **Identification** asks: which of these known speakers is talking?
- **Verification** asks: is this person who they claim to be?

Identification is a classification problem. Verification is a matching problem, and it has to work for speakers the system never saw in training.

## Speaker identification
I classified the voices of different speakers using Gaussian mixture models (GMMs) and deep learning. A GMM models the distribution of a speaker's acoustic features, and you classify new audio by asking which speaker's model explains it best. Deep networks learn the features themselves.

## Speaker verification
To verify a user on a phone call by their voice, I used the Generalized End-to-End (GE2E) loss in PyTorch to learn speaker embeddings. Training batches contain several speakers with several utterances each. The loss pulls each utterance towards the center of its own speaker and pushes it away from the others. At test time you compare the embedding of the incoming voice with the stored one, and a threshold makes the decision.

## Putting it behind an API
I completed the cloud architecture for a REST API around the verification model, with Docker and Flask, so applications could call it.

## Lessons
- The threshold is a business decision. Raising it blocks fraud and annoys real users.
- Phone audio is narrow-band and noisy, so train on audio that looks like production.
- Voice is sensitive data. Store embeddings with the same care as passwords.
