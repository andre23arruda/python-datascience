#%% Aulas 1 e 2 - importando pandas e carregando arquivo
import pandas as pd

dados = pd.read_csv(r'csv/aluguel.csv',sep = ';') # separado por ';' o normal é ser separado por virgula normal
dados.head()

#%% Aula 2 - informações sobre a base de dados
print(dados.dtypes)
tipos_de_dados = pd.DataFrame(dados.dtypes,columns = ['Tipos de Dados']) # criando dataframe
tipos_de_dados.columns.name = 'Variáveis' # renomeando coluna padão index
tipos_de_dados 
print(f'A base de dados apresenta {dados.shape[0]} imoveis e {dados.shape[1]} caracteristicas')

#%% Aula Extra - lendo outros formatos
dados_json = pd.read_json(r'csv/aluguel.json') #json
print('\n ---------------- json ----------------')
print(dados_json.head())

dados_txt = pd.read_table(r'csv/aluguel.txt') # txt (normalmente é separado por tabulação)
print('\n ---------------- txt ----------------')
print(dados_txt.head())

dados_excel = pd.read_excel(r'csv/aluguel.xlsx') # excel
print('\n ---------------- xlsx ----------------')
print(dados_excel.head())

dados_html = pd.read_html(r'csv/dados_html_1.html') # tabela html contida em um site
print('\n ---------------- html ----------------')
print(dados_html[0].head()) # read_html retorna uma lista, por isso [0]

#%% Aula 3 - tipos de imoveis
import pandas as pd

dados = pd.read_csv(r'csv/aluguel.csv',sep = ';') # separado por ';' o normal é ser separado por virgula normal
tipos_de_imoveis = pd.DataFrame(dados['Tipo'].drop_duplicates().reset_index(drop=True))
tipos_de_imoveis.columns.name = 'Id'
tipos_de_imoveis

#%% Aula Extra - criando estrutura de dados
import pandas as pd
data = [1,2,3,4,5]
s = pd.Series(data) # series a partir de uma lista
index = ['Linha ' + str(i) for i in range(len(data))] # contrução de lista com for embutido
s = pd.Series(data = data,index = index)  # series a partir de uma lista

data_dict = {'Linha ' + str(i+1): i+1 for i in range(len(data))}
s_from_dict = pd.Series(data_dict)
s_from_dict

s1 = s+2 # somando valores em uma series
s1

#%% Aula Extra - DataFrame
data = [[1,2,3],
        [4,5,6],
        [7,8,9]]
data

df1 = pd.DataFrame(data)
df1

index = ['Linha ' + str(i) for i in range(len(data))] # nome das linhas
columns = ['Coluna ' + str(i) for i in range(len(data[0]))] # nome das colunas

df1 = pd.DataFrame(data = data,index = index) # criando dataframe com o nome da linhas
df1.columns = columns # determinando o nome das colunas
df1
# é possivel criar desse jeito com dicionarios e tuplas tambem

#%% Aula Extra - concatenar dataframe
df1 = pd.DataFrame(data = data,index = index) # criando dataframe com o nome da linhas
df1.columns = columns # determinando o nome das colunas

df2 = pd.DataFrame(data = data,index = index) # criando dataframe com o nome da linhas
df2.columns = columns # determinando o nome das colunas

df3 = pd.DataFrame(data = data,index = index) # criando dataframe com o nome da linhas
df3.columns = columns # determinando o nome das colunas

df1[df1>0] = 'A'
df2[df2>0] = 'B'
df3[df3>0] = 'C'

df4 = pd.concat([df1,df2,df3]) # concatenando na vertical
df4

df5 = pd.concat([df1,df2,df3],axis=1) # concatenando na horizontal
df5

#%% Aula 4 - imoveis residenciais
import pandas as pd

dados = pd.read_csv(r'csv/aluguel.csv',sep = ';') # separado por ';' o normal é ser separado por virgula normal
residencial = ['Casa','Quitinete','Apartamento']
selecao_residencial = dados['Tipo'].isin(residencial)
selecao_residencial.head(10)

dados_residencial = dados[selecao_residencial].reset_index(drop=True)
dados_residencial2 = dados.query('Tipo == "Casa" or Tipo == "Quitinete" or Tipo == "Apartamento"').reset_index(drop=True) # pode ser desse jeito também

#%% Aula 4 - exportando dados csv
dados_residencial.to_csv(r'csv/aluguel_residencial.csv',sep=';',index=False)
dados_residencial2 = pd.read_csv(r'csv/aluguel_residencial.csv',sep=';')

#%% Aula Extra - Ordenando dataframe
import pandas as pd
data = [[1,2,3],
        [4,5,6],
        [7,8,9]]

df = pd.DataFrame(data,list('321'),list('ZYX')) # dataframe com nome de linhas e colunas

df1 = df.sort_index() # ordenando de acordo com index
df1.sort_index(inplace=True,axis=1) # ordenando de acordo com o nome das colunas

df2 = df.sort_values(by=['X']) # Ordenando de acordo com a coluna X
df2
# o parametro inplace serve para atualizar os valores no dataframe 

#%% Aula 5 - Seleções e frequencias
import pandas as pd

dados = pd.read_csv(r'csv/aluguel.csv',sep = ';') # separado por ';' o normal é ser separado por virgula normal

dados_tipo_apartamento = dados.query('Tipo == "Apartamento"')
print(f'\nApartamentos: {dados_tipo_apartamento.shape[0]}')

casas = ['Casa','Casa de Condomínio','Casa de Vila']
casas_selecao = dados.Tipo.isin(casas)
dados_tipo_casas = dados[casas_selecao]
n_tipos_casas = dados_tipo_casas.Tipo.value_counts().reset_index()
n_tipos_casas.columns = ['Tipo','Total']
print('\n')
print(n_tipos_casas)


dados_60a_100a = dados.query('Area >= 60 and Area <=100') 
dados_60a_100a_V2 = dados[(dados.Area >= 60) & (dados.Area <=100)] # Pode ser assim também

print(f'\nImoveis com area maior que 60 e menor que 100 m²: {dados_60a_100a.shape[0]}')

dados_4q_2000r = dados.query('Quartos >= 4 and Valor < 2000')
print(f'\nImoveis com pelo menos 4 quartos e aluguel menor que R$2000: {dados_4q_2000r.shape[0]}')

#%% Aula Extra - Formas de seleção
data = [[1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]]

df = pd.DataFrame(data,'L1 L2 L3 L4'.split(),'C1 C2 C3'.split()) # dataframe com nome de linhas e colunas
df

df[0:1] # exibindo a primeira linha somente
df[0:1][['C3','C2']] # exibindo a primeira e as duas ultimas colunas

df.loc['L4'] # encontrando linha através de seu nome
df.loc[['L4','L2']] # encontrando linhas através de seu nome
df.loc['L1','C2'] # encontrando elemento através do nome da linha e coluna
df.loc[['L4','L2'],['C1','C2']] # encontrando elemento através do nome da linha e coluna

df.iloc[1,2] # encontrando elemento através do numero da linha e da coluna
df.iloc[[1,2],[1,2]] # encontrando elemento através do numero da linha e da coluna

#%% Aula 6 - Criando dados faltantes
import pandas as pd

dados = pd.read_csv(r'csv/aluguel.csv',sep = ';') # separado por ';' o normal é ser separado por virgula normal
dados.loc[0:25,'IPTU'] = None # colocando valor nulo em alguns IPTU
dados.loc[10:18,'Condominio'] = None # colocando valor nulo em alguns Condominio
dados.loc[5:16,'Valor'] = None # colocando valor nulo em alguns Valor
dados.to_csv(r'csv/aluguel_edit.csv',sep=';',index=False) # salvando esses novos dados

#%% Aula 6 - Tratando dados faltantes
import pandas as pd

dados = pd.read_csv(r'csv/aluguel_edit.csv',sep = ';') # separado por ';' o normal é ser separado por virgula normal

dados.info() # informações sobre as colunas (exibe a quantidade de valores não nulos)
dados_null = dados.isnull() # quem é null

dados[dados.Valor.isnull()] # exibindo imoveis que tem valor null

A = dados.shape[0]
dados.dropna(subset= ['Valor'],inplace=True)
B = dados.shape[0]

print(f'\nValores antigos: {A} \nValores novos: {B} \nDrop: {A-B}')


#%% Aula 6 - Tratando dados faltantes (parte 2)
# Vamos remover quem é apartamento e condominio é null
selecao = ~((dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())) # vou descartar quem satisfaz essas condições
dados2 = dados[selecao]
print(f'\nValores antigos: {dados.shape[0]} \nValores novos: {dados2.shape[0]} \nDrop: {dados.shape[0] - dados2.shape[0]}')
dados2.info() # mas podemos ver que ainda tem null
# para isso, vamos preencher com zero quem é null
dados2 = dados2.fillna({'Condominio':0,'IPTU':0})
dados2.info() # mas podemos ver que ainda tem null
dados2.to_csv(r'csv/aluguel_essencial.csv',sep=';',index=False) # salvando esses novos dados

#%% Aula extra - métodos de interpolação
import pandas as pd

data = [0.5,None,None,0.52,0.54,None,None,0.59,0.60,None,0.7]
s = pd.Series(data)
s

s1 = s.fillna(0) # preenche null com zero
s2 = s.fillna(method='ffill') # preenche null com o valor anterior
s3 = s.fillna(method='bfill') # preenche null com o valor posterior
s4 = s.fillna(method='ffill',limit=1) # preenche com valor anterior só uma vez, se tive 2 null seguidos, só preenche um
s5 = s.fillna(value=s.mean())

#%% Aula 7 - Novas variáveis
import pandas as pd

dados = pd.read_csv(r'csv/aluguel_essencial.csv',sep=';') 
dados.drop(['Valor m2','Tipo Agregado'],axis=1,inplace=True) # removendo as colunas Valor m2 e Tipo agregado para cria-las
dados.head()

dados['Valor Bruto'] = dados.Valor + dados.Condominio + dados.IPTU
dados['Valor m2'] = (dados.Area / dados.Valor).round(2)
casa = ['Casa','Casa de Condomínio','Casa de Vila']
dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')
# usando lambda function para colocar o valor em cada registro com o método apply

#%% Aula Extra - Contando registros
import pandas as pd

dados = pd.read_csv(r'csv/aluguel_essencial.csv',sep=';') 

dados.Tipo.unique() # quais tipos de imoveis tem registrado
dados.Tipo.value_counts() # tipos de imoveis e suas contagens

#%% Aula 8 - Agrupamentos
import pandas as pd

dados = pd.read_csv(r'csv/aluguel_essencial.csv',sep=';') 
dados.Valor.mean()

bairros = ['Barra da Tijuca','Copacabana','Ipanema','Leblon']
selecao = dados.Bairro.isin(bairros)
dados = dados[selecao]

grupo_bairro = dados.groupby('Bairro') # agrupando por bairros
grupo_bairro_info = grupo_bairro.groups # algumas informações
# Agrupa por bairro e mantém as caracteristicas (Valor, area, condominio, etc )
grupo_bairro[['Valor','Condominio']].mean().round(2)  # Tirando media de valor e condominio de cada grupo

#%% Aula 8 - Estatisticas descritivas
pd.set_option('display.max_columns', 8) # configurando numero de colunas que devem ser exibidas

grupo_bairro.Valor.describe().round(2) # exibindo informações
grupo_info = grupo_bairro.Valor.aggregate(['min','max','sum']).reset_index() # exibindo apenas min, max e sum
grupo_info.columns = ['Bairro','Minimo','Maximo','Soma']

fig = grupo_bairro.Valor.mean().plot.bar(color = 'g')
fig.set_ylabel('Valor do Aluguel')
fig.set_title('Valor médio do aluguel por bairro')

#%% Aula extra - classes de valores
import pandas as pd

dados = pd.read_csv(r'csv/aluguel_essencial.csv',sep=';') 

classes = [0,2,4,6,100] # classes de numero de quartos
labels_classes = ['<= 2 quartos','3 <= quartos <= 4','5 <= quartos <= 6', '7 <= quartos'] # labels de cada classe
quartos = pd.cut(dados.Quartos,classes,labels=labels_classes) # dividindo em classes
quartos.value_counts()








