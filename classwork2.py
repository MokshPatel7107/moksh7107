#WAP to find the minimum of three numbers.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if num1==num2 and num2==num3:
    print("All three number are same")
elif num1==num2:
    if num1<num3:
        print("num1 and num2 are same and smallest")
    else:
        print("num3 is the smallest")
elif num2==num3:    
    if num2<num1:
        print("num2 and num3 are same and smallest")
    else:
        print("num1 is the smallest")
elif num3==num1:
    if num3<num2:
        print("num3 and num1 are same and smallest")
    else:
        print("num2 is the smallest")
else:
    if num1<num2 and num1<num3:
        print("num1 is the smallest")
    elif num2<num3 and num2<num3:
        print("num2 is the smallest")
    else:
        print("num3 is the smallest")
    
