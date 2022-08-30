import random

import requests
#https://zhengzhou.anjuke.com/?
ugList = ["Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
          "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
          "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11"]

header = {"User-Agent":random.choice(ugList)}
wd = {"wd":"和润林湖美景"}
r = requests.get("https://zhengzhou.anjuke.com/?",params = wd,headers = header)
try:
    print(r.text)
except ConnectionError:
    print("停止输出")
