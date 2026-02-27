lst = []

while True:
    dct = {}

    dct['code'] = input('학번을 입력하세요: ')
    if dct['code'].lower() == 'exit':
        break
    dct['name'] = input('이름을 입력하세요: ')
    dct['kor'] = int(input('국어 점수를 입력하세요: '))
    dct['eng'] = int(input('영어 점수를 입력하세요: '))
    dct['math'] = int(input('수학 점수를 입력하세요: '))
    dct['total'] = dct['kor'] + dct['eng'] + dct['math']
    dct['avg'] = dct['total'] / 3

    lst.append(dct)
    print()

print('\n%20s %s %-20s' %('***', '성적표', '***'))
print('=================================================')
print('학번    이름    국어    영어    수학    총점    평균')
print('=================================================')
total = 0
total_avg = 0

for dct in lst:
    total += 1
    total_avg += dct['avg']
    print('%s  %s  %4d   %4d   %4d    %4d    %4.2f' %
        (dct['code'], dct['name'], dct['kor'], dct['eng'], dct['math'], dct['total'], dct['avg']))
print('=================================================')
print('\t\t\t학생수 : %d\t\t\t전체 평균 : %5.2f' % (total, total_avg/total))
print('=================================================')