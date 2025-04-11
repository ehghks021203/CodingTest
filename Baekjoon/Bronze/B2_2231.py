# 2231. 분해합
from sys import stdin, stdout

def solution(n: int) -> int:
	min_num = float("inf")
	for num in range(n, 0, -1):
		dsum = sum(map(int, list(str(num))))
		if num + dsum == n:
			min_num = min(num, min_num)
	# 생성자를 찾지 못했으면
	if min_num == float("inf"): return 0
	return min_num

if __name__ == "__main__":
	N = int(stdin.readline())
	stdout.write(f"{str(solution(N))}\n")

# (PyPy3) Result: 110736KB / 264ms