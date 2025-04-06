# 27440. 1로 만들기 3
from sys import stdin, stdout
from collections import deque

def solution(n: int) -> int:
	queue = deque([(n, 0)])
	visited = set()
	while queue:
		cn, count = queue.popleft()
		if cn == 1: return count
		else:
			if cn not in visited:
				visited.add(cn)
				if cn % 3 == 0: queue.append((cn // 3, count + 1))
				if cn % 2 == 0: queue.append((cn // 2, count + 1))
				queue.append((cn - 1, count + 1))

if __name__ == "__main__":
	N = int(stdin.readline())
	stdout.write(str(solution(N)) + "\n")

# (PyPy3) Result: 114572KB / 128ms
# NOTE: 먼저 1에 도달하는 경로의 횟수가 가장 적으니 그냥 그거 반환해주면 됨. (다 순회할 필요 X)