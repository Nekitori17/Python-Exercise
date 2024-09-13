sum_to = int(input("Enter a number to calculate the sum to: "))

if sum_to > 2:
    total = 0
    for i in range(1, sum_to + 1):
        total += i

    print(total)
else:
    print("Enter a number greater than 2")