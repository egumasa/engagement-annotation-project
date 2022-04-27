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
| [FRAGMENT](#fragment)               | An imcomplete sentential unit. Typically, without any verbs.                                                                                                                                                                                         |


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

Common subordinate conjunctions, which introduce a subordinate clause, include:
- **Concessions**: although, as, as though, even, even though, though, just as though, whereas, while
- **Conditions**: even if, if, in case, provided (that), unless, as long as, as much as,
- **Temporal**: after, as, as soon as, as long as, before, once, still, till, until, when, whenever, while
- **Contrasts**: although, though, whereas, while, rather than, 
- **Causal relations**: as, because, in order (that), so that, now that, since
  


In webanno, you will annotate these in the following manner:
![Figure_subordinate](/figures/Main_subordinate1.png)

In some cases, a subordinate clause can also be realized non-finite verbs with present participles (e.g., -ing).

![Figure_justifying](figures/clauses/present_participle.png)

![Figure_taking](figures/clauses/present_participle2.png)




## Embedded clauses

Emdedded clauses are defined as:
> a type of dependent clause that function as a part of another clause. That is, an embedded clause is included in a subject, object of another clause (i.e., complement clause) or function as an adjective to modify a noun (i.e., relative clause).

In webanno, you will annotate these in the following manner:
![Figure_Embedded](/figures/Embedded1.png)

## Fragment

Fragment here is defined as an indepent line in the annotation data that does not have any clausal element.

This is mostly due to the automatic sentence segmentation issue or syntactic errors in the original essays.

Examples include:
- (Norris, 2009)
- Ibid. (2008, p. 2)
- For example, 
- ,
- p. 36).
- Sincerely,
- Dear Kris,

These are all categorized as Fragment. Since fragment is used to detect any non-clausal, minor textual segments in the data, it won't be used with other categories. That is, when a sentence have at least one `Main`, `Subordinate`, or `Embedded`, that sentence do not get `Fragment`.

Conversely, the followings are still categorized into `Main` even if they seems they are cut off in the middle:

- The author argues:
- He went to France via 
- No one seems to disagree with the view that 

The examples above are considered `Main` clause because there is at least one [finite verb](1_Basic_grammar.md)—`argues`, `went to`, and `seems`.
We are going to treat these example as 

Note that Empty lines has automatically converted to `EMPTYSENT—Skip Annotation`. When you encounter this, just skip the sentence.


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


