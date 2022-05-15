import RPi.GPIO as g
import time

def d2b(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    res = 0
    for m in range(0, 255):
        m_b = d2b(m)
        time.sleep(0.05)
        g.output(dac, m_b)
        if g.input(comp):
            res += 1
        else:
            break
    return res


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

g.setmode(g.BCM)
g.setup(dac, g.OUT)
g.setup(comp, g.IN)
g.setup(troyka, g.OUT, initial=0)

try:
    msg = ''
    while msg != 'q':
        num = adc()
        num = num * 3.3 / 256
        print(num)
        msg = input()
        g.output(dac, 0)
finally:
    g.output(dac, 0)
    g.cleanup()