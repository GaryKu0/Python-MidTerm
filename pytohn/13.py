#made value input into list
value = input("輸入一整數序列:")
list=[]
OriList=[]
for i in value:
    list.append(i)
    OriList.append(i)
list.reverse()
if list == OriList:
    print("Yes")
else:
    print("No")
    