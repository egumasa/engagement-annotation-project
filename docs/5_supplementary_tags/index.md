---
layout: default
title: Step 5–Supplementary tags
has_children: true
nav_order: 9
---

## Step 5—Annotatiting Supplementary moves in Engagement resource analysis


NEW in version 2
{: .label .label-green}

The following tags essentially supplement the discourse moves (Step 2-4), so that the entire annotation provide more valuable information about the discourse moves as well as help the machine to identify the engagement resources more confidently.
At the final step of the annotation, we will provide annotation of these supplementary moves. This is set up as an independent layer in webanno, so they are considered conceptually separate from (but supplementary to) Engagement moves.


## Table 2. Categories of Supplementary tags 

### Reference to information internal or external to the writing

- This category of tags aims to identify what elements in the discourse refers to any internal/external materials.
- `Citations` and `Sources` are two category that pertains to how `EXTERNAL` materials are referenced in the discourse.
- `ENDOPHORIC` pertains to how the writer refers to the other part of its own writing.

| Tag                                 | Description                                                                                   | Examples                                      |
| ----------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------- |
| [Citations](CITATION.md)            | Mentions to external source(s) in the text in forms of in-text or narrative citation.         | `(Martin & White, 2005)`, `Ortega (2009)`,    |
| [Sources](Sources.md)               | Mentions to external source(s) in the text in forms of nominal expression.                    | `The annual report by X`, `Numerous studies`  |
| [Endophoric markers](ENDOPHORIC.md) | Refer to information in other parts of its own text                                           | as noted `above`, see `Fig 1`, `in section 2` |
| [Quoted](QUOTED.md)                 | Segment of text with direct quotation (including the quotation marks, both single and double) | `"Stay hungry. Stay foolish."`                |

{: .tips}
> Citation/External source tag subsumes CITATION in the previous (version 1) guideline. It additionally include explicit reference to external materials (e.g., written or oral report, news, discussion, etc.).
> Citation is moved to supplementary category because it can co-occur with `MONOGLOSS`.

### Text organizing devices 

- Text organizing devices includes "discourse signals" that "refers to discourse acts, sequencing, and text-stages" (or what Hyland's called `framemarkers`; Hyland, 2005)
- The following tags are used when we interpret the writer's intension is to let the reader know about the organization of its own text itself (independent from the content of the argument).

| Tag                                         | Description                                                         | Examples                                                                                                          |
| ------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| [Goal-announcing](GOAL.md)                  | Signal the purpose/goals of the text itself                         | `my purpose is`, `Section 2 describes`, `the chapter/section focuses/proposes`, `we intend to`, `in this chapter` |
| [Text-sequencing/staging](TEXT-SEQUENCE.md) | Refer to sequences and stages of argumentative elements in the text | `First`, `Lastly`, `to start with`, `so far`, `overall`,                                                          |

### Logical connections/ Transition phrases

- Tags in this categories are those that the writer uses to cohesively link between their ideas and argumentative elements. So, these tags are more relevant to the actual content of the argument (compared to `Text organizing devices` above).
- Here we are dealing with logical connections that were NOT the foci of ENGAGEMENT moves (e.g., `COUNTER`).

| Tag                             | Description                                                         | Examples                                                             |
| ------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------- |
| [Summative**](SUMMATIVE.md)     | Signal summaries in the part of the text                            | `to conclude`, `in short`, `to sum up`, `The conclusion is`          |
| [Exemplifying](EXEMPLIFYING.md) | Signal illustrations/examples in the text                           | `for example`, `to illustrate`, `e.g.`,                              |
| [Expository](EXPOSITORY.md)     | Signal elaboration/clarification in the subsequent part of the text | `in other words`, `that is`, `i.e.`, `I mean`, `this means`          |
| Compare/Contrast                | Signal                                                              |                                                                      |
| [Justifying](JUSTIFY.md)        | Signal persuasion through justification or substantiation.          | `because of X`, `due to X`, `therefore`                              |
| [Purpose/Result](PURPOSE.md)    | Signal Purposes and Result                                          | `as a result`, `for that purpose`, `in order to X`                   |
| [Temporal markers](TEMPORAL.md) | Refer to when an event happened                                     | `First`\*, `At last`, `finally`\*, `then`, `next time`, `previously` |


{: .tips}
> Justifying is equivalent to the `JUSTIFY` tag in the previous version (ver 1). The reason for this change is based on the observation that `JUSTIFY` can co-occur with `MONOGLOSS`, which suggests the distinct roles of justification.


Notes: 
`*` in the table shows that the item's function needs to be carefully examined in the immediate context.
`**` Summative may have both Text-organizing function as well as logical function, but we use the same tag.

### Notes on theoretical framework

- Goal-announcing and text-sequencing and staging are based on Frame markers in Hyland (2005).
- Endophoric markers are based on Hyland (2005).
- Citations and Sources are related to Evidentials in Hyland (2005), but they are distinct given that Evidential is covered in Engagement (or ATTRIBUTE).

## References

Hyland, K. (2005). Metadiscourse: Exploring interaction in writing. Continuum.

