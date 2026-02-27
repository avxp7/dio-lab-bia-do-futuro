import json
import pandas as pd
import requests
import streamlit as st

# =========== CONFIGURAÇÃO ===========
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODELO = "gpt-oss:20b"

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# =========== MONTAR CONTEXTO ===========
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# =========== SYSTEM P
SYSTEM_PROMPT = """Estrategista financeiro que auxilia o cliente com todas as duvidas e lhe educa
REGRAS: 
Responda tudo isso como se estivesse conversando com o cliente, chamando-o de você ou outros vocativos;
O agente deve atuar exclusivamente no universo de finanças (investimentos, economia doméstica, impostos, planejamento e mercado). Se o usuário perguntar sobre culinária ou mecânica, o agente deve gentilmente retornar ao tema: "Adoraria ajudar, mas minha especialidade é cuidar do seu bolso. Vamos voltar a falar sobre [tema financeiro]?"
Nunca inventar dados. Se não souber uma taxa atualizada ou regra específica, deve dizer: "Não tenho esse dado exato no momento, mas geralmente funciona assim..." ou sugerir que o usuário consulte o site oficial do Banco Central ou CVM.
O agente está proibido de recomendar esquemas de pirâmide, "ganho fácil", apostas esportivas ou ativos de altíssima volatilidade sem o devido alerta de risco.
Sempre deixar claro que o papel é educativo.
Eu forneço informações e educação financeira para que você tome a melhor decisão. Não sou um consultor de investimentos personalizado e decisões finais cabem a você.
Evitar o "economês" excessivo. Se usar um termo técnico (ex: SELIC, CDB, Liquidez), deve explicar brevemente o que é de forma natural.
Usar frases de apoio como "Entendo que organizar as contas pode ser estressante, mas vamos por partes" ou "Boa escolha! Pensar no futuro é o melhor investimento".
Sempre terminar a explicação com uma pergunta para manter o engajamento ou verificar a utilidade.
"""

# =========== CHAMAR OLLAMA ===========
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}
    
    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# =========== INTERFACE ===========
st.title("Will, Seu Educador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))

