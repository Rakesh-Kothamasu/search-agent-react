from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage

from langchain_groq import ChatGroq      
from langchain.tools import tool 
from langchain_tavily import TavilySearch

llm = ChatGroq(model="qwen/qwen3.8-27b", temperature=0)
tools = [TavilySearch()]
agent=create_agent(model=llm, tools=tools)
def main():
    print("Hello World")
    result = agent.invoke({"messages": [HumanMessage(content="Search for Boga Chenchu Vinay profile who is working at staples india on LinkedIn and provide the link")]})    
    print(result["messages"][-1].content)

if __name__ == "__main__":
    main()