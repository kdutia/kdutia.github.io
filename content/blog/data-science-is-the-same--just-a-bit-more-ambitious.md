+++
date = '2025-09-02T09:01:23+01:00'
draft = true
title = 'data science is the same with LLMs, just a bit more ambitious'
+++

I recently co-organised the [2nd Climate NLP workshop](https://aclanthology.org/volumes/2025.climatenlp-1/) at [ACL](https://en.wikipedia.org/wiki/Association_for_Computational_Linguistics), and we had the good fortune of having a very senior researcher in the field on the organising committee – who also agreed to be part of a panel called *The Future of NLP Research*. His answer to one of the questions on this panel made me think *a lot* about my work as someone working on NLP, so much that I thought it was worth sharing through writing.

The question, and answer were:

> **panel host:** What are the most pressing challenges in NLP, and what advice would you give to researchers starting in the field?
>
> **researcher:** With modern NLP we have more purchase to understand arguments, what makes them persuasive or less persuasive, and how they shape debates and opinions. **The time of LLMs is a time of opportunity, as we can do much more powerful things with language.**

*(emphasis my own)[^1]*

I've not really stopped thinking about that answer since. It lifted a lot of the weirdness around working on applied social impact NLP in the last few years. Going from a place where working on social impact NLP felt like you were one of a few hundred people tackling the niche problems that come when you try to do *✨ machine learning ✨* in a context that's not really set up or resourced for what you're doing, to suddenly being surrounded by people doing similar things to you – and wondering what your role as a 'traditional' data scientist is.

To me, there are 3 parts to how data science is the same with LLMs, but also a bit more ambitious.

- [The tasks haven't really changed](#the-tasks-havent-really-changed) (the same)
- [Pretty much anyone now do NLP](#pretty-much-anyone-can-now-do-nlp) (different; good!)
- [Applied NLP needs to be supported by good science](#applied-nlp-needs-to-be-supported-by-good-science) (also the same)

## The tasks haven't really changed

For applied NLP, the tasks we're tackling are broadly the same. This won't be news to you if you were working on NLP before around 2021, and doesn't apply so much to *research* in NLP. But, with each AI buzzword seeming to get more attention, a refresher was definitely helpful for me.

Let's break down some tasks:

- **retrieval augmented generation** is:
  - search a.k.a. [information retrieval](https://en.wikipedia.org/wiki/Information_retrieval), plus
  - automatic summarisation, which has been around since the 1950s [^2]

- **AI agents** are:
  - query reformulation (i.e. rewriting a human's query to better suit a system), around since the 1960s [^3]
  - search (again!)

- **text classification** is, well, still text classification

The tasks being broadly the same as they always were means that in almost all instances there's *decades* worth of smart humans thinking about the problem you're trying to tackle with an LLM. There are benchmarks, UX studies, and thoughts about ethics and potential harms which all still apply to a modern system.

## Pretty much anyone can now do NLP

With LLMs, the barrier to entry to get near to state-of-the-art performance on many NLP tasks to anyone who can write a prompt template, and populate it with some input text and any other variables. This goes for most of the tasks above (classification, query reformulation and tool use) as well as tasks that used to require heavy knowledge of linguistics, statistics or both (coreference resolution, named entity recognition, relation extraction, word sense disambiguation...).

Working in an applied setting, this is great! We've got a whole team of people who spend their days thinking about climate and nature policy, and now they're able to train their own classifiers. *And* we've got a whole team of people who think about building impactful research tools and thinking about their users – and they can do NLP too. I won't write any more on this, as Drew Breunig [has already put it better](https://www.dbreunig.com/2025/04/10/the-domain-experts-are-drivers.html) (via Simon Willison).

What does that mean for the applied data scientist? We should focus more on ensuring our domain experts have a good understanding of ML models and how to use them, we should help them be able to write prompts they can run against our data, and we need to support them with good science 👇.

## Applied NLP needs to be supported by good science

(measurement science, plus human science)

---

[^1]: To add a bit more context, this was said at a climate workshop, where some of the big challenges are tackling misinformation and public debate.

[^2]: Section 3.1.1, https://arxiv.org/abs/2406.11289v1

[^3]: https://www.sciencedirect.com/science/article/abs/pii/S0306457318305466