PlanAndTime="386,36000" #input("輸入月租費型式及通話時間為：")
PlanAndTime=PlanAndTime.split(",")
perSec=''
if PlanAndTime[0]=="186":
    perSec=0.09
    over1x=0.9
    over1xup=0.8
elif PlanAndTime[0]=="386":
    perSec=0.08
    over1x=0.8
    over1xup=0.7
elif PlanAndTime[0]=="586":
    perSec=0.07
    over1x=0.7
    over1xup=0.6
elif PlanAndTime[0]=="986":
    perSec=0.06
    over1x=0.6
    over1xup=0.5
if (float(PlanAndTime[1])*perSec) <= float(PlanAndTime[0]):
    Fee=perSec*float(PlanAndTime[1])
elif float(PlanAndTime[1])*perSec <= (float(PlanAndTime[0])*2):
    OriginalFee=perSec*float(PlanAndTime[1])
    discount=(OriginalFee-PlanAndTime[0])*over1x
    Fee=float(PlanAndTime[0])+discount
else:
    OriginalFee=perSec*float(PlanAndTime[1])
    Fee=OriginalFee*0.7
print("通話費為：",round(Fee,0))