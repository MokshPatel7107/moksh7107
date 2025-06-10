num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
num3 = int(input("Enter the value of num3: "))
num4 = int(input("Enter the value of num4: "))
num5 = int(input("Enter the value of num5: "))

if num1==num2 and num2==num3 and num3==num4 and num4==num5:
    print("All five numbers are same")
elif num1==num2 and num2==num3 and num3==num4:
    if num5>num1:
        print("num5 is the greatest number and all others are same")
    else:
        print("num1, num2, num3, num4 are same and greatest")
elif num1==num2 and num2==num3 and num3==num5:
    if num4>num1:
        print("num4 is the greatest number and all others are same")
    else:
        print("num1, num2, num3, num5 are same and greatest")
elif num1==num2 and num2==num4 and num4==num5:
    if num3>num1:
        print("num3 is the greatest number and all others are same")
    else:
        print("num1, num2, num4, num5 are same and greatest")
elif num1==num3 and num3==num4 and num4==num5:
    if num2>num1:
        print("num2 is the greatest number")
    else:
        print("num1, num3, num4, num5 are same and greatest")
elif num2==num3 and num3==num4 and num4==num5:
    if num1>num2:
        print("num1 is the greatest number and all others are same")
    else:
        print("num2, num3, num4, num5 are same and greatest")
elif num1==num2 and num2==num3 and num4==num5:
    if num1>num4:
        print("num1, num2, num3 are same and greatest while num4, num5 are also same")
    else:
        print("num4, num5 are same and greatest while num1, num2, num3 are also same")
elif num1==num2 and num2==num4 and num3==num5:
    if num1>num3:
        print("num1, num2, num4 are same and greatest while num3, num5 are also same")
    else:
        print("num3, num5 are same and greatest while num1, num2, num4 are also same")
elif num1==num2 and num2==num5 and num3==num4:
    if num1>num3:
        print("num1, num2, num5 are same and greatest while num3, num4 are also same")
    else:
        print("num3, num4 are same and greatest while num1, num2, num5 are also same")
elif num2==num3 and num3==num4 and num1==num5:
    if num2>num1:
        print("num2, num3, num4 are same and greatest while num1, num5 are also same")
    else:
        print("num1, num5 are same and greatest while num2, num3, num4 are also same")
elif num2==num3 and num3==num5 and num1==num4:
    if num2>num1:
        print("num2, num3, num5 are same and greatest while num1, num4 are also same")
    else:
        print("num1, num4 are same and greatest while num2, num3, num5 are also same")
elif num3==num4 and num4==num5 and num1==num2:
    if num3>num1:
        print("num3, num4, num5 are same and greatest while num1, num2 are also same")
    else:
        print("num1, num2 are same and greatest while num3, num4, num5 are also same")
elif num1==num4 and num4==num5 and num2==num3:
    if num1>num2:
        print("num1, num4, num5 are same and greatest while num2, num3 are also same")
    else:
        print("num2, num3 are same and greatest while num1, num4, num5 are also same")
elif num1==num3 and num3==num4 and num2==num5:
    if num1>num2:
        print("num1, num3, num4 are same and greatest while num2, num5 are also same")
    else:
        print("num2, num5 are same and greatest while num1, num3, num4 are also same")
elif num1==num3 and num3==num5 and num2==num4:
    if num1>num2:
        print("num1, num3, num5 are same and greatest while num2, num4 are also same")
    else:
        print("num2, num4 are same and greatest while num1, num3, num5 are also same")
elif num2==num4 and num4==num5 and num1==num3:
    if num2>num1:
        print("num2, num4, num5 are same and greatest while num1, num3 are also same")
    else:
        print("num1, num3 are same and greatest while num2, num4, num5 are also same")
elif num1==num2 and num2==num3:
    if num4>num1 and num4>num5:
        print("num4 is the greatest number while num1, num2, num3 are same and num5 is different")
    elif num4>num1 and num4<num5:
        print("num5 is the greatest number while num1, num2, num3 are same and num4 is different")
    elif num4<num1 and num4>num5:
        print("num1, num2, num3 are same and greatest while num4, num5 are different")
    elif num4<num1 and num4<num5:
        if num5>num1:
            print("num5 is the greatest number while num1, num2, num3 are same and num4 is different")
        else:
            print("num1, num2, num3 are same and greatest while num4, num5 are different")
    else:
        print("num1, num2, num3 are same and greatest while num4, num5 are different")
elif num1==num2 and num2==num4:
    if num3>num1 and num3>num5:
        print("num3 is the greatest number while num1, num2, num4 are same and num5 is different")
    elif num3>num1 and num3<num5:
        print("num5 is the greatest number while num1, num2, num4 are same and num3 is different")
    elif num3<num1 and num3>num5:
        print("num1, num2, num4 are same and greatest while num 3, num5 are different")
    elif num3<num1 and num3<num5:
        if num5>num1:
            print("num5 is the greatest number while num1, num2, num4 are same and num3 is different")
        else:
            print("num1, num2, num4 are same and greatest while num 3, num5 are different")
    else:
        print("num1, num2, num4 are same and greatest while num 3, num5 are different")
elif num1==num2 and num2==num5:
    if num3>num1 and num3>num4:
        print("num3 is the greatest number while num1, num2, num5 are same and num4 is different")
    elif num3>num1 and num3<num4:
        print("num4 is the greatest number while num1, num2, num5 are same and num3 is different")
    elif num3<num1 and num3>num4:
        print("num1, num2, num5 are same and greatest while num3, num4 are different")
    elif num3<num1 and num3<num4:
        if num4>num1:
            print("num4 is the greatest number while num1, num2, num5 are same and num3 is different")
        else:
            print("num1, num2, num5 are same and greatest while num3, num4 are different")
    else:
        print("num1, num2, num5 are same and greatest while num3, num4 are different")
elif num2==num3 and num3==num4:
    if num1>num2 and num1>num5:
        print("num1 is the greatest number while num2, num3, num4 are same and num5 is different")
    elif num1>num2 and num1<num5:
        print("num5 is the greatest number while num2, num3, num4 are same and num1 is different")
    elif num1<num2 and num1>num5:
        print("num2, num3, num4 are same and greatest while num1, num5 are different")
    elif num1<num2 and num1<num5:
        if num5>num2:
            print("num5 is the greatest number while num2, num3, num4 are same and num1 is different")
        else:
            print("num2, num3, num4 are same and greatest while num1, num5 are different")
    else:
        print("num2, num3, num4 are same and greatest while num1, num5 are different")
elif num2==num3 and num3==num5:
    if num1>num2 and num1>num4:
        print("num1 is the greatest number while num2, num3, num5 are same and num4 is different")
    elif num1>num2 and num1<num4:
        print("num4 is the greatest number while num2, num3, num5 are same and num1 is different")
    elif num1<num2 and num1>num4:
        print("num2, num3, num5 are same and greatest while num1, num4 are different")
    elif num1<num2 and num1<num4:
        if num4>num2:
            print("num4 is the greatest number while num2, num3, num5 are same and num1 is different")
        else:
            print("num2, num3, num5 are same and greatest while num1, num4 are different")
    else:
        print("num2, num3, num5 are same and greatest while num1, num4 are different")
elif num3==num4 and num4==num5:
    if num1>num3 and num1>num2:
        print("num1 is the greatest number while num3, num4, num5 are same and num2 is different")
    elif num1>num3 and num1<num2:
        print("num2 is the greatest number while num3, num4, num5 are same and num1 is different")
    elif num1<num3 and num1>nu3:
        print("num3, num4, num5 are same and greatest while num1, num2 are differnt")
    elif num1<num3 and num1<num2:
        if num2>num3:
            print("num2 is the greatest number while num3, num4, num5 are same and num1 is different")
        else:
            print("num3, num4, num5 are same and greatest while num1, num2 are different")
    else:
        print("num3, num4, num5 are same and greatest while num1, num2 are different")
elif num1==num4 and num4==num5:
    if num2>num1 and num2>num3:
        print("num2 is the greatest number while num1, num4, num5 are same and num3 is different")
    elif num2>num1 and num2<num3:
        print("num3 is the greatest number while num1, num4, num5 are same and num2 is different")
    elif num2<num1 and num2>num3:
        print("num1, num4, num5 are same and greatest while num2, num3 are different")
    elif num2<num1 and num2<num3:
        if num3>num1:
            print("num3 is the greatest number while num1, num4, num5 are same and num2 is different")
        else:
            print("num1, num4, num5 are same and greatest while num2, num3 are different")
    else:
        print("num1, num4, num5 are same and greatest while num2, num3 are different")
elif num1==num3 and num3==num4:
    if num2>num1 and num2>num5:
        print("num2 is the greatest number while num1, num3, num4 are same and num5 is different")
    elif num2>num1 and num2<num5:
        print("num5 is the greatest number while num1, num3, num4 are same and num2 is different")
    elif num2<num1 and num2>num5:
        print("num1, num3, num4 are same and greatest while num2, num5 are different")
    elif num2<num1 and num2<num5:
        if num5>num1:
            print("num5 is the greatest number while num1, num3, num4 are same and num2 is different")
        else:
            print("num1, num3, num4 are same and greatest while num2, num5 are different")
    else:
        print("num1, num3, num4 are same and greatest while num2, num5 are different")
elif num1==num3 and num3==num5:
    if num2>num1 and num2>num4:
        print("num2 is the greatest number while num1, num3, num5 are same and num4 is different")
    elif num2>num1 and num2<num4:
        print("num4 is the greatest number while num1, num3, num5 are same and num2 is different")
    elif num2<num1 and num2>num4:
        print("num1, num3, num5 are same and greatest while num2, num4 are different")
    elif num2<num1 and num2<num4:
        if num4>num1:
            print("num4 is the greatest number while num1, num3, num5 are same and num2 is different")
        else:
            print("num1, num3, num5 are same and greatest while num2, num4 are different")
    else:
        print("num1, num3, num5 are same and greatest while num2, num4 are different")
elif num2==num4 and num4==num5:
    if num1>num2 and num1>num3:
        print("num1 is the greatest number while num2, num4, num5 are same and num3 is different")
    elif num1>num2 and num1<num3:
        print("num3 is the greatest number while num2, num4, num5 are same and num1 is different")
    elif num1<num2 and num1>num3:
        print("num2, num4, num5 are same and greatest while num1, num3 are different")
    elif num1<num2 and num1<num3:
        if num3>num2:
            print("num3 is the greatest number while num2, num4, num5 are same and num1 is different")
        else:
            print("num2, num4, num5 are same and greatest while num1, num3 are different")
    else:
        print("num2, num4, num5 are same and greatest while num1, num3 are different")
elif num1==num2:
    if num1>num3 and num1>num4 and num1>num5:
        print("num1 and num2 are same and greatest while num3, num4, num5 are different")
    elif num1<num3 and num3>num4 and num3>num5:
        print("num3 is the greatest while num1, num2 are same and num4, num5 are different")
    elif num1<num4 and num4>num3 and num4>num5:
        print("num4 is the greatest while num1, num2 are same and num3, num5 are different")
    elif num1<num5 and num5>num3 and num5>num4:
        print("num5 is the greatest while num1, num2 are same and num3, num4 are different")
    else:
        print("num1 and num2 are same and greatest while num3, num4, num5 are different")
elif num1==num3:
    if num1>num2 and num1>num4 and num1>num5:
        print("num1 and num3 are same and greatest while num2, num4, num5 are different")
    elif num1<num2 and num2>num4 and num2>num5:
        print("num2 is the greatest while num1, num3 are same and num4, num5 are different")
    elif num1<num4 and num4>num2 and num4>num5:
        print("num4 is the greatest while num1, num3 are same and num2, num5 are different")
    elif num1<num5 and num5>num2 and num5>num4:
        print("num5 is the greatest while num1, num3 are same and num2, num4 are different")
    else:
        print("num1 and num3 are same and greatest while num2, num4, num5 are different")
elif num1==num4:
    if num1>num2 and num1>num3 and num1>num5:
        print("num1 and num4 are same and greatest while num2, num3, num5 are different")
    elif num1<num2 and num2>num3 and num2>num5:
        print("num2 is the greatest while num1, num4 are same and num3, num5 are different")
    elif num1<num3 and num3>num2 and num3>num5:
        print("num3 is the greatest while num1, num4 are same and num2, num5 are different")
    elif num1<num5 and num5>num2 and num5>num3:
        print("num5 is the greatest while num1, num4 are same and num2, num3 are different")
    else:
        print("num1 and num4 are same and greatest while num2, num3, num5 are different")
elif num1==num5:
    if num1>num2 and num1>num3 and num1>num4:
        print("num1 and num5 are same greatest while num2, num3, num4 are different")
    elif num1<num2 and num2>num3 and num2>num4:
        print("num2 is the greatest while num1, num5 are same and num3, num4 are different")
    elif num1<num3 and num3>num2 and num3>num4:
        print("num3 is the greatest while num1, num5 are same and num2, num4 are different")
    elif num1<num4 and num4>num2 and num4>num3:
        print("num4 is the greatest while num1, num5 are same and num2, num3 are different")
    else:
        print("num1 and num5 are same and greatest while num2, num3, num4 are different")
elif num2==num3:
    if num2>num1 and num2>num4 and num2>num5:
        print("num2 and num3 are same and greatest while num1, num4, num5 are different")
    elif num2<num1 and num1>num4 and num1>num5:
        print("num1 is the greatest while num2, num3 are same and num4, num5 are different")
    elif num1<num4 and num4>num2 and num4>num5:
        print("num4 is the greatest while num2, num3 are same and num4, num5 are different")
    elif num1<num5 and num5>num2 and num5>num4:
        print("num5 is the greatest while num2, num3 are same and num1, num4 are different")
    else:
        print("num2 and num3 are same and greatest while num1, num4, num5 are different")
elif num2==num4:
    if num2>num1 and num2>num3 and num2>num5:
        print("num2 and num4 are same and greatest while num1, num3, num5 are different")
    elif num2<num1 and num1>num3 and num1>num5:
        print("num1 is the greatest while num2, num4 are same and num1, num5 are different")
    elif num1<num3 and num3>num2 and num3>num5:
        print("num3 is the greatest while num2, num4 are same and num1, num5 are different")
    elif num1<num5 and num5>num2 and num5>num3:
        print("num5 is the greatest while num2, num4 are same and num1, num3 are different")
    else:
        print("num2 and num4 are same and greatest while num1, num3, num5 are different")
elif num2==num5:
    if num2>num1 and num2>num3 and num2>num4:
        print("num2 and num5 are same and greatest while num1, num3, num4 are different")
    elif num2<num1 and num1>num3 and num1>num4:
        print("num1 is the greatest while num2, num5 are same and num3, num4 are different")
    elif num1<num3 and num3>num2 and num3>num4:
        print("num3 is the greatest while num2, num5 are same and num1, num4 are different")
    elif num1<num4 and num4>num2 and num4>num3:
        print("num4 is the greatest while num2, num5 are same and num1, num3 are different")
    else:
        print("num2 and num5 are same and greatest while num1, num3, num4 are different")
elif num3==num4:
    if num3>num1 and num3>num2 and num3>num5:
        print("num3 and num4 are same and greatest while num1, num2, num5 are different")
    elif num2<num1 and num1>num3 and num1>num5:
        print("num1 is the greatest while num3, num4 are same and num2, num5 are different")
    elif num1<num2 and num2>num3 and num2>num5:
        print("num2 is the greatest while num3, num4 are same and num1, num5 are different")
    elif num1<num5 and num5>num2 and num5>num3:
        print("num5 is the greatest while num3, num4 are same and num1, num2 are different")
    else:
        print("num3 and num4 are same and greatest while num1, num2, num5 are different")
elif num3==num5:
    if num3>num1 and num3>num2 and num3>num4:
        print("num3 and num5 are and same greatest while num1, num2, num4 are different")
    elif num2<num1 and num1>num3 and num1>num4:
        print("num1 is the greatest while num3, num5 are same and num2, num4 are different")
    elif num1<num2 and num2>num3 and num2>num4:
        print("num2 is the greatest while num3, num5 are same and num1, num4 are different")
    elif num1<num4 and num4>num2 and num4>num3:
        print("num4 is the greatest while num3, num5 are same and num1, num2 are different")
    else:
        print("num3 and num5 are same and greatest while num1, num2, num4 are different")
elif num4==num5:
    if num4>num1 and num4>num2 and num4>num3:
        print("num4 and num5 are same and greatest while num1, num2, num3 are different")
    elif num2<num1 and num1>num3 and num1>num4:
        print("num1 is the greatest while num4, num5 are same and num2, num3 are different")
    elif num1<num2 and num2>num3 and num2>num4:
        print("num2 is the greatest while num4, num5 are same and num1, num3 are different")
    elif num1<num3 and num3>num2 and num3>num4:
        print("num3 is the greatest while num4, num5 are same and num1, num2 are different")
    else:
        print("num4 and num5 are same and greatest while num1, num2, num3 are different")
elif num1>num2 and num1>num3 and num1>num4 and num1>num5:
    print("num1 is the greatest and all other are different")
elif num2>num1 and num2>num3 and num2>num4 and num2>num5:
    print("num2 is the greatest and all other are different")
elif num3>num1 and num3>num2 and num3>num4 and num3>num5:
    print("num3 is the greatest and all other are different")
elif num4>num1 and num4>num2 and num4>num3 and num4>num5:
    print("num4 is the greatest and all other are different")
elif num5>num1 and num5>num2 and num5>num3 and num5>num4:
    print("num5 is the greatest and all other are different")
    






























