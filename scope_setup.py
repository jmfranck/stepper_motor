"Use this proggram to set up the scope to trigger on the step channel"
import RPi.GPIO as g
import time
import sys
if len(sys.argv) < 2:
    print "Add an argument giving the sleep time in microseconds!"
    exit(1)
if len(sys.argv) > 2:
    run_length = int(sys.argv[2])
else:
    run_length = 5
sleep_time = int(sys.argv[1])*1e-6
step_channel = 12
#ms1_channel = 17
#sleep_time = 100e-6
# 210-130 = 80
sleep_time -= 76e-6 # approximate overhead for switching
if sleep_time < 0: sleep_time = 0
g.setmode(g.BCM)
g.setup(step_channel,g.OUT)
#g.setup(ms1_channel,g.OUT)
loop_overhead = 0.5e-3
desired_steps = int(float(run_length)/(2*sleep_time+loop_overhead))
for j in range(desired_steps):
    if j % 10 == 0:
        print j,'/',desired_steps
    time.sleep(sleep_time)
    #g.output(ms1_channel,True) # for quarter step
    time.sleep(2e-6)
    g.output(step_channel,True)
    time.sleep(sleep_time)
    #g.output(ms1_channel,False)
    g.output(step_channel,False)
    time.sleep(2e-6)
g.cleanup()
