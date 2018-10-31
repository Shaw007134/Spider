import json

test = []
# zhilianzhaopin1
for line in open('zhilianzhaopin1.txt', 'rb'):
  test.extend(json.loads(line,encoding="latin1"))

count = 0
salary = 0
x = test[0]
print(x)
# for i in test:
#   low = i['salary'].split('-')[0]
#   high = i['salary'].split('-')[1].split('-')[1].split('元')[0]
#   print("low: " + low)
#   print("high: " + high)


   