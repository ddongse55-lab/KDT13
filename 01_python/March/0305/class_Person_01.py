class Person:
    # 생성자 : 명시적으로 호출하지 않고, 클래스를 객체로 선언할 때 자동으로 호출됨
    def __init__(self):
        self.hello = '★안녕하세요★'

    def greeting(self):
        print(self.hello)


james = Person()
james.greeting()