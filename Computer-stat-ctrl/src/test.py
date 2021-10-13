from boltiot import Bolt #import necessary libraries
import time #conf contains Bolt device id and API key, available from Bolt cloud dashboard
import requests
import json
import config

def send_telegram_message(message):
    """Sends message via Telegram"""
    url = "https://api.telegram.org/" + config.telegram_bot_id + "/sendMessage"
    data = {
        "chat_id": config.telegram_chat_id,
        "text": message
    }
    try:
        response = requests.request(
            "POST",
            url,
            params=data
        )
        print("This is the Telegram URL")
        print(url)
        print("This is the Telegram response")
        print(response.text)
        telegram_data = json.loads(response.text)
        return telegram_data["ok"]
    except Exception as e:
        print("An error occurred in sending the alert message via Telegram")
        print(e)
        return False



mybolt = Bolt(config.API_KEY, config.DEVICE_ID) #Create bolt object

response = json.loads(mybolt.serialWrite(1))
print(response)
response = json.loads(mybolt.serialRead("1"))
print(response)

if(response["value"] == "0"):
	send_telegram_message("The computer is offf...")
if(response["value"] == "1"):
	send_telegram_message("The computer is working")

