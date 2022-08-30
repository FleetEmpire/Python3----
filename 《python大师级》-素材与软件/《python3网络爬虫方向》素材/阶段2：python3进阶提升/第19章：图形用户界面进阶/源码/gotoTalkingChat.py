from tkinter import *
def main():

    # 窗口
    root = Tk()
    root.title('欢迎进入TalkingChat')
    root.geometry('450x400')
    imagefile = PhotoImage(file="py.png")
    info = {}

    #放置标签图片组件
    Label(root,height = 160,image = imagefile).pack()

    #创建2个标签组件
    Label(root, bg = "#FFFFF0",text='用户名:').place(x= 70,y = 170)
    Label(root, bg = "#FFFFF0",text='密   码:').place(x = 70,y = 200)
    #创建2个entry组件
    entry_admin = Entry(root,width = 20)
    entry_admin.place(x = 130,y = 170)
    entry_password = Entry(root,width = 20)
    entry_password.place(x = 130,y = 200)

    def login():
        if  not entry_admin.get() in  info.keys() and not  entry_password.get() in info.values():
            top = Toplevel()
            Label(top,text = "您还未注册").pack()
        #判断如果键和值都在，要判断是否是相对应的值
        if entry_admin.get() in  info.keys() and info[entry_admin.get()]  == entry_password.get():
            top = Toplevel()
            Label(top, text="登录成功").pack()

    #注册账号
    def registerpro():
        #将用户名和密码存储的字典中
        def submit():
            info[entry_ad.get()] = entry_pass.get()
            print(info)
            #关闭窗口
            top.destroy()

        top = Toplevel()
        #两个标签组件
        Label(top, bg="#FFFFF0", text='用户名:').place(x = 0,y = 0)
        Label(top, bg="#FFFFF0", text='密   码:').place(x = 0,y = 20)
        #两个Entry组件
        entry_ad = Entry(top, width=20)
        entry_ad.place(x=50, y=0)
        entry_pass = Entry(top, width=20)
        entry_pass.place(x=50, y=20)
        #创建一个按钮组件
        Button(top,text = "提交",command = submit).place(x = 70,y = 60)

    def exitpro():
        root.quit()

    #创建3个Button组件
    Button(root,text = "登录",command = login).place(x = 90,y = 250)
    Button(root,text = "注册",command = registerpro).place(x = 150,y = 250)
    Button(root,text = "退出",command = exitpro).place(x = 210,y = 250)

    root.mainloop()
if __name__ == '__main__':
    main()

