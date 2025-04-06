# 2606. 바이러스
from collections import deque

class Worm():
	def __init__(self, n: int):
		self.connection = {}
		for c in range(1, n + 1): self.connection[c] = set()

	def add_connection(self, origin: int, target: int) -> None:
		self.connection[origin].add(target)
		self.connection[target].add(origin)
	
	def check_connection(self, computer: int) -> list:
		return self.connection[computer]

	def count_infected_computers(self, computer: int):
		count = 0
		visited = set([computer])
		queue = deque([computer])
		while queue:
			com = queue.popleft()
			for neighbor in self.check_connection(com):
				if neighbor not in visited:
					queue.append(neighbor)
					visited.add(neighbor)
					count += 1
		return count

def solution(worm: Worm, computer: int) -> int:
	return worm.count_infected_computers(computer)

if __name__ == "__main__":
	N = int(input())
	worm = Worm(N)
	M = int(input())
	for _ in range(M): worm.add_connection(*map(int, input().split()))
	print(solution(worm, 1))

# (PyPy3) Result: 112308KB / 112ms