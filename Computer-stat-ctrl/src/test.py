from boltiot import Bolt
import time
import requests
import json
import os
from discord_webhook import DiscordWebhook

mybolt = Bolt(os.environ["API_KEY"], os.environ["DEVICE_ID"]) #Create bolt object

response = json.loads(mybolt.serialWrite(1))
print(response)

response = json.loads(mybolt.serialRead("1"))
print(response)

if(response["value"] == "0"):
    webhook = DiscordWebhook(url=os.environ["DISCORD_URL"], content="The computer is offf...")
    webhook.execute()

if(response["value"] == "1"):
    webhook = DiscordWebhook(url=os.environ["DISCORD_URL"], content="The computer is working")
    webhook.execute()

