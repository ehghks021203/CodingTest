# 15725. 다항함수의 미분
import re

def solution(poly_str: str) -> int:
	terms = re.findall(r"[+-]?[^+-]+", poly_str)
	for term in terms:
		if "x" in term:
			coef = term.rstrip("x").lstrip("+")
			if coef in ["", "+"]:
				return 1
			elif coef == "-":
				return -1
			return int(coef)
	return 0

if __name__ == "__main__":
	poly_str = input()
	print(solution(poly_str))

# (PyPy3) Result: 112640KB / 148ms