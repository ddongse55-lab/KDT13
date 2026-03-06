class SyncValueError(Exception):
  def __init__(self):
    super().__init__('동일한 학번이 이미 존재합니다.')


class OverNumError(Exception):
  def __init__(self):
    super().__init__('\n점수는 100점 초과 입력이 불가능합니다.')


class NegativeNumError(Exception):
  def __init__(self):
    super().__init__('\n점수는 음수 입력이 불가능합니다.')


class Sungjuk:
  def __init__(self):
    self._hakbun = ""
    self._irum = ""
    self._kor = 0
    self._eng = 0
    self._math = 0
    self._tot = 0
    self._avg = 0.0
    self._grade = ""

  def get_hakbun(self):
    return self._hakbun
  def set_hakbun(self, hakbun):
    self._hakbun = hakbun
  hakbun = property(get_hakbun, set_hakbun)

  def get_irum(self):
    return self._irum
  def set_irum(self, irum):
    self._irum = irum
  irum = property(get_irum, set_irum)

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

  def input_sungjuk(self, lst):
    self._hakbun = input("학번 입력 => ")
    try:
      for data in lst:
        if self._hakbun == data.hakbun:
          raise SyncValueError
    except SyncValueError as e:
      print('\n%s\n성적 입력 실패!!\n' %e)
    else:
      self._irum = input("이름 입력 => ")
      self.update_sungjuk()
    # self._kor = int(input("국어 점수 입력 => "))
    # self._eng = int(input("영어 점수 입력 => "))
    # self._math = int(input("수학 점수 입력 => "))

  # 추가 수정
  def update_sungjuk(self):
    try:
        self._kor = int(input("국어 점수 입력 => "))
        if self._kor > 100:
          raise OverNumError
        elif self._kor < 0:
          raise NegativeNumError

        self._eng = int(input("영어 점수 입력 => "))
        if self._eng > 100:
          raise OverNumError
        elif self._eng < 0:
          raise NegativeNumError

        self._math = int(input("수학 점수 입력 => "))
        if self._math > 100:
          raise OverNumError
        elif self._math < 0:
          raise NegativeNumError

    except OverNumError as e:
        print('%s \n성적 입력 실패!!\n' %e)
    except NegativeNumError as e:
        print('%s \n성적 입력 실패!!\n' %e)
    except ValueError as e:
        print('\n점수는 숫자만 입력 가능합니다.\n다시 입력해주세요\n(%s)\n' %e)

    else:
      print('\n성적 입력 성공!!\n')

  def process_sungjuk(self ):
    self._tot = self._kor + self._eng + self._math
    self._avg = self._tot / 3
    if self._avg >= 90:
      self._grade = "수"
    elif self._avg >= 80:
      self._grade = "우"
    elif self._avg >= 70:
      self._grade = "미"
    elif self._avg >= 60:
      self._grade = "양"
    else:
      self._grade = "가"

  def output_sungjuk(self):
    print("%4s %3s %4d  %4d  %4d  %4d  %5.2f  %2s" %
          (self._hakbun, self._irum, self._kor, self._eng, self._math,
           self._tot, self._avg, self._grade))

if __name__ == "__main__":
  obj = Sungjuk()
  obj.input_sungjuk()
  obj.process_sungjuk()
  print("\n\t\t\t *** 성적관리 ***")
  print("==============================================")
  print("학번   이름   국어   영어  수학   총점   평균  등급")
  print("==============================================")
  obj.output_sungjuk()
  print("===============================================")