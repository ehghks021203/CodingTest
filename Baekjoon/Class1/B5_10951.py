# 10951. A + B - 4

def solution(nums: tuple) -> int:
	num1, num2 = nums
	return num1 + num2

if __name__ == "__main__":
	try:
		while True:
			print(solution(map(int, input().split())))
	except:
		exit(0)

# (PyPy3) Result: 108384KB / 92ms