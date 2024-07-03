/* Encuentra el DisplayName de los usuarios que han realizado más de 100 comentarios en total.
Para esto utiliza una subconsulta para calcular el total de comentarios por usuario y luego filtra aquellos usuarios que hayan realizado más de 100 comentarios 
en total. Presenta los resultados en una tabla mostrando el DisplayName de los usuarios */


SELECT u.DisplayName FROM Users u

WHERE u.Id IN (SELECT c.UserId FROM Comments c

GROUP BY c.UserId HAVING COUNT(c.UserId) > 100);