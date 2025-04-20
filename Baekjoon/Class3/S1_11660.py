# 11660. 구간 합 구하기 5

def solution(table: list, m: int) -> None:
	n = len(table)
	dp = [[0] * (n + 1) for _ in range(n + 1)]
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			dp[i][j] = table[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]
	for _ in range(m):
		x1, y1, x2, y2 = map(int, input().split())
		print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])

if __name__ == "__main__":
	N, M = map(int, input().split())
	table = []
	for _ in range(N): table.append(list(map(int, input().split())))
	solution(table, M)

# (PyPy3) Result: 129604KB / 3064ms