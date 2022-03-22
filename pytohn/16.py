
def 找出出現次數最多的字串(number):
    count1={}
    max=1
    for y in range(len(number)):
        number[y]=int(number[y])
        if number[y] in count1:
            count1[number[y]]+=1
        else:
            count1[number[y]]=1
        if int(count1[number[y]]) > max:
            max=int(number[y])
    mostnum=count1[max]
    return [max,mostnum]
def 同花順(color,number): #Stright Flush
    for i in range(len(color)-1):
        if color[i]==color[i+1]:
            continue
        else:
            return False
    for i in range(len(number)-1):
        if int(number[i])+1==int(number[i+1]):
            continue
        else:
            return False
    return True
def 四條(number): #Four of a Kind
    #count=0
    #for i in range(len(number)-1):
    #    if number[i]==number[i+1]:
    #        continue
    #    elif number[i]!=number[i+1]:
    #        count+=1
    #    elif count>1:
    #        return False
    if (找出出現次數最多的字串(number)[1]==4):
        return True
    else:
        return False   
def 葫蘆(number): #Full House

    #if list got 3 same number and 2 same number return True
    if number[0]==number[1] and number[1]==number[2]:
        if number[3]==number[4]:
            return True
        else:
            return False
    if number[0]==number[1] and number[1]!=number[2]:
        if number[2]==number[3] and number[3]==number[4]:
            return True
        else:
            return False
def 順子(number): #Straight
    for i in range(len(number)-1):
        if int(number[i])+1==int(number[i+1]):
            continue
        else:
            return False
def 三條(number): #Three of a Kind
    if 找出出現次數最多的字串(number)[1]==3:
        return True
    else:
        return False
def 兩對(number): #Two Pairs
    tmp=找出出現次數最多的字串(number)
    if tmp[1]==2:
        for i in range(len(number)):
            if tmp[0]==number[i]:
                number.remove(number[i])
                break
        for i in range(len(number)):
            if tmp[0]==number[i]:
                number.remove(number[i])
                break
        if 找出出現次數最多的字串(number)[1]==2:
            return True
        else:
            return False
def 一對(number): #One Pair
    if 找出出現次數最多的字串(number)[1]==2:
        return True
    else:
        return False



P1Poker=["S3","H5","S11","D5","C5"]#input('P1Poker:').split(" ")
P2Poker=['H11', 'D11', 'C2', 'H4', 'S4']#input('P2Poker:').split(" ") 
P1PokerColor=[]
P2PokerColor=[]
#P1
for i in range(len(P1Poker)):
    P1PokerColor.append(P1Poker[i][0])
for j in range(len(P1Poker)):
    P1Poker[j]=P1Poker[j][1:]
#P2
for h in range(len(P2Poker)):
    P2PokerColor.append(P2Poker[h][0])
for c in range(len(P2Poker)):
    P2Poker[c]=P2Poker[c][1:]
#整理排
P1Poker.sort();
P2Poker.sort();
print("P1PokerNumber",P1Poker)
print("P2PokerNumber",P2Poker)
P1point=0
P2point=0
if 一對(P1Poker):
    P1point=1
if 兩對(P1Poker):
    P1point=2
if 三條(P1Poker):
    P1point=3
if 順子(P1Poker):
    P1point=4
if 葫蘆(P1Poker):
    P1point=5
if 四條(P1Poker):
    P1point=6
if 同花順(P1PokerColor,P1Poker):
    P1point=7
if 一對(P2Poker):
    P2point=1
if 兩對(P2Poker):
    P2point=2
if 三條(P2Poker):
    P2point=3
if 順子(P2Poker):
    P2point=4
if 葫蘆(P2Poker):
    P2point=5
if 四條(P2Poker):
    P2point=6
if 同花順(P2PokerColor,P2Poker):
    P2point=7
print("P1point",P1point,"P2point",P2point)
if (P1point>P2point):
    print('P1 win')
elif (P1point<P2point):
    print('P2 win')
print(找出出現次數最多的字串(P1Poker))
print(找出出現次數最多的字串(P2Poker))