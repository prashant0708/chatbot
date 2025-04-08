import streamlit as st
import os
import json
from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph.graph.graph_builder import GraphBuilder
from src.langgraph.LLM.groqllm import GroqLLM
from src.langgraph.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agentic_app():
    ui=LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    print(user_input)

    if not user_input:
        st.error("Error Failed to load user input from the ui")

    ## Text input from the user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your messages")
    if user_message:
        try:

            usercase=user_input.get('selected_usecase')
            model=GroqLLM(user_control_input=user_input).get_llm_model()
            graph_builder = GraphBuilder(model)
            graph = graph_builder.setup_graph(usercase)

            DisplayResultStreamlit(usercase,graph,user_message).display_message_in_ui()
        except Exception as e:
            st.error(f"Error in the Graph {e}")
            return

