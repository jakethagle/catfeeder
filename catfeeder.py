#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

def feed():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT)

	try:
		servo = GPIO.PWM(18, 50)
		servo.start(12.5)
		# Spin left then right because we have two opening to kick food out of
		for index in range(0, 2):
			dutyCycle = 2.5 if (index % 2 == 0) else 12.5
			servo.ChangeDutyCycle(dutyCycle)
			# adjust the sleep time to have the servo spin longer or shorter in that direction
			time.sleep(0.5)
	finally:
		servo.stop()
		GPIO.cleanup()
