import pygame
import sys
from game2048 import ezfe

#初始化游戏
pygame.init()
game_2048 = ezfe()
#创建窗口（画布）、时钟
screen=pygame.display.set_mode(size=(600,430))
pygame.display.set_caption("2048 for the best")
clock=pygame.time.Clock()

#绘制背景
background=pygame.image.load("background.png")
background=pygame.transform.scale(background,(430,430))
overlay=pygame.Surface((600,430),pygame.SRCALPHA)
overlay.fill((255,255,255, 128))
pygame.draw.rect(overlay,(150,150,150),(430,0,170,430))

#游戏区域与控制区域分割线
pygame.draw.line(overlay,(0,0,0),(430,0),(430,430),2)

#开始按钮
start_rect = pygame.Rect(470, 50, 90, 50)
start_background=pygame.Surface(start_rect.size,pygame.SRCALPHA)
pygame.draw.rect(start_background,(0,0,0,225),start_background.get_rect(),border_radius=24)
start_font=pygame.font.SysFont("kaiti",30,True)
start_font=start_font.render("开始",True,"black")
temp_rect=start_font.get_rect(center=start_background.get_rect().center)
pygame.draw.rect(start_background,(255, 255, 0),(2,2,86,46),border_radius=24)
start_background.blit(start_font,temp_rect)
if_get_start=False

# 开始按钮测试
overlay_surface = pygame.Surface((600, 430), pygame.SRCALPHA)
overlay_surface.fill((0, 0, 0, 128))

#分数
source_font=pygame.font.SysFont("kaiti",30,True)
source_font = source_font.render(text="分数：" , antialias=True, color="black")
source_rect = pygame.Rect(430, 300, 150, 100)

#游戏进程主循环
is_running=True
while is_running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                if_get_start=True
                game_2048.randomgenerateNumber()

        if event.type==pygame.KEYDOWN and if_get_start:
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    game_2048.set_direction(
                        {pygame.K_UP: 'up', pygame.K_DOWN: 'down', pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right'}[
                            event.key])
                    game_2048.move()
                    game_2048.randomgenerateNumber()

    source_font_ = pygame.font.SysFont("kaiti", 30, True)
    source = game_2048.get_source()
    source_font_ = source_font_.render(text=str(source), antialias=True, color="black")
    source_rect_ = pygame.Rect(520, 300, 150, 100)

    #打印背景
    screen.blit(background, (0, 0))
    screen.blit(overlay,(0,0))
    screen.blit(start_background, start_rect)
    screen.blit(source_font_, source_rect_)
    screen.blit(source_font, source_rect)

    if if_get_start:
        if game_2048.gameisover:
            is_running=False

        #游戏显示画布
        game_main_surface=pygame.Surface((430,430),pygame.SRCALPHA)
        game_2048.draw_rect(game_main_surface)
        screen.blit(game_main_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)