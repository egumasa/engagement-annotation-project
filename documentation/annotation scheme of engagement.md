
# Welcome to the annotation project!
Welcome! Thank you for your interests in the annotation project. In this project, we will create a hand-annotated corpus (i.e., systematic collection of texts) of academic English written by both first- and second- language writers of English. You will be an annotator of the project as a research assistant (RA), and you will gain hands-on experiences in processes of annotating a linguistic corpus, or more broadly corpus-based and Natural Language Processing (NLP) research.

## Project overview
What constitutes 'good' academic writing? You may think of a range of ways that makes an essay good. For instance, the essay makes a "good" argument; it has a "good" organization; it has "good" content, etc. Although these are all relevant aspects of "good" academic writing, linguists consider that one important aspect of good writing has to do with the way in which the author positions themselves in relation to other voices and possible alternative positions. In other words, in academic writing, the writer is expected to take appropriate "stances" on the subject matter, by "toning down" some of your claims and/or "proclaiming" the most important views. In this annotation project, we are going to annotate sentences taken from essays written by both L1 and L2 writers of English in terms of such stance-taking expressions in each sentence.



## What is this document about?
- This document explains the framework for manual annotation of the corpus. 
- We use the `engagement framework` (Martin & While, 2005) in order to annotate lexico-grammatical features of stance-taking.
- What is stance-taking (/expressions)?—It is elements in the discourse that express the writer's levels of commitment to the idea presented in the writing. For example, a writer can add tentativeness to their idea by acknowledging that it is only one of the possible interpretations. Compare different versions of the same argument:
	- 1. The banks have been greedy. (Stated as if it is a fact)
	- 2. In my view, the banks have been greedy. (Presented as a personal view)
	- 3. A book I read recently said that the banks have been greedy. (Acknowledging a source)
- The ability to appropriately adjust the level of commitment to the idea is one of the important aspects of academic writing. 
- In this project, we will annotate sentences taken from academic essays in terms of the lexico-grammatical features of stance-taking.

## The Goals of the project
- To create a human-annotated corpus of academic English on stance-taking expressions.
- More specifically:
	- To identify specific lexico-grammatical items that enact meanings of stance-taking (e.g., `in my view`, `X said`)
	- To identify specific meanings of stance-taking (we call this Engagement moves) for the identified lexico-grammar items.


# PART I — Understanding Engagement

## Engagement coding scheme
There are 9 categories of engagement moves to annotate in the current project (see [Table 1](#table-1-categories-of-engagement-moves)). Most categories belong to "parent" (or more general) discourse moves, such as `contract` and `expand`. 

Figure 2 shows the entire taxonomy. Based on Figure 2, we can understand that we have finer-grained discource moves as we go deeper into the taxonomy (e.g., `heterogloss` > `contract` > `disclaim` > `deny`). I will explain what these categories mean shortly, but remember that this taxonomy presents alternative stance-taking strategies (or discourse choices) a writer can make to position themselves in the writings. 

![Figure 2](/figures/FullEngagementtaxonomy.png)

### Core Terminologies
The following sub-sections describe core terminologies (category labels) in the coding scheme.

#### Monogloss and Heterogloss
The first (the most coarse-grained) distinction concerns `monogloss` vs. `heterogloss`, which is about whether the utterance recognizes the alternative positions or not. In Monogloss, the utterance does not recognize any alternative views and presents the idea/event as a fact (e.g., "The banks have been greedy"). On the other hand, a heteroglossic utterance includes various ways to at least acknowledge possible alternatives (e.g., "I speculate that the banks have been greedy", "I read somewhere that the banks have been greedy.", "It is unlikely that the banks have been greedy.", etc.).

#### Expansion and Contraction
A heteroglossic move is divided into `expand` and `contract` moves. The distinction is about whether the writer opens up (`expand`) dialogic spaces for alternative viewpoints or to close down (`contract`) the spaces. 
Essentially, writers use `expand` moves to indicate that the idea is only one possible version of the reality. `Expansion` move is further divided into `entertain` and `attribute`, which are explained later.
On the other hand, writers use `contract` moves to close down the dialogic spaces. They can do this by (a) rejecting alternative viewpoints (`disclaim`) or (b) showing greater committment to their ideas (`proclaim`). 

#### Expansion moves—Entertain and Attribute
`Expansion` move includes discourse moves to (a) increase the tentativeness to the statement (`entertain`) and to (b) attribute the idea to external sources (`attribute`). 
For example, a writer can use lexico-grammatical items such as modal verbs (`can`, `may`) and mental verbs (`I believe`) to `entertain` other possible alternatives. The writers can refer to external sources (e.g., `the paper mentioned`) and remain neutral with respect to the presented idea. 

#### Contraction moves—Disclaim and Proclaim
`Contraction` moves concern different ways the writer advances their own views on the topic, and therefore, narrow down or close down the space for negotiation. 
Writers can `disclaim` other views by using `deny` option (e.g., "That is NOT correct.") or using `counter` option (e.g., "Although the paper may be right, there is another possibility."). 
The writers can `proclaim` their views by (a) assuming that the readers would agree their views (`concur`), (b) explicitly underscoring their views as valid (`pronounce`), or (c) use other's perspective/data/claims as correct and reliable (`endorse`).


<details><summary> Interrim Summary </summary>

* `Monoglossic utterance` = An utterance which involves a factual statement, without recognizing other potential views.

* `Heteroglossic utterance` = An utterance which recognizes that the referenced idea is one possible alternatives among others, regardless the author supports or rejects the idea.

* `Contraction strategy` = Discourse moves which close down dialogic space; the speaker/writer acts to challenge, fend off or restrict other alternative positions and voices.

* `Expansion strategy` = Discourse moves which open-up the dialogic space; the speaker/writer actively makes allowances for dialogically alternative positions and voices.

</details>



### Table 1. Categories of Engagement moves
| Strategy    | Engagement moves                           | Description                                                                                                                                                                                                                          |
| ----------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Contraction | [Disclaim: Deny](#disclaim-deny)           | An utterance which invokes a contrary position but which at the same time rejects it directly. The contrary position is hence given very little dialogic space.                                                                      |
| Contraction | [Disclaim: Counter](#disclaim-counter)     | An utterance which expresses the present proposition as replacing and thus 'countering' another proposition which would have been expected.                                                                                          |
| Contraction | [Proclaim: Concur](#proclaim-concur)       | An utterance which shows writers' expectation/assumption that the putative readers will agree with the preposition and/or to have the same knowledge.                                                                                |
| Contraction | [Proclaim: Pronounce](#proclaim-pronounce) | An utterance which expresses a strong level of writer commitment through the author's explicit emphasis and interpolation, thereby closing down the dialogic space.                                                                  |
| Contraction | [Proclaim: Endorse](#proclaim-endorse)     | An utterance which refers to external sources as warrantable, undeniable,  and/or reliable. It expresses the writer’s alignment with and endorsement of an attributed proposition. As such, the dialogic space is somewhat narrowed. |
| Expansion   | [Entertain](#entertain)                    | An utterance which indicates author's position but as only one possibility amongst others, thereby opening up dialogic space.                                                                                                        |
| Expansion   | [Attribute](#attribute)                    | An utterance which signifies dialogic space as the writer attributes the proposition to an external source.                                                                                                                          |
| Monogloss   | [Monogloss](#monogloss)                    | An utterance which does not employ any value of engagement. Such an utterance ignores the dialogic potential in an utterance.                                                                                                        |
| Auxiliary   | [Justify](#justify)                        | An utterance which engage in persuasion through justification or substantiation.                                                                                                                                                     |
| Auxiliary   | In-text Citation                           | In-text citation is where external source(s) are referred to in the text in an parenthetical form. e.g., (Martin & White, 2005); [#REF].                                                                                             |

We are going to look at the raw sentences and tag any of the following `engagement moves`. Using the previous example.
- `In my view (ENTERTAIN)`, the banks have been greedy.
- A book I read recently `said (ATTRIBUTE)` that the banks have been greedy.

Once again, these categories is about discourse meaning that writers make; therefore, the meaning can be realized through different levels of lexico-grammar. This is the topic of the next section.

## Engagement meaning can be expressed using different categories of lexical and grammatical resources

Meanings of engagement (stance-taking) are realized through a range of lexical and grammatical resources. Typical grammatical structures include:
- Modal auxiliaries (e.g., `can`, `may`, `must`)
- Stance adverbs (e.g., `obviously`, `naturally`, `probably`)
- Adverbial phrases (e.g., `according to X`, `as far as I am concerned`, `in my view`)
- Communication/mental verbs (e.g., `X said that`, `the study demonstrated`, `I think`)
- Attributive adjectives (e.g., `it is possible`, `it is likely`)
- Subordinate clauses (e.g., `even though`, `if X...`, `although ...`)
- Negation (e.g., `not`, `never`)

The implications of this include:
- A particular engagement move can be expressed through different levels of grammar.
  - ==> Entertain can be expressed using modal verbs (`can`), adverbial/prepositional phrases (`in my view`), evidentials (`it seems that`).
- A same grammatical structure would function as distinct engagement meaning.
  - ==> Communication verbs (e.g., `suggest`) can express different meanings depending on its subject.  `the data suggest (ENTERTAIN)`  vs. `The author suggested (ATTRIBUTE)`.

So, It is important to fully understand what each category means through closely examines the examples presented below.

## More elaborated description of each category with examples
### Disclaim: Deny
> An utterance which invokes a contrary position but which at the same time rejects it directly. The contrary position is hence given very little dialogic space.

In other words, `deny` move includes acknowledgement to an alternative position so as to reject it. Typically the meaning is realized using negations.
- You do**n’t** need to give up potatoes to lose weight.
- these were definitely **not** the norm
- We are of course **not** dealing with one monolithic hegemonic English voice
- Natural gas burns with twice the heat of coal gas, is **not** poisonous and has **no** odor.

[Back to Table 1](#table-1-categories-of-engagement-moves)

### Disclaim: Counter
>An utterance which expresses the present proposition as replacing and thus 'countering' another proposition which would have been expected.

Typically, `disclaim: counter` involves conjunctions such as *although*, *but*, *however*, which signals the meanings of `Counter` in an explicit manner.
- **Although** the religion motif was not commonly discussed among the discussants, the relevance of this theme to these various texts need to be brought to attention.
- In comparison, 32% of the respondents felt that the conventional downtown was still a major attraction, **even though** the regional centre had gained quite a vast amount of popularity and did to large extent have an air of modernity.
- **While** the Supreme Court rejected the “quality of care” argument in the federation case, the oligopolistic characteristics and purchasing structure of insurance make this outcome unsurprising.
- **Although provisional**, our model has implications for pedagogy.
- **Even though** he had taken all his medication, his leg did*n’t (DENY)* look any better.
- **While** that grief is deeply understood, the problem with tragedies like this one is that they become a heyday for the overly-sincere, maudlin, righteousindignation crowd.
- Every single law is addressed to the men, with the use of the pronoun “he” throughout the text, **even** when the laws are closely referring to female issues.

`Disclaim: Counter` sometimes includes less obvious realizations. For example, adjuncts such as *even*, *only*, *just*, and *still* may "also have a counter-expectational aspect to their meanings" (Martin & White, p. 121).
- They **even** organised a car for you at the airport.
- **Still**, they were able to win the game.

`Disclaim: Counter` would also include some adverbs that encode meanings of counter-expectations.
- `Unexpectedly/Surprisingly/To my surprise`, there seems to have been little smuggling this year.

[Back to Table 1](#table-1-categories-of-engagement-moves)

### Proclaim: Concur
>An utterance which shows writers' expectation for the putative readers to agree with the preposition and/or to have the same knowledge.

There are two sub-types of `concur` which we do not differentiate in the current project. These are `affirm` and `concede` (Tan, 2010).  

`Affirm` examples
- The ability of a population to successfully reproduce is **obviously** a crucial aspect of a society’s survival.
- Bailey, **of course**, was that rarity, a cricketer who at his best was worldclass with both bat and ball.
- The Bush administration, **as** we all know, has rejected the Kyoto agreement
- **As** we can see, the popularity of Woodlands new town between residents and non-residents is directly opposite to each other.

`Concede` examples
- **Admittedly**, he was badly behaved.
- **Indeed**, it is odd that both the FTC and courts have historically regarded huge, publicly traded insurance firms rather than health providers as the legal proxy of patients.
- **Sure**, he broke rules.

Some tricky example, but we all categorize them under `concur`:
- **Certainly** he was badly behaved but look at what he has achieved.

NOTE: **Certainly** illustrates there may be multiple functions that an item can accomplish depending on the context. Here, "Certainly ...., but" can be considered as `concur`, but certainly can be used as `Entertain` (see example).

[Back to Table 1](#table-1-categories-of-engagement-moves)


### Proclaim: Pronounce
>An utterance which expresses a strong level of writer commitment through the author's explicit emphasis and interpolation.
- I therefore **propose** that universities have a greater role in working alongside the NCAA in negotiating its television.
- I **DID** turn out the lights before I left.
- But **the facts of the matter are that** we have never made the national decisions or marshaled the national resources required for such leadership.
- **It is absolutely clear to me that** what Charlotte was arguing was that Crouching Tiger was a bad film to which liberal audiences imputed a significance shaped by their own prejudices about Chinese cinema and the Chinese in general.
- I **contend** it's the worst address by a British Prime Minister.
- **We have to remember that** bobbies move around - and slowly.
- One of the arrested people **in fact** was a Hindu, a chef from Hong Kong.

[Back to Table 1](#table-1-categories-of-engagement-moves)

### Proclaim: Endorse
>An utterance which refers to external sources as warrantable, undeniable, and/or reliable. It expresses the writer’s alignment with and endorsement of an attributed proposition. As such, the dialogic space is somewhat narrowed.

Typically, this is achieved by the use of verbal processes and their nominalized equivalents. Compared to `Attribute`, `Endorse` encodes writers more approval of the content.
- Evidence **showed** that . . . there was “a large number of small competitors, the absence of significant price wars, . . .”
- An interview by the Institute of Policy Studies (IPS) concerning national identity **revealed** that 50% of those interviewed feel that they think of themselves more as citizens of the world than any particular country, up from 45% in 1993.
- More specifically, five studies **demonstrate** that investment dependence – investment by foreign firms in a society’s domestic economy increases economic inequality.
- For instance, young learners were **found** to perform differently on both text comprehension (e.g., Langer, 1985) and production (e.g. Hidi & Hidyard, 1983).
- **As** discussants correctly pointed out, Bernardino of Siena, Martin Le Franc, and the anonymous author of the Errores Gazariorum all have an even more aggressive campaign against witches than did the authors of our previous readings.

[Back to Table 1](#table-1-categories-of-engagement-moves)

### Entertain
>An utterance which opens the dialogic space by acknowledging a proposition as one possibility amongst others.
- I **think** Mary teaches French
- You **must** switch off the lights when you leave.
- It was **probably** the most immature, irresponsible, disgraceful and misleading address ever given by a British Prime Minister.
- It **may** have been the most immature, irresponsible, disgraceful and misleading address ever given by a British Prime Minister.
- It **appears** that maximum price fixing does the greatest harm when set below a competitive level.
- That mismatch **seems** worse than it was ten years ago.
- His defensive behaviour **suggests** he feels ashamed and guilty that you’ve discovered his habit.
- **Generally speaking**, if a person repented the church would pardon him or her regardless of how atrocious the crime was.
- I **believe** that he’s lying. 
- He **may** be lying.
- **Probably** he’s lying.
- It’s **probable** that he's lying.
- Of course, there’s **precious little chance** of that happening in America any time soon.
- He has **certainly** disgraced the Attorney General’s office in lending credence to the assertions of the Swift Boat veterans for Truth.

[Back to Table 1](#table-1-categories-of-engagement-moves)

### Attribute
>An utterance which signifies dialogic space as the writer attributes the proposition to an external source.
- Mr. Mandela **said** the Group of Eight nations have a duty to help battle the scourge of AIDS.
- Dawkins **believes** that religion is not an adaptive evolutionary vestige, but in fact a cultural virus.
- Hovenkamp **argues** that a company could have one hundred percent market share both as a newspaper publisher and distributor, and still have no monopoly power.
- **Chomsky’s belief** that language is for individuals rather than groups.
- The government’s serologist **reportedly** lied about his qualifications.
- It is **said** that he lied about his age as he grew older …
- **According to the authors**, he gave new witches everything they wished as long as they sold their soul to him.
- **As** the discussant post “Witchcraft and Sexual Deviance” mentioned, the church and the public believed that if witches were willing to so publicly flout the word of the Lord, they must also disobey other societal conventions.
- **In Wong’s study**, another ‘‘geographical imagination’’ of Lucky Plaza is the view that it is a place where the Filipino maids get to know their ‘boyfriends’.
- A number of researchers (Meara, 1996; Qian, 1999; Read, 1989; Wesche & Paribakht, 1996), **proposed** that the two dimensions of vocabulary knowledge be known as ‘depth’ and ‘breadth’.

Compared to `Endorse`, `Attribute` keeps a neutral stance on the content attributed.

[Back to Table 1](#table-1-categories-of-engagement-moves)

### Justify
>An utterance which engage in persuasion through justification or substantiation.
- **Because** the steps are made of a smooth, polished—and therefore slippery—stone, the BTA should’ve taken precautions to clean the steps in such wintry conditions.
- Accessibility is quite a key factor **because** it is evident that the regional centre was built on the basis of good infrastructure.

[Back to Table 1](#table-1-categories-of-engagement-moves)

### Monogloss
>An utterance which does not employ any value of engagement. Such an utterance ignores the dialogic potential in an utterance.

This is when no engagement resource can be found in the T-unit.
- Teachers are facing the difficult task of providing an optimal learning environment to students from varying social, cultural, and linguistic backgrounds.
- What is interesting in this example is how neither of the two views that are attributed to others is actually endorsed by the author, even though they are entertained and explicated.
- The purpose of maintaining an expansive approach here is clear: the author seeks to present perspectives and research conducted thus far to lay the groundwork for what should be done.
- Television has helped to shrink the relative distance between people and countries.

[Back to Table 1](#table-1-categories-of-engagement-moves)

## Multiple engagement resources in a T-unit
Often times, we will find multiple engagement resources in a single unit (T-unit). 
- **As the name implies (ATTRIBUTE)** **it seemed (ENTERTAIN)** as if eating children was one of the main focuses of anti-witch writings.
- **Even (COUNTER)** **if repenting (ENTERTAIN)**, the person **could (ENTERTAIN)** still be deceived by the devil again, and **would (ENTERTAIN)** return as a threat.
- Output in the English language class **may (ENTERTAIN)** **not (DENY)** always be a productive or necessary use of classroom time
- **Though (COUNTER)** these ideas **may (ENTERTAIN)** **not (DENY)** be driving educational policy, they are inﬂuencing attitudes in ways that have the potential to affect outcomes.


# Part II — Getting ready to annotate

## 1. Some grammatical details
Because meanings of engagement can be expressed at different levels of lexical and grammatical items, we need to know exactly which part of the sentence we should put a tag on.
This section deals with such structural issues during the annotation. Each section below deals with possible grammatical structure for emgagement, and which items to put a tag on.

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
- **Though** there were several ‘couples’, these were deﬁnitely not the norm.
- The Bush administration, **as** we all know, has rejected the Kyoto agreement

### Coordinating conjunctions
When an engagement meaning is realized by a coordinating conjunctions such as *but* and *yet*, you will put a tag on that item.
- **But** look at what he achieved.
- Schools do not serve as avenues for upward mobility, **but** instead reinforce existing social and economic inequalities.

## Some confusing cases (Under construction)

### Pronounce or Entertain
The main difference between pronounce and entertain is whether the utterance allows for dialogic alternatives. Entertain move allows for alternative interpretations or voices by expressing possibilities. Pronounce move, on the other hand, challenges and dismiss an alternative views (contraction). 
- I am **convinced (ENTERTAIN)** that ... :
- I **contend (PRONOUNCE)** that ...


### Endorse or Attribute
The main difference between endorse and attribute concerns the degree of authors approval of the content of the external sources. In ENDORSE, the author refers to the external source and show their alignment to the idea in order to advance their argument and contract the dialogic space. On the other hand, the main rhetorical effect of ATTRIBUTE is more neutral; the author simply make reference to an external sources. 
- The result **demonstrated (ENDORSE)** that ...
- The author **mentioned (ATTRIBUTE)** that ...

### Modal verbs with permissions/obligations are considered as ENTERTAIN

- You **must** switch off the lights when you leave.


## Some typical engagement patterns (Under construction)

### Entertain + Deny ( + maximizer)
`Maximizer` includes adverbs such as *always*, *severely*, etc.
- Output in the English language class **may (ENTERTAIN)** **not (DENY)** **always (MAXIMIZER)** be a productive or necessary use of classroom time

### Deny + Entertain ( + maximiser)
- **Not (DENY)** to do so **may (ENTERTAIN)** **severely (MAXIMIZER)** weaken the ﬁndings of both.

