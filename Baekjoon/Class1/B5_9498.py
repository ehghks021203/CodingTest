# 9498. 시험 성적

def solution(grade: int) -> str:
	if 90 <= grade <= 100:
		return "A"
	if 80 <= grade <= 89:
		return "B"
	if 70 <= grade <= 79:
		return "C"
	if 60 <= grade <= 69:
		return "D"
	return "F"

if __name__ == "__main__":
	print(solution(int(input())))

# (PyPy3) Result: 108384KB / 92ms