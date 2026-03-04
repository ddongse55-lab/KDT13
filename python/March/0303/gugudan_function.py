def input_num():
    x = int(input('첫번째 숫자를 입력하시오 => '))
    y = int(input('두번째 숫자를 입력하시오 => '))
    print()

    return x, y

def min_max_num(x, y):
    min_num = min(x, y)
    max_num = max(x, y)

    return min_num, max_num

def print_gugudan(min_num, max_num):
    for i in range(min_num, max_num+1):
        print('%3s %d단 %-3s' % ('**', i, '**'), end = '    ')

    for j in range(1, 10):
        print()
        for k in range(min_num, max_num+1):
            print('%d * %d = %3d' % (k, j, k * j), end='    ')



if __name__ == '__main__':
    x, y = input_num()
    min_num, max_num = min_max_num(x, y)
    print_gugudan(min_num, max_num)