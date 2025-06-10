num = int(input("Enter a number whose multiplication table is needed: "))
i = 1
n10 = num*10

while i<=n10:
    if i%num==0:
        print(i)
    i+=1
