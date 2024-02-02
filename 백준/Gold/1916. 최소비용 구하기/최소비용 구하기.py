def find_small():
    min_ = 148932905873628957
    index = 0
    for i in range(1,N+1):
        if value[i] < min_ and not visited[i]:
            min_ = value[i]
            index = i
    return index

def dijk(start):
    visited[start] = True
    value[start] = 0
    for i in graph[start]:
        if value[i[0]] == INF:
            value[i[0]] = i[1]
        else:
            if value[i[0]] > i[1]:
                value[i[0]] = i[1]
    for i in range(N-1):
        now = find_small()
        visited[now] = True
        for j in graph[now]:
            cost = value[now] +j[1]
            if cost < value[j[0]]:
                value[j[0]] = cost


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
start = end = 0
for i in range(M+1):
    if i == M:
        start,end = map(int,input().split())
    else:
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
visited = [False] *(N+1)
value = [INF] * (N+1)

dijk(start)
print(value[end])