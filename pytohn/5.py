from tkinter import N


m = int(input("Give me a number!!"))
nn = 1
n = 1
while nn < m:
    nn = nn*n
    n += 1
print(n-1)
