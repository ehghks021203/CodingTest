# 11720. 숫자의 

def solution(seq: str) -> int:
	sum = 0
	for n in seq:
		sum += int(n)
	return sum

if __name__ == "__main__":
	N = int(input())
	seq = input()
	print(solution(seq))

# (PyPy3) Result: 108384KB / 96ms