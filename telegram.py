import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # grupo (com o ID negativo)

def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"  # ou "MarkdownV2"
    }

    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print(f"[Erro] Falha ao enviar mensagem: {response.text}")
    else:
        print("[Telegram] Mensagem enviada com sucesso!")
