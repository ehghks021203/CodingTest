# 2869. 달팽이는 올라가고 싶다

def solution(a: int, b: int, v: int) -> int:
	return (v - a) // (a - b) + (2 if (v - a) % (a - b) != 0 else 1)

if __name__ == "__main__":
	A, B, V = map(int, input().split())
	print(solution(A, B, V))

# (PyPy3) Result: 108384KB / 84ms