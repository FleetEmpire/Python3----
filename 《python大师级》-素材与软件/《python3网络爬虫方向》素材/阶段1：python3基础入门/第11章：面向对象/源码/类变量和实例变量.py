class Students:  #定义学生类
     gender = "male"

    #初始化属性
     def __init__(self,name,age,grand):
                   self.name = name
                   self.age = age
                   self.grand = grand
     #定义普通（函数）方法
     def learn(self):
         print("我经常去图书馆学习")
     def play(self):
         print("我周末喜欢去公园玩耍")

stu1 = Students ("小明",12,6)
stu2 = Students ("小亮",11,5)
stu1.gender = "female"
print(stu1.name,stu1.age,stu1.grand)                             
print(stu2.name,stu2.age,stu2.grand)                           
print(stu1.gender)                                                                   
print(stu2.gender)






















