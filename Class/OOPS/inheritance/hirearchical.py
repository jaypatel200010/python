class A:
    def one(self):
        print("this is hire archical")

class B(A):
    def two(self):
        print("this is hire archical")

class C(A):
    def three(self):
        print("this is hire archical")

obj = B()
obj.one()
obj.two()

obj1 = C()
obj1.one()
obj1.three()