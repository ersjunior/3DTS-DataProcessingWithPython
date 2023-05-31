# -*- coding: utf-8 -*-
"""desafio_A5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qEpyAV72xudBtWBxrhT9CKd3uUXnyNan

# Desafio Aula 05

* Escolha uma base de dados no
https://www.kaggle.com/datasets

## 0) Se familiarize com sua base, não esqueça de
junto com seus códigos realizar suas
análises/conclusões (use o botão de +Texto).

## 1) Realize sumarizados. Veja qual tipo de
gráfico é útil para sua análise se barras,
linha ou pizza

* 2) Faca análises estatísticas
* a) Apresente o histograma
* b) Calcule os quartis
* c) Apresente o boxplot

Para o desafio da aula 5, escolhi um dataset no kaggle 
que traz informações sobre os salários dos cientistas de dados em 2023.

A amostra contém as informações:

work_year: 
  Ano em que o salário foi pago.

experience_level: 
  Nível de experiência no trabalho durante o ano de 2023.

employment_type: 
  Tipo de emprego para a função

job_title: 
  Função que trabalhou durante o ano

salary: 
  Valor bruto do salário pago

salary_currency: 
  A moeda do salário pago como um código de moeda ISO 4217

salaryinusd: 
  O Salário em USD (Dólar $)

employee_residence: 
  País de residência do funcionário durante o ano de trabalho ISO 3166

remote_ratio: 
  Quantidade total de trabalho feito remotamente

company_location: 
  País da sede da empresa ou filial contratante

company_size: 
  Número médio de pessoas que trabalharam para a empresa no ano   

Formato
Tabela de dados contendo 3755 observações em 11 variáveis.

## Instalando lib necessaria
"""

!pip install country_converter

"""## Importando as bibliotecas necessárias"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import country_converter as coco
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from wordcloud import WordCloud
import warnings
warnings.filterwarnings('ignore')
import nltk

# %matplotlib inline
import os
from google.colab import drive

"""* Acessando arquivo no Drive"""

# Monta o Google Drive
drive.mount('/content/drive')

"""## Iniciando a análise dos dados"""

# Caminho completo do arquivo CSV no Google Drive
caminho_arquivo = '/content/drive/MyDrive/ds_salaries.csv'

# Lendo o arquivo CSV e carregando em um DataFrame
df = pd.read_csv(caminho_arquivo)

# Visualisando o dataframe + dados
print(df.shape)
df.head(5)

"""* Analisando os dados estatisticos de salários """

# Conhecendo os dados
df[['salary_in_usd']].describe().round(2)

"""## Verificando o volume de profissionais e seus níveis de experiência"""

# Renomeando os campos da coluna de nível
df['experience_level'] = df['experience_level'].replace('EN','Junior')
df['experience_level'] = df['experience_level'].replace('MI','Pleno')
df['experience_level'] = df['experience_level'].replace('SE','Senior')
df['experience_level'] = df['experience_level'].replace('EX','Executive')

# Criação do gráfico com Plotly Express
ex_level = df['experience_level'].value_counts()
print(ex_level)

fig = px.treemap(
    ex_level, 
    path = [ex_level.index], 
    values = ex_level.values,
    title = 'Nível de experiência'
)

# Definições do gráfico
fig.update_layout(
# Largura (w) e altura (h) em pixels
    width=800,
    height=500
)

fig.show()

"""* De acordo com a amostra, a maioria dos trabalhadores estão em nível de Sênior / Especialista.
Sendo um volume considerável em relação aos iniciantes / Junior's e com um número muito pequeno quando se trata de cargos em nível executivo

* Verificando a quantidade de cargos diferentes na base
"""

print('Diferentes cargos de trabalho:', len(set(df['job_title'])))

"""## Vendo os cargos de trabalho mais frequentes"""

# Criando uma variável que vai receber os 10 cargos com maior frequência
top10_cargos = df['job_title'].value_counts()[:10]

# Criação do gráfico com Plotly Express
fig = px.bar(
    y = top10_cargos.values, 
    x = top10_cargos.index,
    text = top10_cargos.values, 
    title = 'Top 10 Cargos'
)

# Definições do gráfico
fig.update_layout(
    xaxis_title = "Cargos", 
    yaxis_title = "Quantidade",
# Largura (w) e altura (h) em pixels
    width=1000,
    height=400
)

# Mostrando o gráfico
fig.show()

"""* Os 3 cargos mais comuns na área de dados são

* 1) Engengeiro de dados
* 2) Ciêntista de dados
* 3) Analista de dados

## Temos 4 tipos de Empregos

* PT: Meio período (Part-time)

* FT: Tempo integral (Full-time)

* CT: Contrato (Contract)

* FL: Autônomo (Freelance)
"""

# Trazendo o volume total de grupos de trabalho e separando os grupos por tipo 
grupo = df['employment_type'].value_counts()
tipo_emp = ['Full-Time', 'Part-Time', 'Contract', 'Freelance']

# Criação do gráfico com Plotly Express
fig = px.bar(
    x = tipo_emp, 
    y = grupo.values,
    color = grupo.index, 
    text = grupo.values,
    title = 'Distribuição - Tipo de trabalho'
)

# Definições do gráfico
fig.update_layout(
    xaxis_title = "Tipo de trabalho", 
    yaxis_title = "Quantidade",
# Largura (w) e altura (h) em pixels
    width=1000,
    height=400
)

# Mostrando o gráfico
fig.show()

"""Conforme a distribuição, percebemos que:

* A maior recorrência de contratos é em período integral

* Pouquissimos casos são freelance e/ou meio período

## Top 10 países com mais empregados

* Vamos análisar quais são os 10 países com mais empregados
"""

# Definindo a quantidade de funcionários e separando os países
qtd_funcionarios = df['employee_residence'].value_counts()
top10_paises = qtd_funcionarios[:10]

# Criação do gráfico com Plotly Express
fig = px.bar(
    y = top10_paises.values, 
    x = top10_paises.index,
    color = top10_paises.index,
    text = top10_paises.values,
    title = 'Top 10 Países com mais empregados'
)

# Definições do gráfico
fig.update_layout(
    xaxis_title = "Países", 
    yaxis_title = "Quantidade de funcionários",
# Largura (w) e altura (h) em pixels
    width=1000,
    height=400
)

# Mostrando o gráfico
fig.show()

"""* Em termos de número de funcionários, os EUA lideram, seguidos por GBR, CAN e ESP.

## Comparação de local de empresas e residência de funcionários
"""

# Definindo a localidade de empresas / residência de funcionários
country = coco.convert(
    names=df['company_location'], 
    to="ISO3"
)
df['company_location'] = country

local_empresa = df['company_location'].value_counts()
top10_empresas_funcionarios = local_empresa[:10]

# Criação do gráfico com Plotly Express
fig = go.Figure(
    data = [
        go.Bar(
            name = 'Residência do funcionário',
            x = top10_empresas_funcionarios.index, 
            y = top10_empresas_funcionarios.values,
            text = top10_empresas_funcionarios.values
            ),
        go.Bar(
            name = 'Local da empresa', 
            x = top10_empresas_funcionarios.index,
            y = top10_empresas_funcionarios.values, 
            text = top10_empresas_funcionarios.values
            )
        ]
)

# Definições do gráfico
fig.update_layout(
    barmode = 'group', 
    xaxis_tickangle = -45,
    title='Comparação da Residência do Funcionário e Localização da Empresa',
    # Largura (w) e altura (h) em pixels
    width=1000,
    height=400
)

# Mostrando o gráfico
fig.show()

"""* Em 2023, todos os países possuem um número semelhante de residências de funcionários e localizações de empresas.

## Distribuição por tamanho das empresas

* S = Empresas de pequeno porte

* M = Empresas de médio porte

* L = Empresas de grande porte
"""

# Definindo os grupos de empresas
grupos = df['company_size'].value_counts()

# Criação do gráfico com Plotly Express
fig = px.bar(
    y = grupos.values, 
    x = grupos.index,
    color = grupos.index, 
    text = grupos.values,
    title = 'Distribuição de empresas por porte'
)

# Definições do gráfico
fig.update_layout(
    xaxis_title = "Porte da empresa", 
    yaxis_title = "Quantidade",
    # Largura (w) e altura (h) em pixels
    width=1000,
    height=400
)

# Mostrando o gráfico
fig.show()

"""* O tamanho das empresas consistem principalmente em empresas de médio porte, em seguida, as de grande porte, ficando por ultimo as de pequeno porte.

## Análisando os salários
Boxplot de informação
* média
* máximo
* mínimo

Distribuição salarial
* por faixa
"""

# Trazendo informação de salário em um boxplot e criando o gráfico
fig = px.box(
    y = df['salary_in_usd'], 
    title = 'Salário em Dólar')

# Definições do gráfico
fig.update_layout(
    xaxis_title = "Estatísticas", 
    yaxis_title = "Salário",
    # Largura (w) e altura (h) em pixels
    width=800,
    height=600
)

# Mostrando o gráfico
fig.show()

# Trazendo informação de salário em histograma
hist_data = [df['salary_in_usd']]
group_labels = ['salary_in_usd']

# Criando o gráfico
fig = ff.create_distplot(
    hist_data, 
    group_labels, 
    show_hist = False
)
# Definições do gráfico
fig.update_layout(
    title = 'Distribuição - Salário em Dólar ($)',
    # Largura (w) e altura (h) em pixels
    width=1000,
    height=400
) 
# Mostrando o gráfico
fig.show()

"""* Observamos que o salário em USD ($) está distribuído principalmente entre 95/100k - 175/180k.

## Análise da distribuição de funcionários trabalhando Remoto, Hibrido e Presencial

A coluna 'remote_ratio' consiste em 3 valores:

* 0: Nenhum trabalho remoto (menos de 20%)

* 50 : Parcialmente remoto

* 100 : Totalmente remoto (mais de 80%)
"""

# Criando grupos de trabalho
tipo_trabalho = ['Remoto', 'Hibrido', 'Presencial']
# Criando o gráfico
fig = px.bar(
    x = tipo_trabalho, 
    y = df['remote_ratio'].value_counts().values,
    color = tipo_trabalho, 
    text = df['remote_ratio'].value_counts().values,
    title = 'Distribuição do tipo de trabalho'
)
# Definições do gráfico
fig.update_layout(
    xaxis_title = "Remote Type", 
    yaxis_title = "count",
    # Largura (w) e altura (h) em pixels
    width=1000,
    height=400
)
# Mostrando o gráfico
fig.show()

"""* Em 2023 a maioria das empresas ainda seguirá a rota totalmente remota, seguida de perto pela política híbrida/parcialmente remota e, em seguida, pela política sem controle presencial.

## Nível de experiência por cargos

* Comparação dos níveis de experiência por cargo
"""

# Pegando os dados do df já criado
nivel_exp = df.groupby(['experience_level','job_title']).size()
# Iniciando as variáveis
junior_top5 = nivel_exp['Junior'].sort_values(ascending = False)[:5]
pleno_top5 = nivel_exp['Pleno'].sort_values(ascending = False)[:5]
senior_top5 = nivel_exp['Senior'].sort_values(ascending = False)[:5]
executive_top5 = nivel_exp['Executive'].sort_values(ascending = False)[:5]

# Definindo os níveis de experiência
exp_type = df.groupby(['experience_level','employment_type']).size()

# Criando o gráfico
fig = go.Figure(data=[
    go.Bar(name = 'Junior', x = junior_top5.index, 
           y=junior_top5.values, text = junior_top5.values),
    go.Bar(name = 'Pleno', x = pleno_top5.index,
           y = pleno_top5.values, text = pleno_top5.values ),
    go.Bar(name = 'Senior', x = senior_top5.index,
           y = senior_top5.values, text = senior_top5.values),
    go.Bar(name = 'Executive', x = executive_top5.index,
           y = executive_top5.values, text = executive_top5.values)
    ]
)

fig.update_layout(
    xaxis_tickangle = -45, 
    title = 'Experiece Level with top 5 job designations',
    # Largura (w) e altura (h) em pixels
    width=1000,
    height=400
)
# Mostrando o gráfico
fig.show()

"""#### Observações

* O cargo de Arquiteto de Dados possui apenas pessoas com experiência de nível sênior.

* O nível de entrada/júnior tende a ter uma posição de analista de dados maior em comparação com o cientista de dados, engenheiro de dados e engenheiro de ML.

* Nível Pleno tende a ter maios posições de cientista de dados, engenheiro de dados e analista de dados.

* Obviamente, não há trabalho de cientista de dados e analista de dados com nível executivo, mas tende a ter cargo de engenheiro de dados e diretor.

* O cargo de Cientista de Pesquisa é composto apenas pela posição de nível Pleno

### Tamanho da empresa x nível de experiência dos funcionários de dados

Vamos descobrir quais empresas tem mais pessoas a nível:
* Junior
* Pleno
* Senior
* Executivo
"""

# Trazendo informação do tamanho da empresa e nível de cargo
tamanho_nivel = df.groupby(['experience_level','company_size']).size()

# Criando gráfico
fig = go.Figure(data = [
    go.Bar(name = 'Junior', x = tamanho_nivel['Junior'].index,
           y = tamanho_nivel['Junior'].values, 
           text = tamanho_nivel['Junior'].values),
    go.Bar(name = 'Pleno', x = tamanho_nivel['Pleno'].index,
           y = tamanho_nivel['Pleno'].values, 
           text = tamanho_nivel['Pleno'].values),
    go.Bar(name = 'Senior', x = tamanho_nivel['Senior'].index,
           y = tamanho_nivel['Senior'].values, 
           text = tamanho_nivel['Senior'].values),
    go.Bar(name = 'Executive', x = tamanho_nivel['Executive'].index,
           y = tamanho_nivel['Executive'].values, 
           text = tamanho_nivel['Executive'].values)
    ]
)
# Configurando o gráfico
fig.update_layout(
    xaxis_tickangle = -45, 
    title = 'Nível de experiência por tamanho da empresa',
    # Largura (w) e altura (h) em pixels
    width=1000,
    height=400
)
# Mostrando o gráfico
fig.show()

"""#### Observações:

* Em empresas de grande porte, a maioria são os seniores, seguidos pelos plenos e depois pelos junior's. Muito pouco em nível executivo como pode ser vistos.

* Para empresas de médio porte, Temos o maior volume de nível sênior, seguido pelo nível pleno e, em seguida, os junior's. Executivo um pouco proeminente em comparação com as empresas de grande porte.

* Para empresas / startups de pequeno porte, vemos que consiste em todos os três níveis proporcionalmente, além dos executivos.

## Análise salarial

* Salário base por ano
"""

# Selecionando os anos
ano_2020 = df.loc[(df['work_year'] == 2020)]
ano_2021 = df.loc[(df['work_year'] == 2021)]
ano_2022 = df.loc[(df['work_year'] == 2022)]
ano_2023 = df.loc[(df['work_year'] == 2023)]

# Definindo os as informações para o gráfico
hist_data = [
    ano_2020['salary_in_usd'], 
    ano_2021['salary_in_usd'],
    ano_2022['salary_in_usd'],
    ano_2023['salary_in_usd']
]
group_labels = [
    'Salários 2020', 'Salários 2021',
    'Salários 2022', 'Salários 2023'
]
year_salary = pd.DataFrame(columns = ['2020', '2021', '2022', '2023'])

year_salary['2020'] = ano_2020.groupby(
    'work_year'
).mean('salary_in_usd')['salary_in_usd'].values

year_salary['2021'] = ano_2021.groupby(
    'work_year'
).mean('salary_in_usd')['salary_in_usd'].values

year_salary['2022'] = ano_2022.groupby(
    'work_year'
).mean('salary_in_usd')['salary_in_usd'].values

year_salary['2023'] = ano_2023.groupby(
    'work_year'
).mean('salary_in_usd')['salary_in_usd'].values

# Criando o gráfico
fig1 = ff.create_distplot(
    hist_data, 
    group_labels, 
    show_hist = False
)
fig2 = go.Figure(
    data=px.bar(
        x = year_salary.columns,
        y = year_salary.values.tolist()[0],
        color = year_salary.columns,
        title = 'Média salarial por ano'
      )
)

# Configurando o gráfico 1 e 2
fig1.update_layout(
    title = 'Distribuição salarial por ano',
    # Largura (w) e altura (h) em pixels
    width=1000,
    height=500
)
fig2.update_layout(
    xaxis_title = "Ano trabalhado", 
    yaxis_title = "Média salarial (k)",
    # Largura (w) e altura (h) em pixels
    width=1000,
    height=400
)
# Mostrando o gráfico
fig1.show()
fig2.show()

"""#### Observações 

* Existem valores salariais mais altos em 2023 e 2022 do que os níveis em 2021 e 2020.

* Os níveis salariais em 2021 e 2020 são praticamente os mesmos.

### Salário por nível de experiência
"""

# Selecionando os salários e níveis de experiência
salario_exp = df[['experience_level','salary_in_usd']]
salario_junior = salario_exp.loc[salario_exp['experience_level'] == 'Junior']
salario_pleno = salario_exp.loc[salario_exp['experience_level'] == 'Pleno']
salario_senior = salario_exp.loc[salario_exp['experience_level'] == 'Senior']
salario_exec = salario_exp.loc[salario_exp['experience_level'] == 'Executive']

# criando os eixos os salários e níveis
hist_data = [
    salario_junior['salary_in_usd'], salario_pleno['salary_in_usd'], 
    salario_senior['salary_in_usd'], salario_exec['salary_in_usd']
]
niveis = ['Junior', 'Pleno', 'Senior', 'Executive']

# Gerando as médias
medias = [
    salario_junior['salary_in_usd'].mean(), 
    salario_pleno['salary_in_usd'].mean(),
    salario_senior['salary_in_usd'].mean(), 
    salario_exec['salary_in_usd'].mean(),
    ]
# Criando gráficos 1 e 2
fig1 = ff.create_distplot(
    hist_data, 
    niveis, 
    show_hist = False
)
fig2 = go.Figure(
    data=px.bar(
        x = niveis, y = medias, color = niveis,
        title = 'Média Salarial por nível de experiência')
)

# Configurando os gráficos 1 e 2                            
fig1.update_layout(
    title = 'Distribuição salarial por nível de experiência',
    # Largura (w) e altura (h) em pixels
    width=1000, height=500
)
fig2.update_layout(
    xaxis_title = "Nível de experiência", 
    yaxis_title = "Média salarial (k) ",
    # Largura (w) e altura (h) em pixels
    width=1000, height=400
)
# Mostrando gráficos 1 e 2
fig1.show()
fig2.show()

"""#### Observações 

* Observamos que o nível de junior é distribuído junto com os salários mais baixos, enquanto o nível executivo é plotado junto com os salários mais altos.

### Base salarial por tamanho da empresa
"""

# Selecoinando informações pelo tamanho da empresa
tamanho_emp = df[['company_size','salary_in_usd']]
pequena = salario_exp.loc[tamanho_emp['company_size'] == 'S']
media = salario_exp.loc[tamanho_emp['company_size'] == 'M']
grande = salario_exp.loc[tamanho_emp['company_size'] == 'L']

hist_data = [
    pequena['salary_in_usd'],
    media['salary_in_usd'],
    grande['salary_in_usd']
]
tamanho = ['Pequeno porte', 
           'Médio porte', 
           'Grande porte']

medias = [
    pequena['salary_in_usd'].mean(), 
    media['salary_in_usd'].mean(), 
    grande['salary_in_usd'].mean()
]

# Criando gráficos 1 e 2
fig1 = ff.create_distplot(
    hist_data, 
    tamanho, 
    show_hist = False,
)
fig2 = go.Figure(
    data = px.bar(
        x = tamanho, y = medias, color = tamanho,
        title = 'Média salarial por tamanho de empresa',
    )
)

# Configurando gráficos 1 e 2
fig1.update_layout(
    title = 'Distribuição salarial (k) por tamanho de empresa',
# Largura (w) e altura (h) em pixels
    width=1000, height=500
)
fig2.update_layout(
    xaxis_title = "Tamanho da empresa", 
    yaxis_title = "Média salarial (k)",
# Largura (w) e altura (h) em pixels
    width=1000, height=400
)
# Mostrar Gráficos 1 e 2
fig1.show()
fig2.show()

"""#### Observações

* Percebe-se que as empresas de médio porte estão distribuídas junto com os salários mais altos, as empresas de grande porte têm salários mais altos do que as de pequeno porte.

* Assim, podemos concluir que uma empresa de grande porte não necessariamente tem salários mais altos do que uma empresa de médio porte.
"""