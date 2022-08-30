from datetime import datetime
import time

dd = datetime(2009, 12, 23, hour=12, minute=23, second=45)
print(dd)

dt = datetime.today()
print(dt)
print(time.time())
df = datetime.fromtimestamp(time.time())
print(df)

dn = datetime.now()
print(dn)

du = datetime.utcnow()
print(du)

print(dn.date())
print(dn.time())
dc = datetime.combine(dn.date(), dn.time(), tzinfo=dn.tzinfo)
print(dc)
"""
共同点：都是将日期字符串转换成datetime类型

不同点：

fromisoformat里面的date_string格式必须符合yyyy-MM-dd HH:MM:SS.ffffff否则会报错。
比如datetime.fromisoformat('2019-11-08 22:01')就可以，但是datetime.fromisoformat('20191108 22:01')就会报错。

strptime是只要date_string和后面的format一致就行，
比如datetime.strptime('2019-11-08','%Y-%m-%d')和datetime.strptime('20191108','%Y%m%d')都可以，但是和datetime.striptime('2019-11-08','%Y%m%d')就会报错。
"""
df = datetime.fromisoformat('2019-11-08 22:01')
print(df)
ds = datetime.strptime('2019年11月08','%Y年%m月%d')
print(ds)


dns = dn.strftime('%y年%m月%d日')
print(dns)











