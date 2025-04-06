# 14940. 쉬운 최단거리
from collections import deque

class Map():
	def __init__(self, map_list: list):
		self.graph = {}
		self.data = map_list
		self.wall = []
		for y in range(len(self.data)):
			for x in range(len(self.data[y])):
				if self.data[y][x] == 2: self.start_point = (x, y)
				if self.data[y][x] == 0: self.wall.append((x, y))
				self.graph[(x, y)] = []
				# 상
				if y - 1 >= 0: 
					if self.data[y - 1][x] != 0: self.graph[(x, y)].append((x, y - 1))
				# 하
				if y + 1 < len(self.data): 
					if self.data[y + 1][x] != 0: self.graph[(x, y)].append((x, y + 1))
				# 좌
				if x - 1 >= 0: 
					if self.data[y][x - 1] != 0: self.graph[(x, y)].append((x - 1, y))
				# 우
				if x + 1 < len(self.data[y]): 
					if self.data[y][x + 1] != 0: self.graph[(x, y)].append((x + 1, y))
	
	def calc_distance(self) -> list:
		result = [[-1 for _ in range(len(self.data[0]))] for _ in range(len(self.data))]
		queue = deque([(*self.start_point, 0)])
		visited = set([self.start_point])
		while queue:
			x, y, step = queue.popleft()
			if result[y][x] == -1: result[y][x] = step
			for next in self.graph[(x, y)]:
				if next not in visited:
					queue.append((*next, step + 1))
					visited.add(next)
		for w in self.wall:
			x, y = w
			result[y][x] = 0
		return result

def solution(map_list: list) -> None:
	mymap = Map(map_list)
	print("\n".join(" ".join(map(str, x)) for x in mymap.calc_distance()))

if __name__ == "__main__":
	n, m = map(int, input().split())
	map_list = []
	graph = {}
	for _ in range(n): map_list.append(list(map(int, input().split())))
	solution(map_list)

# (PyPy3) Result: 231156KB / 728ms