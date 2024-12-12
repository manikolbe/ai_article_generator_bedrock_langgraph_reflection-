import streamlit as st
from langchain_core.messages import HumanMessage
from article_workflow import article_workflow
import uuid
from state import ArticleState
from langchain_core.runnables.graph import NodeStyles
import asyncio



# Generate a unique thread_id if not present
if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = uuid.uuid4().hex

st.title("AI Article Writer")

# Display the image in the Streamlit sidebar
node_colors = NodeStyles(default="#f2f0ff", first="#f2f0ff", last="#f2f0ff")
graph_image = article_workflow.get_graph().draw_mermaid_png(node_colors=node_colors,output_file_path=None, background_color="")
st.sidebar.image(graph_image, caption="Workflow Graph", use_container_width=True)

user_input = st.text_input("Enter the topic",value="La Bomba, the boiling river of Peru")

if st.button("Generate Article"):
    initial_state = ArticleState(
        topic=user_input,
        iteration=0
    )
    # # Execute the workflow sync
    # final_state = article_workflow.invoke(
    #                 initial_state,
    #                 config={"configurable": {"thread_id": uuid.uuid4().hex}},
    #                 debug=True)

    progress_bar = st.progress(0.1,"📝 Preparing first draft...")
    placeholder = st.empty()
    

    final_result = {}
    async def run_workflow():
        # Execute the workflow async
        async for chunk in article_workflow.astream(initial_state, stream_mode="updates", debug=True):
            final_result.update(chunk)
            # st.markdown(chunk)
            agent_key = "drafting_agent" if "drafting_agent" in chunk else "reviewing_agent"
            step = chunk[agent_key]["iteration"]
            progress_percentage = int((step/4) * 100)
            progress_bar.progress(progress_percentage, f"{agent_key} completed round: {step}")
            if chunk.get("reviewing_agent"):
                placeholder.markdown(f"**Draft: {step} 🔍**\n\n" + chunk["reviewing_agent"]["review_feedback"].content)  
            else:
                placeholder.markdown(f"**Draft: {step} ✍️**\n\n" + chunk["drafting_agent"]["article_draft"].content)
            
 
            
    asyncio.run(run_workflow())
    
    progress_bar.progress(100, f"✅ Article generation completed")
    placeholder.markdown(final_result["drafting_agent"]["article_draft"].content)

    # st.write("**Final Article Draft:**")
    # st.markdown(final_state["article_draft"].content)

    # # Pretty print the final state
    # st.divider()
    # st.write("### Workflow State:")
    # st.json(final_state)  
