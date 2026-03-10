# 추상클래스
# 클래스 내부에 추상 메서드가 1개 이상 존재할 경우, 해당 클래스를 추상클래스라고 한다.
from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass


class Student(StudentBase):
    def study(self):
        print('공부하기')

    def go_to_school(self):
        print('학교 가기')


class Children(StudentBase):
    def study(self):
        print('재미나게 놀기')

    def go_to_school(self):
        print('유치원 가기')

    def sleep(self):
        print('낮잠 자기')



james = Student()
james.study()
james.go_to_school()
print('--------------')
eujin = Children()
eujin.study()
eujin.go_to_school()
eujin.sleep()

lst = []
lst.append(eujin)
lst.append(james)
for data in lst:
    data.study()
    data.go_to_school()