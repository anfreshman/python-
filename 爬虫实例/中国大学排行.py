import requests
from bs4 import BeautifulSoup
url="https://www.shanghairanking.cn/rankings/bcur/2020"
r = requests.get(url)
try:
  r.raise_for_status
except:
  r.text
  print("网络连接失败")
r.encoding=r.apparent_encoding
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
#得到了目标HTML代码，开始检索大学排名
#print(len(soup('td')))
i=0
m=0
pm=soup('td')
dx=soup('a')
#first=soup(string='清华大学')
first=soup('tbody')
print(first)
#print(first[0].parent.parent.parent)

for bq in soup('tr')[:500]:
   print(bq)
#for bq2 in soup('a')[:500]:
#   print(bq2.string)
#循环输出结果
'''
while i<(len(dx)-19):
  print(dx[i+19].string)
  print(pm[m].string)
  m+=6
  i+=1
'''
