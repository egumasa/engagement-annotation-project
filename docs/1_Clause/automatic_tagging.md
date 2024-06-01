---
layout: default
title: About automatic clause annotation
parent: Step 1–Clause-boundary detection
nav_order: 8
---

# Automatic clause annotation support

From October, 2022, we will introduce semi-automatic clause annotation. This is intended to reduce annotation burden and to facilitate the speed. 
Specifically, I have trained a machine learning model based on our previous annotations (a total of roughly 1,800 sentences) and use this model to produce automatic annotation.

The accuracy of the model is satisfactory, although there will be some misclassification (both over- and under- identification) cases time to time. This page describes some known patterns of mistakes so that you can fix the errors before you start annotation of subsequent layers.


## Accuracy of the model

| Tag           | F1   | Precision | Recall |
| ------------- | ---- | --------- | ------ |
| `MAIN`        | .891 | .896      | .886   |
| `SUBORDINATE` | .800 | .800      | .800   |
| `EMBEDDED`    | .854 | .838      | .872   |
| `FRAGMENT`    | .500 | .545      | .461   |
| overall       | .860 | .861      | .859   |

Overall, the tagging accuracy achieves F1 of .86, with slightly lower scores on `SUBORDINATE` and `FRAGMENT`.
Having these figures in mind would help you to look for any potential errors produced my the automated clause annotation.



## Some known patterns of errors

`SUBORDINATE` when it's not really subordinate clause

Sometimes, the model overidentifies subordinate clause, particularly:

- adverbial/prepositional phrases (`despite NOUN`, `because of NOUN`, `in order to NOUN`)


## Spans of `SUBORDINATE` and/or `EMBEDDED` due to multiple embedding

When multiple `EMBEDDED` clauses are used, the model may have a hard time to differentiate whether the subsequent dependent clauses are a part of the preceeding dependent clause(s) or an independent one. This has to be determined semantically by deciding which part of the sentense the second dependent clause are dependent on in the T-unit.

Consider the following example:

- But I am wondering why it said we could visit the restaurant if you know it would be closed.

The model tagged this T-unit as follows:

- But I am wondering {[why it said we could visit the restaurant]`EMBEDDED` [if you know it would be closed]`SUBORDINATE`}`EMBEDDED`.

This annotation is only partially correct. Particularly, it is unclear which of the "am wondering" (= `MAIN`) or "it said" (= `EMBEDDED`) the `SUBORDINATE` clause ("if you know it would be closed") is attached to. Here, the machine provides both interpretations. I propose an interpretation that "if you know" is attached to "it said", so I propose first modification as follows:

- But I am wondering {why it said we could visit the restaurant [if you know it would be closed]`SUBORDINATE`}`EMBEDDED`.

Now, the `SUBORDINATE` is treated as a part of the larger `EMBEDDED` clause. Additionally, the automatic tagging has several missing annotations. 

- But I am wondering {why it said [we could visit the restaurant]`EMBEDDED` [if you know (it would be closed)`EMBEDDED`]`SUBORDINATE`}`EMBEDDED`.

I have added two `EMBEDDED` which are nested in each of the `EMBEDDED` and `SUBORDINATE` clauses we have had from the outset.


---

Back to [Step1 clause boundary detection](index.md)