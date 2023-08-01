#CALCULATOR IN PYTHON
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "CANNOT DIVIDE BY ZERO(INFINITE)"
def calci():
    print("*****WELCOME TO PYTHON CALCULATOR*****")
    print("\nOPERATIONS IN CALCULATOR:\n")
    print("1.ADDITION(+)\n2.SUBTRACTION(-)\n3.MULTIPLICATION(*)\n4.DIVISION(/)\n5.EXIT\n")
    while True:
        ch=int(input("ENTER YOUR CHOICE FROM ABOVE OPERATIONS:\n"))
        if ch==5:
            print("BYE!!BYE!!")
            break
        if ch not in [1,2,3,4]:
            print("INVALID CHOICE ! PLEASE CHOOSE CORRECT OPTION")
            continue
        n1=float(input("ENTER FIRST NUMBER:"))
        n2=float(input("ENTER SECOND NUMBER:"))
        if ch==1:
            print("RESULT:",add(n1,n2))
        elif ch==2:
            print("RESULT:",subtract(n1,n2))
        elif ch==3:
            print("RESULT:",multiply(n1,n2))
        elif ch==4:
            print("RESULT:",divide(n1,n2))
calci()