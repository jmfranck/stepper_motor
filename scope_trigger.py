import RPi.GPIO as g
import time
g.setmode(g.BCM)
g.setup(21,g.OUT)
def trigger_scope(wait=1e-6):
    """Just quickly flashes the voltage on the scope on GPIO21, which can then be used as a trigger.

    On 3/2/17, tested on Tektronix 2465 CTS 20 mV/div (which seems to be incorrect), A1 trigger level to 360 mV, 50 us/div.
    Yields pulses about 80 us wide (though you can get much faster by eliminating the "wait" statements.
    """
    g.output(21,True)
    time.sleep(wait)
    g.output(21,False)
    time.sleep(wait)
    g.output(21,True)
    time.sleep(wait)
    g.output(21,False)
for j in range(10000):
    trigger_scope()
    time.sleep(0.001)

