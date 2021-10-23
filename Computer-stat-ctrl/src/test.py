from boltiot import Bolt #import necessary libraries
import time #conf contains Bolt device id and API key, available from Bolt cloud dashboard
import requests
import json
import os


mybolt = Bolt(os.environ["API_KEY"], os.environ["DEVICE_ID"]) #Create bolt object

response = json.loads(mybolt.serialWrite(1))
print(response)

