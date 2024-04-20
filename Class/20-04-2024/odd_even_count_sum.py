# using while loop------------------------------

# i = 1
# evcount = 0
# odcount = 0
# evsum = 0
# odsum = 0

# while (i<=5):
#     n = eval(input("Enter number : "))

#     if (n%2==0):
#         print (n,"Is even")
#         evcount+=1
#         evsum+=n

#     else:
#         print(n, "Is odd")
#         odcount+=1
#         odsum+=n
#     i+=1


# print ("Odd numbers : ",odcount)
# print ("even numbers : ",evcount)
# print ("odd numbers sum : ",odsum)
# print ("even numbers sum : ",evsum)


# using for loop-----------------------------
i=1
evcount = 0
odcount = 0
evsum = 0
odsum = 0
for i in range (1,6,1):
    n = eval(input("Enter number : "))

    if (n%2==0):
        print(n,"Is even")
        evcount+=1
        evsum+=n

    else:
        print(n, "Is odd")
        odcount+=1
        odsum+=n

print ("Odd numbers : ",odcount)
print ("even numbers : ",evcount)
print ("odd numbers sum : ",odsum)
print ("even numbers sum : ",evsum)