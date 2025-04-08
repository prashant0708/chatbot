from src.langgraph.state.state import State
from src.langgraph.LLM.groqllm import GroqLLM
from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI



class Basicchatbot:
    def __init__(self,model):
        self.llm=model

        """"
        Process the input state and generate a chatbot response
        """

    def process(self,state:State) ->dict:
        return {"messages":self.llm.invoke(state['messages'])}


