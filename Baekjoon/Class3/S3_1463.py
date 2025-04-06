# 1463. 1로 만들기

def solution(n: int, count: int = 0) -> int:
	dp = [0, 0]
	for i in range(2, n + 1):
		dp.append(dp[i - 1] + 1)
		if i % 2 == 0: dp[i] = min(dp[i // 2] + 1, dp[i])
		if i % 3 == 0: dp[i] = min(dp[i // 3] + 1, dp[i])
	return dp[n]

if __name__ == "__main__":
	N = int(input())
	print(solution(N))

# (PyPy3) Result: 182884KB / 148ms