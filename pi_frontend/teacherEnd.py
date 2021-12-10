import os
import time
import numpy as np
import pygame
from getinfo import send_bluez
from bluez import getBlue
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP
# import RPi.GPIO as GPIO
#
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# os.putenv('SDL_VIDEODRIVER', 'fbcon')  # Display on piTFT
# os.putenv('SDL_FBDEV', '/dev/fb1')
# os.putenv('SDL_MOUSEDRV', 'TSLIB')  # Track mouse clicks on piTFT
# os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')
#
#
# def GPIO27_callback(channel):
#     print("Exit Program...")
#     exit(True)
#
#
# # Set bail button
# GPIO.add_event_detect(27, GPIO.FALLING, callback=GPIO27_callback, bouncetime=300)

pygame.init()
pygame.mouse.set_visible(True)
size = width, height = 320, 240
WHITE = 255, 255, 255
BLACK = 0, 0, 0
screen = pygame.display.set_mode(size)
my_font = pygame.font.Font(None, 24)  # Settings for 1st and 2nd level buttons
my_buttons = {'Read the signals': (160, 70), 'Send the signals': (160, 130), 'Quit': (160, 190)}
my_buttons_lv2 = {'back': (160, 220)}
cord = ''  # Set initial text
cord_surface = my_font.render(cord, True, WHITE)
cord_rect = cord_surface.get_rect(center=(160, 100))

# Initialize two ball collision animation
screen = pygame.display.set_mode(size)

playanimation = False  # Flag for play animation
paused = False  # Flag for pause animation
timelimit = 600
starttime = time.time()
res = []
while True:
    time.sleep(0.02)
    for event in pygame.event.get():  # Detect touch event
        if (event.type == MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif (event.type == MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x, y = pos
            # Save touch position coordinates
            cord = 'Touch at ' + str(x) + ', ' + str(y)
            cord_surface = my_font.render(cord, True, WHITE)
            cord_rect = cord_surface.get_rect(center=(160, 100))
            print(cord)  # Also print coordinates in concole
            if playanimation:  # If currently playing animation
            # Check touch event on 2nd level buttons
                if y > 200:
                    if x > 140:  # If pause/resume button is pressed
                        playanimation = False  # Return to 1st level
            else:
                if x > 140:
                    if y < 90:  # If play button is pressed
                        load = getBlue()
                        playanimation = True  # Switch to animation mode
                        txt = 0
                    if y > 160:  # If play button is pressed
                        print("quit")  # Switch to animation mode
                        exit(True)  # Exit program
                    else:  # If quit button is pressed
                        txt = 1
                        send_bluez(load)
                        playanimation = True  # Switch to animation mode
    screen.fill(BLACK)  # Flush screen
    if (playanimation):  # If currently playing animation
        if txt == 0:
            time.sleep(3)
            default = 'Successful reading the signals'  # Set initial text
            default_surface = my_font.render(default, True, WHITE)
            default_rect = default_surface.get_rect(center=(160, 100))
            screen.blit(default_surface, default_rect)

        if txt == 1:
            default = 'Successful sending the signals'  # Set initial text
            default_surface = my_font.render(default, True, WHITE)
            default_rect = default_surface.get_rect(center=(160, 100))
            screen.blit(default_surface, default_rect)

    # Attach 2nd level buttons to screen
        for my_text, text_pos in my_buttons_lv2.items():
            text_surface = my_font.render(my_text, True, WHITE)
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
    else:  # If currently not playing animation, display touch position coordinates

        default = ''  # Set initial text
        default_surface = my_font.render(default, True, WHITE)
        default_rect = default_surface.get_rect(center=(160, 100))
        screen.blit(default_surface, default_rect)
        # Attach 1sd level buttons to screen
        for my_text, text_pos in my_buttons.items():
            text_surface = my_font.render(my_text, True, WHITE)
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
    pygame.display.flip()  # Display new frame
    # Set bail button
    currenttime = time.time()
    if (currenttime - starttime > timelimit):
        exit(True)