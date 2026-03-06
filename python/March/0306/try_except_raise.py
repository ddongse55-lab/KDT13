def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:
            raise Exception('3의 배수가 아닙니다.')
        print(x)
    # 함수 안에서 예외 처리
    except Exception as e:
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        # raise로 연재 예외를 다시 발생시켜 상위 코드 블록으로 넘김
        raise

try:
    three_multiple()
# 하위 코드 블록에서 예외가 발생해도 실행됨
except Exception as e:
    print('스크립트 파일에서 예외가 발생했습니다.', e)