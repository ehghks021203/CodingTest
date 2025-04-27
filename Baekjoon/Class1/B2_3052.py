# 3052. 나머지

def solution(seq: list) -> int:
	count = 0
	history = []
	for s in seq:
		if s % 42 not in history:
			history.append(s % 42)
			count += 1
	return count

if __name__ == "__main__":
	seq = []
	for _ in range(10): seq.append(int(input()))
	print(solution(seq))

# (PyPy3) Result: 108384KB / 88ms