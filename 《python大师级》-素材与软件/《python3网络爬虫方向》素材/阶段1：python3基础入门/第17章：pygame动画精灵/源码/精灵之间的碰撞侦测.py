# 引入pygame 和sys
import random

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
        self.rect = self.img.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def moving(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.top < 0 or self.rect.bottom > screen.get_height():
            self.speed[1] = - self.speed[1]
        if self.rect.left < 0 or self.rect.right > screen.get_width():
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
ballgroups = pygame.sprite.Group()
for j in range(3):
    for i in range(3):
        newlocation = [i * 100 + 80, j * 100 + 80]
        newspeed = [random.randint(-2, 4), random.randint(-5, 6)]
        # 创建子类对象
        ball = Balls(filename, newlocation, newspeed)
        ballgroups.add(ball)


def collidedemo(ballgroups):
    pygame.time.delay(10)
    screen.fill(COLOR1)
    for ball in ballgroups:
        ball.moving()
        screen.blit(ball.img, ball.rect)

    for ball in ballgroups:
        ballgroups.remove(ball)
        if pygame.sprite.spritecollide(ball, ballgroups, False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]

        ballgroups.add(ball)

    # 刷新屏幕
    pygame.display.update()


# 获取事件并响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    collidedemo(ballgroups)
