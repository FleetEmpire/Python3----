from tkinter import *
from tkinter.colorchooser import *
root = Tk()

def colorful():
    #调出颜色选项卡对象
    color = askcolor()
    print(color[1])

button = Button(root,text = "点我" ,command = colorful)
button.pack()
root.mainloop()
