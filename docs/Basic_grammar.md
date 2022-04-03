---
layout: default
title: Preliminaries— Grammar stuff
nav_order: 2
---

# Preliminaries 
{: .no_toc }
## Table of Contents
{: .no_toc }

1. TOC
{:toc}

## Grammatical terminology
First of all, it is always helpful to clarify important terminologies we will use during the annotation project. When I use the following terms, I use in the following meaning and examples in mind.

| Terminology               | Definition/Description                                              | Example                                                                           |
| ------------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| phrase/constituents       | A group of words which function together (creates meaning).         | The impatient customer (NP)/was acting (VP) /very cranky (ADV) /at the time (PP). |
| clause                    | Linguistic unit containing a verb (and typically a subject).        | I went to the park yesterday. / Be mindful.                                       |
| independent (main) clause | A clause that can stand alone to make a complete sentence           | (The two example above are independent clause and sentence themselves.)           |
| dependent clause          | A clause that are attached to (dependent on) an independent clause. | If you are free (dep. cl), just come to the party (ind. cl).                      |
| ROOT                      | The highest node in the syntactic tree of a sentence.               |                                                                                   |
| head                      | The highest node in the given a phrase/constituent/clause           |                                                                                   |

## Identifying `ROOT` of the sentence
The first task you will do in the annotation is to identify the `ROOT` of the sentence. 
`ROOT` is defined as the highest node in the syntactic tree of the sentence.

![Dependency example 1](/figures/dep1.png)
In this example, `hates` is the `ROOT` of the sentence because it is NOT governed by any other words in the sentence. This means that `hates` is the highest node in the sentence.

### Strategies to identify the ROOT.

1) Find the main verb phrase of a clause. The `Root` is the most lexically heavy verb in the verb phrase. This will work for simple independent sentences. The `ROOT` is bolded in the following examples:
   
 1. These **were** the norm.
 2. spaCy **comes** with free pre-trained models for lots of languages.
 3. Schools do not **serve** as avenues for upward mobility.
 4. Pokémon Legends: Arceus has now been **released** globally! 
 5. One **is** that the salary is very little.

2) If there are subordinate clauses in a sentence, determine which clause govern the other(s). The clause governing the other clauses are considered to have a `ROOT`.

 1. When you finish the work, you can **go** home.
 2. Whenever I’m bored, I **go** to my favorite place: The fridge.
 3. I strongly **believe** that a few cup of coffee will do the trick.


## Coordinated clauses vs Subordinate clauses

### Coordinated clauses
Coordinated clauses are independent clauses that are connected with coordinating conjunction (e.g., `and`, `but`, `or`).

| Independent clause            | Coordinated conjunction | Independent clause                  |
| :---------------------------- | :---------------------- | :---------------------------------- |
| Marianne lives in California, | but                     | Diane lives in Michigan or Vermont. |
| He went to the party,         | but                     | I stayed home.                      |

### Subordinate clauses
A subordinate clause is a dependent clause that is attached to a main clause through the use of subordinate conjunctions (e.g., `because`, `although`, `if`, `when`, `as`, `while`, etc.)

A subordinate clause can either follow or preceed the main clause. We will come back to this later, but when we put a tag on subordinate clause, it will fall onto the conjunction.

| Main clause                          | Subordinate clause                    |
| :----------------------------------- | :------------------------------------ |
| It was hard to write a book together | `because` they live so far apart.     |
| Peggy frequently calls               | `because` she wants to stay in touch. |

| Subordinate clause                            | Main clause                            |
| :-------------------------------------------- | :------------------------------------- |
| `Although` Marianne and Diane live far apart, | they are still friends.                |
| `As` far as I am concerned,                   | there is not much study on this topic. |

## Distinguishing adverbial clauses and adverbial phrases

One tricky grammatical detail that becomes important during annotation is the distinction between adverbial clauses and phrases.
As we will see, we are going to tag the entire phrase (such as `in my view`, `for example`, `as for me`), but we will put a tag on the conjunction (e.g., `as`, `because`, `when`) not the entire clause.
A clause has to have `finite` verb (roughly verb with tense) while a phrase does not have finite verbs (or even lacks a verb).

### Adverbial phrases

| Adverbial phrase  | Else                              |
| :---------------- | :-------------------------------- |
| Yesterday         | I went to the market.             |
| Despite the rain, | the Cub Scouts held the car wash. |

### Adverbial clauses
| Adverbial clause                       | Else                                                                                    |
| :------------------------------------- | :-------------------------------------------------------------------------------------- |
| Because this is a new annotation task, | clarification from the annotator greatly helps.                                         |
| As we mentioned in Chapter I,          | however, we believe that it is better to conceive of grammar and lexicon as intertwined |
|                                        |                                                                                         |

## References
Larsen-Freeman, D., & Celce-Murcia, M. (2016). *The grammar book. Form, meaning and use for English language teachers* (3rd eds).

