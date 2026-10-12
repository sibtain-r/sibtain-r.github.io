---
title: Hercule: turning audio, video, images and PDFs into answers
dek: One destination for four very different formats: text plus structure, and a chatbot on top.
group: now
band: b-maroon
highlight: maroon
where: HighPlains Computing (Los Angeles, remote)
when: 2023 to 2025
tools: Whisper, Qwen vision-language model, AWS Textract, ChromaDB, AWS Bedrock, LangGraph
featured: yes
---

Hercule is an analytics platform for law enforcement. It ingests audio, video, images and PDF documents and turns them into structured data that a chatbot can answer questions about.

## Four formats, one destination
Evidence arrives in formats that have nothing in common. The trick is to give every format the same destination: text plus structure.

- **Audio** goes through self-hosted Whisper for speech-to-text.
- **Images and documents** go through a Qwen vision-language model for understanding, and AWS Textract for structured extraction from forms and tables.
- **Video** brings the two together: what is said and what is shown.
- **PDFs** may be scanned pages or digital documents, so they need both text extraction and layout awareness.

## Structure first, then search
The extracted content does two jobs. The structured fields are stored in a database, where they can be filtered and counted. The extracted text feeds a retrieval-augmented generation (RAG) system built on ChromaDB, with embeddings from AWS Bedrock models, so questions about meaning can be answered from the right passages.

## A chatbot built as a graph
The front door is a chatbot built with LangGraph. A graph makes the control flow explicit: decide what kind of question this is, retrieve, answer, and know when to stop. That is easier to debug than a free-running agent loop, which matters when the people asking need dependable answers.

## Why self-host the models
When the material is sensitive, running speech and vision models yourself is a common choice because it keeps the content under your control. It also gives you control over cost and throughput, which matters when you process batches of long recordings.

## Lessons for anyone building multimodal RAG
- Keep provenance. Every chunk should point back to its source file and, for audio and video, its position in time.
- Normalize before you embed. Clean text retrieves better than raw output.
- Make ingestion repeatable. Re-running a file must not create duplicates.
- Treat extraction quality as a product feature, because retrieval can only be as good as what was extracted.
