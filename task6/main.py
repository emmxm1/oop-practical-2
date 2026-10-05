a = float(input())
b = float(input())
c = float(input())

if a == b == c:
    print("TIE")
elif a == b and a > c:
    print("TIE")
elif a == c and a > b:
    print("TIE")
elif b == c and b > a:
    print("TIE")
elif a > b and a > c:
    print("A")
elif b > a and b > c:
    print("B")
else:
    print("C")