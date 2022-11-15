---
layout: default
title: FRAGMENT
parent: Step 1–Clause-boundary detection
nav_order: 5
---

## Fragment

{: .def}
> Fragment here is defined as an indepent line in the annotation data that does not have any clausal element.

This is mostly due to the automatic sentence segmentation issue or syntactic errors in the original essays.

Examples include:
- (Norris, 2009)
- Ibid. (2008, p. 2)
- For example, 
- ,
- p. 36).
- Sincerely,
- Dear Kris,

These are all categorized as Fragment. Since fragment is used to detect any non-clausal, minor textual segments in the data, it won't be used with other categories. That is, when a sentence have at least one `Main`, `Subordinate`, or `Embedded`, that sentence do not get `Fragment`.

{: .note}
> See [Monogloss in fragments](../3_Categories/MONOGLOSS.md#monogloss-in-fragments).

Conversely, the followings are still categorized into `Main` even if they seems they are cut off in the middle:

- The author argues:
- He went to France via 
- No one seems to disagree with the view that 

The examples above are considered `Main` clause because there is at least one [finite verb](1_Basic_grammar.md)—`argues`, `went to`, and `seems`.
We are going to treat these example as 

Note that Empty lines has automatically converted to `EMPTYSENT—Skip Annotation`. When you encounter this, just skip the sentence.


