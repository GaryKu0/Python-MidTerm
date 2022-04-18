# 輸入一數x 輸出x*x的菱形
x = int(input("請輸入一數字:"))
# 輸出x*x的菱形
for i in range(x+1):
        print(' '*(x-i)+'*'*(2*i-1))
x=x-1
for i in range(x,0,-1):
        print(' ',end='')
        print(' '*(x-i)+'*'*(2*i-1))