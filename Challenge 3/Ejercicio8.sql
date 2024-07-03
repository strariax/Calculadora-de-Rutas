--Muestra las 10 publicaciones m�s populares basadas en la puntuaci�n (Score) de la tabla Posts. 
--Ordena las publicaciones por puntuaci�n de forma descendente y selecciona solo las 10 primeras. Presenta los resultados en una tabla mostrando el Title
--de la publicaci�n y su puntuaci�n 

SELECT TOP (10) Title, Score

FROM Posts

WHERE Title IS NOT NULL

ORDER BY Score DESC
