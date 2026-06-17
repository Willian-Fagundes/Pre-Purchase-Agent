from ddgs import DDGS
from langchain.tools import tool


@tool
def search_tool(pesquisa : str, max_resultados = 12) -> str:
    """
    Pesquisa informações na internet utilizando DDGS.
    Retorna resultados relacionados à consulta.
    """
    ddgs = DDGS()
    results_list = []
    
    try:
        results = ddgs.text(pesquisa, max_results = max_resultados, region="br-pt")
        if not results:
            return "Nenhum resultado para a pesquisa"
        for item in results:
            results_list.append(
                f"""
                Título: {item.get('title')}
                Resumo: {item.get('body')}
                Link: {item.get('href')}
                """
            )

        return "\n".join(results_list)

    except Exception as e:
        return "Erro ", e



