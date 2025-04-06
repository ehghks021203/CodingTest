# 1260. DFS와 BFS
from collections import deque

def dfs(graph: dict, node: int, result: list = []) -> list:
	if node in result:
		return result
	else:
		result.append(node)
		for n in graph[node]:
			dfs(graph, n, result)
		return result

def bfs(graph: dict, node: int) -> list:
	queue = deque([node])
	result = []
	while queue:
		cn = queue.popleft()
		if not cn in result:
			result.append(cn)
			for nn in graph[cn]:
				queue.append(nn)
	return result

def solution(graph: dict, node: int) -> None:
	for k in graph: graph[k].sort()
	print(" ".join(map(str, dfs(graph, node))))
	print(" ".join(map(str, bfs(graph, node))))

if __name__ == "__main__":
	N, M, V = map(int, input().split())
	edge = []
	graph = {}
	for i in range(1, N + 1): graph[i] = []
	for _ in range(M): edge.append(list(map(int, input().split())))
	for i in range(M): 
		if not edge[i][1] in graph[edge[i][0]]: graph[edge[i][0]].append(edge[i][1])
		if not edge[i][0] in graph[edge[i][1]]: graph[edge[i][1]].append(edge[i][0])
	solution(graph, V)

# (PyPy3) Result: 117520KB / 176ms