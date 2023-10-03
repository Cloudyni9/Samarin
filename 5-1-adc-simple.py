import RPi.GPIO as gpio
from time import sleep


gpio.setmode(gpio.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setup(dac, gpio.OUT)
comp = 14
troyka = 13


gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)



def dec2bin(a):
    return [int(x) for x in bin(a)[2:].zfill(8)]


def adc():
    for i in range(256):
        dac_ = dec2bin(i)
        gpio.output(dac, dac_)
        comp_ = gpio.input(comp)
        sleep(0.001)
        if comp_ == 1:
            return i

try:
    while (True):
        i = adc()
        if i != 0:
            print(3.3 * i / 256)



finally:
    gpio.output(dac, 0)
    gpio.cleanup()
