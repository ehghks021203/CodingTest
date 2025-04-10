# 1697. 숨바꼭질
from collections import deque

def solution(subin_x: int, sister_x: int) -> int:
	queue = deque([(subin_x, 0)])
	visited = set([subin_x])
	while queue:
		x, move_count = queue.popleft()
		if x == sister_x: return move_count
		for nx in [x - 1, x + 1, x * 2]:
			if nx > 100_000: continue
			if nx not in visited:
				visited.add(nx)
				queue.append((nx, move_count + 1))

if __name__ == "__main__":
	N, K = map(int, input().split())
	print(solution(N, K))

# (PyPy3) Result: 157680KB / 192ms