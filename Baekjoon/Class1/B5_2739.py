# 2739. 구구단

def solution(n: int) -> None:
	[print(f"{n} * {i} = {n * i}") for i in range(1, 10)]

if __name__ == "__main__":
	N = int(input())
	solution(N)

# (PyPy3) Result: 108384KB / 92ms