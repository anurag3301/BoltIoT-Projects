import requests
import json
import time
from boltiot import Bolt
import config

mybolt = Bolt(config.bolt_api_key, config.device_id)      # Connecting to the cloud using the API key and Bolt ID

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
    data = get_youtube_data(config.youtube_api, config.channel_id)
    if data:
        subs = str(data["subs"])
        views = str(data["views"])
        send = subs+ "$" + views 
    else:
        send = "-1$-1"
    response = mybolt.serialWrite(send)    
    print(response)
    time.sleep(30)
