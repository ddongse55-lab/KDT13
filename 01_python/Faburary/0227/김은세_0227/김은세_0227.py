x = int(input('첫번째 숫자를 입력하시오: '))
y = int(input('두번째 숫자를 입력하시오: '))

min_num = min(x, y)
if min_num < 0:
    min_num = 2
max_num = max(x, y)

print()
print('\t\t\t\t ★ 소수의 개수 ★')
print('==================================================')
count = 0
for i in range(min_num, max_num + 1):
    for j in range(2, i):
        if i % j == 0:
            break

    else:
        count += 1
        if count % 10 == 0:
            print('%4d' % i)
        else:
            print('%4d' % i, end = ' ')

if count % 10 != 0:
    print()

print('==================================================')
print('\t\t\t\t\t\t\t 총 소수의 개수 :', count, '개')