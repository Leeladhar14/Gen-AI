from typing_extensions import TypedDict
from langchain_core.messages import HumanMessage,AIMessage
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END

class Question(TypedDict):
    """_summary_

    Args:
        TypedDict (_type_): _description_
    """

    