import streamlit as st
import pandas as pd
import plotly_express as px
import matplotlib.pyplot as plt
import csv



st.set_page_config(layout='wide',page_title="Projeto ISIS")

#df = pd.read_csv('panambiteste.csv', sep=',', quoting=csv.QUOTE_NONE)
#dfcru = df

cidades_disponiveis = ['Todas','Ajuricaba','Alegria','Augusto Pestana','Chiapeta','Coronel Bicaco','Ijuí','Panambi','Santo Augusto']
cidade_selecionada = st.sidebar.selectbox('Selecione a Cidade', cidades_disponiveis)

if cidade_selecionada == 'Ijuí':
  df = pd.read_csv('ijuiteste.csv', sep=',', quoting=csv.QUOTE_NONE)
elif cidade_selecionada == 'Panambi':
  df = pd.read_csv('panambiteste.csv', sep=',', quoting=csv.QUOTE_NONE)
elif cidade_selecionada == 'Santo Augusto':
  df = pd.read_csv('santoaugustoteste.csv', sep=',', quoting=csv.QUOTE_NONE)
elif cidade_selecionada == 'Alegria':
  df = pd.read_csv('alegriateste.csv', sep=',', quoting=csv.QUOTE_NONE)
elif cidade_selecionada == 'Augusto Pestana':
  df = pd.read_csv('augustopteste.csv', sep=',', quoting=csv.QUOTE_NONE)
elif cidade_selecionada == 'Chiapeta':
  df = pd.read_csv('chiapetateste.csv', sep=',', quoting=csv.QUOTE_NONE)
elif cidade_selecionada == 'Coronel Bicaco':
  df = pd.read_csv('celbicacoteste.csv', sep=',', quoting=csv.QUOTE_NONE)
elif cidade_selecionada == 'Ajuricaba':
  df = pd.read_csv('ajuricabateste.csv', sep=',', quoting=csv.QUOTE_NONE)
else:
  df = pd.read_csv('tudo.csv', sep=',', quoting=csv.QUOTE_NONE) 
  
dfcru = df

# Extrair o ano da coluna de data, assumindo que a coluna se chama 'data'
df['ano'] = df['pa_mvm'].astype(str).str[:4]

# Seleção de ano
anos_disponiveis = ['Todos'] + list(df['ano'].unique())
ano_selecionado = st.sidebar.selectbox('Selecione o Ano', anos_disponiveis)



# Filtrar o DataFrame pelo ano selecionado, se não for "Todos"
if ano_selecionado != 'Todos':
    df = df[df['ano'] == ano_selecionado]

    
    
# Seleção de CID
cids_disponiveis = ['Todos'] + list(df['pa_cidpri'].unique())
cid_selecionado = st.sidebar.selectbox('Selecione o CID', cids_disponiveis)
paleta_de_cores = ['#272b00','#004323','#188A52', '#4A9C76','#739a7a', '#A7D8C1', '#808080','#A4A4A4',  '#d3d3d3','#FFFFFF']
paleta_de_cores1 = ['#004323','#4A9C76','#739a7a','#FFFFFF']
# Filtrar o DataFrame pelo CID selecionado, se não for "Todos"
if cid_selecionado != 'Todos':
    #paleta_de_cores = ['#004f00','#2c9b22','#8ced75', '#e2ffcb']
    paleta_de_cores = ['#004323','#4A9C76','#739a7a','#FFFFFF']
    df = df[df['pa_cidpri'] == cid_selecionado]

# Seleção de ano
#anos_disponiveis = df['ano'].unique()
#ano_selecionado = st.sidebar.selectbox('Selecione o Ano', anos_disponiveis)

# Filtrar o DataFrame pelo ano selecionado
#df = df[df['ano'] == ano_selecionado]

contagem = df['pa_cidpri'].value_counts().reset_index()
contagem.columns = ['cid', 'ocorrencias']
contagem = contagem.head(11)
#df1 = df['pa_cidpri'].head(10)
#df['contagem'] = df['pa_cidpri'].map(df1)
#agrupado.to_csv('seu_arquivo_com_contagem.csv', index=False)
#print(df1)
fig = px.pie(contagem, values='ocorrencias',names='cid', title='Ocorrências de Cada CID', color_discrete_sequence=paleta_de_cores)
fig.update_traces(textposition='outside', textinfo='value+percent+label')
fig.update_layout(font = dict(color='black'))

#fig
#sex = st.sidebar.selectbox('Cid',df['pa_cidpri'].unique())
#df_filtered = df[df['pa_sexo'] == sex]

col1, col2 = st.columns(2) 
col3, col4 = st.columns(2)
col6, col7 = st.columns(2)

#plt.figure(figsize=(10, 6))
#grouped_data1.plot.pie(autopct='%1.1f%%', startangle=140, cmap='viridis', legend=True)
#plt.ylabel('')
#plt.title('Distribuição de pa_cidpri')
#plt.show()

#figure=px.pie(df['pa_cidpri'], names=['pa_cidpri'], title='Distribuição de pa_cidpri')
col1.plotly_chart(fig)

# Contando as ocorrências de cada valor na coluna 'sexo'
contagem_sexo = df['pa_sexo'].value_counts().reset_index()

# Renomeando as colunas
contagem_sexo.columns = ['sexo', 'ocorrencias']

# Criando o gráfico de barras com Plotly Express
fig1 = px.bar(contagem_sexo, x='sexo', y='ocorrencias', title='Ocorrências por Sexo',color = 'sexo',color_discrete_sequence=paleta_de_cores)
fig1.update_xaxes(tickfont=dict(color='black'))
fig1.update_yaxes(tickfont=dict(color='black'))
fig1.update_layout(xaxis_title_font=dict(color='black'),yaxis_title_font=dict(color='black'))

col2.plotly_chart(fig1)


# Definindo as faixas etárias
def categorizar_idade(idade):
    if idade <= 12:
      return 'Crianças'
    elif 13 <= idade <= 19:
      return 'Adolescentes'
    elif 20 <= idade <= 59:
      return 'Adultos'
    else:
      return 'Idosos'

# Criando uma nova coluna 'faixa_etaria' com as categorias de idade
df['faixa_etaria'] = df['pa_idade'].apply(categorizar_idade)

# Contando as ocorrências de cada valor na coluna 'faixa_etaria'
contagem_faixa_etaria = df['faixa_etaria'].value_counts().reset_index()

# Renomeando as colunas
contagem_faixa_etaria.columns = ['faixa_etaria', 'ocorrencias']

# Criando o gráfico de barras com Plotly Express
fig2 = px.bar(contagem_faixa_etaria, x='faixa_etaria', y='ocorrencias', title='Ocorrências por Faixa Etária',color='faixa_etaria',color_discrete_sequence=paleta_de_cores1)
fig2.update_xaxes(tickfont=dict(color='black'))
fig2.update_yaxes(tickfont=dict(color='black'))
fig2.update_layout(xaxis_title_font=dict(color='black'),yaxis_title_font=dict(color='black'))
# Exibindo o gráfico
col3.plotly_chart(fig2)

def categorias(raca):
  int(raca)  
  if raca == 1:
    return 'BRANCA'
  elif raca == 2:
    return 'PRETA'
  elif raca == 3:
    return 'PARDA'   
  elif raca == 4:
    return 'AMARELA' 
  elif raca == 5:
    return 'INDIGENA'  
  elif raca == 99:
    return 'SEM INFORMACAO'           
  else:
      return 'NI'

# Limpar os valores da coluna 'raca_cor' e mapear para as categorias
df['pa_racacor'] = df['pa_racacor'].map(categorias)

# Contar as ocorrências de cada categoria na coluna 'raca_cor'
contagem_raca_cor = df['pa_racacor'].value_counts().reset_index()

# Renomear as colunas
contagem_raca_cor.columns = ['raca_cor', 'ocorrencias']

# Criar o gráfico de barras com Plotly Express
fig3 = px.bar(contagem_raca_cor, x='raca_cor', y='ocorrencias', title='Ocorrências por Raça/Cor',
             labels={'raca_cor': 'Raça/Cor', 'ocorrencias': 'Ocorrências'},
             text='ocorrencias')

# Atualizar o layout para melhorar a legibilidade
fig3.update_layout(xaxis_tickangle=-45)
fig3.update_xaxes(tickfont=dict(color='black'))
fig3.update_yaxes(tickfont=dict(color='black'))
fig3.update_layout(xaxis_title_font=dict(color='black'),yaxis_title_font=dict(color='black'))
# Exibir o gráfico
#col4.plotly_chart(fig3)

# Filtrar o DataFrame para incluir apenas o público feminino
df_feminino = df[df['pa_sexo'] == 'F']

# Contar as ocorrências de cada valor na coluna 'cid' para o público feminino
contagem_cid_feminino = df_feminino['pa_cidpri'].value_counts().reset_index()

# Renomear as colunas
contagem_cid_feminino.columns = ['cid', 'ocorrencias']

# Selecionar os 10 CIDs mais frequentes
top_10_cids_feminino = contagem_cid_feminino.head(10)

# Criar o gráfico de barras com Plotly Express
fig4 = px.bar(top_10_cids_feminino, x='cid', y='ocorrencias', title='CIDs no Público Feminino',
             labels={'cid': 'CID', 'ocorrencias': 'Ocorrências'}, text='ocorrencias', color='cid',
             color_discrete_sequence=paleta_de_cores)

# Atualizar o layout para melhorar a legibilidade
fig4.update_layout(xaxis_tickangle=-45)
fig4.update_xaxes(tickfont=dict(color='black'))
fig4.update_yaxes(tickfont=dict(color='black'))
fig4.update_layout(xaxis_title_font=dict(color='black'),yaxis_title_font=dict(color='black'))
# Exibir o gráfico
col6.plotly_chart(fig4)

# Extrair o ano da coluna de data, assumindo que a coluna se chama 'data'
df['ano'] = df['pa_mvm'].astype(str).str[:4]

# Contar as ocorrências de cada linha dividida por ano
contagem_ano = df.groupby(['ano', 'pa_cidpri']).size().reset_index(name='ocorrencias')

top_10_cids_por_ano = contagem_ano.groupby('ano').apply(lambda x: x.nlargest(10, 'ocorrencias')).reset_index(drop=True)

# Criar o gráfico de barras empilhadas com Plotly Express
fig5 = px.bar(top_10_cids_por_ano, x='ocorrencias', y='ano', color='pa_cidpri', 
             title='Ocorrências por ano',
             labels={'ano': 'Ano', 'ocorrencias': 'Ocorrências', 'cid': 'CID'},color_discrete_sequence=paleta_de_cores)

fig5.update_xaxes(tickfont=dict(color='black'))
fig5.update_yaxes(tickfont=dict(color='black'))
fig5.update_layout(xaxis_title_font=dict(color='black'),yaxis_title_font=dict(color='black'))
# Exibir o gráfico
col4.plotly_chart(fig5)

# Filtrar o DataFrame para incluir apenas o público feminino
df_masculino = df[df['pa_sexo'] == 'M']

# Contar as ocorrências de cada valor na coluna 'cid' para o público feminino
contagem_cid_masculino = df_masculino['pa_cidpri'].value_counts().reset_index()

# Renomear as colunas
contagem_cid_masculino.columns = ['cid', 'ocorrencias']

# Selecionar os 10 CIDs mais frequentes
top_10_cids_masculino = contagem_cid_masculino.head(10)

# Criar o gráfico de barras com Plotly Express
fig6 = px.bar(top_10_cids_masculino, x='cid', y='ocorrencias', title='CIDs no Público Masculino',
             labels={'cid': 'CID', 'ocorrencias': 'Ocorrências'}, text='ocorrencias',color='cid',
             color_discrete_sequence=paleta_de_cores)

# Atualizar o layout para melhorar a legibilidade
fig6.update_layout(xaxis_tickangle=-45)
fig6.update_xaxes(tickfont=dict(color='black'))
fig6.update_yaxes(tickfont=dict(color='black'))
fig6.update_layout(xaxis_title_font=dict(color='black'),yaxis_title_font=dict(color='black'))
# Exibir o gráfico
col7.plotly_chart(fig6)

# Definir a faixa etária adulta
df['pa_idade'] = pd.to_numeric(df['pa_idade'], errors='coerce')
df_adulto = df[(df['pa_idade'] >= 20) & (df['pa_idade'] <= 59)]

# Contar as ocorrências de cada valor na coluna 'cid' para o público adulto
contagem_cid_adulto = df_adulto['pa_cidpri'].value_counts().reset_index()
contagem_cid_adulto.columns = ['cid', 'ocorrencias']

# Selecionar os 10 CIDs mais frequentes
top_10_cids_adulto = contagem_cid_adulto.head(10)

# Criar o gráfico de barras com Plotly Express
fig7 = px.bar(top_10_cids_adulto, x='cid', y='ocorrencias', title='Top 10 CIDs no Público Adulto',
             labels={'cid': 'CID', 'ocorrencias': 'Ocorrências'}, text='ocorrencias',
             color='cid', color_discrete_sequence=px.colors.qualitative.G10)


# Atualizar o layout para melhorar a legibilidade
fig7.update_layout(xaxis_tickangle=-45)
fig7.update_xaxes(tickfont=dict(color='black'))
fig7.update_yaxes(tickfont=dict(color='black'))
fig7.update_layout(xaxis_title_font=dict(color='black'),yaxis_title_font=dict(color='black'))
# Exibir o gráfico
#col8.plotly_chart(fig7)




