class Company:
    def __init__(self, compName, compLoc):
        self.compName = compName
        self.compLoc = compLoc
    
    def disp(self):
        print(self.compName)
        print(self.compLoc)
    
class Employee(Company):
    pass

obj = Employee('Google','Pune')
obj.disp()