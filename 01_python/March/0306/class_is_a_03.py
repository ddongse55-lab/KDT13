# 다중 상속의 경우 동일한 이름의 메서드가 여러 개의 상위클래스에 동일하게 있을 때,
# 먼저 선언된 상위클래스의 메서드를 우선적으로 상속받는다.

class Person:
    def __init__(self):
        print('Person Class')

    def greeting(self):
        print('★안녕하세요★')


class University:
    def __init__(self):
        print('University Class')

    def manage_credit(self):
        print('※학점 관리※')

    def greeting(self):
        print('☆안녕하세요☆')


class Undergraduate(Person, University):
    def study(self):
        print('공부하기')



james = Undergraduate()
james.greeting()
james.manage_credit()
james.study()



