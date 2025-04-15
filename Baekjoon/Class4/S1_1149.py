# 1149. RGB거리

def solution(houses: list) -> int:
	dp = []
	for idx in range(len(houses)):
		if idx == 0: 
			dp.append(houses[0])
		else:
			dp.append([0, 0, 0])
			dp[idx][0] = houses[idx][0] + min(dp[idx - 1][1], dp[idx - 1][2])
			dp[idx][1] = houses[idx][1] + min(dp[idx - 1][0], dp[idx - 1][2])
			dp[idx][2] = houses[idx][2] + min(dp[idx - 1][0], dp[idx - 1][1])
	return min(dp[-1])

if __name__ == "__main__":
	N = int(input())
	houses = []
	for _ in range(N): houses.append(list(map(int, input().split())))
	print(solution(houses))

# (PyPy3) Result: 110708KB / 100ms