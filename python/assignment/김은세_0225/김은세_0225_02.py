x = int(input('첫번째 숫자를 입력하시오 => '))
y = int(input('두번째 숫자를 입력하시오 => '))

if x > y:
    x, y = y, x

for i in range(x, y+1):
    print('\n%3s %d단 %-3s' % ('**', i, '**'))
    for j in range(1, 10):
        print('%d * %d = %3d' % (i, j, i * j))

