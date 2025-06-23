from langchain_community.tools.requests.tool import RequestsGetTool
from langchain_core.tools import tool
from bs4 import BeautifulSoup

requests_tool = RequestsGetTool()

@tool
def extract_class_link(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    link = soup.find("a", string=lambda t: "class" in t.lower())
    return link["href"] if link else "No class link found."

# Combine in an agent
from langchain.agents import initialize_agent, AgentType
tools = [requests_tool, extract_class_link]
agent = initialize_agent(tools, AgentType.ZERO_SHOT_REACT_DESCRIPTION)

res = agent.run("GET https://directai.blog/gen-ai-classroom-notes/")
print(res)
