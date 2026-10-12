---
title: An email generator on GPT-J: templates, prompts and a person in the loop
dek: More than 15 condition-based templates for cold emails, introductions and subject lines.
group: llm
band: b-navy
highlight: navy
where: AI Bees (Hamburg, remote)
when: September 2021 to February 2022
tools: GPT-J, GPT-Neo, LangChain, Prompt engineering
featured: no
---

In 2021 I built an email generator for the marketing team at AI Bees, using a self-hosted GPT-J model and prompt engineering.

## What it made
Cold emails, introductory messages for sales and marketing campaigns, and subject lines. More than 15 different condition-based text-generation templates were created.

## Why templates
A language model asked to "write a cold email" produces something different every time. Condition-based templates fix the structure and let the model fill in the parts that should vary: the audience, the offer and the tone. The result is output a marketer can predict and review.

## Prompt engineering in practice
- Show the model examples of the format you want.
- Put the conditions in the prompt explicitly.
- Keep each template focused on one kind of message.
- Review outputs the way you would review a junior writer's drafts.

## Why self-host
Open models such as GPT-J and GPT-Neo could run on infrastructure we controlled, which made cost and data handling predictable. Orchestration used LangChain.

## Looking back
The models of that era needed careful prompting and a human in the loop. Today's models follow instructions much better, but the lessons carry over: constrain the structure, show examples, and keep a person responsible for what goes out.
