def factorial(n):
    if n == 1:                  # n이 1일 때,
        return 1                # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n-1)   # n과 factorial 함수에 n-1을 넣어서 반환된 값

    # 반복문(for문)을 이용해서 factorial 구하기
    # result = 1
    # for i in range(1, n+1):
    #     result *= i
    # return result


print(factorial(5))