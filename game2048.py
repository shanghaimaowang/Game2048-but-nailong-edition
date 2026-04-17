import random
import pygame
from get_number_background import get_number_background



class ezfe:
    #初始化棋盘
    def __init__(self,matrix_size=(4,4),max_score_filepath : int=None,**kwargs):
        self.move_direction = None
        self.source=0
        self.matrix_size=matrix_size
        self.max_score_filepath=max_score_filepath
        #self.initialize()
        #初始化方格都为null
        self.game_matrix=[["null"for _ in range(self.matrix_size[1])]
                          for _ in range(self.matrix_size[0])]

    def randomgenerateNumber(self):
        empty_pos=[]
        for i in range(self.matrix_size[0]):
            for j in range(self.matrix_size[1]):
                if self.game_matrix[i][j]=="null":
                    empty_pos.append([i,j])
        if len(empty_pos)==0:return
        empty=random.choice(empty_pos)
        i=empty[0]
        j=empty[1]
        self.game_matrix[i][j]=2 if random.random()>0.1 else 4


    def draw_rect(self,screen):
        cell_size=104
        gap=2
        start_x=0
        start_y=0
        #测试格子打印效果
        # self.game_matrix[0][0]=2048
        for i in range(self.matrix_size[0]):
            for j in range(self.matrix_size[1]):
                x=start_x+i*(cell_size+gap)
                y=start_y+j*(cell_size+gap)
                val=self.game_matrix[i][j]
                if val=="null":
                    bg_color=(200, 190, 180,125)
                    pygame.draw.rect(screen, bg_color, (x, y, cell_size, cell_size), border_radius=8)
                else:
                    num_background=get_number_background().get_number_background(val)
                    mask=pygame.Surface((104,104),pygame.SRCALPHA)
                    pygame.draw.rect(mask,(255,255,255),(0,0,104,104),border_radius=8)
                    if val<100:
                        sizeo=80
                    elif val>=100 and val<1000:
                        sizeo=60
                    else:
                        sizeo=55
                    num=pygame.font.SysFont("kaiti", size=int(sizeo))
                    num=num.render(str(val),True,(51, 51, 51))
                    num_rect=pygame.Rect(x,y,cell_size,cell_size)
                    temp=num.get_rect(center=num_rect.center)

                    screen.blit(num_background,(x,y))
                    screen.blit(mask,(x,y),special_flags=pygame.BLEND_RGBA_MIN)
                    screen.blit(num,temp)

    def set_direction(self,direction):
        self.move_direction=direction

    def move(self):
        def extract(array):
            array_new=[]
            for i in array:
                if i!='null':array_new.append(i)
            return array_new

        # def merge(array):
        #     source=0
        #     if len(array)<2:return array,source
        #     for i in range(len(array)-1):
        #         if array[i]==array[i+1]:
        #             array[i]*=2
        #             array.pop(i+1)
        #             array.append('null')
        #             if isinstance(array[i], int):source+=array[i]
        #     return array,source

        def merge(array):
            """
            对已去除 'null' 的纯数字列表进行合并，返回合并后的列表（不含 'null'）及本次得分。
            """
            if len(array) < 2:
                return array, 0

            merged = []
            score = 0
            i = 0
            while i < len(array):
                if i < len(array) - 1 and array[i] == array[i + 1]:
                    merged.append(array[i] * 2)
                    score += array[i] * 2
                    i += 2  # 跳过下一个元素
                else:
                    merged.append(array[i])
                    i += 1
            return merged, score

        if self.move_direction is None:return
        elif self.move_direction=='left':
            for j in range(self.matrix_size[1]):
                col_=[]
                for i in range(self.matrix_size[0]):
                    col_.append(self.game_matrix[i][j])
                col_=extract(col_)
                col_,source_t=merge(col_)
                self.source+=source_t
                col_=col_+['null',]*(self.matrix_size[0]-len(col_))
                for i in range(self.matrix_size[0]):
                    self.game_matrix[i][j]=col_[i]

        elif self.move_direction=='right':
            for j in range(self.matrix_size[0]):
                col_=[]
                for i in range(self.matrix_size[1]):
                    col_.append(self.game_matrix[i][j])
                col_=extract(col_)
                col_.reverse()
                col_,source_t=merge(col_)
                self.source+=source_t
                col_=col_+['null',]*(self.matrix_size[0]-len(col_))
                col_.reverse()
                for i in range(self.matrix_size[0]):
                    self.game_matrix[i][j]=col_[i]

        elif self.move_direction=='up':
            for i in range(self.matrix_size[0]):
                col_=[]
                for j in range(self.matrix_size[1]):
                    col_.append(self.game_matrix[i][j])
                col_=extract(col_)
                col_, source_t=merge(col_)
                self.source+=source_t
                col_=col_+['null',]*(self.matrix_size[0]-len(col_))
                for j in range(self.matrix_size[0]):
                    self.game_matrix[i][j]=col_[j]

        elif self.move_direction=='down':
            for i in range(self.matrix_size[0]):
                col_=[]
                for j in range(self.matrix_size[1]):
                    col_.append(self.game_matrix[i][j])
                col_=extract(col_)
                col_.reverse()
                col_,source_t=merge(col_)
                self.source+=source_t
                col_=col_+['null',]*(self.matrix_size[0]-len(col_))
                col_.reverse()
                for j in range(self.matrix_size[0]):
                    self.game_matrix[i][j]=col_[j]

