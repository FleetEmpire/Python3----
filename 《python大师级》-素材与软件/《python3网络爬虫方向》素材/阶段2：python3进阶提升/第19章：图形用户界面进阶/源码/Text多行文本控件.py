from tkinter import *

root = Tk()
# 创建text文本框控件
text1 = Text(root, height=10, width=80)
text1.pack()


# 创建按钮控件
def clickfunc():
    print("你点击我了")


button = Button(root, text="点击我", command=clickfunc)
button.pack()
# 将按钮插入到文本控件中
text1.window_create(INSERT, window=button)
root.mainloop()
