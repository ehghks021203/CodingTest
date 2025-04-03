# 10816. 숫자 카드 2

def solution(cards: list, targets: list) -> list:
	counts = {}
	result = []
	for card in cards:
		if not card in counts: counts[card] = 1
		else: counts[card] += 1
	for target in targets:
		if not target in counts: result.append(0)
		else: result.append(counts[target])
	return result

if __name__ == "__main__":
	N = int(input())
	cards = list(map(int, input().split()))
	M = int(input())
	targets = list(map(int, input().split()))
	print(" ".join(map(str, solution(cards, targets))))

# (PyPy3) Result: 260500KB / 460ms