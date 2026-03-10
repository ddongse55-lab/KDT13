dct = {}

dct['code'] = input('학번을 입력하세요: ')
dct['name'] = input('이름을 입력하세요: ')
dct['kor'] = int(input('국어 점수를 입력하세요: '))
dct['eng'] = int(input('영어 점수를 입력하세요: '))
dct['math'] = int(input('수학 점수를 입력하세요: '))
dct['total'] = dct['kor'] + dct['eng'] + dct['math']
dct['avg'] = dct['total'] / 3

if dct['avg'] >= 90:
    dct['grade'] = '수'
elif dct['avg'] >= 80:
    dct['grade'] = '우'
elif dct['avg'] >= 70:
    dct['grade'] = '미'
elif dct['avg'] >= 60:
    dct['grade'] = '양'
else:
    dct['grade'] = '가'

print('\n%23s %s %-23s' %('***', '성적표', '***'))
print('=======================================================')
print('학번    이름    국어    영어    수학    총점    평균    등급')
print('=======================================================')
print('%s  %s  %4d   %4d   %4d    %4d    %4.2f    %s' %
      (dct['code'], dct['name'], dct['kor'], dct['eng'], dct['math'], dct['total'], dct['avg'], dct['grade']))
print('=======================================================')