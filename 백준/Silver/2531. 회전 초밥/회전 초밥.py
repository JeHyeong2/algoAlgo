import sys
input = sys.stdin.readline

N, D, K, C = map(int,input().split())

dish = []
for i in range(N):
    dish.append(int(input()))
counting_list = [0]*(D+1)
counting_list[C] = 1
count =1

dish.extend(dish[:K-1])

for i in range(K):
    if counting_list[dish[i]] == 0:
        counting_list[dish[i]] = 1
        count += 1
    else:
        counting_list[dish[i]] += 1

_max = count

for i in range(1,N):

    counting_list[dish[i-1]] -= 1

    if counting_list[dish[i-1]] == 0:
        count -= 1

    if counting_list[dish[i+K-1]] == 0:
        counting_list[dish[i+K-1]] += 1
        count +=1
    else:
        counting_list[dish[i + K - 1]] += 1
    _max = max(_max,count)



# for i in range(N):
#     dish.append(int(input()))
#
# dish.extend(dish[:K-1])
#
# for i in range(N):
#     can_eat = set(dish[i:i+K])
#     can_eat.add(C)
#     if len(can_eat) > _max:
#         _max = len(can_eat)
#     if _max == K+1:
#         break

print(_max)
