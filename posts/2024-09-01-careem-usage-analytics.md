---
title: The unglamorous side of ML work: usage analytics for a ride-hailing client
dek: Not every project is a model. Sometimes the job is getting the definitions right.
group: ops
band: b-maroon
highlight: maroon
where: HighPlains Computing, for Careem
when: 2023 to 2025
tools: Python, SQL, Reporting
featured: no
---

Not every project at a company is a model. For Careem, a ride-hailing client of HighPlains Computing, my work was analytics: reports on how people used the product.

## The questions
- How many users log in, and how many do not?
- Who uses what?
- Which platforms do they use?

These sound simple. They are not, until the definitions are settled.

## Definitions come first
"Active user" can mean logged in today, logged in this week, or completed an action. Pick one, write it down, and use it everywhere. Most disagreements about a dashboard are really disagreements about a definition.

## Clean before you count
Login events arrive with duplicates, missing fields and inconsistent platform labels. A report is only as trustworthy as the cleaning behind it, so I treat the cleaning step as part of the analysis rather than a chore before it.

## Make it repeatable
A report someone has to rebuild by hand every month is a liability. Scripted, parameterized reports that rerun on fresh data turn a one-off analysis into something a team can rely on.

## What it taught me
Working on analytics next to ML systems made me more careful about metrics in ML too. A model with a good score on the wrong measure is still the wrong model.
