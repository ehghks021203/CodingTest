# 11659. 구간 합 구하기 4

def solution(seq: list, m: int):
	# 누적 합 리스트
	prefix_sum = [0]
	for num in seq:
		prefix_sum.append(num + prefix_sum[-1])
	for _ in range(M):
		idx1, idx2 = map(int, input().split())
		print(prefix_sum[idx2] - prefix_sum[idx1 - 1])

if __name__ == "__main__":
	N, M = map(int, input().split())
	seq = list(map(int, input().split()))
	solution(seq, M)

# (PyPy3) Result: 127156KB / 2876ms