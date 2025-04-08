from typing import Annotated,List,TypedDict
from langgraph.graph.message import add_messages

class State(TypedDict):
    """
    Represent the stractured of  state used in the graph
    """
    messages:Annotated[list,add_messages]




