class A:
    def details(self):
        print("class A")
class B:
    def details1(self):
        print("class B")
class C(A,B):
    def details3(self):
        super().details()
        super().details1()
        print("class C")
c = C()
c.details3()