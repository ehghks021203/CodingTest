# 30802. 웰컴 키트

def solution(n: int, size: list, t: int , p: int) -> None:
	total = 0
	for s in size:
		total += (s - 1) // t + 1
	print(total)
	print(n // p, n % p)

if __name__ == "__main__":
	N = int(input())
	S, M, L, XL, XXL, XXXL = map(int, input().split())
	T, P = map(int, input().split())
	solution(N, [S, M, L, XL, XXL, XXXL], T, P)

# (PyPy3) Result: 108384KB / 92ms