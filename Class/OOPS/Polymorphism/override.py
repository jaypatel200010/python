#method overriding :- same method name in inheritade class
class g:
    def mul(self):
        print("Class g")

class a:
    def mul(self):
        super().mul()
        print("class a")


class b(a,g):
    def mul(self):
        super().mul()               #to tackle the override and also access the class a fun with same name
        print("thanks!!!!")

obj = b()
obj.mul()
