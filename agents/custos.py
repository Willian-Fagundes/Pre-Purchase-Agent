from langchain.agents import create_agent
from src.utils import load_prompt

costs_prompt = load_prompt("costs.md")

def agente_custos(llm):
    agent = create_agent(
        llm,
        tools = [],
        system_prompt = costs_prompt)
    return agent

def resumo_custos(llm, pesquisa):
    custos = agente_custos(llm)
    resultado = custos.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"{pesquisa}"
                }
            ]
        }
    )
    return resultado["messages"][-1].content