# 1012. 유기농 배추
from collections import deque

def solution(cabbage: list) -> int:
	worm = 0
	queue = deque([cabbage[0]])
	not_visited = set(cabbage[1:])
	while True:
		worm += 1
		while queue:
			x, y = queue.popleft()
			for next in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
				if next in not_visited:
					queue.append(next)
					not_visited.remove(next)
		if len(not_visited) != 0:
			queue.append(not_visited.pop())
		else:
			return worm

if __name__ == "__main__":
	T = int(input())
	for _ in range(T):
		cabbage = []
		M, N, K = map(int, input().split())
		for _ in range(K): cabbage.append(tuple(map(int, input().split())))
		print(solution(cabbage))

# (PyPy3) Result: 112652KB / 140ms