from boltiot import Bolt
import time
import requests
import json
import os


mybolt = Bolt(os.environ["API_KEY"], os.environ["DEVICE_ID"]) #Create bolt object

response = json.loads(mybolt.serialWrite(1))
print(response)

