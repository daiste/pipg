from gpiozero import LED
import time

led = LED(17)
print ("Start : %s" % time.ctime())
count = 0
while (count<100):
	led.on()
	print("Led on ",count)
	time.sleep( 0.1 )
	led.off()
	#print("led off")
	time.sleep( 0.1)
	count = count+1
print("End : %s" % time.ctime())
