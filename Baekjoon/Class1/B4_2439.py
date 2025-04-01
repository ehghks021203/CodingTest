# 2439. 별 찍기 - 2

def solution(n: int) -> None:
	for i in range(1, n + 1):
		print(" " * (n - i) + "*" * i)

if __name__ == "__main__":
	N = int(input())
	solution(N)

# (PyPy3) Result: 108384KB / 88ms