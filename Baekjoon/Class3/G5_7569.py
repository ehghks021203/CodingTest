# 7569. 토마토
from collections import deque

def solution(tomato: list) -> int:
	ripens = []
	for f in range(len(tomato)):
		for x in range(len(tomato[f])):
			for y in range(len(tomato[f][x])):
				if tomato[f][x][y] == 1:
					ripens.append((f, x, y, 0))

	queue = deque(ripens)
	while queue:
		f, x, y, day = queue.popleft()
		for nf, nx, ny in [(f + 1, x, y), (f - 1, x, y), (f, x + 1, y), (f, x - 1, y), (f, x, y + 1), (f, x, y - 1)]:
			if nf < 0 or nf >= len(tomato): continue
			if nx < 0 or nx >= len(tomato[f]): continue
			if ny < 0 or ny >= len(tomato[f][x]): continue
			if tomato[nf][nx][ny] == 0: 
				tomato[nf][nx][ny] = 1
				queue.append((nf, nx, ny, day + 1))

	for f in range(len(tomato)):
		for x in range(len(tomato[f])):
			for y in range(len(tomato[f][x])):
				if tomato[f][x][y] == 0:
					return -1
	return day

if __name__ == "__main__":
	M, N, H = map(int, input().split())
	tomato = []
	for floor in range(H):
		tomato.append([])
		for _ in range(N):
			tomato[floor].append(list(map(int, input().split())))
	print(solution(tomato))

# (PyPy3) Result: 217560KB / 708ms