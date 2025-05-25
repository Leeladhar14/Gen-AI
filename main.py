from typing_extensions import TypedDict
from langgraph.graph import START, END, StateGraph

class State(TypedDict):
    message: str



def node1(state: State) -> State:
    """This is node1
    """

    state['message'] += "node1"
    return state

def node2(state: State) -> State:

    state['message'] +="node2"
    return state



def node3(state: State) -> State:

    state['message'] +="node3"
    return state


builder:StateGraph = StateGraph(State)

#  add nodes

builder.add_node("node1", node1)
builder.add_node("node2", node2)
builder.add_node("node3", node3)

#  add edge
builder.add_edge(START, "node1")
builder.add_edge("node1","node2")
builder.add_edge("node2","node3")
builder.add_edge("node3",END)


graph = builder.compile()