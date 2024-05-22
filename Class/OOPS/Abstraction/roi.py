from abc import ABC,abstractmethod

class RBI():
    def roi(self):
        pass

class SBI():
    def roi(self):
        print("SBI got 7.0%")

class kotak():
    def roi(self):
        print("kotak got 8.0%")

class HDFC():
    def roi(self):
        print("HDFC got 7.5%")

obj = SBI()
obj.roi()
obj1 = kotak()
obj1.roi()
obj2 = HDFC()
obj2.roi()