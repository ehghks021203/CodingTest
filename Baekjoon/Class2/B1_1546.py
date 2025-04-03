# 1546. 평균

def solution(grades: list) -> float:
	new_grades = [grade / max(grades) * 100 for grade in grades]
	return sum(new_grades) / len(new_grades)

if __name__ == "__main__":
	N = int(input())
	print(solution(list(map(int, input().split()))))

# (PyPy3) Result: 109544KB / 92ms