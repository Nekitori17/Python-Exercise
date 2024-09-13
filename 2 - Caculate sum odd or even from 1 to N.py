sum_to = int(input("Enter a number to calculate the sum to: "))
is_even =  True if input("Enter 1 for even or 0 for odd: ") == "1" else False

if sum_to > 2:
    total = 0
    for i in range(1, sum_to + 1):
        if is_even:
            if i % 2 == 0:
                total += i
        else:
            if i % 2 != 0:
                total += i

    print(total)
else:
    print("Enter a number greater than 2")