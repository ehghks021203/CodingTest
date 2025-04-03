# 2798. 블랙잭

def solution(threshold: int, seq: list, result = []):
	max_num = 0
	if len(result) == 3:
		if (sum(result) > threshold):
			return 0
		return sum(result)
	for idx in range(len(seq)):
		result.append(seq[idx])
		max_num = max(solution(threshold, seq[idx + 1:], result), max_num)
		result.pop()
	return max_num

if __name__ == "__main__":
	N, M = map(int, input().split())
	print(solution(M, list(map(int, input().split()))))

# (PyPy3) Result: 11420KB / 152ms