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
        "body": "{\"21\": {\"id\": 21, \"titulo\": \"Test postman3\", \"curso\": \"Test2\", \"respondido\": false, \"likes\": 0, \"texto\": \"hola\", \"archivo\": null, \"usuario_gmail\": \"sofiyin@patata.edu.pe\"}, \"22\": {\"id\": 22, \"titulo\": \"otro\", \"curso\": \"ADA\", \"respondido\": false, \"likes\": 0, \"texto\": \"hola\", \"archivo\": null, \"usuario_gmail\": \"yared.riveros@utec.edu.pe\"}, \"23\": {\"id\": 23, \"titulo\": \"Tutorial de ingles plis\", \"curso\": \"Ingles\", \"respondido\": false, \"likes\": 0, \"texto\": \"Ayuda no se ingle\", \"archivo\": null, \"usuario_gmail\": \"romina.romani@utec.edu.pe\"}}"
    }

- Leer todas las preguntas de un usuario en específico: https://4cko1or492.execute-api.us-east-1.amazonaws.com/test/preguntas/leerPreguntas
    - POST
    Envías:
    ```json
    {
        "usuario_gmail": "yared.riveros@utec.edu.pe"
    }
    Recibes:
    ```json
    {
        "statusCode": 200,
        "body": "{\"22\": {\"id\": 22, \"likes\": 0, \"texto\": \"hola\", \"archivo\": null, \"usuario_gmail\": \"yared.riveros@utec.edu.pe\", \"titulo\": \"otro\", \"curso\": \"ADA\", \"respondido\": false}}"
    }

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
    Recibes:
    {
        "statusCode": 200,
        "body": "\"Respuesta creada exitosamente.\""
    }

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
    Recibes:
    ```json
    {
        "statusCode": 200,
        "body": "\"Usuario creado exitosamente.\""
    }

### Tags

- listas todos los tags: https://4cko1or492.execute-api.us-east-1.amazonaws.com/test/tags
    - GET.
    Recibes:
    ```json
    {
        "statusCode": 200,
        "body": "{\"1\": {\"id\": 1, \"nombre\": \"ADA\", \"descripcion\": \"Se ense\ña a analizar y dise\ñar algoritmos, y mejoramiento de su complejidad\"}, \"2\": {\"id\": 2, \"nombre\": \"TEO\", \"descripcion\": \"Se ense\ñan los principios de la computacion como automatas\"}, \"3\": {\"id\": 3, \"nombre\": \"AED\", \"descripcion\": \"Se ense\ñan los tipos de estructuras de datos y su funcionamiento\"}, \"4\": {\"id\": 4, \"nombre\": \"Arquitectura\", \"descripcion\": \"Se ense\ña a dise\ñar componentes de un microprocesador\"}, \"5\": {\"id\": 5, \"nombre\": \"Progra 1\", \"descripcion\": \"Se ense\ña a programar en python\"}, \"6\": {\"id\": 6, \"nombre\": \"Progra 2\", \"descripcion\": \"Se ense\ña a programar C++\"}, \"7\": {\"id\": 7, \"nombre\": \"Intro a Computacion cuantica\", \"descripcion\": \"Se ense\ñan los principios de la cuantica\"}, \"8\": {\"id\": 8, \"nombre\": \"Ing. Software\", \"descripcion\": \"Se ense\ña como planear un proyecto, su ejecucion y su mantenimiento\"}, \"9\": {\"id\": 9, \"nombre\": \"Machine learning\", \"descripcion\": \"Se ense\ña cual es el funcionamiento y presicion de los modelos existentes\"}, \"10\": {\"id\": 10, \"nombre\": \"DBP\", \"descripcion\": \"Se ense\ña a dise\ñar y crear paginas web y aplicaciones mobiles, y subirlo a la nube para su ejecucion\"}, \"11\": {\"id\": 11, \"nombre\": \"Test\", \"descripcion\": null}, \"12\": {\"id\": 12, \"nombre\": \"Ingle\", \"descripcion\": null}}"
    }