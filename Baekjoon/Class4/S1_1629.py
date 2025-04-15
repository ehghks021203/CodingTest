# 1629. 곱셈

def solution(n: int, m: int, d: int) -> int:
	if m == 0: return 1
	if m == 1: return n % d
	half = solution(n, m // 2, d)
	if m % 2 == 0: return (half * half) % d
	else: return (half * half * (n % d)) % d

if __name__ == "__main__":
	A, B, C = map(int, input().split())
	print(solution(A, B, C))

# (PyPy3) Result: 108384KB / 92ms