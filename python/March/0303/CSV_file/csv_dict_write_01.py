import csv

fieldnames = ['id', 'name', 'price', 'amount']
data = [
    {'id': '1', 'name': 'apple', 'price': '5000', 'amount': '5'},
    {'id': '2', 'name': 'pencil', 'price': '500', 'amount': '42'},
    {'id': '3', 'name': 'pineapple', 'price': '8000', 'amount': '5'},
    {'id': '4', 'name': 'pen', 'price': '1500', 'amount': '10'}
]

f = open('data2.scv', 'w')
# DictWriter : 딕셔너리 형태로 작성
# fieldnames = fieldnames : 필드 네임 지정
writer = csv.DictWriter(f, fieldnames=fieldnames)

# 순수한 데이터만 저장하고 싶다면, writer.writeheader() 작성X
writer.writeheader()
# writerows: 한 번에 모든 data를 출력할 때 사용
writer.writerows(data)

# 한 줄 씩 출력할 때 아래의 for문 사용
# for row in data:
#     writer.writerow(row)

f.close()