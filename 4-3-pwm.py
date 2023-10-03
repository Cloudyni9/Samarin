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
