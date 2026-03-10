class A:
    def __init__(self, x):
        self.aa = x

    def printA(self):
        print(self.aa)

class B(A):
    def __init__(self, x, y):
        # A.__init__(self, x)
        # super(B, self).__init__(x)
        super().__init__(x)
        self.bb =y

    def printB(self):
        print(self.bb)

class C(B):
    def __init__(self, x, y, z):
        # B.__init__(self, x, y)
        # super(C, self).__init__(x, y)
        super().__init__(x, y)
        self.cc = z

    def printC(self):
        print(self.cc)



