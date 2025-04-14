from langgraph.graph import START,END,StateGraph
from langgraph.prebuilt import tools_condition,ToolNode
from src.langgraph.nodes.basic_chatbot_node import Basicchatbot
from src.langgraph.state.state import State
from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph.tools.tool import get_tools,Tool_Node
from src.langgraph.nodes.chatbot_with_tool import ChatboatwithTool


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
    
    def chatbot_with_tools_build_graph(self):
        """ 
        Build Chatbot graph with tool integration
        
        """
        tools = get_tools()
        tool_node = Tool_Node(tools)
        
        llm = self.llm
        
        chatbot_with_node = ChatboatwithTool(llm)
        chatbot_node = chatbot_with_node.create_chatbot(tools)
        
        
        ## Add nodes
        self.graph_builder.add_node("Chatbot" , chatbot_node)
        self.graph_builder.add_node("tools",tool_node)
        
        ## flow
        self.graph_builder.add_edge(START,"Chatbot")
        self.graph_builder.add_conditional_edges("Chatbot",tools_condition)
        self.graph_builder.add_edge("tools","Chatbot")
        return self.graph_builder.compile()
        
        

    def setup_graph(self,usecase:str):
        if usecase=="Basic Chatbot":
            return self.basic_chatbot_build_grap()
        if usecase=="ChatBotwithTool":
            return self.chatbot_with_tools_build_graph()
        
        
        
        
        
        
        
        
        
            
        

