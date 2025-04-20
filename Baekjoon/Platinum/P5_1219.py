# 1219. 오민식의 고민
from collections import deque

def solution(n: int, start: int, end: int, edges: list, income: list) -> str:
	pay = [float("inf")] * (n + 1)
	pay[start] = -income[start]
	graph = [[] for _ in range(n + 1)]
	changed_nodes = []
	for s, e, cost in edges: graph[s].append(e)
	for i in range(1, n + 1):
		for s, e, cost in edges:
			if pay[s] != float("inf") and pay[e] > pay[s] + cost - income[e]:
				pay[e] = pay[s] + cost - income[e]
				if i == n: 
					changed_nodes.append(e)
	visited = [False] * (n + 1)
	queue = deque(changed_nodes)
	while queue:
		n = queue.popleft()
		if n == end: return "Gee"
		for nn in graph[n]:
			if not visited[nn]:
				visited[nn] = True
				queue.append(nn)
	if pay[end] == float("inf"): return "gg"
	return -pay[end]

if __name__ == "__main__":
	N, S, E, M = map(int, input().split())
	edges = [tuple(map(int, input().split())) for _ in range(M)]
	income = list(map(int, input().split()))
	print(solution(N, S, E, edges, income))

# (PyPy3) Result: 113500KB / 128ms