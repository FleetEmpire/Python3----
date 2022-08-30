import random
import time
import urllib.parse
import urllib.request


ugList = ["Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
          "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
          "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11"]

header = {"User-Agent":random.choice(ugList)}
#print(header)


def loadpage(allurl):
    print("正在下载-----")
    urr = urllib.request.Request(allurl,headers = header)
    response = urllib.request.urlopen(urr).read()
    return response


def savepage(html, fileName):
    print("正在保存-----")
    f = open(fileName,"wb")
    f.write(html)
    f.close()


def getallurl(url,keyvaule,starpage,endpage):
    for i in range(starpage, endpage + 1):
        allurl = url+keyvaule+"&pn="+str((i-1)*50)
        #定义输出文件的路径
        fileName = r"./百度贴吧//"+"第"+str(i)+"页爬虫.html"
        #loadpage函数下载网页
        html = loadpage(allurl)
        savepage(html,fileName)




#程序执行的入口
if __name__=="__main__":
    kw = input("请输入贴吧")
    starpage = int(input("请输入起始页码"))
    endpage = int(input("请输入终止页码"))
    url = "http://tieba.baidu.com/f?"
    keyvaule = urllib.parse.urlencode({"kw":kw})
    getallurl(url,keyvaule,starpage,endpage)
    time.sleep(10)



