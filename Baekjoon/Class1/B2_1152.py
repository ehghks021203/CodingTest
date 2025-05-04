# 1152. 단어의 개수

def solution(string: str) -> int:
	string = string.strip()
	if string == "": return 0
	return len(string.split(" "))

if __name__  == "__main__":
	print(solution(input()))

# (PyPy3) Result: 129672KB / 120ms