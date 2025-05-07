import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def save_flight_info(cursor, data):
    cursor.execute("""
        INSERT INTO voos_info (
            origem, destino, data_ida, data_volta, preco, moeda,
            carrierCode, flightNumber, departureIATA, departureTime,
            arrivalIATA, arrivalTime, created_at
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, data)
