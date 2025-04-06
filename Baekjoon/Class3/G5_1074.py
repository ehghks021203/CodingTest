# 1074. Z

def solution(n: int, r: int, c: int, count: int = 0) -> int:
	if n == 1:
		if r % 2 == 0 and c % 2 == 0: return count
		if r % 2 == 0 and c % 2 == 1: return count + 1
		if r % 2 == 1 and c % 2 == 0: return count + 2
		if r % 2 == 1 and c % 2 == 1: return count + 3
	else:
		if r < 2 ** n // 2 and c < 2 ** n // 2: return solution(n - 1, r, c, count)
		if r < 2 ** n // 2 and not c < 2 ** n // 2: return solution(n - 1, r, c - 2 ** n // 2, count + (2 ** n // 2) ** 2)
		if not r < 2 ** n // 2 and c < 2 ** n // 2: return solution(n - 1, r - 2 ** n // 2, c, count + ((2 ** n // 2) ** 2) * 2)
		if not r < 2 ** n // 2 and not c < 2 ** n // 2: return solution(n - 1, r - 2 ** n // 2, c - 2 ** n // 2, count + ((2 ** n // 2) ** 2) * 3)

if __name__ == "__main__":
	N, r, c = map(int, input().split())
	print(solution(N, r, c))

# (PyPy3) Result: 108384KB / 88ms