'''
1、需寻找的图片网址为Project以及Unitia
Unitia以 https://ba.hitomi.la/galleries/1294943/ 开头，
后接图片名
Project以 https://ba.hitomi.la/galleries/1286145/ 开头

2、图片名用列表保存
'''

from extract_data import extract_data
from download import download

unitia = "https://hitomi.la/reader/1294943.html"

project = "https://hitomi.la/reader/1286145.html"

unitia_img = extract_data(unitia)
unitia_id = unitia.split('reader'+'/')[1].split('.html')[0]
print(unitia_id)

download(unitia_img, unitia_id) 


