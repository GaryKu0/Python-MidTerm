L=""
while L!="end":
    L = input("輸入整數數列(end結束):")
    if L=="end":
        break
    Answer = []
    for i in range(len(L)):#從第一個開始
        for j in range(i,len(L)):
            if len(L[i:j+1]) > 1:
                if L[i:j+1] == L[i:j+1][::-1]:
                    Answer.append(L[i:j+1])
    tmp = ""
    for i in Answer:
        if len(i) > len(tmp):
            tmp = i
        elif len(i) == len(tmp):
            if int(i) < int(tmp):
                tmp = i
    print("最長迴文為:",tmp)
print("結束")