from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    return the tools that will use in Tool Node
    """
    tool = [TavilySearchResults(max_results=2)]
    return tool

def Tool_Node(tool):
    """
    Return the Tool Node for the graph
    """
    Tool_node = ToolNode(tools=tool)
    return Tool_node

