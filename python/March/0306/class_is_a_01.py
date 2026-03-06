# 물려주는 클래스
# -> 기반클래스, 부모클래스, 슈퍼클래스, 상위클래스
# 물려받는 클래스
# -> 파생클래스, 자식클래스, 서브클래스, 하위클래스
class Person:
    def greeting(self):
        print('★안녕하세요★')


# 단일 상속: 부모클래스를 1개만 상속 가능 -> Java
# 다중 상속: 부모클래스를 1개 이상 상속 가능 -> Python
# ()안에 1개 이상의 부모클래스 기술이 가능
class Student(Person):
    def study(self):
        print('공부하기')

# 클래스 Student로 객체를 만들면 사용할 수 있는 메서드는 총 2개이다.
james = Student()
# 클래스 Person에서 상속받은 메서드 사용
james.greeting()
# 클래스 Student 내부의 메서드 사용
james.study()


