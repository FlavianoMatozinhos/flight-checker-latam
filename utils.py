from datetime import datetime
import pytz

brasil_tz = pytz.timezone('America/Sao_Paulo')

def to_brazil_time(iso_date_str):
    return datetime.fromisoformat(iso_date_str).astimezone(brasil_tz)

def now_brazil_str():
    return datetime.now(brasil_tz).strftime('%d-%m-%y %H:%M:%S')
