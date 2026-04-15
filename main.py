import pygame
import sys
from game2048 import ezfe

#初始化游戏
pygame.init()

game_2048=ezfe()
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


#开始按钮
start_rect = pygame.Rect(440, 50, 90, 50)
start_background=pygame.Surface(start_rect.size,pygame.SRCALPHA)

start_font=pygame.font.SysFont("kaiti",30,True)
start_font=start_font.render("开始",True,"black")


temp_rect=start_font.get_rect(center=start_background.get_rect().center)
pygame.draw.rect(start_background,(255, 255, 0),start_background.get_rect(),border_radius=8)
start_background.blit(start_font,temp_rect)

ifgetstart=False
overlay_surface = pygame.Surface((600, 430), pygame.SRCALPHA)
overlay_surface.fill((0, 0, 0, 128))
#游戏进程主循环
is_running=True
while is_running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                ifgetstart=True


    screen.blit(background, (0, 0))
    screen.blit(overlay,(0,0))
    screen.blit(start_background, start_rect)
    if ifgetstart:
        screen.blit(overlay_surface, (0, 0))
    pygame.display.flip()
    clock.tick(60)