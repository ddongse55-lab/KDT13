lst = []

while True:
    dct = {}

    dct['code'] = input('제품코드 입력 => ')

    if dct['code'].lower() == 'exit':
        break

    dct['name'] = input('제품명 입력 => ')
    dct['su'] = int(input('수량 입력 => '))
    dct['price'] = int(input('단가 입력 => '))
    dct['charge'] = dct['su'] * dct['price']

    lst.append(dct)
    print()

print('\n\t\t\t *** 제품관리 ***\t\t\t')
print('===========================================')
print('제품코드    제품명    수량      단가    판매금액')
print('===========================================')

total = 0

for dct in lst:
    total += dct['charge']
    print('%5s    %5s   %4d   %7d   %7d'
          %(dct['code'], dct['name'], dct['su'], dct['price'], dct['charge']))
print('===========================================')
print('\t\t\t\t총 금액은', total, '원 입니다.')
print('===========================================')