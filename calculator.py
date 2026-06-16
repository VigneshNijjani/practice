from functools import reduce







while True:
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.division")
    print("5.factorial")
    print("6.exit")
    choice=int(input("enter your choice :"))

    if choice==1:
        a=list(map(int,input("enter your number seperated by spaces :").split()))
        addition=lambda *args :reduce(lambda x,y:x+y,args)
        print("result",addition(*a))

    elif choice==2:
        a=list(map(int,input("enter your number seperated by spaces :").split()))
        subtraction=lambda *args :reduce(lambda x,y:x-y,args)
        print("result",subtraction(*a))
        
    elif choice==3:
        a=list(map(int,input("enter your number seperated by spaces :").split()))
        multiplication=lambda *args :reduce(lambda x,y:x*y,args)
        print("result",multiplication(*a))
        
    elif choice==4:
        a=list(map(int,input("enter your number seperated by spaces :").split()))
        division=lambda *args :reduce(lambda x,y:x/y,args)
        try:
            print("result",division(*a))
        except ZeroDivisionError:
            print("zero division error")        

    elif choice==5:
        a=int(input("enter a single number :"))
        def factorial(number,result=1):
            if number==1:
                return result
            return factorial(number-1,result*number)
        
        print("result",factorial(a))
    
    elif choice==6:
        break

    else:
        print("fuck u")
    

