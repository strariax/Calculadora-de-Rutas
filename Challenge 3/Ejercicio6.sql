/* Elimina todos los comentarios realizados por usuarios con menos de 100 de reputaci�n.
Utiliza una consulta de eliminaci�n para eliminar todos los comentarios realizados y muestra un mensaje indicando cu�ntos comentarios fueron eliminados */

DELETE FROM Comments

WHERE UserId IN (SELECT Id FROM Users WHERE Reputation < 100)

print('Fueron eliminados '+ CAST(@@ROWCOUNT AS VARCHAR) +' comentarios')

