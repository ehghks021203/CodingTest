# 1932. 정수 삼각형

def solution(triangle: list) -> int:
	dp = []
	for i in range(len(triangle)):
		if i == 0:
			dp.append([triangle[0][0]])
		else:
			dp.append([0] * len(triangle[i]))
			for j in range(len(triangle[i])):
				if j == 0: dp[i][j] = triangle[i][j] + dp[i - 1][j]
				elif j + 1 == len(triangle[i]): dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
				else: dp[i][j] = triangle[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])
	return max(dp[-1])

if __name__ == "__main__":
	n = int(input())
	triangle = []
	for _ in range(n):
		triangle.append(list(map(int, input().split())))
	print(solution(triangle))

# (PyPy3) Result: 111668KB / 124ms