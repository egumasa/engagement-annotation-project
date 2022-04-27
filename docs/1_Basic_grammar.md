---
layout: default
title: Preliminaries— Grammatical Terminologies
nav_order: 2
---

# Preliminaries 
{: .no_toc }
## Table of Contents
{: .no_toc }

1. TOC
{:toc}

---

## Grammatical terminology
First of all, it is always helpful to clarify important terminologies we will use during the annotation project. When I use the following terms, I use in the following meaning and examples in mind.

| Terminology               | Definition/Description                                                                                                                                | Example                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| phrase/constituents       | A group of words which function together (creates meaning).                                                                                           | The impatient customer (NP)/was acting (VP) /very cranky (ADV) /at the time (PP). |
| clause                    | Linguistic unit containing a verb (and typically a subject).                                                                                          | I went to the park yesterday. / Be mindful.                                       |
| independent (main) clause | A clause that can stand alone to make a complete sentence                                                                                             | (The two example above are independent clause and sentence themselves.)           |
| dependent clause          | A clause that are attached to (dependent on) an independent clause.                                                                                   | If you are free (dep. cl), just come to the party (ind. cl).                      |
| subordinate clause        | A dependent clause that is attached to a main clause through the use of subordinate conjunctions (e.g., because, although, if, when, as, while, etc.) |                                                                                   |
| embedded clause           | A type of dependent clause that function as a part of another clause.                                                                                 |                                                                                   |
| ROOT                      | The highest node in the syntactic tree of a sentence.                                                                                                 |                                                                                   |
| head                      | The highest node in the given a phrase/constituent/clause                                                                                             |                                                                                   |


--- 
## Coordinated clauses

Contents moved to [clause boundary identification](3_Part2_Clause_boundary.md#coordinated-clauses-–-more-than-one-main-clauses).
## Subordinate clauses

Contents moved to [clause boundary identification](3_Part2_Clause_boundary.md#subordinate-clauses).



## Embedded clauses
An embedded clause is a type of dependent clause that function as a part of another clause. That is, an embedded clause is included in a subject, object of another clause (i.e., complement clause) or function as an adjective to modify a noun (i.e., relative clause).
In the following examples, embedded clauses are _italicized_.

- The paper argued _[that average price is not a meaningful measure of market power]_. (The clause functions as an object of argue.)
- I wanna eat the ramen _[that she mentioned a couple of days ago]_. (The clause modifies "the ramen".)
- And you will meet a man _[who says American Airlines took away his life]_. (The clause modifies "a man".)
- The idea _[that a democratic school is one where kids have an equal vote]_, I think, is a mistake. (The clause is a complement of a noun.)

## Distinguishing adverbial clauses and adverbial phrases

~~One tricky grammatical detail that becomes important during annotation is the distinction between adverbial clauses and phrases.
As we will see, we are going to tag the entire phrase (such as `in my view`, `for example`, `as for me`), but we will put a tag on the conjunction (e.g., `as`, `because`, `when`) not the entire clause.
A clause has to have `finite` verb (roughly verb with tense) while a phrase does not have finite verbs (or even lacks a verb).~~

As of April 9th, we decided to put a tag on the whole subordinate clause. This means that we do not really have to distinguish these two.

### Adverbial phrases


| Adverbial phrase      | Else                              |
| :-------------------- | :-------------------------------- |
| **Yesterday**         | I went to the market.             |
| **Despite the rain**, | the Cub Scouts held the car wash. |


### Adverbial clauses

| Adverbial clause                           | Else                                                                                    |
| :----------------------------------------- | :-------------------------------------------------------------------------------------- |
| **Because this is a new annotation task**, | clarification from the annotator greatly helps.                                         |
| **As we mentioned in Chapter I**,          | however, we believe that it is better to conceive of grammar and lexicon as intertwined |


## A detailed description of dependent clause types
From the grammatical perspective, dependent clauses can be classified into several categories.
Each deserve separate attention in the current documentation. Note there may be a correlation between structural patterns and `engagement` this is never absolute. 
Remember that `engagement` is (discourse) semantic categories.


### Verb + (that-)clause (Embedded)
This pattern typically occurs when clausal complement (such as that-clause) follows mental or communication verbs.

- The author argued _that television has helped to shrink the relative distance between people and countries_.
- I think _Mary teaches French_.
- It appears _that maximum price fixing does the greatest harm when set below a competitive level_.

### Noun + (that-)clause (Embedded)
This patterns occurs when a (that-)clause elaborates content of the noun expression. 

- _The idea that the company has a clear responsibility to the incident_ was rejected by the judge.
- Their argument was based on _the belief that a happy ending is a certainty_.
- Our conclusion is drawn based on _the fact that there was a correlation between the intensifier use and their perception of social identity_.


### Relative clauses (Embedded)
A relative clause is where a clause is used to modify a noun (antecedent). There are two main categories in the use of relative clause.

The first type of relative clause occures when a noun is modified by a whole clause. It is typically used to identify which noun they are talking about out of all the possible cases of the noun.
- The analysis should be regarded as _a tool which alerts us to the potential conflicts_.

The other type of relative clause typically elaborates the content of the whole clause or introduces additional information about the noun expression/whole clause.

- We included all participants into the analysis with the exception of _the Italian participants, which was necessary to control for their native languages._ 


## References
Larsen-Freeman, D., & Celce-Murcia, M. (2016). *The grammar book. Form, meaning and use for English language teachers* (3rd eds).

