from amadeus_client import get_amadeus_client, search_flights
from database import get_db_connection, insert_flight_data
from flight_utils import convert_to_brazil_time, format_datetime, filter_latam_flights, get_cheapest_flight

# Parâmetros da busca
ORIGEM = 'GRU'
DESTINO = 'MLA'
DATA_IDA = '2025-11-08'
ADULTOS = 1

def main():
    amadeus = get_amadeus_client()
    voos = search_flights(amadeus, ORIGEM, DESTINO, DATA_IDA, ADULTOS)

    if not voos:
        print("Nenhum voo encontrado.")
        return

    voos_latam = filter_latam_flights(voos)

    if not voos_latam:
        print("Nenhum voo da LATAM encontrado.")
        return

    voo_mais_barato = get_cheapest_flight(voos_latam)
    preco = voo_mais_barato['price']['total']
    moeda = voo_mais_barato['price']['currency']
    print(f"\n💰 Voo mais barato da LATAM: {preco} {moeda}")

    db = get_db_connection()
    cursor = db.cursor()

    for itinerary in voo_mais_barato['itineraries']:
        for segment in itinerary['segments']:
            dep = segment['departure']
            arr = segment['arrival']

            dep_time = convert_to_brazil_time(dep['at'])
            arr_time = convert_to_brazil_time(arr['at'])

            dep_time_str = format_datetime(dep_time)
            arr_time_str = format_datetime(arr_time)

            print(f"    {dep['iataCode']} ({dep_time_str}) ➜ {arr['iataCode']} ({arr_time_str}) | {segment['carrierCode']}{segment['number']}")

            flight_data = (
                ORIGEM,
                DESTINO,
                DATA_IDA,
                None,  # Data de volta não disponível
                preco,
                moeda,
                segment['carrierCode'],
                segment['number'],
                dep['iataCode'],
                dep_time_str,
                arr['iataCode'],
                arr_time_str
            )

            insert_flight_data(cursor, flight_data)

    db.commit()
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
