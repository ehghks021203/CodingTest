# 2775. 부녀회장이 될테야

dp = [list(range(1, 15))]

def solution(k: int, n: int) -> int:
	global dp
	cnt = 0
	if len(dp) < k + 1:
		while cnt != k:
			cnt += 1
			if len(dp) < cnt + 1:
				l = []
				for i in range(14):
					l.append(sum(dp[cnt - 1][:i + 1]))
				dp.append(l)
	return dp[k][n - 1]

if __name__ == "__main__":
	T = int(input())
	for _ in range(T):
		K = int(input())
		N = int(input())
		print(solution(K, N))

# (PyPy3) Result: 109540KB / 92ms