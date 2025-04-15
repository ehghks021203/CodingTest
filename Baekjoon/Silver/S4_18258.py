# 18258. 큐 2
from sys import stdin, stdout
from collections import deque

def solution(n: int) -> None:
	queue = deque()
	for _ in range(n):
		cmd = list(map(str, stdin.readline().split()))
		if cmd[0] == "push":
			queue.append(int(cmd[1]))
		if cmd[0] == "pop":
			stdout.write(f"{queue.popleft() if len(queue) != 0 else -1}\n")
		if cmd[0] == "size":
			stdout.write(f"{len(queue)}\n")
		if cmd[0] == "empty":
			stdout.write(f"{0 if len(queue) != 0 else 1}\n")
		if cmd[0] == "front":
			stdout.write(f"{queue[0] if len(queue) != 0 else -1}\n")
		if cmd[0] == "back":
			stdout.write(f"{queue[-1] if len(queue) != 0 else -1}\n")

if __name__ == "__main__":
	N = int(stdin.readline())
	solution(N)

# (PyPy3) Result: 165020KB / 964ms