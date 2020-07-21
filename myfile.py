import RPi.GPIO as GPIO
import time
from gtts import gTTS
import os
import pygame
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24
while 1:

    GPIO.setmode(GPIO.BCM)
    print("Distance Measurement In Progress")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    
    GPIO.output(TRIG, False)
    print("Waiting For Sensor To Settle")
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print("Distance:",distance,"cm")
    if distance <= 50:
        
        mytext = 'Alert'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("output.mp3")
        os.system("start output.mp3") 
        file='output.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(2)
    GPIO.cleanup()

