# 1018. 체스판 다시 칠하기

def solution(board: list) -> int:
	min_count = float("inf")
	row_size = len(board)
	col_size = len(board[0])
	if row_size == 8 and col_size == 8:
		white_start = black_start = 0
		for row_idx in range(len(board)):
			for col_idx in range(len(board[row_idx])):
				if board[row_idx][col_idx] == "W":
					if (row_idx + col_idx) % 2 == 0: black_start += 1
					else: white_start += 1
				else:
					if (row_idx + col_idx) % 2 == 0: white_start += 1
					else: black_start += 1
		return min(black_start, white_start)
	for row_start in range(row_size - 7):
		for col_start in range(col_size - 7):
			new_board = []
			for row in board[row_start: row_start + 8]:
				new_board.append(row[col_start:col_start + 8])
			min_count = min(solution(new_board), min_count)
	return min_count

if __name__ == "__main__":
	N, M = map(int, input().split())
	board = []
	[board.append(input()) for _ in range(N)]
	print(solution(board))

# (PyPy3) Result: 110964KB / 116ms