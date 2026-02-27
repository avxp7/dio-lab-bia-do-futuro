## 🤖 Agente Financeiro Inteligente (Ollama + Streamlit)
Este é um agente financeiro proativo que utiliza IA Generativa local para transformar dados bancários em consultoria personalizada. O diferencial desta solução é a privacidade total dos dados, rodando o modelo localmente com Ollama.

## 🚀 Funcionalidades
- Análise Proativa: Identifica padrões de gastos e sugere ajustes antes mesmo do usuário perguntar.
- Consultoria Baseada em Dados: Respostas fundamentadas nos arquivos transacoes.csv e perfil_investidor.json.
- Privacidade Garantida: Processamento local via Ollama (sem envio de dados financeiros para nuvens de terceiros).
- Interface Interativa: Chat intuitivo desenvolvido em Streamlit.

## 🏗️ Estrutura do Projeto
```
├── 📁 data/          # Bases de conhecimento (CSV/JSON)
├── 📁 docs/          # Documentação estratégica e técnica
├── 📁 src/           # Código-fonte
│   └── app.py        # Aplicação Streamlit integrada ao Ollama
└── 📄 requirements.txt
```
## 🛠️ Tecnologias e Stack
- LLM Local: Ollama (Modelo sugerido: llama3 ou mistral)
- Interface: Streamlit
- Processamento de Dados: Pandas
- Orquestração: LangChain (opcional) / Ollama Python Library

## 🏃 Como Rodar o Protótipo
### 1. Preparar o Ollama
Certifique-se de que o Ollama está instalado e rodando:
```
ollama run llama3
```
### 2. Instalar Dependências
No terminal, instale os pacotes necessários:
```
pip install streamlit ollama pandas
```
### 3. Executar o Agente
```
streamlit run src/app.py
```
## 🔒 Segurança e Anti-Alucinação
Para garantir respostas confiáveis, o agente utiliza a técnica de Grounding:

1. O sistema lê os dados em data/ no início da sessão.
2. O System Prompt restringe o LLM a responder apenas com base nos produtos disponíveis em produtos_financeiros.json.
3. Qualquer recomendação de investimento é validada contra o perfil de risco do cliente.

## 📈 Métricas de Avaliação
- Assertividade: Comparação entre o saldo real e o reportado pela IA.
- Aderência: Taxa de sugestões que respeitam o perfil do investidor.
- Latência: Tempo de resposta do modelo rodando localmente.
