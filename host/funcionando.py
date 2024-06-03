import network
import urequests as requests
import time
import json

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('MIND', '1234567890')

# Fill in your router's ssid and password here.
while not wifi.isconnected():
    print(".", end="")
    time.sleep(1)
print(" Connected!")

res = requests.get(url='http://10.92.3.205:5000/')
post_data = json.dumps({ 'account': 'infos'})
resP = requests.post(url='http://10.92.3.205:5000/mandar', headers = {'content-type': 'application/json'}, data = post_data)


print(res.text)
time.sleep(3)
   