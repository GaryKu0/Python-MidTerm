from httpx import options


Balance=int(input("小明身上的錢:"))
Option=input("請輸入有幾種飲料:")
Price=[]
CanBuy=0
for i in range(int(Option)):
    Price.append(int(input("請輸入飲料價格:")))
for i in range(len(Price)):
    if Price[i]<=Balance:
        CanBuy+=1
print(CanBuy)
        