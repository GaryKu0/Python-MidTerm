List=['56','56','34','34','23']#input("輸入一整數序列:").split(" ")
count={}
Howmany=len(List)
max=1 
mostnum=0
for i in range(len(List)):
    if List[i] in count:
        count[List[i]]+=1
    else:
        count[List[i]]=1
    if int(count[List[i]]) > max:
        max=int(List[i])
mostnum=count[str(max)]

if Howmany/2 <= mostnum:
    print ("過半元素:",max)
else:
    print ("過半元素:NO")