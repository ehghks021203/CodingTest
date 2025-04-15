# 11725. 트리의 부모 찾기
from collections import deque

def solution(graph: dict):
	parents = [0] * (len(graph) + 1)
	queue = deque([1])
	visited = set([1])
	while queue:
		n = queue.popleft()
		for nn in graph[n]:
			if nn not in visited:
				parents[nn] = n
				queue.append(nn)
				visited.add(nn)
	return parents[2:]

if __name__ == "__main__":
	N = int(input())
	graph = {}
	for i in range(1, N + 1): graph[i] = []
	for _ in range(N - 1):
		s, e = map(int, input().split())
		graph[s].append(e)
		graph[e].append(s)
	print("\n".join(map(str, solution(graph))))

# (PyPy3) Result: 140716KB / 324ms