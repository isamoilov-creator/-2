n,k,m=map(int,input().split())
d=abs(k-m)-1
print(min(d,n-d-2))
