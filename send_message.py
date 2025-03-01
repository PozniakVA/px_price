import os
import time

import requests
import schedule
from dotenv import load_dotenv

from main import get_data_price


load_dotenv()

token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

time_sleep_value = int(os.getenv("TIME_SLEEP_VALUE"))
interval_in_hours = int(os.getenv("INTERVAL_IN_HOURS"))

def send_message_telegram():
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": f"PX - {get_data_price()} $"
    }

    requests.post(url, data=payload)


schedule.every(interval_in_hours).hours.do(send_message_telegram())

while True:
    schedule.run_pending()
    time.sleep(time_sleep_value)
