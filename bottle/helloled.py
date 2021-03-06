from bottle import route, run, template
from gpiozero import LED, Button
from time import sleep

from subprocess import call
call(["sh","/home/pi/dev/pipg/bottle/testscript.sh"])
###, "-l"])
call(["ls","-l"])

led1 = LED(18)
led2 = LED(23)
led3 = LED(24)
button = Button(2)
active = True

@route('/hello/:name')
def index(name='World'):
    global active
    active = not active
    if active == False:
        led1.off()
        led2.off()
        led3.off()
    else:
        led1.on()
        led2.on()
        led3.on()
    return template('<b>Hello {{name}}: led active:{{active}}</b>!', name=name, active=active)

run(host='0.0.0.0', port=8080)
