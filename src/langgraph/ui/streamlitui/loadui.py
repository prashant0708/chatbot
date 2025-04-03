import streamlit as st
import os
from datetime import date
from src.langgraph.ui.ui_configfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_control = {}
   
       
    def initialize_session(self):
        return {
            "current_step": "requirements",
            "requirements": "",
            "user_stories": "",
            "po_feedback": "",
            "generated_code": "",
            "review_feedback": "",
            "decision": None
        }
    

        
        
    def load_streamlit_ui(self):
        st.set_page_config(page_title= self.config.get_page_title(),layout="wide")
        st.header(self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False
        
        with st.sidebar:
            #Get option from config
            llm_option = self.config.get_llm_option()
            usecase_options = self.config.get_usercase_option()
            API_KEY = self.config.get_api_key()
            
            #LLM selection
            
            self.user_control["selected_llm"] = st.selectbox("Select llm",llm_option)
            if self.user_control["selected_llm"] == 'Groq':
                #Model Option
                model_options = self.config.get_groq_model_options()
                self.user_control["selected_groq_model"] = st.selectbox("Select Model",model_options)
                ## Use case option
                self.user_control["Use_case_option"] = st.selectbox("Select Use case",usecase_options)
                ## API KEY
                self.user_control["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]=st.text_input("API KEY",type="password")
                #self.user_control["GROQ_API_KEY"] = st.selectbox("API KEY",API_KEY)


                 # Validate API key
                if not self.user_control["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
        if "state" not in st.session_state:
            st.session_state.state = self.initialize_session()
       
        
        return self.user_control
    
