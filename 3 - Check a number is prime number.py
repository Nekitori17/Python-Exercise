input_num = int(input("Enter a number: "))
is_prime = True

if input_num == 1:
    print("1 is neither prime nor composite")
elif input_num == 2:
    print("2 is a prime number")
else:
    for i in range(2, input_num):
        if input_num % i == 0:
            is_prime = False
            break

print(f"{input_num} is a {"Prime number" if is_prime else "Composite number"}")
