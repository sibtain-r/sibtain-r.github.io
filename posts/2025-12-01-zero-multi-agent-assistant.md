---
title: Building Zero: a multi-agent assistant for sensitive records
dek: What it takes to make an AI assistant that officers and managers can rely on, told as principles rather than a design document.
group: now
band: b-now
highlight: olive
where: TargetZero (USA, remote)
when: August 2025 to now
tools: Pydantic AI, AWS Bedrock (Claude), FastAPI, Redis Streams, Server-Sent Events, LanceDB, PostgreSQL
featured: yes
---

Zero is an AI assistant for law-enforcement officers and managers. Instead of searching several systems, they ask questions in plain language: who was the victim in an incident, where did it happen, was force used, which vehicle was involved. Zero answers from the records.

Zero is a client's product, so this post stays at the level of principles. The specifics belong to them. The lessons about building assistants for sensitive records belong to everyone.

## Why more than one prompt
A question about an incident can need a structured lookup, a search through free-text narratives, or both. Splitting that work across cooperating agents with clear responsibilities is easier to test than one giant prompt that tries to do everything. I used Pydantic AI because typed tools and validated outputs mean a malformed answer fails loudly instead of quietly reaching a user.

## Getting data in without uploads
Nobody should have to upload files to ask a question. Zero uses connectors that synchronize data from the dispatch system, the jail management system and the law-enforcement records system into its own database. Once the data is there, the assistant is just another reader of it.

## Searching narratives by meaning
Narratives are free text, and officers rarely phrase a question the way a report was written. Semantic search closes that gap. Narrative text is embedded with Amazon Titan models through AWS Bedrock and stored in LanceDB, so the assistant can retrieve passages by meaning and ground its answer in them.

## Sessions that survive a bad connection
Answers stream to the user as they are generated. A dropped connection should not mean a lost answer, or a second model call that you pay for twice. I built the streaming layer on Redis Streams and Server-Sent Events so a client can reconnect and carry on.

## Treating context as a budget
Long conversations eventually collide with the model's context window and with your cost target. Zero manages what stays in context, so conversations remain coherent without dragging every old tool result along.

## Trust is the real feature
In this domain a confident wrong answer is worse than no answer. Most of the engineering effort went into parts users never see:

- Access control that fails closed, because a multi-tenant system must not leak across tenants.
- Guardrails that screen inputs for prompt-injection attempts before they reach the model.
- An evaluation framework that pairs automated regression checks with LLM-based grading, so a prompt change cannot quietly make things worse.
- Audit logging, cost tracking and tracing, so every answer can be explained afterwards.

## What I would tell a team starting out
Write the evaluations early. Decide what the assistant must refuse before deciding what it should answer. And measure cost per conversation from the first week, because it shapes every other design choice.
