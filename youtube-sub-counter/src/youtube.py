import requests
import json
import time
from boltiot import Bolt

bolt_api_key = "0f05f3f5-7704-43fa-ab27-4efd68da9639"  # Replace the string with the API key 
device_id = "BOLT8024024"    # Replace the string with your Bolt ID
youtube_api = "AIzaSyDyNfLg1j0wRmoHuRD_WmJSp9i5WgcMpQ8"
channel_id = "UClqdtHozFJQsFI46mcsrchw"

mybolt = Bolt(bolt_api_key, device_id)      # Connecting to the cloud using the API key and Bolt ID

