# 15654. N과 M (5)

def solution(seq: list, n: int, result: list = [], idx: int = 0) -> None:
	if idx == n:
		print(" ".join(map(str, result)))
		return
	for num in seq:
		if not num in result:
			result.append(num)
			solution(seq, n, result, idx + 1)
			result.pop()

if __name__ == "__main__":
	N, M = map(int, input().split())
	seq = list(map(int, input().split()))
	seq.sort()
	solution(seq, M)

# (PyPy3) Result: 111484KB / 160ms