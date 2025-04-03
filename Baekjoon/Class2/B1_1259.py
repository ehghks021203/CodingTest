# 1259. 팰린드롬수

def solution(n: int) -> bool:
	n = str(n)
	for idx in range(len(n) // 2):
		if n[idx] != n[len(n) - idx - 1]:
			return False
	return True

if __name__ == "__main__":
	while True:
		N = int(input())
		if N == 0: break
		print("yes") if solution(N) else print("no")

# (PyPy3) Result: 108384KB / 92ms