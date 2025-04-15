# 15663. N과 M (9)
from itertools import permutations

def solution(seq: list, m: int) -> list:
	ndseq = set()
	for p in list(permutations(seq, m)):
		ndseq.add(p)
	return sorted(list(ndseq))

if __name__ == "__main__":
	N, M = map(int, input().split())
	seq = list(map(int, input().split()))
	print("\n".join(" ".join(map(str, x)) for x in solution(seq, M)))

# (PyPy3) Result: 117284KB / 136ms