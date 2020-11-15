import requests
from bs4 import BeautifulSoup
import re

def getHTML(page):
#如果不修改header，京东的反机器人系统会判定不给访问权限
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    re = requests.get('https://search.jd.com/Search?keyword=华为&page='+str(page),headers=header)
    try:
        re.raise_for_status
    except:
        print('网络连接有误')
    re.encoding = re.apparent_encoding
    html=re.text
#    print(html[80000:110000])
    return html

def formatHTML(html):
    #得到了该页的HTML网页代码，开始进行分析，该范例主要训练正则表达式能力，故不调用BeauifulSoup库
    #京东商城的商品名在<em></em>标签中，价格在</em><i>标签后
    namePattern='<em><font class="skcolor_ljg">华为</font>[^￥].+?</em>'
    str='<em><font class="skcolor_ljg">华为</font>mate40pro  5G手机 亮黑色 8+256G全网通（碎屏险套餐）</em>'
    pricePattern='</em><i>.+?\.00</i>'
    namesub=''
    name=re.findall(namePattern,html)
    price=re.findall(pricePattern,html)
    for i in range(len(name)):
        #对输出字符串进行简单处理
        print('商品名：'+name[i].split('t>')[1].strip('</em>'))
        print('价格：' +price[i].split('i>')[1].strip('</i>'))
    return

def main():
    html = getHTML(0)
    formatHTML(html)
    return

if __name__ == '__main__':
    main()
