#字典嵌套


#1、嵌套—将字典存储在列表中
'''
stu1 = {"phoneno":12345455,"idcard":132332434,"gender":"男","height":175}
stu2 = {"phoneno":1232455,"idcard":3545434,"gender":"女","height":145}
stu3 = {"phoneno":1232335,"idcard":132334,"gender":"女","height":155}
person = [stu1,stu2,stu3]
for stu in person:
    for key,value in stu.items():
        #print(key,value)
'''
#2、嵌套—将字典存储在字典中
stu1 = {"phoneno":12345455,"idcard":132332434,"gender":"男","height":175}
stu2 = {"phoneno":1232455,"idcard":3545434,"gender":"女","height":145}
stu3 = {"phoneno":1232335,"idcard":132334,"gender":"女","height":155}
person = {"stu1":stu1,"stu2":stu2,"stu3":stu3}
for value_stu in person.values():
    for key,value in value_stu.items():
        print(key,value)
