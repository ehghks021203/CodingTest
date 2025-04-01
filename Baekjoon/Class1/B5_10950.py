# 10950. A + B - 3

def solution(nums: tuple) -> int:
	num1, num2 = nums
	return num1 + num2

if __name__ == "__main__":
	T = int(input())
	[print(solution(map(int, input().split()))) for _ in range(T)]

# (PyPy3) Result: 108384KB / 92ms