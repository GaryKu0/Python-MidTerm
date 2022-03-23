a=int(input("輸入第一行正整數為:"))
Value=input("第二行中數列中的數字為:").split(" ")
count={}
max=1 
mostnum=0
for i in range(len(Value)):
    if Value[i] in count:
        count[Value[i]]+=1
    else:
        count[Value[i]]=1
    if int(count[Value[i]]) > max:
        max=int(Value[i])
        mostnum=count[Value[i]]
mostnum=count[str(max)]
if mostnum==0:
    print ("每隔數字剛好只出現一次")
else:
    print ("最大出現次數的數字為:",max)
    print("出現次數為:",mostnum)