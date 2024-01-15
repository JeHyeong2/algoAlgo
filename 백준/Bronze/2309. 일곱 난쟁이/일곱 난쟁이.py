import random
N = [int(input()) for _ in range(9)]

while True:
    b = random.sample(N,7)
    if sum(b) == 100:
        print(*sorted(b))
        break
