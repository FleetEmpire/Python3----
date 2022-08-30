from tkinter import *

root = Tk()

def click_func(event):
    print(event.x,event.y)

frame = Frame(root,bg = "red",width = 200,height = 300)

frame.bind("<Enter>",click_func)
frame.pack()
root.mainloop()