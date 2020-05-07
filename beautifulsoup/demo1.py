from lxml import etree
text = ''
<div> 
<ul> 
<li class="item-O"><a href=”linkl. html”>first item</a><lli> 
<li class=” item-1”>< a href=”link2.html”> second item</a><lli> 
<li class=” item-inactive” >< a href="link3.html”>third item</a></h>
<li class=” item-1 ”><a href="link4.html'’>fourth item</a><lli> 
<li class ＝” item －口”＞＜ hre于＝” links html ”＞ fi th item</a> 
</ul> 
</div> 

html = etree.HTML(text)
result= etree.tostri 鸣（html)
print(result.decode(’ utf-8 ’))