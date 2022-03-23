TimeandPeople=input("請輸入考試次數及人數:").split(" ")
Ratio=input("").split(" ")
Data = [[0 for col in range(int(TimeandPeople[0]))] for row in range(int(TimeandPeople[1]))]
sum=0
for i in range(len(Data)):
    Data[i]=input("").split(" ")
for i in range(len(Data)):
    for j in range(len(Data[i])):
        sum+=int(Data[i][j])*float(Ratio[j])
print(round(sum/int(TimeandPeople[1]),2))