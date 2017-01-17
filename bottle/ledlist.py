from bottle import route, run, template
from gpiozero import LED, Button
from time import sleep

led1 = LED(18)
led2 = LED(23)
led3 = LED(24)
button = Button(2)
active = True
ledList = [led1, led2, led3]

@route('/hello/:name')
def index(name='World'):
    global active
    global ledList
    active = not active
    i = 0;
    if active == False:
        while i < len(ledList): 
            ledList[i].off()
            i = i + 1 
    else:
        while i < len(ledList):
            ledList[i].on()
            i = i + 1
    return template('<b>Hello {{name}}: led active:{{active}}</b>!', name=name, active=active)

run(host='0.0.0.0', port=8080)
