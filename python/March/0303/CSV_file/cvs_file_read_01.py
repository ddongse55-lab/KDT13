import csv

f = open('output.csv', 'r', encoding ='utf-8', newline ='')

# reader() : 저장되어있는 정보를 리스트 형태로 읽어 한 행씩 출력
reader = csv.reader(f)
print(reader)
for row in reader:
    print(row)

f.close()