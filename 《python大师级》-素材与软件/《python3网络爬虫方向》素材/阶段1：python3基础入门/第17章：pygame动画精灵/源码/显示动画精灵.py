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


# 创建精灵子对象
class Balls(pygame.sprite.Sprite):
    def __init__(self, file_name, location):
        # 初始化父对象
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(filename)
        self.r = self.img.get_rect()
        self.r.left, self.r.top = location


# 定义初始位置
x = 100
y = 100
newlocation = [x, y]

# 创建子类对象
ball01 = Balls(filename, newlocation)

# 获取事件并响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(ball01.img, ball01.r)
    pygame.display.update()
