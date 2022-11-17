---
layout: default
title: Preliminaries— Grammatical Terminologies
nav_order: 3
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

| Terminology               | Definition/Description                                                                                                                                | Example                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| phrase/constituents       | A group of words which function together (creates meaning).                                                                                           | The impatient customer (NP)/was acting (VP) /very cranky (ADV) /at the time (PP).                     |
| clause                    | Linguistic unit containing a verb (and typically a subject).                                                                                          | I went to the park yesterday. / Be mindful.                                                           |
| independent (main) clause | A clause that can stand alone to make a complete sentence                                                                                             | (The two example above are independent clause and sentence themselves.)                               |
| dependent clause          | A clause that are attached to (dependent on) an independent clause.                                                                                   | If you are free (dep. cl), just come to the party (ind. cl).                                          |
| subordinate clause        | A dependent clause that is attached to a main clause through the use of subordinate conjunctions (e.g., because, although, if, when, as, while, etc.) |                                                                                                       |
| embedded clause           | A type of dependent clause that function as a part of another clause.                                                                                 |                                                                                                       |
| ROOT                      | The highest node in the syntactic tree of a sentence.                                                                                                 |                                                                                                       |
| head                      | The highest node in the given a phrase/constituent/clause                                                                                             |                                                                                                       |
| Terminal unit (T-unit)    | A unit of text characterized by a `MAIN` clause with any dependent clauses attached to it.                                                            | {Get it done.} $_{T-unit}$ {If you are free (dep. cl), just come to the party (ind. cl).} $_{T-unit}$ |
| modal verb | An auxillary verb expressing modality. | can, may, could, might, dare, will, would, should, is to, was to, must, ought to, need to, have/has/had to, needn't, don't need to, don't have to, won't, wouldn't, shouldn't, isn't/wasn't, mustn't, oughtn't to, can't, couldn't, mayn't, mightn't, haven't to (Halliday & Mathiessen, 2014, p. 145)
--- 



## Coordinated clauses
Contents moved to [clause boundary identification](./1_Clause/MAIN.md/#coordinated-clauses-–-more-than-one-main-clauses).

## Subordinate clauses
Contents moved to [clause boundary identification](./1_Clause/SUBORDINATE.md).

## Embedded clauses
Contents moved to [clause boundary identification](./1_Clause/EMBEDDED.md).

## Terminal unit (T-unit)

NEW in version 2
{: .label .label-green}

T-unit is a grammatical (syntactic) unit often used to segment for linguistic analysis. 

{: .def}
> A unit of text characterized by a `MAIN` clause with any dependent clauses attached to it.

For instance, each of the following examples constitutes one and only one T-unit (a `MAIN` clause with any other dependent unit):

- Go home!
- I would like to report a recent incident in my department.
- When you are ready, let's have some dinner.
- My parents and I had a good time during the trip.
- Because the manager is the apex of status and authority and because all information must come through this position , the manager is at the focal point for decision making
- When we are tired of doing work, we should just take some rest and come back again later because that may help our focus.


Each of the following sentences consists of two T-units (because of two `MAIN` clause). 
- We run all sounds, and we run the nation.
- They fail to deal with individual learning styles ; and they consume inordinate amounts of classroom hours and educational resources.


We will use the concept of T-unit when discussing primary vs. secondary engagement strategies. Specifically, primary engagement characterizes that of the entire T-unit, while secondary engagement concerns strategy for units that are subordinate to any T-unit.



## Distinguishing adverbial clauses and adverbial phrases

Updated on May 12nd, 2022
{: .label .label-green}

As of April 9th, we decided to put a tag on the whole subordinate clause. This means that we do not really have to distinguish these two.
In the following example, adverbial phrases and clauses are contrasted. 

### Adverbial phrases

| Adverbial phrase                                                 | Else                                                         |
| :--------------------------------------------------------------- | :----------------------------------------------------------- |
| **Yesterday**                                                    | I went to the market.                                        |
| **Despite the rain**,                                            | the Cub Scouts held the car wash.                            |
| **Before/After the play**,                                       | we had coffee.                                               |
| **Since Monday**,                                                | it has been terribly hot.                                    |
| **Because of the small size of the self‐reflection sub‐corpus**, | we have excluded it from our analysis across academic level. |

### Adverbial clauses


| Adverbial clause                           | Else                                                                                    |
| :----------------------------------------- | :-------------------------------------------------------------------------------------- |
| **Because this is a new annotation task**, | clarification from the annotator greatly helps.                                         |
| **As we mentioned in Chapter I**,          | however, we believe that it is better to conceive of grammar and lexicon as intertwined |
| **Before/After the play ended**,           | many patrons were crying.                                                               |
| **Since you talked to me about it**,       | I've become convinced.                                                                  |
| **As far as I know**,                      | he arrived this morning.                                                                |
| **As soon as you can**,                    | give me a call.                                                                         |


## Coordination

Coordinations need special attention in the current annotation. In essense, coordination here means a "list" of two or more linguistic elements combined using coordinating conjunction such as `and`, `or`, etc.

When dealing with coordination, it is important to understand the coordination can happen at different levels of grammar. Or put differently, coordination is a linguistic construction to connect two or more linguistic expression at the same levels of grammar (e.g., NOUNS, VERBS, CLAUSE, etc.). When the sentence is grammatical, it is important to ask coordination of WHAT, in order to differentiating the different types.

### Coordination of noun phrases
Perhaps, the most simple, prototypical coordination occurs when coordinating conjunctions are used to list THINGS (e.g., noun phrases.)

- I ordered _**a panini** and **a cappuccino**_.
- _**My parents** and **I**_ had a good time during the trip.
- Some examples of this type of graphic are _**the histogram** and **the boxplot**_.

### Coordination of adjectives
It is possible for a noun to have multiple modifiers (such as adjectives). In this case, the coordination occurs within a noun phrase.

- [...] to accomplish the KE maneuver in _a **smooth** and **effective** manner_.

It is also possible that two or more adjectives are combied as predicates of the sentence (adjectival complement).

- The space now will be _**smooth** and **flat**_. 


### Coordination of other types of phrases

Coordinations can happen at other types of phrases such as adverbs, adverbial expressions and prepositional phrases.

#### adverbs
- We made an effort to position the Innovation Lab _to **easily** and **quickly** adapt_ to emerging opportunities 

#### adverbial phrases

### Coordination of verb phrases

This requires a little more attention because, in real-life examples, this looks very much alike coordination of two main clauses. 
However, coordination of verb phrases is distinct from coordination of clauses. 
An important characteristics of verb phrase coordination is the fact that the subject of the later verb phrases is omitted and assumed to be shared with the first verb phrase.

- We **went to the cafe** and **ordered two cups of coffee**.

In the example above, the second verb phrase (`ordered two cups of coffee`) does not have an explicit subject. Or more precisely, it shares the subject with the first verb phrase. This means they are **coordinated verb phrases** instead of coordinated clauses.

Similar examples to help you understand the concept.

-  We **administered** the revised instrument to a new sample and **conducted** a confirmatory factor analysis ( CFA ).
-  At the second , they **reverse** and **run** back , ending up again in a line.

{: .tips}
Coordinating verb phrases can be detected by deleting the first element and see if the second element can stand alone.
Because coordinating verb phrases does not have explicit subject in the second part, it cannot be indepent.

### Coordination of MAIN clauses

Compared to coordination of verb phrases, coordination of clauses are combination of two or more clauses. 
This means that each coordinated elements can stand alone as a sentence even if other elements were deleted.

- **We run all sounds**, and **we run the nation**.
- **They fail to deal with individual learning styles** ; **and they consume inordinate amounts of classroom hours and educational resources**.

Having explicit subject in the second coordinated element suggests they are coordination of CLAUSE, not phrases.


### Coordination of SUBORDINATE clauses

A couple more! You now see where I am heading to...? So, as much as we can coordinate MAIN clauses, we can also coordinate SUBORDINATE clauses.
Subordinate clauses are typically those that are introduced by subordinating conjunction such as `because`, `while`, `when`, etc.

From a functional perspective, this is likely happen when the writer wants to list reasons (`because`) and time (`when`).

- **Because the manager is the apex of status and authority** and **because all information must come through this position** , the manager is at the focal point for decision making.

Notice from the example above that the coordination happens between two `Because SUBJ VERB` structure, which indicates that this is a coordination of two subordinate clauses. This is true because we have a main clause (`the manager is at the focal point for decision making`) to which the two coordinated subordinate clauses are attached. 


### Coordination of EMBEDDED clauses

Okay, here we go. It is of course possible to coordinate embedded clauses. This is particularly relevant to us because we will see many cases of this.

A prototypical pattern we will see is the following:

- I think/believe/argue that A, that B, and that C.

Here assume that each of the A, B, and C is clausal element introduced by `that`. So, here we have three that clauses connected via `and`. 

This pattern may be easily confused with coordination of MAIN clauses because each element appears to be a full clause. But remember, if B and C is also the content of "I think", then it is coordinated EMBEDDING rather than completely separate clauses. I am planning to add more examples of this type.


## Bibliography
**<span style="color:blue">(NEEDS REVIEW):</span>** Halliday, M.A.K., &amp; Matthiessen, C.M.I.M. (2014). *Halliday's introduction to functional grammar* (3rd eds). Routledge. 

Larsen-Freeman, D., & Celce-Murcia, M. (2016). *The grammar book. Form, meaning and use for English language teachers* (3rd eds).

