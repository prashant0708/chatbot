"""
Here we will bind the llm with tool
"""
from src.langgraph.state.state import State
class ChatboatwithTool:
    def __init__(self,llm):
        self.llm= llm

    def process(self,state:State):
        """"""

