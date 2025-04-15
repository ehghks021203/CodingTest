# 2747. 피보나치 수

def solution(n: int) -> int:
	if n == 0: return 0
	a, b = 0, 1
	for _ in range(2, n + 1):
		a, b = b, a + b
	return b

if __name__ == "__main__":
	n = int(input())	# n은 45보다 작거나 같은 자연수
	print(solution(n))

# (PyPy3) Result: 108384KB / 88ms