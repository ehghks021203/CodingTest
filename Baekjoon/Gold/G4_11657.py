# 11657. 타임머신

def solution(n: int, edges: list) -> list:
	dist = [float("inf")] * (n + 1)
	dist[1] = 0
	for i in range(1, n + 1):
		for s, e, cost in edges:
			if dist[s] != float("inf") and dist[e] > dist[s] + cost:
				dist[e] = dist[s] + cost
				if i == n: return [-1]	# n번째 반복에서도 갱신된다면 음수 사이클 존재
	# INF의 경우 도달 불가능한 도시이므로 -1
	for i in range(2, len(dist)):
		if dist[i] == float("inf"): dist[i] = -1
	return dist[2:]

if __name__ == "__main__":
	N, M = map(int, input().split())
	edges = [tuple(map(int, input().split())) for _ in range(M)]
	print("\n".join(map(str, solution(N, edges))))

# (PyPy3) Result: 11916KB / 300ms