
from typing import Literal
from langgraph.types import Command
from state import ArticleState
from langchain_aws import ChatBedrock

# Initialize the language model
model = ChatBedrock(
    model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
    credentials_profile_name="default",
    region_name="us-east-1",
)


# Drafting agent function
def drafting_agent(state: ArticleState) -> Command[Literal["reviewing_agent", "__end__"]]:
    # print("--drafting_agent--")
    # print(state)
    topic = state.get("topic", "General Topic")
    feedback = state.get("review_feedback", "No feedback provided yet.")

    state["system_message"] = """You are an expert writer. 
Please draft the article in Markdown format only. 
Do not include any greetings, acknowledgments, or commentary—only the article content.
"""

    prompt = f"{state["system_message"]}\n\nTopic: {topic}."
    if feedback:
        prompt += f"\n\nPlease consider the following feedback: {feedback}"
    response = model.invoke(prompt)
    state["article_draft"] = response
    state["iteration"] += 1
    if state["iteration"] > 2:
        return Command(goto="__end__", update=state)
    return Command(goto="reviewing_agent", update=state)