# 1003. 피보나치 함수

def solution(n: int) -> None:
	if n == 0: 
		print(1, 0)
	else:
		a, b = 0, 1
		for _ in range(n - 1):
			a, b = b, a + b
		print(a, b)

if __name__ == "__main__":
	T = int(input())
	[solution(int(input())) for _ in range(T)]

# (PyPy3) Result: 109544KB / 96ms