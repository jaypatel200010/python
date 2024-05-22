from abc import ABC,abstractmethod

class salary(ABC):
    def payroll(self):
        pass

class jay():
    def payroll(self):
        print("Jay got 50000rs")

class ketan():
    def payroll(self):
        print("ketan got 40000rs")

class uday():
    def payroll(self):
        print("uday got 50000rs")

obj = jay()
obj.payroll()
obj1 = ketan()
obj1.payroll()
obj2 = uday()
obj2.payroll()