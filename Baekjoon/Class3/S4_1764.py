# 1764. 듣보잡

def solution(s: list, h: list) -> None:
	return set.intersection(s, h)

if __name__ == "__main__":
	N, M = map(int, input().split())
	s = set()
	h = set()
	for _ in range(N): s.add(input())
	for _ in range(M): h.add(input())
	sh = sorted(solution(s, h))
	print(len(sh))
	print("\n".join(sh))

# (PyPy3) Result: 121692KB / 188ms