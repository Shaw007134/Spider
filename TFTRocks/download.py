#This script will try to download all the src file
import requests
import json

def download(dic):
  for i in dic:
    if i != "null":
      if 'us_url' in i.keys():
        print(str(i['refs']) + "_us_audio.mp3 downloading")
        us_path = "C:/Users/Shaw/Documents/TOEFL/TFT/" + str(i['refs']) + ".mp3"
        us_audio = requests.get(i['us_url'])
        with open(us_path,'wb') as f:
          f.write(us_audio.content)
        if 'note_url' in i.keys():
          print(str(i['refs']) + "_note_audio.mp3 downloading")
          note_path = "C:/Users/Shaw/Documents/TOEFL/TFT/" + str(i['refs']) + "_note.mp3"
          note_audio = requests.get(i['note_url'])
          with open(note_path,'wb') as f:
            f.write(note_audio.content)

if __name__ == '__main__':
  with open('./tftrocks.txt','r',encoding='utf-8') as load_f:
    dic = json.load(load_f)
  download(dic)
        