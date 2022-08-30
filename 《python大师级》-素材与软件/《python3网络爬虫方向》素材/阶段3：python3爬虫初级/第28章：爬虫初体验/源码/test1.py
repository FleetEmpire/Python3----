import random
import re
import urllib.request

url = r"http://fanyi.youdao.com/"

ug1 = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"
ug2 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
ug3 = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
ug4 = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
ug5 = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
ulist = [ug1,ug2,ug3,ug4,ug5]
ug = random.choice(ulist)
header = {"User-Agent":ug}
#返回请求对象
urr = urllib.request.Request(url,headers = header)

#response = opener.open(urr).read().decode()
#定义opener为全局
urllib.request.install_opener(opener)
response = urllib.request.urlopen(urr).read().decode()


print(response)
str = r"<title>(.*?)</title>"
str1 = re.findall(str,response)
print(str1)
