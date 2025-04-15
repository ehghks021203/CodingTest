# 28278. 스택 2
from sys import stdin, stdout

def solution(n: int):
	stack = []
	for _ in range(n):
		cmd = list(map(int, stdin.readline().split()))
		if cmd[0] == 1:
			stack.append(cmd[1])
		if cmd[0] == 2:
			stdout.write(f"{stack.pop() if len(stack) != 0 else -1}\n")
		if cmd[0] == 3:
			stdout.write(f"{len(stack)}\n")
		if cmd[0] == 4:
			stdout.write(f"{1 if len(stack) == 0 else 0}\n")
		if cmd[0] == 5:
			stdout.write(f"{stack[-1] if len(stack) != 0 else  -1}\n")

if __name__ == "__main__":
	N = int(stdin.readline())
	solution(N)

# (PyPy3) Result: 184220KB / 416ms