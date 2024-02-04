class Company:
    
    @staticmethod
    def disp():
        print("In static method")
    
class Employee(Company):
    pass

obj = Employee()
obj.disp()                          #o/p ===> In static method