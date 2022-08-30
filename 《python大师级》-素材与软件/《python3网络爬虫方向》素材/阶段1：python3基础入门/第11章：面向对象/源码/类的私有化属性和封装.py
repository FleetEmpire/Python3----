#类的私有化属性和方法
#定义
class Cards:          
    def __init__(self,account,password,balance):     
        self.account = account
        self.password = password
        self.__balance = balance
    def deposit(self): 
        print("进行存款")
    def getbalance(self,account,password):
        if self.account == account and self.password == password:
            return self.__balance
        else:
            print("密码不正确")

#创建一张有账号密码存款的银行卡对象
c = Cards("acc123","88888","2800")
b = c.getbalance("acc123","88888")
print(b)


































