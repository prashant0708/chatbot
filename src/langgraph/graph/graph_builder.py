from langgraph.graph import START,END,StateGraph
from src.langgraph.LLM.groqllm import GroqLLM
from src.langgraph.state.state import State
from src.langgraph.nodes.basic_chatbot_node import BasicChatBotNode


class GraphBuilder:
    def __init__(self,model):
        self.llm =model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """
        self.basic_chatbot_node = BasicChatBotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)
        return self.graph_builder.compile()
        
        

    def setup_graph(self,usecase:str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase=="Basic Chatbot":
            return self.basic_chatbot_graph()
        
        
        

        

