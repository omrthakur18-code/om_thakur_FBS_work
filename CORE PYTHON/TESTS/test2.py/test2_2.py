# WAP to calculate the sum of the series 1/1! + 2/2! + ... + n/n!

N = int(input("Enter the value of n: "))

fact = 1
sum = 0

for i in range(1, N + 1):
    fact = fact * i
    sum = sum + (i / fact)

print("Sum of the series =", sum)