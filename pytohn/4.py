import math
x = int(input("輸入x座標："))
y = int(input("輸入y座標："))
a = 0
if (x < 0):
    if (y < 0):
        a = y*y+x*x
        print("第三象限距離為根號"+str(a))
    elif(y > 0):
        a = y*y+x*x
        print("第二象限距離為根號"+str(a))
    elif(y == 0):
        print("On y line")
elif (x > 0):
    if (y > 0):
        a = y*y+x*x
        print("第一象限距離為根號"+str(a))
    elif(y < 0):
        a = y*y+x*x
        print("第四象限距離為根號"+str(a))
    elif(y == 0):
        print("On y line")
elif (x == 0):
    print("On x line")
