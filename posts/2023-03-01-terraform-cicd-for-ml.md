---
title: Terraform, CI/CD and the part of ML that decides whether anything ships
dek: Two years of infrastructure and delivery work across MoodMD, Boston University and Gardiant.
group: ops
band: b-black
highlight: olive
where: Point of IT (US-based company, remote)
when: 2021 to 2023
tools: Terraform, AWS Batch, ECS, Lambda, Docker, Python
featured: yes
---

Before I worked on LLM products, I spent two years on the part of ML that decides whether anything ships: infrastructure and delivery. At Point of IT, a US-based company, I worked on client engagements across three organizations.

## MoodMD
The work was Terraform pipelines plus Python DevOps scripts. A big part of the job was checking that the client's models were actually running, because a model that silently stops serving is worse than one that fails loudly.

## Boston University (BUCAS)
Here I designed a CI/CD pipeline and deployed it. The aim of any pipeline is to make the safe path the easy path, so every change is built, tested and released the same way.

## Gardiant
For Gardiant I wrote Terraform and Python automation for CI/CD of AWS Lambda functions and ECS applications. Lambda and ECS suit different workloads, short event-driven functions and long-running containers, and a good pipeline handles both without special cases.

## Training and inference on AWS Batch
Beyond client projects, I built pipelines on AWS Batch for large-scale model training and inference, with ML services containerized in Docker. Batch handles queueing, compute environments and scaling, so engineers submit jobs instead of managing machines.

## Principles I took from it
- If it is not in code, it does not exist. Environments created by hand cannot be reproduced.
- Monitor model behavior, not only servers. Up is not the same as correct.
- Keep pipelines boring. Surprises belong in experiments, not releases.
