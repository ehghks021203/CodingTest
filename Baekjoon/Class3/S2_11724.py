# 11724. 연결 요소의 개수
from collections import deque

def solution(graph: dict) -> int:
	count = 0
	not_visited = set(graph.keys())
	queue = deque([1])
	not_visited.remove(1)
	while True:
		count += 1
		while queue:
			node = queue.popleft()
			for next in graph[node]:
				if next in not_visited:
					queue.append(next)
					not_visited.remove(next)
		if len(not_visited) != 0: 
			queue.append(not_visited.pop())
		else: 
			return count

if __name__ == "__main__":
	N, M = map(int, input().split())
	graph = {}
	for i in range(1, N + 1): graph[i] = []
	for _ in range(M): 
		u, v = map(int, input().split())
		graph[u].append(v)
		graph[v].append(u)
	print(solution(graph))

# (PyPy3) Result: 177404KB / 472ms
# NOTE: BFS의 경우 노드가 많아지면 느려지는데, **유니온-파인드** 방식을 사용하면 O(α(N))로, 거의 상수 급의 시간복잡도를 갖는다.