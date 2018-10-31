import requests

def download(url,id):
  for i in url:
    img = requests.get(i)
    path = "C:/Users/Shaw/Documents/CG/" + i.split(id+'/')[1]
    print("downloading"+path)
    with open(path,'wb') as f:
          f.write(img.content)

