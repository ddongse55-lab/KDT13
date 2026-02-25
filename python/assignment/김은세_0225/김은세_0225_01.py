x = int(input('단을 입력하시오 => '))

print('%3s %d단 %-3s' %('**', x, '**'))

for i in range(1, 10):
    print('%d * %d = %3d'%(x, i, x*i))