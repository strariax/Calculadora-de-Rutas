--Muestra las 10 publicaciones más populares basadas en la puntuación (Score) de la tabla Posts. 
--Ordena las publicaciones por puntuación de forma descendente y selecciona solo las 10 primeras. Presenta los resultados en una tabla mostrando el Title
--de la publicación y su puntuación 

SELECT TOP (10) Title, Score

FROM Posts

WHERE Title IS NOT NULL

ORDER BY Score DESC
