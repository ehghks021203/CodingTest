# 12865. 평범한 배낭

def solution(k: int, items: list) -> int:
	dp = [[0 for _ in range(k + 1)] for _ in range(len(items) + 1)]
	for ck in range(k + 1):
		for idx in range(1, len(items) + 1):
			if items[idx - 1][0] <= ck:
				dp[idx][ck] = max(items[idx - 1][1] + dp[idx - 1][max(0, ck - items[idx - 1][0])], dp[idx - 1][ck])
			else:
				dp[idx][ck] = max(dp[idx][ck], dp[idx - 1][ck])
	return dp[-1][-1]

if __name__ == "__main__":
	N, K = map(int, input().split())
	items = []
	for _ in range(N): items.append(list(map(int, input().split())))
	print(solution(K, items))

# (PyPy3) Result: 189944KB / 496ms