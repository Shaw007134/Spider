from phrasing_url import phrasing_url
import re

def extract_data(html,refs):
  if html == None:
    dic = 'null'
    return dic
  dic = {}
  dic['refs'] = refs
  post = html.xpath("//body//script//text()")
  #print("post type is {}".format(type(post[0])))
  #这里有点问题，不能用id加refs作为
  title = 'topic":{"id":' + str(refs) + ',"title":'
  try:
    data = post[0].split('window.App=')[1]
  except IndexError:
    dic = 'null'
    return dic

  #print("data type is {}".format(type(data)))
  #print(data)

  #print(title)
  title = data.split(title)[1]
  title = title.split(',"chineseTitle"')[0]
  #print(title)
  dic['title'] = title.replace(u'\"','').replace(u'\\n','')

  answer = data.split('noteTitle')[0]
  answer = answer.split('"Answers":')[1]
  try:
    answer = answer.split('"title":"')[1].split('R1')[0]
  except IndexError:
    dic = 'null'
    return dic
  #print(answer)
  #answer = answer.encode('latin-1').decode('unicode_escape')
  if 'https' in answer:
    answer = answer.split('http')[-1].split(')\\n\\n')[1]
  dic['answer'] = answer\
    .split('Outline')[0].split('Notes')[0].replace('#','').replace('*','') \
    .replace(u'\u2028','').replace(u'\\u2028','').replace(u'\t',' ').replace(u'\n',' ')\
    .replace(u'\\n',' ').replace(u'\",\"','').replace(u'\\','').strip()

  
  if 'Vocabulary' in data:
    vocabulary = data.split('Vocabulary')[1]
    vocabulary = vocabulary.split('"chineseTitle"')[0].split('![Picture]')[0].\
      replace(u',"noteTitle":"",','')
    dic['vocabulary'] = vocabulary.replace(u'\\n',' ').replace(u'\"','').\
      replace('*','').strip()
    if 'R1' in data:
      outline = data.split('Vocabulary')[0].replace(u'2. ','')
      outline = 'R1' + outline.split('R1')[1]
    #print(outline)
    #print(vocabulary)
      dic['outline'] = outline.replace(u'\\n',' ').replace('*','').replace(u'\\u2028','').\
        strip()
    
    # dic['outline'] = outline.encode('latin-1').decode('unicode_escape').replace(u'\\n','')
    # dic['vocabulary'] = vocabulary.encode('latin-1').decode('unicode_escape').replace(u'\\n','')
    # print(dic['outline'])
    # print(dic['vocabulary'])

  audio_url = data.split('"audio_url":"')[1]
  
  url = audio_url.split('","us_audio_url":')[0]
  #print(url)

  us_audio_url = audio_url.split('","us_audio_url":')[1]
  us_audio_url = us_audio_url.split('","note_url":')[0].replace('"','')
  #print(us_audio_url)

  note_audio_url = data.split('"note_url":')[1].strip('"')
  note_audio_url = note_audio_url.split(',"picture_url":')[0].replace(u'\"','')

  

  if len(us_audio_url) > 10:
    us_url = us_audio_url
  else:
    us_url = audio_url
  
  dic['us_url'] = us_url.encode('latin-1').decode('unicode_escape')

  if len(note_audio_url) > 10:
    note_url = note_audio_url
    dic['note_url'] = note_url.encode('latin-1').decode('unicode_escape')
    # print(dic['note_url'])

  #data.replace("\n","")
  
  #print(dic)
  return dic