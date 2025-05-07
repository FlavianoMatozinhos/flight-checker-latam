from amadeus_client import init_amadeus_client, search_flights
from db import get_connection, save_flight_info
from utils import to_brazil_time, now_brazil_str
from telegram import send_telegram_message

ORIGEM = 'GRU'
DESTINO = 'MLA'
DATA_IDA = '2025-11-08'
ADULTOS = 1

def main():
    amadeus = init_amadeus_client()
    voos = search_flights(amadeus, ORIGEM, DESTINO, DATA_IDA, ADULTOS)

    if not voos:
        print("Nenhum voo encontrado.")
        return

    voos_latam = [
        voo for voo in voos if any(
            s['carrierCode'].upper() == 'LA'
            for i in voo['itineraries']
            for s in i['segments']
        )
    ]

    if not voos_latam:
        print("Nenhum voo da LATAM encontrado.")
        return

    mais_barato = min(voos_latam, key=lambda v: float(v['price']['total']))
    preco = mais_barato['price']['total']
    moeda = mais_barato['price']['currency']
    carrier = mais_barato['itineraries'][0]['segments'][0]['carrierCode']
    
    mensagem = f"💰 Voo mais barato da companhia {carrier}: {preco} {moeda}\n\n"
    mensagem += "✈️ Itinerários:\n"
    mensagem += f"🛫 {ORIGEM} ➜ {DESTINO} | {DATA_IDA}\n"

    for it in mais_barato['itineraries']:
        for seg in it['segments']:
            dep = seg['departure']['iataCode']
            arr = seg['arrival']['iataCode']
            num = f"{seg['carrierCode']}{seg['number']}"
            mensagem += f"{dep} ➜ {arr} | {num}\n"

    send_telegram_message(mensagem)

    conn = get_connection()
    cursor = conn.cursor()

    for it in mais_barato['itineraries']:
        for seg in it['segments']:
            dep_time = to_brazil_time(seg['departure']['at'])
            arr_time = to_brazil_time(seg['arrival']['at'])

            data = (
                ORIGEM,
                DESTINO,
                DATA_IDA,
                0,
                preco,
                moeda,
                seg['carrierCode'],
                seg['number'],
                seg['departure']['iataCode'],
                dep_time.strftime('%d/%m/%Y %H:%M:%S'),
                seg['arrival']['iataCode'],
                arr_time.strftime('%d/%m/%Y %H:%M:%S'),
                now_brazil_str()
            )
            save_flight_info(cursor, data)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
