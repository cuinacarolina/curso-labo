#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:20:52 2024

@author: mcerdeiro
"""

import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
#from statsmodels.datasets import get_rdataset
#from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram , cut_tree

#%%
"""
 Herramientas de aprendizaje no supervisado
 Estrategia que vamos  ver: Clustering - Agrupamiento
 metodos para encontrar subgrupos homogneos dentro del conjunto entero de datos
 la seleccion de atributos nos condiciona el agrupamineto
 agrupar de modo que los datos que pertenecen a un mismo grupo sean similares. 
 y los mismos pertenencientes a distintos grupos sean distintos entre si.
 queremos que describan de la mejor forma los datos que cotamos y como se relacionan entre si las variables.
 La distancia entre elementos de un mismo grupo es chica y grande cuando estoy con miembros de distinto grupo.
 Algoritmos de clustering; 
 - De partición:
     cada dato esta en un y solo un cluster
     cada cluster debe tener al menos un dato
 - Jerarquicos:
     (bottom up) : empiezan con n cluster y se combinan grupos
     divisorios (top down): comienzan con un cluster de n observaciones y en cada paso se dividen
 Aplicaciones:
     genes, segmentación del mercado, analisis de redes sociales.
     
     
     
     
 Vamos a ver k-means o k-medias (de partición)
 (inicializacion y asignacion) asignos centroides. los puntos van con el centroide mas cercano
 (actualización) ahora se relocalizan los centroides (van al centro de su grupo asignado)
 (asignacion) se rolocalizan los puntos segun el centroide que les queda mas cerca
 Itero n veces cada iteracion es (asignacion, actualizacion)
 
 
 Funcion de distorcion; a cada punto le calculo la distancia a cada cluster al cuadrado y se la sumo.
 en cada paso voy bajando la metrica
 
 ¿como elegimos el valor de k?
 graficar WCSS con distintos valores de k. Y usamos el metodo codo (cuando baja abruptamente)
 
 Problema para encontrar cluster cuando las densidades son muy distintas o no tiene forma esferica.
 Desventajas
 sensible al ruido y outliers
 necesita especificar numeros de clusters
 
 
 DBSCAN
 basado en la densidad
 Parametros; - eps: distancia para la vecindad
             - minpts: cant de vecinos requeridos
 p punto nucleo
 q es un punto alcanzable desde p 
 ruido es un punto no alcanzable desde p
 cada cluster tiene un punto nucleo. Los que quedan fuera son los outliers.
 """
 #%%
#%%
np.random.seed (0);
X = np.random.standard_normal ((50 ,2));
X[:25 ,0] += 3;
X[:25 ,1] -= 4;

#%%
fig , ax = plt.subplots (1, 1, figsize =(8 ,8))
ax.scatter(X[:,0], X[:,1])
#%%
kmeans = KMeans(n_clusters = 2, random_state = 2, n_init = 20)
kmeans.fit(X)
kmeans.labels_
#%%

fig , ax = plt.subplots (1, 1, figsize =(8 ,8))
ax.scatter(X[:,0], X[:,1], c=kmeans.labels_)
ax.set_title("K-Means Clustering Results with K=2");

#%%
kmeans = KMeans(n_clusters =3, random_state =3, n_init =20)
kmeans.fit(X)
fig , ax = plt.subplots(figsize =(8 ,8))
ax.scatter(X[:,0], X[:,1], c=kmeans.labels_)
ax.set_title("K-Means Clustering Results with K=3");


#%%
kmeans1 = KMeans(n_clusters =3, random_state =3, n_init =1)
kmeans1.fit(X) 
kmeans20 = KMeans(n_clusters =3, random_state =3, n_init =20)
kmeans20.fit(X);

kmeans1.inertia_ , kmeans20.inertia_

#%%
dbclust = DBSCAN(eps=0.5, min_samples=3)

dbclust.fit(X)
fig , ax = plt.subplots(figsize =(8 ,8))
ax.scatter(X[:,0], X[:,1], c=dbclust.labels_)
ax.set_title("DBSCAN Results");
#%% ejemplos
# eps elijo la distancia. min_samples la minima cant de puntos cercanos
dbclust = DBSCAN( eps= 0.5 , min_samples= 10 )
dbclust.fit(X)
fig , ax = plt.subplots(figsize =(8 ,8))
ax.scatter(X[:,0], X[:,1], c=dbclust.labels_)
ax.set_title("DBSCAN Results");

#%%
HClust = AgglomerativeClustering
hc_comp = HClust( distance_threshold =0, n_clusters=None , linkage='complete')
hc_comp.fit(X)
#%%
fig , ax = plt.subplots(figsize =(8 ,8))
ax.scatter(X[:,0], X[:,1], c=hc_comp.labels_)
ax.set_title("Agglomerative Clustering Results");
#%%
HClust = AgglomerativeClustering
hc_comp = HClust( distance_threshold =None, n_clusters=3 , linkage='complete')
hc_comp.fit(X)
#%%
fig , ax = plt.subplots(figsize =(8 ,8))
ax.scatter(X[:,0], X[:,1], c=hc_comp.labels_)
ax.set_title("Agglomerative Clustering Results");
#%%
HClust = AgglomerativeClustering
hc_comp = HClust( distance_threshold = None, n_clusters=2 , linkage='complete')
hc_comp.fit(X)
#%%
fig , ax = plt.subplots(figsize =(8 ,8))
ax.scatter(X[:,0], X[:,1], c=hc_comp.labels_)
ax.set_title("Agglomerative Clustering Results");

#%% EJEMPLO
HClust = AgglomerativeClustering
hc_comp = HClust( distance_threshold = 8, n_clusters= None, linkage = 'complete')
hc_comp.fit(X)

fig , ax = plt.subplots(figsize =(8 ,8))
ax.scatter(X[:,0], X[:,1], c=hc_comp.labels_)
ax.set_title("Agglomerative Clustering Results");


#%%
hc_avg = HClust(distance_threshold =0, n_clusters=None , linkage='average'); 
hc_avg.fit(X)
hc_sing = HClust(distance_threshold =0, n_clusters=None , linkage='single');
hc_sing.fit(X);

#%%
D = np.zeros ((X.shape [0], X.shape [0]));
for i in range(X.shape [0]):
    x_ = np.multiply.outer(np.ones(X.shape [0]) , X[i])
    D[i] = np.sqrt(np.sum((X - x_)**2, 1));
hc_sing_pre = HClust( distance_threshold =0, n_clusters=None , metric='precomputed', linkage='single')
hc_sing_pre.fit(D)

#%%
def compute_linkage(model):
    # Create linkage matrix 
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    return linkage_matrix
    

def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)

#%%

hc_comp = HClust( distance_threshold =0, n_clusters=None , linkage='complete')
hc_comp.fit(X)

linkage_comp = compute_linkage(hc_comp)
dendrogram(linkage_comp)

plt.figure(figsize = (15,15))
plt.title("Hierarchical Clustering Dendrogram")
# plot the top three levels of the dendrogram
#plot_dendrogram(hc_comp, truncate_mode="level", p=3)
dendrogram(linkage_comp , ax=ax , color_threshold =4, above_threshold_color ='black');

#plot_dendrogram(hc_comp)
plt.show()

#%%
cargs = {'color_threshold':-np.inf , 'above_threshold_color':'black'}
linkage_comp = compute_linkage(hc_comp)
fig , ax = plt.subplots(1, 1, figsize =(12, 8))
dendrogram(linkage_comp , ax=ax , ** cargs);

#%%
fig , ax = plt.subplots (1, 1, figsize =(8, 8))
dendrogram(linkage_comp , ax=ax , color_threshold =4, above_threshold_color ='black');

#%%
cut_tree(linkage_comp , n_clusters =4).T

#%%
cut_tree(linkage_comp , height = 3)

#%%
scaler = StandardScaler ()
X_scale = scaler.fit_transform(X)
hc_comp_scale = HClust( distance_threshold =0,
n_clusters=None ,
linkage='complete').fit(X_scale)
linkage_comp_scale = compute_linkage(hc_comp_scale)
fig , ax = plt.subplots (1, 1, figsize =(8, 8))
dendrogram(linkage_comp_scale , ax=ax , ** cargs)
ax.set_title("Hierarchical Clustering with Scaled Features");

#%%
######## OTROS DATOS SINTETICOS
#%%
seed = 75
n_samples = 500
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=0.05, random_state=seed)

noisy_circles = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05, random_state=seed)

blobs = datasets.make_blobs(n_samples=n_samples, random_state=seed)

varied = datasets.make_blobs(n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=seed)
#%%
for dataset in [noisy_moons, noisy_circles, blobs, varied]:
    X, y = dataset
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], s=10)
    

    plt.xticks(())
    plt.yticks(())
    plt.show()

#%%
X, y = noisy_circles
plt.figure()
plt.scatter(X[:, 0], X[:, 1], s=10)


plt.xticks(())
plt.yticks(())
plt.show()


dbclust = DBSCAN(eps=0.1, min_samples=12)

dbclust.fit(X)

plt.scatter(X[:,0], X[:, 1],c=dbclust.labels_)

#%%

X, y = noisy_moons
plt.figure()
plt.scatter(X[:, 0], X[:, 1], s=10)


plt.xticks(())
plt.yticks(())
plt.show()


dbclust = DBSCAN(eps=0.2, min_samples=3)

dbclust.fit(X)

plt.scatter(X[:,0], X[:, 1],c=dbclust.labels_)

#%%

scaler = StandardScaler()
scaler.fit(X)
Xn = scaler.transform(X)

kmeans = KMeans(n_clusters=2, random_state= 2, n_init=20)
kmeans.fit(X)
kmeans.labels_

fig , ax = plt.subplots (1, 1, figsize =(8, 8))
#FALTO COPIAR ALGO
#%%
"""
ANTE DOS EXPLICACIONES POSIBLES. ELEGIREMOS LA MAS SENCILLA
Con menos parametros o complejidad. Evita el sobrejuste. Mejora la interpretación. Los modelos mas simples son lo mas faciles de entender.
Reduce los costos computacionales.
"""