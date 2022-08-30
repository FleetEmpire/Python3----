# 引入pygame 和sys
import random
import time

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


# 创建精灵子对象
class Balls(pygame.sprite.Sprite):
    def __init__(self, file_name, location, speed):
        # 初始化父对象
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(filename)
        self.r = self.img.get_rect()
        self.r.left, self.r.top = location
        self.speed = speed

    def moving(self):
        self.r = self.r.move(self.speed)
        if self.r.top < 0 or self.r.bottom > screen.get_height():
            self.speed[1] = - self.speed[1]
        if self.r.left < 0 or self.r.right > screen.get_width():
            self.speed[0] = -self.speed[0]


# 速度
x_speed = 2
y_speed = 1
newspeed = [x_speed, y_speed]

# 定义初始位置
x = 100
y = 100
newlocation = [x, y]

# 将多个精灵加入列表
ballgroups = []
for j in range(3):
    for i in range(3):
        newlocation = [i * 100 + 80, j * 100 + 80]
        newspeed = [random.randint(-2, 4), random.randint(-5, 6)]
        # 创建子类对象
        ball = Balls(filename, newlocation, newspeed)
        ballgroups.append(ball)

# 获取事件并响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    time.sleep(0.009)
    screen.fill(COLOR1)
    for ball in ballgroups:
        ball.moving()
        screen.blit(ball.img, ball.r)
    # 刷新屏幕
    pygame.display.update()
