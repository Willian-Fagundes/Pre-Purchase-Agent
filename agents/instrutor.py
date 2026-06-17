from langchain.agents import create_agent
from src.utils import load_prompt

instructor_prompt = load_prompt("instructor.md")

def agente_instrutor(llm):
    agent = create_agent(
        llm,
        tools = [],
        system_prompt = instructor_prompt)
    return agent

def resumo_mecanico(llm, pesquisa):
    instrutor = agente_instrutor(llm)
    resultado = instrutor.invoke(
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