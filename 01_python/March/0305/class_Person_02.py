class Person:
    def __init__(self, name, age, address):
        # 앞에 self가 붙은 변수들은 클래스의 속성으로 클래스 내에서 전역변수처럼 사용 가능
        # 이외의 name, age, address는 지역변수로 선언된 함수 내에서만 사용 가능
        self.hello = '★안녕하세요★'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} \n저는 {1}입니다.'.format(self.hello, self.name))


maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()

print('\n이름:', maria.name)
print('나이:', maria.age)
print('주소:', maria.address)

maria.name = '이기자'
print('\n이름:', maria.name)
maria.greeting()
