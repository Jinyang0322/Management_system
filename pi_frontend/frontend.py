
import os
import time
import numpy as np
import pygame
from getinfo import get_announcement, get_scheudule
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
my_buttons = {'Start': (80, 220), 'Quit': (240, 220)}
my_buttons_lv2 = {'courses': (40, 220), 'announce': (120, 220), 'attend': (200, 220), 'Back': (280, 220)}
cord = 'welcome, Jinyang'  # Set initial text
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
                    if x < 80:  # If pause/resume button is pressed
                        res = get_scheudule('jd2249')
                        length = len(res)
                    elif x < 160:  # If fast button is pressed
                        res = get_announcement()
                        length = len(res)

                    elif x < 240:  # If slow button is pressed
                        # 蓝牙part
                        bluetooth = 0
                    else:  # If back button is pressed

                        playanimation = False  # Return to 1st level
            else:  # Check touch event on 1st level buttons
                if y > 200:
                    if x < 160:  # If play button is pressed
                        playanimation = True  # Switch to animation mode
                    else:  # If quit button is pressed
                        exit(True)  # Exit program
    screen.fill(BLACK)  # Flush screen
    if (playanimation):  # If currently playing animation
        length = len(res)
        if length == 0:
            default = 'choose a function'  # Set initial text
            default_surface = my_font.render(default, True, WHITE)
            default_rect = default_surface.get_rect(center=(160, 100))
            screen.blit(default_surface, default_rect)

        for line in range(length):
            content_surface = my_font.render(res[line], True, WHITE)
            content_rect = content_surface.get_rect(center=[160, 50+line*25])
            screen.blit(content_surface, content_rect)

    # Attach 2nd level buttons to screen
        for my_text, text_pos in my_buttons_lv2.items():
            text_surface = my_font.render(my_text, True, WHITE)
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
    else:  # If currently not playing animation, display touch position coordinates

        default = 'welcome Jinyang'  # Set initial text
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


