---
layout: default
title: MAIN clause(s)
parent: Step 1–Clause-boundary detection
nav_order: 1
---


## Simple MAIN clauses

{: .def}
> A clause that can stand alone to make a complete sentence.

In addition to "simple" sentence structure, we will include imperative sentences (commands) as a independent main clause.

In webanno, you will annotate the clause in the following manner:
![Figure_main](../figures/simple_main_clauses1.png)



## Coordinated clauses – More than one MAIN clauses

{: .def}
> Coordinated clauses are independent/main clauses that are connected via coordinating conjunctions (e.g., `and`, `but`, `or`).

You can also consider colon `:` and semi-colon `:` as an implicit coordination of two MAIN clauses.

| Independent clause            | Coordinated conjunction | Independent clause                  |
| :---------------------------- | :---------------------- | :---------------------------------- |
| Marianne lives in California, | but                     | Diane lives in Michigan or Vermont. |
| He went to the party,         | and                     | I stayed home.                      |
| I went to the store           | but                     | they were closed                    |
| I went to the store           | ;                       | they were closed                    |


In webanno, you will annotate the clause in the following manner:
![Figure_Coordinated](../figures/Coord_clauses1.png)

## Coordinated verb phrases – treated as a single MAIN clause


{: .caution}
>When the scope of the coordination is verb phrases—that is, not explicit subject is introducted in the second or later coordinated elements, we will still treat them in a single `MAIN` clause.
> For example:
> The following is one main clause with one T-unit
> - [[I went to see the movie and got home late yesterday]`MAIN`]`T-UNIT`.
> 
> But the following should be two main clauses, because the second element have an explicit subject:
> 
> - [[I went to see the movie]`MAIN`]`T-UNIT` [[and I got home late yesterday]`MAIN`]`T-UNIT`
> 
> Similarly, the following examples are cases of single `MAIN` clause:
> - He keeps trying, but not succeeding. 
> 
> => there is no explicit subject for "succeeding" and keeps is also a common verb for both trying and suceeding.


In the following example the verb 'left' and 'went' are treated within a same clause because the second verb does not have explicit subject.


![VP_coordination](../figures/spans/VP_coordination1.png)

---

Back to [Step1 clause boundary detection](index.md)