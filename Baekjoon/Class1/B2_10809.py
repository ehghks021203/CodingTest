# 10809. 알파벳 찾기

def solution(word: str) -> list:
	alphabet = {}
	for c in range(ord("a"), ord("z") + 1): alphabet[chr(c)] = -1
	for idx in range(len(word)): alphabet[word[idx]] = idx if alphabet[word[idx]] == -1 else alphabet[word[idx]]
	return list(alphabet.values())

if __name__ == "__main__":
	print(" ".join(map(str, solution(input()))))

# (PyPy3) Result: 108384KB / 88ms