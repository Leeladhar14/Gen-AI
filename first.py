from typing_extensions import TypedDict
from typing import Literal, Optional
from langgraph.graph import START,END, StateGraph


class CalcState(TypedDict):
    """State"""
    number1: float
    number2: float
    Operator: Literal["+","-"]
    result: Optional[float]

#  def nodes to the graph

def add_node(state: CalcState) -> CalcState:
    """Add two number
    """

    state["result"] = state['number1'] + state['number2']

    return state

def sub_node(state: CalcState) -> CalcState:
    """sub two numbers
    """

    state['result'] = state['number1'] - state['number2']

    return state

def router(state: CalcState) -> Literal["add","sub"]:
    if state['Operator'] == "+":
        return "add"
    else:
        return "sub"

#  create a StateGrpah

graph_builder = StateGraph(CalcState)

graph_builder.add_node("add",add_node)
graph_builder.add_node("sub",sub_node)

graph_builder.add_conditional_edges(START,router)
graph_builder.add_edge("add",END)
graph_builder.add_edge("sub",END)

first= graph_builder.compile()
