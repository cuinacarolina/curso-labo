# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:26:56 2025

@author: cuina

"""
#%%
import pandas as pd
import duckdb as dd

"""
Ejercicio 7
Tomar el dataset corregido de Dengue DatosDengueYZikaCorregida.csv (del campus virtual) 
y listar los nombres de departamento y sus ids, nombres provincia e id provincia para todos aquellos 
departamentos con mismo nombre, pero distinto id de departamento y distinto id de provincia. 
Ordenarlos por nombre de departamento.
"""
carpeta = "C:/Users/cuina/OneDrive/Escritorio/cursoLaboDatos/Calidad de datos/"
data = pd.read_csv(carpeta+"DatosDengueYZikaCorregida.csv")

res = dd.sql(
    """
    SELECT DISTINCT departamento_nombre, departamento_id, provincia_id, provincia_nombre
    FROM data
    ORDER BY departamento_nombre, departamento_id
    """).df()