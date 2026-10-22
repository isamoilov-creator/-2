n=int(input())
if 11<=n%100<=14:
    print(f"{n} попугаев")
elif n%10==1:
    print(f"{n} попугай")
elif 2<=n%10<=4:
    print(f"{n} попугая")
else:
    print(f"{n} попугаев")
