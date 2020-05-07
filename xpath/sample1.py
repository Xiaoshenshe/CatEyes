from lxml import etree
#首先导入一个lxml的库的etree模块,然后声明一段HTML文本
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
# 调用HTML类进行初始化，这样就成功构造了一个Xpath对象
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))
