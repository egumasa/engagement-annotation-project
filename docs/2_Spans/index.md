---
layout: default
title: Step 2–Span detection
has_children: true
nav_order: 6
---

{: lg}

# Step 2 — Engagement Spans

This section deals with structural/grammatical issues during the annotation, particularly the decisions involving where to put the tag. 

In the example in this document, the span for which the tag should be put is shown in **Bold** face. 

{: .label .label-red}
Under construction


## General principles

It is important to remember that an engagement category (e.g., `ENTERTAIN`) is realized/expressed in a variety of construction types (e.g., `modal verb`, `if-clause`, `adverbial phrase`, etc.). 
Similarly a given construction type (e.g., `It is X that` construction) can take various engagement categories (e.g., `ENTERTAIN`, `PRONOUNCE`).
Step 2 guidelines aim to help us to precisely identify the span of engagement tag in different types of construction. 

### Example construction by category matrix

First, to illustrate what it meant by the previous points, the following matrix shows the example combination between engagement category and construction type. You can confirm that:

1. A construction can express different engagement meaning.
2. An engagement category can be expressed with a range of construction types.


|                                          | Communication (and other) verb                      | Mental verb 'like' clause           | Mental verb 'please' clause | "I am/have" clause                 | "It/there is x that/to" clause                           | Prep. phrase                 | Adv. gp; Prep. Phrase         | Predicator               | Nominalization                      |                                          |
| ---------------------------------------- | --------------------------------------------------- | ----------------------------------- | --------------------------- | ---------------------------------- | -------------------------------------------------------- | ---------------------------- | ----------------------------- | ------------------------ | ----------------------------------- | ---------------------------------------- |
| Prototypical `ENTERTAIN` (guess)         |                                                     | I + **guess** / I **don't know** if |                             | I **am not entirely sure** whether |                                                          |                              | `presumably`                  |                          | **my assumption/impression** (that) | Prototypical `ENTERTAIN` (guess)         |
| Prototypical `ENTERTAIN` (argue)         | I + **argue**                                       |                                     |                             |                                    | **It is arguable** that                                  |                              | **arguably**                  |                          | **our argument** (that)             | Prototypical `ENTERTAIN` (argue)         |
| Prototypical `ENTERTAIN` (think)         |                                                     | I + **think/believe**               | **It strikes me** that      | I **am of the opinion** that       | **It is possible** that, **There is a probability** that | **in my opinion**, **to me** | **perhaps**, **probably**     | X **is likely** to       | **my opinion**,                     | Prototypical `ENTERTAIN` (think)         |
| Prototypical `ENTERTAIN` (suggest)       | I + **suggest**                                     |                                     |                             |                                    |                                                          |                              | **tentatively**               |                          | **our proposal** (that)             | Prototypical `ENTERTAIN` (suggest)       |
| Prototypical `PRONOUNCE` (no doubt)      |                                                     | I **never doubt**/ I **do believe** |                             | I **have no doubt** that           | **There is no doubt** that, **it is indubitable** that   |                              | **indubitably**, **no doubt** |                          |                                     | Prototypical `PRONOUNCE` (no doubt)      |
| Prototypical `PRONOUNCE` (clear/obvious) | We + **conclude**                                   |                                     |                             | I **am sure** that                 | **It is clear** that                                     |                              | **clearly**, **obviously**    |                          |                                     | Prototypical `PRONOUNCE` (clear/obvious) |
| Prototypical `ATTRIBUTE`                 | They + **say**                                      | I + **hear**                        |                             |                                    | **It is said/reported** that                             | **According to X**           | **reportedly**, **allegedly** | X **is said/rumored** to | **their assertion/proposal** that   | Prototypical `ATTRIBUTE`                 |
| Prototypical `ENDORSE`                   | They + **convincingly argue**, They + **confirmed** |                                     |                             |                                    | **There is mounting evidence** that                      |                              |                               | X **is demonstrated** to |                                     | Prototypical `ENDORSE`                   |

**Note**: This table is not an exhaustive list of construction types for each engagement. There will also be possible realization of the category in the empty cells.

### Basic Rules

The following table summarizes basic construction types which may realize any of the engagement meaning and their rules for span detection. 

| Features                                                                                                                 | Example items                                                     | Where to put a tag                             |
| ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- | ---------------------------------------------- |
| [Verb phrases](#verb-phrases)                                                                                            | `runs`, `had seen`, `have been identified`, `have shown`, etc.    | on the entire verb phrase (except model verbs) |
| [Passive construction](#passive-construction)                                                                            | `is determined`, `was said`                                       | on the entire verb phrase (except model verbs) |
| [Mental or communication verbs](#mental-or-communication-verbs)                                                          | `think`, `say`, `tell`                                            | on the entire verb phrase                      |
| [Degree adverb + Verb](#degree-adverb--lexical-verb)                                                                     | `partially agree`,                                                | `degree adverb + lexical verb`                 |
| [It/there is X that/to construction](#it-is-x-thatto-as-interpersonal-metaphor)                                          | `It is unlikely that` ....                                        | See the rule below                             |
| [emphatic do](#emphatic-do)                                                                                              | I `do believe` that ...                                           | `do + lexical verb`                            |
| [Modal verbs](#modal-verbs)                                                                                              | `can`, `have to`                                                  | on the item                                    |
| [Single-word adverbs](#single-word-adverbs)                                                                              | `obviously`, `sure`                                               | on the item                                    |
| [Adverbial/ Prepositional constituency](#multi-word-adverbs-adverbial-and-prepositional-constituency)                    | `in my view`, `to me`, `in actual fact`                           | the entire phrase                              |
| [(Adverbial) subordinate clauses](#subordinate-clauseincluding-both-single-word-and-multi-word-subordinate-conjunctions) | `as SV`, `when SV`, `if SV`, `as long as SV`, `whether or not SV` | the entire subordinate clause                  |
| [Coordinating conjunctions](#coordinating-conjunctions)                                                                  | `but`, `and`, `yet`                                               | on the item                                    |
| [Question](#questions)                                                                                                   | `Who thinks that smoking do no harm in 21st century?`             | on the entire question                         |
| [Comment clause/ parataxis](#comment-clauseparataxis)                                                                    | see examples                                                      | on the entire comment clause                   |
| [Shell nouns](#nominalized-construction)                                                                                 | `the author's belief that/of` ...                                 | `Det + premodifiers + Noun + that/of`          |
| [No + Noun construction](#no--noun-construction)                                                                         | `No rules`, `None of the idea`                                    | `No + head noun`                               |
| [Citations](#citations)                                                                                                  | `Kyle (2020)`; `(Kyle, 2020)`                                     | See details                                    |





{: .tips}
>When in doubt, you can test whether the span is reasonable by separating an idea/issue/problem at hand (i.e., propositional content) from the author's view on that matter.
> Here is an easy example:
> - I think that people are very generous to tourists around here.
>
> Here, `people are very generous to tourists around here` is the idea/issue/problem under consideration. The writer of this sentence uses `I think (= ENTERTAIN)` as an engagement device to say this view is only mine (and there may be other views.)
> 
>To extend this approach, consider the following example:
> - A few years ago, I wrote expressing my concern that the village of West Linton, Peeblesshire, had 'moved'.
>
> In this example, the writer of this sentence says that they expressed their concern by writing. The matter (i.e., propositional content) is the idea/fact that `the village of West Linton, Peeblesshire, had 'moved'`.
> This is the actual content, on which the writer of this sentence takes stances. Then, the question becomes if the writer of this sentence takes any positions on this matter of discussion (Contract? or Expand?). 
> Based on this, I would suggest the following:
>
>- A few years ago, I **wrote expressing my concern that** the village of West Linton, Peeblesshire, had 'moved'.
>
> In this sentence, the writer says that they wrote something. What did they write?—Their concern. Although `wrote` is a concrete action verb, which tends NOT to take on engagement, the non-finite subordinate clause (i.e., expressing SOMETHING) roughly equals to `I said SOMETHING`. Technically, we do not have `ACTION verb + COMMUNICATION verb + Shell noun + that` as a pattern in the list above. However, we can think of putting an `engagement` move on this span. The question becomes then whether we will take `my concern that` or the `ACTION verb + COMMUNICATION verb + Shell noun + that` sequence as a whole. Here we need to think what makes more sense as the writers' possible communicative purposes. If we separate `wrote` from `my concern`, then we would have to treat `wrote` as `MONOGLOSS` and `my concern` as secondary `ENTERTAIN`. On the other hand, if we treat the whole span as single Engagement move, then we can treat the whole as `ENTERTAIN`. This may result in disagreement/discussion, but we may consider that the whole thing as almost equivalent to `I said that ...` then we see them as a whole.