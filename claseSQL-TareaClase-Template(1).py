# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase SQL. Script clase. 
Autor  : Pablo Turjanski
Fecha  : 2025-02-03
"""

# Importamos bibliotecas
import pandas as pd
import duckdb as dd


#%%===========================================================================
# Importamos los datasets que vamos a utilizar en este programa
#=============================================================================

carpeta = "/home/Estudiante/Escritorio/carpeta/"

# Ejercicios AR-PROJECT, SELECT, RENAME
empleado       = pd.read_csv(carpeta+"empleado.csv")
# Ejercicios AR-UNION, INTERSECTION, MINUS
alumnosBD      = pd.read_csv(carpeta+"alumnosBD.csv")
alumnosTLeng   = pd.read_csv(carpeta+"alumnosTLeng.csv")
# Ejercicios AR-CROSSJOIN
persona        = pd.read_csv(carpeta+"persona.csv")
nacionalidades = pd.read_csv(carpeta+"nacionalidades.csv")
# Ejercicios ¿Mismos Nombres?
se_inscribe_en=pd.read_csv(carpeta+"se_inscribe_en.csv")
materia       =pd.read_csv(carpeta+"materia.csv")
# Ejercicio JOIN múltiples tablas
vuelo      = pd.read_csv(carpeta+"vuelo.csv")    
aeropuerto = pd.read_csv(carpeta+"aeropuerto.csv")    
pasajero   = pd.read_csv(carpeta+"pasajero.csv")    
reserva    = pd.read_csv(carpeta+"reserva.csv")    
# Ejercicio JOIN tuplas espúreas
empleadoRol= pd.read_csv(carpeta+"empleadoRol.csv")    
rolProyecto= pd.read_csv(carpeta+"rolProyecto.csv")    
# Ejercicios funciones de agregación, LIKE, Elección, Subqueries 
# y variables de Python
examen     = pd.read_csv(carpeta+"examen.csv")
# Ejercicios de manejo de valores NULL
examen03 = pd.read_csv(carpeta+"examen03.csv")



#%%===========================================================================
# Ejemplo inicial
#=============================================================================
consultaSQL = """
               SELECT DISTINCT DNI, Salario
               FROM empleado;
              """

dataframeResultado = dd.sql(consultaSQL).df()

print(empleado)

consultaSQL = """
               SELECT DISTINCT DNI, Salario
               FROM empleado;
              """

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)


#%%===========================================================================
# Ejercicios AR-PROJECT <-> SELECT
#=============================================================================
# a.- Listar DNI y Salario de empleados 
consultaSQL = """
                SELECT DISTINCT DNI, Salario
                FROM empleado;
              """

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

#%%-----------
# b.- Listar Sexo de empleados 
consultaSQL = """
                SELECT DISTINCT SEXO FROM empleado
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%-----------
#c.- Listar Sexo de empleados (sin DISTINCT)
consultaSQL = """
                SELECT SEXO FROM empleado

              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)


#%%===========================================================================
# Ejercicios AR-SELECT <-> WHERE
#=============================================================================
# a.- Listar de EMPLEADO sólo aquellos cuyo sexo es femenino
consultaSQL = """
                SELECT DISTINCT DNI, NOMBRE, SEXO, SALARIO FROM empleado
                WHERE SEXO = 'F'
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
#b.- Listar de EMPLEADO aquellos cuyo sexo es femenino y su salario es mayor a $15.000
consultaSQL = """
                SELECT DISTINCT DNI, NOMBRE, SEXO, SALARIO FROM empleado
                WHERE SEXO = 'F' AND SALARIO>'15000'
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%===========================================================================
# Ejercicios AR-RENAME <-> AS
#=============================================================================
#a.- Listar DNI y Salario de EMPLEADO, y renombrarlos como id e Ingreso
consultaSQL = """
                SELECT DISTINCT DNI AS id, SALARIO AS Ingreso FROM empleado
            
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 01
#=============================================================================
# Ejercicio 01.1.- Retornar Codigo y Nombre de los aeropuertos de Londres
consultaSQL = """
                 SELECT DISTINCT Codigo, Nombre FROM aeropuerto
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# Ejercicio 01.2.- ¿Qué retorna 
#                       SELECT DISTINCT Ciudad AS City 
#                       FROM aeropuerto 
#                       WHERE Codigo='ORY' OR Codigo='CDG'; ?
consultaSQL = """
                        SELECT DISTINCT Ciudad AS City 
                       FROM aeropuerto 
                       WHERE Codigo='ORY' OR Codigo='CDG'
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# Ejercicio 01.3.- Obtener los números de vuelo que van desde CDG hacia LHR
consultaSQL = """
                    SELECT DISTINCT numero FROM vuelo
                    WHERE Origen = 'CDG' AND Destino = 'LHR'
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# Ejercicio 01.4.- Obtener los números de vuelo que van desde CDG hacia LHR o viceversa
consultaSQL = """
                    SELECT DISTINCT numero FROM vuelo
                    WHERE (Origen = 'CDG' AND Destino = 'LHR')
                    OR (Origen = 'LHR' AND Destino = 'CDG')
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# Ejercicio 01.5.- Devolver las fechas de reservas cuyos precios son mayores a $200
consultaSQL = """
                SELECT DISTINCT fecha FROM reserva
                WHERE precio>'200'
                    
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
#=============================================================================
# Ejercicios AR-UNION, INTERSECTION, MINUS <-> UNION, INTERSECTION, EXCEPT
#=============================================================================
# a1.- Listar a los alumnos que cursan BDs o TLENG

consultaSQL = """
                    SELECT DISTINCT *
                    FROM alumnosBD
                UNION
                    SELECT DISTINCT *
                    FROM alumnosTLeng
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%% -----------
# a2.- Listar a los alumnos que cursan BDs o TLENG (usando UNION ALL)

consultaSQL = """
                      SELECT DISTINCT *
                      FROM alumnosBD
                  UNION ALL
                      SELECT DISTINCT *
                      FROM alumnosTLeng

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# b.- Listar a los alumnos que cursan simultáneamente BDs y TLENG

consultaSQL = """
                    SELECT DISTINCT *
                    FROM alumnosBD
                INTERSECT
                    SELECT DISTINCT *
                    FROM alumnosTLeng

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# c.- Listar a los alumnos que cursan BDs y no cursan TLENG 

consultaSQL = """
                SELECT DISTINCT *
                FROM alumnosBD
            EXCEPT
                SELECT DISTINCT *
                FROM alumnosTLeng

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#=============================================================================
#  EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 02
#=============================================================================
# Ejercicio 02.1.- Devolver los números de vuelo que tienen reservas generadas (utilizar intersección)
consultaSQL = """
                    SELECT DISTINCT numero
                    FROM vuelo
                INTERSECT
                    SELECT DISTINCT nrovuelo
                    FROM reserva
                    
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# Ejercicio 02.2.- Devolver los números de vuelo que aún no tienen reservas
consultaSQL = """
                        SELECT DISTINCT numero
                        FROM vuelo
                    EXCEPT
                        SELECT DISTINCT nrovuelo
                        FROM reserva
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# Ejercicio 02.3.- Retornar los códigos de aeropuerto de los que parten o arriban los vuelos
consultaSQL = """
                        SELECT DISTINCT codigo
                        FROM aeropuerto
                    INTERSECT
                        (SELECT DISTINCT origen
                        FROM vuelo
                    UNION
                        SELECT DISTINCT destino
                        FROM vuelo)
              """
              
dataframeResultado = dd.sql(consultaSQL).df()



#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#=============================================================================
# Ejercicios AR-... JOIN <-> ... JOIN
#=============================================================================
# a1.- Listar el producto cartesiano entre las tablas persona y nacionalidades

consultaSQL = """
                SELECT DISTINCT *
                FROM persona
            CROSS JOIN nacionalidades
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# a2.- Listar el producto cartesiano entre las tablas persona y nacionalidades (sin usar CROSS JOIN)

consultaSQL = """
                    SELECT DISTINCT *
                    FROM persona, nacionalidades
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%% --------------------------------------------------------------------------------------------
# Carga los nuevos datos del dataframe persona para los ejercicios de AR-INNER y LEFT OUTER JOIN
# ----------------------------------------------------------------------------------------------
persona        = pd.read_csv(carpeta+"persona_ejemplosJoin.csv")
# ----------------------------------------------------------------------------------------------
# b1.- Vincular las tablas persona y nacionalidades a través de un INNER JOIN

consultaSQL = """
                    SELECT DISTINCT *
                    FROM persona
                INNER JOIN nacionalidades
                ON nacionalidad = IDN

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# b2.- Vincular las tablas persona y nacionalidades (sin usar INNER JOIN)

consultaSQL = """
                    SELECT DISTINCT *
                    FROM persona, nacionalidades
                    WHERE nacionalidad = IDN
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# c.- Vincular las tablas persona y nacionalidades a través de un LEFT OUTER JOIN

consultaSQL = """
                    SELECT DISTINCT *
                    FROM persona
                LEFT OUTER JOIN nacionalidades
                ON nacionalidad = IDN

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%===========================================================================
# Ejercicios SQL - ¿Mismos Nombres?
#=============================================================================
# a.- Vincular las tablas Se_inscribe_en y Materia. Mostrar sólo LU y Nombre de materia

consultaSQL = """
                    SELECT DISTINCT LU, nombre
                    FROM se_inscribe_en 
                    INNER JOIN materia
                    ON materia.codigo_materia = se_inscribe_en.codigo_materia
              """

dataframeResultado = dd.sql(consultaSQL).df()

    
#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 03
#=============================================================================
# Ejercicio 03.1.- Devolver el nombre de la ciudad de partida del vuelo número 165

consultaSQL = """
                    SELECT DISTINCT ciudad 
                    FROM aeropuerto
                    INNER JOIN vuelo
                    ON origen = codigo
                    WHERE numero = 165
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# Ejercicio 03.2.- Retornar el nombre de las personas que realizaron reservas a un valor menor a $200

consultaSQL = """
                SELECT DISTINCT nombre 
                FROM pasajero
                INNER JOIN reserva
                ON reserva.DNI = pasajero.DNI
                WHERE precio<'200'
                
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# Ejercicio 03.3.- Obtener Nombre, Fecha y Destino del Viaje de todos los pasajeros que vuelan desde Madrid

vuelosAMadrid = dd.sql("""
                       SELECT DISTINCT * 
                       FROM vuelo
                       WHERE Origen = 'MAD'
              """).df()

dniPersonasDesdeMadrid = dd.sql("""
                                SELECT DISTINCT *
                                FROM reserva
                                INNER JOIN vuelosAMadrid
                                ON nrovuelo = numero
              """).df()

consultaSQL = """
                SELECT DISTINCT Nombre, Fecha, Destino
                FROM dniPersonasDesdeMadrid AS dp
                INNER JOIN pasajero AS p
                ON dp.dni = p.dni
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    
#%%===========================================================================
# Ejercicios SQL - Join de varias tablas en simultáneo
#=============================================================================
# a.- Vincular las tablas Reserva, Pasajero y Vuelo. Mostrar sólo Fecha de reserva, hora de salida del vuelo y nombre de pasajero.
    
consultaSQL = """
                SELECT DISTINCT fecha, salida, nombre
                FROM reserva AS r,pasajero AS p,vuelo AS v
                WHERE r.dni = p.dni AND r.nrovuelo = v.numero
              """

dataframeResultado = dd.sql(consultaSQL).df()

    
#%%===========================================================================
# Ejercicios SQL - Tuplas espúreas
#=============================================================================
# a.- Vincular (JOIN)  EmpleadoRol y RolProyecto para obtener la tabla original EmpleadoRolProyecto
    
consultaSQL = """
                SELECT DISTINCT er.empleado, er.rol, rp.proyecto
                FROM empleadoRol AS er
                INNER JOIN rolProyecto AS rp
                ON rp.rol = er.rol
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%===========================================================================
# Ejercicios SQL - Funciones de agregación
#=============================================================================
# a.- Usando sólo SELECT contar cuántos exámenes fueron rendidos (en total)
    
consultaSQL = """
                SELECT count(*) AS cantidadExamenes
                FROM examen

              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# b1.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia
    
consultaSQL = """
                SELECT Instancia, count(*) AS Asistieron
                FROM examen
                GROUP BY Instancia
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# b2.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia (ordenado por instancia)
    
consultaSQL = """
                SELECT Instancia, count(*) AS Asistieron
                FROM examen
                GROUP BY Instancia
                ORDER BY Instancia DESC
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# b3.- Ídem ejercicio anterior, pero mostrar sólo las instancias a las que asistieron menos de 4 Estudiantes
    
consultaSQL = """
                SELECT Instancia, count(*) AS Asistieron
                FROM examen
                GROUP BY Instancia
                HAVING Asistieron < 4                
                ORDER BY Instancia 
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# c.- Mostrar el promedio de edad de los estudiantes en cada instancia de examen
    
consultaSQL = """
                SELECT instancia,AVG(edad) AS promedio_edad
                FROM examen
                GROUP BY Instancia
                ORDER BY Instancia
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - LIKE")
#=============================================================================
# a1.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial.
    
consultaSQL = """
                SELECT Instancia,AVG(nota) AS promedio_nota
                FROM examen
                GROUP BY Instancia
                HAVING Instancia = 'Parcial-01' OR Instancia = 'Parcial-02' 
                ORDER BY Instancia

              """
#HAVING Instancia LIKE 'Parcial%'
dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# a2.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial. Esta vez usando LIKE.
    
consultaSQL = """
                     SELECT Instancia,AVG(nota) AS promedio_nota
                     FROM examen
                     GROUP BY Instancia
                     HAVING Instancia LIKE 'Parcial%'
                     ORDER BY Instancia
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Eligiendo
#=============================================================================
# a1.- Listar a cada alumno que rindió el Parcial-01 y decir si aprobó o no (se aprueba con nota >=4).
    
consultaSQL = """
                SELECT nombre, nota, 
                    CASE WHEN nota >= 4 
                        THEN 'aprobó'
                        ELSE 'no aprobó'
                    END AS Estado
                FROM examen
                WHERE Instancia = 'Parcial-01'
                ORDER BY Estado, Nombre
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# a2.- Modificar la consulta anterior para que informe cuántos estudiantes aprobaron/reprobaron en cada instancia.
    
consultaSQL = """
                SELECT Instancia,
                    CASE WHEN nota >= 4 
                        THEN 'aprobó'
                        ELSE 'no aprobó'
                    END AS Estado,
                COUNT(*) AS Cantidad
                FROM examen
                GROUP BY Instancia, Estado
                ORDER BY Instancia, Estado
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Subqueries
#=============================================================================
#a.- Listar los alumnos que en cada instancia obtuvieron una nota mayor al promedio de dicha instancia


consultaSQL = """
                     SELECT e1.Nombre, e1.Instancia, e1.Nota
                     FROM examen as e1
                     WHERE e1.Nota >= (
                         SELECT AVG (e2.Nota)
                         FROM examen AS e2
                         WHERE e2.Instancia = e1.Instancia
                         )
                     ORDER BY Instancia ASC, Nota DESC
              """


dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# b.- Listar los alumnos que en cada instancia obtuvieron la mayor nota de dicha instancia

consultaSQL = """
                SELECT e1.Nombre, e1.Instancia, e1.Nota
                FROM examen as e1
                WHERE e1.Nota >= ALL(
                    SELECT e2.Nota
                    FROM examen AS e2
                    WHERE e2.Instancia = e1.Instancia
                    )
                ORDER BY e1.Instancia ASC, e1.Nombre ASC;
                
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# c.- Listar el nombre, instancia y nota sólo de los estudiantes que no rindieron ningún Recuperatorio

consultaSQL = """
                SELECT e1.Nombre, e1.Instancia, e1.Nota
                FROM examen as e1
                WHERE e1.Nombre NOT IN (
                    SELECT e2.Nombre
                    FROM examen AS e2
                    WHERE e2.Instancia = 'Recuperatorio-01' OR e2.Instancia = 'Recuperatorio-02'
                    )
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Integrando variables de Python
#=============================================================================
# a.- Mostrar Nombre, Instancia y Nota de los alumnos cuya Nota supera el umbral indicado en la variable de Python umbralNota

umbralNota = 7

consultaSQL =  f"""
                SELECT Nombre, Instancia, Nota
                FROM examen
                WHERE Nota > {umbralNota}
        
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Manejo de NULLs
#=============================================================================
# a.- Listar todas las tuplas de Examen03 cuyas Notas son menores a 9

consultaSQL = """
                SELECT DISTINCT *
                FROM examen03
                WHERE Nota < 9
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# b.- Listar todas las tuplas de Examen03 cuyas Notas son mayores o iguales a 9

consultaSQL = """
                SELECT DISTINCT *
                FROM examen03
                WHERE Nota >= 9
              """


dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# c.- Listar el UNION de todas las tuplas de Examen03 cuyas Notas son menores a 9 y las que son mayores o iguales a 9

consultaSQL = """
                    SELECT *
                    FROM examen03
                    WHERE Nota < 9
                    
                    UNION
                    
                    SELECT *
                    FROM examen03
                    WHERE Nota >= 9

              """


dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# d1.- Obtener el promedio de notas

consultaSQL = """
                SELECT AVG(Nota) AS promedio
                FROM examen03
              """


dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# d2.- Obtener el promedio de notas (tomando a NULL==0)

consultaSQL = """
                SELECT AVG(CASE WHEN Nota IS NULL THEN 0 ELSE Nota END) AS promedio
                FROM examen03
              """


dataframeResultado = dd.sql(consultaSQL).df()

#%%===========================================================================
# Ejercicios SQL - Mayúsculas/Minúsculas
#=============================================================================
# a.- Consigna: Transformar todos los caracteres de las descripciones de los roles a mayúscula

consultaSQL = """
                SELECT empleado, UPPER(rol) AS rol
                FROM empleadoRol
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# b.- Consigna: Transformar todos los caracteres de las descripciones de los roles a minúscula

consultaSQL = """
                SELECT empleado, LOWER(rol) AS rol
                FROM empleadoRol
              """

dataframeResultado = dd.sql(consultaSQL).df()




#%%===========================================================================
# Ejercicios SQL - Reemplazos
#=============================================================================
# a.- Consigna: En la descripción de los roles de los empleados reemplazar las ñ por ni

consultaSQL = """
                    SELECT empleado, REPLACE(rol, 'ñ', 'ni') AS rol
                    FROM empleadoRol
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Desafío
#=============================================================================
# a.- Mostrar para cada estudiante las siguientes columnas con sus datos: Nombre, Sexo, Edad, Nota-Parcial-01, Nota-Parcial-02, Recuperatorio-01 y , Recuperatorio-02

# ... Paso 1: Obtenemos los datos de los estudiantes
data_estudiante = dd.sql("""
                                SELECT DISTINCT Nombre, Sexo, Edad
                                FROM examen
                
                            """).df()
parcial_01 = dd.sql("""
                SELECT da.Nombre, da.Sexo, da.Edad, ex.Nota AS Parcial_01
                FROM data_estudiante as da
                LEFT OUTER JOIN examen AS ex
                ON ex.Nombre = da.Nombre AND ex.Instancia = 'Parcial-01' 
                
               
              """).df()
parcial_02 = dd.sql("""
                 
                SELECT p1.*, ex.Nota AS Parcial_02
                FROM parcial_01 as p1
                LEFT OUTER JOIN examen AS ex
                ON p1.Nombre = ex.Nombre AND ex.Instancia = 'Parcial-02' 
               
              """).df()
recuperatorio_01 = dd.sql("""
                
                 SELECT p2.*, ex.Nota AS Recu_01
                 FROM parcial_02 as p2
                 LEFT OUTER JOIN examen AS ex
                 ON p2.Nombre = ex.Nombre AND ex.Instancia = 'Recuperatorio-01' 
               
              """).df()

recuperatorio_02 = dd.sql("""
               SELECT r1.*, ex.Nota AS Recu_02
               FROM recuperatorio_01 as r1
               LEFT OUTER JOIN examen AS ex
               ON r1.Nombre = ex.Nombre AND ex.Instancia = 'Recuperatorio-02'
                 
               
              """).df()
desafio_1 = recuperatorio_02


#%% -----------
# b.- Agregar al ejercicio anterior la columna Estado, que informa si el alumno aprobó la cursada (APROBÓ/NO APROBÓ). Se aprueba con 4.

desafio_2 = dd.sql("""
                 SELECT desafio_1.*, 
                 CASE WHEN 
                     (desafio_1.parcial_01 > 4 OR desafio_1.Recu_01 > 4 ) AND (desafio_1.parcial_02 > 4 OR desafio_1.Recu_02 > 4 )
                THEN 'APROBO'
                ELSE 'NO APROBO'
                END AS Estado
                FROM desafio_1
                
              """).df()





#%% -----------
# c.- Generar la tabla Examen a partir de la tabla obtenida en el desafío anterior.

consultaSQL = """
                SELECT *
              """

desafio_03 = dd.sql(consultaSQL).df()
