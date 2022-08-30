from tkinter import *
root = Tk()
Label(root,text = "选择你喜欢的人物角色").pack()
persons = {0:"孙悟空",1:"猪八戒",2:"唐玄奘",3:"沙和尚",4:"白龙马"}
v = IntVar() #选项按钮绑定的变量
v.set(0) #默认选择变量为0的组件。


def printselect():
    print(persons[v.get()])


for key,value in persons.items():
    Radiobutton(root,text =value,variable = v,value = key,
                command = printselect,indicatoron = 0,width = 30).pack()
root.mainloop()