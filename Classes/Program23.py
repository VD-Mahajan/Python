class Test:
    
    def m1(x):
        print("In m1()")
    
Test.m1()   # This line give an error because method m1() is instacne method 
            # In order to remove error we need to write the decorator as classmethod or need to change Test.m1() to Test().m1()