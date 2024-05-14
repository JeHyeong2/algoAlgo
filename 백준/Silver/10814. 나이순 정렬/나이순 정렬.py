n = int(input())

l = []
for i in range(n):
    a,b = map(str,input().split())
    l.append([int(a),b,i])
l.sort(key= lambda x:(x[0],x[2]))

for i in range(n):
    print(*l[i][:2])