# 27512. 스네이크

def solution(width: int, height: int) -> int:
	return width * height - (width * height) % 2

if __name__ == "__main__":
	width, height = map(int, input().split())
	print(solution(width, height))

# (PyPy3) Result: 108384KB / 88ms