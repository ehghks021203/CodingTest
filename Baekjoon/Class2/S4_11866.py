# 11866. 요세푸스 문제 0

def solution(n: int, k: int) -> None:
	seq = list(range(1, n + 1))
	res = []
	current_idx = 0
	while True:
		current_idx = (current_idx + (k - 1)) % len(seq)
		res.append(seq[current_idx])
		seq.pop(current_idx)
		if len(seq) == 0:
			break
	print("<" + ", ".join(map(str,res)) + ">")

if __name__ == "__main__":
	N, K = map(int, input().split())
	solution(N, K)

# (PyPy3) Result: 108384KB / 88ms