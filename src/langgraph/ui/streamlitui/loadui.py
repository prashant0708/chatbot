import streamlit as st
from src.langgraph.ui.ui_configfile import Config
import os

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config() 
        self.user_controls = {}

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
        st.set_page_config(page_title=self.config.get_page_title(),layout="wide")
        st.header(self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False


        with st.sidebar:
            # get llm option from the config
            llm_options = self.config.get_llm_options()

            # LLM selections
            self.user_controls["selected_llm"]=st.selectbox("Select LLM",llm_options)

            if self.user_controls["selected_llm"]=='Groq':
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"]=st.selectbox("Select Model",model_options)

                # API Key 
                self.user_controls["GROQ_API_KEY"]=st.session_state["GROQ_API_KEY"]=st.text_input("API Key",type="password")

                # validate api key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter the API Key")

            ## USECASE_OPTIONS
            user_option = self.config.get_usecase_options()
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases",user_option)

            ## Chatbot with tool 
            if self.user_controls["selected_usecase"]== "ChatBotwithTool":
                os.environ["TAVILY_API_KEY"]=self.user_controls["TAVILY_API_KEY"]=st.session_state["TAVILY_API_KEY"]=st.text_input("TAVILY_API_KEY",type="password")
                if not  self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your TAVILY_API_KEY key to proceed. Don't have? refer : https://app.tavily.com/home")

            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()

        return self.user_controls