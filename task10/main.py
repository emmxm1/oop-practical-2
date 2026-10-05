n = int(input())
total = 0
for number in range(2, n + 1): 
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        total += number
print(total)