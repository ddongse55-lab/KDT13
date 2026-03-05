class Sungjuk:
    def __init__(self):
        self._code = ''
        self._name = ''
        self._kor = 0
        self._eng = 0
        self._math = 0
        self._tot = 0
        self._avg = 0.0
        self._grade = ''

    def get_code(self):
        return self._code
    def set_code(self, code):
        self._code = code
    code = property(get_code, set_code)

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    name = property(get_name, set_name)

    def get_kor(self):
        return self._kor
    def set_kor(self, kor):
        self._kor = kor
    kor = property(get_kor, set_kor)

    def get_eng(self):
        return self._eng
    def set_eng(self, eng):
        self._eng = eng
    eng = property(get_eng, set_eng)

    def get_math(self):
        return self._math
    def set_math(self, math):
        self._math = math
    math = property(get_math, set_math)

    def get_tot(self):
        return self._tot
    def set_tot(self, tot):
        self._tot = tot
    tot = property(get_tot, set_tot)

    def get_avg(self):
        return self._avg
    def set_avg(self, avg):
        self._avg = avg
    avg = property(get_avg, set_avg)

    def get_grade(self):
        return self._grade
    def set_grade(self, grade):
        self._grade = grade
    grade = property(get_grade, set_grade)

    def input_sungjuk(self):
        self._code = input('\n학번 입력: ')
        self._name = input('이름 입력: ')
        self._kor = int(input('국어 점수 입력: '))
        self._eng = int(input('영어 점수 입력: '))
        self._math = int(input('수학 점수 입력: '))

    def process_sungjuk(self):
        self._tot = self._kor + self._eng + self._math
        self._avg = self._tot / 3

        if self._avg >= 90:
            self._grade = '수'
        elif self._avg >= 80:
            self._grade = '우'
        elif self._avg >= 70:
            self._grade = '미'
        elif self._avg >= 60:
            self._grade = '양'
        else:
            self._grade = '가'

    def output_sungjuk(self):
        print('%s  %s  %4d   %4d   %4d    %4d    %4.2f    %s' %
              (self._code, self._name, self._kor, self._eng, self._math,
               self._tot, self._avg, self._grade))


if __name__ == '__main__':
    obj = Sungjuk()
    obj.input_sungjuk()
    obj.process_sungjuk()
    print('\n%23s %s %s' % ('***', '성적표', '***'))
    print('=======================================================')
    print('학번    이름    국어    영어    수학    총점    평균    등급')
    print('=======================================================')
    obj.output_sungjuk()
    print('=======================================================')

