# 7576. 토마토
from collections import deque

class Tomato():
	def __init__(self, width: int, length: int, data: list):
		self.size = width * length
		self.graph = {}
		self.data = data
		for i in range(self.size):
			self.graph[i] = []
			if i % width != 0: self.graph[i].append(i - 1)
			if (i + 1) % width != 0: self.graph[i].append(i + 1)
			if i - width >= 0: self.graph[i].append(i - width)
			if i + width < self.size: self.graph[i].append(i + width)
	
	def is_exist(self, index: int) -> bool:
		return False if self.data[index] == -1 else True
	
	def is_ripen(self, index: int) -> bool:
		return False if self.data[index] == 0 else True

	def ripen(self, index: int) -> None:
		self.data[index] = 1
	
	def __len__(self):
		return self.size

def solution(tomato: Tomato) -> int:
	queue = deque()
	for idx in range(len(tomato)):
		if tomato.data[idx] == 1:
			queue.append((idx, 0))	# (idx, day)
	max_days = 0
	while queue:
		idx, day = queue.popleft()
		max_days = max(max_days, day)
		for neighbor in tomato.graph[idx]:
			if tomato.is_exist(neighbor) and not tomato.is_ripen(neighbor):
				tomato.ripen(neighbor)
				queue.append((neighbor, day + 1))
	for idx in range(len(tomato)):
		if not tomato.is_ripen(idx):
			return -1
	return max_days

if __name__ == "__main__":
	M, N = map(int, input().split())
	data = []
	[data.extend(list(map(int, input().split()))) for _ in range(N)]
	tomato = Tomato(M, N, data)
	print(solution(tomato))

# (PyPy3) Result: 303208KB / 1068ms