def sum(num1,num2):
    a,b=num1,num2
    return a+b

def substruct(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2


while True:
    print("enter two number and choose operator")
    a=float(input("first number:"))
    b=float(input("second number:"))
    print("1:ADDITION")
    print("2:sUBSTRACTION")
    print("3:Multiplication")
    choose=input("choose operation:")

    if choose=="1" :
        try:
            print(f"the sum is{sum(a,b)}")
        except:
            print("invalid input")
        finally:
            print("operation complete")
    elif choose=="2":
        try:
            print(f"the substruction is{substruct(a,b)}")
        except:
            print("invalid input")
        finally:
            print("operation complete")
    elif choose=="3":
        try:
            print(f"the Multiplication is{multiply(a,b)}")
        except:
            print("invalid input")
        finally:
            print("operation complete")
    elif choose=="q":
        try:
            exit()
        except:
            print("invalid input")
        finally:
            print("operation complete")
    else:
        print("pleaaaase chooooose !!!!!!!!")
    

    last=input("Do you wish to continue y/n")
    try:
        if last.lower()=="y":
            print("============================================")
        else:
            exit()
    except:
        exit()
