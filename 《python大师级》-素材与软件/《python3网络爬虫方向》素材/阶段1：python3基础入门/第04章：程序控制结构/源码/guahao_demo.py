#后台卡数据
card_num = 454545  #后台账号
password = 123    #后台密码
print("--------------欢迎使用自助服务终端------------")
in_card_num = int(input("请您输入就诊卡号"))
in_password = int(input("请您输入就诊卡密码"))

if in_card_num == card_num and in_password == password:
    print("""
您可以进行如下操作：
        1、存款      2、挂号
        3、查询余额  4、退出操作
    """
    )
    choice = input("请选择您要进行的操作:")
    if choice == "1":
        money = int(input("请输入您存款的金额"))
        print("\n您本次存入的金额为：",money)
    elif choice == "2":
        print("""
         您可以选择一下科室进行挂号：
                      1、皮肤科；        2、内分泌科；
                      3、口腔科；        4、骨科；  5、其他科室
        """)
        number = input("请输入您要挂的科室：")
        if number == "1":
            print("-------------------")
            print("账号为："+str(card_num)+"的用户您好！\n您已成功预约皮肤科")
        elif number == "2":
            print("-------------------")
            print("账号为："+str(card_num)+"的用户您好！\n您已成功挂预约分泌科")
        elif number == "3":
            print("-------------------")
            print("账号为："+str(card_num)+"的用户您好！\n您已成功预约口腔科")
        elif number == "4":
            print("-------------------")
            print("账号为："+str(card_num)+"的用户您好！\n您已成功预约骨科")
        else:
            print("-------------------")
            print("账号为："+str(card_num)+"的用户您好！\n您已成功预约其他科室")
    elif choice == "3":
        print("您当前的余额为：1223")
    else:
        print("请您收好卡片")
else:
   print("用户名密码输入错误****，请重新输入...") 


