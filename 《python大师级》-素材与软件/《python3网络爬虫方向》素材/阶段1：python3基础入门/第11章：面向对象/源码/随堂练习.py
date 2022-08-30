#定义Person类
class Person:
    
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
      
    def personInfo(self): 
        print("姓名:"+self.name+"  年龄:"+str(self.age)
               +"  性别："+self.gender)


#定义农民类并继承Person
class Farmers(Person):
    def __init__(self,job,place):
        self.job = job
        self.place = place
    def personInfo(self):
        print("我是农民我的工作是:"+self.job+
               "\n我工作的地点是:"+self.place)

#定义科学家类并继承Person
class Scientists(Person):
        
    def inventionMechanical(self): 
        print("袁隆平发明了杂交水稻")


f = Farmers("种地","在中国大地")
f.personInfo()
s = Scientists("袁隆平",88,"男")
s.personInfo()
s.inventionMechanical()
