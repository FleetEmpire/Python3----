#引入pygame 和sys
import pygame,sys

#初始化init和设置
pygame.init()
screen = pygame.display.set_mode(size=(200, 300), flags=pygame.RESIZABLE)
pygame.display.set_caption("hello pygame")

#获取事件并响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #刷新屏幕
    pygame.display.update()
