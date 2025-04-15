# 11053. 가장 긴 증가하는 부분 수열

def solution(seq: list) -> int:
	dp = [1] * len(seq)
	for i in range(len(seq)):
		for j in range(i):
			if seq[j] < seq[i]: dp[i] = max(dp[i], dp[j] + 1)
	return max(dp)

if __name__ == "__main__":
	N = int(input())
	A = list(map(int, input().split()))
	print(solution(A))

# (PyPy3) Result: 109544KB / 96ms