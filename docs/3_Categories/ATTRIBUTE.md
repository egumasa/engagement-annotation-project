---
layout: default
title: Expand–ATTRIBUTE
parent: Step 3–Engagement categories
nav_order: 9

---

### Attribute

EXPANSION
{: .label .label-blue }

{: .def}
>An utterance which signifies dialogic space as the writer attributes the proposition to an external source.

Attribute is another expansion strategy. In this move, the writer presents an idea as a version of the truth by (explicitly or implicitly) referring to an external source (e.g., other authors/studies). The attribution can be made to some unspecified sources (see [below](#hear-say-as-attribute)). The writer essentially have no stake in reporting the idea. This can be contrasted with [`ENDORSE`](../3_Categories/ENDORSE.md), where the author shows greater alignments to the attributed idea as a valid and reliable one (hence contraction).

Typically, this move is achieved by "X [third person] says/reports/states/declares/announces" or "According to X", which shows that the idea is borrowed from the external source.
Martin & White (2005) says: "Under the heading of ‘attribution’, we deal with those formulations which disassociate the proposition from the text’s internal authorial voice by attributing it so some external source."

{: .note}
><span style="color:red">Red text</span> is used to mark a [supplementary material reference tags](../5_supplementary_tags/1_Material_ref.md) like [sources](../5_supplementary_tags/1_Material_ref.md/#sources) or [citation](../5_supplementary_tags/1_Material_ref.md#citations). **<span style="color:red">Bolded red text</span>** is used to show when the material reference is part of the span of attribute. See [this section](../5_supplementary_tags/1_Material_ref.md#sources-and-citations-as-supplementing-attribute-and-endorse-move) for more information about how material references interact with attribute.

In many cases, `ATTRIBUTE` occurs where the author explicitly mention the source of information and ackowledge that the original idea is theirs.
- <span style="color:red">[ Mr. Mandela ]SOURCE </span> **[ said ]ATTRIBUTE-PRIMARY** the Group of Eight nations have a duty to help battle the scourge of AIDS.
- <span style="color:red">[ Dawkins ]SOURCE </span> **[ believes ]ATTRIBUTE-PRIMARY** that religion is not an adaptive evolutionary vestige, but in fact a cultural virus.
- <span style="color:red">[ Most linguists ]SOURCE </span> **[ believe ]ATTRIBUTE-PRIMARY** that linguistic structure is most productively studied in its own terms, with its communicative use(s) considered separately.
- <span style="color:red">[ Hovenkamp ]SOURCE </span> **[ argues ]ATTRIBUTE-PRIMARY** that a company could have one hundred percent market share both as a newspaper publisher and distributor, and still have no monopoly power.
- **[ According to <span style="color:red">[ the authors ]SOURCE </span> ]ATTRIBUTE-PRIMARY**, he gave new witches everything they wished as long as they sold their soul to him.
- **[ As <span style="color:red"> the discussant post “Witchcraft and Sexual Deviance</span>” mentioned ]ATTRIBUTE-PRIMARY**, the church and the public believed that if witches were willing to so publicly flout the word of the Lord, they must also disobey other societal conventions.
- <span style="color:red"> [ Tickner ]SOURCE </span>**[ has claimed ]ATTRIBUTE-PRIMARY** that_ regardless of the result, the royal commission was a waste of money and he would proceed with a separate inquiry into the issue headed by Justice Jane Matthews.
- **[ In <span style="color:red">[ Wong's study ]SOURCE </span> ]ATTRIBUTE-PRIMARY**, another ‘‘geographical imagination’’ of Lucky Plaza is the view that it is a place where the Filipino maids get to know their ‘boyfriends’.
- In response to **[ <span style="color:red">[ Jackson ]SOURCE </span>'s assertion ]ATTRIBUTE-SECONDARY** that African Americans had progressed a lot in eighty odd years, <span style="color:red">[ Young ]SOURCE </span> **[ interrupted ]ATTRIBUTE-PRIMARY** him again and **[ informed ]ATTRIBUTE-PRIMARY** him, "we are not going to wait eighty more years, I will tell you that."

##### Hear-say as ATTRIBUTE
In some cases, the author can present the idea without specifying the sources (but still present it as something they hear about).
- **[ It is said ]ATTRIBUTE-PRIMARY** that he lied about his age as he grew older …
- The government’s serologist **[ reportedly ]ATTRIBUTE-PRIMARY** lied about his qualifications.
- **[ It is generally understood ]ATTRIBUTE-PRIMARY** that science has developed a highly sophisticated way of representing ideas.

##### Implicit attribution
Updated on May 30th
{: .label .label-green}

Additionally, `ATTRIBUTE` would include some implicit attribution like the followings:
- <span style="color:red">[ Van de Kooi and Knorr (1973) ]CITATION </span> **[ measured ]ATTRIBUTE-PRIMARY** one office building and five small dwellings over a period from February 1967 to August 1967 in The Netherlands.

&rarr; This can be interpreted as "Van de Kooi and Knorr (1973) **(reported that they)** measured ~." So, in the annotation, we will tag **measured** as `ATTRIBUTE` (see Hood, 2010, p. 181).

- <span style="color:red">[ Anderson (2004) ]CITATION </span> **[ offers ]ATTRIBUTE-PRIMARY** a number of suggestions.

&rarr; Here, **offer + suggestion** can be interpreted as `abstract representation` (called `grammatical metaphor`) of Anderson suggested many things. So, in the annotation we will put `ATTRIBUTE` tag on **offers**.


Compared to [`Endorse`](../3_Categories/ENDORSE.md), `Attribute` keeps a neutral stance on the content attributed.

##### Attribution using prepositional phrase

Some prepositional phrases signaling (metaphorical) locations, can be treated as `ATTRIBUTE`, when that location is an external source.
This include following examples:

- **[ In <span style="color:red">[ Wong's study ]SOURCE </span> ]ATTRIBUTE-PRIMARY**, another ‘‘geographical imagination’’ of Lucky Plaza is the view that it is a place where the Filipino maids get to know their ‘boyfriends’.
- **[ In <span style="color:red">[ recent research ]SOURCE </span> on human evolution ]ATTRIBUTE-PRIMARY** , unique abilities for exact imitation contributed signally to our unique evolutionary trajectory.

{: .note}
> The span of [sources] will not include the section of the noun phrase following the noun. In the above example, the span of source is limited to **<span style="color:red">recent research</span>**. If we included the whole noun phrase **<span style="color:red">recent research on human evolution</span>** as the span, then consistenly tagging the whole noun phrase would be a slippery slope of tagging larger spans, running the risk of ultimately harming ML/AI models: **<span style="color:red">recent research... that I read... in English... on human evolution... in the Americas... the other day... ect.</span>**

> **This rule is a work in progress and may currently be inconsistent in the guidelines.** 

##### Parataxis as ATTRIBUTE
`Attribute` can occur when an author interrupts reported speech content to attribute the source of that content. 

- These initiatives, **[ <span style="color:red">[ President Gorge W. Bush ]SOURCE </span> declared ]ATTRIBUTE-PRIMARY**, would "improve student's knowledge of America history, increase their civic involvement, and deepen their love for our great country."
- Witholding that support, **[ <span style="color:red">[ The court ]SOURCE </span> confesses ]ATTRIBUTE-PRIMARY**, "precludes the maintenance of our federal system" of legitimized judicial supremacy. [#REF 4]

##### Secondary ATTRIBUTE

[Shell nouns](../2_Spans/NOUN_gp.md#shell-nouns-nominalized-construction) take secondary attribute.

- They find support for **[ <span style="color:red">[ their ]SOURCE </span> hypothesis ]ATTRIBUTE-SECONDARY** that the hiring process is the easiest organizational point to discriminate against women.
- Linguists differ in their opinions about **[ <span style="color:red">[ Chomsky ]SOURCE </span>'s belief ]ATTRIBUTE-SECONDARY** that language is for individuals rather than groups.

[Back to Table 1](index.md#table-1-categories-of-engagement-moves){: .btn .btn-outline }
