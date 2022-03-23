Data=[[],[]]
answer=""
for i in range(2):
    Data[i]=input("請輸入數字：")
def WinLoseTie(a,b):
    if b=="1" and a=="5":
            return "輸"
    elif int(a)==int(b)+1: 
        return "贏"
    elif int(a)==int(b)-1:
        return "輸"
    else:
        return "和"
for i in range(len(Data[0])):
    answer+=WinLoseTie(Data[0][i],Data[1][i])
print(answer)
    
    