import machine
from time import sleep
led = machine.Pin(2, machine.Pin.OUT)

while True:
    led.value(1)
    sleep(0.4)
    led.value(0)
    sleep(0.4)

# a change again
