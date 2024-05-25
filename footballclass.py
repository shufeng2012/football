import pygame,sys,os,time
from pygame.locals import *
FILE_PATH = os.path.join(os.path.dirname(__file__),'files')
os.chdir(FILE_PATH)
screen = pygame.display.set_mode((900,600))
def start(screen):
    pygame.init()
    pygame.mixer.init()
    start_music = pygame.mixer.music.load('football_start.mp3')
    font = pygame.font.Font('simsun.ttc',20)
    pygame.mixer.music.play(loops=-1)
    start_background = pygame.image.load('football_start.png')
    screen.blit(start_background,(0,0))
    pygame.display.set_caption('足球游戏')
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                pygame.mixer.music.stop()
                main(screen)
                return
        time.sleep(0.05)
        screen.fill(pygame.Color(0,0,0),Rect(0,560,900,40))
        if int(time.time())%2 ==0:
            screen.blit(font.render('按任意键开始游戏......',1,Color(255,255,255)),[200,565])
        pygame.display.update()
def main(screen):
    playground = pygame.image.load('playground.png')
    music = pygame.mixer.music.load('football_play.mp3')
    clock = pygame.time.Clock()
    pygame.mixer.music.play(loops=-1)
    while True:
        clock.tick(20)
        screen.blit(playground,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()