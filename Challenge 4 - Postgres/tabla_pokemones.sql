CREATE TABLE pokemones (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50),
    habilidad VARCHAR(100),
    ataque INT,
    defensa INT,
    velocidad INT
);
