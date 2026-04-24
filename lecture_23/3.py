class A:
    def __init__(self):
        super().__init__()
        print("Class A")
class B:
    def __init__(self):
        super().__init__()
        print("Class B")
class C(A, B):
    def __init__(self):
        super().__init__()
        # A.__init__(self)
        # B.__init__(self)
        print("Class C")
       
 
print(C.__mro__)
c = C()