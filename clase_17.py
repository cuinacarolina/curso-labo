#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:10:48 2025

@author: Estudiante
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

carpeta = "~/Descargas/Clase 16 - RLS - Archivos clase-20250225/"
autos = pd.read_csv(carpeta + "auto-mpg.xls")
#altura archivo original
altura = pd.read_csv(carpeta + 'Alturas.csv', index_col = 0)
altura = altura[['Altura (cm)','Sexo al nacer (M/F)', 'Unnamed: 3']]
altura = altura.rename(columns={'Unnamed: 3': 'Altura madre (cm)'})

#%%
# archivo solo con varones
altura_varones = altura[altura['Sexo al nacer (M/F)']== 'M']
X = altura_varones[['Altura madre (cm)']]
# archivo original solo con las alturas
alturas = altura[['Altura (cm)']]
Y = alturas[altura['Sexo al nacer (M/F)']== 'M']


neigh = KNeighborsRegressor(n_neighbors=2)
neigh.fit(X, Y)


data_nuevo = pd.DataFrame([{'Altura madre (cm)': 156}])
neigh.predict(data_nuevo)
Y_pred = neigh.predict(X)
mean_squared_error(Y, Y_pred)
#%%
lista = [] #guardo errores
i = 1
eje_x = [] #guardo los k
while i<= 21:
    neigh = KNeighborsRegressor(n_neighbors= i)
    neigh.fit(X, Y)
    data_nuevo = pd.DataFrame([{'Altura madre (cm)': 156}])
    neigh.predict(data_nuevo)
    Y_pred = neigh.predict(X)
    error = mean_squared_error(Y, Y_pred)
    lista.append(error)
    eje_x.append(i)
    i += 1
    
plt.plot(eje_x, lista, marker = 'o')
plt.title('MSE VS Número de Vecinos (k)')
plt.show()
#%%
X = autos[['acceleration']]
Y = autos[['mpg']]
neigh = KNeighborsRegressor(n_neighbors=2)
neigh.fit(X, Y)
Y_pred = neigh.predict(X)
mean_squared_error(Y, Y_pred)

lista = [] #guardo errores
i = 1
eje_x = [] #guardo los k
while i<= 21:
    neigh = KNeighborsRegressor(n_neighbors= i)
    neigh.fit(X, Y)
    Y_pred = neigh.predict(X)
    error = mean_squared_error(Y, Y_pred)
    lista.append(error)
    eje_x.append(i)
    i += 1
    
plt.plot(eje_x, lista, marker = 'o')
plt.title('MSE VS Número de Vecinos (k)')
plt.show()
#%%

sns.pairplot(autos[['mpg', 'acceleration', 'horsepower']])
#%%
X = autos[['acceleration', 'horsepower']]
Y = autos[['mpg']]
neigh = KNeighborsRegressor(n_neighbors=2)
neigh.fit(X, Y)
Y_pred = neigh.predict(X)
mean_squared_error(Y, Y_pred)

lista = [] #guardo errores
i = 1
eje_x = [] #guardo los k
while i<= 21:
    neigh = KNeighborsRegressor(n_neighbors= i)
    neigh.fit(X, Y)
    Y_pred = neigh.predict(X)
    error = mean_squared_error(Y, Y_pred)
    lista.append(error)
    eje_x.append(i)
    i += 1
    
plt.plot(eje_x, lista, marker = 'o')
plt.title('MSE VS Número de Vecinos (k) (aceleration and horsepower respect mpg')
plt.show()
#%%

X = autos[['cylinders', 'displacement']]
Y = autos[['mpg']]
neigh = KNeighborsRegressor(n_neighbors=2)
neigh.fit(X, Y)
Y_pred = neigh.predict(X)
mean_squared_error(Y, Y_pred)

lista = [] #guardo errores
i = 1
eje_x = [] #guardo los k
while i<= 21:
    neigh = KNeighborsRegressor(n_neighbors= i)
    neigh.fit(X, Y)
    Y_pred = neigh.predict(X)
    error = mean_squared_error(Y, Y_pred)
    lista.append(error)
    eje_x.append(i)
    i += 1
    
plt.plot(eje_x, lista, marker = 'o')
plt.title('MSE VS Número de Vecinos (k) (cylinder and displacement respect mpg')
plt.show()

#%%
X = autos[['weight', 'acceleration']]
Y = autos[['mpg']]
neigh = KNeighborsRegressor(n_neighbors=2)
neigh.fit(X, Y)
Y_pred = neigh.predict(X)
mean_squared_error(Y, Y_pred)

lista = [] #guardo errores
i = 1
eje_x = [] #guardo los k
while i<= 21:
    neigh = KNeighborsRegressor(n_neighbors= i)
    neigh.fit(X, Y)
    Y_pred = neigh.predict(X)
    error = mean_squared_error(Y, Y_pred)
    lista.append(error)
    eje_x.append(i)
    i += 1
    
plt.plot(eje_x, lista, marker = 'o')
plt.title('MSE VS Número de Vecinos (k) (weigth and acceleration respect mpg')
plt.show()
#%% 
"""
estaria bueno reescalar los datos. ejemplo aceleracion y peso toman escalas muy difrentes.
si 2 variables tienen rangos muy distintos y quiero comparar en la misma ecala. Busco verlos entre 0 y 1. (normalizar)
"""
autos['weigth_normalizado'] = (autos['weight'] - autos['weight'].min()) / (autos['weight'].max() - autos['weight'].min())

autos['acceleration_normalizado'] = (autos['acceleration'] - autos['acceleration'].min()) / (autos['acceleration'].max() - autos['acceleration'].min())
#%%

X = autos[['weigth_normalizado', 'acceleration_normalizado']]
Y = autos[['mpg']]
neigh = KNeighborsRegressor(n_neighbors=2)
neigh.fit(X, Y)
Y_pred = neigh.predict(X)
mean_squared_error(Y, Y_pred)

lista = [] #guardo errores
i = 1
eje_x = [] #guardo los k
while i<= 21:
    neigh = KNeighborsRegressor(n_neighbors= i)
    neigh.fit(X, Y)
    Y_pred = neigh.predict(X)
    error = mean_squared_error(Y, Y_pred)
    lista.append(error)
    eje_x.append(i)
    i += 1
    
plt.plot(eje_x, lista, marker = 'o')
plt.title('MSE VS Número de Vecinos (k) (weigth and acceleration NORMALIZE respect mpg')
plt.show()

#%%
#%%

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)
errores_train = []
errores_test = []

for k in range (1, 21):
    modelo = KNeighborsRegressor(n_neighbors= k)
    modelo.fit(X_train, Y_train)
    Y_pred_train = modelo.predict(X_train)
    Y_pred_test = modelo.predict(X_test)
    
    error_train = mean_squared_error(Y_train, Y_pred_train)
    
    error_test = mean_squared_error(Y_test, Y_pred_test)
    
    errores_train.append(error_train)
    errores_test.append(error_test)

plt.figure(figsize= (10,10))
plt.plot(list(range(1,21)),errores_train, label = 'train')
plt.plot(list(range(1,21)),errores_test, label = 'test')
plt.legend()
plt.xticks(list(range(1,21)))
plt.xlabel('cantidad de vecinos')
plt.ylabel('MSE')
plt.title('MSE segun cant de vecinos')
plt.grid()
plt.show()

#%%

"""
evaluación de modelos y selección de modelos.
etender como sera el uso, cual es el objetivo del modelo ,que metrica refleja bien lo que queremos medir.
Distintos : atributos
            algoritmos
            hiperparametros

separar un porcentaje de datos para validar un modelo
entrenamos nuestro modelo con ALGUNOS de nuestros datos y vemos como funcionan estos datos
-----
Una parte de los datos no se toca. lo guardas para el Held out.
lo demas haces el ciclo de validacion cruzada. Lo que entrenas. Desarrollo.
Se evalua el modelo obtenido con el conjunto Held out.

"""

#%%

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold
from sklearn import tree
from sklearn.metrics import accuracy_score
#%%

#%%
carpeta = "~/Descargas/Archivos - Clase 18-20250225/"
df = pd.read_csv(carpeta + 'seleccion_modelos.csv')
X = df.drop("Y", axis = 1)
y  = df.Y

X_dev, X_eval, y_dev, y_eval = train_test_split(X,y,random_state=1, test_size=0.1)

alturas = [1,2,3,5,8,13,21]
nsplits = 10
kf = KFold(n_splits= nsplits)

resultados = np.zeros((nsplits,len(alturas)))

#%%

for i, (train_index, test_index) in enumerate(kf.split(X_dev)):

    kf_X_train, kf_X_test = X_dev.iloc[train_index], X_dev.iloc[test_index]
    kf_y_train, kf_y_test = y_dev.iloc[train_index], y_dev.iloc[test_index]
    
    for j, hmax in enumerate(alturas):
        
        arbol = tree.DecisionTreeClassifier(max_depth = hmax)
        arbol.fit(kf_X_train, kf_y_train)
        pred = arbol.predict(kf_X_test)
        score = accuracy_score(kf_y_test,pred)
        
        resultados[i, j] = score

#%% promedio scores sobre los folds
scores_promedio = resultados.mean(axis = 0)


#%% 
for i,e in enumerate(alturas):
    print(f'Score promedio del modelo con hmax = {e}: {scores_promedio[i]:.4f}')

arbol_elegido = tree.DecisionTreeClassifier(max_depth = 1)
arbol_elegido.fit(X_dev, y_dev)
y_pred = arbol_elegido.predict(X_dev)

score_arbol_elegido_dev = accuracy_score(y_dev, y_pred)
print(score_arbol_elegido_dev)

#%% pruebo el modelo elegid y entrenado en el conjunto eval
y_pred_eval = arbol_elegido.predict(X_eval)       
score_arbol_elegido_eval = accuracy_score(y_eval, y_pred_eval)
print(score_arbol_elegido_eval)

#%%

X = autos[['weigth_normalizado', 'acceleration_normalizado']]
Y = autos[['mpg']]

X_dev, X_eval, y_dev, y_eval = train_test_split(X,Y,random_state=1, test_size=0.1)


nsplits = 10
kf = KFold(n_splits= nsplits)
vecinos = range(1,50)
resultados = np.zeros((nsplits, len(vecinos)))

#%%
for j ,(train_index, test_index) in enumerate(kf.split(X_dev)): 

    X_train, X_test = X_dev.iloc[train_index], X_dev.iloc[test_index]
    y_train, y_test = y_dev.iloc[train_index], y_dev.iloc[test_index]
    
    for i, k in enumerate(vecinos):
        neigh = KNeighborsRegressor(n_neighbors= k)
        neigh.fit(X_train, y_train)
        Y_pred = neigh.predict(X_test)
        error = mean_squared_error(y_test, Y_pred)
        resultados[j, i] = error
print(resultados)
#%%
scores_promedio = resultados.mean(axis = 0)
print(scores_promedio)

#%% 
for i,e in enumerate(vecinos):
    print(f'Score promedio del modelo con hmax = {e}: {scores_promedio[i]:.4f}')
#%%
