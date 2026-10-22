n=int(input())
g=n//(17*29)
n%=17*29
s=n//29
k=n%29
if g>0:
   print(g,"галлеонов")
if s>0:
   print(s,"сиклей")
if k>0:
   print(k,"кнатов")
