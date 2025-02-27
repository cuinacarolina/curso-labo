#Descripcion

"""
Materia: Laboratorio de datos - FCEyN - UBA
Nombre del Grupo: Seguidores de Navathe
Autores  : Francisco Peix, Kamala Jimeno Leiton, Carolina Cuiña
Descripción: Código utilizado para trabajar con las fuentes de datos brindadas
Objetivo: 
"""

# %% Imports


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import tree
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn import metrics
from sklearn.metrics import accuracy_score

# %%Carga de datos

#carpeta = '~/Downloads/TP02-seguidoresdenavathe/'
carpeta = '~/Descargas/Archivos TP-02-20250227/'
mnistc = pd.read_csv(carpeta + 'mnist_c_fog_tp.csv', index_col=0)

#Hay 786 columnas incluyendo el indice, sino hay 785 columnas.
#Cada columna posee como nombre a el numero respectivo a la posicion en la que se encuentra (asumiendo que primer columna posee el valor 0) con excepcion de la ultima, cuyo nombre es 'labels' 

# %% Funciones propias definidas

# %% Codigo fuera de funciones


numero_0 = mnistc[mnistc['labels'] == 0]
numero_1 = mnistc[mnistc['labels'] == 1]
numero_2 = mnistc[mnistc['labels'] == 2]
numero_3 = mnistc[mnistc['labels'] == 3]
numero_4 = mnistc[mnistc['labels'] == 4]
numero_5 = mnistc[mnistc['labels'] == 5]
numero_6 = mnistc[mnistc['labels'] == 6]
numero_7 = mnistc[mnistc['labels'] == 7]
numero_8 = mnistc[mnistc['labels'] == 8]
numero_9 = mnistc[mnistc['labels'] == 9]


#%%
import numpy as np
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_openml

# Cargar el conjunto de datos MNIST
# Aquí utilizamos MNIST de OpenML como ejemplo. Puedes usar MNIST-C1 "Fog" de la misma manera.

X, y = mnistc.drop(['labels'], axis = 1), mnistc['labels']

# Filtramos solo los dígitos 0 a 9
# Si tienes MNIST-C1 "Fog", reemplaza 'X' y 'y' con tus datos preprocesados de "Fog"
X = X.values
y = y.values

# Normalizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicar k-NN para encontrar las imágenes más cercanas
k = 3 
knn = NearestNeighbors(n_neighbors=k, metric='euclidean')  # Usamos distancia Euclidiana
knn.fit(X_scaled)

# Elegir una imagen aleatoria de cada dígito para compararla con las imágenes de otros dígitos
indices_por_digito = {digit: np.where(y == digit)[0] for digit in range(10)}

# Función para mostrar una imagen de 28x28
def mostrar_imagen(imagen, titulo):
    imagen_2d = imagen.reshape(28, 28)  # Convertir el vector a una imagen 28x28
    plt.imshow(imagen_2d, cmap='gray')
    plt.title(titulo)
    plt.axis('off')

# Vamos a comparar una imagen aleatoria de cada dígito con las imágenes más cercanas de otros dígitos
plt.figure(figsize=(12, 12))

for digit in range(10):
    # Seleccionar una imagen aleatoria del dígito
    indice_imagen = np.random.choice(indices_por_digito[digit])
    imagen_referencia = X_scaled[indice_imagen]

    # Encontrar los k vecinos más cercanos
    distancias, indices = knn.kneighbors([imagen_referencia])

    # Mostrar la imagen de referencia y sus imágenes más cercanas
    plt.subplot(10, k + 1, digit * (k + 1) + 1)
    mostrar_imagen(X[indice_imagen], f'Dígito {digit}')

    for i, indice in enumerate(indices[0]):
        plt.subplot(10, k + 1, digit * (k + 1) + 2 + i)
        mostrar_imagen(X[indice], f'Distancia {distancias[0][i]:.2f}')

plt.show()


