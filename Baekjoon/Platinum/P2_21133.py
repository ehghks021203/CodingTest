# 21133. N-Queen 2
import sys

def solution(n: int):
	board = []
	if n % 6 == 3:
		for i in range(4, n + 1, 2):
			board.append(i)
		board.append(2)
		for i in range(5, n + 1, 2):
			board.append(i)
		board.append(1)
		board.append(3)
	else:
		for i in range(2, n + 1, 2):
			board.append(i)
		if n % 6 == 2:
			board.append(3)
			board.append(1)
			for i in range(7, n + 1, 2):
				board.append(i)
			board.append(5)
		else:
			for i in range(1, n + 1, 2):
				board.append(i)
	return board

if __name__ == "__main__":
	N = int(sys.stdin.readline())
	sys.stdout.write("\n".join(map(str, solution(N))))

# (PyPy3) Result: 109544KB / 100ms