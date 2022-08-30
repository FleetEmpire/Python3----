from lxml import etree

text = '''
<div>
  <ul>
    <li calss = "item01">这是一个li标签</a></li>
    <li calss = "item02"><a href="https://www.baidu.com/">小张</a></li>
    <li calss = "item03"><a href="https://www.baidu.com/">小王</a></li>
    <li calss = "item04">
        <span>小王</span>
    </li>
  </ul>
</div>
'''
'''
html = etree.HTML(text)  #这个对象是特殊的html
result = etree.tostring(html,encoding="utf-8").decode()
print(result)
'''

html= etree.parse("./test.html",etree.HTMLParser())
result = etree.tostring(html,encoding="utf-8").decode()
print(result)
'''
value_html = html.xpath("//div")
print(value_html)
print(type(value_html))
print(value_html[0])
print(value_html[0].text)
'''
'''
value_html = html.xpath("//div//p")
print(value_html[0])
print(value_html[0].text)
'''
"""
value_html = html.xpath("//div/span[@class='span01']")
print(value_html[0])
print(value_html[0].text)
"""

value_html = html.xpath("//div/span/@class")
print(value_html)

value_html = html.xpath("//a/@href")
print(value_html)

