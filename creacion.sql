DROP TABLE IF EXISTS usuarios;
CREATE TABLE usuarios(
gmail VARCHAR(100) PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
carrera VARCHAR(100) NOT NULL,
ciclo INT NOT NULL,
contrasenha varchar(100) NOT NULL
);


DROP TABLE IF EXISTS post;
CREATE TABLE post(
id SERIAL PRIMARY KEY,
likes INT NOT NULL,
texto TEXT NOT NULL,
archivo TEXT,
fecha DATE,
usuario_gmail VARCHAR(100) NOT NULL,
FOREIGN KEY(usuario_gmail) REFERENCES usuarios(gmail)
);




DROP TABLE IF EXISTS preguntas;


CREATE TABLE preguntas(
id SERIAL PRIMARY KEY,
titulo TEXT NOT NULL,
curso VARCHAR(50) NOT NULL,
respondido BOOL NOT NULL,
FOREIGN KEY(id) REFERENCES post(id)
);





DROP TABLE IF EXISTS respuestas;
CREATE TABLE respuestas(
id SERIAL PRIMARY KEY,    
correcto BOOL NOT NULL,
post_id INT NOT NULL,
FOREIGN KEY(id) REFERENCES post(id),
FOREIGN KEY(post_id) REFERENCES post(id)
);



DROP TABLE IF EXISTS tags;
CREATE TABLE tags(
id SERIAL PRIMARY KEY,
nombre varchar(100) NOT NULL,
descripcion TEXT
);




DROP TABLE IF EXISTS tageado;
CREATE TABLE tageado(
id_tag SERIAL,
id_pregunta SERIAL,
PRIMARY KEY(id_tag, id_pregunta),
FOREIGN KEY(id_tag) REFERENCES tags(id),
FOREIGN KEY(id_pregunta) REFERENCES preguntas(id)
);

/* queries to test the database:
/*insert an user*/
INSERT INTO usuarios (gmail, nombre, carrera, ciclo, contrasenha) VALUES ('usuario0@gmail.com', 'usuario0', 'CS', 5, '01234');
INSERT INTO usuarios (gmail, nombre, carrera, ciclo, contrasenha) VALUES ('usuario1@gmail.com', 'usuario1', 'CS', 9, 'abcde');

/*insert a question (it requires a post) */
INSERT INTO post VALUES (1,15,'hola','archivo', '2023-06-18','usuario0@gmail.com');
INSERT INTO preguntas VALUES (1,'pregunta0','aed', FALSE);

/*insert an answer (it requires a post) */
INSERT INTO post VALUES (2,0,'abc','archivo_null', '2023-06-21','usuario1@gmail.com');
INSERT INTO respuestas VALUES (2,TRUE,1); /*is the post with id 1 and answers to the post with id 1*/ 
SELECT * FROM post;


/*insert a tag*/
INSERT INTO tags VALUES (1, 'programming', 'is a ...');
SELECT * FROM tags;


/*insert for relation between tags and question*/
INSERT INTO tageado VALUES (1, 1);
SELECT * FROM tageado;
*/


/*
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

*/