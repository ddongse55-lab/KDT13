import csv

f = open('data2.scv', 'r')
# DictReader: 딕셔너리 형태로 읽어들임
reader = csv.DictReader(f)

for row in reader:
    print(row)

f.close()