# 11478. 서로 다른 부분 문자열의 개수
from sys import stdin, stdout

def solution(string: str) -> int:
	str_set = set()
	string = string[:-1]
	for l in range(1, len(string) + 1):
		for i in range(0, len(string)):
			str_set.add(string[i:i+l])
	return len(str_set)

if __name__ == "__main__":
	S = stdin.readline()
	stdout.write(f"{solution(S)}\n")

# (PyPy3) Result: 309532KB / 780ms
# NOTE: Suffix Array & LCP Array를 사용하여 시간 단축 가능 (O(N^2) -> O(NlogN))