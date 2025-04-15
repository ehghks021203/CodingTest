# 1181. 단어 정렬

def solution(words: list) -> list:
	return sorted(list(set(words)), key=lambda x: (len(x), x))

if __name__ == "__main__":
	N = int(input())
	words = []
	for _ in range(N): words.append(input())
	print("\n".join(solution(words)))

# (PyPy3) Result: 118028KB / 160ms