print("Собака короткошерстной породы? ")
a=input()
if a.lower()=="да":
    print("Рост собаки менее 50см?")
    q=input()
    if q.lower()=="да":
        print("У собаки короткий хвост?")
        w=input()
        if w.lower()=="да":
            print("английский бульдог")
        else:
            print("У собаки длинные уши?")
            e=input()
            if e.lower()=="да":
                print("гончая")
            else:
                print("У собаки короткое тело?")
                r=input()
                if r.lower()=="да":
                    print("мопс")
                else:
                    print("чихуахуа")
    else:
        print("Собака весит более 50кг?")
        w=input()
        if w.lower()=="да":
            print("датский дог")
        else:
            print("фоксхаунд")
else:
    print("Рост собаки менее 50см?")
    q=input()
    if q.lower()=="да":
        print("У собаки доброжелательный характер?")
        w=input()
        if w.lower()=="да":
            print("кокер-спаниэль")
        else:
            print("ирландский сеттер")
    else:
        print("У собаки рост менее 70см?")
        e=input()
        if e.lower()=="да":
            print("У собаки длинные уши?")
            r=input()
            if r.lower()=="да":
                print("большой вандейский грифон")
            else:
                print("колли")
        else:
            print("Окрас рыжий с белыми отметинами?")
            t=input()
            if t.lower()=="да":
                print("сенбернар")
            else:
                print("Белоснежный окрас?")
                y=input()
                if y.lower()=="да":
                    print("ирландский волкодав")
                else:
                    print("ньюфаундлер")










    