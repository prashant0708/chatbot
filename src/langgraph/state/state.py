from typing import Annotated,List,TypedDict,Literal,Optional
from langchain_core.messages import AIMessage,HumanMessage
from langgraph.graph.message import add_messages


class State(TypedDict):
    """
    Represent the stracture the state used in the graph
    """
    messages: Annotated[list, add_messages]
    