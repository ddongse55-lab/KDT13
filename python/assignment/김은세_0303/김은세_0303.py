# 두 숫자를 입력받는 합수
def input_num():
    x = int(input('첫번째 숫자를 입력하시오: '))
    y = int(input('두번째 숫자를 입력하시오: '))

    return x, y

# 큰 수와 작은 수를 정의하는 함수
# 음수가 입력되면 작은 수는 무조건 2로 정의
def min_max_num(x, y):
    min_num = min(x, y)
    if min_num < 0:
        min_num = 2
    max_num = max(x, y)

    return min_num, max_num

# 소수인지 판단 후 출력하는 함수
count = 0
def print_prime_num(min_num, max_num):
    global count
    for i in range(min_num, max_num + 1):
        for j in range(2, i):
            if i % j == 0:
                break

        else:
            count += 1
            if count % 10 == 0:
                print('%4d' % i)
            else:
                print('%4d' % i, end=' ')

# 총 소수의 개수를 출력하는 함수
def print_total_num():
    if count % 10 != 0:
        print()

    print('총 소수의 개수 =', count)



if __name__ == '__main__':
    x, y = input_num()
    min_num, max_num = min_max_num(x, y)

    print()
    print_prime_num(min_num, max_num)
    print_total_num()
