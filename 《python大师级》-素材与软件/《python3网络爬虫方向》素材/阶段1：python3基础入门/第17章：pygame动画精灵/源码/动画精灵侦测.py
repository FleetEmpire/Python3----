# 引入pygame 和sys
import random

import pygame
import sys

# 初始化init和设置
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("hello pygame")
filename = r"A/ball.png"
# 创建颜色对象
RED = pygame.Color("red")
COLOR1 = (123, 45, 90)

screen.fill(COLOR1)


# 创建一个球的类
class Myballs(pygame.sprite.Sprite):
    # 设置类的属性
    def __init__(self, file_name, location, speed):
        # 初始化父类对象
        pygame.sprite.Sprite.__init__(self)
        # 初始化子类对象
        self.image = pygame.image.load(file_name)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.top < 0 or self.rect.bottom > screen.get_height():
            self.speed[1] = -self.speed[1]
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
        ball = Myballs(filename, newlocation, newspeed)
        ballgroups.add(ball)


# 创建碰撞的方法
def collide_demo(sprite_group):
    screen.fill(COLOR1)
    for ball in sprite_group:
        ball.move()
        screen.blit(ball.image, ball.rect)
        pygame.time.delay(3)

    for ball in sprite_group:
        sprite_group.remove(ball)  # 首先把自己排除
        if pygame.sprite.spritecollide(ball, sprite_group, False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
        sprite_group.add(ball)
        # collide_demo(sprite_group)
    pygame.display.flip()  # 显示pygame中所有的内容


# 获取事件并响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    collide_demo(ballgroups)
