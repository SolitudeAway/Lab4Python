import math
sum = 0
x = 0.5
i = 1
n = input("Ввести значення n: ", )
n = int(n)
for i in range (1,n+1):
    i = 1/(i**2)
    sum+=i
y=1/sum*(math.sin(x))
print("Значення y: ", y)
