/* Para cada usuario, muestra el número total de publicaciones (Posts), comentarios (Comments) y medallas (Badges) que han realizado. 
Utiliza uniones (JOIN) para combinar la información de las tablas Posts, Comments y Badges por usuario. Presenta los resultados en una tabla
mostrando el DisplayName del usuario junto con el total de publicaciones, comentarios y medallas */

--SELECT TOP (10)
--    u.DisplayName,
--    COUNT(p.Id) AS TotalPosts,
--    COUNT(c.Id) AS TotalComments,
--    COUNT(b.Id) AS TotalBadges
--FROM 
--    Users u
--LEFT JOIN 
--    Posts p ON u.Id = p.OwnerUserId
--LEFT JOIN 
--    Comments c ON u.Id = c.UserId
--LEFT JOIN 
--    Badges b ON u.Id = b.UserId
--GROUP BY 
--    u.DisplayName;

SELECT 
    u.DisplayName,
    COALESCE(p.TotalPosts, 0) AS TotalPosts,
    COALESCE(c.TotalComments, 0) AS TotalComments,
    COALESCE(b.TotalBadges, 0) AS TotalBadges
FROM 
    Users u
LEFT JOIN 
    (SELECT OwnerUserId, COUNT(*) AS TotalPosts FROM Posts GROUP BY OwnerUserId) p ON u.Id = p.OwnerUserId
LEFT JOIN 
    (SELECT UserId, COUNT(*) AS TotalComments FROM Comments GROUP BY UserId) c ON u.Id = c.UserId
LEFT JOIN 
    (SELECT UserId, COUNT(*) AS TotalBadges FROM Badges GROUP BY UserId) b ON u.Id = b.UserId
ORDER BY 
    TotalPosts DESC, TotalComments DESC, TotalBadges DESC;

