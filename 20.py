print("Клетка:")
k=input()
k1=k[0]
k2=k[1]
if int(k2)%2==1:
    if k1 in "aceg":
        print("Черный")
    if k1 in "bdfh":
        print("Белый")
else:
    if int(k2)%2==0:
        if k1 in "aceg":
            print("Белый")
    if k1 in "bdfh":
        print("Черный")



