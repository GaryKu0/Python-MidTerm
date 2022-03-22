summer=[2.1,3.02,4.39,4.97,5.63]
NotSummer=[2.10,2.68,3.61,4.01,4.50]
number=int(input("輸入一個數"))
summerMonth=0
Notsummermonth=0
if number<120 and number>0:
    Notsummermonth=int(number)*NotSummer[0]
    summermonth=int(number)*summer[0]
elif number<330:
    Notsummermonth=120*NotSummer[0]+(int(number)-120)*NotSummer[1]
    summermonth=120*summer[0]+(int(number)-120)*summer[1]
elif number<500:
    Notsummermonth=120*NotSummer[0]+210*NotSummer[1]+(int(number)-330)*NotSummer[2]
    summermonth=120*summer[0]+210*summer[1]+(int(number)-330)*summer[2]
elif number<700:
    Notsummermonth=120*NotSummer[0]+210*NotSummer[1]+170*NotSummer[2]+(int(number)-500)*NotSummer[3]
    summermonth=120*summer[0]+210*summer[1]+170*summer[2]+(int(number)-500)*summer[3]
elif number>700:
    Notsummermonth=120*NotSummer[0]+210*NotSummer[1]+170*NotSummer[2]+200*NotSummer[3]+(int(number)-700)*NotSummer[4]
    summermonth=120*summer[0]+210*summer[1]+170*summer[2]+200*summer[3]+(int(number)-700)*summer[4]
print("Non-Summer:",Notsummermonth)
print("Summer:",summermonth)