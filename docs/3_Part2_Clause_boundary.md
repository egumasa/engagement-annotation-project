---
layout: default
title: Part2–Clause boundary detection
nav_order: 4
---

New
{: .label .label-green}
# Clause boundary detection 


Clause boundary detection is an auxiliary task, which aims to help you to think about the overall structure of the sentence before tagging any engagement values.

The followings are how we will tag on different types of clauses:

| Label                               | definition                                                                                                                                                                                                                                           |
| :---------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [MAIN](#simple-main-clauses)        | An independent clause, which function as complete unit.                                                                                                                                                                                              |
| [SUBORDINATE](#subordinate-clauses) | A dependent clause attached to a main clause through the use of subordinate conjunctions (e.g., `because`, `although`, `if`, `when`, `as`, `while`, etc.)                                                                                            |
| [EMBEDDED](#embedded-clauses)       | a type of dependent clause that function as a part of another clause. That is, an embedded clause is included in a subject, object of another clause (i.e., complement clause) or function as an adjective to modify a noun (i.e., relative clause). |
| FRAGMENT                            | An imcomplete sentential unit. Typically, without any verbs.                                                                                                                                                                                         |


**NOTE**: When we identify clauses, we do NOT consider punctuation at the end of the clause boundaries as a part of the clause. 

## Simple MAIN clauses

Simple main clauses are defined as:
> A clause that can stand alone to make a complete sentence.

In addition to "simple" sentence structure, we will include imperative sentences (commands) as a independent main clause.

In webanno, you will annotate the clause in the following manner:
![Figure_main](/figures/simple_main_clauses1.png)

## Coordinated clauses – More than one MAIN clauses

Coordinated clauses are defined as:
> A complex clause where two or more MAIN clauses are combined via coordinated conjunctions (e.g., and, but, or).

You can also consider colon `:` and semi-colon `:` as an implicit coordination of two MAIN clauses.

- [I went to the store]; [they were closed].
- [I went to the store], [but they were closed].

In webanno, you will annotate the clause in the following manner:
![Figure_Coordinated](/figures/Coord_clauses1.png)


## SUBORDINATE clauses

Subordinate clauses are defined as:
> a dependent clause that is attached to a main clause through the use of subordinate conjunctions (e.g., `because`, `although`, `if`, `when`, `as`, `while`, etc.)

In webanno, you will annotate these in the following manner:
![Figure_subordinate](/figures/Main_subordinate1.png)



## Embedded clauses

Emdedded clauses are defined as:
> a type of dependent clause that function as a part of another clause. That is, an embedded clause is included in a subject, object of another clause (i.e., complement clause) or function as an adjective to modify a noun (i.e., relative clause).

In webanno, you will annotate these in the following manner:
![Figure_Embedded](/figures/Embedded1.png)



## Real examples—Mixture of different clause types

In real example, we will deal with mixture of different types. 
This is illustrated in the following examples.

![Figure_real_examples](/figures/Real_examples1.png)

### Comments on the real examples

20: The subject of this sentence is `The idea`, and the main verb is `is`. There are two embedded clauses. One is a complement of the noun `idea`, which elaborates on the content of that idea (i.e., complement clause). The other is `I think`, which function as attached (i.e., parataxic) node to the main clause. 

21: We have one additional subordinate clause and an additional embedded clause in this example. The embedded clause is the content of the main verb (i.e., the content of what the citizens believe). Grammatically, this is called a complement clause of the main verb. The embedded clause has two parts, Embedded-main, which we do not tag, and Embedded-subordinate, which we will treat as a subordinate clause.

22: This example has one additional embedded clause functioning as the complement of the verb `feel`.

23: This example has one additional subordinate clause. The subordinate clause is introduced by a subordinate conjunction `as`, which add secondary information to the main clause.

24: This example has two main clauses, and there is one subordinate clause, which I consider attached to the first main clause. We have two main clauses because both parts has finite verbs "the player **is** ..." and "they must **pay** ...". The semi-colon works as implicit coordination between the clauses. Finally, the subordinate clause is introduced by a subordinate conjunction `once`, which add extra Temporal information to the main clause (c.f., `before/after/since Y do X`).

25: This has two main clauses, coordinated implicitly by a colon `:`. The first MAIN clause has additional embedded clause, which is the complement of the verb `argue`.  



## Problems in the sentence segmentation

Sometimes, the annotation dataset may have weird lines. This may include completely empty lines, or just a word in line. It can also have cases where in-text citations are ill-formatted.

1. IF the dataset has empty lines, skip annotating that line.
2. If the sentence is imcomplete, use the `FRAGMENT` tag.
  - In 1999, (FRAGMENT)
  - are examples of this concept (FRAGMENT)


