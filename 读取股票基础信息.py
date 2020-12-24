import requests
from bs4 import BeautifulSoup
import re
import codecs


#获取页面源码
def getHtml(url):
    html = ""
    r = None
    try:
#        headers = {'User-Agent': 'Mozilla/5.0'}
#    headers = {'Cookie':'session=eyJpZCI6ImJjNGNjNjAwLTQ1OGYtMTFlYi1hMzFkLTMzODk4MGJjYWZmYSJ9; session.sig=HfWwpmEUF8wFrqfcsIAoHhEgtn0; _ga=GA1.2.1385182798.1608776921; _gid=GA1.2.157124533.1608776921; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2210000000000000001%22%2C%22%24device_id%22%3A%221769293b1b86da-024fcfa493d2c1-3a614f0b-2073600-1769293b1b9618%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22aladingpc%22%7D%2C%22first_id%22%3A%221769293b1b86da-024fcfa493d2c1-3a614f0b-2073600-1769293b1b9618%22%7D; _gat=1; JSESSIONID=1C337AEF0B545AD8629C3629F4B7BC22; ngxid=rBFdQF/kKK4gSe7jojieAg==; _gat_gtag_UA_155294166_1=1'}
        r = requests.get(url)
#    r = requests.get(url,headers=headers)
        r.raise_for_status
        r.apparent_encoding 
        html = r.text
        return html
    except:
        return ''
    

#处理页面源码，获取需要查询的股票代码
#由于技术更迭，目前没有找到合适的数据来源，暂时先不进行这一步
def getName(url):
    name = ""
    return name
#!!!!!!!!!!!!!!!!!!!!



#处理页面源码，获得指定信息并存入键值对中
def getData(html):
    soup = BeautifulSoup(html,"html.parser")
    name = ""
    price = 0;
    namePattern = 'nameCN":".*?"'
    pricePattern = 'latestPrice".*?"'
    name = re.findall(namePattern,html)
    price = re.findall(pricePattern,html)
    data = {'name':'','price':0}
    data['name']=name[0].split(':')[1]
    data['price']=price[0].split(':')[1]
    return data


#将键值对写入文件中
def writeIntoFile(data):
    f = codecs.open("file/stock1.txt",'a+')
    f.write(data['name']+':'+data['price']+"\r\n")
    f.close
    return

#程序逻辑：
#   从某一数据源得到股票列表，通过股票列表到老虎社区得到当前价格并存入文件
def main():
    number = '000593'
    url = "https://www.laohu8.com/stock/" + number
    html = getHtml(url)
    data = getData(html)
    print(data)
    writeIntoFile(data)

main()
    



    
    

    
