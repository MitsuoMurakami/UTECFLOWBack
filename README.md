# UTECFLOWBack

## Rutas

### Preguntas

- Crear una pregunta: https://4cko1or492.execute-api.us-east-1.amazonaws.com/test/preguntas/crearPregunta
    - POST: crea una pregunta. Se le manda un json con la siguiente forma:
        ```json
            {
            "texto": "Ayuda no se ingle",
            "archivo": "None",
            "titulo": "Tutorial de ingles plis",
            "usuario_gmail": "romina.romani@utec.edu.pe",
            "curso": "Ingles",
            "respondido": false,
            "tags": [
                "Ingle"
                ]
            }
        ```
        Recibes:
        ```json
        {
            "statusCode": 200,
            "body": "{\"22\": {\"id\": 22, \"likes\": 0, \"texto\": \"hola\", \"archivo\": null, \"usuario_gmail\": \"yared.riveros@utec.edu.pe\", \"titulo\": \"otro\", \"curso\": \"ADA\", \"respondido\": false}}"
        }

- Leer todas las preguntas: https://4cko1or492.execute-api.us-east-1.amazonaws.com/test/preguntas/leerPreguntas
    - GET
    Recibes:
    ```json
    {
    "statusCode": 200,
    "body": [
        {
            "id": 21,
            "titulo": "Test postman3",
            "curso": "Test2",
            "respondido": false,
            "likes": 0,
            "texto": "hola",
            "archivo": null,
            "usuario_gmail": "sofiyin@patata.edu.pe"
        },
        {
            "id": 22,
            "titulo": "otro",
            "curso": "ADA",
            "respondido": false,
            "likes": 0,
            "texto": "hola",
            "archivo": null,
            "usuario_gmail": "yared.riveros@utec.edu.pe"
        }
    ]
}
    ```

- Leer todas las preguntas de un usuario en específico: https://4cko1or492.execute-api.us-east-1.amazonaws.com/test/preguntas/leerPreguntas
    - POST
    Envías:
    ```json
    {
        "usuario_gmail": "yared.riveros@utec.edu.pe"
    }
    ```
    Recibes:
    ```json
    {
    "statusCode": 200,
    "body": [
        {
            "id": 22,
            "likes": 0,
            "texto": "hola",
            "archivo": null,
            "usuario_gmail": "yared.riveros@utec.edu.pe",
            "titulo": "otro",
            "curso": "ADA",
            "respondido": false
        }
    ]
}
    ```

### Respuestas

- https://4cko1or492.execute-api.us-east-1.amazonaws.com/test/respuestas
    - POST: crea una respuesta.
    Envías:
    ```json
    {
    "id_pregunta": 23,
    "texto": "Pruebe Duolingo mi estimada",
    "archivo": "None",
    "usuario_gmail": "virginia@queso.edu.pe"
    }
    ```
    Recibes:
    ```json
    {
        "statusCode": 200,
        "body": "\"Respuesta creada exitosamente.\""
    }
    ```

### Usuarios

- https://4cko1or492.execute-api.us-east-1.amazonaws.com/test/usuarios
    - POST: crea un usuario.
    Envías:
    ```json
    {
    "username": "admin",
    "usuario_gmail": "admin@utec.edu.pe",
    "carrera": "cs",
    "ciclo": 10,
    "password": "nose"
    }
    ```
    Recibes:
    ```json
    {
        "statusCode": 200,
        "body": "\"Usuario creado exitosamente.\""
    }
    ```

### Tags

- listas todos los tags: https://4cko1or492.execute-api.us-east-1.amazonaws.com/test/tags
    - GET.
    Recibes:
    ```json
    {
    "statusCode": 200,
    "body": [
        {
            "id": 1,
            "nombre": "ADA",
            "descripcion": "Se enseña a analizar y diseñar algoritmos, y mejoramiento de su complejidad"
        },
        {
            "id": 2,
            "nombre": "TEO",
            "descripcion": "Se enseñan los principios de la computacion como automatas"
        }
    ]
    ```
