dct = {}

dct['code'] = input('제품코드 입력 => ')
dct['name'] = input('제품명 입력 => ')
dct['su'] = int(input('수량 입력 => '))
dct['price'] = int(input('단가 입력 => '))
dct['charge'] = dct['su'] * dct['price']

print('\n제품코드    제품명    수량    단가    판매금액')
print('===========================================')
print('%4s     %4s   %4d    %4d   %7d'
      %(dct['code'], dct['name'], dct['su'], dct['price'], dct['charge']))
print('===========================================')