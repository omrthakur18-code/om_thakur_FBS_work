# 1. Write a program print following patterns:



for i in range(1, 5):
    # Print spaces
    for j in range(1,5-i):
        print("  ", end="")

    value = 1

    # Print Pascal Triangle
    for j in range(1, i + 1):
        print(value, end="  ")
        value = value * (i - j) // j

    print()