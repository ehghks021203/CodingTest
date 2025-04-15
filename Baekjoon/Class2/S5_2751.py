# 2751. 수 정렬하기 2

def solution(seq: list) -> list:
	return sorted(seq)

if __name__ == "__main__":
	N = int(input())
	seq = []
	for _ in range(N): seq.append(int(input()))
	print("\n".join(map(str, solution(seq))))
# (PyPy3) Result: 208384KB / 696ms