# 1269. 대칭 차집합
from sys import stdin, stdout

def solution(A: set, B: set) -> int:
	return len(A ^ B)

if __name__ == "__main__":
	An, Bn = map(int, stdin.readline().split())
	A = set(list(map(int, stdin.readline().split())))
	B = set(list(map(int, stdin.readline().split())))
	stdout.write(f"{solution(A, B)}\n")

# (PyPy3) Result: 209024KB / 276ms