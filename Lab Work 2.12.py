age = int(input("Enter your age: "))

if age<=12:
    print("You are child")
elif age>=13 and age<=19:
    print("You are teenager")
elif age>=20 and age<=59:
    print("You are adult")
else:
    print("You are senior")
