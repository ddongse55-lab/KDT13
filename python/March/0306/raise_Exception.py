try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:
        # raise Exception() -> 필요에 의해 인위적으로 예외를 발생
        raise Exception('3의 배수가 아닙니다.')
    print(x)
except Exception as e:
    print('예외가 발생했습니다.', e.args[0])