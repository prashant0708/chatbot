from src.langgraph.state.state import State

class BasicChatBotNode:
    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict:
        """
        Process the input of the state and generate the responce 
        """
        return {"messages":self.llm.invoke(state["messages"])}