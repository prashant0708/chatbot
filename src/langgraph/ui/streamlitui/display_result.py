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
                for value in event.values():
                    with st.chat_message("user"):
                        st.write(user_messages)
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)
                        
        elif usecase=="ChatBotwithTool":
            initial_state = {"messages": [user_messages]}
            res = graph.invoke(initial_state)
            #print(res)
            for message in res['messages']:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message)==ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write("Tool Call End")
                elif type(message)==AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)