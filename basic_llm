from typing_extensions import TypedDict
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph,START,END
from typing import Optional

# def the state
class QuestionState(TypedDict):
     message: str
     response: Optional[str]


#  init chat model object for gemini
model = init_chat_model("gemini-2.0-flash-001", model_provider="google_vertexai",project="buoyant-keel-461215-a8")


# LLm node function def
def llm_node(state: QuestionState) -> QuestionState:

     state['response'] = model.invoke(state['message'])

     return state

llm_graph = StateGraph(QuestionState)
llm_graph.add_node("llm",llm_node)
llm_graph.add_edge(START,"llm")
llm_graph.add_edge("llm",END)

graph = llm_graph.compile()