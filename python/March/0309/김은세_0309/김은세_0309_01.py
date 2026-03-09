# import os,sys
# print(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test"))
# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test"))

from 김은세_0309_02 import Sangpum

lst = []

def menu_title():
  print("\t*** 상품 정보 관리 ***")
  print("1. 상품정보 입력")
  print("2. 상품정보 출력")
  print("3. 상품정보 조회")
  print("4. 상품정보 수정")
  print("5. 상품정보 삭제")
  print("6. 프로그램 종료")
  print()

def input_sangpum():
  print()
  obj = Sangpum()
  obj.input_sangpum(lst)
  obj.process_charge()
  #global lst
  lst.append(obj)

def print_sangpum():
  if len(lst) == 0:
    print("\n출력할 데이터가 없음!!\n")
    return

  print('\n\t\t\t\t*** 제품관리 ***')
  print('============================================')
  print('제품코드    제품명     수량      단가    판매금액')
  print('============================================')
  total = 0
  for obj in lst:
      total += obj.charge
      obj.output_sangpum()
  print('============================================')
  print('\t\t\t\t 총 금액은 %d원 입니다.' %total)
  print('============================================')

def search_sangpum():
  if len(lst) == 0:
    print("\n조회할 데이터가 없음1!!\n")
    return

  code = input("\n조회할 상품코드 입력 => ")
  for obj in lst:
    if obj.code == code:
        print('\n제품코드    제품명     수량      단가    판매금액')
        print('============================================')
        obj.output_sangpum()
        print('============================================\n')
        break
  else:
    print("\n조회할 상품 정보가 없음2!!\n")


def update_sangpum():
  if len(lst) == 0:
    print("\n수정할 데이터가 없음1!!\n")
    return

  code = input("\n수정할 상품 코드 입력 => ")
  for obj in lst:
    if obj.code == code:
      print()
      obj.update_sangpum_data()
      obj.process_charge()
      print("\n상품코드 %s 정보 수정 성공!!\n" % code)
      break
  else:
    print("\n수정할 상품 정보가 없음2!!!\n")

def delete_sangpum():
  if len(lst) == 0:
    print("\n삭제할 데이터가 없음1!!\n")
    return

  code = input("\n삭제할 상품 코드 입력 => ")
  for obj in lst:
    if obj.code == code:
      lst.remove(obj)
      print("\n상품 코드 %s 정보 삭제 성공!!\n" % code)
      break
  else:
    print("\n삭제할 상품 정보가 없음2!!!\n")

if __name__ == "__main__":
  while True:
    menu_title()
    try:
        menu = int(input("메뉴를 선택하세요(1~6) => "))
    except Exception as e:
        print('\n접근 방법이 잘못되었습니다.\n숫자를 다시 입력하세요!!(%s)\n' %e)
        continue
    if menu == 1:
      input_sangpum()
    elif menu == 2:
      print_sangpum()
    elif menu == 3:
      search_sangpum()
    elif menu == 4:
      update_sangpum()
    elif menu == 5:
      delete_sangpum()
    elif menu == 6:
      print("\n프로그램 종료!!")
      break
    else:
      print("\n메뉴를 다시 입력하세요!!\n")
