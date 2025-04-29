# 2577. 숫자의 개수

def solution(a: int, b: int, c: int) -> int:
	result = list(str(a * b * c))
	num_count = [0] * 10
	for r in result: num_count[int(r)] += 1
	return num_count

if __name__ == "__main__":
	A = int(input())
	B = int(input())
	C = int(input())
	print("\n".join(map(str, solution(A, B, C))))

# (PyPy3) Result: 108384KB / 88ms