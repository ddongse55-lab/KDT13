def circle_area(radius, print_format):
    # radius, print_format : 형식매개변수
    area = 3.14 * (radius ** 2)
    print_format(area)

if __name__ == '__main__':
    # radius = 3, print_format = lambda x: print('결과값:', round(x, 1))
    # -> 형식 매개변수 print_format에 lambda 표현식을 대입하는 형식
    circle_area(3, lambda x: print('결과값:', round(x, 1)))
    # radius = 3, print_format = lambda x: print('결과값:', round(x, 2))
    circle_area(3, lambda x: print('결과값:', round(x, 2)))

    a = lambda x: print('결과값:', round(x, 1))
    circle_area(3, a)
