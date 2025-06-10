for i in range(1, 51):
    print(i, end="-")
    if i%6==0:
        print("Divisible by both 2 and 3")
    elif i%2==0:
        print("Divisible by 2")
    elif i%3==0:
        print("Divisible by 3")
    else:
        print("Divisible by none")
