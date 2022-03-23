HowMany=int(input("組數為:"))
for i in range(HowMany):
    Input_Value=input("輸入"+str(i+1)+"組:").split(" ")
    Fee=int(Input_Value[0])*250+int(Input_Value[1])*175
    print("第"+str(i+1)+"組費用為:"+str(Fee))