class Father:
    fatherName=''
    def father(self):
        print(self.fatherName)
    
class Mother:
    motherName=''
    def mother(self):
        print(self.motherName),

class Child(Father,Mother):

    def parents(self):
        print(f'FatherName : {self.fatherName}')
        print(f'MotherName : {self.motherName}')
    
    
child1=Child()
child1.fatherName='Vishal'
child1.motherName='Xyz'
child1.parents()