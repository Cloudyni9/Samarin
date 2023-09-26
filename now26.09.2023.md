import RPi.GPIO as gpio
import sys

dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def binary(a, b):
    return [int(x) for x in bin(a)[2:].zfill(b)]

try:
    while (True):
        c = input('input 0-255 ')
        if c == 'q':
            sys.exit()
        elif c.isdigit() and int(c) % 1 == 0 and 0 <= int(c) <= 255:
            gpio.output(dac, binary(int(c), 8))
            print("{:.4f}".format(int(c) / 256 * 3.3))
        elif not c.isdigit():
            print('is not a true symbol')


except ValueError:
    print('input number 0-255')
except KeyboardInterrupt:
    print('done')

finally:
    gpio.output(dac, 0)
    gpio.cleanup()



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



import RPi.GPIO as gpio


dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setmode(gpio.BCM)
gpio.setup(19, gpio.OUT)
gpio.setup(dac, gpio.OUT)

pwm = gpio.PWM(19, 1000)
pwm.start(0)

try:
    while (True):
        c = int(input())
        pwm.ChangeDutyCycle(c)
        print("{:.2f}".format(c * 3.3/100))


finally:
    gpio.output(19, 0)
    gpio.output(dac, 0)
    gpio.cleanup()


