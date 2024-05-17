class A:
    def one(self):
        print("this is hire archical")

class B(A):
    def two(self):
        print("this is hire archical")

class C:
    def three(self):
        print("this is hire archical")

class D(B,C):
    def four(self):
        print("this is hire archical")

obj = D()
obj.one()
obj.two()
obj.three()
obj.four()



