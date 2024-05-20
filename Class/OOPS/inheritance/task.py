class A:
    def team(self):
        print("Team name = MI")
        print("total team score is : 200")
        b = input("Enter batsman name : ")
        print("batsman name : ",b)
        # c = int(input("enter batsman score : "))
        print("runs : 100")

class B(A):
    def data(self):
        
        print("bowler name is : patel")
        print("no of wickets taken : 5")
        # print("wickets",w)


class C(B):
    def average(self):
        print("Avg is :",200/11)
        print("Man of the match is : Jaykumar ")
        print("Score : 100 runs")
        print("Highest wicket taker is patel: ")
        print("No of wickets 5")



obj = C()
obj.team()
obj.data()
obj.average()