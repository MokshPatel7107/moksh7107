print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print()
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            row = int(input("Enter the number of rows for the pattern: "))
            print()
            print("Pattern:")
            for i in range(1, row+1):
                for j in range(1, i+1):
                    print("*", end="")
                print()
        case 2:
            print()
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            i = start
            while i>=start and i<=end:
                if i%2==0:
                    print("Number", i, "is Even")
                else:
                    print("Number", i, "is Odd")
                i+=1

            n = end - start + 1
            add = int(n/2*(start + end)) 

            print("Sum of all numbers from", start, "to", end, "is:", add)
        case _:
            print("Exiting the program. Goodbye!")
            break
