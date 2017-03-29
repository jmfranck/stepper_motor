import RPi.GPIO as GPIO
import time
from scope_trigger import trigger_scope
GPIO.setmode(GPIO.BCM)
MS1pin = 4
MS2pin = 17
MS3pin = 16
DIRpin = 25
STEPpin = 12 


GPIO.setup(MS1pin, GPIO.OUT)
GPIO.setup(MS2pin, GPIO.OUT)
GPIO.setup(MS3pin, GPIO.OUT)
GPIO.setup(DIRpin, GPIO.OUT)
GPIO.setup(STEPpin, GPIO.OUT)

def forward(delay,steps):
    for i in range(steps):
        trigger_scope()
        set_step('00000')
        time.sleep(1e-6)
        set_step('00101')
        set_step('10101')
        time.sleep(1e-6)
        set_step('00000')
        time.sleep(delay)

#def backward(delay,steps):
#    for i in range(steps):
#        set_step('00000')
#        time.sleep(1e-6)
#        set_step('00000')
#        set_step('10000')
#        time.sleep(1e-6)
#        set_step('00000')
#        time.sleep(delay)
#
def set_step(step_str):
        assert len(step_str) == 5,"the string step_str is the wrong length"
        GPIO.output(STEPpin, step_str[0] == '1')
        GPIO.output(MS1pin, step_str[1] == '1')
        GPIO.output(MS2pin, step_str[2] == '1')
        GPIO.output(MS3pin, step_str[3] == '1')
        GPIO.output(DIRpin, step_str[4] == '1')

#while True:
set_step('00000')
delay = raw_input("Delay between steps (microseconds)?")
howlong = raw_input("Step for how long (seconds)")
forward(int(delay)*1e-6, int(int(howlong)/(int(delay)*1e-6)))
set_step('00000')
#steps = raw_input("How many steps backwards?")
#backward(int(delay)/1000.0, int(steps))
GPIO.cleanup()
