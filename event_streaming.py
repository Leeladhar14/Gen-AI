from langgraph.graph import StateGraph, START, END, MessagesState
from langchain.chat_models import init_chat_model
from typing import TypedDict
import asyncio

model_id="gemini-2.5-flash-preview-05-20"
llm = init_chat_model(model=model_id,model_provider="google_vertexai",project="buoyant-keel-461215-a8")



# llm

# async for event in llm.astream_events("Hi this is khaja. What is latest update by google vertex"):
#     if event["event"] == "on_chat_model_stream":
#         print(event["data"]["chunk"].content)


class MyState(TypedDict):
    message: str

from time import sleep
def node_1(state: MyState) -> MyState:
    state['message'] = "Im in node 1"
    sleep(2)
    return state

def node_2(state: MyState) -> MyState:
    state['message'] = "Im in node 2"
    sleep(2)
    return state

def node_3(state: MyState) -> MyState:
    state['message'] = "Im in node 3"
    sleep(2)
    return state

def node_4(state: MyState) -> MyState:
    state['message'] = "Im in node 4"
    sleep(2)
    return state

def node_5(state: MyState) -> MyState:
    state['message'] = "Im in node 5"
    sleep(2)
    return state

my_graph_builder = StateGraph(MyState)
my_graph_builder.add_node("node1", node_1)
my_graph_builder.add_node("node2", node_2)
my_graph_builder.add_node("node3", node_3)
my_graph_builder.add_node("node4", node_4)
my_graph_builder.add_node("node5", node_5)
my_graph_builder.set_entry_point("node1")
my_graph_builder.set_finish_point("node5")
my_graph_builder.add_edge("node1", "node2")
my_graph_builder.add_edge("node2", "node3")
my_graph_builder.add_edge("node3", "node4")
my_graph_builder.add_edge("node4", "node5")
my_graph = my_graph_builder.compile()






async def process_events():
    async for event in my_graph.astream_events({"message": ""}):
        # if event["event"] == "on_chain_stream" and event['data']['chunk']:
        #     print(f"{event['name']} response = {event['data']['chunk']}")
        if event["event"] == 'on_chain_end':
            print(event['data']['output']['message'])

# Entry point for the script
if __name__ == "__main__":
    asyncio.run(process_events())