--Muestra los 5 comentarios m�s recientes de la tabla Comments. Ordena los comentarios por fecha de creaci�n de forma descendente 
--y selecciona solo los 5 primeros. Presenta los resultados en una tabla mostrando el Text del comentario y la fecha de creaci�n


SELECT TOP (5) Text, CreationDate

FROM Comments

WHERE Text IS NOT NULL

ORDER BY CreationDate DESC