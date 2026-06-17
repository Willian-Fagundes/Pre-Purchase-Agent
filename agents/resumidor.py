from langchain.agents import create_agent
from src.utils import load_prompt

summarizer_prompt = load_prompt("summarizer.md")

def agente_resumidor(llm):
    return create_agent(
        llm,
        tools=[],
        system_prompt=summarizer_prompt
    )

def resumo_resumidor(llm, mecanico_text, custos_text, historico_text):
    resumidor = agente_resumidor(llm)

    input_text = (
        "Use os relatórios abaixo para gerar o resumo final.\n\n"
        "Relatório Mecânico:\n"
        f"{mecanico_text}\n\n"
        "Relatório de Custos:\n"
        f"{custos_text}\n\n"
        "Relatório de Histórico:\n"
        f"{historico_text}\n"
    )

    resultado = resumidor.invoke(
        {
            "messages": [
                {"role": "user", "content": input_text}
            ]
        }
    )
    return resultado["messages"][-1].content
