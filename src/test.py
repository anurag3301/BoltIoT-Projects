from boltiot import Bolt #import necessary libraries
import conf, time #conf contains Bolt device id and API key, available from Bolt cloud dashboard



mybolt = Bolt(conf.API_KEY,conf.DEVICE_ID) #Create bolt object


response = mybolt.serialWrite(1)
print(response)
response = mybolt.serialRead("1")
print(response)
