# 11279. 최대 힙
from sys import stdin, stdout
from heapq import heappush, heappop

def solution(n: int):
	heap = []
	for _ in range(n):
		x = int(stdin.readline())
		if x == 0:
			try: stdout.write(f"{heappop(heap)[1]}\n")
			except: stdout.write("0\n")
		else:
			heappush(heap, (-x, x))
		
if __name__ == "__main__":
	N = int(stdin.readline())
	solution(N)

# (PyPy3) Result: 117188KB / 168ms