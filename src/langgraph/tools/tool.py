from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    return the tools that will use in Tool Node
    """
    tool = [TavilySearchResults(max_results=2,
                                description="Useful for answering any general question using the web, especially queries starting with what, why, how, where, or when.")]
    return tool

def Tool_Node(tool):
    """
    Return the Tool Node for the graph
    """
    Tool_node = ToolNode(tools=tool)
    print(f'tool node function from Too_Node{Tool_node}')
    return Tool_node

