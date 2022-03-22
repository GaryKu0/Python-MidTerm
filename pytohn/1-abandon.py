number = 15693 #input("輸入一個數")
# list all prime number from 1 to number
prime_list = []
for i in range(1, int(number)+1):
    if i == 1:
        prime_list.append(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
prime_list.reverse()
# separate number to single number
seNum = []
for i in range(len(number)):
    seNum.append(number[i])
print(prime_list)
HowmanyPrime = len(prime_list)
print(HowmanyPrime)
countnumber = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
               '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for i in seNum:
    if i == "1":
        countnumber['1'] += 1
    elif i == '2':
        countnumber['2'] += 1
    elif i == '3':
        countnumber['3'] += 1
    elif i == '4':
        countnumber['4'] += 1
    elif i == '5':
        countnumber['5'] += 1
    elif i == '6':
        countnumber['6'] += 1
    elif i == '7':
        countnumber['7'] += 1
    elif i == '8':
        countnumber['8'] += 1
    elif i == '9':
        countnumber['9'] += 1
    elif i == '0':
        countnumber['0'] += 1
print(countnumber)

sePrime=[]
finalPrime=0
for i in range(len(str(prime_list))):
    for a in range(len(str(prime_list[i]))):
        sePrime.append(number[a])
    countPrime={'0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
               '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    finalPrime=prime_list[i]
    for i in sePrime:
        if i == "1":
            countPrime['1'] += 1
        elif i == '2':
            countPrime['2'] += 1
        elif i == '3':
            countPrime['3'] += 1
        elif i == '4':
            countPrime['4'] += 1
        elif i == '5':
            countPrime['5'] += 1
        elif i == '6':
            countPrime['6'] += 1
        elif i == '7':
            countPrime['7'] += 1
        elif i == '8':
            countPrime['8'] += 1
        elif i == '9':
            countPrime['9'] += 1
        elif i == '0':
            countPrime['0'] += 1
    #if countPrime every value is lower or equal to countnumber,break
    if countPrime['1'] <= countnumber['1'] and countPrime['2'] <= countnumber['2'] and countPrime['3'] <= countnumber['3'] and countPrime['4'] <= countnumber['4'] and countPrime['5'] <= countnumber['5'] and countPrime['6'] <= countnumber['6'] and countPrime['7'] <= countnumber['7'] and countPrime['8'] <= countnumber['8'] and countPrime['9'] <= countnumber['9'] and countPrime['0'] <= countnumber['0']:
        break
print(countPrime)
print(finalPrime)
    