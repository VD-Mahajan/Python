class Demo:
    
    def __init__(self):
        pass
        
    def instance_method(self):
        print("In instance_method")
        
    @classmethod
    def class_method(cls):
        print("In class_method")
       
    @staticmethod 
    def static_method():
        print("In static_method")
    
Demo().instance_method()
Demo.class_method()
Demo.static_method()