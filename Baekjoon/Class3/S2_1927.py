# 1927. 최소힙
from sys import stdin, stdout
from heapq import heappop, heappush

def solution(heap: list, x: int) -> None:
	if x == 0:
		try: stdout.write(str(heappop(heap)) + "\n")
		except: stdout.write("0\n")
	elif x > 0:
		heappush(heap, x)

if __name__ == "__main__":
	N = int(stdin.readline())
	heap = []
	for _ in range(N): solution(heap, int(stdin.readline()))

# (PyPy3) 114280KB / 164ms