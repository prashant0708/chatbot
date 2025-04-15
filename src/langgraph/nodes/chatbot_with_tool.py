"""
Here we will bind the llm with tool
"""
from src.langgraph.state.state import State
from langchain_core.messages import AIMessage,HumanMessage

# def preprocess_query(user_query:str)->str:
#     trigger_words = ["what", "why", "how", "when", "where", "who", "which","What",
#                      "WHAT","WHY","Why","How","HOW","When","WHEN","WHO","Who","WHERE","Where","Which"]
#     words = user_query.split()
#     print(words)
#     if words and words[0] in trigger_words:
#         return f"Search online and answer the  question: {user_query}"
#     else:
#         return user_query




class ChatboatwithTool:
    def __init__(self,llm):
        self.llm= llm

    # def process(self,state:State):
    #     """
    #     process the input state and generate a response with tool integration 
    #     """
    #     user_input =state["messages"][-1].content if state["messages"] else ""
    #     print(f"This is Before preprocess the user input:{user_input}")
    #     user_input = preprocess_query(user_input)
    #     print(f"This is after preprocess the user input:{user_input}")
    #     llm_response =  self.llm.invoke([{"role":"user","content":{user_input}}])
        
    #     ## simpulate tool specific logic
    #     tools_response = f"Search online and answer the following question:{user_input}"
    #     return {"messages": [llm_response,tools_response]}
    
    def create_chatbot(self,tools):
        """
        Return a chatbot node function
        """
        llm_with_tools = self.llm.bind_tools(tools)
        
        def chatbot_node(state:State):
            """ 
            Chatbot logic for processing the input state and returning a response
            """
            system_msg = {"role": "system", "content": "Search online and answer the following question."}
            llm_response =  llm_with_tools.invoke([system_msg]+state["messages"])
            #print(f"******************************[State[Message]]*******************{state["messages"]}")
            ## Some excercise to update the user prompt
            user_input = state["messages"][-1]
            #print(f"*******************{user_input}******************")
            new_content = "Search online and answer the question: " +user_input.content
            new_msg = HumanMessage(content=new_content)
            state["messages"][-1] = new_msg
            #print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$[State[Message]]$$$$$$$$$$$$$$$$$$${state["messages"]}")

            
            
            return {"messages":llm_response}
        
        
        return chatbot_node