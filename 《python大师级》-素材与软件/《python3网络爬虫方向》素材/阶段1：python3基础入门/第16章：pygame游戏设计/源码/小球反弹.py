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

x = 100
y = 100
x_bujin = 1
y_bujin = 2


# 反弹函数
def fantan():
    global x, y, x_bujin, y_bujin
    screen.fill(COLOR1)
    x += x_bujin
    y += y_bujin

    if x > screen.get_width() or x < 0:
        x_bujin = -x_bujin
    if y > screen.get_height() or y < 0:
        y_bujin = -y_bujin

    screen.blit(img, [x, y])
    pygame.display.update()


# 获取事件并响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fantan()
