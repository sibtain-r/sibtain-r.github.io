---
title: PackageX: reading parcel labels in real time
dek: Sender and receiver details from messy, multilingual parcel photos, above 0.94 F1.
group: doc
band: b-maroon
highlight: maroon
where: PackageX (mailroom OCR service)
when: 2021
tools: OCR, LayoutLMv2, LayoutLMv3, ONNX, PyTorch Serve, FastAPI, TensorFlow Lite
featured: yes
---

PackageX built a mailroom service. Parcels arrive at co-working spaces, and the people working there need to know when theirs has come. My work was reading the label.

## The task
Extract the sender and receiver details from images of parcels, in many languages, so parcels can be tracked and users notified.

## The pipeline
Optical character recognition converts the image to text. A transformer-based multimodal model, LayoutLM, labels the entities by combining the image, the bounding boxes and the text. I used LayoutLMv2 for labeling entities, reaching an F1-score above 0.94, and LayoutLMv3 for real-time extraction.

## Real time, and personal data
Labels contain names and addresses, which is personal data, and the service had to run in real time. I extracted PII from package images in real time and built the data annotation pipeline for the mailroom OCR service.

## Benchmarks
I also benchmarked visual-linguistic models for key information extraction, on OCR data and on direct images: CUTIE, Donut and CLIP. They represent different ideas. CUTIE reads documents as a grid of text, Donut skips OCR and reads the image directly, and CLIP matches images with text.

## Serving
Models were optimized for low latency with ONNX and served with PyTorch Serve behind FastAPI. Lightweight computer-vision models were built with TensorFlow Lite for mobile deployment.

## Lessons
- Annotation tooling decides how fast you iterate. The annotation pipeline mattered as much as the model.
- Parcel labels are chaotic: handwriting, stickers, curved surfaces, many scripts. Evaluate on that mess.
- Latency is a feature. A label read that takes too long is not a real-time service.
