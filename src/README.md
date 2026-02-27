# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

# Agente de Finanças Inteligente

Este projeto é um assistente financeiro desenvolvido para rodar localmente utilizando **Ollama**. O objetivo é oferecer suporte educacional e prático sobre finanças pessoais com uma interface amigável em Streamlit.

---

## Passo a Passo de Execução

### Setup do Ollama
Antes de rodar a aplicação, você precisa configurar o modelo de linguagem local:

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull gpt-oss

# 3. Testar se funciona
ollama run gpt-oss "Olá!"
## Estrutura Sugerida

```
### Código completo
todo o código-fonte está no arquivo 'app.py'

### Como Rodar
Siga as instruções abaixo para preparar o ambiente Python e executar a interface:

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que o Ollama está rodando
ollama serve

# 3. Rodar o app
streamlit run src/app.py
```

## Exemplo de interação
<img width="1863" height="913" alt="{E4D02DAB-2545-483D-8250-ECB002B58515}" src="https://github.com/user-attachments/assets/8f2fd845-38c3-4e47-b0a4-1d50bdbaba55" />
