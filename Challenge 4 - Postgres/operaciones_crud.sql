-- Create

INSERT INTO pokemones (nombre, tipo, habilidad, ataque, defensa, velocidad) VALUES 
('Snorlax', 'Normal', 'Sebo', 32, 43, 18);

INSERT INTO entrenadores (nombre, edad, ciudad) VALUES 
('Sabrina', 20, 'Ciudad Azafrán');

-- Read

SELECT * FROM pokemones;

-- Update

UPDATE pokemones SET ataque = 60 WHERE nombre = 'Pikachu';

-- Delete

DELETE FROM pokemones WHERE nombre = 'Charmander';