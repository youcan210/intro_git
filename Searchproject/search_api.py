import csv
import eel

# JavaScriptから呼べるように関数を登録

def search_open(row,csv_file):
  with open('test.csv') as f:
    reader = csv.reader(f)
    source = []


def search():
  # -------------------↑
  for row in reader:
    print(row)
    source.append(row[0])
  for in_name in source:
    in_name = input('名前を入力')
    if in_name in source:
      print(in_name[0:10] +('の名前はあります'))
    elif in_name != source:
      print('登録されていません')
      source.append(in_name)
      with open('test.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow([in_name])
# JavaScriptの関数の戻り値をPythonで取得するには？
search()
eel.js_function()
# 最初の画面のHTMLファイルを指定

eel.init("web")
eel.start("index.html", size=(800,800),port=9999)