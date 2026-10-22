print("PIN-код:")
q=input()
if len(q)==4:
    if int(q)<1900 or int(q)>2050:
        if len(set(q)):
            print("OK")
        else:
            print("ERROR")
    else:
        print("ERROR")
else:
    print("ERROR")