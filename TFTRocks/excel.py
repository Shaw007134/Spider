import sys
import json
from xlrd import open_workbook
from xlwt import Workbook

# input_file = sys.argv[1]
# output_file = sys.argv[2]

def excel(list_dic, output_file):
  output_workbook = Workbook()
  output_worksheet = output_workbook.add_sheet('tftrocks')

  headers = ['refs','title','answer','outline','vocabulary','us_url','note_url']

  for row in range(len(list_dic)+1):
    if row == 0:
      for col in range(len(headers)):
        output_worksheet.write(row,col,headers[col])
    else:
      data = list_dic[row-1]
      if data != 'null':
        row_data = [data['refs'],data['title'],data['answer']]
        if 'outline' in data.keys():
          row_data.append(data['outline'])
        else:
          row_data.append('')
        if 'vocabulary' in data.keys():
          row_data.append(data['vocabulary'])
        else:
          row_data.append('')
        if 'us_url' in data.keys():
          row_data.append(data['us_url'])
        else:
          row_data.append('')
        if 'note_url' in data.keys():
          row_data.append(data['note_url'])
        else:
          row_data.append('')
        
        for col in range(len(headers)):
          output_worksheet.write(row,col,row_data[col])

  output_workbook.save(output_file)

if __name__ == '__main__':
  with open('./tftrocks.txt','r',encoding='utf-8') as load_f:
    list_dic = json.load(load_f)
  output_file = './output.xls'
  excel(list_dic,output_file)