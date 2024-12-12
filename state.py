from langgraph.graph import  MessagesState
from typing import Optional

# Define the shared state schema
class ArticleState(MessagesState):
    article_draft: Optional[str] = None
    review_feedback: Optional[str] = None
    iteration: int = 0  # Default value
    system_message: Optional[str] = ""
    topic: Optional[str] = None