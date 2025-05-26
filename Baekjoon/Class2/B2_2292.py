# 2292. 벌집

def solution(x: int) -> int:
	if x == 1: return 1
	w = 6
	pos = 1
	count = 0
	while pos < x:
		pos += w
		w += 6
		count += 1
	return count + 1

if __name__ == "__main__":
	N = int(input())
	print(solution(N))

# (PyPy3) Result: 109544KB / 116ms