# 오버라이딩 = 재정의
# 메서드 오버라이딩
# -> 부모클래스에서 상속받은 메서드에 대해 자식클래스에서 재정의하는 경우
class Person:
    def greeting(self):
        print('★안녕하세요★')


class Student(Person):
    def greeting(self):
        print('안녕하세요')
        print('저는 파이썬 도장 학생입니다')



james = Student()
james.greeting()
