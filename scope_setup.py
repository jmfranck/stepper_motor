"Use this proggram to set up the scope to trigger on the step channel"
import RPi.GPIO as g
import time
step_channel = 12
sleep_time = 10e-6
g.setmode(g.BCM)
g.setup(step_channel,g.OUT)
for j in range(int(100./sleep_time)):
    time.sleep(sleep_time)
    g.output(step_channel,True)
    time.sleep(sleep_time)
    g.output(step_channel,False)
g.cleanup()
