from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(2)
active = False

while True:
    if active == False:
        led.off()
    else:
        led.on()
    button.wait_for_press()
    button.wait_for_release()
    active = not active
