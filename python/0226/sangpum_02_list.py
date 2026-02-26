lst = []

while True:
    put = []

    put.append(input('제품코드 입력 => '))
    if put[0].lower() == 'exit':
        break
    put.append(input('제품명 입력 => '))
    put.append( int(input('수량 입력 => ')))
    put.append(int(input('단가 입력 => ')))
    put.append(put[2]*put[3])

    lst.append(put)
    print()

print('\n\t\t\t *** 제품관리 ***\t\t\t')
print('===========================================')
print('제품코드    제품명    수량      단가    판매금액')
print('===========================================')
total = 0
for put in lst:
    total += put[-1]
    print('%5s    %5s   %4d   %7d   %7d' %(put[0], put[1], put[2], put[3], put[-1]))
print('===========================================')
print('\t\t\t  총 판매금액은', total, '원 입니다.')
print('===========================================')