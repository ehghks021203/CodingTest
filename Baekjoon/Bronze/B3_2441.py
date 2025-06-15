# 2441. 별 찍기 - 4

def solution(n: int) -> None:
	for i in range(n, 0, -1):
		print(" " * (n - i) + "*" * i)

if __name__ == "__main__":
	N = int(input())
	solution(N)

# (PyPy3) Result: 108384KB / 84ms