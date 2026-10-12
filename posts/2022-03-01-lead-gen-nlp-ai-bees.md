---
title: NLP for lead generation: classifying replies, finding entities, choosing prospects
dek: A 0.91 F1 reply classifier, a multilingual entity model and LangChain pipelines for a marketing team in Hamburg.
group: llm
band: b-navy
highlight: navy
where: AI Bees (Hamburg, remote)
when: 2021 to 2022
tools: PyTorch, DistilBERT, XLM-RoBERTa, LangChain, FastAPI, Docker
featured: no
---

At AI Bees, a company in Hamburg, I built NLP for marketing: finding the right prospects and handling their replies.

## Understanding replies
When prospects answer outreach messages, someone has to decide what each answer means: interested, not now, not relevant. I trained a response classifier on DistilBERT. Because labeled replies are scarce, I augmented the text data to enlarge the training set. The model reached an F1-score of 0.91 on test data.

## Pulling out the details
I trained an XLM-RoBERTa model for named-entity recognition, to extract relevant information from text. A multilingual model was a natural fit for a company working across languages.

## Choosing prospects
One of the services analyzed LinkedIn profiles using Big Five (OCEAN) psychological tests, implemented with transformer models such as DistilBERT, to help target the right prospects.

## Shipping it
The tools were built as LangChain pipelines, dockerized and served through FastAPI. PyTorch powered the classifier and the entity model.

## Writing at scale
For generating outreach text I used self-hosted GPT-J and GPT-Neo. There is a separate post about that.

## Takeaways
- Data augmentation is a cheap first move when labels are scarce.
- Small, well-tuned models beat large ones for narrow classification, and they are cheaper to serve.
- A service is not finished when the model works. It is finished when someone else can call it.
