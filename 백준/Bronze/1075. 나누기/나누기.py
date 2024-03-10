N = int(input())
F = int(input())
NewN = str(N)
last = int(NewN[-2:])

a= N%F
ans = 0

if last - a >= 0:
    last = last - a
    while last > 0:
        last -= F
    if last != 0:
        last += F
else:
    last = last + (F-a)

if last < 10:
    print(f"0{last}")
else:
    print(last)