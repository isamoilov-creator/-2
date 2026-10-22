n=int(input("Число: "))
d1=n//1000
d2=(n//100)%10
d3=(n//10)%10
d4=n%10
if d1==d4 and d2==d3:
    print("настоящее")
else:
    print("кривое")







#a=input("Число: ")
#if a==a[::-1]:
#    print("Настоящее")
#else:
#    print("Кривое")
