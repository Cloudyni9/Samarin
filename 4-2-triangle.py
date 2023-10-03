import RPi.GPIO as gpio
from time import sleep
import sys

dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def dec2bin(a, b):
    return [int(x) for x in bin(a)[2:].zfill(b)]

try:
    while (True):
        c = input()
        if c == 'q':
            sys.exit()
        elif not c.isdigit():
            print('is not a disigned intenger')
            sys.exit()
        n = int(c)/512
        for i in range(256):
            gpio.output(dac, dec2bin(i, 8))
            sleep(n)
        for i in range(255, -1, -1):
            gpio.output(dac, dec2bin(i, 8))
            sleep(n)






finally:
    gpio.output(dac, 0)
    gpio.cleanup()
