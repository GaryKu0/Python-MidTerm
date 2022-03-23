Account_Detail={"123":456,"456":789,"789":888,"336":558,"775":666,"566":221}
Balance={"123":9000,"456":5000,"789":6000,"336":10000,"775":12000,"566":7000}
HowMany=int(input("組數為:"))
for i in range(HowMany):
    AccountAndPassword=input().split(" ")
    if Account_Detail[AccountAndPassword[0]]==int(AccountAndPassword[1]):
        print(Balance[AccountAndPassword[0]])
    else:
        print("ERROR")