"Use this proggram to set up the scope to trigger on the step channel"
import RPi.GPIO as g
import time
step_channel = 12
#ms1_channel = 17
sleep_time = 100e-6
# 210-130 = 80
sleep_time -= 76e-6 # approximate overhead for switching
if sleep_time < 0: sleep_time = 0
g.setmode(g.BCM)
g.setup(step_channel,g.OUT)
#g.setup(ms1_channel,g.OUT)
for j in range(int(10./sleep_time)):
    time.sleep(sleep_time)
    #g.output(ms1_channel,True) # for quarter step
    time.sleep(2e-6)
    g.output(step_channel,True)
    time.sleep(sleep_time)
    #g.output(ms1_channel,False)
    g.output(step_channel,False)
    time.sleep(2e-6)
g.cleanup()
