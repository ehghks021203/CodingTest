# 9012. 괄호

def solution(vps: str) -> bool:
	count = 0
	for c in vps:
		if c == "(": count += 1
		elif c == ")": count -= 1
		if count == -1: return False
	return True if count == 0 else False

if __name__ == "__main__":
	T = int(input())
	[print("YES" if solution(input()) else "NO") for _ in range(T)]

# (PyPy3) Result: 