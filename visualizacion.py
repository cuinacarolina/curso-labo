# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:34:58 2025
Visualización
@author: cuina
"""

import pandas as pd
import duckdb as dd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression

#%%
data_ping = sns.load_dataset('penguins')

#%%
"""
a. ¿Qué representa cada línea del dataframe?
    cada fila es un indiduo de pinguinos.
b. ¿Cuántas muestras hay en total?
    344
c. ¿Cuáles son las especies de pingüinos consideradas?
    Adelie, Chinstrap, Gentoo
d. ¿Cuáles son las islas estudiadas?
    Dream, Torgersen, Biscoe
e. Para cada pingüino, ¿con qué datos contamos?
    especie, isla, longitud del pico, ancho del pico, longitud de la aleta, masa, sexo 
"""
especies = dd.sql(
    """
    SELECT DISTINCT species
    FROM data_ping
    """).df()
    
islas = dd.sql(
    """
    SELECT DISTINCT island
    FROM data_ping
    """).df()    
#%%

"""
3. Averiguar si las islas están pobladas mayormente por alguna especie en particular, o
si éstas coexisten, y en ambos casos deberá notificar en qué proporciones.
Es importante mencionar que deberá reportar sus descubrimientos de manera
resumida a través de gráficos de barra y de torta.
"""
#de barra
fig, ax = plt.subplots()
sns.countplot(data=data_ping, x='island', hue='species', palette='Set2', ax=ax)
ax.set_title('Cantidad de Pingüinos por Especie e Isla')
ax.set_xlabel('Isla')
ax.set_ylabel('cant por especie')
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
ax.bar_label(ax.containers[2])
plt.show()

#de torta
fig, axes = plt.subplots(1, len(islas), figsize=(5 * len(islas), 5))
islas = ['Dream', 'Torgersen', 'Biscoe']
for i, isla in enumerate(islas):
    ax = axes[i]
    data_isla = data_ping[data_ping['island'] == isla]
    especies_por_isla = data_isla['species'].value_counts()
    especies_por_isla.plot(kind='pie', 
                           ax = ax,
                           autopct= '%1.1f%%',
                           colors= ['yellow', 'green', 'red'],
                           shadow = True)
    ax.set_title(f"Especies en {isla}")
    ax.set_ylabel('')
#%%    
"""
4. Realizar un histograma de la variable grosor del pico. Repetir separando por
especies (con el mismo rango de valores en los ejes, para poder comparar).
"""

fig, ax = plt.subplots()
sns.histplot(data = data_ping, x = 'bill_depth_mm', palette = 'colorblind')
ax.set_title('Cantidad de Pingüinos por grosor del pico')
ax.set_xlabel('Grosores del pico en mm')
ax.set_ylabel('cant de pinguinos')
#%%
#separado por especie
fig, ax = plt.subplots()
sns.histplot(data = data_ping, x = 'bill_depth_mm', hue = 'species', palette = 'colorblind')
ax.set_title('Cantidad de Pingüinos por grosor del pico')
ax.set_xlabel('Grosores del pico en mm')
ax.set_ylabel('cant de pinguinos')

#%%

"""
5. Realizar lo mismo con las demás variables corporales de los pingüinos. A partir de
estos gráficos, responder:
a. ¿Se puede determinar la especie de un pingüino a partir de una sola
característica? 
    Yo creo que no porque en todos los graficos se superponen 
b. ¿Hay alguna característica que permita discernir entre especies mejor que
otras? 
    La longitud de la aleta
"""
fig, ax = plt.subplots()
sns.histplot(data = data_ping, x = 'bill_length_mm', hue = 'species', palette = 'colorblind')
ax.set_title('Cantidad de Pingüinos por long del pico')
ax.set_xlabel('Grosores del pico en mm')
ax.set_ylabel('cant de pinguinos')    

fig, ax = plt.subplots()
sns.histplot(data = data_ping, x = 'flipper_length_mm', hue = 'species', palette = 'colorblind')
ax.set_title('Cantidad de Pingüinos por long de aleta')
ax.set_xlabel('Grosores del pico en mm')
ax.set_ylabel('cant de pinguinos')      

fig, ax = plt.subplots()
sns.histplot(data = data_ping, x = 'body_mass_g', hue = 'species', palette = 'colorblind')
ax.set_title('Cantidad de Pingüinos por masa corporal')
ax.set_xlabel('Grosores del pico en mm')
ax.set_ylabel('cant de pinguinos')  

#%%
"""
Realizar ahora histogramas de las variables observadas, separadas por sexo (f/m).
De manera análoga, considerar si hay alguna variable que permita deducir el sexo
de un pingüino. No no hay, aunque las hembras tiene el pico mas corto y menos ancho.
"""

fig, ax = plt.subplots()
sns.histplot(data = data_ping, x = 'bill_depth_mm', hue = 'sex', palette = 'deep', bins = 10 )
ax.set_title('Cantidad de Pingüinos por grosor del pico')
ax.set_xlabel('Grosores del pico en mm')
ax.set_ylabel('cant de pinguinos')

fig, ax = plt.subplots()
sns.histplot(data = data_ping, x = 'bill_length_mm', hue = 'sex', palette = 'deep' , bins = 10)
ax.set_title('Cantidad de Pingüinos por long del pico')
ax.set_xlabel('Grosores del pico en mm')
ax.set_ylabel('cant de pinguinos')    

fig, ax = plt.subplots()
sns.histplot(data = data_ping, x = 'flipper_length_mm', hue = 'sex', palette = 'deep' , bins = 10)
ax.set_title('Cantidad de Pingüinos por long de aleta')
ax.set_xlabel('Grosores del pico en mm')
ax.set_ylabel('cant de pinguinos')      

fig, ax = plt.subplots()
sns.histplot(data = data_ping, x = 'body_mass_g', hue = 'sex', palette = 'deep' , bins = 10)
ax.set_title('Cantidad de Pingüinos por masa corporal')
ax.set_xlabel('Grosores del pico en mm')
ax.set_ylabel('cant de pinguinos')  
#%%
"""
7. Realizar scatterplots de pares de variables corporales, separadas por sexo. A partir
de los gráficos, responder:
a. ¿Hay algún par de variables que permita deducir el sexo?
    TAL VEZ EL DE BODY MASS RESPECT DE BILL DEPTH
b. ¿Y si se fija una especie en particular?

"""
data_ping_clean = dd.sql("""
                         SELECT *
                         FROM data_ping
                         WHERE bill_depth_mm IS NOT NULL AND bill_length_mm IS NOT NULL
                         AND sex IS NOT NULL
                         """
                         ).df()
    
colores = {'Male': 'yellow', 'Female': 'magenta'}
data_ping_clean['color'] = data_ping_clean['sex'].map(colores)
fig, ax = plt.subplots()
ax.scatter(data = data_ping_clean, x = 'bill_depth_mm', y = 'bill_length_mm', c = data_ping_clean['color'])
ax.set_title('ancho respecto de longitud del pico por sexo') 
ax.set_xlabel('Bill Depth (mm)')
ax.set_ylabel('Bill Length (mm)')
 
#%%
#ESTE GRAFICO (ANCHO DEL PICO, MASA CORPORAL) ES EL MAS ACERCADO A QUE SE SEPAREN POR SEXO
fig, ax = plt.subplots()
ax.scatter(data = data_ping_clean, x = 'bill_depth_mm', y = 'body_mass_g', c = data_ping_clean['color'])
ax.set_title('ancho del pico respecto de la masa corporal por sexo') 
ax.set_xlabel('bill depth (mm)')
ax.set_ylabel('body mass  (g)')
#%%
#SEPARO POR ESPECIE

data_Adelie = dd.sql("""
                         SELECT *
                         FROM data_ping_clean
                         WHERE species = 'Adelie'
                         ORDER BY bill_length_mm
                         """
                         ).df()

fig, ax = plt.subplots()
ax.scatter(data = data_Adelie, x = 'bill_depth_mm', y = 'body_mass_g', c = data_Adelie['color'])
ax.set_title('ancho del pico respecto de la masa corporal por sexo') 
ax.set_xlabel('bill depth (mm)')
ax.set_ylabel('body mass  (g)')    

data_Gentoo = dd.sql("""
                         SELECT *
                         FROM data_ping_clean
                         WHERE species = 'Gentoo'
                         """
                         ).df()

fig, ax = plt.subplots()
ax.scatter(data = data_Gentoo, x = 'bill_depth_mm', y = 'body_mass_g', c = data_Gentoo['color'])
ax.set_title('ancho del pico respecto de la masa corporal por sexo') 
ax.set_xlabel('bill depth (mm)')
ax.set_ylabel('body mass  (g)') 
    
data_Chinstrap = dd.sql("""
                         SELECT *
                         FROM data_ping_clean
                         WHERE species = 'Chinstrap'
                         """
                         ).df()

fig, ax = plt.subplots()
ax.scatter(data = data_Chinstrap, x = 'bill_depth_mm', y = 'body_mass_g', c = data_Chinstrap['color'])
ax.set_title('ancho del pico respecto de la masa corporal por sexo') 
ax.set_xlabel('bill depth (mm)')
ax.set_ylabel('body mass  (g)')     

#%%

"""
8. Realizar un scatterplot de las variables largo y grosor del pico agregando colores
para distinguir las especies. Responder:
a. ¿Qué especie muestra mayor dispersión en estas variables?
    Yo creo que Gentoo y Adelie tienen rangos claros de concentracion y Chinstrap no. 
    Pero hay puntos de Adelie muy alejados de la concentración
b. La relación entre estas variables, ¿es similar en las 3 especies?
    No no es similar
"""

colores = dict(zip (['Adelie', 'Chinstrap', 'Gentoo'] , ['green', 'yellow', 'magenta'] ))
fig, ax = plt.subplots()

for especie in ['Adelie', 'Chinstrap', 'Gentoo']:
    ax.scatter(data = data_ping[data_ping['species'] == especie], x = 'bill_depth_mm', y = 'bill_length_mm', c = colores[especie], alpha = 0.5, label = especie)
ax.legend()
ax.grid(True)
ax.set_xlabel('bill_depth_mm')
ax.set_ylabel('bill_length_mm')    

fig.savefig('scatter_diamalt')
plt.show()     
    
#%%
"""
9. Para los pingüinos hembra, a partir de una de sus característica en particular
(obviamente que no sea a partir del campo especie), ¿se puede predecir a qué
especie pertenece? ¿Y combinando más de una característica? 
NO SE PUEDE PREDECIR A PARTIR DE UNA CARACTERISTICA

"""
data_female = dd.sql("""
                     SELECT *
                     FROM data_ping_clean
                     WHERE sex = 'Female'
                     """
                     ).df()
    
colores = dict(zip (['Adelie', 'Chinstrap', 'Gentoo'] , ['green', 'yellow', 'magenta'] ))
fig, ax = plt.subplots()

for especie in ['Adelie', 'Chinstrap', 'Gentoo']:
    ax.scatter(data = data_female[data_female['species'] == especie], x = 'bill_depth_mm', y = 'bill_length_mm', c = colores[especie], alpha = 0.5, label = especie)
ax.legend()
ax.grid(True)
ax.set_xlabel('bill_depth_mm')
ax.set_ylabel('bill_length_mm')    

fig.savefig('scatter_diamalt')
plt.show()    

#%%
# 10. Repetir el punto anterior pero para pingüinos macho.

data_male = dd.sql("""
                     SELECT *
                     FROM data_ping_clean
                     WHERE sex = 'Female'
                     """
                     ).df()
    
colores = dict(zip (['Adelie', 'Chinstrap', 'Gentoo'] , ['green', 'yellow', 'magenta'] ))
fig, ax = plt.subplots()

for especie in ['Adelie', 'Chinstrap', 'Gentoo']:
    ax.scatter(data = data_male[data_male['species'] == especie], x = 'bill_depth_mm', y = 'bill_length_mm', c = colores[especie], alpha = 0.5, label = especie)
ax.legend()
ax.grid(True)
ax.set_xlabel('bill_depth_mm')
ax.set_ylabel('bill_length_mm')    

fig.savefig('scatter_diamalt')
plt.show()       
#%%
colores = dict(zip (['Adelie', 'Chinstrap', 'Gentoo'] , ['green', 'yellow', 'magenta'] ))
fig, ax = plt.subplots()

for especie in ['Adelie', 'Chinstrap', 'Gentoo']:
    ax.scatter(data = data_male[data_male['species'] == especie], x = 'body_mass_g', y = 'bill_length_mm', c = colores[especie], alpha = 0.5, label = especie)
ax.legend()
ax.grid(True)
ax.set_xlabel('bill_depth_mm')
ax.set_ylabel('bill_length_mm')    

fig.savefig('scatter_diamalt')
plt.show()  
#%%
"""
11. Realizar un gráfico (de línea) donde se vea la relación entre la variable largo del pico
y masa corporal, para la especie Adelie. Sugerencia: reordenar el subconjunto de
pingüinos Adelie por la variable largo del pico, y utilizarlo para graficar.
"""

fig, ax = plt.subplots()
ax.plot('bill_length_mm','body_mass_g', data = data_Adelie)
ax.set_title('largo del pico respecto de la masa corporal de Adelie')
ax.set_xlabel('bill_length_mm')
ax.set_ylabel('body_mass_g')

#%%
"""
12. Realizar un gráfico de barras apiladas para visualizar la cantidad de pingüinos de
cada sexo dentro de cada especie.
"""
#CANT DE PINGUINOS DE CADA SEXO DENTRO DE CADA ESPECIE

data_counts = data_ping_clean.groupby(['species', 'sex']).size().unstack()

fig, ax = plt.subplots(figsize=(8, 6))

data_counts['Female'].plot(kind='bar', stacked=True, color="#4A4063", label='Female', ax=ax)
data_counts['Male'].plot(kind='bar', stacked=True, color='skyblue', label='Male', bottom=data_counts['Female'], ax=ax)

plt.xlabel("Especies")
plt.ylabel("Cantidad")
plt.title("Distribución de Machos y Hembras por Especie")
plt.legend(title="Sexo")
plt.xticks(rotation=0)
plt.show()

#%%

#13. Realizar un boxplot de la variable ancho del pico, separado por sexo. ¿Qué se observa?

fig, ax= plt.subplots()

data_ping_clean.boxplot(by = ['sex'], column = ['bill_depth_mm'], ax=ax, grid = False, showmeans = True)

fig.suptitle('')
ax.set_title('Ancho del pico por sexo')
ax.set_xlabel('Sexo')
ax.set_ylabel('Ancho del pico (mm)')

#%%
# 14. Realizar un boxplot de la variable largo de aleta, separado por especie. ¿Qué se observa?

fig, ax= plt.subplots()

data_ping_clean.boxplot(by = ['species'], column = ['flipper_length_mm'], ax=ax, grid = False, showmeans = True)

fig.suptitle('')
ax.set_title('largo de la especie por especie')
ax.set_xlabel('Especies')
ax.set_ylabel('Largo de la aleta (mm)')

#%%
#15. Realizar un violinplot de la variable largo de aleta, separado por sexo.
ax = sns.violinplot(x = "sex", y = "flipper_length_mm", data = data_ping_clean, palette = {"Female": "orange", "Male": "skyblue"})
ax.set_title('largo de la aleta por sexo')
ax.set_xlabel('Sexo')
ax.set_ylabel('largo (mm)')
ax.set_xticklabels(['Femenino', 'Masculino'])

#%%

#16. Realizar un violinplot de la variable masa corporal, separado por especie.
ax = sns.violinplot(x = "species", y = "body_mass_g", data = data_ping_clean, palette = {"Adelie": "orange", "Chinstrap": "skyblue", "Gentoo": "green"})
ax.set_title('masa corporal por especie')
ax.set_xlabel('especies')
ax.set_ylabel('masa (g)')
ax.set_xticklabels(['Adelie', 'Chinstrap', 'Gentoo'])



    