# 1238. 파티
from heapq import heappop, heappush

def solution(graph: dict, party: int):
	dtime = []
	s = 1
	while len(dtime) != len(graph):
		pq = [(0, s)]
		gdist = [float("inf")] * (len(graph) + 1)
		bdist = [float("inf")] * (len(graph) + 1)
		gdist[s] = bdist[party] = 0
		while pq:
			d, n = heappop(pq)
			if d > gdist[n]: continue
			if n == party: break
			for nn, cost in graph[n]:
				nd = d + cost
				if nd < gdist[nn]:
					heappush(pq, (nd, nn))
					gdist[nn] = nd
		dtime.append(gdist[party])
		pq = [(0, party)]
		while pq:
			d, n = heappop(pq)
			if d > bdist[n]: continue
			if n == s: break
			for nn, cost in graph[n]:
				nd = d + cost
				if nd < bdist[nn]:
					heappush(pq, (nd, nn))
					bdist[nn] = nd
		dtime[s - 1] += bdist[s]
		s += 1
	return max(dtime)

if __name__ == "__main__":
	N, M, X = map(int, input().split())
	graph = {}
	for i in range(1, N + 1): graph[i] = []
	for _ in range(M):
		s, e, c = map(int, input().split())
		graph[s].append((e, c))
	print(solution(graph, X))

# (PyPy3) Result: 117816KB / 620ms