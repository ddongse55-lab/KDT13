class BlankValueError(Exception):
  def __init__(self):
    super().__init__('공백 입력 불가')


class SyncValueError(Exception):
  def __init__(self):
    super().__init__('동일한 상품코드가 이미 존재합니다.')


class NegativeNumError(Exception):
  def __init__(self):
    super().__init__('\n현재 입력 칸에는 음수 입력이 불가능합니다.')


class Sangpum:
  def __init__(self):
    self._code = ""
    self._name = ""
    self._amount = 0
    self._price = 0
    self._charge = 0
    self._tot = 0



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

  def get_amount(self):
    return self._amount
  def set_amount(self, amount):
    self._amount = amount
  amount = property(get_amount, set_amount)

  def get_price(self):
    return self._price
  def set_price(self, price):
    self._price = price
  price = property(get_price, set_price)

  def get_charge(self):
    return self._charge
  def set_charge(self, charge):
    self._charge = charge
  charge = property(get_charge, set_charge)

  def get_tot(self):
    return self._tot
  def set_tot(self, tot):
    self._tot = tot
  tot = property(get_tot, set_tot)

  def input_sangpum(self, lst):
    while True:
      try:
        self._code = input("상품코드 입력 => ")
        if self._code.strip() == "":
          raise BlankValueError
        else:
          for data in lst:
            if self._code == data.code:
              raise SyncValueError
      except Exception as e:
        print('\n%s\n상품 입력 실패!!\n' % e)
      else:
          break
    while True:
      try:
        self._name = input("상품명 입력 => ")
        if self._name.strip() == "":
          raise BlankValueError

      except Exception as e:
        print('\n%s\n상품 입력 실패!!\n' % e)
      else:
        self.update_sangpum_data()
        break

  def input_sangpum_data(self, title):
      while True:
          try:
              data = int(input(f"{title} 입력 => ").strip())

              if data <= 0:
                  raise NegativeNumError()

              return data

          except ValueError as e:
              print('\n숫자만 입력 가능합니다.\n다시 입력해주세요\n(%s)\n' % e)
          except Exception as e:
              print('%s \n상품정보 입력 실패!!\n' % e)

  def update_sangpum_data(self):
      self._amount = self.input_sangpum_data("수량")
      self._price = self.input_sangpum_data("단가")
      print('\n상품정보 입력 성공!!\n')

  def process_charge(self):
      self._charge = self._amount * self._price

  def output_sangpum(self):
      print('%5s    %5s   %4d   %7d   %7d'
            % (self._code, self._name, self._amount, self._price, self._charge))

if __name__ == "__main__":
  obj = Sangpum()
  obj.input_sangpum()
  obj.update_sangpum_data()
  obj.process_charge()
  print('\n\t\t\t\t*** 제품관리 ***')
  print('============================================')
  print('제품코드    제품명     수량      단가    판매금액')
  print('============================================')
  obj.output_sangpum()
  print('============================================')