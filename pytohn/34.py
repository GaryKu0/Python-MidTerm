from math import fabs


Detect=False        
while Detect==False:
    num=int(input("請輸入一個數字："))
    if num>=11 and num<=1000:
        Detect=True
    else:
        print("ERROR")
if num%2==0 and num%11==0 and num%5!=0 and num%7!=0:
    print(str(num)+"為新公倍數?:YES")
else:
    print(num+"為新公倍數?:NO")
    