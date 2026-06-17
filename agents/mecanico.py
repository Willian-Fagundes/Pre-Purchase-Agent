from langchain.agents import create_agent
from src.utils import load_prompt

mechanic_prompt = load_prompt("mechanic.md")

def agente_mecanico(llm):
    agent = create_agent(
        llm,
        tools = [],
        system_prompt = mechanic_prompt)
    return agent

def resumo_mecanico(llm, pesquisa):
    mecanico = agente_mecanico(llm)
    resultado = mecanico.invoke(
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
