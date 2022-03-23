ScoreType=['國文','英文','微積分','體育','程式設計']
s=-99999
Score=[]
sum=0
for i in range(5):
    while s>100 or s<0:
        s=int(input(ScoreType[i]+":"))
        if (s>100 or s<0):
            print("ERROR")
        else:
            Score.append(s)
    s=-99999
    sum=sum+Score[i]
print("Average:",sum/5)
Score.sort()
print("Highest:",Score[4])
print("Lowest:",Score[0])
        