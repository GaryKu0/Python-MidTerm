N=input("輸入N及M為:").split(" ")
Martix = [[0 for col in range(int(N[1]))] for row in range(int(N[0]))]
for i in range(int(N[0])):
    Martix[i]=input("輸入Martix為:").split(" ")
for i in range(int(N[0])-1):
    for j in range(int(N[1])):
        print(Martix[i][j]+Martix[i+1][j])

    