from datetime import datetime
import pytz
from config import TIMEZONE

def convert_to_brazil_time(iso_datetime_str):
    utc_time = datetime.fromisoformat(iso_datetime_str)
    brazil_tz = pytz.timezone(TIMEZONE)
    return utc_time.astimezone(brazil_tz)

def format_datetime(dt):
    return dt.strftime('%d/%m/%Y %H:%M:%S')

def filter_latam_flights(flights):
    return [
        flight for flight in flights
        if any(
            segment['carrierCode'].upper() == 'LA'
            for itinerary in flight['itineraries']
            for segment in itinerary['segments']
        )
    ]

def get_cheapest_flight(flights):
    return min(flights, key=lambda f: float(f['price']['total']))
