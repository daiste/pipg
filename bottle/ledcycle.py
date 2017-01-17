from bottle import route, run, template
from gpiozero import LED, Button
from time import sleep, time
from random import random

led1 = LED(18)
led2 = LED(23)
led3 = LED(24)
led4 = LED(12)
led5 = LED(16)
led6 = LED(21)
button = Button(2)
active = True
ledList = [led1, led2, led3, led4, led5, led6]

@route('/hello/:name')
def index(name='World'):
    global active
    global ledList
    global time
    active = not active
    i = 0;
    prev = len(ledList) -2
    if active == False:
        while i < len(ledList): 
            ledList[i].off()
            i = i + 1 
    else:
        #while i < len(ledList):
        while (True):
            if i == len(ledList):
                i = 0
            if prev == len(ledList):
                prev = 0
            ledList[i].on()
            ledList[prev].off()
            #sleep(random()/4)
            sleep(0.3)
            i = i + 1
            prev = prev + 1
    return template('<b>Hello {{name}}: led active:{{active}}</b>!', name=name, active=active)

run(host='0.0.0.0', port=8080)
