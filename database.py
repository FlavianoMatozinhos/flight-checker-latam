import mysql.connector
from config import DB_CONFIG

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def insert_flight_data(cursor, flight_data):
    insert_query = """
        INSERT INTO voos_info (
            origem, destino, data_ida, data_volta, preco, moeda,
            carrierCode, flightNumber, departureIATA, departureTime,
            arrivalIATA, arrivalTime
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, flight_data)
