count =1
while True:
    a, b = map(int,input().split())
    if a == 0:
        break
    print(f"Hole #{count}")
    if b == 1:
        print("Hole-in-one.")
        count += 1
        print('')
        continue
    if a - b == 0:
        print("Par.")
        count += 1
        print('')
        continue
    if a - b == 3:
        print("Double eagle.")
        count += 1
        print('')
        continue
    if a - b == 2:
        print("Eagle.")
        count += 1
        print('')
        continue
    if a - b == 1:
        print("Birdie.")
        count += 1
        print('')
        continue
    if a - b == -1:
        print("Bogey.")
        count += 1
        print('')
        continue
    if a - b <= -2:
        print("Double Bogey.")
        count += 1
        print('')
        continue
