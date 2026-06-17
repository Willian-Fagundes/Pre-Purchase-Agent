from src.llms import qwen_model, gpt_model
from agents.pesquisador import resultado_pesquisa
from agents.mecanico import resumo_mecanico
from agents.custos import resumo_custos
from agents.resumidor import resumo_resumidor

qwen = qwen_model()
gpt = gpt_model()

pesquisa = input("Insira o veículo: ")

texto_pesquisa = resultado_pesquisa(qwen, pesquisa)
texto_mecanico = resumo_mecanico(qwen, texto_pesquisa)
texto_custos = resumo_custos(qwen, texto_pesquisa)

resumo_final = resumo_resumidor(gpt, texto_mecanico, texto_custos, texto_pesquisa)

print(resumo_final)


