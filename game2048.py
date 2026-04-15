import random
import pygame
import get_number_background


class ezfe():
    #初始化棋盘
    def __init__(self,matrix_size=(4,4),max_score_filepath : int=None,**kwargs):
        self.matrix_size=matrix_size
        self.max_score_filepath=max_score_filepath
        #self.initialize()
        #初始化方格都为null
        self.game_matrix=[["null"for _ in range(self.matrix_size[1])]
                          for _ in range(self.matrix_size[0])]

    def randomgenerateNumber(self):
        empty_pos=[]
        for i in range(self.matrix.size[0]):
            for j in range(self.matrix_size[1]):
                if self.game_matrix[i][j]=="null":
                    empty_pos.append([i,j])
        if len(empty_pos)==0:return
        empty=random.choice(empty_pos)
        i=empty[0]
        j=empty[1]
        self.game_matrix[i][j]=2 if random.random()>0.1 else 4

    def update(self):
        game_matrix_before = [row.copy() for row in self.game_matrix]
        #self.move()
        if self.game_matrix != game_matrix_before:
            self.randomgenerateNumber()

    def draw_rect(self,screen):
        cell_size=100
        gap=10
        start_x=0
        start_y=0
        for i in range(self.matrix_size[0]):
            for j in range(self.matrix_size[1]):
                x=start_x+i*(cell_size+gap)
                y=start_y+j*(cell_size+gap)
                val=self.game_matrix[i][j]
                if val=="null":
                    bg_color=(200, 190, 180)
                    pygame.draw.rect(screen, bg_color, (x, y, cell_size, cell_size), border_radius=8)
                else:
                    bg_color=(255, 255, 255, 255)




