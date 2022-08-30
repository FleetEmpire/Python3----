from tkinter import *
root = Tk()
v = StringVar()
v.set("女")


def printselect():
    str1 = v.get()
    if str1 == "男":
        print("选项是男孩")
    else:
        print("选项是女孩")


rboy = Radiobutton(root,text = "男孩",variable = v,value = "男",command = printselect).pack()
rgirl = Radiobutton(root,text = "女孩",variable = v ,value = "女",command = printselect).pack()
root.mainloop()