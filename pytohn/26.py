#字元出現次數
DetectWord=""
while DetectWord!="end":
    DetectWord=input("檢測的字元:(end結束)")
    if (DetectWord=="end"):
        break
    DetectChar=input("檢測的單一字元:")
    count=0
    for i in range(len(DetectWord)):
        if DetectWord[i]==DetectChar:
            count+=1
    print("字元",DetectChar,"出現次數為:",count)
    