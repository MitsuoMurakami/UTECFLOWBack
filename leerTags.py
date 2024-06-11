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
    
    # Ejecutar la consulta para obtener todos los registros de la tabla "tags"
    cursor.execute("SELECT * FROM tags;")
    tags = cursor.fetchall()
    
    # Obtener los nombres de las columnas
    colnames = [desc[0] for desc in cursor.description]
    
    # Cerrar la conexión
    cursor.close()
    conn.close()
    
    # Convertir cada fila a un diccionario y agregarlo a la lista "tags_json"
    tags_json = [dict(zip(colnames, tag)) for tag in tags]
    
    # Generar un diccionario donde cada id de pregunta es la clave y el valor es el diccionario de la pregunta
    tags_dict = {tag['id']: tag for tag in tags_json}
    
    # Devolver los resultados en formato JSON
    return {
        'statusCode': 200,
        'body': json.dumps(tags_dict)
    }
