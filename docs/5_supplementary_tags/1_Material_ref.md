---
layout: default
title: Material references
parent: Step 5–Supplementary tags
nav_order: 1

---



# 1. Reference to information internal or external to the writing

The first category aims to identify the elements of discourse which refers to any internal/external materials. For our purpose, these tags go hand-in-hand with engagement moves such as `ATTRIBUTE` and `ENDORSE`, allowing us to identify whether the writer makes explicit references to the "sources" of their argument.

- `Citations` and `Sources` are two category that pertains to how `EXTERNAL` materials are referenced in the discourse.
- `ENDOPHORIC` pertains to how the writer refers to the other part of its own writing.

| Tag                                          | Description                                                                                   | Examples                                      |
| -------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------- |
| References to external sources               |                                                                                               |                                               |
| ‖—[Citations](#citations)                    | Mentions to external source(s) in the text in forms of in-text or narrative citation.         | `(Martin & White, 2005)`, `Ortega (2009)`,    |
| ‖—[Sources](#sources)                        | Mentions to external source(s) in the text in forms of nominal expression.                    | `The annual report by X`, `Numerous studies`  |
| References text internally                   |                                                                                               |                                               |
| ‖—[Endophoric markers](#endophoric-markers)  | Refer to information in other parts of its own text                                           | as noted `above`, see `Fig 1`, `in section 2` |
| [Quoted](#quoted-materials-or-direct-quotes) | Segment of text with direct quotation (including the quotation marks, both single and double) | `"Stay hungry. Stay foolish."`                |

{: .tips}
> Citation/External source tag subsumes CITATION in the previous (version 1) guideline. It additionally include explicit reference to external materials (e.g., written or oral report, news, discussion, etc.).
> Citation is moved to supplementary category because it can co-occur with `MONOGLOSS`.


## Citations

{: .def}
> Citation is segment of the text where external source(s) are referenced in the text. 

There are several types of citation format to identify in the current corpus. 
In the dataset to annotate, there will be cases where the citation is cut in the middle (e.g., `(Bell &amp;amp.`). 
This is because the automatic system I used to segment the essay into sentences is not perfect. 
In such cases, we will still tag the fragment of the citation as `CITATION`. (see more example of this kind)

### 1. Narrative citation—Author (DATE) pattern
Narrative citation pattern is where author's name is explicitly referenced in the prose. 

The following examples were taken from Nesi (2021):
- **Schapiro et al. (2001)** demonstrated (BAWE code: 3060a SS level 4)
- **Lipton (1991, p.419)** refers (BAWE code: 0177b AH level 3)
- In 1991, **Aram et al. (Menyuk, 1995:4)** reviewed (BAWE code: 6206b AH level 3)
- **Batliwala (1993 cited in Sen, 1997: 2)** brings into focus (BAWE code: 0422a SS level 4)
- **Piaget (as cited in Rubin, LeMare and Lollis, 1990)** offers (BAWE code: 0014c LS level 2)
- **Gisela Bock (in Bridenthal et al., 1984)** argues (BAWE code: 0408f SS level 3)
- quoted by **Aitchison (1989:260)** as claiming (BAWE code: 6055a AH level 1)
- supported by **Kjelsan et al. (2004)** who found (BAWE code: 0014a LS level 2)
- In **Brown et al. (1994)** it says to look for (BAWE code: 3101b SS level 1)
- In another study by **Kerr and MacCoun (1985)** theydemonstrated (BAWE code: 0014e LS level 3)
- **Lloyd and Lishman (1975)** originally demonstrated (BAWE code: 0016a LS level 1)
- Some predictions made by **Robertson et al (1999)** make this even clearer’
- - According to **Jones (1998)**, "students often had difficulty using APA style, especially when it was their first time" **(p. 199)**.


Note: BAWE code shows the writing ID number in the British Academic Written English corpus (Nesi & Gardner, 2012).

### 2. In-text citations—(Author, date) pattern
In-text citations are those which the external sources are cited in parenthetical form.

Nesi (2021) presented the following examples:
- ideas of nationalism often associated with both the ideology and actions of racism **(Fenton, 1999)** 
- the coping technique adopted to achieve what is believed to be desirable **(Gordon, 1990)** 
- his theory on blackbody radiation **(Planck 1900)** for which he was later awarded a Nobel Prize 
- one-third to half of all diabetics already have evidence of organ or tissue damage **(UK Prospective Diabetes Study Group, 1991)**. 

Additionally, you will encounter a various citation format during the annotation.
**MLA (and ASA as closely associated format)**
- Romantic poetry is characterized by the "spontaneous overflow of powerful feelings" **(Wordsworth 263)**.
- Wordsworth extensively explored the role of emotion in the creative process **(263)**.
- Human beings have been described as "symbol-using animals" **(Burke 3)**.
- Marx and Engels described human history as marked by class struggles **(79; ch. 1)**.
- Relativity's theoretical foundations can be traced to earlier work by Faraday and Maxwell **(Einstein 782)**.
- Although some medical ethicists claim that cloning will lead to designer children **(R. Miller 12)**, others note that the advantages for medical research outweigh this consideration **(A. Miller 46)**.
- The authors claim that one cause of obesity in the United States is government-funded farm subsidies **(Franck et al. 327)**.

**IEEE (Note that many of this has already been converted to [#REF] in the data)**
- A trenchcoat and mask can easily disguise a few owls as a human, as experimentally shown by **Smith [1], [2]**.
- Italian owls are suspicious of outsiders, as noted in **[3]–[5]**.
- This is disputed by **Civetta [6]** and **Strix [7]**, who are not owls in masks.
- The city of Florence is under an ancient curse, as repeatedly and exhaustively described in **[8]**, **[10]**, **[13]–[17]**, **[20]**.

### 3.The use of ibid., etc.
`ibid` is sometimes used to indicate the already-referenced materials. 
- His conclusion is that the vegetation was predominantly closed forest, but that some areas such as floodplains and chalklands had more open vegetation **(ibid: 140)**.

When the sentence included references as follows, typically used with `(op.cit.)`, mark the entire sequence as citation:
- **Millington, T., & Sutherland Williams, M., (op.cit.), pp.2**

[Back to Top](#1-reference-to-information-internal-or-external-to-the-writing){: .btn .btn-outline }

---

## Sources 

{: .def}
> Source is segment of the text where source(s) of information are referenced/mentioned in the text in forms of nominalized expressions. 


#### Examples
- **Previous studies** showed ....
- **The annual report by Google** mentioned the possibility of further expansion to...
- According to **the annual report by Google**...
- In **the annual report by Google**...


- When the writer uses a parenthetical form or any in-text citation format, they should be tagged as Citation.

For instance:
- **(Google, 2020)**. => `Citation` rather than `SOURCE`.

[Back to Top](#1-reference-to-information-internal-or-external-to-the-writing){: .btn .btn-outline }

---


## Endophoric markers

NEW in version 2
{: .label .label-green}

{: .def}
> Endophoric markers are text segments (expressions) that refer to information in other parts of its own text

### Description

Endophoric markers are used to mark any mentions to the other parts of its own text. Typically, the marker includes following expressions:

- `(In) Chapter X`, `(In) Part X`, `(In) Section X`, `(In) the X chapter`, `(In) the X part`, `(In) the X section`, `(In) This chapter`, `(In) This part`, `(In) This section`, 
- `Example X`, `Fig.X`, `Figure X`, `P. X`, `Page X`, `Table X`, (these have to be within its own text, and not from external sources.)
- `X above`, `X above`, `X before`, `X below`, `X earlier`, `X later`,

### Examples

- As described **above**, other participants felt financial and psychological constraints that resulted in maintaining what Foucault (1995) recognized as the discipline of routine.
- **Table 5** lists three methods frequently used in the literature.
- Response to Joan Kelly Hall's article by Paul Seedhouse follows **on page 527 of this paper**.
- As discussed **in Chapter 1** and further developed **in Chapter 2**, frequency of occurrence is less important than the contingency between cue and interpretation. (Assumed that these Chapters are from the text itself.)
- As **Table 3** shows, vocabulary size and depth were significantly correlated.
- As **Figure 7** shows, to provide a manual enactment of the literal meaning of “sever,” the teacher raises his right hand off the table, brings it to face level, as if in readiness to cut off a limb, then executes a swift downward chopping movement.
- As illustrated **in Figure 3**, contexts of biliteracy can occur along continua of micro to macro scales, characterized by more oral or written language use and by multiple languages or only monolingual resources—or anywhere in between.
- Consider the italicized expressions of attitude in **example 6**, which were flatly declared and thus presented as “not at issue.”
- **Table 13 below** shows the frequency of the two semantic motives discussed **above** across the four sub-corpora. 
- (29) Nursing and agriculture journals, as noted **earlier in this paper**, often have required sections.


[Back to Top](#1-reference-to-information-internal-or-external-to-the-writing){: .btn .btn-outline }

---

## Quoted materials or Direct quotes

Quoted tags are used to indicate that the materials in that span is NOT the writer's wording, but something borrowed from other sources. 
This tag allows us to separate the writer's own engagement move from the direct quotes of other persons' engagement. 

### SPAN

When you use this tag, put a tag from **the quotation mark which starts the quote** to **the closing quotation mark**. We do not differentiate whether they are single or double quotation marks, or whether it has weirdly formated characters (e.g., `”`, `'`). We will use this tag for a segment of text whether you (as a potential reader) can identify that the segment is NOT the writer's own wording, but borrowed materials. 
If you do not identify the start or end of the quotation in the annotation file, you can indicate this by staring the `QUOTE` tag from the beginning or the end of the annotation file (to indicate the continuation).

[Back to Top](#1-reference-to-information-internal-or-external-to-the-writing){: .btn .btn-outline }
