#类和对象
class Students: #定义学生类
    #定义属性
    name = ""
    age = 0
    gender = ""
    grand = 0
    #定义类的方法
    def learn(self):
        print("学习")
    def play(self):
        print("玩耍")

stu1 = Students()
stu2 = Students()
stu3 = Students()

stu1.name = "小张"
stu1.age = 12
stu1.name = "小王"
stu1.age = 14




print(stu1.name)
print(stu1.age)
stu1.learn()








