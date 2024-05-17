#exception handling
#Try, except, else and finally
#used to handle errors from user side.

try:
    n1 = int(input("Enter num 1 : "))
    n2 = int(input("Enter num 2 : "))

    print("Addition : ",n1+n2)

except:
    print("invalid input!!")

else:
    print("Try executed")

finally:
    print("Finally executed!!!")

# try:
#     l = [1,2,3,4,5]

#     n=int(input("enter index number : "))
#     print("value is : ",l[n])

# except:

#     print("Invalid input!!")
