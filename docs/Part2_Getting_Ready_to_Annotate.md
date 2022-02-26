---
layout: default
title: Part2—Grammatical details
nav_order: 3
---
# Part II — Getting ready to annotate
{: .no_toc }
## Table of Contents
{: .no_toc }

1. TOC
{:toc}

## 1. Where to put a tag on
Because meanings of engagement can be expressed at different levels of lexical and grammatical items, we need to know exactly which part of the sentence we should put a tag on.
This section deals with such structural issues during the annotation. Each section below deals with possible grammatical structure for emgagement, and which items to put a tag on.


| Features                                                                                              | Example items              | Where to put a tag                                          |
| ----------------------------------------------------------------------------------------------------- | -------------------------- | ----------------------------------------------------------- |
| [Modal verbs](#modal-verbs)                                                                           | can, have to               | on the item                                                 |
| [Single-word adverbs](#single-word-adverbs)                                                           | obviously, sure            | on the item                                                 |
| [Adverbial/ Prepositional constituency](#multi-word-adverbs-adverbial-and-prepositional-constituency) | in my view                 | the entire phrase                                           |
| [Mental or communication verbs](#mental-or-communication-verbs)                                       | think, say, tell           | on the item (= [`Root`](#identifying-root-of-the-sentence)) |
| [Subordinate conjunctions](#subordinate-conjunctions-modified)                                        | as, when, if               | on the item                                                 |
| [Multi-word subordinate conjunctions](#multi-word-subordinate-conjunctions-modified)                  | as long as, whether or not | on the multiword item                                       |
| [Coordinating conjunctions](#coordinating-conjunctions)                                               | but, and, yet              | on the item                                                 |



### Modal verbs
When an engagement meaning is realized by a modal verbs (e.g., can, may, might, have to, etc.), you will put a tag on the modal.
- He **may** be lying.
- Teachers **should** show students the language needed to achieve these rhetorical features of argumentative writing.

### Single-word adverbs
When an engagement meaning is realized by a single word adverbs (e.g., probably, surprisingly, etc.), you will put a tag on the item.
- **Obviously**, he was lying. 
- He was **probabily** lying,

### Multi-word adverbs/ adverbial and prepositional constituency
When an engagement meaning is realized by a multi-word adverbs, such as prepositional phrases, adverbial phrases, you will put a tag on the whole constituency.
- **In my view**, these were the norm.
- **Generally speaking**, if a person repented the church would pardon him or her regardless of how atrocious the crime was.

### Mental or Communication verbs
When an engagement meaning is realized by a mental or communication verbs, you will put a tag on the lexical verb.
- Our analysis **confirms** previous work showing that incorporating various perspectives on an issue is a valuable feature of argumentative, analytical writing.

### Subordinate conjunctions (Modified!!!)
When an engagement meaning is realized by a subordinate conjunctions such as *although*, *while*, and *if*, you will put a tag on the conjunction.
- **Although** the religion motif was not commonly discussed among the discussants, the relevance of this theme to these various texts need to be brought to attention.
- **Though** there were several ‘couples’, these were definitely not the norm.
- The Bush administration, **as** we all know, has rejected the Kyoto agreement

### Multi-word subordinate conjunctions (Modified!!!)
When an engagement meaning is realized by a multi-word subordinate conjunctions such as *as long as* and *where or not*, you will put a tag on the multi-word sequence.
- **As long as** the response addresses the question, it can be long.

### Coordinating conjunctions
When an engagement meaning is realized by a coordinating conjunctions such as *but* and *yet*, you will put a tag on that item.
- **But** look at what he achieved.
- Schools do not serve as avenues for upward mobility, **but** instead reinforce existing social and economic inequalities.


## Identifying ROOT of the sentence
In some cases, you need to identify the `ROOT` of the sentence. 
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

## Determining T-unit



Some sentences were taken from [a website](https://www.scarymommy.com/funny-phrases/)
