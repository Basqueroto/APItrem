import network
import urequests as requests
import time
import json
import machine, time
from machine import Pin
from machine import Pin, I2C
import utime, math

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('MIND', '1234567890') #nome e senha da red

# Fill in your router's ssid and password here.
while not wifi.isconnected():
    print(".", end="")
    time.sleep(1)
print(" Connected!")

# pwm
pwm = PWM(Pin(2), freq=50, duty=0)
host = 'http://10.92.3.205:5000'
state = 'direita'
controleId = 'one'

def Servo(servo, angle):
    # angle / 180（ * 2（0°-180°） + 0.5（）/ 20ms * 1023
    pwm.duty(int(((angle)/180 *2 + 0.5) / 20 * 1023))    


def moveServo(position):
    Servo(pwm, position)
    utime.sleep(1)
    print("Servo  Angle : ",position)

while True:

    resP = requests.get(url=f'{host}/controleTrilhos', headers = {'content-type': 'application/json'})
    print(resP)
    
    state = resP
    
    if state[controleId] == 'direita':
        moveServo(0)
    else:
        moveServo(180)
    
    time.sleep(1)

