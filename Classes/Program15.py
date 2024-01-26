class Company:
    '''This is Company class'''
    def init(self):
        self.empId = 100
        self.empName = 'Shashi'
        self.empSal = 100000
        
c = Company()
print(c.__doc__)
print(c.__dict__)