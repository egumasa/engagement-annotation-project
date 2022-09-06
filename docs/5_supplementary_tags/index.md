---
layout: default
title: Step 5–Supplementary tags
has_children: true
nav_order: 9
---

## Step 5—Annotatiting Supplementary moves in Engagement resource analysis

The following tags essentially supplement the discourse moves (Step 2-4), so that the entire annotation provide more valuable information about the discourse moves as well as help the machine to identify the engagement resources more confidently.
At the final step of the annotation, we will provide annotation of these supplementary moves. This is set up as an independent layer in webanno, so they are considered conceptually separate from (but supplementary to) Engagement moves.


## Table 2. Categories of Supplementary tags 

### Reference to information internal or external to the writing

| Tag                | Description                                                                                   | Examples                                     |
| ------------------ | --------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Citations          | Mentions to external source(s) in the text in forms of in-text or narrative citation.         | `(Martin & White, 2005)`, `Ortega (2009)`,   |
| Sources            | Mentions to external source(s) in the text in forms of nominal expression.                    | `The annual report by X`, `Numerous studies` |
| Endophoric markers | Refer to information in other parts of its own text                                           | `noted above`, `see Fig 1`, `in section 2`   |
| QUOTED             | Segment of text with direct quotation (including the quotation marks, both single and double) |                                              |

{: .tips}
> Citation/External source tag subsumes CITATION in the previous (version 1) guideline. It additionally include explicit reference to external materials (e.g., written or oral report, news, discussion, etc.).
> Citation is moved to supplementary category because it can co-occur with `MONOGLOSS`.

### Text organizing devices

| Tag                     | Description                                                         | Examples                                                                                                          |
| ----------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Goal-announcing         | Signal the purpose/goals of the text itself                         | `my purpose is`, `Section 2 describes`, `the chapter/section focuses/proposes`, `we intend to`, `in this chapter` |
| Text-sequencing/staging | Refer to sequences and stages of argumentative elements in the text | `First`, `Lastly`, `to start with`, `so far`, `overall`,                                                          |
| Temporal markers        | Refer to when an event happened                                     | `First`\*, `At last`, `finally`\*, `then`, `next time`, `previously`                                              |

### Logical connections/ Transition phrases

| Tag            | Description                                                | Examples                                                    |
| -------------- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| Summative      | Signal summaries in the part of the text                   | `to conclude`, `in short`, `to sum up`, `The conclusion is` |
| Exemplifying   | Signal illustrations/examples in the text                  | `for example`, `to illustrate`, `e.g.`,                     |
| Expository     | Signal elaboration in the subsequent part of the text      | `in other words`, `that is`, `i.e.`, `I mean`, `this means` |
| Justifying     | Signal persuasion through justification or substantiation. | `because of X`, `due to X`, `therefore`                     |
| Purpose/Result | Signal Purposes and Result                                 | `as a result`, `for that purpose`, `in order to X`          |

{: .tips}
> Justifying is equivalent to the `JUSTIFY` tag in the previous version (ver 1). The reason for this change is based on the observation that `JUSTIFY` can co-occur with `MONOGLOSS`, which suggests the distinct roles of justification.


Note: * in the table shows that the item's function needs to be carefully examined in the immediate context.



