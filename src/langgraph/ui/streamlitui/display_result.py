import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json

class DisplayResultStreamlit:
    def __init__(self,use_case,graph,user_message):
        self.use_case = use_case
        self.graph = graph
        self.user_message = user_message

    def display_result_ui(self):
        usecase= self.use_case
        graph = self.graph
        user_message = self.user_message
        if usecase == "Basic Chatbot":
            for event in graph.stream({"messages":[HumanMessage(content=user_message)]}):
                #print(f"this is from event display{event.values()}")
                for value in event['messages'][-1]:
                    print(value)
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("Prashant AI assistant"):
                        st.write(event.values())
