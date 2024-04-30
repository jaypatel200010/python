from task1 import *

while True: 
    
    menu="""

------------press---------------
    1.reverse
    2.length
    3.middle
    4.concat
    5.exit


"""

    print(menu)

    c = int(input("Enter choice : "))

    if c==1:
        sreverse()

    elif c==2:
        slen()

    elif c==3:
        middle()

    elif c==4:
        smerge()

    elif c==5:
        print("Thank you for using website :")
        break
    else:
        print("Invalid")
        break