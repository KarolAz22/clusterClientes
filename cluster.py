# -*- coding: utf-8 -*-
"""cluster.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OduCy72KKMmAkNXmSKhc9RWD7SzodRkH
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
#import matplotlib.pyplot
from matplotlib import pyplot
import plotly.express as px
import seaborn as sb
# %matplotlib inline
#1 Sistema travando
#2 problema com nota fiscal
#3 notas em contingência
#4 atendimento agendado
#5 problemas com calculo
#6 problemas com NFe/NFCe/XML
#7 certificado digital
#8 Atualização de versão
#9 Comercial
#10 Aguardando chamado
#11 Erro na data/impressora
#12 treinamento
#13 Duvidas 
#14 erro na chave de acesso
#15 problema com banco de dados
#16 demora no atendimento

dadosAGO = pd.read_csv('ligações_AGO.csv')
dadosSET = pd.read_csv('ligações_SET.csv')
dadosOUT = pd.read_csv('ligações_OUT.csv')
dadosNOV = pd.read_csv('ligações_NOV.csv')
dadosDEZ = pd.read_csv('ligações_DEZ.csv')

remover = ['CODCLIENTE','NOMEFANTASIA','CLASSIFICACAO','DATA','PROBLEMA','SOLUCAO','DATASOLUCAO','SOLUCIONADOPOR']
#remover2 = ['CODCLIENTE','NOMEFANTASIA','CLASSIFICAO','DATA','CONTATO','PROBLEMA','SOLUÇÃO','DATA SOLUÇÃO','SOLUÇÃO', 'SOLUCIONADO POR']
#remover3 = ['cate','NOMEFANTASIA','CLASSIFICAO','DATA','PROBLEMA','SOLUCIONADO POR','DATA SOLUÇÃO']
 
x = dadosAGO.drop(remover,axis=1)
s = dadosSET.drop(remover, axis=1)
o = dadosOUT.drop(remover,axis=1)
#o= o.drop(324, axis=0) 
nov = dadosNOV.drop(remover, axis=1)
dez = dadosDEZ.drop(remover, axis=1)
 
#x['SUPORTE/COMERCIAL'] = x['SUPORTE/COMERCIAL'].map({'SUPORTE':'31',
                             #'COMERCIAL':'32',
                             
                             #},
                             #na_action=0)
#o['SUPORTE/COMERCIAL'] = o['SUPORTE/COMERCIAL'].map({'SUPORTE':'31',
                             #'COMERCIAL':'32',
                             
                             #},
                             #na_action=0)
#a['SUPORTE/COMERCIAL'] = a['SUPORTE/COMERCIAL'].map({'SUPORTE':'31',
                            # 'COMERCIAL':'32',
                             
                            # },
                            # na_action=0)
#x = x.fillna(0) #Preencher todos os valores faltantes por 0
#o = o.fillna(0) #Preencher todos os valores faltantes por 0
#s = s.fillna(0) #Preencher todos os valores faltantes por 0
x = x.dropna() #exclui os espaços vazios
o = o.dropna()
s = s.dropna()
nov = nov.dropna()
dez = dez.dropna()

m = pd.merge(x, o, how = 'outer')
n = pd.merge(m, s, how = 'outer')
p = pd.merge(n,nov, how = 'outer')
q = pd.merge(p,dez, how = 'outer')
fig = px.scatter(q, x = 'SUPORTE/COMERCIAL', y = 'CIDADE', color = 'SUPORTE/COMERCIAL')
#fig = px.scatter(m, x = 'SUPORTE/COMERCIAL', y = 'BAIRRO', color = 'BAIRRO')
#fig = px.scatter(s, x = 'SUPORTE/COMERCIAL', y = 'CIDADE', color = 'CIDADE')
fig.show()
q

from sklearn import cluster
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
 
#m = pd.merge(x, o, how = 'outer')
#n = pd.merge(m, s, how = 'outer')
#data_df = pd.DataFrame(n)

le = LabelEncoder()
q.CIDADE =  le.fit_transform(q.CIDADE)

q
#x.CIDADE = le.fit_transform(x.CIDADE)
#x
 
#s.CIDADE = le.fit_transform(s.CIDADE)
#dadosSET
 
#o.CIDADE = le.fit_transform(o.CIDADE)
 
#x = x.fillna(0) #Preencher todos os valores faltantes por 0
#o = o.fillna(0) #Preencher todos os valores faltantes por 0
#s = s.fillna(0) #Preencher todos os valores faltantes por 0
 
#m = pd.merge(x, o, how = 'outer')
#n = pd.merge(m, s, how = 'outer')
#fig = px.scatter(n, x = 'SUPORTE/COMERCIAL', y = 'CIDADE', color = 'SUPORTE/COMERCIAL')
#fig = px.scatter(m, x = 'SUPORTE/COMERCIAL', y = 'BAIRRO', color = 'BAIRRO')
#fig = px.scatter(s, x = 'SUPORTE/COMERCIAL', y = 'CIDADE', color = 'CIDADE')
#fig.show()

#x = x.values
#o = o.values
#m = m.values
#labelencoder_x = LabelEncoder()
#labelencoder_o = LabelEncoder()
#labelencoder_m = LabelEncoder()
#x[:, 0] = labelencoder_x.fit_transform(x[:, 0])
#o[:, 0] = labelencoder_o.fit_transform(o[:, 0])
#m[:, 0] = labelencoder_m.fit_transform(m[:, 0])

#clf = cluster.KMeans(n_clusters = 3,random_state=0)
#clf = clf.fit(x)
#cluster1 = clf.labels_
#cluster1

#clf2 = cluster.KMeans(n_clusters = 3,random_state=0)
#clf2 = clf2.fit(o)
#cluster2 = clf2.labels_
#cluster2

#34 cidades em média
clf3 = cluster.KMeans(n_clusters = 8,random_state=0)
clf3 = clf3.fit(q)
cluster3 = clf3.labels_
cluster3

#total = cluster1,cluster2
#total
#matplotlib.pyplot.hist(total)
#matplotlib.pyplot.show()
#fig = px.scatter(total, x = [1], y = [0],  width = 800)
#fig.update_traces(marker = dict(size = 12, line=dict(width = 2)), selector = dict(mode = 'markers'))
#fig.show()
#fig = px.scatter(cluster1, x = [0], y = [1]) #dispersão (não funciona)
#fig.show()

data_df = pd.DataFrame(cluster3)
data_df = data_df.rename({0: 'class_cluster'},axis = 1)


fig = px.scatter(data_df, x = 'class_cluster',  color = 'class_cluster')
fig.show() #gráfico com os dados gerados pelo K-Means
data_df

#pd.set_option('min_rows',100)
#data_df

#l = dadosNOV.drop(remover,axis=1)
#l['k-classes']=cluster1
#l

clf4 = cluster.AffinityPropagation()
clf4 = clf4.fit(q)
cr4 = clf4.labels_
cr4

from google.colab import drive
drive.mount('/content/drive')