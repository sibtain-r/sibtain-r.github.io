---
title: A voice bot for insurance calls: speech in, classifier, Tacotron 2 out
dek: Three modules, a trained voice, and the failure modes of phone bots.
group: speech
band: b-olive
highlight: olive
where: Care Cloud (Islamabad)
when: 2019
tools: Tacotron 2, Rasa Core, Rasa NLU, Text classification
featured: no
---

Insurance companies get a flood of phone calls, and many are the same few questions. In 2019 I built a voice bot to answer them.

## Three modules
1. **Voice to text** transcribes the caller.
2. **A text classifier** works out what they are asking.
3. **Text to speech** answers in a natural voice.

Keeping them separate meant each could be improved or replaced independently.

## Training a voice
For text to speech, I trained Tacotron 2 on the M-AILABS dataset. Tacotron 2 is a sequence-to-sequence model that predicts a spectrogram from text, and a vocoder turns the spectrogram into audio. I exposed it as a text-to-speech API so other services could use it.

## The flow around it
I also built automated IVR call flows with Rasa Core and Rasa NLU, which handle intent detection and dialogue management for the conversations.

## What phone bots punish
- Latency. Silence on a call feels like an error.
- Recognition mistakes. The classifier needs to cope with a wrong word or two.
- Escalation. A bot that cannot help should hand the caller to a person quickly.

## Lessons
Voice interfaces are a pipeline of fallible parts. Design for the failure of each one, and log enough to see which part failed.
