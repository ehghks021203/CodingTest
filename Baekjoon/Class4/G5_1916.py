# 1916. 최소비용 구하기
from heapq import heappop, heappush

def solution(graph: dict, start: int, end: int) -> int:
	dist = [float("inf")] * (len(graph) + 1)
	dist[start] = 0
	pq = [(0, start)]
	while pq:
		d, n = heappop(pq)
		if n == end: return d
		if d > dist[n]: continue
		for nn, cost in graph[n]:
			nd = d + cost
			if nd < dist[nn]:
				dist[nn] = nd
				heappush(pq, (nd, nn))

if __name__ == "__main__":
	N = int(input())
	M = int(input())
	graph = {}
	for i in range(1, N + 1): graph[i] = []
	for _ in range(M): 
		s, e, c = map(int, input().split())
		graph[s].append((e, c))
	S, E = map(int, input().split())
	print(solution(graph, S, E))

# (PyPy3) Result: 121708KB / 220ms