---
layout: default
title: Part6—Recommended procedures
nav_order: 8
---

Updated on 24th April 
{.label .label-green}
# Part 5 — Engagement tagging: Rules and Spans
{: .no_toc }
## Table of Contents
{: .no_toc }

1. TOC
{:toc}

---
# Annotation procedure

## 1. Clause boundary detection

For each sentence, annotation should start with clause boundary segmengation and clause type identification.
I will not repeat the content here, but you should refer to the [clause boundary detection](3_Part2_Clause_boundary.md) for details.

## 2. Modal sense disambiguation

Once a sentence has been annotated for clause boundary and types, we will annotate the sense of modal verbs (if any).
This will allow us to prepare for the following engagement annotation because although most modal verbs function as `entertain` it is not always the case.

See [Modal sense Disambiguation](Modal-verb-sense.md) for details of this step.

## 3. Engagement annotation

Finally, we look for any engagement in the sentence.

- A main clause should get at least one monogloss or any other heteroglossic tags. If there is NO heteroglossic tag, the main clause should have a monogloss tag.
- Embedded clauses may or may not get engagement tag(s).
- Subordinate clauses can get an engagement tag spanning the entire clause (e.g., `COUNTER`, `ENTERTAIN`).
- Additionally, subordinate clauses may have additional engagement items inside the clause.

The following steps are meant to help you to look for potential linguistic structures that engagement strategy can surface. This is not an exhaustive list, so they should be used as only a recommended guidance.

### Functional perspective
1. Does the sentence hedge their statement (e.g., expression of likelihood)?
2. Does the sentence attribute the claim to any sources?
3. Does the sentence assert their own point of view WITHOUT recognition to others (i.e., `Monogloss`)?


### Structural perspective
1. Look out for any verbs in the main clause; Are they potentially engagement item (e.g., `say`, `believe`); Who says or believes?
2. Look for any conjunctions and adverbial phrases in the main clauses.
3. Look for any modal verbs, negative particles, .
4. Does the sentence cite any sources?


# Procedure at work 
Consider the following example:
> The question I will seek to answer is not whether schools should offer curricular choice.

This sentence is annotated for clause types as follows:
![example-clause](figures/Tutorial/example_clause_boundary.png)

1. First, we look for any engagement in the main clause. In this case we have `not` in the main clause, which is `DENY`.

2. Next, we look at the two embedded clauses. We find modal verbs in both clauses, so we need to think about the in which sense these are used.
   - We consider that the first one is more related to `willingness` and `temporal` meaning than, for example, `epistemic`. So, we do not think this one is `ENTERTAIN`. 
   - On the other hand, the second modal verb `should` is used in the `deontic` sense, which suggests that it can be considered `ENTERTAIN`.

Going through this process, the annotation for this example sentence will look like:
![example-annotated](figures/Tutorial/example1_annotated.png)
