n,m=map(int,input().split('x'))
k=int(input())
print("успешно" if k<n*m and (k%n==0 or k%m==0) else "неосуществимо")
