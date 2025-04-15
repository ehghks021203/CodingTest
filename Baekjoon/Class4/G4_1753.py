# 1753. 최단경로
from sys import stdin, stdout
from heapq import heappop, heappush

def solution(graph: dict, start: int) -> None:
	dist = [float("inf")] * (len(graph.keys()) + 1)
	dist[start] = 0
	pq = [(0, start)]
	while pq:
		curr_dist, node = heappop(pq)
		if curr_dist > dist[node]:
			continue
		for next, cost in graph[node]:
			new_dist = curr_dist + cost
			if new_dist < dist[next]:
				dist[next] = new_dist
				heappush(pq, (new_dist, next))
	for i in range(1, len(graph.keys()) + 1):
		if dist[i] == float("inf"):
			stdout.write("INF\n")
		else:
			stdout.write(f"{str(dist[i])}\n")

if __name__ == "__main__":
	V, E = map(int, stdin.readline().split())
	graph = {}
	for i in range(1, V + 1): graph[i] = []
	K = int(stdin.readline())
	for _ in range(E): 
		s, e, c = map(int, stdin.readline().split())
		graph[s].append((e, c))
	solution(graph, K)

# (PyPy3) Result: 136104KB / 392ms