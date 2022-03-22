def prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

a = "156"#input("請輸入正整數：")
b = []
print(len(a))
for i in range(len(a)):
    for j in range(i,len(a)):
        c = prime(int(a[i:j+1]))
        if c:
            b.append(a[i:j+1])
if b:
    print(f"子字串中最大的質數為：{max(b)}")
else:
    print("No prime found")