#学生信息管理系统—增删改查操作
stu1 = {"name":"小张","age":10,"gender":"male","grand":"3(1)"}
stu2 = {"name":"小龙","age":13,"gender":"female","grand":"3(2)"}
stu3 = {"name":"小赵","age":12,"gender":"male","grand":"3(4)"}
stu4 = {"name":"小王","age":11,"gender":"female","grand":"3(6)"}
students = [stu1,stu2,stu3,stu4]
while True:
    print("\n\n---------学生信息管理系统----------")
    print("1.增加学生\n2.删除学生\n3.修改学生\n4.查找学生\n5.退出程序")
    num = int(input("请输入您要操作的编号"))
    #1.增加学生
    if num == 1:
        #让用户输入信息
        name = input("请输入要增加的学生的姓名")
        age = int(input("请输入要增加的学生的年龄"))
        gender = input("请输入要增加的学生的性别")
        grand = input("请输入要增加的学生的班级")
        #将学生信息添加到新的字典中
        stu5 = {"name":name,"age":age,"gender":gender,"grand":grand}
        students.append(stu5)
        
        #刷新学生信息（遍历学生信息）
        for stu in students:
            print("-----------")
            for key,value in stu.items():
               print(key,value) 

    #2.删除学生
    elif num == 2:
        print("1.按照序号删除\n2.全部删除")
        choose = int(input("请选择你要的操作"))
        if choose == 1:
             stu_number = int(input("请选择要删除学生的编号"))
             students.pop(stu_number-1)
             print("该学生已经被删除")
             #刷新学生信息（遍历学生信息）
             for stu in students:
                 print("-----------")
                 for key,value in stu.items():
                    print(key,value) 
        
        elif choose == 2:
            yes_no = input("确定要清空所有数据吗？yes/no")
            if yes_no == "yes":
                print("学生数据已经清空")
                students.clear()
        else:
            print("选择有误")


    #3.修改学生信息
    elif num == 3:
        print("当前有"+str(len(students))+"个学生")
        stu_number = int(input("请输入要修改学生的编号"))
        students.pop(stu_number-1)
        #让用户输入信息
        name = input("请输入要修改的学生的姓名")
        age = int(input("请输入要修改的学生的年龄"))
        gender = input("请输入要修改的学生的性别")
        grand = input("请输入要修改的学生的班级")
        #将学生信息添加到新的字典中
        stu5 = {"name":name,"age":age,"gender":gender,"grand":grand}
        students.insert(stu_number-1,stu5)
        #刷新学生信息（遍历学生信息）
        for stu in students:
            print("-----------")
            for key,value in stu.items():
                print(key,value)

    #4.查找学生
    elif num == 4:
        print("当前有"+str(len(students))+"个学生")
        #刷新学生信息（遍历学生信息）
        for stu in students:
            print("-----------")
            for key,value in stu.items():
                print(key,value)

    #5.退出程序
    elif num == 5:
        yes_no = input("您确定要退出吗？yes/no")
        if yes_no == "yes":
            print("程序已关闭！欢迎下次再来")
            break
    else:
        print("您输入有误，请重新输入")
    
