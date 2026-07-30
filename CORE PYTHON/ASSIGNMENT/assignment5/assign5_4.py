# 4. WAP to print Armstrong number within a given range


s = int(input("Enter the starting range: "))
e = int(input("Enter the ending range: "))

for i in range(s, e + 1):

    num = i
    count = len(str(i))      # Number of digits

    total = 0
    temp = num

    while temp > 0:
        d = temp % 10
        total = total + (d ** count)
        temp = temp // 10

    if total == num:
        print(num)
