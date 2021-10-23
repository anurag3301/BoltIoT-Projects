from boltiot import Bolt
import time
import requests
import json
import os
from discord_webhook import DiscordWebhook

mybolt = Bolt(os.environ["API_KEY"], os.environ["DEVICE_ID"]) #Create bolt object

response = json.loads(mybolt.serialWrite(1))
print(response)
webhook = DiscordWebhook(url=os.environ["DISCORD_URL"], content=str(response))
webhook.execute()
