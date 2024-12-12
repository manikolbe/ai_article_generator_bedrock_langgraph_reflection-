
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

# Reviewing agent function
def reviewing_agent(state: ArticleState) -> Command[Literal["drafting_agent"]]:
    # print("--reviewing_agent--")
    # print(state)
    draft = state["article_draft"]
    state["system_message"] = """You are a meticulous editor. 
Please review the draft and provide a feedback. 
Do not include any greetings, acknowledgments, or commentary—only the feedback."""

    prompt = f"{state["system_message"]}\n\nArticle Draft:\n{draft}"
    response = model.invoke(prompt)
    state["review_feedback"] = response
    return Command(goto="drafting_agent", update=state)