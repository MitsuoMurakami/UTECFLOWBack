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

    # Traer todas las respuestas de una pregunta
    cursor = conn.cursor()
    cursor.execute(f"SELECT respuestas.id, texto, post_id, correcto , likes,archivo, usuario_gmail FROM respuestas JOIN post ON respuestas.id=post.id WHERE respuestas.post_id = {event['id_pregunta']};")
    
    respuestas = cursor.fetchall()
    conn.close()

    # Convertir a JSON
    respuestas_json = []
    for respuesta in respuestas:
        respuestas_json.append({
            'id': respuesta[0],
            'texto': respuesta[1],
            'pregunta_id': respuesta[2],
            'correcto': respuesta[3],
            'likes': respuesta[4],
            'archivo': respuesta[5],
            'usuario_gmail': respuesta[6]
        })

    # generar un diccionario donde cada id de respuesta es la clave y el valor es el diccionario de la respuesta
    respuestas_dict = {}
    for respuesta in respuestas_json:
        respuestas_dict[respuesta['id']] = respuesta

    return {
        'statusCode': 200,
        'body': json.dumps(respuestas_dict)
    }