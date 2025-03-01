import os

import requests
from dotenv import load_dotenv


load_dotenv()

token = os.getenv("BOT_TOKEN")
network = os.getenv("NETWORK")
addresses = os.getenv("ADDRESSES")

def get_data_price():
    url = f"https://api.geckoterminal.com/api/v2/simple/networks/{network}/token_price/{addresses}/"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            return response.json()["data"]["attributes"]["token_prices"][addresses][0:6]
        except Exception:
            return "Щось сталось потойбічне 🤷🏿‍♂️"
    else:
        return "Щось сталось потойбічне 🤷🏿‍♂️"


def get_chat_id():
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "result" in data and len(data["result"]) > 0:
            chat_id = data["result"][0]["my_chat_member"]["chat"]["id"]
            print(f"Chat ID: {chat_id}")
            return chat_id
        else:
            print("Немає нових повідомлень.")
    else:
        print(f"Помилка запиту: {response.status_code}")


# get_chat_id()
