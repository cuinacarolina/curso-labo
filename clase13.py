#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:13:44 2025

@author: Estudiante
"""

import pandas as pd
import duckdb as dd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
## PIP INSTALL SCIKIT-LEARN
carpeta = "/home/Estudiante/Descargas/"
planilla = pd.read_excel(carpeta + "DatosTiemposDeReaccion-DerechaIzquierda.xlsx") 
planilla_manohabil = pd.read_excel(carpeta + "DatosTiemposDeReaccion-HabilNoHabil.xlsx") 

#%%
#grafico izq der 
fig, ax= plt.subplots()

sns.histplot(data = planilla, x = 'Tiempo', hue = 'Mano', palette = 'colorblind')
ax.set_title('Es mas rápida la reacción con mano derecha o izquierda?')
ax.set_xlabel('Tiempo en segundos')
ax.set_ylabel('Cantidad de personas que midieron ese tiempo')

#%%

# los datos tenen variabilidad son representantes de esa poblacion
# la cs de datos nos ayudan a tomar decisiones sobre bases de datos sobre conocimientos previos
#%%

iris = load_iris(as_frame = True)
data = iris.frame
atributos = iris.data
Y = iris.target

iris.target_names
diccionario = dict(zip([0,1,2], iris.target_names))
#%%
atri = ['sepal length (cm)', 'sepal width(cm)']
#%%
nbins = 35
f, s = plt.subplots(2,2)
plt.suptitle('Histogramas de los 4 atributos', size = 'large')
sns.histplot(data = data, x = 'sepal length (cm)', hue = 'target', bins = nbins, stat = 'probability', ax = s[0,0], palette = 'viridis')
sns.histplot(data = data, x = 'petal width (cm)', hue = 'target', bins = nbins, stat = 'probability', ax = s[0,1], palette = 'viridis')
sns.histplot(data = data, x = 'sepal width (cm)', hue = 'target', bins = nbins, stat = 'probability', ax = s[1,0], palette = 'viridis')
sns.histplot(data = data, x = 'petal length (cm)', hue = 'target', bins = nbins, stat = 'probability', ax = s[1,1], palette = 'viridis')

#%% UMBRALES
def clasificador_iris(fila):
    sep_l = fila['sepal length (cm)']
    if sep_l <= 5:
        clase = 0
    elif sep_l <= 7:
        clase = 1
    else:
        clase = 2
    return clase

#%% MATRIZ DE CONFUSION
# OCURRENCY VA ENTRE 0 Y 1 MIDE QUE TAN BIEN CLASIFICADO ESTA 0 ES TODO MAL Y 1 ES PERFECTO
"""
clases = set(data['target'])
matriz_confusion = np.zeros((3,3))
for clase_real in range(3):
    for clase_predicha in range(3):
        filtro = (data_clasif['target']== i) &
        (data_clasif['clase_asignada'] == j)
        cuenta = len(data_clasif[filtro])
        matriz_confusion[i,j] = cuenta
matriz_confusion

exactitudes = []
for umbral in [5,7]:
    data_clasif = data.copy()
    for i, fila in data_clasif.iterrows():
        sep_l = fila['sepal length (cm)']
        if sep_l <= 5:
            clase = 0
        elif sep_l <= 7:
            clase = 1
        else:
            clase = 2
            data_clasif['clase_asignada'] = clase
"""
#%%
#arboles de decision 
carpeta1 = "/home/Estudiante/Descargas/Archivos+Script-20250218/"

test_titanic = pd.read_csv(carpeta1 + "test_titanic.csv") 

titanic_competencia = pd.read_csv(carpeta1 + "titanic_competencia.csv") 

titanic_training = pd.read_csv(carpeta1 + "titanic_training.csv") 
 
arboles = pd.read_csv(carpeta1 + "arboles.csv") 


fig, ax= plt.subplots()

sns.histplot(data = test_titanic, x = 'Survived', hue = 'Sex', palette = 'colorblind')
ax.set_title('sobreviven mas mujeres o varones')
ax.set_xlabel('sobrevivientes')
ax.set_ylabel('Cantidad')


fig, ax= plt.subplots()

sns.histplot(data = test_titanic, x = 'Survived', hue = 'Pclass', palette = 'colorblind')
ax.set_title('sobreviven por clase')
ax.set_xlabel('sobrevivientes')
ax.set_ylabel('Cantidad')

fig, ax= plt.subplots()

sns.histplot(data = test_titanic, x = 'Survived', hue = 'Age', palette = 'colorblind')
ax.set_title('sobreviven por edad')
ax.set_xlabel('sobrevivientes')
ax.set_ylabel('Cantidad')



#%%










