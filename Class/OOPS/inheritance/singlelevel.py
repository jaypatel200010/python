class a:
    def mul(self):
        a = int(input("enter num 1 : "))
        b = int(input("enter num 2 : "))
        print("Multiplication is : ",a*b)


class b(a):
    def mul2(self):
        print("thanks!!!!")

obj = b()
obj.mul()
obj.mul2()