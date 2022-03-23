#Guess Number
Guessed=False
answer="7364"
A=B=0
while Guessed==False:
    guessNumber=input("Guess a number:")
    for i in range(len(answer)):
        if guessNumber[i] in answer:
            if answer[i]==guessNumber[i]:
                A+=1
            else:
                B+=1
        else:
            continue
    print(f"A:{A} B:{B}")
    A=B=0
    if guessNumber==answer:
        Guessed=True
        print("You win!")