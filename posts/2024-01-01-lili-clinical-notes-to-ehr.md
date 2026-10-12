---
title: Lili: from physician notes to a filled-in EHR encounter
dek: Extracting diagnoses, procedures and medications from free text, then writing them into the record through FHIR.
group: now
band: b-maroon
highlight: maroon
where: HighPlains Computing (Los Angeles, remote)
when: 2023 to 2025
tools: AWS Batch, SageMaker, ECS, Athena, DynamoDB, FHIR APIs
featured: yes
---

Lili reads the notes a doctor writes or dictates after seeing a patient and turns them into a filled-in encounter in an electronic health record (EHR) system.

## The problem
After a visit, someone has to translate free-text notes into codes and fields. The doctor mentions diagnoses, procedures, medications and immunizations, and the record needs all of them in structured form. It is slow, repetitive and easy to get wrong.

## What Lili extracts
- **ICD-10 codes** for diagnoses.
- **CPT codes** for procedures and services.
- **Medications**, with the details the note provides.
- **Anatomy**, meaning which part of the body a finding or procedure refers to.
- Immunizations and procedures the doctor performed.

## From text to a record
Extraction produces structured data. The last mile is writing it into the EHR, and that is where FHIR (Fast Healthcare Interoperability Resources) comes in. FHIR is a REST-style standard where things like patients, encounters and appointments are resources you create and read over an API. I worked extensively with FHIR APIs to create encounters and appointments and to handle the other operations involved in processing clinical notes.

## The infrastructure
Clinical notes arrive in volume and not on a schedule, so the pipeline runs on AWS services chosen for that shape of work: AWS Batch for batch compute, SageMaker for models, ECS for services, Athena for querying data in place, and DynamoDB for fast key-based lookups.

## Why healthcare is its own discipline
- Codes are not interchangeable. A near-miss code is still wrong, so evaluation has to be strict.
- Privacy rules shape every design choice, from logging to storage.
- Integration is half the work. A model that extracts perfectly but cannot write into the EHR saves nobody time.

Lili is where my earlier healthcare NLP work, the speech and text projects at Care Cloud, met production-grade infrastructure.
