print("Press 1 for English")
print("Press 2 for Hindi")
print("Press 3 for Gujarati")
print()
language = int(input("Enter your choice: "))
print()
match language:
    case 1:
        print("Press 1 for recharge of 28 days")
        print("Press 2 for recharge of 62 days")
        print("Press 3 for recharge of 84 days")
        print()
        recharge_type1 = int(input("Enter your recharge pack number: "))
        print()
        match recharge_type1:
            case 1:
                print("Congratulations your recharge for 28 days is done")
            case 2:
                print("Congratulations your recharge for 62 days is done")
            case 3:
                print("Congratulations your recharge for 84 days is done")
            case _:
                print("Invalid choice")        

    case 2:
        print("28 din k recharge k liye 1 dabae")
        print("62 din k recharge k liye 2 dabae")
        print("84 din k recharge k liye 3 dabae")
        print()
        recharge_type2 = int(input("Apne recharge ka number batae: "))
        print()
        match recharge_type2:
            case 1:
                print("Aapka 28 din ka recharge ho gaya hai, dhanyavad")
            case 2:
                print("Aapka 62 din ka recharge ho gaya hai, dhanyavad")
            case 3:
                print("Aapka 84 din ka recharge ho gaya hai, dhanyavad")
            case _:
                print("Invalid choice")        

    case 3:
        print("28 divas no recharge mate 1 dabavo")
        print("62 divas no recharge mate 2 dabavo")
        print("84 divas no recharge mate 3 dabavo")
        print()
        recharge_type3 = int(input("Tamaro recharge number lakho: "))
        print()
        match recharge_type3:
            case 1:
                print("Abhinandan tamaro 28 divas no recharge thai gayo che")
            case 2:
                print("Abhinandan tamaro 62 divas no recharge thai gayo che")
            case 3:
                print("Abhinandan tamaro 84 divas no recharge thai gayo che")
            case _:
                print("Invalid choice")        

    case _:
        print("Invalid choice")        




    








