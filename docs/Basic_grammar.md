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

## Grammatical terminologies we will use.
First of all, it is always helpful to clarify important terminologies we will use during the annotation project. When I use the following terms, I use in the following meaning and examples in mind.

| Terminology         | Definition/Description                                               | Example                                                                 |
| ------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| phrase/constituents | A group of words which creates a meaningful chunk.                   | a dog (NP), during the meeting (PP), went to the park (VP)              |
| clause              | Linguistic unit with a verb (and typically a subject).               | I went to the park yesterday. / Be mindful.                             |
| independent clause  | A clause that can stand alone to make a complete sentence            | (The two example above are independent clause and sentence themselves.) |
| dependent clause    | A clause that are attached  to (dependent on) an independent clause. | If you are free (dep. cl), just come to the party (ind. cl).            |
| ROOT                | the highest node in the syntactic tree of the sentence.              |                                                                         |
| head                |                                                                      |                                                                         |



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

