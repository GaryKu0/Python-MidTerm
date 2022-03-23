from gettext import find


matrix=input("請輸入陣列大小:")

AllNum=[]
for i in range(int(matrix)):
    Matrix[i]=input("輸入Matrix為:").split(" ")
    for j in range(int(matrix)):
        AllNum.append(int(Matrix[i][j]))
AllNum.sort(reverse=True)
#print(AllNum)
coordinate=[]
Max=int(AllNum[0])+int(AllNum[1])+int(AllNum[2])
for i in range(3):
    Find=AllNum[i]
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            #print("目前搜尋的數字為:",Find,"被搜尋",Matrix[i][j])
            if Matrix[i][j]==str(Find):
                #print("位置為",i+1,",",j+1)
                coordinate.append(str(i+1)+","+str(j+1))
                break
print(str(AllNum[0])+"+"+str(AllNum[1])+"+"+str(AllNum[2])+"="+str(Max))
print(coordinate)