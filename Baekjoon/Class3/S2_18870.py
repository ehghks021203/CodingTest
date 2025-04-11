# 18870. 좌표 압축

def solution(seq: list) -> list:
	comp_dict = {}
	res = []
	pn = float("inf")
	nn = 0
	for n in sorted(seq):
		if pn != n:
			comp_dict[n] = nn
			pn = n
			nn += 1
	for num in seq:
		res.append(comp_dict[num])
	return res

if __name__ == "__main__":
	N = int(input())
	seq = list(map(int, input().split()))
	print(" ".join(map(str, solution(seq))))

# (PyPy3) Result: 282724KB / 780ms