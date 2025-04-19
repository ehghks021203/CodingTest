# 2805. 나무 자르기
from sys import stdin, stdout

def solution(n: int, m: int, trees: list) -> int:
	low = 0
	high = max(trees)
	cut = 0
	while low <= high:
		mid = (low + high) // 2
		total = sum(max(0, tree - mid) for tree in trees)
		if total >= m: 
			cut = mid
			low = mid + 1
		else: high = mid - 1
	return cut

if __name__ == "__main__":
	N, M = map(int, stdin.readline().split())
	trees = list(map(int, stdin.readline().split()))
	stdout.write(str(solution(N, M, trees)) + "\n")

# (PyPy3) Result: 258360KB / 620ms