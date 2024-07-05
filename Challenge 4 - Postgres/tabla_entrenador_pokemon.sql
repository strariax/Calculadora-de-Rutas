CREATE TABLE entrenador_pokemon (
    entrenador_id INT,
    pokemon_id INT,
    PRIMARY KEY (entrenador_id, pokemon_id),
    FOREIGN KEY (entrenador_id) REFERENCES entrenadores(id) ON DELETE CASCADE,
    FOREIGN KEY (pokemon_id) REFERENCES pokemones(id) ON DELETE CASCADE
);
