
min = ""
max = ""
input_value = input("Give me number!! (x,y,z)")
# use mapping separate the input_value
input_value = input_value.split(",")
input_value.sort()
minInput_Value = input_value
print(minInput_Value)
for l in minInput_Value:
    min += str(l)
input_value.reverse()
maxInput_Value = input_value
print(maxInput_Value)
for i in maxInput_Value:
    max += str(i)

answer = int(max)-int(min)
print(max, "-", min, "=", answer)
