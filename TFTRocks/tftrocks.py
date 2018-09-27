'''
1、url规律为https://tft.rocks/topic/1-658
2、html需要提取的内容为
  a. 标题
  b. 音频网址
  c. 音频文本加评论
3、条件处理
  a、多个录音，还有评论，选取第一个?
  b、是否是空白的
'''

import json
from phrasing_url import phrasing_url
from extract_data import extract_data
from download import download



initial = "https://tft.rocks/topic/"
i = 1
tft_list = []
list_issue = [216,471,491,655,656,657,658]
while i < 659 :
  if i in list_issue:
    url_issue = initial + str(i)
    dic = {"refs": i, "url": url_issue}
  else:
    html = phrasing_url(initial, i)
    dic = extract_data(html, i)
    print(dic)
    tft_list.append(dic)
  i = i + 1

#print(data)
#print(dic)
with open('tftrocks.txt', 'w',encoding='utf-8') as f:
  #f.write(json.dumps(dic,ensure_ascii=False,indent=2))
  json.dump(tft_list,f,ensure_ascii=False,indent=2)
    #f.write(json.dumps(i))
  



  



