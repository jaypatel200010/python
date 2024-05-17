class g:
    def multi(self):
        print("this is multilevel")



class a(g):
    def mul(self):
        a = int(input("enter num 1 : "))
        b = int(input("enter num 2 : "))
        print("Multiplication is : ",a*b)


class b(a):
    def mul2(self):
        print("thanks!!!!")

obj = b()
obj.multi()
obj.mul()
obj.mul2()