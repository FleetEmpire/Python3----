#定义动物类
class Animal:
    
    def __init__(self,gender,color):
        self.gender = gender
        self.color = color
        
    def eat(self):
        print("动物们要吃饭了")

    def play(self):
        print("动物们特别喜欢玩耍")

#定义猫类并继承父类
class Cat(Animal):
    pass
#实例化对象
bosi = Cat("母","gray")
print(bosi.gender)
bosi.eat()








































