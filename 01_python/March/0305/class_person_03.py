# 접근제한자
# - 파이썬은 자바나 C++처럼 명시적으로 public, protected, private와 같은 키워드를 사용하지 않는 대신
#   밑줄(_)을 사용해서 접근제한을 구분한다.
# - 밑줄이 없는 경우는 public처럼 객체 생성 후 누구나 외부에서 직접 접근이 가능하다.
# - 밑줄(_)이 하나인 경우에는 비공개 모드로서 직접적인 접근을 제한하고 있어 객체 생성 후 외부에서 직접 접근을 해서는 안된다.
#   하지만 접근을 시도하면 오류없이 접근은 가능하다.
# - 밑줄(_)이 두 개인 경우는 객체 생성 후 외부에서 직접적인 접근을 할 수 없으며
#   객체 생성 후 직접 접근을 시도하면 정의되지 않은 속성이나 메서드라고 오류메시지가 발생한다.
# - 밑줄(_)이 두 개인 경우는 객체 내부에서는 접근이 가능하며 자식 클래스에게 상속이 되지 않는다.


class Person:
    def __init__(self, name, age, address, wallet):
        # 앞에 self가 붙은 변수들은 클래스의 속성으로 클래스 내에서 전역변수처럼 사용 가능
        # 이외의 name, age, address는 지역변수로 선언된 함수 내에서만 사용 가능'
        self.name = name
        self.age = age
        self.address = address
        # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
        # 비공개 속성의 경우 외부에서 접근할 수 없으므로 값을 읽고 쓸 수 있는 메서드를 만들자
        # -> get(값을 참조)/set(값을 설정) 메서드
        self.__wallet = wallet

    def pay(self, amount):
        if amount > self.__wallet:
            print('잔액이 부족합니다.')
            return
        self.__wallet -= amount
        print('현재 잔액은 {0}원 입니다.'.format(self.__wallet))


maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
# 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함
# maria.__wallet -= 10000
maria.pay(3000)
maria.pay(10000)
