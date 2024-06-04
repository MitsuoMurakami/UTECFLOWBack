import json
import boto3
import psycopg2

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

        # Obtener de "event" el id de la pregunta
        id_pregunta = event['id_pregunta']

        # Obtener de "event" los atributos texto, archivo, U.gmail, pregunta_id
        correcto = False
        likes = 0
        texto = event['texto']
        archivo = event['archivo']
        U_gmail = event['usuario_gmail']
        pregunta_id = id_pregunta

        # Insertar en la tabla "respuestas" los datos obtenidos
        cursor.execute(f"INSERT INTO respuestas (correcto, likes, texto, archivo, usuario_gmail, pregunta_id) VALUES ({correcto}, {likes}, '{texto}', '{archivo}', '{U_gmail}', {pregunta_id});")

        conn.commit()
        
        # Publicar en Tema_Respuesta: problema, esto notificará a todos los usuarios. Se puede arreglar con SES, pero academy no tiene acceso
        sns_client = boto3.client('sns')
        response_sns = sns_client.publish(
            TopicArn = 'arn:aws:sns:us-east-1:519224807613:Tema_Respuesta',
            Subject = 'Respondieron a tu pregunta! Revísala',
            Message = json.dumps('Un usuario a respondido a tu pregunta')
            # MessageAttributes = 
            )
        
        return{
            'statusCode': 200,
            'body': json.dumps('Respuesta creada exitosamente.')
        }
    
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error creando respuesta.')
        }
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()