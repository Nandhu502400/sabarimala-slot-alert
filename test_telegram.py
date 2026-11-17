
import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": "Sabarimala Cloud Monitor Connected Successfully! 🙏"
    },
    timeout=20
)

response.raise_for_status()
print("Telegram message sent successfully!")
