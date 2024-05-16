# class


# class one:
#     def add(self):
#         num1 = int(input("enter num1 : "))
#         num2 = int(input("enter num2 : "))
#         print("Addition of two num is",num1+num2)

#     def mul(self):
#         num1 = int(input("enter num1 : "))
#         num2 = int(input("enter num2 : "))
#         print("multiplication of two num is",num1*num2)

#     def sub(self):
#         num1 = int(input("enter num1 : "))
#         num2 = int(input("enter num2 : "))
#         print("subtraction of two num is",num1-num2)

# obj = one()
# obj.add()
# obj.mul()
# obj.sub()


# nested class

class one:
    def add(self):
        num1 = int(input("enter num1 : "))
        num2 = int(input("enter num2 : "))
        print("Addition of two num is",num1+num2)

    class two:
        def mul(self):
            num1 = int(input("enter num1 : "))
            num2 = int(input("enter num2 : "))
            print("multiplication of two num is",num1*num2)

class three:
    def sub(self):
        num1 = int(input("enter num1 : "))
        num2 = int(input("enter num2 : "))
        print("subtraction of two num is",num1-num2)

obj = one()
obj.add()

obj2 = obj.two()
obj2.mul()

obj3 = three()
obj3.sub()