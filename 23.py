k=int(input())
if k==1:
    print(0)
elif k<=10:
    print(k-1)
elif k<=190:
    k-=11
    n=10+k//2
    print(n if k%2==0 else n%10)
else:
    k-=191
    n=100+k//3
    if k%3==0:
        print(n//100)
    elif k%3==1:
        print((n//10)%10)
    else:
        print(n%10)
