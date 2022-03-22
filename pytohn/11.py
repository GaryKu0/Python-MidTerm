#zodiac search
zodiac=["Sagittarius","Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio" ]
month,day=map(int,input("輸入月即日為:").split())
print(month,day)
if month==1:
    if day<20:
        print("星座為:",zodiac[0])
    else:
        print("星座為:",zodiac[1])
elif month==2: 
    if day<19:
        print("星座為:",zodiac[1])
    else:
        print("星座為:",zodiac[2])
elif month==3:
    if day<20:
        print("星座為:",zodiac[2])
    else:
        print("星座為:",zodiac[3])
elif month==4:
    if day<20:
        print("星座為:",zodiac[3])
    else:
        print("星座為:",zodiac[4])
elif month==5:
    if day<21:
        print("星座為:",zodiac[4])
    else:
        print("星座為:",zodiac[5])
elif month==6:
    if day<21:
        print("星座為:",zodiac[5])
    else:
        print("星座為:",zodiac[6])
elif month==7:
    if day<22:
        print("星座為:",zodiac[6])
    else:
        print("星座為:",zodiac[7])
elif month==8:
    if day<23:
        print("星座為:",zodiac[7])
    else:
        print("星座為:",zodiac[8])
elif month==9:
    if day<23:
        print("星座為:",zodiac[8])
    else:
        print("星座為:",zodiac[9])
elif month==10:
    if day<23:
        print("星座為:",zodiac[8])
    else:
        print("星座為:",zodiac[9])
elif month==11:
    if day<22:
        print("星座為:",zodiac[9])
    else:
        print("星座為:",zodiac[10])
elif month==12:
    if day<22:
        print("星座為:",zodiac[10])
    else:
        print("星座為:",zodiac[11])
    