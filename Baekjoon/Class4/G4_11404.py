# 11404. 플로이드

def solution(n: int, edges: list) -> list:
	dist = [[float("inf")] * n for _ in range(n)]
	for i in range(n): dist[i][i] = 0
	for s, e, c in edges: dist[s - 1][e - 1] = min(dist[s - 1][e - 1], c)
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if dist[i - 1][j - 1] > dist[i - 1][k - 1] + dist[k - 1][j - 1]:
					dist[i - 1][j - 1] = dist[i - 1][k - 1] + dist[k - 1][j - 1]
	return dist

if __name__ == "__main__":
	n = int(input())
	m = int(input())
	edges = []
	for _ in range(m): edges.append(tuple(map(int, input().split())))
	for y in solution(n, edges):
		for x in y:
			if x == float("inf"): print("0", end=" ")
			else: print(x, end=" ")
		print()

# (PyPy3) Result: 126740KB / 232ms