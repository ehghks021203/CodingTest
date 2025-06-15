# 2440. 별 찍기 - 3

def solution(n: int) -> None:
	for i in range(n, 0, -1):
		print("*" * i)

if __name__ == "__main__":
	N = int(input())
	solution(N)

# (PyPy3) Result: 108384KB / 92ms