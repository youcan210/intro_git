import csv
source = []
with open('sample.csv') as f:
  reader = csv.reader(f)
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
    with open('sample.csv','a') as f:
      writer = csv.writer(f)
      writer.writerow([in_name])