from bottle import route, run, template
from gpiozero import LED, Button
from time import sleep

led = LED(18)
button = Button(2)
active = False

@route('/hello/:name')
def index(name='World'):
    global active
    active = not active
    if active == False:
        led.off()
    else:
        led.on()
    return template('<b>Hello {{name}}: led active:{{active}}</b>!', name=name, active=active)

run(host='0.0.0.0', port=8080)
