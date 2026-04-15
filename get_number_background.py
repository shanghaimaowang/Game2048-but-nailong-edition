import pygame

class get_number_background:

     def get_number_background(self,value):
          if value== 2:
               number2 = pygame.image.load("number_image/2.png")
               number2 = pygame.transform.scale(number2, (100, 100))
               return number2
          elif value==4:
               number4 = pygame.image.load("number_image/4.png")
               number4 = pygame.transform.scale(number4, (100, 100))
               return number4
          elif value==8:
            number8 = pygame.image.load("number_image/8.png")
            number8 = pygame.transform.scale(number8, (100, 100))
            return number8
          elif value==16:
                number16 = pygame.image.load("number_image/16.png")
                number16 = pygame.transform.scale(number16, (100, 100))
                return number16
          elif value==32:
                number32 = pygame.image.load("number_image/32.png")
                number32 = pygame.transform.scale(number32, (100, 100))
                return number32
          elif value==64:
                number64 = pygame.image.load("number_image/64.png")
                number64 = pygame.transform.scale(number64, (100, 100))
                return number64
          elif value==128:
                number128 = pygame.image.load("number_image/128.png")
                number128 = pygame.transform.scale(number128, (100, 100))
                return number128
          elif value==256:
                number256 = pygame.image.load("number_image/256.png")
                number256 = pygame.transform.scale(number256, (100, 100))
                return number256
          elif value==512:
                number512 = pygame.image.load("number_image/512.png")
                number512 = pygame.transform.scale(number512, (100, 100))
                return number512
          elif value==1024:
                number1024 = pygame.image.load("number_image/1024.png")
                number1024 = pygame.transform.scale(number1024, (100, 100))
                return number1024
          elif value==2048:
                number2048 = pygame.image.load("number_image/2048.png")
                number2048 = pygame.transform.scale(number2048, (100, 100))
                return number2048
          else:return None

