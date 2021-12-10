
import os
import time
import numpy as np
import pygame
from getinfo import get_announcement, get_scheudule, get_question, post_ans
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from datetime import date
import time

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
class Frontend:
    def __init__(self):
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # os.putenv('SDL_VIDEODRIVER', 'fbcon')  # Display on piTFT
        # os.putenv('SDL_FBDEV', '/dev/fb1')
        # os.putenv('SDL_MOUSEDRV', 'TSLIB')  # Track mouse clicks on piTFT
        # os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')
        pygame.init()
        pygame.mouse.set_visible(True)
        self.size = width, height = 320, 240
        self.WHITE = 255, 255, 255
        self.BLACK = 0, 0, 0
        self.screen = pygame.display.set_mode(self.size)
        self.my_font = pygame.font.Font("Raleway-Regular.ttf", 20)  # Settings for 1st and 2nd level buttons
        self.my_font1 = pygame.font.Font("Tangerine-Bold.ttf", 35)
        self.my_buttons = {'Start': (80, 220), 'Quit': (240, 220)}
        self.my_buttons_lv2 = {'1.show courses': (100, 50), '2. view announcement': (100, 100), '3.vote for survey': (100, 150)}
        self.my_buttons_lv3 = {'Back': (290, 220)}
        self.my_buttons_lv4 = {'True': (90, 130), 'False': (230, 130)}
        self.cord = 'welcome, Jinyang'  # Set initial text
        self.date = str(date.today())
        self.time = time.strftime("%H:%M:%S")
        self.cord_surface = self.my_font1.render(self.cord, True, self.BLACK)
        self.time_surface = self.my_font1.render(self.time, True, self.BLACK)
        self.date_surface = self.my_font1.render(self.date, True, self.BLACK)
        self.cord_rect = self.cord_surface.get_rect(center=(160, 100))
        self.time_rect = self.time_surface.get_rect(center=(160, 150))
        self.date_rect = self.date_surface.get_rect(center=(160, 180))
        self.RED = 255, 0, 0
        self.cursorIdx = 0
        self.cursor = {'-->': (80, 50)}



    # def GPIO27_callback(self,channel):
    #     print("Exit Program...")
    #     exit(True)


    def drawBackground(self):
        bg = pygame.image.load("flower.png")
        bg = pygame.transform.scale(bg, (320, 240))
        self.screen.blit(bg, (0, 0))

    def drawIcon(self):
        icon = pygame.image.load("bigred.png")
        icon = pygame.transform.scale(icon, (40, 40))
        self.screen.blit(icon, (20, 10))

    def drawCursor(self):
        # draw the buttons
        for my_text, pos in self.cursor.items():
            vertical = 50 + self.cursorIdx * 50
            pos = (70, vertical)
            text_surface = self.my_font.render(my_text, True, self.RED)
            orderRect = text_surface.get_rect(topleft=pos)
            self.screen.blit(text_surface, orderRect)




    def loopbegin(self):
        # Initialize two ball collision animation
        screen = pygame.display.set_mode(self.size)
        playanimation = False  # Flag for play animation
        showmessage = False
        paused = False  # Flag for pause animation
        timelimit = 600
        starttime = time.time()
        res = []
        length = 0
        num = 0
        while True:
            time.sleep(0.2)
            self.drawBackground()
            self.drawIcon()
            for event in pygame.event.get():  # Detect touch event

                if (event.type == MOUSEBUTTONDOWN):
                    pos = pygame.mouse.get_pos()
                elif (event.type == MOUSEBUTTONUP):
                    pos = pygame.mouse.get_pos()
                    x, y = pos
                    # Save touch position coordinates
                    cord = 'Touch at ' + str(x) + ', ' + str(y)
                    cord_surface = self.my_font.render(cord, True, self.WHITE)
                    cord_rect = cord_surface.get_rect(center=(160, 100))
                    print(cord)  # Also print coordinates in concole
                    if playanimation:  # If currently playing animation
                    # Check touch event on 2nd level buttons
                        if 200 > x > 110 :
                            if y < 75:  # If pause/resume button is pressed
                                if num != 1:
                                    num = 1
                                    self.cursorIdx = 0
                                else:
                                    res = get_scheudule('jd2249')
                                    showmessage = True

                            elif y < 125:  # If fast button is pressed
                                if num != 2:
                                    num = 2
                                    self.cursorIdx = 1
                                else:
                                    res = get_announcement()
                                    showmessage = True
                            elif y < 175:  # If slow button is pressed
                                if num != 3:
                                    num = 3
                                    self.cursorIdx = 2
                                else:
                                    showmessage = True
                                    res = get_question()

                        elif y > 200 and x > 270:  # If back button is pressed
                            if showmessage:
                                showmessage = False
                                num = 0
                            else:
                                playanimation = False  # Return to 1st level

                        elif length == 1 and showmessage:
                            print('111111')
                            if 115 < y < 145:
                                if 70 < x < 110:
                                    showmessage = False
                                    post_ans()
                                elif 210 < x < 250:
                                    showmessage = False

                    else:  # Check touch event on 1st level buttons
                        if y > 200:
                            if x < 160:  # If play button is pressed
                                playanimation = True  # Switch to animation mode
                            else:  # If quit button is pressed
                                exit(True)  # Exit program
            # screen.fill(self.BLACK)  # Flush screen
            if (playanimation):  # If currently playing animation
                length = len(res)
                if not showmessage:
                    # default = 'choose a function'  # Set initial text
                    # default_surface = self.my_font.render(default, True, self.BLACK)
                    # default_rect = default_surface.get_rect(center=(160, 100))
                    # screen.blit(default_surface, default_rect)
                    for my_text, text_pos in self.my_buttons_lv2.items():
                        text_surface = self.my_font.render(my_text, True, self.BLACK)
                        rect = text_surface.get_rect(topleft=text_pos)
                        screen.blit(text_surface, rect)
                    self.drawCursor()
                else:
                    for line in range(length):
                        content_surface = self.my_font.render(res[line], True, self.BLACK)
                        content_rect = content_surface.get_rect(center=[160, 50+line*25])
                        screen.blit(content_surface, content_rect)
                    if length == 1:
                        for my_text, text_pos in self.my_buttons_lv4.items():
                            text_surface = self.my_font.render(my_text, True, self.BLACK)
                            rect = text_surface.get_rect(center=text_pos)
                            screen.blit(text_surface, rect)



            # Attach 2nd level buttons to screen
                for my_text, text_pos in self.my_buttons_lv3.items():
                    text_surface = self.my_font.render(my_text, True, self.BLACK)
                    rect = text_surface.get_rect(center=text_pos)
                    screen.blit(text_surface, rect)
            else:  # If currently not playing animation, display touch position coordinates
                time1 = time.strftime("%H:%M:%S")
                time_surface = self.my_font1.render(time1, True, self.BLACK)
                time_rect = time_surface.get_rect(center=(160, 150))
                screen.blit(self.cord_surface, self.cord_rect)
                screen.blit(time_surface, time_rect)
                screen.blit(self.date_surface, self.date_rect)
                # Attach 1sd level buttons to screen
                for my_text, text_pos in self.my_buttons.items():
                    # default = 'choose a function'  # Set initial text
                    # default_surface = self.my_font.render(default, True, self.WHITE)
                    # default_rect = default_surface.get_rect(center=(160, 100))
                    # screen.blit(default_surface, default_rect)
                    text_surface = self.my_font.render(my_text, True, self.BLACK)
                    rect = text_surface.get_rect(center=text_pos)
                    screen.blit(text_surface, rect)
            pygame.display.flip()  # Display new frame
            # Set bail button
            currenttime = time.time()
            if (currenttime - starttime > timelimit):
                exit(True)



c = Frontend()
c.loopbegin()