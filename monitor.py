
import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=20
    )
    response.raise_for_status()

send_alert(
    "🟢 SABARIMALA SLOT ALERT!\n"
    "Date: 12 December 2026\n"
    "Pilgrims: 5\n"
    "Route: Nilakkal – Pamba\n"
    "Check official booking immediately:\n"
    "https://sabarimalaonline.org/"
)
