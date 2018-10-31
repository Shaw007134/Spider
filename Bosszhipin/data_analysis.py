import json
# import csv
import pygal
import jieba
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from collections import Counter
import MySQLdb

db = MySQLdb.connect(host="localhost",port=3306,db="mydb",user="root",password="MY.ustc007")
cursor = db.cursor()



test = []
for line in open('bosszhipin2.txt', 'rb'):
  test.extend(json.loads(line,encoding="latin1"))

def salaryToInt(salary):
  container = []
  temp = salary.split('-')
  container.append(int(temp[0].split('k')[0])*1000)
  container.append(int(temp[1].split('k')[0])*1000)
  return container

def stat_num(num):
  dic = {
    'min': min(num),
    'max': max(num),
    'min_max': max(num) - min(num),
    'mean': np.mean(num),
    'median': np.median(num),
    'modes': stats.mode(num)[0][0],
  }
  return dic
#薪资信息，最低和最高薪资差值分组，统计每组数量，画图
low = []
high = []
mid = []

education = []
experience = []
address = []
edu_salary = {}
exp_salary = {}
post_ul = []
company_dec = []
import MySQLdb

db = MySQLdb.connect(host="localhost",port=3306,db="mydb",user="root",password="MY.ustc007",charset="utf8")
cursor = db.cursor()

j = 0

for i in test:
  
  salary = salaryToInt(i['salary'])
  low.append(salary[0])
  high.append(salary[1])
  mid_salary = (salary[0]+salary[1])/2
  mid.append(mid_salary)
  grad = i['graduation']
  exp = i['experience']
  add = i['address']

  # data = [j+1, i['post'], i['company'], low[j],high[j],mid[j],add,grad,exp,'',i['company_dec']]
  # cursor.execute("""INSERT INTO zhipin VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""",data)
  j = j+1
  education.append(grad)

  if (edu_salary == {}):
    edu_salary[grad] = [0,0,0,1]
    edu_salary[grad][0] += salary[0]
    edu_salary[grad][1] += salary[1]
    edu_salary[grad][2] += mid_salary
  else:
    try:
      edu_salary[grad][0] += salary[0]
      edu_salary[grad][1] += salary[1]
      edu_salary[grad][2] += mid_salary
      edu_salary[grad][3] += 1
    except:
      pass
      edu_salary[grad] = [0,0,0,1]
      edu_salary[grad][0] += salary[0]
      edu_salary[grad][1] += salary[1]
      edu_salary[grad][2] += mid_salary


  experience.append(exp)

  if (exp_salary == {}):
    exp_salary[exp] = [0,0,0,1]
    exp_salary[exp][0] += salary[0]
    exp_salary[exp][1] += salary[1]
    exp_salary[exp][2] += mid_salary
  else:
    try:
      exp_salary[exp][0] += salary[0]
      exp_salary[exp][1] += salary[1]
      exp_salary[exp][2] += mid_salary
      exp_salary[exp][3] += 1
    except:
      pass
      exp_salary[exp] = [0,0,0,1]
      exp_salary[exp][0] += salary[0]
      exp_salary[exp][1] += salary[1]
      exp_salary[exp][2] += mid_salary


  address.append(add)

db.commit()

low = np.array(low)
high = np.array(high)
mid = np.array(mid)
unique_grad = set(education)
grad_counter = Counter(education)



freq_grad = []
for grad in unique_grad:
  freq = education.count(grad)
  freq_grad.append(freq)


def histData(arr):
  a = np.histogram(arr, bins=10)
  f = a[0]
  edge = a[1]
  hist_pyg = []
  for i in range(0,9):
    i = (f[i],edge[i],edge[i+1])
    hist_pyg.append(i)
  return hist_pyg

hist = pygal.Histogram()
hist.add('salary',histData(mid))
hist.title = 'Distribution of salary'
hist.x_labels = [5000,10000,15000,20000,25000,30000,35000]
hist.render_to_file('salary.svg')

#薪资与学历
#饼图-学历要求分布
pie_edu = pygal.Pie()
unique_grad_list = list(unique_grad)
pie_edu.title = 'Educational qualification for Data Analysts (in %)'
per_edu = [round(i/3,2) for i in freq_grad]
for i in range(0,len(unique_grad_list)): 
  pie_edu.add(unique_grad_list[i],per_edu[i])
pie_edu.render_to_file('education_pie.svg')
#条形图-学历与薪资
for i in unique_grad_list:
  edu_salary[i][0] = round(edu_salary[i][0]/edu_salary[i][3])
  edu_salary[i][1] = round(edu_salary[i][1]/edu_salary[i][3])
  edu_salary[i][2] = round(edu_salary[i][2]/edu_salary[i][3])
  
mid_salary_edu = []
for values in edu_salary.values():
  mid_salary_edu.append(values[2])
low_salary_edu = []
for values in edu_salary.values():
  low_salary_edu.append(values[0])
high_salary_edu = []
for values in edu_salary.values():
  high_salary_edu.append(values[1])

hist = pygal.Bar()
hist.title = "Salary by Education"
hist.x_labels = edu_salary.keys()
hist.x_title = "Education"
hist.y_title = "Salary"
hist.add('salary-mid', mid_salary_edu)
hist.add('salary-low', low_salary_edu)
hist.add('salary-high', high_salary_edu)
hist.render_to_file('edu_salary.svg')


#薪资与工作年限
#饼图-年限要求分布
exp_count = Counter(experience)
exp_list = list(exp_count.keys())
exp_list_freq = list(exp_count.values())
exp_list_freq = [round(i/3,2) for i in exp_list_freq]
pie_exp = pygal.Pie()
pie_exp.title = 'Experience requirement for Data Analysts'
for i in range(0,len(exp_list)):
  pie_exp.add(exp_list[i],exp_list_freq[i])
pie_exp.render_to_file('experience_pie.svg')

#条形图-学历与薪资
for i in list(exp_count.keys()):
  exp_salary[i][0] = round(exp_salary[i][0]/exp_salary[i][3])
  exp_salary[i][1] = round(exp_salary[i][1]/exp_salary[i][3])
  exp_salary[i][2] = round(exp_salary[i][2]/exp_salary[i][3])
mid_salary_exp = []
for values in exp_salary.values():
  mid_salary_exp.append(values[2])
low_salary_exp = []
for values in exp_salary.values():
  low_salary_exp.append(values[0])
high_salary_exp = []
for values in exp_salary.values():
  high_salary_exp.append(values[1])

hist = pygal.Bar()
hist.title = "Salary by Experience"
hist.x_labels = exp_salary.keys()
hist.x_title = "Experience"
hist.y_title = "Salary"
hist.add('salary-mid', mid_salary_exp)
hist.add('salary-low', low_salary_exp)
hist.add('salary-high', high_salary_exp)
hist.render_to_file('exp_salary.svg')

#城市分布
#BOSS直聘只展示300条数据，每个城市，甚至全国，其数据已经经过了筛选
#薪资与城市


#公司类型


