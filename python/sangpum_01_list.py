put = []

put.append(input('제품코드 입력 => '))
put.append(input('제품명 입력 => '))
put.append( int(input('수량 입력 => ')))
put.append(int(input('단가 입력 => ')))
put.append(put[2]*put[3])

print('\n제품코드    제품명    수량    단가    판매금액')
print('===========================================')
print('%4s     %4s   %4d    %4d   %6d' %(put[0], put[1], put[2], put[3], put[-1]))
print('===========================================')