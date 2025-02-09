# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 18:41:59 2025
GUIA 5 SQL
@author: cuina
"""
import pandas as pd
import duckdb as dd

carpeta = "/users/cuina/Downloads/guia5/"
casos      = pd.read_csv(carpeta+"casos.csv")
departamento      = pd.read_csv(carpeta+"departamento.csv")
grupoetario    = pd.read_csv(carpeta+"grupoetario.csv")
provincia     = pd.read_csv(carpeta+"provincia.csv")
tipoevento      = pd.read_csv(carpeta+"tipoevento.csv")
# Listar sólo los nombres de todos los departamentos que hay en la tabla departamento

ejercicioaa = dd.sql("""
                 SELECT descripcion
                 FROM departamento
            """).df()

#Listar sólo los nombres de todos los departamentos que hay en la tabla departamento (eliminando los registros repetidos)
ejercicioab = dd.sql("""
                 SELECT DISTINCT descripcion
                 FROM departamento
            """).df()
            
#Listar sólo los códigos de departamento y sus nombres, de todos los departamentos que hay en la tabla departamento.
ejercicioac = dd.sql("""
                 SELECT descripcion, id
                 FROM departamento
            """).df()
# Listar todas las columnas de la tabla departamento
ejercicioad = dd.sql("""
                 SELECT *
                 FROM departamento
            """).df()
# Listar los códigos de departamento y nombres de todos los departamentos que hay en la tabla departamento. 
#Utilizar codigo_depto y nombre_depto, 
ejercicioae = dd.sql("""
                 SELECT id AS cpdigo_Depto, descripcion AS nombre_depto
                 FROM departamento
            """).df()

# Listar los registros de la tabla departamento cuyo código de provincia es igual a 54

ejercicioaf = dd.sql("""
                 SELECT *
                 FROM departamento AS d
                 WHERE d.id_provincia = 54
            """).df()

# Listar los registros de la tabla departamento cuyo código de provincia es igual a 22, 78 u 86.

ejercicioag = dd.sql("""
                 SELECT *
                 FROM departamento AS d
                 WHERE d.id_provincia = 22 OR d.id_provincia = 78 OR d.id_provincia = 86
            """).df()

# Listar los registros de la tabla departamento cuyos códigos de provincia se encuentren entre el 50 y el 59 (ambos valores inclusive).

ejercicioah = dd.sql("""
                 SELECT *
                 FROM departamento AS d
                 WHERE d.id_provincia >= 50 AND d.id_provincia <= 59 
            """).df()

#Devolver una lista con los código y nombres de departamentos, asociados al nombre de la provincia al que pertenecen.

ejercicioba = dd.sql("""
                 SELECT d.descripcion, d.id_provincia, p.descripcion
                 FROM departamento AS d
                 INNER JOIN provincia AS p
                 ON d.id_provincia = p.id
            """).df()

# Devolver los casos registrados en la provincia de “Chaco”.

casos_idprovincia = dd.sql("""
                     SELECT c.*, d.id_provincia 
                     FROM casos AS c
                     INNER JOIN departamento AS d
                     ON c.id_depto = d.id
                     """ ).df()
casos_id_descripcion = dd.sql("""
                              SELECT c.*, p.descripcion
                              FROM casos_idprovincia AS c
                              INNER JOIN provincia as p
                              ON c.id_provincia = p.id
                            """).df()
ejerciciobc = dd.sql("""
                     SELECT c.id, c.id_tipoevento, c.anio, c.semana_epidemiologica, c.id_depto, c.id_grupoetario, c.cantidad
                     FROM casos_id_descripcion AS c
                     WHERE c.descripcion = 'Chaco'
                     """ ).df()                 

# Devolver aquellos casos de la provincia de “Buenos Aires” cuyo campo cantidad supere los 10 casos.
ejerciciobd = dd.sql("""
                     SELECT c.id, c.id_tipoevento, c.anio, c.semana_epidemiologica, c.id_depto, c.id_grupoetario, c.cantidad
                     FROM casos_id_descripcion AS c
                     WHERE c.descripcion = 'Buenos Aires' AND c.cantidad > 10
                     """ ).df()   
#VER CA Y CB       
#Devolver un listado con los nombres de los departamentos que no tienen ningun caso asociado
ejercicioca = dd.sql("""
                     SELECT d.descripcion
                     FROM departamento AS d
                FULL    OUTER JOIN casos AS c 
                     ON c.id_depto = d.id
                     WHERE c.id IS NULL;
                     
                   """ ).df()
#Devolver un listado con los tipos de evento que no tienen ningún caso sociado

ejerciciocb = dd.sql("""
                        SELECT e.id
                        FROM tipoevento AS e 
                      FULL  OUTER JOIN  casos AS c 
                        ON e.id = c.id_tipoevento
                        WHERE c.id = NULL
                  """  ).df()
                  
# Calcular la cantidad total de casos que hay en la tabla casos.                
ejercicioda= dd.sql("""
                        SELECT count(*) AS cant_casos
                        FROM casos
                  """  ).df()

# tipo de caso, año y cantidad
# calcular cant total de casos para cada año y tipo de caso
ejerciciodb= dd.sql("""
                        SELECT c.id_tipoevento, c.anio, count(*) AS cantidad
                        FROM casos AS c
                        GROUP BY c.id_tipoevento, c.anio
                        ORDER BY c.id_tipoevento , c.anio ASC
                  """  ).df()

ejerciciodc= dd.sql("""
                        SELECT c.id_tipoevento, count(*) AS cantidad
                        FROM casos AS c
                        WHERE c.anio = 2019
                        GROUP BY c.id_tipoevento
                        ORDER BY c.id_tipoevento 
                        
                  """  ).df()

# Calcular la cantidad total de departamentos que hay por provincia. Presentarla información ordenada por código de provincia.

ejerciciodd= dd.sql("""
                        SELECT d.id_provincia , count(*) AS cantidad
                        FROM departamento AS d
                        GROUP BY d.id_provincia
                       ORDER BY d.id_provincia ASC
                        
                  """  ).df()

ejerciciode = dd.sql("""
                     SELECT c.id_depto
                     FROM casos AS c
                     WHERE c.anio = 2019 AND c.cantidad <= (SELECT MIN(cantidad) FROM casos WHERE c.anio = 2019)
                
    """).df()

ejerciciodf = dd.sql("""
                     SELECT c.id_depto
                     FROM casos AS c
                     WHERE c.anio = 2020 AND c.cantidad >= (SELECT MAX(cantidad) FROM casos WHERE c.anio = 2020)
                
    """).df()
    
# Listar el promedio de cantidad de casos por provincia y año.
# ejercicio D - G

casos_provincia = dd.sql( """
                            SELECT c.*, d.id_provincia
                            FROM casos AS c 
                            INNER JOIN departamento AS d 
                            ON c.id_depto = d.id
                            """   ).df()
ejerciciodg = dd.sql( """
                            SELECT c.id_provincia, c.anio, AVG(c.cantidad) AS promedio
                            FROM casos_provincia AS c 
                            GROUP BY c.id_provincia, c.anio
                            ORDER BY c.id_provincia ASC, c.anio ASC
                            """).df()
# ejercicio D H
ejerciciodh = dd.sql( """
                            SELECT c.id_provincia, c.anio, c.id_depto
                            FROM casos_provincia AS c
                            WHERE c.cantidad = (
                                SELECT MAX(c2.cantidad) 
                                FROM casos_provincia AS c2 
                                WHERE c2.id_provincia = c.id_provincia 
                                AND c2.anio = c.anio
                            )
                            ORDER BY c.id_provincia ASC, c.anio ASC;

                            """).df()

# Mostrar la cantidad de casos total, máxima, mínima y promedio que tuvo la rovincia de Buenos Aires en el año 2019.

ejerciciodi= dd.sql( """  SELECT count(*) AS casos_total, MAX(c.cantidad) AS maxima, MIN(c.cantidad) AS minima, AVG(c.cantidad) AS promedio
                    FROM casos_id_descripcion AS c
                    WHERE c.descripcion = 'Buenos Aires' AND c.anio = 2019
                    """).df()

#ejerciciodj= dd.sql( """  SELECT count(*) AS casos_total, MAX(c.cantidad) AS maxima, MIN(c.cantidad) AS minima, AVG(c.cantidad) AS promedio
#                    FROM casos_id_descripcion AS c
#                    WHERE COUNT(c.cantidad) >= 1000
#                    """).df()
# FALTO EJERCICIO D J
casos_provincia_depto = dd.sql( """  
                            SELECT c.*, d.descripcion AS n_depto
                            FROM casos_id_descripcion AS c 
                            INNER JOIN departamento AS d 
                            ON c.id_depto = d.id 
                            """).df()

ejerciciodk = dd.sql( """  SELECT  n_depto, descripcion AS provincia, AVG(cantidad) AS promedio
                            FROM casos_provincia_depto 
                            WHERE anio = 2019 OR anio = 2020
                            GROUP BY n_depto, anio, descripcion
                            ORDER BY provincia ASC, n_depto ASC
                            """).df()
"""
Devolver una tabla que tenga los siguientes campos: descripción de tipo de
evento, id_depto, nombre de departamento, id_provincia, nombre de
provincia, total de casos 2019, total de casos 2020.
"""
casos_evento = dd.sql ( """ SELECT c.*, e.descripcion AS n_evento
                           FROM casos_provincia_depto AS c
                           INNER JOIN tipoevento AS e
                           ON c.id_tipoevento = e.id
                           """).df()
auxdl1 = dd.sql( """   SELECT n_depto, id_depto, n_depto, id_provincia, descripcion AS n_provincia, count(*) AS casos_2019
                            FROM casos_evento 
                            WHERE anio = 2019
                            GROUP BY n_depto, id_depto, id_provincia, descripcion, anio
                            ORDER BY n_depto ASC, id_provincia ASC, anio ASC 
                            """).df()
auxdl2 = dd.sql( """   SELECT n_depto, id_depto, n_depto, id_provincia, descripcion AS n_provincia, count(*) AS casos_2020
                            FROM casos_evento 
                            WHERE anio = 2020
                            GROUP BY n_depto, id_depto, id_provincia, descripcion, anio
                            ORDER BY n_depto ASC, id_provincia ASC, anio ASC 
                            """).df()
ejerciciodl = dd.sql( """
                     SELECT aux1.*, aux2.casos_2020
                     FROM auxdl1 AS aux1
                     INNER JOIN auxdl2 AS aux2
                     ON aux1.n_depto = aux2.n_depto 
                     """ ).df()
# Devolver el departamento que tuvo la mayor cantidad de casos sin hacer uso de MAX, ORDER BY ni LIMIT.                     
ejercicioea = dd.sql( """
                    SELECT id_depto 
                    FROM casos
                    WHERE cantidad >= ALL (SELECT cantidad
                                           FROM casos)
                    """).df()
# Devolver los tipo de evento que tienen casos asociados. (Utilizando ALL o ANY).

ejercicioeb = dd.sql( """
                    SELECT DISTINCT id_tipoevento
                    FROM casos
                    WHERE id_tipoevento = ANY (SELECT id
                                               FROM tipoevento)
                    """).df()
                                              
# Devolver los tipo de evento que tienen casos asociados (Utilizando IN, NOT IN).
ejerciciofa = dd.sql( """
                     SELECT DISTINCT id_tipoevento
                     FROM casos 
                     WHERE id_tipoevento IN ( SELECT id FROM tipoevento)
    """).df()

#  Devolver los tipo de evento que NO tienen casos asociados (Utilizando IN, NOT IN).

ejerciciofb = dd.sql( """
                     SELECT DISTINCT id
                     FROM tipoevento
                     WHERE id NOT IN ( SELECT id_tipoevento FROM casos)
    """).df()

# Devolver los tipo de evento que tienen casos asociados (Utilizando EXISTS, NOT EXISTS).
ejercicioga = dd.sql( """
                     SELECT DISTINCT id_tipoevento
                     FROM casos 
                     WHERE EXISTS ( SELECT id FROM tipoevento)
    """).df()

#Listar las provincias que tienen una cantidad total de casos mayor al promedio de casos del país. Hacer el listado agrupado por año.
auxha = dd.sql( """
                    SELECT id_provincia, COUNT(*) AS cantidad_anio, anio
                    FROM casos_provincia 
                    GROUP BY id_provincia, anio
                    ORDER BY anio ASC, id_provincia ASC
                    """).df()
promedio_anio = dd.sql( """
                    SELECT AVG(cantidad_anio) AS promedio, anio
                                            FROM auxha
                                            GROUP BY anio
                                            ORDER BY anio ASC
                    """).df()
ejercicioha = dd.sql( """
                    SELECT a.id_provincia, a.cantidad_anio, a.anio
                    FROM auxha AS a 
                    JOIN promedio_anio AS p
                    ON a.anio = p.anio
                    WHERE a.cantidad_anio >= p.promedio
                    GROUP BY a.anio, a.id_provincia, a.cantidad_anio
                    ORDER BY a.anio
                    """).df()


#Por cada año, listar las provincias que tuvieron una cantidad total 
#de casos mayor a la cantidad total de casos que la provincia de Corrientes.
ejerciciohb = dd.sql( """
                    SELECT id_provincia, cantidad_anio, anio
                    FROM auxha 
                    WHERE (cantidad_anio >= (SELECT cantidad_anio FROM (SELECT *
                                            FROM auxha 
                                            WHERE id_provincia = 18))) AND id_provincia != 18
                    GROUP BY anio, id_provincia, cantidad_anio
                    ORDER BY anio ASC, id_provincia ASC 
                    """).df()

ejercicioia = dd.sql( """
                    SELECT id, descripcion
                    FROM departamento
                    ORDER BY descripcion DESC, id ASC
                    """).df()
                
ejercicioib = dd.sql( """
                    SELECT descripcion
                    FROM provincia 
                    WHERE descripcion LIKE 'M%'
                    """).df()
ejercicioic = dd.sql( """
                    SELECT descripcion
                    FROM provincia 
                    WHERE descripcion LIKE 'S___a%'
                    """).df()

ejercicioid = dd.sql( """
                    SELECT descripcion
                    FROM provincia 
                    WHERE descripcion LIKE '%a'
                    """).df()
                    
ejercicioie = dd.sql( """
                    SELECT descripcion
                    FROM provincia 
                    WHERE descripcion LIKE '_____'
                    """).df()
                    
ejercicioif = dd.sql( """
                    SELECT descripcion
                    FROM provincia 
                    WHERE descripcion LIKE '%do%'
                    """).df()

ejercicioig = dd.sql( """
                    SELECT descripcion
                    FROM provincia 
                    WHERE (descripcion LIKE '%do%') AND (id < 30)
                    """).df()                    
ejercicioih = dd.sql( """
                    SELECT id AS codigo_depto, descripcion AS nombre_depto
                    FROM departamento
                    WHERE (descripcion LIKE '%san%') OR (descripcion LIKE '%San%')
                    ORDER BY descripcion DESC
                    """).df()  

ejercicioii = dd.sql( """
                    SELECT c.descripcion AS nom_provincia, c.n_depto AS nom_depto, c.anio, c.semana_epidemiologica, g.descripcion AS grupoetario, c.cantidad
                    FROM casos_provincia_depto AS c
                    JOIN grupoetario AS g
                    ON c.id_grupoetario = g.id
                    WHERE (c.cantidad > 10) AND (c.descripcion LIKE '%a')
                    ORDER BY c.cantidad DESC, c.descripcion ASC, c.n_depto ASC, g.descripcion ASC
                    
                    """).df()  

auxejercicioij = dd.sql( """
                    SELECT c.descripcion AS nom_provincia, c.n_depto AS nom_depto, c.anio, c.semana_epidemiologica, g.descripcion AS grupoetario, c.cantidad
                    FROM casos_provincia_depto AS c
                    JOIN grupoetario AS g
                    ON c.id_grupoetario = g.id
                    WHERE c.descripcion LIKE '%a'
                    ORDER BY c.cantidad DESC, c.descripcion ASC, c.n_depto ASC, g.descripcion ASC
                    
                    """).df()  

ejercicioij = dd.sql(""" 
                     SELECT *
                     FROM auxejercicioij
                     WHERE cantidad = (SELECT MAX(cantidad) FROM auxejercicioij)
                   """ ).df()

#Listar los id y descripción de los departamentos. Estos últimos sin tildes y en orden alfabético.

ejercicioja = dd.sql(""" 
                     SELECT id, 
                     REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(descripcion, 'ó', 'o'), 'á', 'a'), 'é', 'e'), 'í', 'i'), 'ú', 'u') AS descripcion
                     FROM departamento
                     ORDER BY descripcion ASC
                   """ ).df()
#Listar los nombres de provincia en mayúscula, sin tildes y en orden alfabético
ejerciciojb = dd.sql(""" 
                     SELECT id, UPPER(descripcion) AS descripcion
                     FROM ejercicioja
                   """ ).df()
