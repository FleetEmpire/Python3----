# 引入pygame 和sys
import pygame
import sys

# 初始化init和设置
pygame.init()
screen = pygame.display.set_mode(size=(800, 600), flags=pygame.RESIZABLE)
pygame.display.set_caption("hello pygame")
filename = r"A/ball.png"
# 创建颜色对象
RED = pygame.Color("red")
COLOR1 = (123, 45, 90)

screen.fill(COLOR1)
img = pygame.image.load(filename)

# 定义移动的函数
x = 100
y = 100
x_bujin = 0.08
y_bujin = 0.02


def move():
    global x, y
    x += x_bujin
    y += y_bujin
    screen.fill(COLOR1)
    screen.blit(img, (x, y))


# 获取事件并响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    move()

    pygame.display.update()
