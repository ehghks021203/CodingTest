# 10952. A + B - 5

def solution(num1: int, num2: int) -> int:
	return num1 + num2

if __name__ == "__main__":
	while True:
		num1, num2 = map(int, input().split())
		if num1 == num2 == 0:
			break
		else:
			print(solution(num1, num2))

# (PyPy3) Result: 108384KB / 92ms