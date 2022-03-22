number=[11,3,	5,5,	5]
count1={}
max=1
for y in range(len(number)):
    if number[y] in count1:
        count1[number[y]]+=1
    else:
        count1[number[y]]=1
    if int(count1[number[y]]) > max:
        max=int(number[y])
mostnum=count1[str(max)]