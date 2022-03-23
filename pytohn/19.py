import re
Howmany=int(input("測試資料量:"))
result=""
for i in range(Howmany):
    print("輸入第"+str(i+1)+"筆資料:")
    Blood=input("").split(" ")
    Father=Blood[0]
    Mother=Blood[1]
    Child=Blood[2]
    if Father==Mother:
        if Father=="O":
            if Child=="A" or Child=="B" or Child=="AB":
                result="孩子不是你的,頭頂綠綠的😢"
            elif Child=="O":
                result="YES"
        elif Father=="A":
            if Child=="AB" or Child=="B":
                result="孩子不是你的,頭頂綠綠的😢"
            elif Child=="O" or Child=="A":
                result="YES"
        elif Father=="B":
            if Child=="AB" or Child=="A":
                result="孩子不是你的,頭頂綠綠的😢"
            elif Child=="O" or Child=="B":
                result="YES"
        elif Father=="AB":
            if Child=="O":
                result="孩子不是你的,頭頂綠綠的😢"
            elif Child=="AB" or Child=="A" or Child=="B":
                result="YES"
    else:
        if Father=="O":
            if Mother=="A" or Mother=="B" or Mother=="AB":
                if Child=="AB":
                    result="孩子不是你的,頭頂綠綠的😢"
            if Mother=="O":
                if Child!="O":
                    result="孩子不是你的,頭頂綠綠的😢"
                else:
                    result="YES"
            if Mother=="B"or Mother=="A":
                if Child!=Mother:
                    if Child!=Father:
                        print("孩子不是你的,頭頂綠綠的😢")
                    else:
                        result="YES"
                else:
                    result="YES"
            if Mother=="AB":
                if Child!="O" and Child!="AB":
                    result="孩子不是你的,頭頂綠綠的😢"
                else:
                    result="YES"
        if Father=="A":
            if Mother=="AB":
                if Child=="O":
                    result="孩子不是你的,頭頂綠綠的😢"
                else:
                    result="YES"
            if Mother=="B":
                result="Yes"
        if Father=="B":
            if Mother=="AB":
                if Child=="O":
                    result="孩子不是你的,頭頂綠綠的😢"
                else:
                    result="YES"
            if Mother=="A":
                result="Yes"
    print(result)
            
                
                
    
    
    