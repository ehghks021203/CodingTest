# 8958. OX퀴즈

def solution(result: str) -> int:
	score = 0
	combo = 0
	for r in result:
		if r == "O": 
			score += 1 + combo
			combo += 1
		else:
			combo = 0
	return score

if __name__ == "__main__":
	TC = int(input())
	for _ in range(TC): print(solution(input()))

# (PyPy3) Result: 109544KB / 100ms