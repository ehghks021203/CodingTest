# 2475. 검증수

def solution(seq: list) -> int:
	sum = 0
	for s in seq:
		sum += s ** 2
	return sum % 10

if __name__ == "__main__":
	print(solution(list(map(int, input().split()))))

# (PyPy3) Result: 108384KB / 88ms