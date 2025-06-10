num1 = int(input("Enter value of num1: "))
num2 = int(input("Enter value of num2: "))
print()
print("Press 1 to use +")
print("Press 2 to use -")
print("Press 3 to use *")
print("Press 4 to use /")
print()
symbol = int(input("Enter your choice: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1*num2
division = num1/num2
print()
match symbol:
    case 1:
        print("Addition of ", num1, "and", num2, "is", addition)
    case 2:
        print("Subtraction of ", num1, "and", num2, "is", subtraction)
    case 3:
        print("Multiplication of ", num1, "and", num2, "is", multiplication)
    case 4:
        print("Division of ", num1, "and", num2, "is", division)
