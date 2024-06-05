#magic methods

class User:
    def __init__(self,a,b):        
        print("INIT called")
        self.x = a
        self.y = b

    def __str__(self):
        print("str called")
        return "{0},{1}".format(self.x,self.y)
    
    
    def __add__(self,obj):
        print("add called")
        x = self.x+obj.x
        y = self.y+obj.y

        return(x,y)
    
obj = User(10,20)
print(obj)

obj1 = User(30,40)
print(obj1)

print("addition is",obj1+obj)