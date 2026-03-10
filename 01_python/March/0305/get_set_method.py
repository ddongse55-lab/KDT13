class Person:
    def __init__(self, name, age, address, wallet):
        self._name = name
        self._age = age
        self._address = address
        self._wallet = wallet

    # name 속성에 대한 get/set 메소드
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    name = property(get_name, set_name)

    # age 속성에 대한 get/set 메소드
    def get_age(self):
        return self._age
    def set_age(self, age):
        self._age = age
    age = property(get_age, set_age)

    # address 속성에 대한 get/set 메소드
    def get_address(self):
        return self._address
    def set_address(self, address):
        self._address = address
    address = property(get_address, set_address)

    # wallet 속성에 대한 get/set 메소드
    def get_wallet(self):
        return self._wallet
    def set_wallet(self, wallet):
        self._wallet = wallet
    wallet = property(get_wallet, set_wallet)

    def pay(self, amount):
        if amount > self._wallet:
            print('잔액이 부족합니다.')
            return
        self._wallet -= amount
        print('현재 잔액은 {0}원 입니다.'.format(self._wallet))


if __name__ == '__main__':
    maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
    print(maria.name)
    maria.name = '이기자'
    print(maria.name)
