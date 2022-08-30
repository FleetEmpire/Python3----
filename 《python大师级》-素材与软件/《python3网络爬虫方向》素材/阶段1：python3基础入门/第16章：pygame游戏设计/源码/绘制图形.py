#引入pygame 和sys
import pygame,sys

#初始化init和设置
pygame.init()
screen = pygame.display.set_mode(size=(400, 800), flags=pygame.RESIZABLE)
pygame.display.set_caption("hello pygame")

RED = (23,59,200)
BLUE = pygame.Color("blue")
COLORS = pygame.Color("#000000")

#获取事件并响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    
    pygame.draw.circle(screen,RED,(100,100),100,10) 
    #刷新屏幕
    pygame.display.update()




