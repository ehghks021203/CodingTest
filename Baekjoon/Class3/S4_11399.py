# 11399. ATM

def solution(time: list) -> int:
	result = 0
	time.sort()
	for i in range(len(time)):
		result += sum(time[:i + 1])
	return result

if __name__ == "__main__":
	N = int(input())
	time = list(map(int, input().split()))
	print(solution(time))

# (PyPy3) Result: 110576KB / 92ms