---
name: grill-me
description: >-
  Use when the user wants to stress-test a plan, decision, idea, or piece of
  writing, says "grill me" / "拷问我", or wants an idea turned into committed
  decisions through a relentless interview.
---
# Grill me (adapted from mattpocock/skills grill-me + grilling, MIT)

Interview the user relentlessly until you reach a shared understanding. Works on anything (software, business calls, applications, writing, life plans); needs no repo and writes no files.

## The design tree
Map the subject as a **design tree**: every decision branches into the decisions that hang off it.

## Work in rounds
- The **frontier** = every decision whose prerequisites are already settled, i.e. questions you can ask now without guessing at unheard answers.
- Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for answers.
- A question that depends on another question still open in this round belongs to a later round.
- After each round, recompute the frontier from scratch; settled decisions unblock new questions. Later rounds should ask things earlier rounds couldn't.
- If the user prefers, switch to one question at a time.

Round format:

```
❓ **Q1** - **<question title>**: <body, may include multiple choices>

➡️ <your recommended answer, with a short reason>

---

❓ **Q2** - ...
```

Word each question so "yes" accepts your recommendation. The user can answer the round by number.

## Facts vs decisions
- Finding **facts** is your job, never the user's. If a question needs a fact from files, the web, or tools, look it up (in the background if slow) instead of asking. Only questions downstream of a pending lookup wait; ask the rest now.
- **Decisions** are the user's. Never answer your own decision questions; put each to them and wait.

## Keep it a conversation
- The user owns the scope. Push back hard on vague or weak answers; challenge assumptions; point out decisions they are making without noticing.
- Watch for passivity ("agreed, agreed"): if they nod along to everything, flag it and ask them to steer.
- "I don't know" is a real answer. For **ungrillable** questions (need something to react to, e.g. how a design feels), stop grilling that branch and suggest making a quick draft/prototype first.
- If the session balloons, the scope is too big: propose splitting it and grilling the pieces.
- No question cap; the user can say wrap up at any time.

## Ending
The session is done when the frontier is empty: every branch visited, nothing silently assumed. Then give a concise summary of every decision made, and ask the user to confirm shared understanding. Do not act on the plan until they confirm.
