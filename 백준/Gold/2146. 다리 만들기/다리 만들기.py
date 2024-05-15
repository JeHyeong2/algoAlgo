# 2146 다리 만들기
from collections import deque

n = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
inum = 2  # 육지번호
ans = int(1e9)  # 최단거리


# 대륙 번호 넘버링
def island_numbering(i, j):
  d = deque([(i, j)])

  while d:
    cx, cy = d.popleft()
    graph[cx][cy] = inum
    for dx, dy in direction:
      nx, ny = dx + cx, dy + cy
      if (0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1):
        graph[nx][ny] = inum
        d.append((nx, ny))


# 다리 짓기
def shortcut(inum):
  # 각 대륙마다 최단거리 탐색
  d = deque([])
  dist = [[-1] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if graph[i][j] == inum:
        dist[i][j] = 0
        d.append((i, j))  # inum에 해당하는 육지들 전부 저장

  # 최단거리 탐색
  while d:
    cx, cy = d.popleft()
    for dx, dy in direction:
      nx, ny = cx + dx, cy + dy
      if (0 <= nx < n and 0 <= ny < n):
        # 아직 방문 하지 않은 바다라면
        if (graph[nx][ny] == 0 and dist[nx][ny] == -1):
          dist[nx][ny] = dist[cx][cy] + 1
          d.append((nx, ny))

        # 다른 대륙에 도착했다면
        elif graph[nx][ny] > 0 and graph[nx][ny] != inum:
          return dist[cx][cy]

  return int(1e9)


for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      island_numbering(i, j)
      inum += 1

# 가장 짧은 다리 길이 찾기
for num in range(2, inum):
  temp = shortcut(num)
  ans = min(ans, temp)

print(ans)