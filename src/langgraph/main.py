import  streamlit as st
import json 

from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph.LLM.groqllm import GroqLLM
from src.langgraph.graph.graph_builder import GraphBuilder
from src.langgraph.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """
    #load ui
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input :
        st.error("Error: Failed to load user input")
        return
    
    #Text input for the user
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe 
    else :
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            # config_llm
            obj_config_llm = GroqLLM(user_control_input=user_input)
            print(obj_config_llm)
            model =obj_config_llm.get_llm_model()
            if not model:
                st.error("Error: No use case selected")
                return
            
            ## initilize the set up and graph based on the use case
            usecase = user_input.get('Use_case_option')
            if not usecase:
                st.error("Error:Use case not selected")
                return
            
            ## graph Builder

            graph_builder = GraphBuilder(model)

            try:
                graph=graph_builder.setup_graph(usecase=usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_ui()
            except Exception as e:
                    st.error(f"Error: Graph setup failed - {e}")
                    return
        except Exception as e:
                 raise ValueError(f"Error Occurred with Exception : {e}")