from langgraph.graph import StateGraph, START, END
from state import ArticleState
from agents.drafting_agent import drafting_agent
from agents.reviewing_agent import reviewing_agent



# Build the graph
builder = StateGraph(ArticleState)
builder.add_node("drafting_agent", drafting_agent)
builder.add_node("reviewing_agent", reviewing_agent)
builder.add_edge(START, "drafting_agent")
# builder.add_edge("reviewing_agent", "drafting_agent")
# builder.add_edge("drafting_agent", "reviewing_agent")
# builder.add_edge("drafting_agent", END)

# Compile the graph
article_workflow = builder.compile()
print(article_workflow.get_graph().draw_mermaid())
