---
layout: default
title: Other
parent: Step 2–Span detection
nav_order: 4
---

Updated in version 3
{: .label .label-green}


# Other important structures

## Questions

When an engagement meaning is realized by a question, we will tag the whole question **INCLUDING the question mark**. This will result in **not completely overlapping span** for clause detection and engagement because clause detection does not include punctuation at the end of the clause.

![questions](figures/spans/questions.png)


## Comment clause/parataxis

- Well, I'm going to feel lucky if my car isn't towed, **I think**.
- The conclusion, **it seems**, is intolerable. (Treated as `primary` engagement)


# Rules for specific tags

## Citations

For citations, we will tag the entire span of the citation.
Sometimes, due to the sentence segmentation issue, the dataset will include citations cut in the middle (see the last example in the screenshot).
- The extremely high prevalence of child and adolescent exposure to violence in U.S. inner-cities <engmt class="monogloss">is</engmt> alarming **(Bell &amp;amp**.


## SOURCE


![Citation](figures/spans/citation.png)

