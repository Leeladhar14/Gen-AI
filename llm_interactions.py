from typing_extensions import TypedDict
from typing import Optional
from langgraph.graph import START, END, StateGraph
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage

class QuestionState(TypedDict):
    question: str
    response: Optional[str]


model_id = "gemini-2.0-flash-lite-001"
llm = init_chat_model(model=model_id, model_provider="google_vertexai", project="buoyant-keel-461215-a8")

def ask_llm(state: QuestionState) -> QuestionState:
    message = HumanMessage(content=state["question"])
    response = llm.invoke([message])
    state['response'] = response.content.strip()
    return state

state_builder = StateGraph(QuestionState)

state_builder.add_node("brain", ask_llm)
state_builder.add_edge(START, "brain")
state_builder.add_edge("brain", END)

graph = state_builder.compile()
