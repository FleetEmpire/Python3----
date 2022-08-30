import requests

url = "https://www.douban.com/"
# 创建session对象
session = requests.session()
# 构造登录所需要的参数
data = {"username": "18221104460", "password": "zxcvbnm123"}
# 提交数据，获取cookie
session.post(url, data)
# 让session再次进行请求
res = session.get(url)
print(res.text)
