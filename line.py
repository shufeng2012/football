import pygame,sys,os
from pygame.locals import *
 
# 初始化 Pygame
pygame.init()
 
# 创建窗口
screen = pygame.display.set_mode((900,600))
FILE_PATH = os.path.join(os.path.dirname(__file__),'files')
os.chdir(FILE_PATH)
 
while True:
    # 事件处理
    playground = pygame.image.load('playground.png')
    screen.blit(playground,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # 获取鼠标位置
    mouse_pos = pygame.mouse.get_pos()
    
    # 打印鼠标坐标
    print("当前鼠标坐标为：", mouse_pos)
    
    # 更新显示
    pygame.display.update()