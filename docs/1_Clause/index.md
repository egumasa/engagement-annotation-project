---
layout: default
title: Step 1–Clause-boundary detection
has_children: true
nav_order: 2
---

# Clause boundary detection 


Clause boundary detection is an auxiliary task, which aims to help you to think about the overall structure of the sentence before tagging any engagement values. 

{: .note }
Since this is a auxiliary task, we do not really do full-fledged clausal analysis, such as non-finite clauses as modifier of nouns, etc.. Thus, the following guideline is not intended to conduct a full clausal analysis, but abbrebiated version that helps us during the engagement annotation.


## Definition of clausal strategies to annotate

The followings are how we will tag on different types of clauses:

| Label                               | definition                                                                                                                                                                                                                                                                                                                                  |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [MAIN](#simple-main-clauses)        | An independent clause, which function as complete unit.                                                                                                                                                                                                                                                                                     |
| [SUBORDINATE](#subordinate-clauses) | A dependent clause attached to a main clause through the use of subordinate conjunctions (e.g., `because`, `although`, `if`, `when`, `as`, `while`, etc.)                                                                                                                                                                                   |
| [EMBEDDED](#embedded-clauses)       | a type of dependent clause that function as a part of another clause. That is, an embedded clause is included in a subject, object of another clause (i.e., complement clause) or function as an adjective to modify a noun (i.e., relative clause). Inserted clauses, such as parataxis, are also considered as a type of embedded clause. |
| [FRAGMENT](#fragment)               | An imcomplete sentential unit. Typically, without any verbs.                                                                                                                                                                                                                                                                                |


{: .note }
When we identify clauses, we do NOT consider punctuation at the end of the clause boundaries as a part of the clause. 