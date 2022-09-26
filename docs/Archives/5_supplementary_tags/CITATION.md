---
layout: default
title: Citations
parent: Step 5–Supplementary tags
nav_order: 1

---

## Citations

{: .def}
> Citation is segment of the text where external source(s) are referenced in the text. 

There are several types of citation format to identify in the current corpus. 
In the dataset to annotate, there will be cases where the citation is cut in the middle (e.g., `(Bell &amp;amp.`). 
This is because the automatic system I used to segment the essay into sentences is not perfect. 
In such cases, we will still tag the fragment of the citation as `CITATION`. (see more example of this kind)

#### 1. Narrative citation—Author (DATE) pattern
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

#### 2. In-text citations—(Author, date) pattern
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

#### 3.The use of ibid., etc.
`ibid` is sometimes used to indicate the already-referenced materials. 
- His conclusion is that the vegetation was predominantly closed forest, but that some areas such as floodplains and chalklands had more open vegetation **(ibid: 140)**.

When the sentence included references as follows, typically used with `(op.cit.)`, mark the entire sequence as citation:
- **Millington, T., & Sutherland Williams, M., (op.cit.), pp.2**



## Bibliographical References

The illustrative examples were taken from:
- Nesi, H. (2021). Sources for courses: Metadiscourse and the role of citation in student writing. Lingua, 253, 103040. https://doi.org/10.1016/j.lingua.2021.103040
