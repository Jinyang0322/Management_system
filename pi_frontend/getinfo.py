import requests
import pygame
from datetime import date
import time


def get_announcement():
    res = []
    r = requests.get(' http://127.0.0.1:8000/viewannounce/')
    dic = r.json()
    for i in dic.values():
        res.append(i)

    return res


def get_scheudule(sid):
    res = []
    url = 'http://127.0.0.1:8000/viewcourse/' + sid
    r = requests.get(url=url)
    dic = r.json()
    for i in dic.values():
        res.append(i)

    return res

def get_question():
    res = []
    url = 'http://127.0.0.1:8000/viewquestion/'
    r = requests.get(url=url)
    dic = r.json()
    for i in dic.values():
        res.append(i)

    return res


def post_ans():
    payload = {}
    url = 'http://127.0.0.1:8000/survey/answer/'
    r = requests.post(url=url, data=payload)


# def drawBackground():
#     bg = pygame.image.load("bg_image.jpg")
#     bg = pygame.transform.scale(bg, (320, 240))
#     screen.blit(bg, (0, 0))
#
# def drawIcon():
#     icon = pygame.image.load("delivery.png")
#     icon = pygame.transform.scale(icon, (40, 40))
#     screen.blit(icon, (270, 10))






