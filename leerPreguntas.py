import json
import psycopg2

def lambda_handler(event, context):
    conn = psycopg2.connect(
        dbname='UTECFlow_DB',
        user='postgres',
        password='M0duVxeLuqO5oymKPtxj',
        host='utecflowdb.cqvghkgnty5p.us-east-1.rds.amazonaws.com',
        port='5432'
    )

    # Traer todas las preguntas ordenadas por número de likes
    cursor = conn.cursor()
    cursor.execute("SELECT preguntas.id, titulo, curso, respondido, likes, texto,archivo, usuario_gmail  FROM preguntas JOIN post ON preguntas.id=post.id ORDER BY likes DESC;")
    #cursor.execute("SELECT * FROM preguntas ORDER BY likes DESC;")
    preguntas = cursor.fetchall()
    conn.close()

    # Convertir cada pregunta a un diccionario y agregarlo a la lista "preguntas_json"
    preguntas_json = []
    for pregunta in preguntas:
        preguntas_json.append({
            'id': pregunta[0],
            'titulo': pregunta[1],
            'curso': pregunta[2],
            'respondido': pregunta[3],
            'likes': pregunta[4],
            'texto': pregunta[5],
            'archivo': pregunta[6],
            'usuario_gmail': pregunta[7]
        })

    # Generar un diccionario donde cada id de pregunta es la clave y el valor es el diccionario de la pregunta
    preguntas_dict = {pregunta['id']: pregunta for pregunta in preguntas_json}

    return {
        'statusCode': 200,
        'body': json.dumps(preguntas_dict)
    }
