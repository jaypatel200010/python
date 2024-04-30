def prime():
    a = int(input("Enter number 1 : "))
    c = 0

    for i in range(1,a+1):
        if(a%i==0):
            c+=1
    if c==2:
        return "Number is prime"
        
    else:
        return "Number is not prime"
        
print(prime())