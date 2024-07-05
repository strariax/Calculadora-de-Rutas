CREATE TABLE batallas (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    entrenador1_id INT,
    entrenador2_id INT,
    pokemon1_id INT,
    pokemon2_id INT,
    resultado VARCHAR(50),
    FOREIGN KEY (entrenador1_id) REFERENCES entrenadores(id) ON DELETE CASCADE,
    FOREIGN KEY (entrenador2_id) REFERENCES entrenadores(id) ON DELETE CASCADE,
    FOREIGN KEY (pokemon1_id) REFERENCES pokemones(id) ON DELETE CASCADE,
    FOREIGN KEY (pokemon2_id) REFERENCES pokemones(id) ON DELETE CASCADE
);