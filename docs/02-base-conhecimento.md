# Base de Conhecimento

## Dados Utilizados


| Arquivo | Formato | Função do Will |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, o que faz com que o atendimento seja mais preciso. |
| `perfil_investidor.json` | JSON | Personalizar os dados do cliente, obtendo os dados necessários para o agente ter sua resposta clara e objetiva. |
| `produtos_financeiros.json` | JSON | Mostrar os produtos que estão a mostra para que o cliente seja ensinado de forma totalmente educativa. |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente. |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O produto (FII) subistituiu o fundo multimercado, pois ele pode ser um bom produto para o cliente, trazendo segurança e confiabilidade.

---

## Estratégia de Integração

### Como os dados são carregados?
>  Descreva como seu agente acessa a base de conhecimento.

Pode ser colocando os dados no prompt ou carregando pelo código.

```Python
import pandas as pd
import json

# CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

# JSONs
with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
    perfil = json.load(f)

with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
    produtos = json.load(f)
```


### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Mostrei os dados desta forma para o agente pode ter uma simplificação dos dados para ter um contexto bem introduzido. Mas que pode ser alterado.

```text
Dados do cliente e perfil:

Perfil Geral
Profissão: Analista de Sistemas (32 anos).

Renda: R$ 5.000,00 mensais.

Perfil: Moderado, porém não aceita riscos no momento.

Situação Financeira Atual
Patrimônio Total: R$ 15.000,00.

Reserva de Emergência: Possui R$ 10.000,00 (faltam R$ 5.000,00 para a meta).

Próximos Passos (Metas)
Curto Prazo (Junho/2026): Finalizar a reserva de emergência (mais R$ 5.000,00).

Médio Prazo (Dezembro/2027): Juntar R$ 50.000,00 para a entrada de um apartamento.

Transações do cliente:

data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

Histórico de atendimento:

data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim


Produtos disponíveis:

[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Imobiliário (FII)",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI 10%-12% ao ano",
    "aporte_minimo": 10.00,
    "indicado_para": "Perfil moderado que busca diversificação e renda recorrente mensal"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

Com os dados do cliente, aqui estão as informações mais importantes do mesmo, fazendo com que otimizamos mais tokens.

```
Perfil do Cliente
- Dados: Analista de Sistemas, 32 anos.

- Renda Mensal: R$ 5.000,00.
- Situação Financeira (Outubro/2025)
- Patrimônio Atual: R$ 15.000,00.
- Reserva de Emergência: R$ 10.000,00 (Meta: R$ 15.000,00).
- Capacidade de Poupança: Aproximadamente R$ 2.511,10/mês.

- Médio Prazo (Dezembro/2027): Acumular R$ 50.000,00 para entrada de um apartamento.

Histórico e Interesses
- O cliente busca conhecimento constante em Renda Fixa, com dúvidas sanadas sobre CDB, Tesouro Direto (Selic) e acompanhamento de metas. O histórico de suporte indica que ele é digitalmente ativo, mas já enfrentou problemas de visualização no app.

...
```
