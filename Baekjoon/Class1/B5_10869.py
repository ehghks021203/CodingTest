# 10869. 사칙연산

def solution(num1: int, num2: int) -> None:
	print(f"{num1 + num2}\n{num1 - num2}\n{num1 * num2}\n{num1 // num2}\n{num1 % num2}")

if __name__ == "__main__":
	A, B = map(int, input().split())
	solution(A, B)

# (PyPy3) Result: 108384KB / 96ms