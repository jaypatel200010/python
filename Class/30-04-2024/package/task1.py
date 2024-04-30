def sreverse():
    n = input("Enter number : ")

    print("Reverse string is : ",n[::-1])

def slen():
    n = input("Enter string : ")
    print("length of string is : ",len(n))

def middle():
    n = input("Enter string : ")

    n1 = int(len(n)/2)
    print(n[n1-1]+n[n1]+n[n1+1])

def smerge():
    n = input("Enter string 1 : ")
    n1 = input("Enter string 2 : ")

    print("Merged string is",n+n1)

    