import re
'''
\d 表示0-9的数字，只匹配一个
match是从前往后进行匹配，如果刚开始匹配不成，
后面就不在匹配，直接返回None
'''

'''
result = re.match(r"\d","2python")
print(result)

result = re.match(r"\d","python2")
print(result)
'''

'''
[12345678] 表示任选其中1个元素
[1-8]表示1到8任选其中1个元素
[1-35-8]表示1到3,5到8任选1个元素
'''
'''
result = re.match(r"[12345678]","2python")
print(result)

result = re.match(r"[1-35-8]","4python")
print(result)
'''
'''
[a-z] a到z的小写字母任选一个元素
[A-Z] A到Z的大写字母任选一个元素
[1-35-8a-zA-Z] 1到3 5到8 a到z A到Z
任选其中一个元素
.匹配任意单字符（除了\n）

'''
'''

result = re.match(r"[a-z]","python2")
print(result)

result = re.match(r"[1-35-8a-zA-Z]","3python")
print(result)
'''

'''

\w  可以匹配数字、字母、下划线、希腊字母、俄文字母等
\s  匹配空白字符（空格、table键）

所有使用大写字母表示的都是相反的
\W  \S   \D
'''
'''
result = re.match(r"\w","python2")
print(result)

result = re.match(r"\s","   3python")
print(result)
'''
'''
{}表示限定的位数,可与单字符组合使用
{4}表示限定4位
{1,3}表示1到3位

\d{1,2}表示可以匹配1-2位数字
\d{1,5}表示可以匹配1-5位数字
\d{11}表示可以匹配11位

[1-57-9]{1,2}表示匹配1到5 7到9数字1到2位
[1-9a-zA-Z]{6}表示匹配数字和字母 6位

'''
'''
result = re.match(r"\d{1,2}","3python")
print(result)

result = re.match(r"[1-9a-zA-Z]{6}","3python")
print(result)
'''
'''
匹配手机号:首位是0371固定的，-可写可不写
尾号是8位数字，0371-45585522
?号表示它前面一位可有可无
'''
'''
num = input("请输入电话号")
result = re.match(r"0371-?\d{8}",num)
if result:
    print("匹配成功")
else:
    print("匹配不成功！")
'''
'''
{} * +表示的都是限定位数
{}里面
*表示至少有0个
+ 表示至少有1个  表示字符的个数

.*  表示匹配至少0个除\n以外的符号
.+ 表示匹配至少1个除\n以外的符号
[a-zA-Z_]+ 表示至少有1位大小写字母
[a-zA-Z0-9_]*  表示至少有0位大小写字母和数字



^ 表示以谁开头开头
$  表示以谁结尾

^\d+ 表示以数字开头
^[a-zA-Z_]  表示以字母当做开头
[a-zA-Z_]*$ 表示从前到后都必须是字母

'''
'''
result = re.match(r"[a-zA-Z_]+","python")
print(result)

result = re.match(r"[a-zA-Z0-9_]*","3python")
print(result)

result = re.match(r"^[a-zA-Z_]","python3")
print(result)

result = re.match(r"[a-zA-Z_]*$","python_abc")
print(result)
'''
'''
1.判断变量的名称:由数字、字母、下划线组成，不能以数字作为开头
[a-zA-Z_][a-zA-Z0-9_]*$


2.判断4-20位163邮箱格式
[a-zA-Z0-9_]{4,20}@163\.com$


3.判断163邮箱、126邮箱
[a-zA-Z0-9_]{4,20}@(163|126)\.com$
'''
'''
result = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*$","1name")
print(result)


result = re.match(r"[a-zA-Z0-9_]{4,20}@163\.com$","1name@163.com")
print(result)

result = re.match(r"[a-zA-Z0-9_]{4,20}@(163|126)\.com$","1name@126.com")
print(result)
'''
'''
#1.匹配: <h1>sdfsdfg</h1>

str = "<h1>python01</h1>"
result = re.match(r"<\w*>.*</\w*>",str)
print(result)

#<>和/括号还用他们自身匹配。
#\w可以匹配数字、字母、下划线、希腊字母、俄文字母等
#*表示至少有0个
#.匹配任意单字符（除了\n）
'''
'''
#2.匹配: <h1>sdfsdfg</h1>

str = "<h1>python01</h1>"
result = re.match(r"<(\w*)>.*</\1>",str)
print(result)

'''
'''
#3.匹配: <body> <h1>sdfsdfg</h1></body>

str = "<body><h1>sdfsdfg</h1></body>"
result = re.match(r"<(\w*)><(\w*)>.*</\2></\1>",str)
print(result)
'''

'''
#4.匹配: <body> <h1>sdfsdfg</h1></body>

str = "<body><h1>sdfsdfg</h1></body>"
result = re.match(r"<(?P<n1>\w*)><(?P<n2>\w*)>.*</(?P=n2)></(?P=n1)>",str)
print(result)

?P<n1>  表示给组设置变量名 ，将其定义在组内
(?P=n1)   使用变量
只不过是把组当做一个变量，然后在使用这个变量

'''
'''
match
是从头匹配，如果刚开始匹配不成，就无法在进行匹配了；

result = re.match(r"[a-zA-Z_]","好name")
print(result)
'''

'''
search
寻找，只要字符串中有满足正则表达式就算匹配成功；
匹配的顺序是从左往右开始

result = re.search(r"[a-zA-Z_]","好name名字a")
print(result)
'''
'''
findall
找到所有满足正则的数据，返回一个列表；

result = re.findall(r"[a-zA-Z_]","好name名字a")
print(result)
'''



'''
sub
根据正则匹配成功之后，在进行替换，可以替换很多个


result = re.sub(r"[a-zA-Z_]","a","好name名字a")
print(result)
'''































