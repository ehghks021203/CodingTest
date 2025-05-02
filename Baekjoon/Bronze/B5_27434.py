# 27434. 팩토리얼 3
import sys

sys.setrecursionlimit(10**6)

def solution(n: int) -> int:
	if n == 0: return 1
	return solution(n - 1) * n

if __name__ == "__main__":
	print(solution(int(input())))

# (PyPy3) Result: 1539956KB / 3052ms