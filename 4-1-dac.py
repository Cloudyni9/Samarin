import RPi.GPIO as gpio
import sys

dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def binary(a, b):
    return [int(elem) for elem in bin(a)[2:].zfill(b)]

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