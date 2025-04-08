from langgraph.graph import START,END,StateGraph
from src.langgraph.nodes.basic_chatbot_node import Basicchatbot
from src.langgraph.state.state import State
from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI


class GraphBuilder  :
    def __init__(self,model):
        self.graph_builder = StateGraph(State)
        self.llm=model

    def basic_chatbot_build_grap(self):
        self_basic_chatbot_node = Basicchatbot(self.llm)
        self.graph_builder.add_node("chatbot",self_basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)
        return self.graph_builder.compile()


    def setup_graph(self,usecase:str):
        if usecase=="Basic Chatbot":
            return self.basic_chatbot_build_grap()
        

