n = input()
for i in range(len(n)):
    if n[i] == n[len(n)-i-1]:
        continue
    else:
        print(0)
        break
else:
    print(1)
