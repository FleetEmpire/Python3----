#构造函数
class Students:
    #初始化属性
    def __init__(self,name,age,gender,grand):
        self.name = name
        self.age = age
        self.gender = gender
        self.grand = grand
  
    #定义方法
    def learn(self):
        print("我喜欢学习")

stu1 = Students("小王",12,"男",3)
print(stu1.age)
stu1.learn()

