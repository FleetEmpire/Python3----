from tkinter import *
root = Tk() #创建窗体对象
root.title("你好") #设置窗体标题
root.geometry("300x100") #设置窗体大小
'''
方式1：组件对象[“关键字参数”] = 所要修改的值  注意：中括号中的值是一个字符串类型
方式2：组件对象.config(关键字参数 = 所要修改的值)
'''
def helloButton():
    #button["text"] = "中国人"
    button.config(text = '你好')
button = Button(root,text = 'Hello Button',command = helloButton,
                fg = "red",
                height = 10,
                width = 17,
                font = ("宋体",12)
                )
button.pack()
root.mainloop()