import requests
import json
import time
from boltiot import Bolt

bolt_api_key = "0f05f3f5-7704-43fa-ab27-4efd68da9639"  # Replace the string with the API key 
device_id = "BOLT8024024"    # Replace the string with your Bolt ID
youtube_api = "AIzaSyDyNfLg1j0wRmoHuRD_WmJSp9i5WgcMpQ8"
channel_id = "UCDzhFuVYou1D8w1ABZo3b9A"

mybolt = Bolt(bolt_api_key, device_id)      # Connecting to the cloud using the API key and Bolt ID

def get_youtube_data(key, id):
    url  = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + id\
            + "&key=" + key
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        return {"subs" : data["items"][0]["statistics"]["subscriberCount"],\
                "views": data["items"][0]["statistics"]["viewCount"]}
    except:
        return None


while True:
    data = get_youtube_data(youtube_api, channel_id)
    if data:
        subs = str(data["subs"])
        views = str(data["views"])
        send = subs+ "$" + views 
    else:
        send = "-1$-1"
    response = mybolt.serialWrite(send)    
    print(response)
    time.sleep(30)
