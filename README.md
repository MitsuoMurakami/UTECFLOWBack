# UTECFLOWBack

## Rutas

- https://4cko1or492.execute-api.us-east-1.amazonaws.com/test/preguntas
    - POST: crea una pregunta. Se le manda un json con la siguiente forma:
        ```json
            {
            "texto": "Ayuda gentita :( es mi tricaaa",
            "archivo": "None",
            "titulo": "Pruebe por inducción que sqrt(n) = O(n)",
            "usuario_gmail": "yared.riveros@utec.edu.pe",
            "curso": "Calculo 1",
            "respondido": false,
            "tags": [
                "ADA"
            ]
            }
- https://4cko1or492.execute-api.us-east-1.amazonaws.com/test/respuestas
    - POST: crea una respuesta. Se le manda un json de la siguiente forma:
        ```json
        {
        "id_pregunta": 15,
        "texto": "Prueba: 0<=sqrt(n)<=1*n. :D",
        "archivo": "None",
        "usuario_gmail": "mitsuo.murakami@utec.edu.pe"
        }
- https://4cko1or492.execute-api.us-east-1.amazonaws.com/test/usuarios
    - POST: crea un usuario. Se le manda un json con la siguiente forma:
        ```json
        {
        "username": "sofia",
        "usuario_gmail": "sofiyin@patata.edu.pe",
        "carrera": "cs",
        "ciclo": 1,
        "password": "dasdas"
        }