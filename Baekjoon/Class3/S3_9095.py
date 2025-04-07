# 9095. 1, 2, 3 더하기

def solution(seq: list) -> int:
	dp = [1, 2, 4]
	for t in seq:
		for n in range(1, t + 1):
			if n > len(dp):
				dp.append(sum(dp[-3:]))
		print(dp[t - 1])

if __name__ == "__main__":
	T = int(input())
	solution([int(input()) for _ in range(T)])

# (PyPy3) Result: 108384KB / 88ms
# NOTE: DP는 점화식만 찾으면 됨