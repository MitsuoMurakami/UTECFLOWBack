import json
import boto3
import psycopg2
from psycopg2 import sql

db_host = "utecflowdb.cqvghkgnty5p.us-east-1.rds.amazonaws.com"
db_port = "5432"
db_name = "UTECFlow_DB"
db_user = "postgres"
db_password = "M0duVxeLuqO5oymKPtxj"

def lambda_handler(event, context):
    conn = None
    cursor = None
    
    try:
        # RDS POSTGRES
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        
        cursor = conn.cursor()

        # Obtener de "event" los datos
        likes = 0
        texto = event['texto']
        archivo = event['archivo'] if event['archivo'] != "None" else None
        U_gmail = event['usuario_gmail']
        titulo = event['titulo']
        curso = event['curso']
        respondido = event['respondido']
        tags = event['tags']

        # Insertar en la tabla "preguntas" los datos obtenidos
        cursor.execute("""
            INSERT INTO preguntas (likes, texto, archivo, usuario_gmail, titulo, curso, respondido) 
            VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id;
        """, (likes, texto, archivo, U_gmail, titulo, curso, respondido))

        pregunta_id = cursor.fetchone()[0]
        conn.commit()

        # Taggear la pregunta
        for tag in tags:
            cursor.execute("SELECT id FROM tags WHERE nombre = %s;", (tag,))
            tag_row = cursor.fetchone()

            if not tag_row:
                cursor.execute("INSERT INTO tags (nombre) VALUES (%s) RETURNING id;", (tag,))
                tag_id = cursor.fetchone()[0]
                conn.commit()
            else:
                tag_id = tag_row[0]

            cursor.execute("INSERT INTO tageado (id_tag, id_pregunta) VALUES (%s, %s);", (tag_id, pregunta_id))
            conn.commit()
        
        # Publicar en Tema_Pregunta: problema, esto notificará a todos los usuarios. Se puede arreglar con SES, pero academy no tiene acceso
        sns_client = boto3.client('sns')
        response_sns = sns_client.publish(
            TopicArn='arn:aws:sns:us-east-1:519224807613:Tema_Pregunta',
            Subject='Recibimos tu pregunta',
            Message=json.dumps('Pronto otros usuarios responderan tu pregunta!')
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Pregunta creada exitosamente.')
        }
    
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error creando pregunta.')
        }
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
