import RPi.GPIO as g
import time
g.setmode(g.BCM)
g.setup(16,g.OUT)
g.output(16,True)
time.sleep(2)
g.output(16,False)

