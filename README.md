# Pre-Purchase-Agent

Resumo rápido

Pre-Purchase-Agent é um conjunto simples de agentes que auxiliam na análise pré-compra de veículos. Cada agente gera relatórios especializados (pesquisa, mecânica, custos) que são consolidados pelo agente resumidor em um relatório executivo.

Estrutura do projeto

- agents/: implementações dos agentes (pesquisador, mecanico, custos, resumidor)
- prompts/: prompts usados pelos agentes
- src/: inicializador e utilitários (llms.py, main.py, utils.py)
- tools/: ferramentas auxiliares
- requirements.txt: dependências Python
- LICENSE: licença do projeto

Requisitos

- Python 3.10+
- Variáveis de ambiente:
  - `GROQ_API_KEY` (chave para o provedor de LLM usado no projeto)
- Instalar dependências:

```bash
pip install -r requirements.txt
```

Como executar

1. Exporte a variável de ambiente `GROQ_API_KEY`:

```bash
export GROQ_API_KEY="sua_chave_aqui"
```

2. Rode o script principal:

```bash
python src/main.py
```

3. Siga as instruções no prompt para informar o veículo ou consulta desejada. O fluxo padrão é:
- `pesquisador` realiza a busca
- `mecanico` gera o resumo técnico
- `custos` calcula estimativas de manutenção
- `resumidor` consolida tudo em um relatório executivo

Notas de desenvolvimento

- Os prompts estão em `prompts/summarizer.md` e outros arquivos correspondentes.
- Use `utils.load_prompt()` para carregar prompts nos agentes.
- Estruture novos agentes seguindo o padrão em `agents/pesquisador.py` e `agents/mecanico.py`.

Licença

Veja o arquivo `LICENSE` para detalhes sobre a licença.
