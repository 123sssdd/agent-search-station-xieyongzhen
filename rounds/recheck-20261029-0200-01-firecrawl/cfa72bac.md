[Sitemap](https://aaronyuqi.medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Faaronyuqi.medium.com%2Ffirst-hand-comparison-of-langgraph-crewai-and-autogen-30026e60b563&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-------------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav--------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Faaronyuqi.medium.com%2Ffirst-hand-comparison-of-langgraph-crewai-and-autogen-30026e60b563&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

[![Aaron Yu](https://miro.medium.com/v2/resize:fill:40:40/2*b4vkP5KsPtAC-xrjzQOAPQ.jpeg)](https://aaronyuqi.medium.com/?source=post_page---post_author_sidebar--30026e60b563-----------------2ca35c724505------------------------)

## Aaron Yu

I am not a coder, but I like solving problems programmably

Follow writer

[Agentic Ai](https://medium.com/tag/agentic-ai?source=post_page---header_tags--30026e60b563-----------------------------------------)

[Genai](https://medium.com/tag/genai?source=post_page---header_tags--30026e60b563-----------------------------------------)

[Multi Agent Systems](https://medium.com/tag/multi-agent-systems?source=post_page---header_tags--30026e60b563-----------------------------------------)

[Langgraph](https://medium.com/tag/langgraph?source=post_page---header_tags--30026e60b563-----------------------------------------)

[Crew Ai](https://medium.com/tag/crew-ai?source=post_page---header_tags--30026e60b563-----------------------------------------)

# First hand comparison of LangGraph, CrewAI and AutoGen

[![Aaron Yu](https://miro.medium.com/v2/resize:fill:32:32/2*b4vkP5KsPtAC-xrjzQOAPQ.jpeg)](https://aaronyuqi.medium.com/?source=post_page---byline--30026e60b563-----------------------------------------)

[Aaron Yu](https://aaronyuqi.medium.com/?source=post_page---byline--30026e60b563-----------------------------------------)

Follow

4 min read

·

Mar 9, 2025

34

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D30026e60b563&operation=register&redirect=https%3A%2F%2Faaronyuqi.medium.com%2Ffirst-hand-comparison-of-langgraph-crewai-and-autogen-30026e60b563&source=---header_actions--30026e60b563---------------------post_audio_button--------------------)

Share

Multi-agent framework become more important as companies are experimenting multi-agent workload for various use cases. There are many popular frameworks in the market now #LangGraph #CrewAI #AutoGen #Swarm #MagenticOne #PydanticAI. I spent some time over the weekend and tested the first three and here are what I have.

As a travel industry practitioner, of course I will use an airline use case: 𝙘𝙧𝙚𝙖𝙩𝙞𝙣𝙜 𝙖 𝙢𝙪𝙡𝙩𝙞-𝙖𝙜𝙚𝙣𝙩 𝙛𝙡𝙤𝙬 𝙩𝙝𝙖𝙩 𝙙𝙤𝙚𝙨 𝙧𝙚𝙨𝙚𝙖𝙧𝙘𝙝, 𝙘𝙤𝙢𝙥𝙤𝙨𝙞𝙩𝙞𝙤𝙣, 𝙖𝙣𝙙 𝙧𝙚𝙫𝙞𝙚𝙬 𝙛𝙤𝙧 𝙖 𝙜𝙞𝙫𝙚𝙣 𝙖𝙞𝙧𝙡𝙞𝙣𝙚. To keep the testing consistent, I used the OpenAI API directly with the same prompts, etc.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*tLF1-fjMNargJLQjaZC8fA.png)

The DAG output from LangGraph, I used the same flow for CrewAI and AutoGen. Of course you can design a more sophisticated Agentic flow, e.g. use an Agent to plan the research, create the task list, have an orchestration agent to coordinate all the agents, etc.

I compared developer experience, startup complexity, state management, agent framework adaptability, and more. However, I didn’t have time to explore more advanced comparisons like memory and tool usage, etc.

𝗛𝗲𝗿𝗲’𝘀 𝘄𝗵𝗮𝘁 𝗜 𝗳𝗼𝘂𝗻𝗱:

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*wA7TxnVwT2DKohkuwgXYmg.png)

🧠 𝗟𝗮𝗻𝗴𝗴𝗿𝗮𝗽𝗵

\- Easy-to-understand DAG function

\- Integrates seamlessly with Langchain

\- Rigid state management — state needs to be well-defined upfront, which can become complex and messy in more intricate agentic networks

\- When used with Langchain, normal pitfalls apply: over-abstraction, unstable memory integration, etc.

\- Memory handling can be tricky due to Langchain’s known issues with memory modules (I tested this before in another prototype, it was not easy to use….)

## Get Aaron Yu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

Remember me for faster sign in

👥 𝗖𝗿𝗲𝘄 𝗔𝗜

\- Clear object structure: Agent, Crew, Task, etc.

\- Logging is a huge pain — normal print and log functions don’t work well inside Task, making debugging difficult

\- Seamless state management with out-of-the-box agent coordination

\- Quick startup time, but tough to refine for complex systems due to poor logging capabilities

\- Well-established memory concept, making memory management more straightforward compared to Langgraph

💻 𝗔𝘂𝘁𝗼𝗴𝗲𝗻

\- Procedural code style — developers must “create” orchestration among agents manually, with no DAG support

\- Gives better control over code compared to other frameworks

\- Initial setup takes longer, and code readability drops as the agentic network grows in complexity

\- Highly extensible with strong tooling support for complex workflows

\- Strong memory handling and tooling support, making it a good fit for advanced use cases

Each framework has its strengths and trade-offs, and the best choice really depends on your project’s needs.

Which of these frameworks have you tried? Do you have a favorite? 💬

The LangGraph code for your reference.

```
import os

import streamlit as st
from langgraph.graph import START, END, StateGraph
from duckduckgo_search import DDGS
from duckduckgo_search.exceptions import DuckDuckGoSearchException
import time
import random
from openai import OpenAI
from typing_extensions import TypedDict

# Configure Streamlit layout with two columns: main content and logs
st.set_page_config(layout="wide")
main_content, log_content = st.columns(2)

# Utility function to log messages in the log content column
def util_st_log(content):
    log_content.markdown(
        f"<div style='font-size:10px; overflow-y: hidden'>{content}</div>",
        unsafe_allow_html=True
    )

# Initialize titles for the app and logs
log_content.title("Logs")
main_content.title("Agentic AI Framework - LangGraph")

# Setup API clients
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
ddgs = DDGS()

# Define state structure
class State(TypedDict):
    search_results: list
    insights: str
    review_feedback: str
    need_review: bool
    iteration: int
    airline: str

# Data gathering agent to fetch search results
class DataGathererAgent:
    def gather_data(self, state: State, max_retries: int = 3):
        airline = state["airline"]
        util_st_log(f"Gathering data for {airline}...")
        queries = [\
            f"{airline} airline history overview",\
            f"{airline} airline leadership structure",\
            f"{airline} airline fleet, routes, market presence",\
            f"{airline} airline revenue, growth, market share",\
            f"{airline} airline partnerships and expansion",\
            f"{airline} airline recent news and updates"\
        ]

        search_results = []
        for query in queries:
            for attempt in range(max_retries):
                try:
                    results = ddgs.text(query, max_results=1)
                    util_st_log(f"Search results for '{query}': {results}")
                    if results:
                        search_results.extend(results)
                    time.sleep(random.uniform(1.0, 3.0))
                    break
                except DuckDuckGoSearchException as e:
                    util_st_log(f"Search error: {str(e)}")
                    if "Ratelimit" in str(e):
                        wait_time = (attempt + 1) * 5
                        util_st_log(f"Rate limit hit. Waiting {wait_time} seconds before retry...")
                        time.sleep(wait_time)
                    if attempt == max_retries - 1:
                        util_st_log(f"Max retries reached for query: {query}. Continuing with available data.")

        if not search_results:
            util_st_log("No search results obtained. Using fallback data.")
            search_results = [{\
                "title": f"About {airline}",\
                "body": f"Fallback information about {airline}. This is placeholder data."\
            }]
        return {"search_results": search_results, "iteration": 0, "insights": "", "review_feedback": None, "airline": state["airline"]}

# Analysis agent to generate insights
class AnalysisAgent:
    def analyze_data(self, state: State):
        search_content = "\n".join([result["body"] for result in state["search_results"] if "body" in result])
        prompt = ("Summarize the following search content about an airline in clear, informative paragraphs.")
        if state["review_feedback"]:
            prompt += f"\n\nFeedback from reviewer: {state['review_feedback']}"

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an expert data analyst."},\
                      {"role": "user", "content": prompt}]
        )

        insights = response.choices[0].message.content
        util_st_log(f"Insights: {insights}")
        return {"search_results": state["search_results"], "insights": insights, "iteration": state["iteration"], "review_feedback": None, "airline": state["airline"]}

# Reviewer agent to review the insights
class ReviewerAgent:
    def review_insights(self, state: State, max_iterations=2):
        review_prompt = ("Review the following airline report for clarity and quality. If revision is needed, start with 'Needs revision'.")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an expert reviewer."},\
                      {"role": "user", "content": state["insights"]}]
        )

        review_feedback = response.choices[0].message.content
        need_revision = "Needs revision" in review_feedback and state["iteration"] < max_iterations

        util_st_log(f"Review feedback: {review_feedback}")
        return {"search_results": state["search_results"], "insights": state["insights"], "iteration": state["iteration"] + 1, "review_feedback": review_feedback if need_revision else None, "airline": state["airline"], "need_review": need_revision}

# Report compiler agent to display the final report
class ReportCompilerAgent:
    def compile_report(self, state: State):
        main_content.title(f"Airline Report for {state['airline']}")
        main_content.write(state["insights"])
        return state

# Instantiate agents
data_gatherer = DataGathererAgent()
analysis_agent = AnalysisAgent()
reviewer_agent = ReviewerAgent()
report_compiler = ReportCompilerAgent()

# Build the state graph
builder = StateGraph(State)
builder.add_node("gather_data", data_gatherer.gather_data)
builder.add_node("analyze_data", analysis_agent.analyze_data)
builder.add_node("review_insights", reviewer_agent.review_insights)
builder.add_node("compile_report", report_compiler.compile_report)

builder.add_edge(START, "gather_data")
builder.add_edge("gather_data", "analyze_data")
builder.add_conditional_edges("analyze_data", lambda state: "review_insights")
builder.add_conditional_edges("review_insights", lambda state: "analyze_data" if state["need_review"] else "compile_report")

graph = builder.compile()

# User input and process trigger
airline = main_content.text_input("Enter the name of an airline", "Cathay Pacific")
if main_content.button("Generate Report"):
    initial_state = {"search_results": [], "insights": "", "iteration": 0, "review_feedback": None, "airline": airline}
    graph.invoke(initial_state)
```

[Agentic Ai](https://medium.com/tag/agentic-ai?source=post_page---footer_tags--30026e60b563-----------------------------------------)

[Genai](https://medium.com/tag/genai?source=post_page---footer_tags--30026e60b563-----------------------------------------)

[Multi Agent Systems](https://medium.com/tag/multi-agent-systems?source=post_page---footer_tags--30026e60b563-----------------------------------------)

[Langgraph](https://medium.com/tag/langgraph?source=post_page---footer_tags--30026e60b563-----------------------------------------)

[Crew Ai](https://medium.com/tag/crew-ai?source=post_page---footer_tags--30026e60b563-----------------------------------------)

[![Aaron Yu](https://miro.medium.com/v2/resize:fill:48:48/2*b4vkP5KsPtAC-xrjzQOAPQ.jpeg)](https://aaronyuqi.medium.com/?source=post_page---post_author_info--30026e60b563-----------------------------------------)

[![Aaron Yu](https://miro.medium.com/v2/resize:fill:64:64/2*b4vkP5KsPtAC-xrjzQOAPQ.jpeg)](https://aaronyuqi.medium.com/?source=post_page---post_author_info--30026e60b563-----------------------------------------)

Follow

[**Written by Aaron Yu**](https://aaronyuqi.medium.com/?source=post_page---post_author_info--30026e60b563-----------------------------------------)

[81 followers](https://aaronyuqi.medium.com/followers?source=post_page---post_author_info--30026e60b563-----------------------------------------)

· [6 following](https://aaronyuqi.medium.com/following?source=post_page---post_author_info--30026e60b563-----------------------------------------)

I am not a coder, but I like solving problems programmably

Follow

[Help](https://help.medium.com/hc/en-us?source=post_page-----30026e60b563-----------------------------------------)

[Status](https://status.medium.com/?source=post_page-----30026e60b563-----------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----30026e60b563-----------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----30026e60b563-----------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----30026e60b563-----------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----30026e60b563-----------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----30026e60b563-----------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----30026e60b563-----------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----30026e60b563-----------------------------------------)

reCAPTCHA

Recaptcha requires verification.

protected by **reCAPTCHA**