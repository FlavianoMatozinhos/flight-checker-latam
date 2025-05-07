from amadeus import Client, ResponseError
from config import AMADEUS_CLIENT_ID, AMADEUS_CLIENT_SECRET

def init_amadeus_client():
    return Client(
        client_id=AMADEUS_CLIENT_ID,
        client_secret=AMADEUS_CLIENT_SECRET
    )

def search_flights(amadeus, origem, destino, data_ida, adultos=1, max_voos=100):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origem,
            destinationLocationCode=destino,
            departureDate=data_ida,
            adults=adultos,
            currencyCode='BRL',
            max=max_voos
        )
        return response.data
    except ResponseError as e:
        print(f"[ERRO] Falha na API Amadeus: {e}")
        return []
