# 13549. 숨바꼭질 3
from heapq import heappop, heappush
from collections import deque

# NOTE: 다익스트라를 통한 최단거리 계산
def solution_with_dijkstra(subin_x: int, sister_x: int) -> int:
	dist = [float("inf")] * 100_001
	dist[subin_x] = 0
	pq = [(0, subin_x)]
	while pq:
		d, x = heappop(pq)
		if x == sister_x: return dist[sister_x]
		if d > dist[x]: continue
		for nx, cost in [(x - 1, 1), (x + 1, 1), (x * 2, 0)]:
			if nx > 100_000 or nx < 0: continue
			nd = d + cost
			if nd < dist[nx]:
				dist[nx] = nd
				heappush(pq, (nd, nx))
	return dist[sister_x]

# NOTE: BFS를 통한 최단거리 계산 (deque를 활용한 0-1 너비우선탐색)
def solution_with_BFS(subin_x: int, sister_x: int) -> int:
	dist = [float("inf")] * 100_001
	dist[subin_x] = 0
	queue = deque([(subin_x, 0)])
	while queue:
		x, d = queue.popleft()
		if x == sister_x: return d
		for nx, cost in [(x - 1, 1), (x + 1, 1), (x * 2, 0)]:
			if nx > 100_000 or nx < 0: continue
			if dist[x] + cost < dist[nx]:
				if cost == 0: queue.appendleft((nx, d))
				else: queue.append((nx, d + 1))
				dist[nx] = dist[x] + cost

if __name__ == "__main__":
	N, K = map(int, input().split())
	print(solution_with_dijkstra(N, K))
	print(solution_with_BFS(N, K))

# (PyPy3) Result with dijstra: 113680KB / 184ms
# (PyPy3) Result with BFS:     113548KB / 124ms