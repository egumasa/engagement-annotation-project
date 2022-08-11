---
layout: default
title: Archives–Part5—Modal sense disambiguation
parent: Archives
nav_order: 25
---
# Modal sense disambiguation

Modal verbs in English are tricky because the form and function do not have one-to-one correspondence. 
In Engagement annotation, we will annotate the semantic/functional categories of the modal verbs before assigning them into Engagement class.

## List of modal verbs

In order to better classify modal verbs into different engagement categories (`Entertain` or not), we will classify the senses of modal verb.
Following Halliday & Mathiessen (2014, p. 145), the following items are considered as modal verbs (Modal operators) in this project:
- can, may, could, might, (dare), will, would, should, is to, was to, must, ought to, need to, have/has/had to
- needn't, don't need to, don't have to, won't, wouldn't, shouldn't, (isn't/wasn't), mustn't, oughtn't to, can't, couldn't, (mayn't, mightn't, haven't to).

## Semantic classes and how to deal with them

There are three types in modal sense classification.

| Class     | General Meaning                                 | Engagement tag                        |
| :-------- | :---------------------------------------------- | :------------------------------------ |
| Epistemic | probability, possibility, speaker's jusdgements | ENTERTAIN                             |
| Deontic   | request, permission, obligation                 | ENTERTAIN                             |
| Dynamic   | ability, willingness,                           | Leave untagged for Engagement for now |

The annotation will happen in two-step manner. 

1) For each occurrence of modal verbs, assign modal sense classes from `Epistemic`, `Deontic`, `Dynamic:Capacity`, or `Dynamic:Willingness`.

2) `Epistemic` and `Deontic` modal verbs are then categorized as `ENTERTAIN` for the Engagement layer. The rest of the modal verbs will be left untagged at the Engagement layer.

## Epistemic modal — Modal of probability and possibility

`Epistemic` modal can be identified "using a paraphrase such as: “someone is likely/ unlikely to do something”, or “something is likely/possible/(im)probable to happen/to be the case”" (p. 10).
Sometimes this category also indicates `assumption` or `deduction` by the speaker.

- Geez, Buddha **must** be so annoyed!
- He **may** be home by now.
- Someone is knocking at the door. That **will** be John.
- This manuscript is damned hard to read. **Maybe** some more light can help.
- John **may/must** have been in his office. 
- Mary **ought to / should / could** be at school by now. 
- He **can't** be in his office now. (Palmer, 2001, p. 15)
- They **'ll** be in the office. (They always are at this time)
- It **can** rain very hard in winter.

## Deontic modal — Modal of request, permission and obligation

Deontic modality has two sub-classes: request and permission. "Deontic modality is directive in that the event is controlled by circumstances external to the subject of the sentence (more strictly the person or persons identified by the subject)." (Palmer, 2003, p.7).

`Request` can be identified "using as paraphrase: “need to do something” or “it is required to do something”" (p. 10).

`Permission` can be identified "using as paraphrase: “allow/don’t allow somebody to do something”"

According to Martin & White (2005), deontic modal is categorized as `Entertain`.
- We **must** have clear European standards.	(obligation)
- You **may** enter this building.	(permission)
- We **should** be thankful for what he has done for us, so we must find a way to show our gratitude to him.	(obligation)
- John **may/can** come in now. (permission)
- John **must** come in now.	(obligation)
- You **can** smoke in here. (permission)
- You **needn't/ don't have to** come in.
- You **need to** do the following before the exam.

## Dynamic modal – Modal of capability, ability, and willingness

`Dynamic` modal can be identified "using the paraphrase “be (un)able to do something”" (p. 10).
They typically relates to the `capacity` of the subject-participant of the clause.
The control of the event is internal to the subject; that is, capacity and willingness is internal to the subject.

- They **ca**n’t even read them.	(ability)
- That kid **can** sing like Frank Sinatra.	(ability)
- She **can** run a mile in four minutes. (ability)
- I **will** do it for you.	(willingness)
  
## Confusing cases 
To be updated...
### Dynamic vs. deontic `can`


- You can do this, if you want.
  
### Epistemic vs. Dynamic `could`


- He could have arrived in time.

### Epistemic vs deontic `should` –This is less important because they will be ENTERTAIN anyway.


- He should be aware of the issue.
