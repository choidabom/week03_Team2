import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result = 123456789

n, m = map(int, sys.stdin.readline().split())
#print(n, m)
visited = [[False for i in range(m)] for j in range(n)]
maze = []
for _ in range(n):
	temp = list(sys.stdin.readline())
	if temp[-1] == '\n':
		temp.pop()
	maze.append(temp)
#print(maze)

def solve(y, x, step):
	global n, m, result
	if (x == m-1) and (y == n-1):
		if step < result:
			result = step
		return
	for i in range(4):
		nextx = x + dx[i]
		nexty = y + dy[i]
		if (nextx>=0) and (nextx<m) and (nexty>=0) and (nexty<n):
			if visited[nexty][nextx]:
				continue
			if maze[nexty][nextx]=='0':
				continue
			if maze[nexty][nextx]=='1':
				visited[nexty][nextx] = True
				solve(nexty, nextx, step+1)
				visited[nexty][nextx] = False

solve(0, 0, 1)
print(result)