def myfunc(**args):
    print(type(args))
    for k,v in args.items():
        print(f'{k}:{v}')

myfunc(a=1,b=2,c=3)