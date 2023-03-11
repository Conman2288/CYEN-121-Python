####################################
# Name: Connor Heard
# Date: 2 / 13 / 2023
# Desc: Rpi 04: Simon
####################################
import RPi.GPIO as GPIO
from time import sleep
from random import randint
import pygame

# set to True to enable debugging mode
DEBUG = True

# a variable that keeps track of the score
score = 0

# initialize the pygame library
pygame.init()

# set the GPIO pin numbers
# the switches from left to right
switches = [20, 16, 12, 26]
# LEDs from left to right
leds = [6, 13, 19, 21]
# the sounds that map to each LED (from L to R)
sounds = [pygame.mixer.Sound("one.wav"), pygame.mixer.Sound("two.wav"), pygame.mixer.Sound("three.wav"), pygame.mixer.Sound("four.wav")]

# use he Broadcom pin mode
GPIO.setmode(GPIO.BCM)

# setup the input and output pins
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

# this function turns the LEDs on
def all_on():
    for i in leds:
        GPIO.output(leds, True)
        
# this function turns the LEDs off
def all_off():
    for i in leds:
        GPIO.output(leds, False)
        
# this function flashes the LEDs a few times when the player loses the game
def lose():
    for i in range(0, 4):
        all_on()
        sleep(0.5)
        all_off()
        sleep(0.5)
        
################# Main Program ########################
# initialize the Simon sequence
# each item in the sequence represents an LED (or switch) indexed at 0 through 3
seq = []
# randomly add the first two items to the sequence
seq.append(randint(0, 3))
seq.append(randint(0, 3))

print("Welcome to Simon!")
print("Try to play the sequence back by pressing the switches.")
print("Press the switches or Ctrl+C to exit...")
# we'll discuss this later, but this allows us to detect
# when Ctrl+C is pressed so that we can reset the GPIO pins
try:
    # keep going untill the user presses Ctrl+C
    while(True):
        # randomly add one more item to the sequence
        seq.append(randint(0, 3))
        if (DEBUG):
            # display the sequence to the console
            if (len(seq) > 3):
                print()
            print("seq={}".format(seq))
            
        # display the sequence using the LEDs
        for s in seq:
            if (len(seq) < 5):
                # turn the appropriate LED on
                GPIO.output(leds[s], True)
                # play its corresponding sounds
                sounds[s].play()
                # wait and turn the LED off again
                sleep(1)
                GPIO.output(leds[s], False)
                sleep(0.5)
            # When the user reaches a sequence of 5 notes then the leds and sound speed up
            elif (len(seq) < 7):
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(0.9)
                GPIO.output(leds[s], False)
                sleep(0.4)
            # when the user reaches a sequence of 7 notes, the leds and sound speed up
            elif (len(seq) < 10):
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(0.8)
                GPIO.output(leds[s], False)
                sleep(0.3)
            # when the user reaches a sequence of 10 notes, the leds and sound speed up
            elif (len(seq) < 13):
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(0.7)
                GPIO.output(leds[s], False)
                sleep(0.25)
            # when the user reaches a sequence of 13 notes, the leds and sound speed up
            elif (len(seq) < 15):
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(0.6)
                GPIO.output(leds[s], False)
                sleep(0.15)
                
            # If the player reaches to a sequence of 15, the leds stop flashing
            else:
                sleep(0.15)
                sounds[s].play()
                sleep(0.6)
                
        
        # Wait for player input
        # initialize the count of switches pressed to 0
        switch_count = 0
        # keep accepting player input until the number of items in the sequence is reached
        while (switch_count < len(seq)):

            # Initially note that no switch is pressed
            # This will help with the switch debouncing
            pressed = False
            # so long as no swith is currently pressed...
            while(not pressed):
                # ... we can check the status of each switch
                for i in range (len(switches)):
                    # if one switch is pressed
                    while (GPIO.input(switches[i]) == True):
                        # note its index
                        val = i
                        # note that a switch has now been pressed
                        pressed = True
                    
            if (DEBUG):
                # display the index of the switch pressed
                print(val)
                                               
            # light the matching LED
            GPIO.output(leds[val], True)
            # play its corresponding sound
            sounds[val].play()
            # wait and turn the LED off again
            sleep(1)
            GPIO.output(leds[val], False)
            sleep(0.25)
            
            # check to see if this LED is correct in the sequence
            if (val != seq[switch_count]):
                # player is incorrect; invoke the lose
                lose()
                # print out the score to the player
                if (len(seq) == 3):
                    print("You didn't even make it to a sequence!")
                else:
                    print("You made it to a sequence of {}!".format(len(seq)))
                # reset the GPIO pins
                GPIO.cleanup()
                # exit the game
                exit(0)
            
            # if the playar has the item in the sequence correct, increment the count.
            switch_count += 1
# detect Ctrl+C
except KeyboardInterrupt:
    # reset the GPIO pins
    GPIO.cleanup()
    print("\nSionara!")
                    
