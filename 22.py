n,k,m=map(int,input().split())
if n<=k:
    s=2
elif (2*n)%k==0:
    s=(2*n)//k
else:
    s=(2*n)//k+1
print(s*m)
