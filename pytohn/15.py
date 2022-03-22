password=input("輸入一四位數:")
list=[]
for i in password:
    list.append(i)
for i in range(len(list)):
    list[i]=(int(list[i])+7)%10
print ("輸出加密後的數字為:"+str(list[2])+str(list[3])+str(list[0])+str(list[1]))
    