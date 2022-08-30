# 引入pygame 和sys
import pygame
import sys

# 初始化init和设置
pygame.init()
screen = pygame.display.set_mode(size=(800, 600), flags=pygame.RESIZABLE)
pygame.display.set_caption("hello pygame")

# 创建颜色对象
RED = pygame.Color("red")
COLOR1 = (123, 45, 90)
filename = r"A/ball.png"

# 获取事件并响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    img = pygame.image.load(filename)
    screen.blit(img, (100, 100))
    pygame.display.update()
