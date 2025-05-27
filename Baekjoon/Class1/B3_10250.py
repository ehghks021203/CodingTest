# 10250. ACM 호텔

def solution(h: int, w: int, n: int) -> int:
	return (h if n % h == 0 else n % h) * 100 + (0 if n % h == 0 else 1) + (n // h)
	
if __name__ == "__main__":
	for _ in range(int(input())):
		H, W, N = map(int, input().split())
		print(solution(H, W, N))

# (PyPy3) Result: 108384KB / 96ms