import random
l1 = random.randint(1,50)
while True:
    num = int(input("Enter num : "))
    if num < l1:
        print("entered num is lesser!!")
    elif num > l1:
        print("entered num is greater!!")
    elif num == l1:
        print("Congratulation you won!!")
        break
    else:
        print("invalid number")