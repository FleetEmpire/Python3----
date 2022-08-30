from tkinter import *
root = Tk()

#建立上层框架
f_upper = Frame(root,bg = "#FF1493")
f_upper.pack()

button1 = Button(f_upper,text = "按钮1").pack(side = LEFT,padx = 4,pady =4)
button2 = Button(f_upper,text = "按钮2").pack(side = LEFT,padx = 4,pady =4)

#建立下层框架
f_lower = Frame(root,bg = "#87CEEB")
f_lower.pack()

label1 = Label(f_lower,text = "标签1").pack()
label2 = Label(f_lower,text = "标签2").pack()
root.mainloop()