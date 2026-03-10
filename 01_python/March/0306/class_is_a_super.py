class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '★안녕하세요★'


class Student(Person):
    def __init__(self):
        # super()로 기반 클래스의 생성자 메서드 호출
        super().__init__()
        print('Student __init__')
        self.school = '파이썬 코딩 도장'


james = Student()
print(james.school)
# 기반클래스의 속성을 출력하려고 하면 에러가 발생
# -> 생성자 메서드의 경우 클래스로 객체가 생성될 때, 자동으로 호출되는데 클래스 Person의 객체가 따로 생성되지 않음
#    따라서 클래스 Person의 생성자가 호출되지 않았기 때문에 hello라는 속성이 생성되지 않음
# -> super()로 클래스 Student의 생성자 메서드 내에 클래스 Person의 생성자 메서드 호출을 통해 해결
print(james.hello)


