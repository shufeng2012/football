import pygame,sys,os,time
from pygame.locals import *

FILE_PATH = os.path.join(os.path.dirname(__file__),'files')
os.chdir(FILE_PATH)

class player_one:
    player_two_image = pygame.image.load('player_two.png')
    score2 = 0
    def __init__(self,screen):
        self.player_one_line = [100-10,300-10]
        self.screen = screen
        self.rect = Rect(780,290,30,30)

    def move(self,KEY):         #获取按键
        if KEY == K_RIGHT:
            self.player_one_line[0] += 1
        elif KEY == K_LEFT:
            self.player_one_line[0] -= 1
        elif KEY == K_UP:
            self.player_one_line[1] -= 1
        elif KEY == K_DOWN:
            self.player_one_line[1] += 1
        else:
            pass

    def goal(self):         #进球函数
        self.score2 += 1

    def out(self):          #出界函数
        self.score2 -= 1