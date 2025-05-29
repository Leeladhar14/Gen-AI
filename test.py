#  langgraph contians mainly state node and edge
#  Typedict is for storing the state
#  langgraph.graph imports the default nodes start end and stategrpah is to build the state graph
from typing_extensions import TypedDict
from langgraph.graph import START, END, StateGraph
from typing import Literal,Optional
#  define state

class CalcState(TypedDict):
    """state
    """
    number1: float
    number2: float
    operator: Literal["+","-"]
    result: Optional[float]


# create two nodes 
def add(state: CalcState) -> CalcState:
    """add
    """
    state['result'] = state['number1'] + state['number2']
    return state

def sub(state: CalcState) -> CalcState:
    """sub
    """

    state['result'] = state['number1'] - state['number2']
    return state

def conditionaledge(state: CalcState) -> Literal["add","sub"]:
    if state['operator'] == "+":
        return "add"
    else:
        return "sub"

graph_builder = StateGraph(CalcState)
#  add nodes to the graph
graph_builder.add_node("add",add)
graph_builder.add_node("sub",sub)

#  add edge to the graph
graph_builder.add_edge(START,conditionaledge)
graph_builder.add_edge("add",END)
graph_builder.add_edge("sub",END)



#  compile the graph

first = graph_builder.compile()


