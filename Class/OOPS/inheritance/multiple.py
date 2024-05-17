class a:
    def parent(self):
        print("this is parent class!!!")

class b:
    def subparent(self):
        print("this is subparent class!!!")

class c(a,b):
    def child(self):
        print("this is child class!!!")


obj = c()
obj.parent()
obj.subparent()
obj.child()