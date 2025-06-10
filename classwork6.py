num = int(input("Enter your number: "))

i = 1

while i<=num:
    if i%3==0 and i%5==0:
        print(i)
    i+=1


n = int(input("Enter your number: "))

for i in range (1, n, 15):
    print(i)
