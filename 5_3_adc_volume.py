import RPi.GPIO as g
import time

def d2b(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    res = 0
    i = 0
    while i < 8:
        time.sleep(0.02)
        g.output(dac[i], g.HIGH)
        time.sleep(0.03)
        if not g.input(comp):
            g.output(dac[i], g.LOW)
        else:
            res += 2**(7 - i)
        i += 1
    return res
    


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
leds = [21, 20, 16, 12, 7, 8, 25, 24]

g.setmode(g.BCM)
g.setup(dac, g.OUT)
g.setup(comp, g.IN)
g.setup(troyka, g.OUT, initial=0)
g.setup(leds, g.OUT)

try:
    while True:
        num = adc()
        i = num * 8 // 256
        l = [0] * (8 - i) + [1] * i
        g.output(leds, l)
        g.output(dac, 0)
        time.sleep(0.1)
finally:
    g.output(dac, 0)
    g.cleanup()