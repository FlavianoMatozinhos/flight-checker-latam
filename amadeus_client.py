from amadeus import Client, ResponseError
from config import AMADEUS_CLIENT_ID, AMADEUS_CLIENT_SECRET

def get_amadeus_client():
    return Client(
        client_id=AMADEUS_CLIENT_ID,
        client_secret=AMADEUS_CLIENT_SECRET
    )

def search_flights(amadeus, origin, destination, departure_date, adults=1, max_results=100):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=departure_date,
            adults=adults,
            currencyCode='BRL',
            max=max_results
        )
        return response.data
    except ResponseError as error:
        print("Erro ao buscar voos:", error)
        return []
