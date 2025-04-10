# 11726. 2xn 타일링

def solution(n: int) -> int:
	dp = [0, 1, 2]
	for i in range(3, n + 1):
		dp.append((dp[i - 1] + dp[i - 2]) % 10_007)
	return dp[n]

if __name__ == "__main__":
	n = int(input())
	print(solution(n))

# (PyPy3) Result: 108384KB / 92ms