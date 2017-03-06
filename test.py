
import RPi.GPIO as GPIO
import time
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

forward_seq = ['10110','11111','11100','10100
reverse_seq = list(forward_seq)
reverse_seq.reverse()

def forward(delay,steps):
        for i in range(steps):
                set_step('00000')
		time.sleep(1e-6)
		set_step('00001')
		set_step('10001')
		time.slep(1e-6)
		set_step('00000')
		time.sleep(delay)

def forward(delay,steps):
	for i in range(steps):
		set_step('00000')
		set_step('10001')
		time.sleep(1e-6)
		set_step('00000')

def set_step(step_str):
        assert len(step_str) == 5,"the string step_str is the wrong length"
        GPIO.output(STEPpin, step_str[0] == '1')
        GPIO.output(MS1pin, step_str[1] == '1')
        GPIO.output(MS2pin, step_str[2] == '1')
        GPIO.output(MS3pin, step_str[3] == '1')
        GPIO.output(DIRpin, step_str[5] == '1') as GPIO




while True:
	set_step('00000')
	delay = raw_input("Delay between steps (milliseconds)?")
	steps = raw_input("How many steps forward?")
	forward(int(delay/1000.0, int(steps))
	set_step('00000')
	steps = raw_input("How many steps backwards?")
	backwards(int(delay)/1000.0, int(steps))

