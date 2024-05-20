def hello(fv):
    def fvx():
        print("welcome!!!!!")
        fv()
        print("thanks!!!!!!")

    fvx()

@hello
def fac():
    n= int(input("Enter number : "))
    fac = 1
    for i in range(1,n+1):
        fac = fac*i
    print(fac)