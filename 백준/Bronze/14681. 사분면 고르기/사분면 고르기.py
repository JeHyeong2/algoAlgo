a = int(input())
b = int(input())


if a != abs(a) and b != abs(b):
    print(3)
elif a != abs(a) and b == abs(b):
    print(2)
elif a == abs(a) and b != abs(b):
    print(4)
else:
    print(1)