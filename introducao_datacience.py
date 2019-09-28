#%% Aula 1 -carregar pandas e ler arquivo
import pandas as pd
notas = pd.read_csv(r"csv/ratings.csv")
notas.head()
notas.shape

#%% Aula 1 - renomear colunas
notas.columns = ['usuarioID','filmeId','nota','momento']
notas.head()

#%% Aula 1 - series
nota = notas['nota'] # ou notas.nota
nota_unica = nota.unique()
nota_contagem = nota.value_counts()
media = nota.mean()

#%% Aula 2 - series
import matplotlib.pyplot as plt
nota = notas.nota
nota.plot(kind='hist')
plt.show()

#%% Aula 2 - Características
media = notas.nota.mean()
mediana = notas.nota.median()
print(f'Media: {media}')
print(f'Mediana: {mediana}')
notas.nota.describe()

#%% Aula 2 - seaborn plot
import seaborn as sns
sns.boxplot(notas.nota)
plt.show()


#%% Aula 3 - Carregar filmes
filmes = pd.read_csv(r"csv/movies.csv")
filmes.columns = ['filmeId','titulo','generos']
filmes.head()

#%% Aula 3 - Fazendo consultas no dataframe
filme_1 = notas.query("filmeId == 1") # acessamos a coluna filmeId e vemos quem é igual a 1
filme_1_nota = filme_1.nota
mean_filme_1_nota = filme_1_nota.mean()

#%% Aula 3 - agrupar filmes
grupos_filmes = notas.groupby("filmeId") # agrupando de acordo com i ID do filme
grupos_media = grupos_filmes.mean() # em cada grupo, tirando a media de cada caracteristica
medias_por_filme = grupos_media.nota # filtrando nota
medias_por_filme.head()

#%% Aula 3 - Tipos de plots
fig = plt.figure()
fig.suptitle('Histograma das medias dos filmes', fontsize=16)

plt.subplot(141)
medias_por_filme.plot(kind = 'hist') # histograma
plt.subplot(142)
sns.boxplot(medias_por_filme) # boxplot
plt.subplot(143)
sns.distplot(medias_por_filme,bins=10) # histograma com seaborn
plt.subplot(144)
plt.hist(medias_por_filme) # histograma com pyplot

plt.show()

#%% Aula 4 - Carregar tmdb (kaggle)
tmdb = pd.read_csv(r"csv/tmdb_5000_movies.csv")
pd.set_option('display.max_columns', 5) # configurando numero de colunas que devem ser exibidas
tmdb.head()

tmdb_languages = tmdb['original_language'].value_counts() # isso é uma series
tmdb_languages_df = tmdb_languages.to_frame().reset_index()
tmdb_languages_df.columns = ['original_language','total']
tmdb_languages_df.head()

#%% Aula 4 - plot tmdb idiomas
fig = plt.figure()
fig.suptitle('Contagem do idioma dos filmes', fontsize=16)
plt.subplot(121)
sns.barplot(x='original_language',y='total',data=tmdb_languages_df)
plt.subplot(122)
plt.pie(tmdb_languages_df['total'],labels = tmdb_languages_df['original_language'])
plt.show()

#%% Aula 4 - tirando informação de interesse
total_de_ingles = tmdb_languages_df.query('original_language == "en"').total[0] # procurando quem é ingles, pegando o total na primeira posicao
total_de_resto = tmdb_languages_df.query('original_language != "en"').total.sum() # procurando quem não é ingles, pegando total, somando todo mundo
dados = {'lingua': ['ingles','outros'],
         'total': [total_de_ingles,total_de_resto]
        }
dados = pd.DataFrame(dados)

fig = plt.figure()
fig.suptitle('Contagem do idioma dos filmes', fontsize=16)
plt.subplot(121)
sns.barplot(x='lingua',y='total',data=dados)
plt.subplot(122)
plt.pie(dados['total'],labels = dados['lingua'])
plt.show()

#%% Aula 5 - titando informação de interesse parte 2
tmdb_sem_ingles = tmdb.query('original_language != "en"') # procurando quem não é ingles
tmdb_sem_ingles_contagem = tmdb_sem_ingles.original_language.value_counts()

# catplot plota por categoria e kind faz contagem das categorias, muito fácil (já é um plot personalizado)
sns.catplot(x='original_language', # eixo x
            kind = 'count', # caplot vai fazer contagem da categoria
            data=tmdb_sem_ingles, # dados que contem as categorias
            aspect = 2, # aspecto retangular (dobro)
            palette = "GnBu_d", # colormap
            order=tmdb_sem_ingles_contagem.index # ordenado de acordo com a contagem de valores dos idiomas
            )

plt.show()








