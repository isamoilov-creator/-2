s=input()
dx=abs(ord(s[0])-ord(s[3]))
dy=abs(int(s[1])-int(s[4]))
print("верно" if (dx==1 and dy==2) or (dx==2 and dy==1) else "ошибка")
