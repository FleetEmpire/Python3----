import pygame,sys
from random import *

size = [1000,800]
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
#创建一个球的类
class myball(pygame.sprite.Sprite):
    #设置类的属性
    def __init__(self, file_name,location,speed):
        #初始化父类对象
       pygame.sprite.Sprite.__init__(self)
        #初始化子类对象
       self.image = pygame.image.load(file_name)
       self.rect = self.image.get_rect()
       self.rect.left,self.rect.top = location
       self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.top < 0 or self.rect.bottom > screen.get_height():
            self.speed[1] = -self.speed[1]
        if self.rect.left< 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]
images = [r"./A/bubble1.png","./A/bubble2.png","./A/bubble3.png","./A/bubble4.png"]
flag = 0
#首选创建多个角色
balls = pygame.sprite.Group()
for row in range(0,2):
    for column in range(0,2):
        location = [column*200+20,row*200+20]
        speed = [choice([-6,6]),choice([-10,15])]
        newball = myball(images[flag],location,speed)  
        balls.add(newball)
        flag += 1
#创建碰撞的方法
def collide_demo(sprite_group):
    screen.fill([0,0,0])
    for ball in sprite_group:
        ball.move()
        screen.blit(ball.image,ball.rect)
        pygame.time.delay(20)
       
    for ball in sprite_group:
        sprite_group.remove(ball)#首先把自己排除
        if pygame.sprite.spritecollide(ball,balls,False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
        sprite_group.add(ball)
        #collide_demo(sprite_group)
    pygame.display.flip()#显示pygame中所有的内容

    
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
           size = [event.size[0],event.size[1] ]
           screen = pygame.display.set_mode(size,pygame.RESIZABLE)
    collide_demo(balls)
    






    
  
        



