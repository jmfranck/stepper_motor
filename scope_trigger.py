import RPi.GPIO as g
import time
g.setmode(g.BCM)
g.setup(21,g.OUT)
def trigger_scope(wait=100e-6):
    """Just quickly flashes the voltage on the scope

    On 3/2/17, tested on Tektronix 2465 CTS 20 mV/div (which seems to be incorrect), A1 trigger level to 360 mV, 100 us/div"""
    g.output(21,True)
    time.sleep(wait)
    g.output(21,False)
    time.sleep(wait)
    g.output(21,True)
    time.sleep(wait)
    g.output(21,False)
for j in range(100):
    trigger_scope()
    time.sleep(0.5)

