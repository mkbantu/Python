progress=True
print("============================================")
print("A  DIGITAL MONITORING SYSTEM FOR TEMPERATURE")
while progress:
    try:
        temp=float(input("Enter the temperature :"))
        if temp>=85:
            print("critical temperature-shutdown required")
        elif temp>=70:
            print("high temperature")
        elif temp>=50:
            print("warning")
        else:
            print("normal")
    except:
        print("Invalid input. Please enter a valid temperature.")


    try:
        choice=str(input("Do you want to continue (yes/no) :"))
        if choice.lower() == "no":
            progress=False
    except ValueError:
        print("Invalid input. Please write yes /no for choice.")
    else :
        print()
        print("A  DIGITAL MONITORING SYSTEM FOR TEMPERATURE")
    finally:
        print("============================================")