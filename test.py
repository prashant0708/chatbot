import  streamlit as st
import json 

from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph.LLM.groqllm import GroqLLM
from src.langgraph.graph.graph_builder import GraphBuilder
from src.langgraph.ui.streamlitui.display_result import DisplayResultStreamlit

""""
def load_langgraph_agenticai_app():
    #load ui
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    print(user_input)

    if not user_input :
        st.error("Error: Failed to load user input")
        return
    
    #Text input from the user
    if st.session_state.IsFetchButtonClicked:
        user_message=st.session_state.timeframe
    else:
        user_message = st.chat_message("Enter the message ")
        
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
        
test= load_langgraph_agenticai_app()
"""
import os 
from langchain_groq import ChatGroq
import streamlit as st


class GroqLLM:
    def __init__(self,user_control_input):
        self.user_control_input = user_control_input
    def get_llm_model (self):
        try:
            groq_api_key = self.user_control_input["GROQ_API_KEY"]
            print(groq_api_key)
            selected_groq_model = self.user_control_input["selected_groq_model"]
            if groq_api_key =="" and os.environ["GROQ_API_KEY"]==" ":
                st.error("Please enter the Groq API key")
            llm = ChatGroq(api_key=groq_api_key,model=selected_groq_model)
            print(llm.invoke("How are you"))

            return llm
        except Exception as e:
            raise ValueError(f" error occured in llm {e}")
ui = LoadStreamlitUI()
user_input = ui.load_streamlit_ui()
print(user_input)
test= GroqLLM(user_input)
result = test.get_llm_model()
