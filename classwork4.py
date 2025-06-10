print("Press 1 to order Pizza")
print("Press 2 to order Burger")
print("Press 3 to order Sandwich")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print()
        print("***********************************")
        print("Press 1 to order Fresh Dough Pizza")
        print("Press 2 to order Thin Crust Pizza")
        print("Press 3 to order Cheese Burst Pizza")
        print("***********************************")
        print()
        pizza_type = int(input("Place your order: "))
        print()
        match pizza_type:
            case 1:
                print("You ordered Fresh Dough Pizza")
                print("Thank you!!!")
            case 2:
                print("You ordered Thin Crust Pizza")
                print("Thank you!!!")
            case 3:
                print("You ordered Cheese Burst Pizza")
                print("Thank you!!!")
    case 2:
        print()
        print("***********************************")
        print("Press 1 to order Cheese Burger")
        print("Press 2 to order Panner Tikka Burger")
        print("Press 3 to order Maharaja Burger")
        print("***********************************")
        print()
        burger_type = int(input("Place your order: "))
        print()
        match burger_type:
            case 1:
                print("You ordered Cheese Burger")
                print("Thank you!!!")
            case 2:
                print("You ordered Panner Tikka Burger")
                print("Thank you!!!")
            case 3:
                print("You ordered Maharaja Burger")
                print("Thank you!!!")
    case 3:
        print()
        print("***********************************")
        print("Press 1 to order Veg Sandwich")
        print("Press 2 to order Grilled Sandwich")
        print("Press 3 to order Cheese Grilled Sandwich")
        print("***********************************")
        print()
        sandwich_type = int(input("Place your order: "))
        print()
        match sandwich_type:
            case 1:
                print("You ordered Veg Sandwich")
                print("Thank You")
            case 2:
                print("You ordered Grilled Sandwich")
                print("Thank You")
            case 3:
                print("You ordered Cheese Grilled Sandwich")
                print("Thank You")
    case _:
        print("Invalid choice...")

