from tkinter import *
root = Tk()
sv = StringVar()
sv.set("sdfsdfdsf")
entry = Entry(root,text = 'input your text here',textvariable = sv ,width = 9)
entry.pack()


def func1():
    entry.select_range(0,5)


Button(root,text = "点我",command = func1).pack()
root.mainloop()
