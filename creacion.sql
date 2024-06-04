DROP TABLE IF EXISTS usuarios;
CREATE TABLE usuarios(
gmail VARCHAR(100) PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
carrera VARCHAR(100) NOT NULL,
ciclo INT NOT NULL,
contrasenha varchar(100) NOT NULL
);


DROP TABLE IF EXISTS preguntas;

CREATE TABLE preguntas(
id SERIAL PRIMARY KEY,
titulo TEXT NOT NULL,
curso VARCHAR(50) NOT NULL,
respondido BOOL NOT NULL,
likes INT NOT NULL,
texto TEXT NOT NULL,
archivo TEXT,
usuario_gmail VARCHAR(100) NOT NULL
);


DROP TABLE IF EXISTS respuestas;
CREATE TABLE respuestas(
id SERIAL PRIMARY KEY,
correcto BOOL NOT NULL,
likes INT NOT NULL,
texto TEXT NOT NULL,
archivo TEXT,
usuario_gmail VARCHAR(100) NOT NULL,
pregunta_id SERIAL NOT NULL,
FOREIGN KEY(usuario_gmail) REFERENCES usuarios(gmail),
FOREIGN KEY(pregunta_id) REFERENCES preguntas(id)
);

DROP TABLE IF EXISTS tags;
CREATE TABLE tags(
id SERIAL PRIMARY KEY,
nombre varchar(100) NOT NULL
);



DROP TABLE IF EXISTS tageado;
CREATE TABLE tageado(
id_tag SERIAL,
id_pregunta SERIAL,
PRIMARY KEY(id_tag, id_pregunta),
FOREIGN KEY(id_tag) REFERENCES tags(id),
FOREIGN KEY(id_pregunta) REFERENCES preguntas(id)
);