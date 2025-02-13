#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:05:32 2025

@author: Estudiante
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

carpeta = "/home/Estudiante/Escritorio/carpeta/"
escritorio = "/home/Estudiante/Escritorio/"
data_vino = pd.read_csv(carpeta + 'wine.csv', sep = ";")
cheetahRegion= pd.read_csv(carpeta + 'cheetahRegion.csv')
gaseosas= pd.read_csv(carpeta + 'gaseosas.csv')
ageAtDeath = pd.read_csv(carpeta + 'ageAtDeath.csv')
tips = pd.read_csv(carpeta + 'tips.csv')
ventaCasas = pd.read_csv(carpeta + 'ventaCasas.csv')
#%%


plt.scatter(data = data_vino, x = 'fixed acidity', y = 'citric acid')

fig, ax = plt.subplots()
plt.rcParams['font.family'] = 'sans-serif'
ax.scatter( data = data_vino,
           x = 'fixed acidity',
           y = 'citric acid',
           s = 8,
           color = 'magenta')
    
ax.set_title('Acidez vs contenido de acido citrico') #titulo
ax.set_xlabel('Acidez (g/dm3)', fontsize = 'medium') #nombre eje x
ax.set_ylabel('Contenido de ácido cítrico (g/dm3)')

#%%
data_espacios_verdes = pd.read_csv(escritorio + 'arbolado-en-espacios-verdes.csv')
pd.read_csv(escritorio + 'arbolado-en-espacios-verdes.csv', index_col = 2)

# las 30 especies mas frecuentes 
mas_frec= list(data_espacios_verdes['nombre_com'].value_counts().index)[:30]
filtro = data_espacios_verdes[data_espacios_verdes['nombre_com'].isin(mas_frec)]

plt.scatter( data = filtro,x = 'diametro' ,y = 'altura_tot')

plt.scatter( data = filtro,x = 'long' ,y = 'lat')

#%%
#TERMINAR
colores = dict(zip (['Exótico', 'Nativo/Autóctono', 'No Determinado'] , ['green', 'yellow', 'magenta'] ))
fig, ax = plt.subplots()

for origen in ['Exótico', 'Nativo/Autóctono', 'No Determinado']:
    ax.scatter(data = filtro[filtro['origen'] == origen], x = 'diametro', y = 'altura_tot', c = colores[origen], alpha = 0.5, label = origen)
ax.legend()
ax.grid(True)
ax.set_xlabel('Diámetro de tronco')
ax.set_ylabel('Altura total')    

fig.savefig('scatter_diamalt')
plt.show()    
    
#%%

fig, ax = plt.subplots()
plt.rcParams['font.family'] = 'sans-serif'
tamanoBurbuja = 5 
ax.scatter(data = data_vino, x= 'fixed acidity', y = 'citric acid', s = data_vino['residual sugar']*tamanoBurbuja)

ax.set_title('Relación entre tres variables') #titulo
ax.set_xlabel('Acidez (g/dm3)', fontsize = 'medium') #nombre eje x
ax.set_ylabel('Contenido de ácido cítrico (g/dm3)', fontsize = 'medium')

#%%

fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 9.0
data_vino['type'].value_counts().plot(kind = 'pie',
                                 ax = ax,
                                 autopct = '%1.1f%%', #añadir porcentajes
                                 colors = ['#66b3ff', '#ff9999'], #cambiar colores
                                 startangle = 90, #iniciar en angulo 90
                                 shadow = True, #añadir sombra
                                 explode = (0.1, 0), #separar la primera slice
                                 legend = False
                                 )  #evitar leyenda 
ax.set_ylabel('') #remover el label del eje Y
ax.set_title('Distribución de Tipos de Vino') #añadir un titulo

#%%

fig, ax = plt.subplots()
plt.rcParams['font.family'] = 'sans-serif'
plt.scatter( data = data_vino,x = 'pH' ,y = 'volatile acidity')
ax.set_title('pH and volatile acidity relation') #titulo
ax.set_xlabel('pH', fontsize = 'medium') #nombre eje x
ax.set_ylabel('volatile acidity', fontsize = 'medium')

#%%

fig, ax = plt.subplots()
plt.rcParams['font.family'] = 'sans-serif'

ax.bar(data = cheetahRegion, x = 'Anio', height = 'Ventas')
ax.set_title('Ventas de la compañia Cheetah Sports')
ax.set_xlabel('Año', fontsize = 'medium')
ax.set_ylabel('Ventas (millones de $)', fontsize = 'medium')
ax.set_xlim(0, 11)
ax.set_ylim(0, 250)

ax.set_xticks(range(1,11,1)) #muestra todos los ticks del eje x 
ax.set_yticks([]) #remueve los ticks del eje 
ax.bar_label(ax.containers[0], fontsize = 8) #agrega la etiqueta a la barra


#%%

fig, ax = plt.subplots()
plt.rcParams['font.family'] = 'sans-serif'
cheetahRegion.plot(x = 'Anio',
                   y = ['regionEste', 'regionOeste'],
                   kind = 'bar',
                   label = ['Region Este', 'Region Oeste'],
                   ax = ax)

#%%

fig, ax = plt.subplots()

#Grafica la serie regionEste
ax.bar(cheetahRegion['Anio'], cheetahRegion['regionEste'], label = 'Region Este', color = '#4A4063')

#Grafica la serie regionOeste
ax.bar(cheetahRegion['Anio'], cheetahRegion['regionOeste'], bottom = cheetahRegion['regionEste'], label = 'Region Oeste', color = 'skyblue')

#%%
fig, ax = plt.subplots()
plt.rcParams['font.family'] = 'sans-serif'

ax.plot('Anio', 'Ventas', data = cheetahRegion, marker = 'o')

ax.set_title('Ventas de la compañía Cheetah Sports')
ax.set_xlabel('Año', fontsize = 'medium')
ax.set_ylabel('Ventas (millones de $)', fontsize = 'medium')
ax.set_xlim(0, 12)
ax.set_ylim(0, 250)

#%%

fig, ax = plt.subplots()
plt.rcParams['font.family'] = 'sans-serif'

ax.plot('Anio', 'regionEste', data = cheetahRegion,
        marker = '.' , 
        linestyle = '-' ,
        linewidth = 0.5,
        label = 'Región Este',
        )

ax.plot('Anio', 'regionOeste', data = cheetahRegion,
        marker = '.' , 
        linestyle = '-' ,
        linewidth = 0.5,
        label = 'Región Oeste',
        )
#%%
gaseosas['Compras_gaseosas'].value_counts(normalize = True)

fig, ax = plt.subplots()
ax = gaseosas['Compras_gaseosas'].value_counts(normalize=True).plot.bar(ax=ax)

ax.set_title('Frecuencia Venta de Gaseosas')
ax.set_xlabel('Marcas de gaseosas')
ax.set_yticks([])
ax.bar_label(ax.containers[0], fontsize=8)
ax.tick_params(axis= 'x', labelrotation=0)

#%%

fig, ax= plt.subplots()
sns.histplot(data = ageAtDeath['AgeAtDeath'], bins=17)
#%%

# generar un grafico en funcion del sexo y dia de la semana 

fig, ax= plt.subplots()

sns.histplot(data = tips, x = 'tip', hue = 'sex', palette = 'colorblind')
#%%

#mean promedio
#median mediana
#std desviacion estandar
tips['tip'].mode() #2
tips['tip'].mean() #2.99
tips['tip'].median() #2.9
tips['tip'].describe()

#%%
fig, ax= plt.subplots()

ax.boxplot(ventaCasas['PrecioDeVenta'],showmeans = True)
ax.set_title('Precio de venta de casas')
ax.set_xticks([])
ax.set_ylabel('Precio de venta ($)')
ax.set_ylim(0,500)
#%%

fig, ax= plt.subplots()
tips.boxplot(by = ['sex'], column = ['tip'], ax=ax, grid = False, showmeans = True)

fig.suptitle('')
ax.set_title('Propinas')
ax.set_xlabel('Sexo')
ax.set_ylabel('Valor de Propina ($)')
#%%

ax = sns.boxplot(x = "day",
                 y = "tip",
                 hue = "sex",
                 data = tips,
                 order = ['Thur', 'Fri', 'Sat', 'Sun'],
                 palette= { "Female" : "orange", "Male" : "skyblue"})

ax.set_title('Propinas')
ax.set_xlabel('Día de la Semana')
ax.set_ylabel('Valor de Propina ($)')
ax.set_ylim(0,12)
ax.legend(title = "Sexo")
ax.set_xticklabels(['Jueves', 'Viernes', 'Sábado', 'Domingo'])

#%%
ax = sns.violinplot(x = "sex", y = "tip", data = tips, palette = {"Female": "orange", "Male": "skyblue"})
ax.set_title('Propinas')
ax.set_xlabel('Sexo')
ax.set_ylabel('Valor de Propina ($)')
ax.set_ylim(0,12)
ax.set_xticklabels(['Femenino', 'Masculino'])
#%%