---
title: My first chatbot: a contextual EHR assistant
dek: Intent detection, an LSTM for context, and later Rasa Core.
group: speech
band: b-olive
highlight: olive
where: Care Cloud (Islamabad)
when: 2018 to 2020
tools: LSTM, Rasa Core, Rasa NLU, Flask, SQLAlchemy
featured: no
---

My first project at Care Cloud, in 2018, was a contextual chatbot for electronic health records.

## What contextual means
A user asks "show me her last visit", and then "and the medications?" The second question only makes sense with the first in mind. A chatbot that handles each message alone cannot follow a conversation.

## Intent and context
I built it from two parts: intent detection, to decide what the user wants, and an LSTM to manage the context of the conversation.

## Growing up
Later I used Rasa Core and Rasa NLU for the EHR virtual assistant and for IVR call flows. Rasa gives you proper dialogue management, with stories, slots and policies, instead of one-off code for each conversation.

## The plumbing
Chatbots need data. I developed REST APIs with Flask as microservices that fetch data from the database via SQLAlchemy and update records.

## Lessons
- Healthcare users will test the edges, so plan for "I don't understand" with a useful fallback.
- Keep NLU and business logic apart. The first changes weekly and the second should not.
- Never let a chatbot change a record without confirming.
