/* Elimina todos los comentarios realizados por usuarios con menos de 100 de reputación.
Utiliza una consulta de eliminación para eliminar todos los comentarios realizados y muestra un mensaje indicando cuántos comentarios fueron eliminados */

DELETE FROM Comments

WHERE UserId IN (SELECT Id FROM Users WHERE Reputation < 100)

print('Fueron eliminados '+ CAST(@@ROWCOUNT AS VARCHAR) +' comentarios')

