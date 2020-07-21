import RPi.GPIO as GPIO          #Import GPIO library
import time                      #Import time library
from gtts import gTTS
import os
import pygame
GPIO.setmode(GPIO.BOARD)         #Set GPIO pin numbering
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Enable input and pull up resistors
while True:
    input_state = GPIO.input(12) #Read and store value of input to a variable
    if input_state == False:     #Check whether pin is grounded
        mytext = 'ok google call my contact'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("first.mp3")
        os.system("start first.mp3") 
        file='first.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(2)#Print 'Button Pressed'
    time.sleep(0.3)    