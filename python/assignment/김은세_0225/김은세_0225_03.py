x = int(input('첫번째 숫자를 입력하시오 => '))
y = int(input('두번째 숫자를 입력하시오 => '))

if x > y:
    x, y = y, x

for i in range(x, y+1):
    print('%3s %d단 %-3s' % ('**', i, '**'), end = '    ')
for j in range(1, 10):
    print()
    for k in range(x, y+1):
        print('%d * %d = %3d' % (k, j, k * j), end='    ')

