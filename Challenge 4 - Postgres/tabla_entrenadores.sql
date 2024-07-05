CREATE TABLE entrenadores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT,
    ciudad VARCHAR(100)
);