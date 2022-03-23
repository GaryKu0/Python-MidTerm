HowMany=input("How many Data to you need to process?")
Data = [[0 for col in range(4)] for row in range(int(HowMany))]
for i in range(int(HowMany)):
    for j in range(4):
        Data[i][j]=input("輸入第"+str(i+1)+"筆資料的第"+str(j+1)+"個數字:")
for i in range(int(HowMany)):
    if int(Data[i][1])-int(Data[i][0])==int(Data[i][2])-int(Data[i][1]) and int(Data[i][2])-int(Data[i][1])==int(Data[i][3])-int(Data[i][2]) :
        answer="此為等差數列"
        Data[i].append(int(Data[i][3])+(int(Data[i][3])-int(Data[i][2])))
    elif int(Data[i][1])/int(Data[i][0])==int(Data[i][2])/int(Data[i][1]) and int(Data[i][2])/int(Data[i][1])==int(Data[i][3])/int(Data[i][2]):
        answer="此為等比數列"
        Data[i].append(int(Data[i][3])*(int(Data[i][3])/int(Data[i][2])))
    print(Data[i])
    print(answer)