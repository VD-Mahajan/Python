while True:
    try:
        age = int(input())
        break
    except ValueError:
        print('Oops!')
    else:
        print('No Exception found')         # Code is unreachable  (does not give error)
    finally:
        print('finally')
    
print(age)