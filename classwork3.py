#WAP to find the greatest of four numbers.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
num4 = int(input("Enter num4: "))

if num1==num2 and num2==num3 and num3==num4:
    print("All numbers are same")
elif num1==num2 and num2==num3:
    if num1>num4:
        print("num1, num2, num3 are same and greatest")
    else:
        print("num4 is the greatest")
elif num1==num2 and num2==num4:
    if num1>num3:
        print("num1, num2, num4 are same and greatest")
    else:
        print("num3 is the greatest")
elif num1==num3 and num3==num4:
    if num1>num2:
        print("num1, num3, num4 are same and greatest")
    else:
        print("num2 is the greatest")
elif num2==num3 and num3==num4:
    if num1>num4:
        print("num2, num3, num4 are same and greatest")
    else:
        print("num1 is the greatest")
elif num1==num2 and num3==num4:
    if num1>num3:
        print("num1 and num2 are same and greatest, while num3 and num4 are also same")
    else:
        print("num3 and num4 are same and greatest, while num1 and num2 are also same")
elif num1==num3 and num2==num4:
    if num1>num2:
        print("num1 and num3 are same and greatest, while num2 and num4 are also same")
    else:
        print("num2 and num4 are same and greatest, while num1 and num3 are also same")
elif num1==num4 and num2==num3:
    if num1>num3:
        print("num1 and num4 are same and greatest, while num2 and num3 are also same")
    else:
        print("num2 and num3 are same and greatest, while num1 and num4 are also same")
elif num1==num2:
    if num1>num3 and num1>num4:
        print("num1 and num2 are same and greatest")
    elif num1<num3 and num1>num4:
        print("num3 is the greatest")
    elif num1<num3 and num1<num4:
        if num3>num4:
            print("num3 is the greatest")
        else:
            print("num4 is the greatest")
    else:
        print("num4 is the greatest")
elif num2==num3:
    if num2>num1 and num2>num4:
        print("num2 and num3 are same and greatest")
    elif num2<num1 and num2>num4:
        print("num1 is the greatest")
    elif num2<num1 and num2<num4:
        if num1>num4:
            print("num1 is the greatest")
        else:
            print("num4 is the greatest")
    else:
        print("num4 is the greatest")
elif num3==num4:
    if num3>num1 and num3>num2:
        print("num3 and num4 are same and greatest")
    elif num3<num1 and num3>num4:
        print("num1 is the greatest")
    elif num3<num1 and num3<num2:
        if num1>num2:
            print("num1 is the greatest")
        else:
            print("num2 is the greatest")
    else:
        print("num2 is the greatest")
elif num1==num3:
    if num1>num2 and num1>num4:
        print("num1 and num3 are same and greatest")
    elif num1<num2 and num1>num4:
        print("num2 is the greatest")
    elif num1<num2 and num1<num4:
        if num2>num4:
            print("num2 is the greatest")
        else:
            print("num4 is the greatest")
    else:
        print("num4 is the greatest")
elif num1==num4:
    if num1>num2 and num1>num3:
        print("num1 and num4 are same and greatest")
    elif num1<num3 and num1>num2:
        print("num3 is the greatest")
    elif num1<num2 and num1<num3:
        if num2>num3:
            print("num2 is the greatest")
        else:
            print("num3 is the greatest")
    else:
        print("num3 is the greatest")
elif num2==num4:
    if num2>num1 and num2>num3:
        print("num2 and num4 are same and greatest")
    elif num2<num3 and num2>num1:
        print("num3 is the greatest")
    elif num2<num3 and num2<num1:
        if num3>num1:
            print("num3 is the greatest")
        else:
            print("num1 is the greatest")
    else:
        print("num1 is the greatest")
elif num1>num2 and num1>num3 and num1>num4:
    print("num1 is the greatest")
elif num2>num1 and num2>num3 and num2>num4:
    print("num2 is the greatest")
elif num3>num1 and num3>num2 and num3>num4:
    print("num3 is the greatest")
elif num4>num1 and num4>num2 and num4>num3:
    print("num4 is the greatest")0
    

