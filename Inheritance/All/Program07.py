class Father:
    fatherName=''
    
class Mother:
    motherName=''

class Child(Father,Mother):
    def __init__(self):
        self.fatherName='Vishal'
        self.motherName='Xyz'

    def displayData(self):
        print(f'FatherName : {self.fatherName}')
        print(f'MotherName : {self.motherName}')
    
    
child1=Child()
child1.displayData()