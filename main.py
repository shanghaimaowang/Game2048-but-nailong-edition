import pygame
import sys
import game2048

#初始化游戏
pygame.init()
#创建窗口（画布）、时钟
screen=pygame.display.set_mode(size=(600,430))
pygame.display.set_caption("2048 for the best")
clock=pygame.time.Clock()

#绘制背景
background=pygame.image.load("background.png")
background=pygame.transform.scale(background,(600,430))
overlay=pygame.Surface((600,430),pygame.SRCALPHA)
overlay.fill((255,255,255, 128))

#将格子绘制在画布上




#游戏进程主循环
is_running=True
while is_running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background, (0, 0))
    screen.blit(overlay,(0,0))
    pygame.display.flip()
    clock.tick(60)