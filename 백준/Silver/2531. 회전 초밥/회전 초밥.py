N, D, K, C = map(int,input().split())

dish = []
_max = 0
for i in range(N):
    dish.append(int(input()))

dish.extend(dish[:K-1])

for i in range(N):
    can_eat = set(dish[i:i+K])
    can_eat.add(C)
    if len(can_eat) > _max:
        _max = len(can_eat)
    if _max == K+1:
        break

print(_max)
