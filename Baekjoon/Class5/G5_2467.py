# 2467. 용액

def solution(s: list) -> tuple:
	minimum = float("inf")
	left = 0
	right = len(s) - 1
	while left < right:
		if minimum > abs(s[left] + s[right]):
			minimum = abs(s[left] + s[right])
			sol = (s[left], s[right])
		if abs(s[left]) < abs(s[right]): right -= 1
		else: left += 1
	return sol

if __name__ == "__main__":
	N = int(input())
	S = list(map(int, input().split()))
	print(" ".join(map(str, solution(S))))

# (PyPy3) Result: 124112KB / 124ms
# NOTE: 여기서는 두 포인터를 사용해 풀었지만, 이분 탐색으로도 해결 가능