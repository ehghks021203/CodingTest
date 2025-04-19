# 1865. 웜홀

def solution(n: int, edges: list) -> bool:
	dist = [100_000_000] * (n + 1)
	for i in range(n + 1):
		for s, e, cost in edges:
			if dist[e] > dist[s] + cost:
				dist[e] = dist[s] + cost
				if i == n: return True
	return False

if __name__ == "__main__":
	TC = int(input())
	for _ in range(TC):
		N, M, W = map(int, input().split())
		edges = []
		for _ in range(M):
			s, e, c = map(int, input().split())
			edges.append((s, e, c))
			edges.append((e, s, c))
		for _ in range(W):
			s, e, c = map(int, input().split())
			edges.append((s, e, -c))	# 음수 가중치로 변환
		if solution(N, edges): print("YES")
		else: print("NO")

# (PyPy3) Result: 112548KB / 228ms