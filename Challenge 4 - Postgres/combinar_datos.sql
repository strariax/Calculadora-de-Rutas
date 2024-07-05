SELECT e.nombre AS Entrenador, p.nombre AS Pokemon, p.tipo, p.habilidad, p.ataque, p.defensa, p.velocidad
FROM entrenador_pokemon ep
JOIN entrenadores e ON ep.entrenador_id = e.id
JOIN pokemones p ON ep.pokemon_id = p.id;
