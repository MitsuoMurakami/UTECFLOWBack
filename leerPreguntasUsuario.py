import json
import psycopg2

def lambda_handler(event, context):
    # Conexión a la base de datos
    conn = psycopg2.connect(
        dbname='UTECFlow_DB',
        user='postgres',
        password='M0duVxeLuqO5oymKPtxj',
        host='utecflowdb.cqvghkgnty5p.us-east-1.rds.amazonaws.com',
        port='5432'
    )
    
    # Crear un cursor
    cursor = conn.cursor()
    
    # Obtener el correo del usuario de los parámetros de consulta
    usuario_gmail = event['usuario_gmail']
    
    # Traer las preguntas del usuario ordenadas por número de likes
    cursor.execute("""
        SELECT id, likes, texto, archivo, usuario_gmail, titulo, curso, respondido
        FROM preguntas
        WHERE usuario_gmail = %s
        ORDER BY likes DESC;
    """, (usuario_gmail,))
    
    preguntas = cursor.fetchall()
    
    # Cerrar la conexión
    cursor.close()
    conn.close()
    
    # Convertir cada pregunta a un diccionario y agregarlo a la lista "preguntas_json"
    preguntas_json = []
    for pregunta in preguntas:
        preguntas_json.append({
            'id': pregunta[0],
            'likes': pregunta[1],
            'texto': pregunta[2],
            'archivo': pregunta[3],
            'usuario_gmail': pregunta[4],
            'titulo': pregunta[5],
            'curso': pregunta[6],
            'respondido': pregunta[7]
        })
    
    # Generar un diccionario donde cada id de pregunta es la clave y el valor es el diccionario de la pregunta
    preguntas_dict = {pregunta['id']: pregunta for pregunta in preguntas_json}
    
    # Devolver las preguntas en formato JSON
    return {
        'statusCode': 200,
        'body': json.dumps(preguntas_dict)
    }
