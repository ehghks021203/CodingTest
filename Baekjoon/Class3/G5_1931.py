# 1931. 회의실 배정
from sys import stdin, stdout

def solution(conv: list) -> int:
	count = 1
	conv.sort(key=lambda x: (x[1], x[0]))
	curr_conv = conv[0]
	for idx in range(1, len(conv)):
		if curr_conv[1] <= conv[idx][0]:
			count += 1
			curr_conv = conv[idx]
	return count

if __name__ == "__main__":
	N = int(stdin.readline())
	conv_info = [list(map(int, stdin.readline().split())) for _ in range(N)]
	stdout.write(str(solution(conv_info)))

# (PyPy3) Result: 127168KB / 324ms