class A:
    def team(self):
        print("Team name = MI")
        print("total team score is : 200")
        b = input("Enter batsman name : ")
        print("batsman name : ",b)
        c = int(input("enter batsman score : "))
        print("score",c)

class B(A):
    def data(self):
        d = input("Enter bowler name : ")
        print("bowler name is : ",d)
        w = int(input("enter no of wicets taken : "))
        print("wickets",w)


class C(B):
    def average(self):
        print("Avg is :",200/11)