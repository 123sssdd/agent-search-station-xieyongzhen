[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40danieldkang%2Fai-agent-benchmarks-are-broken-c1fedc9ea071&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-------------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav--------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40danieldkang%2Fai-agent-benchmarks-are-broken-c1fedc9ea071&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[![Daniel Kang](https://miro.medium.com/v2/resize:fill:80:80/1*8sAXYMCZGbP8K09lihLN-Q.jpeg)](https://medium.com/@danieldkang?source=post_page---post_author_sidebar--c1fedc9ea071-----------------15128583ec9e------------------------)

## Daniel Kang

Follow writer

# AI Agent Benchmarks are Broken

[![Daniel Kang](https://miro.medium.com/v2/resize:fill:64:64/1*8sAXYMCZGbP8K09lihLN-Q.jpeg)](https://medium.com/@danieldkang?source=post_page---byline--c1fedc9ea071-----------------------------------------)

[Daniel Kang](https://medium.com/@danieldkang?source=post_page---byline--c1fedc9ea071-----------------------------------------)

Follow

5 min read

·

Jul 8, 2025

9

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dc1fedc9ea071&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40danieldkang%2Fai-agent-benchmarks-are-broken-c1fedc9ea071&source=---header_actions--c1fedc9ea071---------------------post_audio_button--------------------)

Share

[Benchmarks](https://dl.acm.org/doi/10.1145/2209249.2209271) are foundational to evaluating the strengths and limitations of AI systems, guiding both [research](https://direct.mit.edu/daed/article/151/2/85/110602/Searching-for-Computer-Vision-North-Stars) and [industry](https://www.anthropic.com/news/claude-4) development. As AI agents move from research demos to [mission](https://developer.nvidia.com/blog/automating-gpu-kernel-generation-with-deepseek-r1-and-inference-time-scaling/)- [critical](https://openai.com/index/computer-using-agent/) [applications](https://www.anthropic.com/claude-code), researchers and practitioners are building benchmarks to evaluate their capabilities and limitations. These AI agent benchmarks are significantly more complex than traditional AI benchmarks in task formulation (e.g., often requiring a simulator of realistic scenarios) and evaluation (e.g., no gold label), requiring greater effort to ensure their reliability.

Unfortunately, many current AI agent benchmarks are far from reliable. Consider [WebArena](https://webarena.dev/), a benchmark used by [OpenAI](https://openai.com/index/computer-using-agent/) and others to evaluate AI agents on interactions with websites. In [a task to calculate the duration of a route](https://ibm-cuga.19pc1vtv090u.us-east.codeengine.appdomain.cloud/html/render_82.html), an agent answered “45 + 8 minutes” and was marked correct by WebArena, although the correct answer is “63 minutes.” Moreover, among 10 popular AI agent benchmarks (e.g., SWE-bench, OSWorld, KernelBench, etc.), we found severe issues in 8 of them, causing in some cases up to 100% misestimation1 of agents’ capabilities.

These numbers make one thing clear: to understand an agent’s true abilities, we must build AI agent benchmarks in a more rigorous way.

How do we build AI agent benchmarks we can trust? In our [recent work](https://arxiv.org/abs/2507.02825), we break down the failure modes in current AI agent benchmarks and introduce a checklist that minimizes the gamability of AI agent benchmarks and ensures they measure what they claim to measure. In future posts, we will provide recommendations for creating AI agent benchmarks we can trust!

## How do Current AI Agent Benchmarks Fail?

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/0*0gufbICGjBokFfA1)

_Operational and conceptual processes of AI agent evaluation. Task and outcome validity are essential to ensure that benchmark results truly reflect agents’ capabilities._

In AI agent benchmarks, agents are asked to complete tasks end-to-end, such as [fixing a code issue in a large repository](https://www.swebench.com/original.html) or [creating a travel plan](https://webarena.dev/).

This ambitious scope creates two challenges that traditional AI benchmarks rarely face:

1. _Fragile simulators_: Tasks often run inside simulated/containerized websites, computers, or databases. If these mini-worlds are buggy or outdated, an agent can simply find a shortcut to pass or find the task impossible.
2. _No easy “gold” answer_: Task solutions may be code, API calls, or paragraph-long plans, which don’t fit a fixed answer key.

Given these challenges, we propose two validity criteria that are particularly important for AI agent benchmarks:

_Task Validity_: Is a task solvable _if and only if_ the agent possesses the target capability?

> Example failure: [τ-bench](https://sierra.ai/resources/research/tau-bench) scores a “do-nothing” agent as correct on 38% of airline tasks, even though the trivial agent does not understand the airline ticketing policy.

_Outcome Validity_: Does the evaluation result (e.g., tests or checks) truly indicate task success?

> Example failure: As shown in the example before, [WebArena](https://webarena.dev/) partially relies on LLM-as-a-Judge that makes mistakes for problems as simple as “45+8≠63.”

## Our Research: AI Agent Benchmark Checklist

We curated the AI agent Benchmark Checklist (ABC), a 43-item checklist based on 17 AI agent benchmarks used by leading AI providers. ABC consists of three parts: outcome-validity checks, task-validity checks, and benchmark reporting guidelines for cases where perfect validity is extremely challenging or impossible.

## Get Daniel Kang’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

Remember me for faster sign in

The full, print-friendly checklist is publicly available [online](https://uiuc-kang-lab.github.io/agentic-benchmarks/assets/checklist.pdf).

## An Overview of Our Findings via ABC

We applied ABC on ten popular AI agent benchmarks, including SWE-bench Verified, WebArena, OSWorld, and more.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/0*aS52w2lgqlzfsgKj)

_Results of applying ABC on ten widely used AI agent benchmarks._

Out of the 10 benchmarks, we found:

1. 7/10 contain shortcuts or impossible tasks.
2. 7/10 fail outcome validity.
3. 8/10 fail to disclose known issues.

Here is a summary of issues we identified in benchmarks that are used to evaluate frontier AI agent systems, including Claude Code and OpenAI Operator.

**SWE-bench** and **SWE-bench Verified** use manually crafted unit tests to evaluate the correctness of agent-generated code patches. Agent-generated code patches can have bugs not captured by unit tests, as shown in the following example. By [augmenting unit tests](https://arxiv.org/abs/2506.09289), we observed significant ranking changes in the leaderboard, affecting 41% agents for SWE-bench Lite and 24% for SWE-bench Verified.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/0*U4fBo2JtFsmH5gug)

_The IBM SWE-1.0 agent produces an incorrect solution not captured by SWE-bench, since the unit tests do not cover the red branch._

**KernelBench** uses tensors with random values to evaluate the correctness of agent-generated kernel code written in CUDA. Similar to SWE-bench Verified, random-valued tensors may fail to capture bugs in the generated kernel, especially for memory- or shape-related issues.

**τ-bench** uses substring matching and database state matching to evaluate agents, which allows a do-nothing agent to pass 38% of tasks. The following example demonstrates one of these tasks.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/0*4g8y6VvQuI06HeGg)

_A task example in τ-bench where a trivial agent that does nothing can pass the evaluation._

**WebArena** uses strict string matching and a naive LLM-judge to evaluate the correctness of agents’ actions and outputs, which leads to 1.6–5.2% misestimation of agents’ performance in absolute terms.

**OSWorld** develops agent evaluation partially based on outdated websites, resulting in a 28% underestimation of agents’ performance in absolute terms. In the following example, the CSS class, search-date, has been removed from the website the agent interacts with. Because the evaluator still relies on an outdated selector, it marks the agent’s correct actions as incorrect.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/0*xfnfYQUub9UXhv96)

**SWE-Lancer** fails to securely store test files, which allows an agent to overwrite tests and pass all tests.

## Next Steps with ABC

We build ABC as an actionable framework to help

1. Benchmark developers troubleshoot potential issues or demonstrate their thorough work.
2. Agent/Model developers dive into the underlying benchmarks deeply beyond reporting a “start-of-the-art” number.

Please check our [paper](https://arxiv.org/abs/2507.02825) for details. The full checklist, code examples, and the growing registry of assessed benchmarks live at our [GitHub repository](https://github.com/uiuc-kang-lab/agentic-benchmarks). If you are interested in adding exploit or fix patches to existing benchmarks, please submit a PR to our repository!

We invite contributions, issue reports, and pull requests! Reach out to us if you are interested in using or iterating on ABC.

_Written by the ABC authors_

[![Daniel Kang](https://miro.medium.com/v2/resize:fill:96:96/1*8sAXYMCZGbP8K09lihLN-Q.jpeg)](https://medium.com/@danieldkang?source=post_page---post_author_info--c1fedc9ea071-----------------------------------------)

[![Daniel Kang](https://miro.medium.com/v2/resize:fill:128:128/1*8sAXYMCZGbP8K09lihLN-Q.jpeg)](https://medium.com/@danieldkang?source=post_page---post_author_info--c1fedc9ea071-----------------------------------------)

Follow

[**Written by Daniel Kang**](https://medium.com/@danieldkang?source=post_page---post_author_info--c1fedc9ea071-----------------------------------------)

[451 followers](https://medium.com/@danieldkang/followers?source=post_page---post_author_info--c1fedc9ea071-----------------------------------------)

· [11 following](https://medium.com/@danieldkang/following?source=post_page---post_author_info--c1fedc9ea071-----------------------------------------)

Follow

[Help](https://help.medium.com/hc/en-us?source=post_page-----c1fedc9ea071-----------------------------------------)

[Status](https://status.medium.com/?source=post_page-----c1fedc9ea071-----------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c1fedc9ea071-----------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c1fedc9ea071-----------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----c1fedc9ea071-----------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c1fedc9ea071-----------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----c1fedc9ea071-----------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c1fedc9ea071-----------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----c1fedc9ea071-----------------------------------------)

reCAPTCHA

Recaptcha requires verification.

protected by **reCAPTCHA**