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

        # Obtener de "event" los atributos de la tabla de usuarios
        username = event['username']
        U_gmail = event['usuario_gmail']
        carrera = event['carrera']
        ciclo = event['ciclo']
        password=event['password']

        # Insertar en la tabla "usuarios"
        cursor.execute(f"INSERT INTO usuarios (nombre, gmail, carrera, ciclo,contrasenha) VALUES ('{username}', '{U_gmail}', '{carrera}', {ciclo}, '{password}');")

        conn.commit()
        
        return{
            'statusCode': 200,
            'body': json.dumps('Usuario creado exitosamente.')
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