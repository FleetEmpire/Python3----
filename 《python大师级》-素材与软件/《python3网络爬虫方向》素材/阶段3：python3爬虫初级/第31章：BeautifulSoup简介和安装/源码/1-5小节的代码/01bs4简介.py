from bs4 import BeautifulSoup
import re

py_str_html = """
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title class="title_one">这是一个python简介</title>
</head>
<body>
    <p id="p_id" class="title1" name="pythonjieshao"><b>python爬虫简介</b></p>
    <p class="jianjie" >python是一种非常好用的语言，很多人都用他
        <a href="https://www.zhihu.com/question/20799742" class="jieshao1" id="pylink1">知乎python</a>
        <a href="https://jingyan.baidu.com/article/48a42057310a64a92425041b.html" class="jieshao2" id="pylink2">百度python</a>
        <a href="https://www.jianshu.com/p/c380f4d3e6cd" class="jieshao3" id="pylink3">简书python</a>
    <div class="title1"></div>

    </p>

</body>
</html>
"""
#案例1：解析字符串形式html
soup = BeautifulSoup(py_str_html,"lxml")
#print(soup)
#案例2：解析本地html,需要说明是utf-8,这是国际标准，gbk是国家标准。
#soup = BeautifulSoup(open("测试html.html", encoding='UTF-8'))
# 在一定范围内纠正html语法
#print(soup)
#格式化输出html对象
print(soup.prettify())
#1.根据标签名获取标签对象，
print(soup.title)
#1.1 如何获取标签的信息
print(soup.title.string)
#1.2 如何获取标签的名字
print(soup.title.name)
#1.3 如何获取第1个标签的属性:获取title标签中所有的属性
print(soup.title.attrs)
#2.1 默认获取body下的第1个子标签(子标签对象)
print("-------------------------")
print(soup.body.p)

#2.1.2 获取body下的第1个子标签(子标签对象),结果是生成器，需遍历显示
for i in soup.body.p.descendants:
    print(i)
print("==================================")
#1.根据标签名搜索一类标签
#返回的是类型是：bs4.element.Tag,bs4包下特有的结果集，里面装的是标签对象。
data_tags = soup.find_all("p")
for tag in data_tags:
    print(tag.attrs)
"""
重要总结：<标签名 属性>值</p>,标签是由3部分构成：
标签值、标签名 、标签属性组成 
1.标签对象调用string：表示获取标签中的值
2.标签对象调用name：表示获取标签名
3.标签对象调用attrs：表示获取标签属性
我们可以通过标签树获取标签的全部。
"""
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
#2.根据正则表达式，搜索符合要求的标签
data_tags = soup.find_all(re.compile("^b"))  #表示以b字母开头的标签提出到结果集中
print(data_tags)
for tag in data_tags:
    print(tag.name)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
#3.根据属性查找标签：id属性、class属性等,返回的也是标签对象
#data_tags = soup.find_all(id="p_id")
#data_tags = soup.find_all(class_ = "title1")#表示以b字母开头的标签提出到结果集中
data_tags = soup.find_all(name = "p",attrs = {"class":"title1"})
print(data_tags)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
#4.根据内容查找对应标签值
#字符串含有python的，都会获取到。这个用处 比较大
data_tags = soup.find_all(text=re.compile("python"))  #表示以b字母开头的标签提出到结果集中
print(data_tags)



