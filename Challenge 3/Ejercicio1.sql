/* De la Tabla Users selecciona las columnas DisplayName, Age, y Reputation de los usuarios mayores a 30 años, ordenados por reputación de forma descendente,
puedes tomar una cantidad de 200 usuarios para esto.
Debes filtrar los usuarios por edad y muestra solo aquellos mayores de 30 años. Luego, ordena los resultados por reputación de forma descendente.
Presenta los resultados en una tabla mostrando solo las columnas DisplayName, Age, y Reputation */

SELECT DisplayName, Age, Reputation

FROM Users

WHERE Age > 30

ORDER BY Reputation DESC