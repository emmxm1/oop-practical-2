limit = int(input())

a = 1 
b = 1

total = 0 
count = 0

while a < limit: 
    total += a 
    count += 1

    a, b = b, a + b
print(total)
print(count)