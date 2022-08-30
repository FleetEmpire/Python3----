from tkinter import *
root = Tk()
scale = Scale(root,
              from_ = 0,
              to = 20,
              troughcolor = "red",
              width = "30",
              tickinterval = 2,
              label = "我的刻度尺",
              length = 300,
              orient = HORIZONTAL,
              resolution = 2




              ).pack()
root.mainloop()