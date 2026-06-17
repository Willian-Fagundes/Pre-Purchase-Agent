from langchain.agents import create_agent
from src.utils import load_prompt

researcher_prompt = load_prompt("researcher.md")

def researcher(llm):
    from tools.tools import search_tool
    agent = create_agent(
        llm,
        tools = [search_tool],
        system_prompt = researcher_prompt        
    )

    return agent

def resultado_pesquisa(llm,query):
    pesquisador = researcher(llm)
    resultado = pesquisador.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"{query}"
                }
            ]
        }
    )
    return resultado["messages"][-1].content



