from tkinter import *
root = Tk()

root.title("你好")
root.geometry("220x500")
color = "#DC143C"

def change_color(source):
    r = r_scale.get()
    g = g_scale.get()
    b = b_scale.get()
    color = "#%02x%02x%02x"%(r,g,b)
    print(color)
    frame.config(bg = color)


r_scale = Scale(root,from_ = 0,to = 255,tickinterval = 50,
                label = "red",length = 200,orient = HORIZONTAL,command = change_color)
g_scale = Scale(root,from_ = 0,to = 255,tickinterval = 50,
                label = "green",length = 200,orient = HORIZONTAL,command = change_color)
b_scale = Scale(root,from_ = 0,to = 255,tickinterval = 50,
                label = "blue",length = 200,orient = HORIZONTAL,command = change_color)
scales = [r_scale,g_scale,b_scale]
for i in range(len(scales)):
    scales[i].grid(row = i+1,column = 0)

frame = Frame(root,bg = color,height = 100,width = 100)
frame.grid(row = 4,column = 0)


root.mainloop()