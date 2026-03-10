class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '★안녕하세요★'


# 자식클래스에서 생성자 메서드가 없는 경우
# 객체를 생성할 때, 부모클래스의 생성자 메서드를 자동으로 호출한다.
class Student(Person):
    pass

james = Student()
print(james.hello)