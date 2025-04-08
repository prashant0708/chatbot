from src.langgraph.ui.streamlitui import loadui
from langchain_groq import ChatGroq
import streamlit as st
import os


class GroqLLM:
    def __init__(self,user_control_input):
        self.user_control_input = user_control_input

        # Groq : API KEY
        # Model : 

    def get_llm_model(self):
        try:
            Groq_api_key = self.user_control_input['GROQ_API_KEY']
            Selected_groq_model = self.user_control_input["selected_groq_model"]

            if Groq_api_key=="" and  os.environ["GROQ_API_KEY"]=='':

                st.error("Please enter the API key")

            llm= ChatGroq(api_key=Groq_api_key,model=Selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error Occured as Exception: {e}")
        print(llm.invoke("Hello I am from GROQLLM"))
        
        return llm
    

