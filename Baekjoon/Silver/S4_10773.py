# 10773. 제로
from sys import stdin, stdout

def solution(k: int) -> int:
	stack = []
	for _ in range(k):
		num = int(stdin.readline())
		if num == 0:
			if len(stack) != 0: stack.pop()
		else:
			stack.append(num)
	return sum(stack)

if __name__ == "__main__":
	K = int(stdin.readline())
	stdout.write(f"{solution(K)}\n")

# (PyPy3) Result: 114588KB / 108ms