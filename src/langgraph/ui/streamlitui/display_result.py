import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json

class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_messages):
        self.usecase=usecase
        self.graph=graph
        self.user_messages = user_messages

    def display_message_in_ui(self):
        usecase=self.usecase
        graph=self.graph
        user_messages = self.user_messages
        if usecase=="Basic Chatbot":
            for event in graph.stream({"messages":("user",user_messages)}):
                
                print(event.values())
                for value in event.values():
                    print(value["messages"])
                    with st.chat_message("user"):
                        st.write(user_messages)
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)