# 11050. 이항 계수 1

def factorial(n: int) -> int:
	if n == 0: return 1
	return n * factorial(n - 1)

def solution(n: int, k: int) -> int:
	return factorial(n) // (factorial(n - k) * factorial(k))

if __name__ == "__main__":
	N, K = map(int, input().split())
	print(solution(N, K))

# (PyPy3) Result: 108384KB / 96ms