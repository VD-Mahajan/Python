class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def talk(self):
        print(f'My name is {self.name}')
        print(f'My roll no is {self.roll_no}')
        print(f'and marks are {self.marks}')
    
s=Student('Vishal',37,89)
s.talk()
print(id(s))