import json
import datetime
import time

from phrasing_url import phrasing_url
from extract_data import extract_data

initial_url = "https://www.zhipin.com/c101280600/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&page="

dic = []
i = 1
while i < 11:
  print("\n\n"+"pharsing page: " + str(i))
  url = initial_url + str(i) + '&ka=page-' + str(i)
  print(url)
  html = phrasing_url(url)
  dic.append(extract_data(html))
  print("Time now: "+ str(datetime.datetime.now()))
  time.sleep(60)
  i=i+1

with open('bosszhipin2.txt', 'w', encoding='utf-8') as f:
    f.write(json.dumps(dic,ensure_ascii=False))