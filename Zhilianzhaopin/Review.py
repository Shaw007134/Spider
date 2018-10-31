from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta

x = 4
y = 5
z = x + y
print("Output #2: Four plus five equals {0:d}.".format(z))

a = [1,2,3,4]
b = ["first", "second", "third", "fourth"]
c = a + b
print("Output #3: {0}, {1}, {2}".format(a,b,c))

print("Output #11: {0:.4f}".format(exp(3)))


string1 = "my deli is due in may"
string1_list1 = string1.split()
string1_list2 = string1.split(" ",2)
print("Output {0}".format(string1_list1))
print("Output {0} and {1} and {2}".format(string1_list2[0],string1_list2[1],string1_list2[2]))


string2 = "you, del, is,due,in,june"
string2_list = string2.split(',')
print("String2: {0}".format(','.join(string2_list)))

string3 = "$$The unwanted characters have been removed._---++"
string3_strip = string3.strip('$_-+')
print("Output {0:s}".format(string3_strip))

string4 = "The quick brown fox jumps over the lazy dog."
string4_list = string4.split()
#pattern1 = re.compile(r"The", re.I)
pattern2 = re.compile(r"(?P<match_word>The)", re.I)
count = 0
for word in string4_list:
    if pattern2.search(word):
        count += 1
        print("{:s}".format(pattern2.search(word).group('match_word')))
        
print("Output {0:d}".format(count))


today = date.today()
print("Output {0!s}".format(today))
print("Output {0!s}".format(today.year))
current_datetime = datetime.today()
print("Output {0!s}".format(current_datetime))

one_day = timedelta(days=-1)
yesterday = today + one_day
print("Output: {0}".format(yesterday))
date_diff = today - yesterday
print("Output {0!s}".format(str(date_diff).split()[0])) 


a_dict = {'one':5, 'two':4, 'three':3}
dict_copy = a_dict.copy()
print("Output a_dict {}".format(a_dict))
order1 = sorted(dict_copy.items(), key=lambda item: item[0])
print("Output order1 {}".format(order1))
order2 = sorted(dict_copy.items(), key=lambda item: item[1])
print("Output order2 {}".format(order2))
order3 = sorted(dict_copy.items(), key=lambda x: x[0], reverse=True)
print("Output order3 {}".format(order3))


my_data = [(1,2,3),(4,5,6),(7,8,9),(7,8,9)]
set_of_tuples1 = {x for x in my_data}
set_of_tuples2 = set(my_data)
print("Output: {}".format(set_of_tuples2))


