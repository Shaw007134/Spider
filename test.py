#This function will extract the information of the job description

from phrasing_url import phrasing_url
import json
from clearlist import clearlist

url = "http://jobs.zhaopin.com/CC286596486J00047833312.htm"

html = phrasing_url(url)

post_ul = ''

#cont = html.xpath("(//div[@class='tab-inner-cont'])[1]//text()")
cont = html.xpath("//ul[@class='terminal-ul clearfix']//text()")
#intro = {"{}".format(cont[2*i-1]):"{}".format(cont[2*i]) for i in range(int(len(cont)/2))}

company = html.xpath("//ul[@class='terminal-ul clearfix terminal-company mt20']//text()")
print(cont)
print(clearlist(cont))
'''
ps=cont.xpath("//p//text()")
with open('test.txt', 'w', encoding='utf-8') as f:
    for i in ps:
        f.write(json.dumps(i,ensure_ascii=False,indent=2))
        f.write("\n")
'''
# for terminalpage in html.xpath("//div[@class='terminalpage-main clearfix']"):
#     print(terminalpage)
#     for box in terminalpage.xpath("//div[@class='tab-cont-box']"):
#         print(box)
#         cont = box.xpath("//div[@class='tab-inner-cont']")[0]
#         print(cont)
#         ps=cont.xpath("//p//text()")
#         with open('test.txt', 'w', encoding='utf-8') as f:
#             for i in ps:
#                 f.write(json.dumps(i,ensure_ascii=False,indent=2))
#                 f.write("\n")
        # for i in range(len(ps)-1):
        #     print(ps[i].xpath("/text()"))
        #     post_ul += ps[i].xpath("text()").replace("\n","").strip()
#print(post_ul)
