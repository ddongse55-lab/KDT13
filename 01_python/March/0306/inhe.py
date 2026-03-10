# 모든 클래스의 부모 클래스 -> object 클래스
class A(object):
    def __init__(self):
        self.aa =10

    def printA(self):
        print(self.aa)

class B(A):
    def __init__(self):
        # A.__init__(self)
        # super(B, self).__init__
        super().__init__()
        self.bb =20

    def printB(self):
        print(self.bb)

class C(B):
    def __init__(self):
        # B.__init__(self)
        # super(C, self).__init__
        super().__init__()
        self.cc =30

    def printC(self):
        print(self.cc)



