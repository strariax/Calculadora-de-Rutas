/* Actualiza la columna Location de la tabla Users cambiando todas las ubicaciones vac�as por "Desconocido".
Utiliza una consulta de actualizaci�n para cambiar las ubicaciones vac�as. Muestra un mensaje indicando que la actualizaci�n se realiz� correctamente. */

UPDATE Users SET Location = 'Desconocido' WHERE Location IS NULL OR Location = ''

print('La actualizacion se realiz� correctamente')
