# 11286. 절댓값 힙
from sys import stdin, stdout
from heapq import heappop, heappush, nsmallest

def solution(heap: list, x: int) -> None:
	if x == 0:
		try: stdout.write(str(heappop(heap)[1]) + "\n")
		except: stdout.write("0\n")
	elif x > 0: heappush(heap, (x, x))
	else: heappush(heap, (-x - 0.5, x))

if __name__ == "__main__":
	N = int(stdin.readline())
	heap = []
	for _ in range(N): solution(heap, int(stdin.readline()))

# (PyPy3) 119920KB / 300ms