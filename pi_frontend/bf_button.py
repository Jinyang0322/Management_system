# -*- coding=utf-8 -*-
import threading
import pygame
from pygame.locals import MOUSEBUTTONDOWN


# CLICK_EFFECT_TIME = 100
class BFButton(object):
    def __init__(self, parent, rect, text='Button', click=None):
        self.x,self.y,self.width,self.height = rect
        self.bg_color = (255,250,205)
        self.parent = parent
        self.surface = parent.subsurface(rect)
        self.is_hover = False
        self._text = text
        self._visible = True
        self.init_font()

    def init_font(self):
        font = pygame.font.SysFont('arial',24)
        white = 100, 100, 100
        self.textImage = font.render(self._text, True, white)
        w, h = self.textImage.get_size()
        self._tx = (self.width - w) / 2
        self._ty = (self.height - h) / 2


    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.init_font()

    def draw(self):
        self.surface.fill(self.bg_color)
        self.surface.fill(self.bg_color)
        pygame.draw.rect(self.surface, (0,0,0), (0,0,self.width,self.height), 1)
        pygame.draw.rect(self.surface, (100,100,100), (0,0,self.width-1,self.height-1), 1)
        pygame.draw.rect(self.surface, self.bg_color, (0,0,self.width-2,self.height-2), 1)
        self.surface.blit(self.textImage, (self._tx, self._ty))
