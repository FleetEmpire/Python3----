from tkinter import *
root = Tk()
Label(root,text = "选择你喜欢的食物").grid(row = 1)

#创建食物的字典
food = {0:"蛋炒饭",1:"红烧肉",2:"盖浇饭",3:"油泼面",4:"烧烤",5:"大盘鸡",6:"清蒸鱼"}

selects = {}
#以此创建Checbutton对象。
for i in range(len(food)):
    selects[i] = BooleanVar()
    Checkbutton(root,text = food[i],variable = selects[i]).grid(row = i+2)


def selectfunc():
     for key ,value in selects.items():
        if value.get() == True:
            print(food[key])

Button(root,text = "提交",command = selectfunc).grid(row = len(food)+2)


root.mainloop()