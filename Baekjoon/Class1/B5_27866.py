# 27866. 문자와 문자열

def solution(word: str, idx: int) -> str:
	return word[idx - 1]

if __name__ == "__main__":
	word = input()
	idx = int(input())
	print(solution(word, idx))

# (PyPy3) Result: 108384KB / 92ms