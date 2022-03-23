N=input("輸入X*X的矩陣為:").split(" ")
M=input("輸入X*X的矩陣為:").split(" ")
Martix = [[0 for col in range(int(N[1]))] for row in range(int(N[0]))]
Martix2 = [[0 for col in range(int(M[1]))] for row in range(int(M[0]))]
for i in range(int(N[0])):
    Martix[i]=input("輸入Martix為:").split(" ")
for i in range(int(N[0])-1):
    for j in range(int(N[1])):
        print(Martix[i][j]+Martix[i+1][j])
for i in range(int(M[0])):
    Martix2[i]=input("輸入Martix為:").split(" ")
for i in range(int(M[0])-1):
    for j in range(int(M[1])):
        print(Martix2[i][j]+Martix2[i+1][j])
if N[0]==M[0] and N[1]==M[1]:
    print("Martix相加")
    for i in range(int(N[0])):
        for j in range(int(N[1])):
            Martix[i][j]=int(Martix[i][j])+int(Martix2[i][j])
    for i in range(int(N[0])-1):
        for j in range(int(N[1])):
            print(str(Martix[i][j])+str(Martix[i+1][j]))
else:
    print("兩個矩陣無法相加")