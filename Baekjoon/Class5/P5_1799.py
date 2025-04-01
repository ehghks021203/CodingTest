# 1799. 비숍

def solution(board: list, check: dict, idx: int = 0, count: int = 0) -> int:
	max_count = 0
	if idx >= len(board):
		return max(max_count, count)
	x, y = board[idx]
	if not check["u"][x + y] and not check["d"][x - y + (N - 1)]:
		check["u"][x + y] = check["d"][x - y + (N - 1)] = True
		max_count = max(solution(board, check, idx + 1, count + 1), max_count)
		check["u"][x + y] = check["d"][x - y + (N - 1)] = False
	max_count = max(solution(board, check, idx + 1, count), max_count)
	return max_count

if __name__ == "__main__":
	N = int(input())
	board = [list(map(int, input().split())) for _ in range(N)]
	black_board, white_board = [], []
	for row in range(N):
		for col in range(N):
			if board[row][col] == 1:
				if (row + col) % 2 == 0:
					black_board.append((row, col))
				else:
					white_board.append((row, col))
	check = {
		"u": [False] * (2 * N - 1),
		"d": [False] * (2 * N - 1),
	}
	black_max = solution(black_board, check)
	white_max = solution(white_board, check)
	print(black_max + white_max)

# (PyPy3) Result: 117256KB / 516ms