---
layout: default
title: Verbal group + clausal projection 
parent: Step 2–Span detection
nav_order: 1
---

Updated in version 3
{: .label .label-green}


# Verbal group + clausal projection 

| Features                                                                        | Example items                                                  | Where to put a tag                             |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------- |
| [Verb phrases](#general-principles-on-verbal-groups)                            | `runs`, `had seen`, `have been identified`, `have shown`, etc. | on the entire verb phrase (except model verbs) |
| ‖-[Negation](#passive-construction)                                             | `is determined`, `was said`                                    | on the entire verb phrase (except model verbs) |
| ‖-[Passive construction](#passive-construction)                                 | `is determined`, `was said`                                    | on the entire verb phrase (except model verbs) |
| ‖-[Degree adverb + Verb](#degree-adverb--lexical-verb)                          | `partially agree`,                                             | `degree adverb + lexical verb`                 |
| [Mental or communication verbs](#mental-or-communication-verbs)                 | `think`, `say`, `tell`                                         | on the entire verb phrase                      |
| [It/there is X that/to construction](#it-is-x-thatto-as-interpersonal-metaphor) | `It is unlikely` that ....                                     | See the rule below                             |
| [emphatic do](#emphatic-do)                                                     | I `do believe` that ...                                        | `do + lexical verb`                            |
| [Modal verbs](#modal-verbs)                                                     | `can`, `have to`                                               | on the item                                    |


{: .tips}
> From version 3, we do not include the conjunction `that/whether` that introduces projection clauses in the span.
> 
> Previously, we were including them:
> - **It’s probable/likely/possible that** he’s lying.
> 
> From version 3, we exclude them:
> - **It’s probable/likely/possible** that he’s lying.
> 
> This is primarily based on the fact that the meanings/function of engagement is expressed outside the projection clause, and sometimes intervening words (adverbs, clausal conjunctions) make it hard to include the projection without including too many other elements.




## General principles on verbal groups


When an engagement meaning is realized by a verb phrase, you will put a tag on the entire verb phrase (including Auxiliary + negation + lexical verbs + particles).
One exception to note is when a [modal auxiliary](#modal-verbs) is in the verb phrase. In such cases, we will treat the modal verb separately from the verb phrase.


- They **have found** it very difficult to understand each other ‘s lifestyles.
- Discussants correctly **pointed out** that Bernardino of Siena, Martin Le Franc, and the anonymous author of the Errores Gazariorum all **have** an even more aggressive campaign against witches than **did** the authors of our previous readings.
- Our analysis **confirms** previous work showing that incorporating various perspectives on an issue is a valuable feature of argumentative, analytical writing.

{: .note}
>Previously (in version 1), we have put a tag on "most lexically heavy verbs".

### Negation

When there are `negative perticles (e.g., not, never)` we will still consider it within the span.

- Even though he **had taken** all his medication, his leg **did n’t look** any better.
- The effect of Morphological Awareness **did not achieve** significance ( β = .193, p = .263). 
  
### Passive construction

When we put a tag on passive construction (e.g., `MONOGLOSS`, `ATTRIBUTE`), we include `copula verb + lexical verb` in the span.


- The data **was collected** in the local community.
- The allegations **are believed** to involve several teenagen aged from 12 to 18.
- At least some of the abuse **is claimed** to have taken place last year.
- It **was expected** that they would interview him later today.

### Degree adverb + Lexical verb

When there is a degree adverb that directly modify the lexical verb that expresses ENGAGEMENT meaning, then we consider these two as a set of engagement move.

- I **partially agree** with the statement above.
- He **completely opposed** to the report.


## Mental or Communication verbs

When an engagement meaning is realized by a mental or communication verbs, you will put a tag on the lexical verb.
We do not include `that` that introduces the projection clause.

### Communication/mental verbs (`like` pattern)

- I **think** that ~.
- I **suppose** that ~.
- I **don't believe** that ~.
- We **hear** that


### Communication/mental verbs (`please` pattern)

- **It strikes me** that ~.
- **It occurred to me** that ~.
- **It surprizes me** that ~.
- **It puzzles me** that ~.


![commuverbs](figures/spans/comm_verb.png)


## I am/have X that/whether/how ~

- I **am sure** that
- I **am not entirely sure** whether
- I **am of the opinion** that
- I **have no doubt** that


## It is X that/to — as Interpersonal metaphor

When there is `It is X that ~`, `It is X to ~` or `there is/are X that` construction, we will tag the entire span of this construction. 
This decision is based on the fact that these construction function as introducing the stance of the writer as a whole (they almost function as chunks). 


### It/there is X that 
When the `that-clause` govern the following clause, the tag spans are from `It/There` before `that`:
- **It’s probable/likely/possible** that he’s lying.
- **It is possible that** it is your duty to tell me.
- **It seems likely that** Mary knows.
- **It is absolutely clear to me** that what Charlotte was arguing was that Crouching Tiger was a bad film to which liberal audiences imputed a significance shaped by their own prejudices about Chinese cinema and the Chinese in general.
- **There is no doubt** that globalization has a deep effect on China.
- However, **there is mounting evidence** that processes of language acquisition, use, and change are not independent of one another but are facets of the same system.
- **There can be no doubt**, however, that the imperial Byzantine silks have a power and a dignity, a feeling for design and texture, seldom rivalled in the history of textiles.
- **It is said** that television keeps people at home. 
- **It is widely accepted** that the processes that occur at the presentation of a single word are strongly dependent on the grammatical context that accumulated before the word, for example.


### It is X (for Y) to  

When a `to-infinitive` govern the following clause, the tag spans are from `It` to the adjectival complement.
- **It is possible** for a layer of ice to form under the circumstances.
- But **it is likely** to have an impact in the near future.
- It was found, for example, that **it is more likely** to occur in NNS–NNS dyads rather than between NSs and NNSs (Varonis & Gass, 1985 ).
- **It would be possible** to suppose, for instance, that the tnre Schrodinger-like equation involves non-linearities.



In the following pattern, we can identify two strategies.
- It seems fairly obvious to most people that Watson tremendously oversimplified the learning process.

First, `It seems fairly obvious` gets a span, because this is a variant of `It is X to`.
Second, `seems` should get another tag because they add `ENTERTAIN` value to the author's assessment using `fairly obvious`.

- **It *seems* fairly obvious** to most people that Watson tremendously oversimplified the learning process.



![Interpersonal_meta](figures/spans/Interpersonal_metaphor.png)


## X is/are in NOMINAL that

- FL teachers **have been in general agreement** that the target language should be used as much as possible in the FL classroom.


## Modal verbs

When an engagement meaning is realized by a modal verbs (e.g., can, may, might, have to, etc.), you will put a tag on the modal.
- He **may** be lying.
- Teachers **should** show students the language needed to achieve these rhetorical features of argumentative writing.

![modal](figures/spans/modals.png)

### List of modal verbs

Following Halliday & Mathiessen (2014, p. 145), the following items are considered as modal verbs (Modal operators) in this project:
- can, may, could, might, (dare), will, would, should, is to, was to, must, ought to, need to, have/has/had to
- needn't, don't need to, don't have to, won't, wouldn't, shouldn't, (isn't/wasn't), mustn't, oughtn't to, can't, couldn't, (mayn't, mightn't, haven't to).


## Emphatic do

A typical realization of `PRONOUNCE` is the use of emphatic do. In this case, we will put a tag on `do + lexical verb`:

- We `do believe` that researchers should view this disciplinary division as an opportunity rather than an obstacle.

This is a strategy to prevent any `ENTERTAIN` tagged on `believe` when there is already a `PRONOUNCE` in the sentence.

