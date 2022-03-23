A=1
J=11
Q=12
K=13
card=input("輸入一副牌:").split(" ")
sum=0
for i in card:
    if i=="A":
        sum+=1
    elif i=="J":
        sum+=11
    elif i=="Q":
        sum+=12
    elif i=="K":
        sum+=13
    else:
        sum+=int(i)
print(sum)