#!/usr/bin/env python
# coding: utf-8


# instalar a lib do pandas em seu projeto usando o comando:
# pip install pandas

# após a instalação do pandas, importe a lib para o projeto
import pandas as pd

# Passo 1: Importar a base de dados
tabela = pd.read_csv(r"D://seu-arquivo-csv/telecom_users.csv")

# Passo 2: Visualizar a base de dados
# - Entender quais informações estão disponiveis
# - Descobrir os erros da base de dados]
tabela = tabela.drop("Unnamed: 0", axis=1) # Remove uma coluna inutil - axis diz se remove uma linha (0) ou coluna (1)
display(tabela) # visualizar a tabela (display pois usei o jupyter, em uma IDE seria print)


# Passo 3: Tratamento dos dados (A informação que não te ajuda, te atrapalha)
# - Valores que estão reconhecidos de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce") # convertendo os dados da coluna em numeros

# - Valores vazios
# --- Deletando colunas vazias
tabela = tabela.dropna(how="all", axis=1) #dropna para localizar linhas ou colunas vazias

# --- Deletando linhas com algum valor vazio
tabela = tabela.dropna(how="any", axis=0) #dropna para localizar linhas ou colunas vazias

print(tabela.info()) # visualizar a informação da tabela

# Passo 4: Analise inicial
# - Como estão nossos cancelamentos?
print(tabela["Churn"].value_counts())
print("------------------")
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) #normalize são os valores calculados em percentuais


# Passo 5: Analise mais completa
# - Comparar cada coluna da tabela com a coluna de cancelamento

# - instalar a lib que utilizaremos com o comando:
# - pip install plotly

# importar a lib para o projeto
import plotly.express as px

# -- etapa 1: criar o grafico
# grafico = px.histogram(tabela, x="MesesComoCliente", color="Churn") exemplo para informar coluna manualmente

# para mudar a cor do grafico: px.histogram(tabela, x=coluna, color="Churn", color_discrete_sequences["blue", "green"])
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")

    # -- etapa 2: exibir o grafico
    grafico.show()


# Conclusões e Ações:

# - Clientes com contrato mensal tem muito mais chances de cancelar
# -- Podemos fazer promoções para o cliente ir para o contrato anual
# 
# - Familias maiores tendem a cancelar menos do que familias maiores
# -- Podemos fazer promoções para pessoa pegar uma linha adicional de telefone
# 
# - Meses como cliente baixos tem muito cancelamento. Clientes com pouco tempo tendem a cancelar muito mais
# -- A primeira experiencia do cliente na operadora pode estar sendo muito ruim
# -- Talvez a captação de clientes esteja trazendo muitos clientes desqualificados
# -- Ideia: A gente pode criar incentivos para o cliente ficar mais tempo como cliente
# 
# - Quanto mais serviços o cliente tem, menor a chance dele cancelar
# -- Podemos fazer promoções com mais serviços para os clientes
# 
# - Tem algo no serviço de fibra que está fazendo os clientes cancelarem
# -- Agir no serviço de fibra
# 
# - Clientes no boleto, tem muito mais chance de cancelar
# -- Temos que fazer alguma ação para os clientes irem para outras formas de pagamento

