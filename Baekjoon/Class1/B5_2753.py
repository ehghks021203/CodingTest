# 2753. 윤년

def solution(year: int) -> bool:
	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
		return True
	return False

if __name__ == "__main__":
	print("1" if solution(int(input())) else "0")

# (PyPy3) Result: 108384KB / 88ms