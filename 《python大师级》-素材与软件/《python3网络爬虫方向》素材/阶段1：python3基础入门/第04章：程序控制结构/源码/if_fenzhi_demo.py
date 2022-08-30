#if单分支结构
'''
1、编写一个程序：如果你高数成绩在90分以上，就可以获得奖学金。
2、获取用户输入的身高，然后判断如果你的身高在180cm以上，就给出一个提示，你可以进篮球队。

math = 10
if math >= 90:
    print("获得奖学金")

height = int(input("请输入您的身高"))
if height >= 180:
    print("你可以进入篮球队")
'''
#if双分支结构
'''
1、编写一个程序：获取用户输入的数字，并判断这个数字是偶数还是奇数。

num = int(input("请输入任意一个数字"))
if num%2 == 0:
    print("数字"+str(num)+"是偶数")
else:
    print("数字"+str(num)+"是奇数")

num = int(input("请输入任意一个数字"))
if num%2 == 0:
    print("数字"+str(num)+"是偶数")

if num%2 == 1:
    print("数字"+str(num)+"是奇数")
'''

#if多分支结构
'''
案例：如果你的成绩高于90分，奖励一台笔记本电脑；
如果你的成绩高于80分，奖励一套python学习教程；
如果你的成绩高于70分，奖励一支笔；否则你就要
重做试卷。（这是我们生活中常用的自然语言描述的）
首先一定要理清它所在的存在的逻辑关系。
'''

score = int(input("请输入你的成绩"))
if score >= 90:
    print("奖励笔记本")
else:
    if score >= 80:
        print("奖励python学习教程")
    else:
        if score >= 70:
            print("奖励一支笔")
        else:
            print("重做试卷")


score = int(input("请输入你的成绩"))
if score >= 90:
    print("奖励笔记本")
elif score >= 80:
    print("奖励python学习教程")
elif score >= 70:
    print("奖励一支笔")
else:
    print("重做试卷")

'''
score = int(input("请输入你的成绩"))
if 条件1:
    #代码块
elif 条件2:
    #代码块
elif 条件3:
    #代码块
else:
    #代码块
'''




















