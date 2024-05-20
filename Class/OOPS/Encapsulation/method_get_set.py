class User:
    def get(self,__a,__b):
        self.__g = __a
        self.__h = __b


    def set(self):
        print("value of A : ",self.__g)
        print("value of B : ",self.__h)


obj = User()
obj.get(10,20)
obj.set()